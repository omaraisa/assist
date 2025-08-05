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
from .ai.function_declarations import FunctionDeclaration

logger = logging.getLogger(__name__)

def _get_declarations_stateless(function_ids_str: str) -> str:
    """
    A stateless helper to get function declarations.
    It imports and accesses the necessary data directly to avoid state issues.
    """
    try:
        # Access the class variables directly without creating an instance
        available_functions = SpatialFunctions.AVAILABLE_FUNCTIONS
        functions_declaration = FunctionDeclaration.functions_declarations
        
        # Parse the input - handle multiple formats: single int, single string, array of ints, array of strings
        function_ids = []
        
        if isinstance(function_ids_str, str):
            cleaned_input = function_ids_str.strip().strip('"').strip("'")
            
            # Try to parse as JSON array first (e.g., "[4]", '["4"]', "[4,5]")
            try:
                parsed = ast.literal_eval(cleaned_input)
                if isinstance(parsed, list):
                    # Convert all elements to integers
                    function_ids = [int(x) for x in parsed]
                else:
                    # Single value
                    function_ids = [int(parsed)]
            except (ValueError, SyntaxError):
                # If JSON parsing fails, try as single value
                try:
                    function_ids = [int(cleaned_input)]
                except ValueError:
                    return f"Error: Could not parse function IDs from input: {function_ids_str}"
        else:
            # Direct input (shouldn't happen, but handle it)
            if isinstance(function_ids_str, list):
                function_ids = [int(x) for x in function_ids_str]
            else:
                function_ids = [int(function_ids_str)]
        
        result = {}
        for func_id in function_ids:
            if func_id in available_functions:
                func_name = available_functions[func_id]
                if func_name in functions_declaration:
                    result[func_name] = functions_declaration[func_name]
        
        # Format the result into a string
        if not result:
            return "No function declarations found for the given IDs."

        output = []
        for func_name, details in result.items():
            output.append(f"Function: {func_name}")
            output.append(f"  Description: {details.get('description', 'N/A')}")
            output.append("  Parameters:")
            params = details.get("parameters", {})
            if not params:
                output.append("    - None")
                continue
            required_params = details.get("required", [])
            for param_name, param_details in params.items():
                param_type = param_details.get('type', 'any')
                is_required = "required" if param_name in required_params else "optional"
                default_info = f", default: {param_details['default']}" if 'default' in param_details else ""
                output.append(f"    - {param_name} ({param_type}, {is_required}{default_info}): {param_details.get('description', '')}")
        return "\n".join(output)

    except Exception as e:
        logger.error(f"Error in _get_declarations_stateless: {e}")
        return f"Error getting function declaration: {e}"

class LangChainAgent:
    """Agent that uses LangChain to interact with AI models."""

    def __init__(self, model_key: str, websocket_manager: Any):
        self.spatial_functions = SpatialFunctions(websocket_manager)
        self.tools = self._get_tools()
        self.set_model(model_key)

    def _get_tools(self) -> List[Tool]:
        """Gets the tools for the LangChain agent."""
        return [
            Tool(
                name="get_functions_declaration",
                func=_get_declarations_stateless,
                description="Gets the function declaration for one or more functions. Input must be a string representing a list of integers (e.g., '[8]' or '[1, 2, 3]').",
            ),
            Tool(
                name="execute_spatial_function",
                func=self._execute_spatial_function,
                description="Executes a spatial function. Input must be a string representing a dictionary with 'function_name' and its arguments.",
            ),
        ]


    def _execute_spatial_function(self, tool_input_str: str) -> Dict[str, Any]:
        """
        Parses the input string from the agent and sends the function request to ArcGIS Pro via websocket.
        The input string should be a dictionary containing 'function_name' and its arguments.
        """
        function_name = "[unknown]"
        try:
            # The agent can sometimes wrap its output in an extra layer of quotes.
            # We parse it twice to be safe.
            temp_input = ast.literal_eval(tool_input_str)
            if isinstance(temp_input, str):
                tool_input = ast.literal_eval(temp_input)
            else:
                tool_input = temp_input

            if not isinstance(tool_input, dict):
                return {"error": f"Parsed input is not a dictionary. Got type: {type(tool_input)}"}

            function_name = tool_input.pop("function_name", None)
            if not function_name:
                return {"error": "'function_name' must be provided in the input dictionary."}

            # Check if function exists in available functions
            if function_name not in SpatialFunctions.AVAILABLE_FUNCTIONS.values():
                return {"error": f"Function '{function_name}' is not available."}

            # Send function request to ArcGIS Pro via websocket (same as web interface)
            arcgis_client = self.spatial_functions.websocket_manager.get_arcgis_client()
            if not arcgis_client:
                return {"error": "ArcGIS Pro client not connected."}

            payload = {
                "type": "execute_function",
                "function_name": function_name,
                "parameters": tool_input
            }
            
            import asyncio
            asyncio.run(self.spatial_functions.websocket_manager.send_to_client(arcgis_client, payload))
            return {"success": True, "message": f"Function '{function_name}' sent to ArcGIS Pro for execution."}

        except (SyntaxError, ValueError) as e:
            return {"error": f"Failed to parse input string: {e}. Input was: {tool_input_str}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred while executing '{function_name}': {e}"}

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
        You are a helpful AI assistant for ArcGIS Pro.

        You have access to the following tools:
        {tools}

        Here is the current state of the ArcGIS Pro project:
        {arcgis_state}

        Here is a list of available functions you can use:
        {available_functions}

        To use a function, you must first get its declaration using the `get_functions_declaration` tool with the function's ID.
        The declaration will be returned as a string, describing the function, its parameters, and their types.
        Once you have the declaration, you can execute the function using the `execute_spatial_function` tool.

        Use the following format:

        Question: the input question you must answer
        Thought: you should always think about what to do
        Action: the action to take, should be one of [{tool_names}]
        Action Input: the input to the action
        Observation: the result of the action
        ... (this Thought/Action/Action Input/Observation can repeat N times)
        Thought: I now know the final answer
        Final Answer: the final answer to the original input question

        Begin!

        Question: {input}
        Thought:{agent_scratchpad}
        """
        return PromptTemplate(template=template, input_variables=["tools", "tool_names", "input", "agent_scratchpad", "arcgis_state", "available_functions"])

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
                "chat_history": history_messages,
                "arcgis_state": json.dumps(arcgis_state, indent=2),
                "available_functions": json.dumps(self.spatial_functions.AVAILABLE_FUNCTIONS, indent=2)
            })

            return response
        except Exception as e:
            logger.error(f"Error generating LangChain agent response: {e}", exc_info=True)
            return {
                "type": "error",
                "content": f"Error in LangChain Agent: {e}",
                "model": self.model_key
            }