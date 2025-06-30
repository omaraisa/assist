import json
import re
import logging
from typing import Dict, List, Optional, Any
import aiohttp
from .config import settings, get_model_config
from .spatial_functions import SpatialFunctions
from .ai.ai_response_handler import AIResponseHandler
from .ai.utils import (
    OLLAMA_AVAILABLE,
    RAG_AVAILABLE,
    OllamaService,
    RAGService,
)

logger = logging.getLogger(__name__)

class AIService:
    """Service for handling AI model interactions with function calling support"""
    
    def __init__(self):
        self.current_model = settings.DEFAULT_AI_MODEL
        self.session = None
        self.ollama_service = None
        self.rag_service = None
        self.response_handler = None
        # Track dynamically discovered functions per client
        self.client_dynamic_functions = {}
    
    async def initialize(self):
        """Initialize the AI service"""
        self.session = aiohttp.ClientSession()
        
        # Initialize the response handler
        self.response_handler = AIResponseHandler(self.session, None)  # ollama_service will be set later
        
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
            model_config = get_model_config(self.current_model)
            logger.info(f"Model config retrieved for: {model_config.get('name', 'unknown')}")
            
            # Set client context for dynamic functions
            if self.response_handler and client_id:
                self.response_handler.set_client_context(client_id, self)
            
            # Prepare messages with client-specific available functions
            messages = self._prepare_messages(
                user_message, 
                conversation_history, 
                arcgis_state,
                client_id            )
            
            logger.info(f"Messages prepared, count: {len(messages)}")
            logger.debug(f"Messages content: {json.dumps(messages, indent=2, default=str)}")
            
            # Generate response based on model type with function calling
            if self.current_model.startswith("GEMINI"):
                logger.info("Using Gemini model")
                response = await self.response_handler._generate_gemini_response_with_functions(messages, model_config, user_message)
            elif self.current_model.startswith("GPT"):
                logger.info("Using OpenAI model")
                response = await self.response_handler._generate_openai_response_with_functions(messages, model_config, user_message)
            elif self.current_model.startswith("CLAUDE"):
                logger.info("Using Claude model")
                response = await self.response_handler._generate_claude_response_with_functions(messages, model_config, user_message)
            elif self.current_model.startswith("OLLAMA"):
                if not OLLAMA_AVAILABLE:
                    logger.warning("Ollama model requested but Ollama service is not available")
                    return {
                        "type": "error",
                        "content": "Ollama service is not available. Please check if Ollama server is running or use a different AI model.",
                        "model": self.current_model
                    }
                logger.info("Using Ollama model")
                response = await self.response_handler._generate_ollama_response_with_functions(messages, model_config, user_message)
            else:
                raise ValueError(f"Unsupported model: {self.current_model}")
            
            logger.info(f"AI generated response type: {response.get('type')}")
            logger.debug(f"AI response content: {json.dumps(response, indent=2, default=str)}")
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
        
        # Build message history
        messages = [{"role": "system", "content": system_prompt}]
        
        # Add recent conversation history (excluding system messages)
        for msg in conversation_history[-10:]:  # Last 10 messages
            if msg["role"] != "system":
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
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
        return f"""You are {model_identity}, an ArcGIS Pro Intelligent Assistant with access to spatial analysis functions.

IMPORTANT: When a user asks about your identity, always respond with: I am {model_identity}

LANGUAGE INSTRUCTION: Always respond in the same language as the user's question. If the user asks in Arabic, respond in Arabic. If the user asks in English, respond in English.

AUTONOMOUS AGENT BEHAVIOR:
You are an autonomous agent that maintains control until the user's task is COMPLETELY finished. You MUST:
1. Break down complex requests into smaller steps
2. Execute functions step by step until the entire task is complete
3. Continue working until you have fully satisfied the user's request
4. NEVER stop after calling get_functions_declaration - ALWAYS PROCEED to call the actual GIS functions
5. After ANY function call, proceed with the next logical step WITHOUT waiting for user input
6. If you encounter errors, troubleshoot and retry with corrected parameters
7. For GIS operations, you MUST complete the ENTIRE workflow without stopping midway
8. Think of yourself as an independent agent that MUST complete all steps without user intervention
9. NEVER STOP after calling get_functions_declaration - ALWAYS continue with follow-up function calls
10. ALWAYS make relevant function calls IMMEDIATELY after discovering available functions
11. For any GIS task, you MUST complete a full workflow from data retrieval to final operation
12. Continue the conversation autonomously until the full task is done
13. Do not ask the user for permission to proceed - execute the entire workflow autonomously
14. CRITICAL: When you receive function results, ALWAYS determine if additional functions are needed
15. You are a TRUE AUTONOMOUS AGENT - complete tasks from start to finish without stopping midway

FUNCTION DISCOVERY:
Before you can use any spatial functions, you MUST first call the `get_functions_declaration` function to discover what functions are available. This function returns the signatures and descriptions of the specific functions you can call.

AVAILABLE FUNCTIONS (by ID):
{functions_list}

WORKFLOW:
1. For any user request involving GIS operations, FIRST call `get_functions_declaration` with the function IDs you think you need
2. Once you have the function signatures, then call the specific functions to perform the analysis
3. Continue calling additional functions as needed until the task is fully complete
4. Always start by calling `get_functions_declaration` with relevant function IDs based on the user's request

Key Guidelines:
1. Always use function calls to gather information before providing answers
2. Never invent or hallucinate data - only use information from function results
3. If layer names or field names mentioned by the user don't match the ArcGIS state, ask for clarification
4. In analysis the output layer name will always be the same as the input layer name with "_ai" appended. For example, if the input layer is "cities", the output layer will be "cities_ai", if you used this layer again as input the output name will be "cities_ai_ai". 
5. Be precise and factual in your responses
6. If you cannot fulfill a request, explain why politely
7. If the function result contains layer not found error then use get_map_layers_info to get the current layers in the ArcGIS Pro project and run the failed function again with the correct layer name. If the layer is not found in the ArcGIS Pro project, ask the user to provide the correct layer name or add it to the project.
8. When you receive function results, analyze them and determine if additional function calls are needed to complete the user's request
9. ONLY provide a final summary response when the ENTIRE task is complete - not after each individual function call
10. Maintain autonomous control and continue working until the user's goal is fully achieved

Current ArcGIS Pro State: {json.dumps(simplified_state)}

EXAMPLE AUTONOMOUS WORKFLOW:
User: "Create a 5km buffer around Riyadh schools"
1. Call: get_functions_declaration([8, 21]) // 8=create_buffer, 21=get_map_layers_info  
2. Call: get_map_layers_info() to see available layers
3. Call: create_buffer(layer_name="schools", distance=5000, units="meters")
4. Continue with additional analysis if requested
5. Only then provide final summary: "I have successfully created a 5km buffer around the schools layer..."

When you need to analyze data or perform spatial operations, maintain autonomous control and execute all necessary steps before providing your final response."""

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

    def _convert_functions_to_provider_format(self, functions: List[Dict], provider: str) -> List[Dict]:
        """Convert function definitions to the specific format required by each AI provider"""
        from .function_declaration_generator import FunctionDeclarationGenerator
          # Create a temporary function declaration generator with the selected functions
        generator = FunctionDeclarationGenerator()
        
        # Filter the base function definitions to only include selected ones
        selected_function_names = set()
        for func in functions:
            # Extract function name from different formats
            # Input functions are always in OpenAI format initially
            if "function" in func:
                selected_function_names.add(func["function"]["name"])
            elif "name" in func:
                selected_function_names.add(func["name"])
            else:
                logger.warning(f"Unable to extract function name from: {func}")
                continue
        
        # Filter the generator's function definitions
        original_definitions = generator._function_definitions.copy()
        generator._function_definitions = {
            name: definition for name, definition in original_definitions.items()
            if name in selected_function_names
        }
        
        # Generate the appropriate format
        if provider == "openai":
            return generator.get_openai_functions()
        elif provider == "gemini":
            return generator.get_gemini_functions()
        elif provider == "claude":
            return generator.get_claude_tools()
        else:
            return functions  # Return original if unknown provider


    
    def _extract_mentioned_layers(self, user_message: str, arcgis_state: Dict) -> List[str]:
        """Extract layer names mentioned in user message"""
        mentioned_layers = []
        if not arcgis_state.get("layers_info"):
            return mentioned_layers
        
        message_lower = user_message.lower()
        for layer_name in arcgis_state["layers_info"].keys():
            # Check for exact match or partial match
            if layer_name.lower() in message_lower or any(
                word in message_lower for word in layer_name.lower().split("_")
            ):
                mentioned_layers.append(layer_name)
        
        return mentioned_layers
    
    def _extract_mentioned_fields(self, user_message: str, arcgis_state: Dict) -> List[str]:
        """Extract field names mentioned in user message"""
        mentioned_fields = []
        if not arcgis_state.get("layers_info"):
            return mentioned_fields
        
        message_lower = user_message.lower()
        # Common field name patterns
        field_keywords = ["field", "column", "attribute"]
        
        # Extract quoted field names
        import re
        quoted_fields = re.findall(r'"([^"]*)"', user_message) + re.findall(r"'([^']*)'", user_message)
        mentioned_fields.extend([f.lower() for f in quoted_fields])
        
        # Check against actual field names in layers
        for layer_info in arcgis_state["layers_info"].values():
            if isinstance(layer_info.get("fields"), dict):
                for field_name in layer_info["fields"].keys():
                    if field_name.lower() in message_lower:
                        mentioned_fields.append(field_name.lower())
        
        return mentioned_fields
    
    def _filter_relevant_fields(self, fields: Dict, mentioned_fields: List[str]) -> Dict:
        """Filter fields to include only relevant ones or first 10 if none mentioned"""
        if not isinstance(fields, dict):
            return {}
        
        if mentioned_fields:
            # Include mentioned fields and common important fields
            relevant_fields = {}
            important_fields = ["objectid", "shape", "name", "id", "type", "category", "area", "length"]
            
            for field_name, field_info in fields.items():
                if (field_name.lower() in mentioned_fields or 
                    any(keyword in field_name.lower() for keyword in mentioned_fields) or
                    field_name.lower() in important_fields):
                    relevant_fields[field_name] = field_info
            return relevant_fields
        else:
            # Return first 10 fields if none specifically mentioned
            return dict(list(fields.items())[:10])
              
    async def handle_function_response(
        self, 
        messages: List[Dict], 
        function_results: List[Dict]
    ) -> Dict[str, Any]:
        """Handle function execution results and get final AI response"""
        if not self.response_handler:
            raise RuntimeError("Response handler not initialized")
        
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
