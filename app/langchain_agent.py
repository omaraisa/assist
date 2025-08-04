import logging
import json
import ast
from typing import Dict, List, Any

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import Tool
from langchain_core.messages import AIMessage, HumanMessage

from .spatial_functions import SpatialFunctions
from .config import settings

logger = logging.getLogger(__name__)

class LangChainAgent:
    """Agent that uses LangChain to interact with AI models."""

    def __init__(self, model_key: str):
        self.spatial_functions = SpatialFunctions()
        self.tools = self._get_tools()
        self.set_model(model_key)

    def _get_tools(self) -> List[Tool]:
        """Gets the tools for the LangChain agent."""
        tools = []
        for func_id, func_name in self.spatial_functions.AVAILABLE_FUNCTIONS.items():
            declaration = self.spatial_functions.get_functions_declaration([func_id])
            description = declaration.get(func_name, {}).get('description', '')

            # Create a wrapper function to handle tools that take no arguments
            def _tool_wrapper(tool_func, *args, **kwargs):
                logger.info(f"Calling tool: {tool_func.__name__} with args: {args} and kwargs: {kwargs}")
                if tool_func.__name__ in ["get_map_layers_info", "get_map_tables_info", "get_current_project_path", "get_default_db_path"]:
                    return tool_func()
                
                # Handle args passed as a single dictionary or a JSON string
                if args:
                    tool_input = args[0]
                    if isinstance(tool_input, str):
                        try:
                            tool_input = ast.literal_eval(tool_input)
                        except (ValueError, SyntaxError):
                            # Not a literal dict, proceed with original args
                            pass
                    
                    if isinstance(tool_input, dict):
                        # Pass the dictionary as keyword arguments
                        return tool_func(**tool_input)

                # Fallback to the original call
                return tool_func(*args, **kwargs)

            tools.append(
                Tool(
                    name=func_name,
                    func=lambda *args, tool_func=getattr(self.spatial_functions, func_name), **kwargs: _tool_wrapper(tool_func, *args, **kwargs),
                    description=description
                )
            )
        return tools

    def set_model(self, model_key: str):
        """Sets the AI model for the agent."""
        from .config import get_model_config
        self.model_key = model_key
        model_config = get_model_config(model_key)
        self.llm = ChatGoogleGenerativeAI(
            model=model_config["model"],
            google_api_key=model_config["api_key"],
            temperature=model_config["temperature"],
            max_output_tokens=model_config["max_tokens"],
        )
        self.prompt = self._create_prompt_template()
        self.agent = create_react_agent(self.llm, self.tools, self.prompt)
        self.agent_executor = AgentExecutor(agent=self.agent, tools=self.tools, verbose=True, handle_parsing_errors=True)
        logger.info(f"LangChain agent model set to: {self.model_key}")

    def _create_prompt_template(self) -> PromptTemplate:
        """Creates the prompt template for the agent."""
        template = """
        You are a helpful AI assistant.
        You have access to the following tools:
        {tools}

        Use the following format:

        Question: the input question you must answer
        Thought: you should always think about what to do
        Action: the action to take, should be one of [{tool_names}]
        Action Input: the input to the action, as a dictionary where keys are the parameter names.
        Observation: the result of the action
        ... (this Thought/Action/Action Input/Observation can repeat N times)
        Thought: I now know the final answer
        Final Answer: the final answer to the original input question

        Begin!

        Question: {input}
        Thought:{agent_scratchpad}
        """
        return PromptTemplate(template=template, input_variables=["tools", "tool_names", "input", "agent_scratchpad"])

    async def generate_response(
        self,
        user_message: str,
        conversation_history: List[Dict],
        arcgis_state: Dict,
        client_id: str = None
    ) -> Dict[str, Any]:
        """Generates a response using the LangChain agent."""
        logger.info(f"LangChain agent generating response for: {user_message[:100]}...")

        try:
            history_messages = []
            for msg in conversation_history:
                if msg.get("role") == "user":
                    history_messages.append(HumanMessage(content=msg.get("content")))
                elif msg.get("role") == "assistant":
                    history_messages.append(AIMessage(content=msg.get("content")))

            response = await self.agent_executor.ainvoke({
                "input": user_message,
                "chat_history": history_messages
            })

            return response
        except Exception as e:
            logger.error(f"Error generating LangChain agent response: {e}", exc_info=True)
            return {
                "type": "error",
                "content": f"Error in LangChain Agent: {e}",
                "model": self.model_key
            }