from langchain_core.callbacks.base import BaseCallbackHandler

# Custom callback to log all agent intermediate steps (thoughts, actions, etc.)
class LoggingCallbackHandler(BaseCallbackHandler):
    def __init__(self, logger):
        self.logger = logger

    def on_chain_start(self, serialized, inputs, **kwargs):
        self.logger.info(f"[Agent Start] Inputs: {inputs}")

    def on_chain_end(self, outputs, **kwargs):
        self.logger.info(f"[Agent End] Outputs: {outputs}")

    def on_tool_start(self, serialized, input_str, **kwargs):
        self.logger.info(f"[Tool Start] Input: {input_str}")

    def on_tool_end(self, output, **kwargs):
        self.logger.info(f"[Tool End] Output: {output}")

    def on_text(self, text, **kwargs):
        # This is called for every intermediate step (thought, action, observation, etc.)
        self.logger.info(f"[Agent Step] {text}")

    def on_agent_action(self, action, **kwargs):
        self.logger.info(f"[Agent Action] {action}")

    def on_agent_finish(self, finish, **kwargs):
        self.logger.info(f"[Agent Finish] {finish}")
import logging
import json
import ast
from typing import Dict, List, Any

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import Tool
from langchain_core.messages import AIMessage, HumanMessage

from .config import settings

logger = logging.getLogger(__name__)

