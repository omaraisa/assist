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
    ) -> Dict[str, Any]:
        """Generate AI response with function calling support"""
        try:
            logger.info(f"Generating response for model: {self.current_model}")
            logger.info(f"User message: {user_message[:100]}...")
            
            model_config = get_model_config(self.current_model)
            logger.info(f"Model config retrieved for: {model_config.get('name', 'unknown')}")
            
            # Prepare messages with all available functions
            messages = self._prepare_messages(
                user_message, 
                conversation_history, 
                arcgis_state            )
            
            logger.info(f"Messages prepared, count: {len(messages)}")
            
            # Generate response based on model type with function calling
            if self.current_model.startswith("GEMINI"):
                logger.info("Using Gemini model")
                return await self.response_handler._generate_gemini_response_with_functions(messages, model_config, user_message)
            elif self.current_model.startswith("GPT"):
                logger.info("Using OpenAI model")
                return await self.response_handler._generate_openai_response_with_functions(messages, model_config, user_message)
            elif self.current_model.startswith("CLAUDE"):
                logger.info("Using Claude model")
                return await self.response_handler._generate_claude_response_with_functions(messages, model_config, user_message)
            elif self.current_model.startswith("OLLAMA"):
                if not OLLAMA_AVAILABLE:
                    logger.warning("Ollama model requested but Ollama service is not available")
                    return {
                        "type": "error",
                        "content": "Ollama service is not available. Please check if Ollama server is running or use a different AI model.",
                        "model": self.current_model
                    }
                logger.info("Using Ollama model")
                return await self.response_handler._generate_ollama_response_with_functions(messages, model_config, user_message)
            else:
                raise ValueError(f"Unsupported model: {self.current_model}")
                
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
        arcgis_state: Dict
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

You have access to various GIS functions that you can call to analyze spatial data, perform calculations, and retrieve information. Use these functions to provide accurate, data-driven responses.

FUNCTION DISCOVERY:
Before you can use any spatial functions, you MUST first call the `get_functions_declaration` function to discover what functions are available. This function returns the signatures and descriptions of the specific functions you can call.

AVAILABLE FUNCTIONS (by ID):
{functions_list}

WORKFLOW:
1. For any user request involving GIS operations, FIRST call `get_functions_declaration` with the function IDs you think you need
2. Once you have the function signatures, then call the specific functions to perform the analysis
3. Always start by calling `get_functions_declaration` with relevant function IDs based on the user's request

Key Guidelines:
1. Always use function calls to gather information before providing answers
2. Never invent or hallucinate data - only use information from function results
3. If layer names or field names mentioned by the user don't match the ArcGIS state, ask for clarification
4. In analysis the output layer name will always be the same as the input layer name with "_ai" appended. For example, if the input layer is "cities", the output layer will be "cities_ai", if you used this layer again as input the output name will be "cities_ai_ai". 
5. Be precise and factual in your responses
6. If you cannot fulfill a request, explain why politely
7. If the function result contains layer not found error then use get_map_layers_info to get the current layers in the ArcGIS Pro project and run the failed function again with the correct layer name. If the layer is not found in the ArcGIS Pro project, ask the user to provide the correct layer name or add it to the project.
8. When you receive function results, ALWAYS provide a clear, concise, and user-friendly summary or answer based on the results. DO NOT simply repeat or dump the raw function result or JSON. Synthesize the information into a natural, helpful response for the user.

Current ArcGIS Pro State: {json.dumps(simplified_state)}

EXAMPLE WORKFLOW:
User: "Create a buffer around schools"
1. First call: get_functions_declaration([8, 21]) // 8=create_buffer, 21=get_map_layers_info  
2. Then call: get_map_layers_info() to see available layers
3. Finally call: create_buffer(layer_name="schools", distance=1000, units="meters")

When you need to analyze data or perform spatial operations, follow this workflow and use the available functions. Provide clear, informative responses based on the actual results."""

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
        
        return await self.response_handler.handle_function_response(messages, function_results)
