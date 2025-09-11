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
        import json
        import re
        function_name = "[unknown]"
        try:
            # Enhanced parsing to handle Ollama's extra conversational text
            cleaned_input = tool_input_str.strip()

            # Try to extract JSON from the input using regex
            # Look for JSON-like patterns: {...} or {...}
            json_patterns = [
                r'\{.*\}',  # Match JSON objects
            ]

            json_match = None
            for pattern in json_patterns:
                match = re.search(pattern, cleaned_input, re.DOTALL)
                if match:
                    json_match = match.group(0)
                    break

            if json_match:
                # Use the extracted JSON
                tool_input_str = json_match

            # Try to parse as JSON first
            try:
                tool_input = json.loads(tool_input_str)
            except json.JSONDecodeError:
                # If JSON parsing fails, try ast.literal_eval as fallback
                try:
                    temp_input = ast.literal_eval(tool_input_str)
                    if isinstance(temp_input, str):
                        tool_input = json.loads(temp_input)
                    else:
                        tool_input = temp_input
                except (ValueError, SyntaxError):
                    return {"error": f"Failed to parse input as JSON or Python literal: {tool_input_str}"}

            if not isinstance(tool_input, dict):
                return {"error": f"Parsed input is not a dictionary. Got type: {type(tool_input)}"}

            function_name = tool_input.pop("function_name", None)
            if not function_name:
                return {"error": "'function_name' must be provided in the input dictionary."}

            # Extract parameters (remaining tool_input after removing function_name)
            parameters = tool_input

            # Default aggregation to SUM for add_chart_to_dashboard if not specified
            if function_name == "add_chart_to_dashboard" and "aggregation" not in parameters:
                parameters["aggregation"] = "SUM"

            # Handle dashboard functions locally (server-side)
            dashboard_functions = [
                "generate_dashboard_for_target_layer",
                "get_current_dashboard_layout",
                "get_current_dashboard_charts",
                "get_dashboard_field_detailed_description",
                "update_dashboard_charts",
                "delete_charts_from_dashboard",
                "update_dashboard_layout"
            ]
            
            if function_name in dashboard_functions:
                return self._execute_dashboard_function(function_name, parameters)

            arcgis_client = self.websocket_manager.get_arcgis_client()
            if not arcgis_client:
                return {"error": "ArcGIS Pro client not connected."}

            if isinstance(parameters, dict) and "arguments" in parameters and len(parameters) == 1 and isinstance(parameters["arguments"], dict):
                parameters = parameters["arguments"]

            # For add_chart_to_dashboard, overwrite layer_name with the one from dashboard JSON
            if function_name == "add_chart_to_dashboard":
                try:
                    import os
                    dashboard_path = os.path.join(os.path.dirname(__file__), '..', 'progent_dashboard.json')
                    if os.path.exists(dashboard_path):
                        with open(dashboard_path, 'r', encoding='utf-8') as f:
                            dashboard_data = json.load(f)
                        parameters["layer_name"] = dashboard_data.get("layer_name", parameters.get("layer_name", "Unknown Layer"))
                        
                        # Validate field names
                        fields = parameters.get("fields", [])
                        if fields:
                            validation = validate_field_names(fields)
                            if not validation["valid"]:
                                return {"error": validation["message"]}
                except Exception as e:
                    logger.warning(f"Failed to load dashboard JSON for layer_name override: {e}")

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
                        result_data = result.get("data", result)
                        
                        # Handle dashboard update broadcasting for any function that returns is_dashboard_update
                        if (isinstance(result_data, dict) and 
                            result_data.get("success") and 
                            result_data.get("is_dashboard_update")):
                            try:
                                # Load the current dashboard
                                import os
                                dashboard_path = os.path.join(os.path.dirname(__file__), '..', 'progent_dashboard.json')
                                if os.path.exists(dashboard_path):
                                    with open(dashboard_path, 'r', encoding='utf-8') as f:
                                        dashboard_data = json.load(f)
                                    
                                    # Special handling for add_chart_to_dashboard results
                                    if (result_data.get("is_chart_addition") and 
                                        result_data.get("new_chart") and 
                                        result_data.get("layout_item")):
                                        # Add the new chart to the existing dashboard
                                        if "charts" not in dashboard_data:
                                            dashboard_data["charts"] = []
                                        dashboard_data["charts"].append(result_data["new_chart"])
                                        
                                        # Add the layout item to the existing layout
                                        if "layout" not in dashboard_data:
                                            dashboard_data["layout"] = {"items": []}
                                        if "items" not in dashboard_data["layout"]:
                                            dashboard_data["layout"]["items"] = []
                                        dashboard_data["layout"]["items"].append(result_data["layout_item"])
                                        
                                        # Save the updated dashboard back to the file
                                        with open(dashboard_path, 'w', encoding='utf-8') as f:
                                            json.dump(dashboard_data, f, indent=2, ensure_ascii=False)
                                    
                                    # Transform for frontend and broadcast
                                    from .main import transform_dashboard_for_frontend
                                    frontend_payload = transform_dashboard_for_frontend(dashboard_data)
                                    
                                    # Broadcast the transformed payload if successful, otherwise broadcast raw data
                                    payload_to_broadcast = frontend_payload if isinstance(frontend_payload, dict) and "error" not in frontend_payload else dashboard_data
                                    
                                    asyncio.run(self.websocket_manager.broadcast_to_type("chatbot", {
                                        "type": "dashboard_update",
                                        "data": payload_to_broadcast
                                    }))
                                    
                                    # Mark that dashboard update has been handled by agent
                                    result_data["_dashboard_update_handled"] = True
                                    
                            except Exception as broadcast_error:
                                # Log but don't fail the function call
                                print(f"Warning: Failed to broadcast dashboard update: {broadcast_error}")
                        
                        return result_data
                
                import time
                time.sleep(check_interval)
                elapsed_time += check_interval
            
            return {"error": f"Timeout waiting for response from ArcGIS Pro for function '{function_name}'."}

        except (SyntaxError, ValueError) as e:
            return {"error": f"Failed to parse input string: {e}. Input was: {tool_input_str}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred while executing '{function_name}': {e}"}

    def _execute_dashboard_function(self, function_name: str, parameters: dict) -> dict:
        """Execute dashboard functions locally on the server side using the new API."""
        import json
        result = {}
        try:
            # The agent sometimes wraps parameters in an 'arguments' dict. Unwrap it.
            if isinstance(parameters, dict) and "arguments" in parameters and isinstance(parameters["arguments"], dict):
                parameters = parameters["arguments"]

            # Special handling for generate_dashboard_for_target_layer to fetch insights if needed
            if function_name == "generate_dashboard_for_target_layer":
                # If no field_insights provided, fetch them from the layer
                if not parameters.get("field_insights"):
                    arcgis_client = self.websocket_manager.get_arcgis_client()
                    if not arcgis_client:
                        return {"success": False, "message": "ArcGIS Pro client not connected for field analysis."}
                    
                    session_id = str(uuid.uuid4())
                    analysis_payload = {
                        "type": "execute_function", "function_name": "analyze_layer_fields",
                        "parameters": {"layer": parameters.get("layer_name")}, "session_id": session_id,
                        "source_client": self.client_id
                    }
                    asyncio.run(self.websocket_manager.send_to_client(arcgis_client, analysis_payload))

                    max_wait_time = 120
                    check_interval = 0.2
                    elapsed_time = 0
                    field_insights = None
                    while elapsed_time < max_wait_time:
                        if self.websocket_manager.has_function_result(session_id):
                            insight_result = self.websocket_manager.get_function_result(session_id)
                            if insight_result and insight_result.get("data", {}).get("success"):
                                field_insights = insight_result.get("data", {}).get("field_insights")
                                break
                        import time
                        time.sleep(check_interval)
                        elapsed_time += check_interval

                    if not field_insights:
                        return {"success": False, "message": "Failed to get field insights from ArcGIS Pro."}

                    parameters["field_insights"] = field_insights

            # Dynamically call the correct dashboard function
            if function_name == "generate_dashboard_for_target_layer":
                layer_name = parameters.get("layer_name")
                analysis_type = parameters.get("analysis_type", "overview")
                theme = parameters.get("theme", "default")
                field_insights = parameters.get("field_insights")
                result = generate_dashboard_for_target_layer(layer_name, analysis_type, theme, field_insights)
            elif function_name == "get_current_dashboard_layout":
                result = get_current_dashboard_layout()
            elif function_name == "get_current_dashboard_charts":
                result = get_current_dashboard_charts()
            elif function_name == "get_dashboard_field_detailed_description":
                result = get_dashboard_field_detailed_description()
            elif function_name == "update_dashboard_charts":
                charts_data = parameters.get("charts_data", [])
                
                # Validate field names in charts_data
                all_fields = []
                for chart_update in charts_data:
                    chart = chart_update.get("chart", {})
                    fields = chart.get("fields", [])
                    all_fields.extend(fields)
                
                if all_fields:
                    validation = validate_field_names(all_fields)
                    if not validation["valid"]:
                        return {"success": False, "error": validation["message"]}
                
                result = update_dashboard_charts(charts_data)
                
                # Handle websocket calls for chart additions if required
                if result.get("success") and result.get("requires_websocket_calls"):
                    charts_to_add = result.get("charts_to_add", [])
                    successful_additions = 0
                    addition_errors = []
                    
                    arcgis_client = self.websocket_manager.get_arcgis_client()
                    if not arcgis_client:
                        result = {"success": False, "error": "ArcGIS Pro client not connected for chart additions."}
                    else:
                        # Process each chart addition via websocket - simple approach
                        for i, chart_params in enumerate(charts_to_add):
                            try:
                                session_id = str(uuid.uuid4())
                                payload = {
                                    "type": "execute_function",
                                    "function_name": "add_chart_to_dashboard",
                                    "parameters": chart_params,
                                    "session_id": session_id,
                                    "source_client": self.client_id
                                }
                                
                                asyncio.run(self.websocket_manager.send_to_client(arcgis_client, payload))
                                
                                # Wait for response
                                import time
                                max_wait_time = 120
                                check_interval = 0.2
                                elapsed_time = 0
                                
                                while elapsed_time < max_wait_time:
                                    if self.websocket_manager.has_function_result(session_id):
                                        addition_result = self.websocket_manager.get_function_result(session_id)
                                        if addition_result:
                                            # Check for success in ArcGIS Pro response structure
                                            # ArcGIS Pro returns: {"status": "success", "data": {"success": true, ...}}
                                            response_status = addition_result.get("status")
                                            response_data = addition_result.get("data", {})
                                            
                                            if response_status == "success" or response_data.get("success"):
                                                successful_additions += 1
                                                break
                                            else:
                                                # Extract error message from ArcGIS Pro response
                                                error_msg = response_data.get("error", "Unknown error")
                                                addition_errors.append(f"Chart {i+1}: {error_msg}")
                                                break
                                        else:
                                            addition_errors.append(f"Chart {i+1}: No response received")
                                            break
                                    time.sleep(check_interval)
                                    elapsed_time += check_interval
                                
                                if elapsed_time >= max_wait_time:
                                    addition_errors.append(f"Chart {i+1}: Timeout waiting for response")
                                    
                            except Exception as e:
                                addition_errors.append(f"Chart {i+1}: {str(e)}")
                        
                        # Update result based on websocket call outcomes
                        if successful_additions == len(charts_to_add):
                            # Step 3: Handle reindexing if needed (simple JSON manipulation)
                            if result.get("requires_reindexing") and "original_index" in result:
                                original_index = result["original_index"]
                                
                                # Call the simple reindexing function
                                from .progent_functions import reindex_last_chart_to_position
                                reindex_result = reindex_last_chart_to_position(original_index)
                                
                                if reindex_result.get("success"):
                                    result = {
                                        "success": True,
                                        "message": f"Successfully updated and reindexed chart to position {original_index}",
                                        "is_dashboard_update": True
                                    }
                                else:
                                    result = {
                                        "success": True,
                                        "message": f"Chart updated but reindexing failed: {reindex_result.get('error')}",
                                        "is_dashboard_update": True
                                    }
                            else:
                                result = {
                                    "success": True,
                                    "message": f"Successfully updated {successful_additions} charts in dashboard",
                                    "is_dashboard_update": True
                                }
                        elif successful_additions > 0:
                            result = {
                                "success": True,
                                "message": f"Partially successful: {successful_additions}/{len(charts_to_add)} charts updated. Errors: {'; '.join(addition_errors)}",
                                "is_dashboard_update": True
                            }
                        else:
                            result = {
                                "success": False,
                                "error": f"Failed to add any charts. Errors: {'; '.join(addition_errors)}"
                            }
            elif function_name == "delete_charts_from_dashboard":
                indices = parameters.get("indices", [])
                result = delete_charts_from_dashboard(indices)
            elif function_name == "update_dashboard_layout":
                layout_updates = parameters.get("layout_updates", {})
                result = update_dashboard_layout(layout_updates)
            else:
                return {"success": False, "message": f"Unknown dashboard function: {function_name}"}

            # Broadcast dashboard update to frontend clients if this was a dashboard modification
            if result.get("success") and result.get("is_dashboard_update"):
                try:
                    # Load the updated dashboard and broadcast it
                    import os
                    dashboard_path = os.path.join(os.path.dirname(__file__), '..', 'progent_dashboard.json')
                    if os.path.exists(dashboard_path):
                        with open(dashboard_path, 'r', encoding='utf-8') as f:
                            dashboard_data = json.load(f)
                        
                        # Special handling for add_chart_to_dashboard results
                        if result.get("is_chart_addition") and result.get("new_chart") and result.get("layout_item"):
                            # Add the new chart to the existing dashboard
                            if "charts" not in dashboard_data:
                                dashboard_data["charts"] = []
                            dashboard_data["charts"].append(result["new_chart"])
                            
                            # Add the layout item to the existing layout
                            if "layout" not in dashboard_data:
                                dashboard_data["layout"] = {"items": []}
                            if "items" not in dashboard_data["layout"]:
                                dashboard_data["layout"]["items"] = []
                            dashboard_data["layout"]["items"].append(result["layout_item"])
                            
                            # Save the updated dashboard back to the file
                            with open(dashboard_path, 'w', encoding='utf-8') as f:
                                json.dump(dashboard_data, f, indent=2, ensure_ascii=False)
                        
                        # Transform for frontend and broadcast
                        from .main import transform_dashboard_for_frontend
                        frontend_payload = transform_dashboard_for_frontend(dashboard_data)
                        
                        # Broadcast the transformed payload if successful, otherwise broadcast raw data
                        payload_to_broadcast = frontend_payload if isinstance(frontend_payload, dict) and "error" not in frontend_payload else dashboard_data
                        
                        asyncio.run(self.websocket_manager.broadcast_to_type("chatbot", {
                            "type": "dashboard_update",
                            "data": payload_to_broadcast
                        }))
                        
                        # Mark that dashboard update has been handled by agent
                        result["_dashboard_update_handled"] = True
                        
                except Exception as broadcast_error:
                    # Log but don't fail the function call
                    print(f"Warning: Failed to broadcast dashboard update: {broadcast_error}")

            return result
                
        except Exception as e:
            return {"success": False, "message": f"Error executing dashboard function '{function_name}': {str(e)}"}

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

