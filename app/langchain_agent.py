try:
    from langchain_core.callbacks.base import BaseCallbackHandler
except Exception:
    # Minimal fallback so module can be imported when LangChain is not installed.
    class BaseCallbackHandler:
        def __init__(self, *args, **kwargs):
            pass

        def on_chain_start(self, *args, **kwargs):
            return None

        def on_chain_end(self, *args, **kwargs):
            return None

        def on_tool_start(self, *args, **kwargs):
            return None

        def on_tool_end(self, *args, **kwargs):
            return None

        def on_text(self, *args, **kwargs):
            return None

        def on_agent_action(self, *args, **kwargs):
            return None

        def on_agent_finish(self, *args, **kwargs):
            return None


# Custom callback to log all agent intermediate steps (thoughts, actions, etc.)
class LoggingCallbackHandler(BaseCallbackHandler):
    def __init__(self, logger):
        super().__init__()
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
        # This is called for every intermediate step (thought, action, etc.)
        self.logger.info(f"[Agent Step] {text}")

    def on_agent_action(self, action, **kwargs):
        self.logger.info(f"[Agent Action] {action}")

    def on_agent_finish(self, finish, **kwargs):
        self.logger.info(f"[Agent Finish] {finish}")
import logging
import json
import ast
import uuid
import asyncio
from typing import Dict, List, Any

try:
    from langchain_core.prompts import PromptTemplate
except Exception:
    # Minimal PromptTemplate fallback
    class PromptTemplate:
        def __init__(self, template: str, input_variables: list):
            self.template = template
            self.input_variables = input_variables

try:
    from langchain.agents import create_react_agent, AgentExecutor
except Exception:
    def create_react_agent(llm, tools, prompt):
        raise RuntimeError("LangChain agents not available in this environment")

    class AgentExecutor:
        def __init__(self, *args, **kwargs):
            raise RuntimeError("LangChain AgentExecutor not available in this environment")

try:
    from langchain.tools import Tool, BaseTool
except Exception:
    class Tool:
        def __init__(self, name: str, func, description: str = ""):
            self.name = name
            self.func = func
            self.description = description

    class BaseTool:
        name = "base_tool"
        description = "Base fallback tool"

