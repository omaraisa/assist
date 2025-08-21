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
        # Add callback handler for logging all agent steps
        self.callback_handler = LoggingCallbackHandler(logger)
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
                description="Executes a spatial function. Input must be a stringified dictionary with 'function_name' and parameters. Parameters can be provided either as top-level keys or inside an 'arguments' object.",
            ),
        ]


    def _execute_spatial_function(self, tool_input_str: str) -> Dict[str, Any]:
        """
        Parses the input string from the agent and sends the function request to ArcGIS Pro via websocket.
        Waits for and returns the actual function response from ArcGIS Pro.
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

            # Send function request to ArcGIS Pro via websocket and wait for response
            arcgis_client = self.spatial_functions.websocket_manager.get_arcgis_client()
            if not arcgis_client:
                return {"error": "ArcGIS Pro client not connected."}

            # Generate unique session ID for this function call
            import uuid
            session_id = str(uuid.uuid4())

            # Unwrap nested 'arguments' if present to avoid passing unexpected keyword 'arguments'
            parameters = tool_input
            if isinstance(parameters, dict) and "arguments" in parameters and len(parameters) == 1 and isinstance(parameters["arguments"], dict):
                parameters = parameters["arguments"]

            payload = {
                "type": "execute_function",
                "function_name": function_name,
                "parameters": parameters,
                "session_id": session_id  # Add session ID to track this specific call
            }
            
            import asyncio
            
            # Send the request
            asyncio.run(self.spatial_functions.websocket_manager.send_to_client(arcgis_client, payload))
            
            # Wait for the response with timeout
            max_wait_time = 30  # Maximum 30 seconds wait
            check_interval = 0.2  # Check every 200ms
            elapsed_time = 0
            
            while elapsed_time < max_wait_time:
                if self.spatial_functions.websocket_manager.has_function_result(session_id):
                    result = self.spatial_functions.websocket_manager.get_function_result(session_id)
                    if result:
                        # Return the actual function result from ArcGIS Pro
                        return result.get("data", result)
                
                # Sleep and increment elapsed time
                import time
                time.sleep(check_interval)
                elapsed_time += check_interval
            
            # Timeout reached
            return {"error": f"Timeout waiting for response from ArcGIS Pro for function '{function_name}'. Please check if ArcGIS Pro is responsive."}

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
        You are a helpful AI assistant for ArcGIS Pro.

        Conversation so far:
        {chat_history}

        You have access to the following tools:
        {tools}

        Here is the current state of the ArcGIS Pro project:
        {arcgis_state}

        Here is a list of available functions you can use:
        {available_functions}

        To use a function, you must first get its declaration using the `get_functions_declaration` tool with the function's ID.
        The declaration will be returned as a string, describing the function, its parameters, and their types.
        Once you have the declaration, you can execute the function using the `execute_spatial_function` tool.

        IMPORTANT: Do NOT use markdown formatting, code blocks, or triple backticks (```) in your responses. Provide plain text answers only.

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
        return PromptTemplate(template=template, input_variables=["tools", "tool_names", "input", "agent_scratchpad", "arcgis_state", "available_functions", "chat_history"])

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
                    chat_history_lines.append(f"Progent: {msg.get('content','')}")
            chat_history_str = "\n".join(chat_history_lines)

            response = await self.agent_executor.ainvoke({
                "input": user_message,
                "arcgis_state": json.dumps(arcgis_state, indent=2),
                "available_functions": json.dumps(self.spatial_functions.AVAILABLE_FUNCTIONS, indent=2),
                "chat_history": chat_history_str
            })

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