from .progent_functions import AVAILABLE_FUNCTIONS, generate_dashboard_for_target_layer, get_current_dashboard_layout, get_current_dashboard_charts, get_dashboard_field_detailed_description, update_dashboard_charts, delete_charts_from_dashboard, update_dashboard_layout
from .config import settings
from .ai.function_declarations import FunctionDeclaration

logger = logging.getLogger(__name__)

def validate_field_names(fields_list):
    """
    Validate field names against the dashboard JSON field_insights.
    Returns a dict with 'valid': bool and 'message': str
    """
    try:
        import os
        dashboard_path = os.path.join(os.path.dirname(__file__), '..', 'progent_dashboard.json')
        if not os.path.exists(dashboard_path):
            return {"valid": False, "message": "Dashboard file not found"}
        
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            dashboard_data = json.load(f)
        
        field_insights = dashboard_data.get("field_insights", {})
        valid_fields = list(field_insights.keys())
        
        invalid_fields = []
        for field in fields_list:
            if field not in valid_fields:
                invalid_fields.append(field)
        
        if not invalid_fields:
            return {"valid": True, "message": "All field names are valid"}
        else:
            return {
                "valid": False, 
                "message": f"Invalid field names: {', '.join(invalid_fields)}. Please select from: {', '.join(valid_fields)}"
            }
            
    except Exception as e:
        return {"valid": False, "message": f"Error validating fields: {str(e)}"}

