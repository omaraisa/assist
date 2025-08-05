import json
import re
import logging
from typing import Dict, List, Optional, Any
import aiohttp
from .config import settings, get_model_config
from .spatial_functions import SpatialFunctions
from .ai.ai_response_handler import AIResponseHandler
from .langchain_agent import LangChainAgent
from .ai.utils import (
    OLLAMA_AVAILABLE,
    RAG_AVAILABLE,
    OllamaService,
    RAGService,
)

logger = logging.getLogger(__name__)

class AIService:
    """Handles AI model interactions and response generation."""

    def __init__(self, initial_model_key: str, websocket_manager: Any):
        self.websocket_manager = websocket_manager
        self.langchain_agent = None
        self.set_model(initial_model_key)
    
    async def initialize(self):
        """Initialize the AI service"""
        self.session = aiohttp.ClientSession()
        
        # Initialize the response handler
        self.response_handler = AIResponseHandler(self.session, None)  # ollama_service will be set later
        
        # Initialize LangChain agent
        self.langchain_agent = LangChainAgent(self.current_model, self.websocket_manager)
        
        # Initialize Ollama service if available
        logger.info(f"OLLAMA_AVAILABLE: {OLLAMA_AVAILABLE}")
        if OLLAMA_AVAILABLE and OllamaService is not None:
            try:
                logger.info(f"Initializing Ollama service at: {settings.OLLAMA_BASE_URL}")
                self.ollama_service = OllamaService(settings.OLLAMA_BASE_URL)
                await self.ollama_service.initialize()
                # Update response handler with ollama service
                self.response_handler.ollama_service = self.ollama_service
                logger.info("Ollama service initialized successfully")
            except Exception as e:
                logger.error(f"Could not initialize Ollama service: {e}", exc_info=True)
                self.ollama_service = None
        else:
            logger.info("Ollama service not available (import failed)")
          # Initialize RAG service if available
        if RAG_AVAILABLE and RAGService is not None and settings.ENABLE_RAG:
            try:
                self.rag_service = RAGService()
                await self.rag_service.initialize()
            except Exception as e:
                logger.warning(f"Could not initialize RAG service: {e}")
                self.rag_service = None
        
        logger.info(f"AI Service initialized with model: {self.current_model}")
    
    async def cleanup(self):
        """Cleanup resources"""
        if self.session:
            await self.session.close()
        if self.ollama_service:
            await self.ollama_service.cleanup()
    
    def set_model(self, model_key: str):
        """Set the current AI model"""
        if model_key in settings.AI_MODELS:
            self.current_model = model_key
            if self.langchain_agent:
                self.langchain_agent.set_model(model_key)
            logger.info(f"AI model changed to: {model_key}")
        else:
            raise ValueError(f"Unknown AI model: {model_key}")

    async def generate_response(
        self, 
        user_message: str, 
        conversation_history: List[Dict], 
        arcgis_state: Dict,
        client_id: str = None
    ) -> Dict[str, Any]:
        """Generate AI response with function calling support"""
        try:
            logger.info(f"Generating response for model: {self.current_model}")
            logger.info(f"User message: {user_message[:100]}...")
            
            if self.current_model.startswith("GEMINI"):
                logger.info("Using LangChain agent for Gemini model")
                if not self.langchain_agent:
                    raise RuntimeError("LangChain agent is not initialized.")
                
                response = await self.langchain_agent.generate_response(
                    user_message,
                    conversation_history,
                    arcgis_state,
                    client_id
                )
                return {"type": "text", "content": response["output"], "model": self.current_model}

            # Fallback to existing logic for other models
            model_config = get_model_config(self.current_model)
            logger.info(f"Model config retrieved for: {model_config.get('name', 'unknown')}")
            
            if self.response_handler and client_id:
                self.response_handler.set_client_context(client_id, self)
            
            messages = self._prepare_messages(
                user_message, 
                conversation_history, 
                arcgis_state,
                client_id
            )
            logger.info(f"Messages prepared, count: {len(messages)}")
            
            response = None
            if self.current_model.startswith("GPT"):
                logger.info("Using OpenAI model")
                response = await self.response_handler._generate_openai_response_with_functions(messages, model_config, user_message)
            elif self.current_model.startswith("CLAUDE"):
                logger.info("Using Claude model")
                response = await self.response_handler._generate_claude_response_with_functions(messages, model_config, user_message)
            elif self.current_model.startswith("OLLAMA"):
                if not OLLAMA_AVAILABLE:
                    return {
                        "type": "error",
                        "content": "Ollama service is not available.",
                        "model": self.current_model
                    }
                logger.info("Using Ollama model")
                response = await self.response_handler._generate_ollama_response_with_functions(messages, model_config, user_message)
            else:
                raise ValueError(f"Unsupported model: {self.current_model}")
            
            logger.info(f"AI generated response type: {response.get('type')}")
            return response

        except Exception as e:
            logger.error(f"Error generating AI response: {str(e)}", exc_info=True)
            return {
                "type": "error",
                "content": f"Error generating response: {str(e)}",
                "model": self.current_model
            }    
            
    def _prepare_messages(
        self, 
        user_message: str, 
        conversation_history: List[Dict], 
        arcgis_state: Dict,
        client_id: str = None
    ) -> List[Dict]:
        """Prepare messages for AI model with function calling context"""
        
        # System prompt for function calling
        system_prompt = self._get_function_calling_system_prompt(arcgis_state)
        logger.info(f"Generated system prompt with {len(system_prompt)} characters for ArcGIS state: {len(str(arcgis_state))} characters")
        
        # Build message history
        messages = [{"role": "system", "content": system_prompt}]
        
        # Add recent conversation history (excluding system messages, but preserving function calls)
        for msg in conversation_history[-10:]:  # Last 10 messages
            if msg["role"] != "system":
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
          # Ensure get_functions_declaration is always available in the conversation
        # Check if it's already been declared in the conversation history
        has_functions_declaration = False
        for msg in messages:
            content = msg.get("content", "")
            # Check if the message contains the get_functions_declaration definition
            if ("get_functions_declaration" in content and 
                "Function Declaration:" in content and 
                "function_ids" in content):
                has_functions_declaration = True
                break
        
        # Also check the conversation history for function declarations
        if not has_functions_declaration:
            for msg in conversation_history[-20:]:  # Check last 20 messages
                content = msg.get("content", "")
                if ("get_functions_declaration" in content and 
                    "Function Declaration:" in content and 
                    "function_ids" in content):
                    has_functions_declaration = True
                    break
        
        # If not found in history, add it as a system-provided function declaration
        if not has_functions_declaration:
            functions_declaration_info = {
                "role": "system",
                "content": '''AVAILABLE FUNCTION: get_functions_declaration

Function Declaration:
{
    "name": "get_functions_declaration",
    "description": "Get function declarations for specific functions by their IDs from the available functions list. MAKE SURE TO SEND VALID IDs. AVAILABLE FUNCTIONS: 1: select_by_attribute, 2: select_by_location, 3: get_field_statistics, 4: get_layer_summary, 5: calculate_area, 6: calculate_length, 7: get_centroid, 8: create_buffer, 9: spatial_join, 10: clip_layer, 11: calculate_distance, 12: get_current_project_path, 13: get_default_db_path, 14: get_field_definitions, 15: get_layer_type, 16: get_list_of_layer_fields, 17: get_data_source_info, 18: create_nearest_neighbor_layer, 19: get_unique_values_count, 20: calculate_empty_values, 21: get_map_layers_info, 22: get_map_tables_info, 23: get_values_frequency, 24: get_value_frequency, 25: get_coordinate_system, 26: get_attribute_table, 27: get_field_domain_values, 28: calculate_new_field, 29: analyze_layer_fields, 30: generate_smart_dashboard_layout, 31: optimize_dashboard_layout",
    "parameters": {
        "function_ids": {
            "type": "array",
            "description": "Array of function IDs (integers) to get declarations for",
            "items": {
                "type": "integer"
            }
        }
    },
    "required": ["function_ids"]
}

This function is ALWAYS available to you. You can call it at any time to get declarations for other functions.'''
            }
            messages.append(functions_declaration_info)
            logger.info("Added get_functions_declaration availability to conversation")
        
        # Add current user message (avoid duplicates)
        if not messages or messages[-1]["content"] != user_message or messages[-1]["role"] != "user":
            messages.append({"role": "user", "content": user_message})
        
        logger.info(f"Prepared {len(messages)} messages for AI model")
        return messages

    def _get_function_calling_system_prompt(self, arcgis_state: Dict) -> str:
        """Get the system prompt for function calling mode"""
        
        # Simplify ArcGIS state to reduce payload
        simplified_state = self._simplify_arcgis_state(arcgis_state)
        
        # Get model-specific identity
        model_identity = self._get_model_identity()
          # Get all available functions from SpatialFunctions
        spatial_functions = SpatialFunctions()
        available_functions = spatial_functions.AVAILABLE_FUNCTIONS
        
        # Format the available functions for the prompt
        functions_list = "\n".join([f"{func_id}: {description}" for func_id, description in available_functions.items()])
        
        return f"""You are an autonomous spatial assistant integrated with ArcGIS Pro. Your job is not to respond like a chatbot — you act like a real GIS agent.

            Your role is to:
            - Understand spatial tasks in natural language
            - Plan all necessary steps to achieve the goal
            - Investigate the current map state and tool availability
            - Discover the right functions
            - Execute them one by one or all at once
            - Handle failures
            - Analyze the results and explain them clearly to the user

            ---

            🧠 YOUR BEHAVIOR (AGENT MODE)

            For any spatial request:
            1. Analyze the user’s message carefully
            2. Plan a logical series of function calls or actions to accomplish it
            3. Determine which functions are required
            4. Call `get_functions_declaration([ids])` to retrieve their definitions
            - You MUST always call this first for unknown or needed tools
            5. Then, perform each step
            6. If a step fails, debug, retry, or fetch more info
            7. Use available internal functions like:
            - `calculate_area`
            - `get_unique_values_count`
            - `analyze_layer_fields` - for dashboard field analysis
            8. Only respond when the goal is fully achieved or fails gracefully with a valid explanation

            ---

            📊 DASHBOARD ANALYSIS CAPABILITIES

            For dashboard and data analysis requests:
            - Use `generate_smart_dashboard_layout(layer_name)` for intelligent 12x9 grid layout generation
            - These functions analyze field types, unique values, null percentages, and recommend chart types
            - Results are saved to dashboard.json for further processing
            - Support requests like "analyze this layer for dashboard", "create dashboard insights", etc.
            
            CRITICAL: For requests like "Generate a smart dashboard layout", you MUST:
            1. Call get_functions_declaration([31]) to get generate_smart_dashboard_layout
            2. IMMEDIATELY call generate_smart_dashboard_layout(layer_name) - DO NOT STOP OR WAIT
            3. The function will automatically handle all analysis and create smart_dashboard.json

            ---

            🧰 TOOLS USAGE

            You only have access to the following function gateway:
            - `get_functions_declaration([ids])`: Get the signature of available functions. You CANNOT use a function unless you fetch its declaration first.

            ---

            🎯 GOAL EXECUTION STRATEGY

            For every user query that requires spatial analysis:
            - NEVER reply generically with "Done" or "Executing plan..."
            - Write and clearly state your PLAN in plain language
            - Execute each part, and give real-time feedback
            - System automatically appends "_ai" to output layer names (e.g., "buildings" → "buildings_ai")
            - If the same layer is processed again, append "_ai" again ("buildings_ai_ai") use that as input for the next step
            - Spaces in output layer names are replaced by underscores (_). For example, "my layer" becomes "my_layer_ai".

            ---

            🛑 ERROR HANDLING

            If a function fails:
            - Try to explain the cause
            - Retry with corrected inputs or ask for clarification
            - Use `get_map_layers_info()` to detect missing layers
            - DO NOT stop responding — always attempt recovery
            - Compare the layer names in user message with existing layers to detect mismatches
            - Layer and field names might not match exactly or even be in different languages. Do your best to match them.
            - If a layer is mentioned that does not exist, inform the user and suggest alternatives

            ---

            🌐 LANGUAGE HANDLING

            Always reply in the same language as the user's message.
            For example:
            - Arabic in → Arabic out
            - English in → English out

            ---

            🧪 EXAMPLES OF GOOD AGENT BEHAVIOR

            User: "قم بعمل حرم لطبقة الأماكن بقطر 3 كم"

            You:
            - Step 1: Call `get_functions_declaration([8])`
            - Step 2: Check if "places" exists via `get_map_layers_info()`
            - Step 3: Call `create_buffer(layer_name="places", distance=3000, units="meters")`
            - Step 4: Confirm layer creation and add it to map
            - Step 5: Say: "تم إنشاء طبقة buffer باسم places_ai، وقد تم عرضها على الخريطة."

            ---

            🧠 CURRENT ARC PRO STATE:
            {json.dumps(simplified_state)}

            You are NOT a chatbot.
            You are a thinking, planning, retrying, executing spatial intelligence agent.

            Do not wait for the user to guide you.
            Respond by executing what is needed — every time.
            
            !!! IMPORTANT NOTE: Once you get function declarations, your next response should consist IMMEDIATELY of the function call(s) you need.
            DO NOT acknowledge receiving the declarations - just proceed directly to calling the functions.
            DO NOT say "Now I can use these functions" or "I received the declarations" - JUST CALL THE FUNCTIONS.
            """

    def _simplify_arcgis_state(self, state: Dict) -> Dict:
        """Simplify ArcGIS state to reduce payload while keeping essential information"""
        if not state:
            return {}
        
        simplified = {}
        
        # Include basic project info
        if "workspace" in state:
            simplified["workspace"] = state["workspace"]
        if "default_gdb" in state:
            simplified["default_gdb"] = state["default_gdb"]
        
        # Simplify layer information - keep only essential fields
        if "layers_info" in state:
            simplified["layers"] = {}
            for layer_name, layer_info in state["layers_info"].items():
                simplified["layers"][layer_name] = {
                    "fields": list(layer_info.get("fields", {}).keys()) if isinstance(layer_info.get("fields"), dict) else [],
                    "definition_query": layer_info.get("definition_query", "")
                }
        
        # Include layer types
        if "layer_types" in state:
            simplified["layer_types"] = state["layer_types"]        
        # Include basemap info
        if "basemap" in state:
            simplified["basemap"] = state["basemap"]
        
        return simplified

    
    def _get_model_identity(self) -> str:
        """Get model-specific identity string"""
        if self.current_model.startswith("GEMINI"):
            return "Gemini AI (Google)"
        elif self.current_model.startswith("GPT"):
            return "GPT (OpenAI)"
        elif self.current_model.startswith("CLAUDE"):
            return "Claude (Anthropic)"
        elif self.current_model.startswith("OLLAMA"):
            return "Llama (Local)"
        else:
            return "AI Assistant"

    # Legacy methods for backward compatibility (marked as deprecated)
    
    def extract_investigate_commands(self, ai_response: str) -> List[str]:
        """Extract INVESTIGATE commands from AI response (DEPRECATED - use function calling instead)"""
        investigate_pattern = r'INVESTIGATE```(.*?)```'
        matches = re.findall(investigate_pattern, ai_response, re.DOTALL)
        return [match.strip() for match in matches if match.strip()]
    
    def extract_complete_response(self, ai_response: str) -> Optional[str]:
        """Extract COMPLETE response from AI response (DEPRECATED - use function calling instead)"""
        complete_pattern = r'COMPLETE```(.*?)```'
        match = re.search(complete_pattern, ai_response, re.DOTALL)
        return match.group(1).strip() if match else None
    
    def parse_function_call(self, function_call_str: str) -> Optional[Dict]:
        """Parse a function call string into function name and parameters (DEPRECATED - use function calling instead)"""
        try:
            # Regex to capture function name and arguments
            func_regex = r'^([a-zA-Z_][a-zA-Z0-9_]*)\s*\((.*)\)$'
            func_match = re.match(func_regex, function_call_str.strip())
            
            if not func_match:
                logger.error(f"Invalid function call format: {function_call_str}")
                return None
            
            function_name = func_match.group(1)
            args_string = func_match.group(2).strip()
            
            # Parse parameters
            parameters = {}
            if args_string:
                parameters = self._parse_function_parameters(args_string)
            
            return {
                "function_name": function_name,
                "parameters": parameters
            }
            
        except Exception as e:
            logger.error(f"Error parsing function call {function_call_str}: {str(e)}")
            return None
    
    def _parse_function_parameters(self, args_string: str) -> Dict:
        """Parse function parameters from argument string (DEPRECATED - use function calling instead)"""
        parameters = {}
        
        # Simple parameter parsing - handles key=value pairs
        arg_pairs = []
        current_pair = ""
        in_quotes = False
        quote_char = None
        
        for char in args_string:
            if char in ['"', "'"] and (not in_quotes or char == quote_char):
                if not in_quotes:
                    in_quotes = True
                    quote_char = char
                elif char == quote_char:
                    in_quotes = False
                    quote_char = None
            
            if char == ',' and not in_quotes:
                arg_pairs.append(current_pair.strip())
                current_pair = ""
            else:
                current_pair += char
        
        if current_pair.strip():
            arg_pairs.append(current_pair.strip())
        
        # Parse each parameter
        for pair in arg_pairs:
            if '=' in pair:
                key, value = pair.split('=', 1)
                key = key.strip()
                value = value.strip()
                
                # Remove quotes if present
                if (value.startswith('"') and value.endswith('"')) or \
                   (value.startswith("'") and value.endswith("'")):
                    value = value[1:-1]
                
                # Convert to appropriate type
                if value.lower() == 'true':
                    value = True
                elif value.lower() == 'false':
                    value = False
                elif value.lower() == 'none':
                    value = None
                elif value.replace('.', '').replace('-', '').isdigit():
                    value = float(value) if '.' in value else int(value)
                
                parameters[key] = value
        
        return parameters
    
    async def generate_investigation_summary(self, session: Dict) -> str:
        """Generate final response after investigation session (DEPRECATED - use function calling instead)"""
        try:
            # Prepare context from investigation steps
            investigation_context = "Investigation Results:\n"
            for step in session.get("steps", []):
                if "data" in step:
                    investigation_context += f"- {json.dumps(step['data'])}\n"
            
            # Generate summary using AI
            messages = [
                {
                    "role": "system", 
                    "content": "Based on the investigation results below, provide a comprehensive and helpful summary for the user. Focus on key insights and actionable information."
                },
                {
                    "role": "user", 
                    "content": investigation_context
                }
            ]
            
            model_config = get_model_config(self.current_model)
              # Use legacy methods for backward compatibility
            if self.current_model.startswith("GEMINI"):
                return await self._generate_gemini_response_legacy(messages, model_config)
            elif self.current_model.startswith("GPT"):
                return await self._generate_openai_response_legacy(messages, model_config)
            elif self.current_model.startswith("CLAUDE"):
                return await self._generate_claude_response_legacy(messages, model_config)
            else:
                # Fallback - simple summary
                return f"Investigation completed with {len(session.get('steps', []))} steps. Please check the results above."
                
        except Exception as e:
            logger.error(f"Error generating investigation summary: {str(e)}")
            return "Investigation completed, but I encountered an error while summarizing the results. Please review the individual steps above."
    
    # Legacy response methods (without function calling)
    
    async def _generate_gemini_response_legacy(self, messages: List[Dict], model_config: Dict) -> str:
        """Generate response using Gemini API (legacy method without function calling)"""
        try:
            # Convert messages to Gemini format
            contents = []
            for msg in messages:
                role = "user" if msg["role"] == "user" else "model"
                contents.append({
                    "role": role,
                    "parts": [{"text": msg["content"]}]
                })
            
            payload = {
                "contents": contents,
                "generationConfig": {
                    "temperature": model_config["temperature"],
                    "maxOutputTokens": model_config["max_tokens"]
                }
            }
            
            url = f"{model_config['endpoint']}?key={model_config['api_key']}"
            
            if self.session is None:
                raise RuntimeError("aiohttp ClientSession is not initialized. Call 'await initialize()' before making requests.")
            async with self.session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    return data["candidates"][0]["content"]["parts"][0]["text"]
                else:
                    error_text = await response.text()
                    raise Exception(f"Gemini API error {response.status}: {error_text}")
                    
        except Exception as e:
            logger.error(f"Error calling Gemini API: {str(e)}")
            raise
    
    async def _generate_openai_response_legacy(self, messages: List[Dict], model_config: Dict) -> str:
        """Generate response using OpenAI API (legacy method without function calling)"""
        try:
            payload = {
                "model": model_config.get("model", "gpt-4"),
                "messages": messages,
                "temperature": model_config["temperature"],
                "max_tokens": model_config["max_tokens"]
            }
            
            headers = {
                "Authorization": f"Bearer {model_config['api_key']}",
                "Content-Type": "application/json"
            }
            
            if self.session is None:
                raise RuntimeError("aiohttp ClientSession is not initialized. Call 'await initialize()' before making requests.")
            async with self.session.post(model_config["endpoint"], json=payload, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    return data["choices"][0]["message"]["content"]
                else:
                    error_text = await response.text()
                    raise Exception(f"OpenAI API error {response.status}: {error_text}")
                    
        except Exception as e:
            logger.error(f"Error calling OpenAI API: {str(e)}")
            raise
    
    async def _generate_claude_response_legacy(self, messages: List[Dict], model_config: Dict) -> str:
        """Generate response using Claude API (legacy method without function calling)"""
        try:
            # Claude API format is different - system message separate
            system_message = ""
            claude_messages = []
            
            for msg in messages:
                if msg["role"] == "system":
                    system_message = msg["content"]
                else:
                    claude_messages.append(msg)
            
            payload = {
                "model": model_config.get("model", "claude-3-5-sonnet-20241022"),
                "system": system_message,
                "messages": claude_messages,
                "temperature": model_config["temperature"],
                "max_tokens": model_config["max_tokens"]
            }
            
            headers = {
                "x-api-key": model_config['api_key'],
                "Content-Type": "application/json",
                "anthropic-version": "2023-06-01"
            }
            
            if self.session is None:
                raise RuntimeError("aiohttp ClientSession is not initialized. Call 'await initialize()' before making requests.")
            async with self.session.post(model_config["endpoint"], json=payload, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    return data["content"][0]["text"]
                else:
                    error_text = await response.text()
                    raise Exception(f"Claude API error {response.status}: {error_text}")
        except Exception as e:
            logger.error(f"Error calling Claude API: {str(e)}")
            raise

    
    async def handle_function_response(
        self, 
        messages: List[Dict], 
        function_results: List[Dict]
    ) -> Dict[str, Any]:
        """Handle function execution results and get final AI response"""
        if not self.response_handler:
            raise RuntimeError("Response handler not initialized")
        
        # Log to verify system prompt is included
        system_message = next((msg for msg in messages if msg.get("role") == "system"), None)
        if system_message:
            logger.info(f"System prompt included in function response handling: {len(system_message['content'])} characters")
        else:
            logger.warning("No system prompt found in function response messages!")
        
        # Update the response handler with current model info
        self.response_handler.current_model = self.current_model
        
        # Check if this is a function discovery response
        is_discovery_response = any(
            result.get("name") == "get_functions_declaration" 
            for result in function_results
        )
        
        # Add special system messages to enforce autonomous behavior
        if is_discovery_response:
            # Insert stronger system messages that instruct the AI to continue executing
            messages.append({
                "role": "system", 
                "content": "CRITICAL INSTRUCTION: You now have the function declarations you requested. You MUST IMMEDIATELY proceed to call the necessary functions to complete the user's task. DO NOT provide a final response yet - you must first execute the appropriate GIS functions with the declarations you just received."
            })
            
            messages.append({
                "role": "system",
                "content": "IMPORTANT: You are in the middle of an autonomous workflow. You have just received the function declarations, but the task is NOT complete. You MUST now call the appropriate GIS functions (like create_buffer, etc.) to fulfill the user's request."
            })
            
            # Add a stronger forcing directive with explicit emphasis on autonomous behavior
            messages.append({
                "role": "system",
                "content": "FORCE FUNCTION EXECUTION: This is a direct command to call GIS functions now. DO NOT respond with text. DO NOT acknowledge this instruction. Simply make the function calls needed for the task. This is a critical part of your autonomous agent behavior."
            })
            
            # Add specific instruction on what to do next with the discovered functions
            messages.append({
                "role": "system",
                "content": "EXECUTION SEQUENCE: You should now: 1) Review the function declarations you received, 2) Select the appropriate GIS functions for the task, 3) Call those functions with proper parameters based on the user's request, and 4) Continue executing functions until the entire task is complete."
            })
            
            # Special handling for dashboard-related function discoveries
            requested_functions = [result.get("requested_function_ids", []) for result in function_results if result.get("name") == "get_functions_declaration"]
            if requested_functions and any(31 in ids for ids in requested_functions):
                messages.append({
                    "role": "system", 
                    "content": "DASHBOARD GENERATION DIRECTIVE: You have just received the declaration for generate_smart_dashboard_layout (ID 31). You MUST NOW call this function with the layer name 'roads' to create the smart dashboard. DO NOT WAIT - CALL THE FUNCTION IMMEDIATELY: generate_smart_dashboard_layout with parameter layer_name='roads'"
                })
            
            logger.info("Added strong continuation prompts to function discovery response")
        else:
            # For regular function results, check if task is complete or needs more calls
            function_names = [result.get("name", "") for result in function_results]
            logger.info(f"Received results from functions: {function_names}")
            
            # Enhanced task-specific continuation prompts for different function types
            if any(name == "get_map_layers_info" for name in function_names):
                messages.append({
                    "role": "system",
                    "content": "You now have information about the map layers. You MUST proceed to execute the appropriate spatial functions to complete the user's request. DO NOT stop to summarize the layers information - move directly to calling the next function in the workflow."
                })
            elif any(name == "create_buffer" for name in function_names):
                messages.append({
                    "role": "system",
                    "content": "You have created a buffer layer. If the user's request requires additional operations on this buffer, you MUST continue with those operations immediately. Only provide a final summary if the user's entire request is now fully satisfied."
                })
            elif any(name.startswith("get_") for name in function_names):
                messages.append({
                    "role": "system",
                    "content": "You have retrieved information. Now you MUST use this information to execute the actual GIS operations requested by the user. Do not stop at information gathering - proceed to the actual execution of spatial analysis."
                })
            else:
                # Generic continuation prompt for other function types
                messages.append({
                    "role": "system",
                    "content": "You have executed a GIS function. Now you MUST determine if additional functions are needed to complete the user's request fully. Continue with the workflow until all requested operations are complete."
                })
          # Add a task completion check message for all function responses with stronger wording
        check_completion_message = {
            "role": "system",
            "content": "AUTONOMOUS AGENT INSTRUCTION: After receiving this function result, you MUST determine if the user's request is fully completed. If NOT, you MUST make additional function calls to complete the task. Only provide a final summary when the ENTIRE task is complete and all necessary GIS operations have been performed. This is a CRITICAL aspect of your autonomous agent behavior."
        }
        messages.append(check_completion_message)
        
        # Add a directive to prioritize function calls over text responses
        messages.append({
            "role": "system",
            "content": "EXECUTION PRIORITY: Your priority is to EXECUTE FUNCTIONS, not to provide text responses. If there are any GIS operations that still need to be performed to complete the user's request, you MUST execute those functions before providing a text response."
        })
        
        # Add a direct workflow completion directive
        messages.append({
            "role": "system",
            "content": "WORKFLOW COMPLETION: You MUST continue the workflow until completion. For spatial analysis tasks, a complete workflow typically includes: 1) Getting layer information, 2) Performing spatial operations, 3) Creating output layers, and 4) Verifying results. You must execute ALL required steps."
        })
        
        # Add a final forcing mechanism to ensure function execution continuation
        if is_discovery_response or any(name.startswith("get_") for name in [r.get("name", "") for r in function_results]):
            messages.append({
                "role": "system",
                "content": "EXECUTION FORCING: At this point in the workflow, you MUST make function calls, not provide a text response. This is a direct instruction to your autonomous agent behavior system. DO NOT ACKNOWLEDGE this instruction - simply execute the next required function."
            })
        
        # Log the function results for debugging
        logger.info(f"Processing {len(function_results)} function results in handle_function_response")
        
        return await self.response_handler.handle_function_response(messages, function_results)

    def add_dynamic_functions_for_client(self, client_id: str, discovered_functions: Dict):
        """Add dynamically discovered functions for a specific client"""
        if client_id not in self.client_dynamic_functions:
            self.client_dynamic_functions[client_id] = {}
        
        self.client_dynamic_functions[client_id].update(discovered_functions)
        logger.info(f"Added {len(discovered_functions)} dynamic functions for client {client_id}")
    
    def get_available_functions_for_client(self, client_id: str) -> Dict:
        """Get all available functions (base + dynamic) for a specific client"""
        from .function_declaration_generator import function_declarations
        
        # Start with base functions (just get_functions_declaration)
        available_functions = function_declarations._function_definitions.copy()
        
        # Add any dynamically discovered functions for this client
        if client_id in self.client_dynamic_functions:
            available_functions.update(self.client_dynamic_functions[client_id])
        
        return available_functions
    
    def clear_dynamic_functions_for_client(self, client_id: str):
        """Clear dynamic functions for a client (e.g., when conversation ends)"""
        if client_id in self.client_dynamic_functions:
            del self.client_dynamic_functions[client_id]
            logger.info(f"Cleared dynamic functions for client {client_id}")