class ExecuteSpatialFunctionTool(BaseTool):
    name: str = "execute_spatial_function"
    description: str = (
        "Executes a spatial function. Input must be a stringified dictionary with 'function_name' "
        "and parameters. Parameters can be provided either as top-level keys or inside an 'arguments' object."
    )
    websocket_manager: Any
    client_id: str

    def _run(self, tool_input_str: str) -> Dict[str, Any]:
        function_name = "[unknown]"
        try:
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

            # Extract parameters (remaining tool_input after removing function_name)
            parameters = tool_input

            # Handle dashboard functions locally (server-side)
            dashboard_functions = [
                "generate_smart_dashboard_layout",
                "get_current_dashboard_layout", 
                "get_current_dashboard_charts",
                "get_field_stories_and_samples",
                "update_dashboard_charts"
            ]
            
            if function_name in dashboard_functions:
                return self._execute_dashboard_function(function_name, parameters)

            arcgis_client = self.websocket_manager.get_arcgis_client()
            if not arcgis_client:
                return {"error": "ArcGIS Pro client not connected."}

            if isinstance(parameters, dict) and "arguments" in parameters and len(parameters) == 1 and isinstance(parameters["arguments"], dict):
                parameters = parameters["arguments"]

            session_id = str(uuid.uuid4())
            payload = {
                "type": "execute_function",
                "function_name": function_name,
                "parameters": parameters,
                "session_id": session_id,
                "source_client": self.client_id
            }
            
            asyncio.run(self.websocket_manager.send_to_client(arcgis_client, payload))
            
            max_wait_time = 120
            check_interval = 0.2
            elapsed_time = 0
            
            while elapsed_time < max_wait_time:
                if self.websocket_manager.has_function_result(session_id):
                    result = self.websocket_manager.get_function_result(session_id)
                    if result:
                        return result.get("data", result)
                
                import time
                time.sleep(check_interval)
                elapsed_time += check_interval
            
            return {"error": f"Timeout waiting for response from ArcGIS Pro for function '{function_name}'."}

        except (SyntaxError, ValueError) as e:
            return {"error": f"Failed to parse input string: {e}. Input was: {tool_input_str}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred while executing '{function_name}': {e}"}

    def _execute_dashboard_function(self, function_name: str, parameters: dict) -> dict:
        """Execute dashboard functions locally on the server side"""
        try:
            if function_name == "generate_smart_dashboard_layout":
                # For generate_smart_dashboard_layout, we need to get field insights first
                layer_name = parameters.get("layer_name")
                analysis_type = parameters.get("analysis_type", "overview")
                theme = parameters.get("theme", "default")
                field_insights = parameters.get("field_insights")
                
                if not field_insights:
                    # Get field insights from ArcGIS Pro first
                    arcgis_client = self.websocket_manager.get_arcgis_client()
                    if not arcgis_client:
                        return {"error": "ArcGIS Pro client not connected for field analysis."}
                    
                    analysis_payload = {
                        "type": "execute_function",
                        "function_name": "analyze_layer_fields",
                        "parameters": {"layer": layer_name},
                        "session_id": str(uuid.uuid4()),
                        "source_client": self.client_id
                    }
                    asyncio.run(self.websocket_manager.send_to_client(arcgis_client, analysis_payload))

                    max_wait_time = 120
                    check_interval = 0.2
                    elapsed_time = 0

                    while elapsed_time < max_wait_time:
                        if self.websocket_manager.has_function_result(analysis_payload['session_id']):
                            result = self.websocket_manager.get_function_result(analysis_payload['session_id'])
                            if result and result.get("data", {}).get("success"):
                                field_insights = result.get("data", {}).get("field_insights")
                                break
                        import time
                        time.sleep(check_interval)
                        elapsed_time += check_interval
                    
                    if not field_insights:
                        return {"error": "Failed to get field insights from analyze_layer_fields"}
                
                return generate_smart_dashboard_layout(layer_name, analysis_type, theme, field_insights)
                
            elif function_name == "get_current_dashboard_layout":
                return get_current_dashboard_layout()
                
            elif function_name == "get_current_dashboard_charts":
                return get_current_dashboard_charts()
                
            elif function_name == "get_field_stories_and_samples":
                return get_field_stories_and_samples()
                
            elif function_name == "update_dashboard_charts":
                charts_data = parameters.get("charts_data", [])
                return update_dashboard_charts(charts_data)
                
            else:
                return {"error": f"Unknown dashboard function: {function_name}"}
                
        except Exception as e:
            return {"error": f"Error executing dashboard function '{function_name}': {str(e)}"}

try:
    from langchain_core.messages import AIMessage, HumanMessage
except Exception:
    # Minimal message fallbacks
    class AIMessage:
        def __init__(self, content: str):
            self.content = content

    class HumanMessage:
        def __init__(self, content: str):
            self.content = content