def _get_declarations_stateless(function_ids_str: str) -> str:
    """
    A stateless helper to get function declarations.
    It imports and accesses the necessary data directly to avoid state issues.
    Enhanced to handle Ollama's tendency to add extra conversational text.
    """
    try:
        # Access the class variables directly without creating an instance
        functions_declaration = FunctionDeclaration.functions_declarations

        # Parse the input - handle multiple formats and extra text from Ollama
        function_ids = []

        if isinstance(function_ids_str, str):
            # Clean the input by removing extra conversational text that Ollama might add
            import re

            # Look for patterns like [10], [1,2,3], 10, "10", etc.
            # Remove common Ollama additions like "Please let me know what you'd like to do next!"
            cleaned_input = function_ids_str.strip()

            # Extract just the function ID part using regex
            # Look for patterns: [digits], digits, "digits", 'digits'
            patterns = [
                r'\[(\d+(?:\s*,\s*\d+)*)\]',  # [10] or [1,2,3]
                r'"(\d+(?:\s*,\s*\d+)*)"',     # "10" or "1,2,3"
                r"'(\d+(?:\s*,\s*\d+)*)'",     # '10' or '1,2,3'
                r'^(\d+(?:\s*,\s*\d+)*)$',     # 10 or 1,2,3 (at start of string)
            ]

            extracted_ids = None
            for pattern in patterns:
                match = re.search(pattern, cleaned_input)
                if match:
                    extracted_ids = match.group(1)
                    break

            if extracted_ids:
                # Split by comma and convert to integers
                id_strings = [id.strip() for id in extracted_ids.split(',')]
                function_ids = [int(id_str) for id_str in id_strings if id_str.isdigit()]
            else:
                # Fallback: try to extract any digits from the input
                digits = re.findall(r'\d+', cleaned_input)
                if digits:
                    function_ids = [int(d) for d in digits[:5]]  # Limit to first 5 digits to avoid false matches
                else:
                    return f"Error: Could not extract function IDs from input: {function_ids_str}"
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
            
            # Add action input examples if they exist
            examples = details.get("action_input_examples", [])
            if examples:
                output.append("  Action Input Examples:")
                for i, example in enumerate(examples, 1):
                    output.append(f"    Example {i}: {json.dumps(example)}")
        
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
        
        logger.info(f"LangChainAgent.set_model called with: {model_key}")
        # Create a safe version of model_config for logging (mask API key)
        safe_config = model_config.copy()
        if "api_key" in safe_config and safe_config["api_key"]:
            safe_config["api_key"] = "***masked***"
        logger.info(f"Model config: {safe_config}")
        
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
                # Only instantiate the LLM if an API key is provided.
                # This prevents crashes when the user hasn't set up their key yet.
                if model_config.get("api_key"):
                    self.llm = ChatGoogleGenerativeAI(
                        model=model_config["model"],
                        google_api_key=model_config.get("api_key"),
                        temperature=model_config["temperature"],
                        max_output_tokens=model_config["max_tokens"],
                    )
                    logger.info("LangChain agent LLM set to Google Gemini")
                else:
                    self.llm = None
                    logger.warning("Google Gemini model selected, but no API key found. The agent will not be functional until a key is provided.")
        else:
            # For non-Gemini models, try to provide a LangChain-compatible
            # adapter for Ollama so the same agent/tools can be reused.
            if model_key.startswith("OLLAMA") or "ollama" in model_config.get("provider", "").lower():
                try:
                    # Use the official langchain-ollama integration with timeout
                    from langchain_ollama import ChatOllama
                    
                    self.llm = ChatOllama(
                        model=model_config.get("model", "llama3.2:3b"),
                        base_url=model_config.get("endpoint", "http://localhost:11434"),
                        temperature=model_config.get("temperature", 0.7),
                        num_predict=model_config.get("max_tokens", 1024),
                        # Add timeout and other parameters to prevent hanging
                        timeout=30,  # 30 second timeout
                        verbose=True
                    )
                    logger.info(f"LangChain agent LLM set to ChatOllama for model: {model_config.get('model')} with 30s timeout")
                except ImportError as ie:
                    logger.warning(f"langchain-ollama not available: {ie}. Ollama models will use direct flow.")
                    self.llm = None
                except Exception as ie:
                    logger.error(f"Error setting up ChatOllama: {ie}. Ollama models will use direct flow.")
                    self.llm = None
            else:
                # No adapter available; do not instantiate LangChain LLM
                self.llm = None
                logger.info(f"LangChain agent not instantiated for model: {model_key}")
        self.prompt = self._create_prompt_template()
        logger.info(f"LangChain agent model set to: {self.model_key}")

    def _simplify_arcgis_state_for_prompt(self, state: Dict) -> str:
        """Simplify ArcGIS state for inclusion in prompt"""
        if not state:
            return "No ArcGIS Pro project currently open."
        
        layers_info = state.get("layers_info", {})
        layer_count = len(layers_info)
        layer_names = list(layers_info.keys())
        
        simplified = f"""
Project: {state.get('project_path', 'Unknown')}
Map: {state.get('map_name', 'Unknown')}
Layers ({layer_count} total): {', '.join(layer_names) if layer_names else 'None'}
Default GDB: {state.get('default_gdb', 'Unknown')}"""
        
        return simplified.strip()

    def _create_prompt_template(self) -> PromptTemplate:
        """Creates the optimized prompt template for the agent with Ollama-specific formatting rules."""
        template = """You are a helpful AI assistant connected to ArcGIS Pro.

Current ArcGIS Pro State: {arcgis_state}

{chat_history}

You can chat normally or help with GIS tasks. For simple questions about the current state (like "how many layers"), answer directly from the ArcGIS state above. Only use tools when you need to perform actual GIS operations.

Available tools: {tools}

Here is a list of available functions you can use:
{available_functions}

To use a function, you must first get its declaration using the `get_functions_declaration` tool with the function's ID.
The declaration will be returned as a string, describing the function, its parameters, and their types.
Once you have the declaration, you can execute the function using the `execute_spatial_function` tool.

WORKFLOW:
1. Use get_functions_declaration with the function ID (like "[10]") to get the function details
2. Look for the actual function name in the response (like "clip_layer")
3. Use execute_spatial_function with ONLY that function name and parameters

CRITICAL: In execute_spatial_function, use the ACTUAL FUNCTION NAME from the declaration, NOT the ID number.

FORMATTING RULES - FOLLOW THESE EXACTLY:

For get_functions_declaration:
- Action Input must be EXACTLY like: [10] or [1,2,3]
- No quotes around the brackets, no extra text

For execute_spatial_function:
- Action Input must be valid JSON with function_name and parameters at the TOP LEVEL
- Parameters go directly in the main JSON object, NOT inside a "parameters" key
- No explanatory text, comments, or extra formatting

EXAMPLES:
- Correct: {{"function_name": "create_buffer", "layer_name": "Fuel_Stations", "distance": 1000}}
- Wrong: {{"function_name": "create_buffer", "parameters": {{"layer_name": "Fuel_Stations", "distance": 1000}}}}

STOPPING CRITERIA:
- When you see a successful result (like {{"success": True, "output_layer": "..."}}), STOP and provide Final Answer
- Do NOT repeat actions that have already been completed
- Do NOT call get_functions_declaration multiple times for the same function

IMPORTANT: Do NOT wrap parameters in a "parameters" object. Put them directly in the main JSON.
IMPORTANT: Do NOT add explanatory text or comments in Action Input - provide ONLY the JSON.
IMPORTANT: Do NOT use markdown formatting, code blocks, or triple backticks (```) in your responses.
IMPORTANT: After seeing a successful function result, immediately provide your Final Answer - do not repeat actions.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

CRITICAL STOPPING RULE:
- When you see Observation with "success": True, immediately proceed to "Thought: I now know the final answer" and "Final Answer:"
- Do NOT repeat previous actions
- Do NOT call the same function multiple times

Begin!

Question: {input}
Thought: {agent_scratchpad}"""
        return PromptTemplate(template=template, input_variables=["tools", "tool_names", "chat_history", "input", "agent_scratchpad", "arcgis_state", "available_functions"])

    async def generate_response(
        self,
        user_message: str,
        conversation_history: List[Dict],
        arcgis_state: Dict,
        client_id: str = None
    ) -> Dict[str, Any]:
        """Generates a response using the LangChain agent with smart message classification."""
        logger.info(f"LangChain agent generating response for: {user_message[:100]}...")

        try:
            if not self.llm:
                raise RuntimeError("LangChain LLM not instantiated.")
            
            # Build chat history for classification
            chat_history_lines = []
            for msg in conversation_history:
                if msg.get("role") == "user":
                    chat_history_lines.append(f"User: {msg.get('content','')}")
                elif msg.get("role") == "assistant":
                    chat_history_lines.append(f"Assistant: {msg.get('content','')}")
            chat_history_str = "\n".join(chat_history_lines)

            # Phase 1: Smart Message Classification
            classification_prompt = f"""You are an AI assistant for ArcGIS Pro. Classify the user's message:

{chat_history_str}
User: {user_message}

Does this message require GIS operations/tools, or is it conversational?

Respond with exactly one word:
- "TOOLS" if the user wants GIS analysis, data manipulation, spatial operations, or asks about layers/maps
- "CHAT" if it's a greeting, general question about you, or casual conversation

Message: {user_message}
Classification:"""

            logger.info(f"Classification prompt sent to AI: {classification_prompt[:500]}...")
            
            from langchain_core.messages import HumanMessage
            classification_response = await self.llm.ainvoke([HumanMessage(content=classification_prompt)])
            classification = classification_response.content.strip().upper()
            
            logger.info(f"Message classification: {classification}")

            if classification == "CHAT":
                # Handle as conversational message - no tools needed
                conversational_prompt = f"""You are a helpful AI assistant for ArcGIS Pro software.

{chat_history_str}

You are directly connected to ArcGIS Pro and can help with GIS tasks when needed, but right now the user is just having a conversation with you.

Respond naturally to their message. Do not use markdown, code blocks, or special formatting.

User: {user_message}
Assistant:"""

                logger.info(f"Conversational prompt sent to AI: {conversational_prompt[:500]}...")
                
                response = await self.llm.ainvoke([HumanMessage(content=conversational_prompt)])
                return {"output": response.content}
            
            else:
                # Handle as GIS operation using tools
                tools = self._get_tools(client_id)
                logger.info(f"Available tools for client {client_id}: {[tool.name for tool in tools]}")
                
                agent = create_react_agent(self.llm, tools, self.prompt)
                agent_executor = AgentExecutor(
                    agent=agent,
                    tools=tools,
                    verbose=True,
                    handle_parsing_errors=True,
                    callbacks=[self.callback_handler],
                    max_iterations=20
                )

                # Simplify ArcGIS state for the prompt
                simplified_state = self._simplify_arcgis_state_for_prompt(arcgis_state)
                
                response = await agent_executor.ainvoke({
                    "input": user_message,
                    "chat_history": chat_history_str,
                    "tool_names": ", ".join([tool.name for tool in tools]),
                    "arcgis_state": simplified_state,
                    "available_functions": json.dumps(AVAILABLE_FUNCTIONS, indent=2)
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