class LangChainAgent:
    """Agent that uses LangChain to interact with AI models."""

    def __init__(self, model_key: str, websocket_manager: Any):
        self.websocket_manager = websocket_manager
        self.tools = self._get_tools()
        # Add callback handler for logging all agent steps
        self.callback_handler = LoggingCallbackHandler(logger)
        # Track the current client id for function calls so we can set source_client
        self._current_request_client_id = None
        self.set_model(model_key)

    def _get_tools(self) -> List[Tool]:
        """Gets the tools for the LangChain agent."""
        return [
            Tool(
                name="execute_arcpy_tool",
                func=self._execute_arcpy_tool,
                description="Executes any ArcGIS Pro geoprocessing tool. The input must be a stringified dictionary containing 'tool_name' (e.g., 'Buffer_analysis') and 'parameters' (a dictionary of the tool's arguments).",
            ),
        ]

    def _execute_arcpy_tool(self, tool_input_str: str, session_id_for_test: str = None) -> Dict[str, Any]:
        """
        Parses the input string from the agent and sends the tool execution request to ArcGIS Pro via websocket.
        Waits for and returns the actual tool response from ArcGIS Pro.
        The input string should be a dictionary containing 'tool_name' and 'parameters'.
        """
        tool_name = "[unknown]"
        try:
            # The agent can sometimes pass a string that needs to be evaluated twice
            try:
                temp_input = ast.literal_eval(tool_input_str)
                if isinstance(temp_input, str):
                    tool_input = ast.literal_eval(temp_input)
                else:
                    tool_input = temp_input
            except (ValueError, SyntaxError):
                 # Fallback for when the input is already a dict (e.g. from tests)
                 if isinstance(tool_input_str, dict):
                     tool_input = tool_input_str
                 else:
                    raise

            if not isinstance(tool_input, dict):
                return {"error": f"Parsed input is not a dictionary. Got type: {type(tool_input)}"}

            tool_name = tool_input.get("tool_name")
            parameters = tool_input.get("parameters")

            if not tool_name or not isinstance(parameters, dict):
                return {"error": "'tool_name' (string) and 'parameters' (dict) must be provided in the input."}

            # Send function request to ArcGIS Pro via websocket and wait for response
            arcgis_client = self.websocket_manager.get_arcgis_client()
            if not arcgis_client:
                return {"error": "ArcGIS Pro client not connected."}

            # Generate unique session ID for this function call
            session_id = session_id_for_test
            if session_id is None:
                import uuid
                session_id = str(uuid.uuid4())

            payload = {
                "type": "execute_tool", # Use a more generic type name
                "tool_name": tool_name,
                "parameters": parameters,
                "session_id": session_id,
                "source_client": self._current_request_client_id
            }
            
            import asyncio
            
            # Use asyncio.run to execute the async function from a sync context
            asyncio.run(self.websocket_manager.send_to_client(arcgis_client, payload))
            
            # Wait for the result from ArcGIS Pro
            max_wait_time = 60  # Increased timeout for potentially long-running tools
            check_interval = 0.2
            elapsed_time = 0
            
            while elapsed_time < max_wait_time:
                if self.websocket_manager.has_function_result(session_id):
                    result = self.websocket_manager.get_function_result(session_id)
                    # The result from Pro will be a JSON string, which needs to be parsed
                    if result:
                         # The final result could be wrapped in 'data' from the old format
                        if isinstance(result, dict) and 'data' in result:
                            return result['data']
                        return result
                
                import time
                time.sleep(check_interval)
                elapsed_time += check_interval
            
            return {"error": f"Timeout waiting for response from ArcGIS Pro for tool '{tool_name}'. The tool may be running, or ArcGIS Pro may be unresponsive."}

        except (SyntaxError, ValueError) as e:
            return {"error": f"Failed to parse input string: {e}. Input was: {tool_input_str}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred while preparing to execute '{tool_name}': {e}"}

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
        # Pass the callback handler to the agent executor
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True,
            handle_parsing_errors=True,
            callbacks=[self.callback_handler]
        )
        logger.info(f"LangChain agent model set to: {self.model_key}")

    def _create_prompt_template(self) -> PromptTemplate:
        """Creates the prompt template for the agent, now including chat history."""
        template = """
        You are an expert GIS Analyst and your goal is to help users by executing ArcGIS Pro geoprocessing tools.

        You have access to the following tool:
        {tools}

        Here is the current state of the ArcGIS Pro project, which includes a list of available layers:
        {arcgis_state}

        **Instructions:**
        1.  Analyze the user's request to identify the appropriate ArcGIS Pro geoprocessing tool. For example, if the user asks to "make a buffer", you should use the `Buffer_analysis` tool.
        2.  Based on the user's request and the available layers from `arcgis_state`, determine the parameters for the tool.
        3.  If the user's request is ambiguous or missing necessary information (e.g., they ask to create a buffer but don't specify a layer or distance), you MUST ask for clarification. Do not attempt to execute a tool with incomplete information. To ask a clarifying question, provide your question as the `Final Answer`.
        4.  Use the `execute_arcpy_tool` to run the tool. The input for this tool is a JSON object with two keys: "tool_name" and "parameters".
        5.  The tool name must be the correct, full name of an `arcpy` tool (e.g., `Buffer_analysis`, `SpatialJoin_analysis`, `Clip_analysis`).
        6.  The `parameters` must be a dictionary where keys are the parameter names and values are the corresponding values.

        **Example Workflow 1: Executing a tool**
        Question: Create a 500 meter buffer around the 'cities' layer and call it 'cities_buffer'.
        Thought: The user wants to create a buffer. The `arcpy` tool for this is `Buffer_analysis`. I have all the required parameters: the input layer ('cities'), the distance ('500 meters'), and the output name ('cities_buffer'). I can now call the `execute_arcpy_tool`.
        Action: execute_arcpy_tool
        Action Input: {{"tool_name": "Buffer_analysis", "parameters": {{"in_features": "cities", "out_feature_class": "cities_buffer", "buffer_distance_or_field": "500 Meters"}}}}
        Observation: {{"status": "success", "data": {{"message": "Tool 'Buffer_analysis' executed successfully.", "output_path": "C:\\Users\\...\\pro_project.gdb\\cities_buffer"}}}}
        Thought: The tool executed successfully and the buffer was created. I will now inform the user.
        Final Answer: The 500-meter buffer for the 'cities' layer has been created successfully and saved as 'cities_buffer'. It has been added to your map.

        **Example Workflow 2: Asking a clarifying question**
        Question: Can you make a buffer for the roads?
        Thought: The user wants to create a buffer for the 'roads' layer. However, they have not specified a buffer distance or an output name. I need to ask for this information.
        Final Answer: I can create a buffer for the 'roads' layer, but I need a bit more information. What distance should the buffer be (e.g., 500 meters, 1 mile), and what would you like to name the new output layer?

        **Important:**
        - Do NOT use markdown formatting, code blocks, or triple backticks (```) in your final answers.
        - The `arcgis_state` provides the names of layers you can use as input for tools.

        Use the following format for your thought process:

        Question: the input question you must answer
        Thought: your reasoning and plan
        Action: the action to take, should be one of [{tool_names}]
        Action Input: the input to the action
        Observation: the result of the action
        ... (this Thought/Action/Action Input/Observation can repeat N times)
        Thought: I now know the final answer
        Final Answer: the final answer to the original input question

        Begin!

        Conversation so far:
        {chat_history}

        Question: {input}
        Thought:{agent_scratchpad}
        """
        return PromptTemplate(template=template, input_variables=["tools", "tool_names", "input", "agent_scratchpad", "arcgis_state", "chat_history"])

    async def generate_response(
        self,
        user_message: str,
        conversation_history: List[Dict],
        arcgis_state: Dict,
        client_id: str = None
    ) -> Dict[str, Any]:
        """Generates a response using the LangChain agent, now including chat history as plain text."""
        logger.info(f"LangChain agent generating response for: {user_message[:100]}...")

        try:
            # Only include user and assistant (final answer) messages in history
            chat_history_lines = []
            for msg in conversation_history:
                if msg.get("role") == "user":
                    chat_history_lines.append(f"User: {msg.get('content','')}")
                elif msg.get("role") == "assistant":
                    chat_history_lines.append(f"Assistant: {msg.get('content','')}")
            chat_history_str = "\n".join(chat_history_lines)

            # Record the client id so tools can set source_client
            self._current_request_client_id = client_id

            response = await self.agent_executor.ainvoke({
                "input": user_message,
                "arcgis_state": json.dumps(arcgis_state, indent=2),
                "chat_history": chat_history_str
            })

            # Clear after invocation
            self._current_request_client_id = None

            return response
        except Exception as e:
            logger.error(f"Error generating LangChain agent response: {e}", exc_info=True)
            
            # Check if this is a quota exceeded error
            error_message = str(e).lower()
            if "quota" in error_message and "exceeded" in error_message:
                return {
                    "output": "🚫 **API Quota Exceeded**\n\nYou have reached your daily quota limit for the Gemini API. Please wait until tomorrow when your quota resets or switch to a different AI model.",
                }
            elif "429" in error_message or "rate limit" in error_message:
                return {
                    "output": "⏱️ **Rate Limit Reached**\n\nYou're sending requests too quickly. Please wait 30-60 seconds and try again.",
                }
            else:
                return {
                    "output": f"Error: {e}",
                }