from .progent_functions import AVAILABLE_FUNCTIONS, generate_smart_dashboard_layout, get_current_dashboard_layout, get_current_dashboard_charts, get_field_stories_and_samples, update_dashboard_charts
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
            if func_id in AVAILABLE_FUNCTIONS:
                func_name = AVAILABLE_FUNCTIONS[func_id]
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
        self.websocket_manager = websocket_manager
        self.callback_handler = LoggingCallbackHandler(logger)
        self.set_model(model_key)

    def _get_tools(self, client_id: str) -> List[BaseTool]:
        """Gets the tools for the LangChain agent."""
        return [
            Tool(
                name="get_functions_declaration",
                func=_get_declarations_stateless,
                description="Gets the function declaration for one or more functions. Input must be a string representing a list of integers (e.g., '[8]' or '[1, 2, 3]').",
            ),
            ExecuteSpatialFunctionTool(websocket_manager=self.websocket_manager, client_id=client_id),
        ]


    

    def set_model(self, model_key: str):
        """Sets the AI model for the agent."""
        from .config import get_model_config
        self.model_key = model_key
        model_config = get_model_config(model_key)
        # Only instantiate the Google Gemini LLM when a Gemini model is selected.
        # Creating a ChatGoogleGenerativeAI instance for non-Gemini models causes
        # the langchain google client to validate the presence of GOOGLE_API_KEY
        # (or google_api_key param) which is not required for local models like Ollama.
        if model_key.startswith("GEMINI"):
            try:
                from langchain_google_genai import ChatGoogleGenerativeAI
            except Exception as ie:
                # If the Google client isn't available, log and set llm to None.
                logger.warning(f"Could not import langchain_google_genai: {ie}. Gemini agent will not be available.")
                self.llm = None
            else:
                self.llm = ChatGoogleGenerativeAI(
                    model=model_config["model"],
                    google_api_key=model_config.get("api_key", None),
                    temperature=model_config["temperature"],
                    max_output_tokens=model_config["max_tokens"],
                )
                logger.info("LangChain agent LLM set to Google Gemini")
        else:
            # For non-Gemini models, try to provide a LangChain-compatible
            # adapter for Ollama so the same agent/tools can be reused.
            if model_key.startswith("OLLAMA") or "ollama" in model_config.get("provider", "").lower():
                try:
                    # Lazy-import OllamaService from the local module
                    from .ollama_service import OllamaService

                    class OllamaLLMAdapter:
                        """Minimal adapter that exposes a generate-like interface
                        compatible with LangChain's expected LLM contract.
                        It forwards requests to the existing OllamaService.
                        """
                        def __init__(self, ollama_service: OllamaService, model_name: str, temperature: float = 0.7, max_tokens: int = 1024):
                            self.ollama = ollama_service
                            self.model = model_name
                            self.temperature = temperature
                            self.max_tokens = max_tokens

                        async def agenerate(self, prompts: List[str], **kwargs):
                            # Convert single prompt into Ollama messages
                            prompt = prompts[0] if isinstance(prompts, list) and prompts else prompts
                            messages = [{"role": "user", "content": prompt}]
                            resp = await self.ollama.generate_response(messages, model=self.model, temperature=self.temperature, max_tokens=self.max_tokens)
                            # LangChain expects a structure with 'generations'
                            return {"generations": [[{"text": resp.get("content", ""), "generation_info": resp.get("usage", {})}]]}

                        async def __call__(self, prompt: str, **kwargs):
                            return await self.agenerate([prompt], **kwargs)

                    # Create or reuse a global OllamaService instance stored on this class
                    if not hasattr(self, "_ollama_service") or self._ollama_service is None:
                        self._ollama_service = OllamaService()
                        # Initialize the service synchronously if necessary
                        try:
                            import asyncio as _asyncio
                            _asyncio.get_event_loop().run_until_complete(self._ollama_service.initialize())
                        except Exception:
                            # If event loop is already running (e.g., uvicorn), create task instead
                            pass

                    self.llm = OllamaLLMAdapter(self._ollama_service, model_config.get("model", "gemma:2b"), temperature=model_config.get("temperature", 0.7), max_tokens=model_config.get("max_tokens", 1024))
                    logger.info("LangChain agent LLM set to Ollama adapter for local model")
                except Exception as ie:
                    logger.warning(f"Could not create Ollama adapter: {ie}. LangChain agent will not be available for Ollama.")
                    self.llm = None
            else:
                # No adapter available; do not instantiate LangChain LLM
                self.llm = None
                logger.info(f"LangChain agent not instantiated for model: {model_key}")
        self.prompt = self._create_prompt_template()
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
            tools = self._get_tools(client_id)
            if not self.llm:
                raise RuntimeError("LangChain LLM not instantiated. LangChain agent is only available for GEMINI models.")
            agent = create_react_agent(self.llm, tools, self.prompt)
            agent_executor = AgentExecutor(
                agent=agent,
                tools=tools,
                verbose=True,
                handle_parsing_errors=True,
                callbacks=[self.callback_handler]
            )

            # Only include user and assistant (final answer) messages in history
            chat_history_lines = []
            for msg in conversation_history:
                if msg.get("role") == "user":
                    chat_history_lines.append(f"User: {msg.get('content','')}")
                elif msg.get("role") == "assistant":
                    chat_history_lines.append(f"Progent: {msg.get('content','')}")
            chat_history_str = "\n".join(chat_history_lines)

            response = await agent_executor.ainvoke({
                "input": user_message,
                "arcgis_state": json.dumps(arcgis_state, indent=2),
                "available_functions": json.dumps(AVAILABLE_FUNCTIONS, indent=2),
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