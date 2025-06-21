import asyncio
import json
import re
import logging
from typing import Dict, List, Optional, Any, Tuple
import aiohttp
from .config import settings, get_model_config
from .function_declarations import openai_functions, gemini_functions, claude_tools, functions_summary

logger = logging.getLogger(__name__)

# Import Ollama and RAG services with better error handling
OLLAMA_AVAILABLE = False
RAG_AVAILABLE = False
OllamaService = None
RAGService = None

def _test_ollama_server():
    """Test if Ollama server is running and accessible"""
    try:
        import requests
        from .config import settings
        
        # Test if Ollama server is running
        response = requests.get(f"{settings.OLLAMA_BASE_URL}/api/tags", timeout=5)
        return response.status_code == 200
    except Exception as e:
        logger.info(f"Ollama server test failed: {e}")
        return False

# Test Ollama server first
if _test_ollama_server():
    try:
        from .ollama_service import OllamaService
        OLLAMA_AVAILABLE = True
        logger.info("Ollama service imported successfully - server is accessible")
    except ImportError as e:
        logger.warning(f"Ollama service import failed: {e}")
        OllamaService = None
else:
    logger.info("Ollama server not accessible - skipping Ollama service import")
    OllamaService = None

try:
    from .rag_service import RAGService
    RAG_AVAILABLE = True
    logger.info("RAG service imported successfully")
except ImportError as e:
    logger.warning(f"RAG service not available: {e}")
    RAGService = None

logger.info(f"Services available - Ollama: {OLLAMA_AVAILABLE}, RAG: {RAG_AVAILABLE}")

class AIService:
    """Service for handling AI model interactions with function calling support"""
    
    def __init__(self):
        self.current_model = settings.DEFAULT_AI_MODEL
        self.session = None
        self.ollama_service = None
        self.rag_service = None
    
    async def initialize(self):
        """Initialize the AI service"""
        self.session = aiohttp.ClientSession()
          # Initialize Ollama service if available
        logger.info(f"OLLAMA_AVAILABLE: {OLLAMA_AVAILABLE}")
        if OLLAMA_AVAILABLE and OllamaService is not None:
            try:
                logger.info(f"Initializing Ollama service at: {settings.OLLAMA_BASE_URL}")
                self.ollama_service = OllamaService(settings.OLLAMA_BASE_URL)
                await self.ollama_service.initialize()
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
        available_functions: Optional[str] = None  # Legacy parameter, now unused
    ) -> Dict[str, Any]:
        """Generate AI response with function calling support"""
        try:
            logger.info(f"Generating response for model: {self.current_model}")
            logger.info(f"User message: {user_message[:100]}...")
            
            model_config = get_model_config(self.current_model)
            logger.info(f"Model config retrieved for: {model_config.get('name', 'unknown')}")
            
            # Classify user intent for optimizations
            intent = self._classify_user_intent(user_message)
            logger.info(f"User intent classified as: {intent}")
            
            # Prepare optimized messages with intent-based payload reduction
            messages = self._prepare_optimized_messages(
                user_message, 
                conversation_history, 
                arcgis_state,
                intent
            )
            
            logger.info(f"Optimized messages prepared, count: {len(messages)}")
              # Generate response based on model type with function calling
            if self.current_model.startswith("GEMINI"):
                logger.info("Using Gemini model")
                return await self._generate_gemini_response_with_functions(messages, model_config, user_message)
            elif self.current_model.startswith("GPT"):
                logger.info("Using OpenAI model")
                return await self._generate_openai_response_with_functions(messages, model_config, user_message)
            elif self.current_model.startswith("CLAUDE"):
                logger.info("Using Claude model")
                return await self._generate_claude_response_with_functions(messages, model_config, user_message)
            elif self.current_model.startswith("OLLAMA"):
                if not OLLAMA_AVAILABLE:
                    logger.warning("Ollama model requested but Ollama service is not available")
                    return {
                        "type": "error",
                        "content": "Ollama service is not available. Please check if Ollama server is running or use a different AI model.",
                        "model": self.current_model
                    }
                logger.info("Using Ollama model")
                return await self._generate_ollama_response_with_functions(messages, model_config, user_message)
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
        
        return f"""You are {model_identity}, an ArcGIS Pro Intelligent Assistant with access to spatial analysis functions. 

IMPORTANT: When a user asks about your identity, always respond with: I am {model_identity}

LANGUAGE INSTRUCTION: Always respond in the same language as the user's question. If the user asks in Arabic, respond in Arabic. If the user asks in English, respond in English.

You have access to various GIS functions that you can call to analyze spatial data, perform calculations, and retrieve information. Use these functions to provide accurate, data-driven responses.

Key Guidelines:
1. Always use function calls to gather information before providing answers
2. Never invent or hallucinate data - only use information from function results
3. If layer names or field names mentioned by the user don't match the ArcGIS state, ask for clarification
4. Be precise and factual in your responses
5. If you cannot fulfill a request, explain why politely
6. When you receive function results, ALWAYS provide a clear, concise, and user-friendly summary or answer based on the results. DO NOT simply repeat or dump the raw function result or JSON. Synthesize the information into a natural, helpful response for the user.

Current ArcGIS Pro State: {json.dumps(simplified_state)}

When you need to analyze data or perform spatial operations, use the available functions. Provide clear, informative responses based on the actual results."""

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

    def _get_essential_openai_functions(self) -> List[Dict]:
        """Get essential OpenAI functions to reduce token usage"""
        # Essential function names for common operations
        essential_names = [
            "get_layer_summary",
            "get_field_statistics", 
            "select_by_attribute",
            "select_by_location",
            "calculate_area",
            "calculate_length",
            "get_centroid",
            "create_buffer",
            "get_unique_values_count"
        ]
        
        # Filter to include only essential functions
        essential_functions = []
        for func in openai_functions:
            if func["function"]["name"] in essential_names:
                essential_functions.append(func)
        
        return essential_functions

    def _classify_user_intent(self, user_message: str) -> str:
        """Classify user intent to determine which function category is needed"""
        message_lower = user_message.lower()
        
        # Intent classification based on keywords and patterns
        # LAYER_INFO: Questions about layers, data sources, structure
        layer_info_keywords = [
            "what layers", "layer info", "layer summary", "data source", "coordinate system",
            "what data", "available layers", "layer type", "layer structure", "map layers",
            "show layers", "list layers", "layer details", "what is this layer"
        ]
        
        # FIELD_ANALYSIS: Questions about fields, attributes, statistics
        field_analysis_keywords = [
            "field", "attribute", "column", "statistics", "unique values", "frequency",
            "values in", "domain", "empty values", "null values", "data types",
            "field definitions", "attribute table", "distinct values", "count of"
        ]
        
        # SELECTION: Operations to select features
        selection_keywords = [
            "select", "find", "filter", "where", "choose", "pick", "subset",
            "features with", "records with", "spatial selection", "location",
            "intersect", "within", "contains", "overlaps"
        ]
        
        # SPATIAL_ANALYSIS: Spatial calculations and analysis
        spatial_analysis_keywords = [
            "area", "length", "distance", "buffer", "centroid", "spatial join",
            "clip", "nearest", "spatial analysis", "geometry", "geographic",
            "calculate area", "calculate length", "create buffer", "spatial relationship"
        ]
        
        # DATA_OPERATIONS: Data manipulation and calculations
        data_operations_keywords = [
            "calculate field", "new field", "add field", "update field", "modify",
            "attribute table", "table data", "edit data", "field calculation"
        ]
        
        # SYSTEM: System information and paths
        system_keywords = [
            "project path", "database path", "default database", "system info",
            "workspace", "geodatabase", "file location"
        ]
        
        # Count matches for each category
        intent_scores = {
            "LAYER_INFO": sum(1 for keyword in layer_info_keywords if keyword in message_lower),
            "FIELD_ANALYSIS": sum(1 for keyword in field_analysis_keywords if keyword in message_lower),
            "SELECTION": sum(1 for keyword in selection_keywords if keyword in message_lower),
            "SPATIAL_ANALYSIS": sum(1 for keyword in spatial_analysis_keywords if keyword in message_lower),
            "DATA_OPERATIONS": sum(1 for keyword in data_operations_keywords if keyword in message_lower),
            "SYSTEM": sum(1 for keyword in system_keywords if keyword in message_lower)
        }
        
        # Find the intent with highest score
        max_score = max(intent_scores.values())
        if max_score == 0:
            return "GENERAL"  # No specific intent detected, use general functions
        
        # Return the intent with highest score
        for intent, score in intent_scores.items():
            if score == max_score:
                return intent
                
        return "GENERAL"

    def _get_functions_by_intent(self, intent: str) -> List[Dict]:
        """Get relevant functions based on classified intent"""
        
        # Function categories mapping
        function_categories = {
            "LAYER_INFO": [
                "get_layer_summary", "get_layer_type", "get_data_source_info", 
                "get_map_layers_info", "get_map_tables_info", "get_coordinate_system"
            ],
            "FIELD_ANALYSIS": [
                "get_field_statistics", "get_field_definitions", "get_unique_values_count",
                "get_values_frequency", "get_value_frequency", "calculate_empty_values",
                "get_field_domain_values", "get_attribute_table"
            ],
            "SELECTION": [
                "select_by_attribute", "select_by_location", "get_layer_summary",
                "get_field_statistics", "get_unique_values_count"  # Support functions for selection
            ],
            "SPATIAL_ANALYSIS": [
                "calculate_area", "calculate_length", "get_centroid", "create_buffer",
                "calculate_distance", "spatial_join", "clip_layer", "create_nearest_neighbor_layer"
            ],
            "DATA_OPERATIONS": [
                "calculate_new_field", "get_attribute_table", "get_field_definitions",
                "get_field_statistics", "get_unique_values_count"
            ],
            "SYSTEM": [
                "get_current_project_path", "get_default_db_path"
            ],
            "GENERAL": [
                # Most commonly used functions for general queries
                "get_layer_summary", "get_field_statistics", "select_by_attribute",
                "select_by_location", "calculate_area", "get_unique_values_count",
                "get_map_layers_info", "create_buffer", "get_attribute_table"
            ]
        }
        
        # Get function names for the intent
        relevant_function_names = function_categories.get(intent, function_categories["GENERAL"])
        
        # Filter OpenAI functions to include only relevant ones
        relevant_functions = []
        for func in openai_functions:
            if func["function"]["name"] in relevant_function_names:
                relevant_functions.append(func)
        
        return relevant_functions    
    

    def _get_intelligent_function_selection(self, user_message: str, provider_format: str = "openai") -> Tuple[List[Dict], str]:
        """Intelligently select functions based on user intent classification"""
        # Classify the user's intent
        intent = self._classify_user_intent(user_message)
        
        # Get relevant functions for the intent
        relevant_functions = self._get_functions_by_intent(intent)
        
        # Convert to appropriate provider format if needed
        if provider_format != "openai":
            relevant_functions = self._convert_functions_to_provider_format(relevant_functions, provider_format)
        
        # Log the intelligent selection for debugging
        logger.info(f"Intent classified as: {intent}")
        logger.info(f"Selected {len(relevant_functions)} functions out of {len(openai_functions)} total")
        
        return relevant_functions, intent
    
    def _convert_functions_to_provider_format_simple(self, openai_functions: List[Dict], provider: str) -> List[Dict]:
        """Convert OpenAI function format to provider-specific format (simple version)"""
        if provider == "gemini":
            # Convert to Gemini function format
            gemini_functions = []
            for func in openai_functions:
                openai_func = func["function"]
                gemini_func = {
                    "name": openai_func["name"],
                    "description": openai_func["description"],
                    "parameters": openai_func["parameters"]
                }
                gemini_functions.append(gemini_func)
            return gemini_functions
        
        elif provider == "claude":
            # Convert to Claude tool format
            claude_tools = []
            for func in openai_functions:
                openai_func = func["function"]
                claude_tool = {
                    "name": openai_func["name"],
                    "description": openai_func["description"],
                    "input_schema": openai_func["parameters"]
                }
                claude_tools.append(claude_tool)
            return claude_tools
        
        # Default return OpenAI format
        return openai_functions

    # Function calling methods for each AI provider      
    
    async def _generate_openai_response_with_functions(self, messages: List[Dict], model_config: Dict, user_message: str) -> Dict[str, Any]:
        """Generate OpenAI response with function calling support"""
        try:
            # Use intelligent function selection to reduce token usage
            selected_functions, intent = self._get_intelligent_function_selection(user_message)
            
            payload = {
                "model": model_config.get("model", "gpt-4"),
                "messages": messages,
                "temperature": model_config["temperature"],
                "max_tokens": model_config["max_tokens"],
                "tools": selected_functions,
                "tool_choice": "auto"
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
                    message = data["choices"][0]["message"]
                    
                    # Check if AI wants to call functions
                    if message.get("tool_calls"):
                        return {
                            "type": "function_calls",
                            "function_calls": message["tool_calls"],
                            "content": message.get("content", "")
                        }
                    else:
                        return {
                            "type": "text",
                            "content": message["content"]
                        }
                else:
                    error_text = await response.text()
                    raise Exception(f"OpenAI API error {response.status}: {error_text}")
                    
        except Exception as e:
            logger.error(f"Error calling OpenAI API: {str(e)}")
            raise
    async def _generate_gemini_response_with_functions(self, messages: List[Dict], model_config: Dict, user_message: str = "") -> Dict[str, Any]:
        """Generate Gemini response with function calling support"""
        try:
            # Convert messages to Gemini format
            contents = []
            for msg in messages:
                role = "user" if msg["role"] == "user" else "model"
                contents.append({
                    "role": role,
                    "parts": [{"text": msg["content"]}]
                })
              # Get intelligent function selection
            selected_functions, user_intent = self._get_intelligent_function_selection(user_message, "gemini")
            
            payload = {
                "contents": contents,
                "tools": [{
                    "function_declarations": selected_functions
                }],
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
                    candidate = data["candidates"][0]
                    content = candidate["content"]
                    
                    # Check if AI wants to call functions
                    if "parts" in content:
                        function_calls = []
                        text_content = ""
                        
                        for part in content["parts"]:
                            if "functionCall" in part:
                                function_calls.append(part["functionCall"])
                            elif "text" in part:
                                text_content += part["text"]
                        
                        if function_calls:
                            return {
                                "type": "function_calls",
                                "function_calls": function_calls,
                                "content": text_content
                            }
                        else:
                            return {
                                "type": "text",
                                "content": text_content
                            }
                    else:
                        return {
                            "type": "text",
                            "content": ""
                        }
                else:
                    error_text = await response.text()
                    raise Exception(f"Gemini API error {response.status}: {error_text}")
                    
        except Exception as e:
            logger.error(f"Error calling Gemini API: {str(e)}")
            raise
    async def _generate_claude_response_with_functions(self, messages: List[Dict], model_config: Dict, user_message: str = "") -> Dict[str, Any]:
        """Generate Claude response with function calling support"""
        try:
            # Claude API format - system message separate
            system_message = ""
            claude_messages = []
            
            for msg in messages:
                if msg["role"] == "system":
                    system_message = msg["content"]
                else:
                    claude_messages.append(msg)
              # Get intelligent function selection
            selected_functions, user_intent = self._get_intelligent_function_selection(user_message, "claude")
            
            payload = {
                "model": model_config.get("model", "claude-3-5-sonnet-20241022"),
                "system": system_message,
                "messages": claude_messages,
                "temperature": model_config["temperature"],
                "max_tokens": model_config["max_tokens"],
                "tools": selected_functions
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
                    content = data["content"]
                    
                    # Check if AI wants to call functions
                    function_calls = []
                    text_content = ""
                    
                    for item in content:
                        if item["type"] == "tool_use":
                            function_calls.append({
                                "id": item["id"],
                                "name": item["name"],
                                "input": item["input"]
                            })
                        elif item["type"] == "text":
                            text_content += item["text"]
                    
                    if function_calls:
                        return {
                            "type": "function_calls", 
                            "function_calls": function_calls,
                            "content": text_content
                        }
                    else:
                        return {
                            "type": "text",
                            "content": text_content
                        }
                else:
                    error_text = await response.text()
                    raise Exception(f"Claude API error {response.status}: {error_text}")
                    
        except Exception as e:
            logger.error(f"Error calling Claude API: {str(e)}")
            raise
      
    async def _generate_ollama_response_with_functions(self, messages: List[Dict], model_config: Dict, user_message: str = "") -> Dict[str, Any]:
        """Generate Ollama response with function calling support"""
        try:
            logger.info(f"Generating Ollama response with model: {model_config.get('model', 'unknown')}")
            
            if not self.ollama_service:
                logger.error("Ollama service not available")
                raise Exception("Ollama service not available")
            
            # Get the model name from config
            model_name = model_config.get("model", "llama3.2:latest")
            logger.info(f"Using Ollama model: {model_name}")
              # Get intelligent function selection (using openai format for ollama)
            selected_functions, user_intent = self._get_intelligent_function_selection(user_message, "openai")
            
            # Use Ollama service to generate response with function calling
            result = await self.ollama_service.generate_with_functions(
                messages=messages,
                functions=selected_functions,  # Use intelligent function selection instead of all functions
                model=model_name
            )
            
            logger.info(f"Ollama response type: {result.get('type', 'unknown')}")
            return result
            
        except Exception as e:
            logger.error(f"Error calling Ollama API: {str(e)}", exc_info=True)
            return {
                "type": "error",
                "content": f"Error with Ollama model: {str(e)}",
                "model": model_config.get("model", "ollama")
            }    # Function execution and response handling methods
    
    def parse_function_calls(self, response: Dict[str, Any]) -> List[Dict]:
        """Parse function calls from AI response into standardized format"""
        if response["type"] != "function_calls":
            return []
        
        function_calls = []
        
        if self.current_model.startswith("GPT"):
            # OpenAI format
            for tool_call in response["function_calls"]:
                if tool_call["type"] == "function":
                    function_calls.append({
                        "id": tool_call["id"],
                        "name": tool_call["function"]["name"],
                        "parameters": json.loads(tool_call["function"]["arguments"])
                    })
        
        elif self.current_model.startswith("GEMINI"):
            # Gemini format
            for func_call in response["function_calls"]:
                function_calls.append({
                    "id": f"gemini_{func_call['name']}_{len(function_calls)}",
                    "name": func_call["name"],
                    "parameters": func_call.get("args", {})
                })
        
        elif self.current_model.startswith("CLAUDE"):
            # Claude format
            for func_call in response["function_calls"]:
                function_calls.append({
                    "id": func_call["id"],
                    "name": func_call["name"],
                    "parameters": func_call["input"]
                })
        
        elif self.current_model.startswith("OLLAMA"):
            # Ollama format: function_calls is a list of dicts with name/arguments
            for idx, func_call in enumerate(response["function_calls"]):
                function_calls.append({
                    "id": f"ollama_{func_call.get('name', 'func')}_{idx}",
                    "name": func_call["name"],
                    "parameters": func_call.get("arguments", {})
                })
        
        return function_calls
    
    async def handle_function_response(
        self, 
        messages: List[Dict], 
        function_results: List[Dict]
    ) -> Dict[str, Any]:
        """Handle function execution results and get final AI response"""
        try:
            model_config = get_model_config(self.current_model)
            
            # Add function results to conversation
            if self.current_model.startswith("GPT"):
                return await self._handle_openai_function_response(messages, function_results, model_config)
            elif self.current_model.startswith("GEMINI"):
                return await self._handle_gemini_function_response(messages, function_results, model_config)
            elif self.current_model.startswith("CLAUDE"):
                return await self._handle_claude_function_response(messages, function_results, model_config)
            elif self.current_model.startswith("OLLAMA"):
                return await self._handle_ollama_function_response(messages, function_results, model_config)
            else:
                raise ValueError(f"Unsupported model: {self.current_model}")
                
        except Exception as e:
            logger.error(f"Error handling function response: {str(e)}")
            return {
                "type": "text",
                "content": f"I encountered an error processing the function results: {str(e)}"
            }
    
    async def _handle_openai_function_response(
        self, 
        messages: List[Dict], 
        function_results: List[Dict], 
        model_config: Dict
    ) -> Dict[str, Any]:
        """Handle OpenAI function calling response with proper message ordering"""
        try:
            # Add tool result messages - the assistant message with tool_calls should already be in history
            for result in function_results:
                # Ensure result content is properly formatted and not null
                result_content = result.get("result")
                if result_content is None:
                    result_content = {"success": True, "message": "Function executed successfully with no return value"}
                elif not isinstance(result_content, (dict, list, str, int, float, bool)):
                    result_content = {"success": True, "message": str(result_content)}
                
                messages.append({
                    "role": "tool",
                    "tool_call_id": result["id"],
                    "content": json.dumps(result_content)
                })
              # Use essential functions only for follow-up to save tokens
            essential_functions = self._get_essential_openai_functions()
            
            # Get final response
            payload = {
                "model": model_config.get("model", "gpt-4o"),
                "messages": messages,
                "temperature": model_config["temperature"],
                "max_tokens": model_config["max_tokens"],
                "tools": essential_functions  # Use reduced function set
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
                    message = data["choices"][0]["message"]
                    content = message.get("content")                    # Handle null content from OpenAI API
                    if content is None:
                        # Extract function results for fallback response
                        content = self._generate_fallback_response(function_results)                    
                    
                    else:
                        # Check if content looks like raw JSON or function result
                        if self._is_raw_function_result(content):
                            logger.info("Detected raw function result, generating user-friendly response")
                            content = self._generate_fallback_response(function_results)

                    return {
                        "type": "text",
                        "content": content
                    }
                else:
                    error_text = await response.text()
                    raise Exception(f"OpenAI API error {response.status}: {error_text}")
                    
        except Exception as e:
            logger.error(f"Error in OpenAI function response handling: {str(e)}")
            # Fallback to simple text response with function results
            results_summary = []
            for result in function_results:
                if isinstance(result.get("result"), dict) and result["result"].get("success"):
                    results_summary.append(f"✓ {result['name']}: {result['result'].get('summary', 'Completed successfully')}")
                else:
                    results_summary.append(f"✓ {result['name']}: Executed successfully")
            
            fallback_content = "I successfully executed the requested functions:\n\n" + "\n".join(results_summary)
            
            return {
                "type": "text",
                "content": fallback_content
            }

    async def _handle_gemini_function_response(
        self, 
        messages: List[Dict], 
        function_results: List[Dict], 
        model_config: Dict
    ) -> Dict[str, Any]:
        """Handle Gemini function calling response"""
        try:
          
            contents = []
            # Track whether we've found the assistant message with function calls
            found_function_call_message = False
            
            # Add all messages except potentially the last assistant message
            for i, msg in enumerate(messages):
                if msg["role"] == "system":
                    # Skip system messages in Gemini contents - they're in the system prompt
                    continue
                elif msg["role"] == "user":
                    contents.append({
                        "role": "user",
                        "parts": [{"text": msg["content"]}]
                    })
                elif msg["role"] == "assistant":
                    # For assistant messages, check if it has function_calls metadata
                    # This is crucial for Gemini API to properly match function calls with responses
                    
                    # If we have function_calls metadata, this is the message we need to handle specially
                    if "function_calls" in msg:
                        found_function_call_message = True
                        
                        # Build the function calls from the stored metadata
                        function_call_parts = []
                        
                        # Add any text content first
                        if msg.get("content"):
                            function_call_parts.append({"text": msg["content"]})
                        
                        # Add function calls based on the stored metadata
                        for func_call in msg["function_calls"]:
                            function_call_parts.append({
                                "functionCall": {
                                    "name": func_call["name"],
                                    "args": func_call.get("parameters", {})
                                }
                            })
                        
                        contents.append({
                            "role": "model",
                            "parts": function_call_parts
                        })
                    else:
                        # Regular assistant message
                        contents.append({
                            "role": "model",
                            "parts": [{"text": msg["content"]}]
                        })
            
            # If we didn't find a function call message, try to reconstruct it from the last assistant message
            # This is a fallback in case the metadata was not properly stored
            if not found_function_call_message and messages:
                for i in range(len(messages) - 1, -1, -1):
                    if messages[i]["role"] == "assistant":
                        # Get the last assistant message
                        last_assistant_msg = messages[i]
                        
                        # Build function calls from the results
                        function_call_parts = []
                        
                        # Add any text content first
                        if last_assistant_msg.get("content"):
                            function_call_parts.append({"text": last_assistant_msg["content"]})
                        
                        # Add function calls based on the results we received
                        for result in function_results:
                            function_call_parts.append({
                                "functionCall": {
                                    "name": result["name"],
                                    "args": result.get("parameters", {})
                                }
                            })
                        
                        # Replace the last model message or add a new one if needed
                        if any(item["role"] == "model" for item in contents):
                            # Find the last model message and replace it
                            for j in range(len(contents) - 1, -1, -1):
                                if contents[j]["role"] == "model":
                                    contents[j] = {
                                        "role": "model",
                                        "parts": function_call_parts
                                    }
                                    break
                        else:
                            # Add a new model message with function calls
                            contents.append({
                                "role": "model",
                                "parts": function_call_parts
                            })
                        
                        break
              # Now add the function responses that match the function calls
            # Ensure the order of function responses matches the order of function calls
            function_response_parts = []
            for result in function_results:
                # Ensure result is properly formatted for Gemini
                result_data = result.get("result")
                if result_data is None:
                    result_data = {"success": True, "message": "Function executed successfully with no return value"}
                elif not isinstance(result_data, (dict, list, str, int, float, bool)):
                    result_data = {"success": True, "message": str(result_data)}
                
                function_response_parts.append({
                    "functionResponse": {
                        "name": result["name"],
                        "response": result_data
                    }
                })
            
            # Add function responses as a user message
            contents.append({
                "role": "user",
                "parts": function_response_parts
            })
            
            # Log the constructed conversation
            logger.info(f"Gemini conversation with function calls: {json.dumps(contents, indent=2)}")
              # Extract user message from conversation for intelligent function selection
            user_message = ""
            for msg in reversed(messages):
                if msg["role"] == "user":
                    user_message = msg["content"]
                    break
            
            # Get intelligent function selection for this context
            selected_functions = self._get_intelligent_function_selection(user_message, "gemini")
            
            payload = {
                "contents": contents,
                "tools": [{
                    "function_declarations": selected_functions
                }],
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
                    
                    # Check for missing candidates
                    if "candidates" not in data or not data["candidates"]:
                        logger.error(f"No candidates in Gemini response: {json.dumps(data, indent=2)}")
                        raise Exception("Gemini API returned no candidates")
                    
                    candidate = data["candidates"][0]
                    
                    # Check for finish reason
                    if "finishReason" in candidate and candidate["finishReason"] != "STOP":
                        logger.warning(f"Gemini API finished with reason: {candidate['finishReason']}")
                      # Check for missing content or parts
                    if "content" not in candidate or "parts" not in candidate["content"]:
                        logger.error(f"Invalid Gemini response structure: {json.dumps(candidate, indent=2)}")
                        raise Exception("Invalid Gemini API response structure")
                    
                    content_parts = candidate["content"]["parts"]
                    
                    text_content = ""
                    for part in content_parts:
                        if "text" in part:
                            text_content += part["text"]
                    
                    return {
                        "type": "text",
                        "content": text_content
                    }
                else:
                    error_text = await response.text()
                    logger.error(f"Gemini API error: {error_text}")
                    logger.error(f"Payload sent: {json.dumps(payload, indent=2)}")
                    raise Exception(f"Gemini API error {response.status}: {error_text}")
                    
        except Exception as e:
            logger.error(f"Error in Gemini function response handling: {str(e)}")
            # Fallback to simple text response with function results
            results_summary = []
            for result in function_results:
                if isinstance(result.get("result"), dict) and result["result"].get("success"):
                    results_summary.append(f"✓ {result['name']}: {result['result'].get('summary', 'Completed successfully')}")
                else:
                    results_summary.append(f"✓ {result['name']}: Executed successfully")
            
            fallback_content = "I successfully executed the requested functions:\n\n" + "\n".join(results_summary)
            
            return {
                "type": "text",
                "content": fallback_content
            }
    async def _handle_claude_function_response(
        self, 
        messages: List[Dict], 
        function_results: List[Dict], 
        model_config: Dict
    ) -> Dict[str, Any]:
        """Handle Claude function calling response"""
        try:
            # Claude format - system message separate
            system_message = ""
            claude_messages = []
            
            for msg in messages:
                if msg["role"] == "system":
                    system_message = msg["content"]
                else:
                    claude_messages.append(msg)
            
            # Add function call results
            tool_result_content = []
            for result in function_results:
                # Ensure result content is properly formatted
                result_content = result.get("result")
                if result_content is None:
                    result_content = "Function executed successfully with no return value."
                elif isinstance(result_content, dict):
                    result_content = json.dumps(result_content)
                elif not isinstance(result_content, str):
                    result_content = str(result_content)
                
                tool_result_content.append({
                    "type": "tool_result",
                    "tool_use_id": result["id"],
                    "content": result_content
                })
            claude_messages.append({
                "role": "user",
                "content": tool_result_content
            })
            
            # Extract user message from conversation for intelligent function selection
            user_message = ""
            for msg in reversed(messages):
                if msg["role"] == "user":
                    user_message = msg["content"]
                    break
            
            # Get intelligent function selection for this context
            selected_functions = self._get_intelligent_function_selection(user_message, "claude")
            
            payload = {
                "model": model_config.get("model", "claude-3-5-sonnet-20241022"),
                "system": system_message,
                "messages": claude_messages,
                "temperature": model_config["temperature"],
                "max_tokens": model_config["max_tokens"],
                "tools": selected_functions
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
                    content = data["content"]
                    
                    text_content = ""
                    for item in content:
                        if item["type"] == "text":
                            text_content += item["text"]
                    
                    # Ensure we have some content
                    if not text_content:
                        # Extract function results for fallback response
                        results_summary = []
                        for result in function_results:
                            if isinstance(result.get("result"), dict) and result["result"].get("success"):
                                results_summary.append(f"✓ {result['name']}: {result['result'].get('summary', 'Completed successfully')}")
                            else:
                                results_summary.append(f"✓ {result['name']}: Executed successfully")
                        
                        text_content = "Based on the function results:\n\n" + "\n".join(results_summary)
                    
                    return {
                        "type": "text",
                        "content": text_content
                    }
                else:
                    error_text = await response.text()
                    logger.error(f"Claude API error: {error_text}")
                    logger.error(f"Payload sent: {json.dumps(payload, indent=2)}")
                    raise Exception(f"Claude API error {response.status}: {error_text}")
                    
        except Exception as e:
            logger.error(f"Error in Claude function response handling: {str(e)}")
            # Fallback to simple text response with function results
            results_summary = []
            for result in function_results:
                if isinstance(result.get("result"), dict) and result["result"].get("success"):
                    results_summary.append(f"✓ {result['name']}: {result['result'].get('summary', 'Completed successfully')}")
                else:
                    results_summary.append(f"✓ {result['name']}: Executed successfully")
            
            fallback_content = "I successfully executed the requested functions:\n\n" + "\n".join(results_summary)
            
            return {
                "type": "text",
                "content": fallback_content
            }

    async def _handle_ollama_function_response(
        self, 
        messages: List[Dict], 
        function_results: List[Dict], 
        model_config: Dict
    ) -> Dict[str, Any]:
        """Handle Ollama function calling response"""
        try:
            if not self.ollama_service:
                logger.error("Ollama service not available")
                raise Exception("Ollama service not available")
            
            # Get the model name from config
            model_name = model_config.get("model", "llama3.2:latest")
            logger.info(f"Handling Ollama function response with model: {model_name}")
              # Use Ollama service to handle function response
            result = await self.ollama_service.handle_function_response(
                messages=messages,
                function_results=function_results,
                model=model_name
            )
            
            return result
            
        except Exception as e:
            logger.error(f"Error in Ollama function response handling: {str(e)}")
            # Fallback to simple text response with function results
            results_summary = []
            for result in function_results:
                if isinstance(result.get("result"), dict) and result["result"].get("success"):
                    results_summary.append(f"✓ {result['name']}: {result['result'].get('summary', 'Completed successfully')}")
                else:
                    results_summary.append(f"✓ {result['name']}: Executed successfully")
            
            fallback_content = "I successfully executed the requested functions:\n\n" + "\n".join(results_summary)
            
            return {
                "type": "text",
                "content": fallback_content
            }

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
        from .function_declarations import FunctionDeclarationGenerator
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

# =======================
    # PHASE 1, STEP 2: ADVANCED ARCGIS STATE PAYLOAD REDUCTION
    # =======================
    
    def _get_relevant_arcgis_state_by_intent(self, intent: str, full_state: Dict, user_message: str) -> Dict:
        """Get only relevant ArcGIS state based on user intent to reduce token usage"""
        if not full_state:
            return {}
        
        # Extract layer names and field names mentioned in user message
        mentioned_layers = self._extract_mentioned_layers(user_message, full_state)
        mentioned_fields = self._extract_mentioned_fields(user_message, full_state)
        
        simplified = {}
        
        # Always include basic project info (minimal tokens)
        if "workspace" in full_state:
            simplified["workspace"] = full_state["workspace"]
        if "default_gdb" in full_state:
            simplified["default_gdb"] = full_state["default_gdb"]
        
        # Intent-specific state reduction
        if intent in ["LAYER_INFO", "GENERAL"]:
            # For layer info queries, include layer names and types only
            if "layers_info" in full_state:
                simplified["layers"] = {}
                for layer_name, layer_info in full_state["layers_info"].items():
                    # Only include layers mentioned in query or first 5 layers if none mentioned
                    if mentioned_layers and layer_name not in mentioned_layers:
                        continue
                    simplified["layers"][layer_name] = {
                        "type": layer_info.get("type", "Unknown"),
                        "feature_count": layer_info.get("feature_count", 0),
                        "geometry_type": layer_info.get("geometry_type", "Unknown")
                    }
                
                # If no specific layers mentioned, include only first 5 layers
                if not mentioned_layers and len(simplified["layers"]) == 0:
                    layer_names = list(full_state["layers_info"].keys())[:5]
                    for layer_name in layer_names:
                        layer_info = full_state["layers_info"][layer_name]
                        simplified["layers"][layer_name] = {
                            "type": layer_info.get("type", "Unknown"),
                            "feature_count": layer_info.get("feature_count", 0),
                            "geometry_type": layer_info.get("geometry_type", "Unknown")
                        }
        
        elif intent == "FIELD_ANALYSIS":
            # For field analysis, include relevant field information
            if "layers_info" in full_state:
                simplified["layers"] = {}
                for layer_name, layer_info in full_state["layers_info"].items():
                    # Include layer if mentioned or if fields are mentioned for this layer
                    include_layer = (not mentioned_layers or layer_name in mentioned_layers or
                                   any(field in str(layer_info.get("fields", {})).lower() for field in mentioned_fields))
                    
                    if include_layer:
                        simplified["layers"][layer_name] = {
                            "fields": self._filter_relevant_fields(layer_info.get("fields", {}), mentioned_fields),
                            "feature_count": layer_info.get("feature_count", 0)
                        }
        
        elif intent in ["SELECTION", "SPATIAL_ANALYSIS"]:
            # For selection and spatial analysis, include fields and geometry info
            if "layers_info" in full_state:
                simplified["layers"] = {}
                for layer_name, layer_info in full_state["layers_info"].items():
                    if not mentioned_layers or layer_name in mentioned_layers:
                        simplified["layers"][layer_name] = {
                            "fields": self._filter_relevant_fields(layer_info.get("fields", {}), mentioned_fields),
                            "geometry_type": layer_info.get("geometry_type", "Unknown"),
                            "feature_count": layer_info.get("feature_count", 0),
                            "definition_query": layer_info.get("definition_query", "")
                        }
        
        elif intent == "DATA_OPERATIONS":
            # For data operations, include field structure and attribute info
            if "layers_info" in full_state:
                simplified["layers"] = {}
                for layer_name, layer_info in full_state["layers_info"].items():
                    if not mentioned_layers or layer_name in mentioned_layers:
                        simplified["layers"][layer_name] = {
                            "fields": layer_info.get("fields", {}),
                            "feature_count": layer_info.get("feature_count", 0)
                        }
        
        elif intent == "SYSTEM":
            # For system queries, minimal info needed
            pass  # Already included workspace and default_gdb
        
        # Include layer types if available (small payload)
        if "layer_types" in full_state:
            if mentioned_layers:
                simplified["layer_types"] = {k: v for k, v in full_state["layer_types"].items() 
                                           if k in mentioned_layers}
            else:
                simplified["layer_types"] = dict(list(full_state["layer_types"].items())[:5])
        
        # Include basemap only for spatial analysis
        if intent == "SPATIAL_ANALYSIS" and "basemap" in full_state:
            simplified["basemap"] = full_state["basemap"]
        
        logger.info(f"Reduced ArcGIS state from {len(str(full_state))} to {len(str(simplified))} characters for intent: {intent}")
        return simplified
    
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
    
    # =======================
    # PHASE 1, STEP 3: CONVERSATION SUMMARIZATION
    # =======================
    
    def _optimize_conversation_history(self, conversation_history: List[Dict], user_message: str) -> List[Dict]:
        """Optimize conversation history to reduce token usage while preserving context"""
        if len(conversation_history) <= 6:
            return conversation_history  # No optimization needed for short conversations
        
        # Keep the most recent 4 messages always
        recent_messages = conversation_history[-4:]
        older_messages = conversation_history[:-4]
        
        # Summarize older messages if there are more than 6 total
        if len(older_messages) > 2:
            summarized_context = self._create_conversation_summary(older_messages, user_message)
            
            # Return summary + recent messages
            optimized_history = [
                {"role": "system", "content": f"Previous conversation summary: {summarized_context}"}
            ] + recent_messages
            
            logger.info(f"Compressed conversation from {len(conversation_history)} to {len(optimized_history)} messages")
            return optimized_history
        else:
            return conversation_history
    
    def _create_conversation_summary(self, messages: List[Dict], current_user_message: str) -> str:
        """Create a concise summary of conversation context"""
        if not messages:
            return "No previous context."
        
        # Extract key information from conversation
        topics = []
        layers_mentioned = set()
        operations_performed = []
        
        for msg in messages:
            if msg["role"] == "user":
                content = msg["content"].lower()
                  # Extract topics
                if any(word in content for word in ["layer", "map", "data"]):
                    topics.append("layer information")
                if any(word in content for word in ["field", "attribute", "column"]):
                    topics.append("field analysis")
                if any(word in content for word in ["select", "filter", "find"]):
                    topics.append("feature selection")
                if any(word in content for word in ["area", "buffer", "distance", "spatial"]):
                    topics.append("spatial analysis")
                if any(word in content for word in ["calculate", "compute", "count"]):
                    topics.append("calculations")
                
                # Extract layer names (basic pattern matching)
                words = content.split()
                for word in words:
                    if len(word) > 3 and not word in ["the", "and", "for", "with", "from", "this", "that"]:
                        if any(char.isupper() for char in word) or "_" in word:
                            layers_mentioned.add(word)
            
            elif msg["role"] == "assistant":
                content = msg["content"].lower()
                if "function" in content or "executed" in content:
                    operations_performed.append("data analysis")
        
        # Create concise summary
        summary_parts = []
        
        if topics:
            unique_topics = list(set(topics))
            summary_parts.append(f"Topics discussed: {', '.join(unique_topics[:3])}")
        
        if layers_mentioned:
            summary_parts.append(f"Layers referenced: {', '.join(list(layers_mentioned)[:3])}")
        
        if operations_performed:
            summary_parts.append(f"Operations: {', '.join(set(operations_performed))}")
        
        if not summary_parts:
            summary_parts.append("General GIS assistance conversation")
        
        return ". ".join(summary_parts) + "."
    
    # =======================
    # UPDATED MESSAGE PREPARATION WITH OPTIMIZATIONS
    # =======================
    
    def _prepare_optimized_messages(
        self, 
        user_message: str, 
        conversation_history: List[Dict], 
        arcgis_state: Dict,
        intent: str
    ) -> List[Dict]:
        """Prepare optimized messages with reduced payload for AI model"""
        
        # Get intent-specific ArcGIS state (Phase 1, Step 2)
        optimized_state = self._get_relevant_arcgis_state_by_intent(intent, arcgis_state, user_message)
        
        # Optimize conversation history (Phase 1, Step 3)
        optimized_history = self._optimize_conversation_history(conversation_history, user_message)
        
        # System prompt with optimized state
        system_prompt = self._get_optimized_system_prompt(optimized_state, intent)
        
        # Build message history
        messages = [{"role": "system", "content": system_prompt}]
        
        # Add optimized conversation history (excluding system messages)
        for msg in optimized_history:
            if msg["role"] != "system":
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
            elif "previous conversation summary" in msg["content"].lower():
                # Include conversation summary as assistant message for better context
                messages.append({
                    "role": "assistant", 
                    "content": f"Context: {msg['content']}"
                })
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        return messages
    
    def _get_optimized_system_prompt(self, optimized_state: Dict, intent: str) -> str:
        """Get optimized system prompt tailored to intent"""
        
        # Get model-specific identity
        model_identity = self._get_model_identity()
        
        # Intent-specific instructions
        intent_instructions = {
            "LAYER_INFO": "Focus on providing layer information, structure, and metadata.",
            "FIELD_ANALYSIS": "Focus on field analysis, statistics, and attribute information.",
            "SELECTION": "Focus on feature selection and filtering operations.",
            "SPATIAL_ANALYSIS": "Focus on spatial calculations, geometry operations, and geographic analysis.",
            "DATA_OPERATIONS": "Focus on data manipulation, field calculations, and attribute operations.",
            "SYSTEM": "Focus on system information and workspace details.",
            "GENERAL": "Provide comprehensive GIS assistance using available functions."
        }
        
        specific_instruction = intent_instructions.get(intent, intent_instructions["GENERAL"])
        
        return f"""You are {model_identity}, an ArcGIS Pro Intelligent Assistant with access to spatial analysis functions.

IMPORTANT: When a user asks about your identity, always respond with: I am {model_identity}

LANGUAGE INSTRUCTION: Always respond in the same language as the user's question.

Current Task Focus: {specific_instruction}

Key Guidelines:
1. Use function calls to gather information before providing answers
2. Never invent data - only use information from function results  
3. Be precise and factual in your responses
4. When you receive function results, provide a clear, user-friendly summary

Current ArcGIS Pro State: {json.dumps(optimized_state)}

Use the available functions to analyze data and provide accurate, helpful responses."""

    # =======================
    # UPDATED FUNCTION CALLING METHODS
    # =======================
    
    # ...existing code...
    
    def _generate_fallback_response(self, function_results: List[Dict]) -> str:
        """Generate a user-friendly fallback response from function results"""
        if not function_results:
            return "I processed your request successfully."
        
        # Process each function result
        responses = []
        for result in function_results:
            function_name = result.get("name", "unknown_function")
            result_data = result.get("result", {})
            
            # Generate specific responses based on function type
            if function_name == "get_map_layers_info":
                response = self._process_layers_info_result(result_data)
            elif function_name == "get_field_statistics":
                response = self._process_field_stats_result(result_data)
            elif function_name == "get_unique_values_count":
                response = self._process_unique_values_result(result_data)
            elif function_name == "select_by_attribute":
                response = self._process_selection_result(result_data)
            elif function_name == "calculate_area":
                response = self._process_area_calculation_result(result_data)
            else:
                # Generic processing for other functions
                response = self._process_generic_result(function_name, result_data)
            
            if response:
                responses.append(response)
        
        return "\n\n".join(responses) if responses else "I processed your request successfully."
    
    def _process_layers_info_result(self, result_data: Dict) -> str:
        """Process get_map_layers_info result into user-friendly text"""
        if not result_data.get("success"):
            return "I couldn't retrieve layer information from the map."
        
        layers = result_data.get("layers", [])
        if not layers:
            return "There are no layers currently loaded in the map."
        
        # Count different layer types
        layer_counts = {}
        visible_layers = []
        hidden_layers = []
        
        for layer in layers:
            layer_type = layer.get("type", "Unknown")
            layer_counts[layer_type] = layer_counts.get(layer_type, 0) + 1
            
            if layer.get("visible", True):
                visible_layers.append(layer["name"])
            else:
                hidden_layers.append(layer["name"])
        
        # Build response
        response_parts = [f"**Current Map Layers ({len(layers)} total):**"]
        
        # Layer summary by type
        if layer_counts:
            type_summary = []
            for layer_type, count in layer_counts.items():
                type_summary.append(f"{count} {layer_type.lower()} layer{'s' if count > 1 else ''}")
            response_parts.append(f"- {', '.join(type_summary)}")
        
        # Visible layers
        if visible_layers:
            response_parts.append(f"\n**Visible Layers ({len(visible_layers)}):**")
            for layer in visible_layers:
                layer_info = next((l for l in layers if l["name"] == layer), {})
                layer_type = layer_info.get("type", "Unknown")
                response_parts.append(f"- {layer} ({layer_type})")
        
        # Hidden layers (if any)
        if hidden_layers:
            response_parts.append(f"\n**Hidden Layers ({len(hidden_layers)}):**")
            for layer in hidden_layers:
                response_parts.append(f"- {layer}")
        
        return "\n".join(response_parts)
    
    def _process_field_stats_result(self, result_data: Dict) -> str:
        """Process field statistics result into user-friendly text"""
        if not result_data.get("success"):
            return "I couldn't retrieve field statistics."
        
        stats = result_data.get("statistics", {})
        field_name = result_data.get("field_name", "field")
        layer_name = result_data.get("layer_name", "layer")
        
        if not stats:
            return f"No statistics available for {field_name} in {layer_name}."
        
        response_parts = [f"**Statistics for {field_name} in {layer_name}:**"]
        
        # Format statistics based on field type
        if "count" in stats:
            response_parts.append(f"- Total records: {stats['count']:,}")
        if "unique_count" in stats:
            response_parts.append(f"- Unique values: {stats['unique_count']:,}")
        if "null_count" in stats:
            response_parts.append(f"- Null/empty values: {stats['null_count']:,}")
        if "min" in stats and "max" in stats:
            response_parts.append(f"- Range: {stats['min']} to {stats['max']}")
        if "mean" in stats:
            response_parts.append(f"- Average: {stats['mean']:.2f}")
        
        return "\n".join(response_parts)
    
    def _process_unique_values_result(self, result_data: Dict) -> str:
        """Process unique values result into user-friendly text"""
        if not result_data.get("success"):
            return "I couldn't retrieve unique values."

        
        unique_values = result_data.get("unique_values", [])
        field_name = result_data.get("field_name", "field")
        layer_name = result_data.get("layer_name", "layer")
        
        if not unique_values:
            return f"No unique values found for {field_name} in {layer_name}."
        
        response_parts = [f"**Unique values in {field_name} ({layer_name}):**"]
        response_parts.append(f"Total unique values: {len(unique_values)}")
        
        # Show first 10 values
        display_values = unique_values[:10]
        for value in display_values:
            response_parts.append(f"- {value}")
        
        if len(unique_values) > 10:
            response_parts.append(f"... and {len(unique_values) - 10} more values")
        
        return "\n".join(response_parts)
    
    def _process_selection_result(self, result_data: Dict) -> str:
        """Process selection result into user-friendly text"""
        if not result_data.get("success"):
            return "The selection operation was not successful."
        
        selected_count = result_data.get("selected_count", 0)
        layer_name = result_data.get("layer_name", "layer")
        
        if selected_count == 0:
            return f"No features were selected in {layer_name} with the specified criteria."
        elif selected_count == 1:
            return f"1 feature was selected in {layer_name}."
        else:
            return f"{selected_count:,} features were selected in {layer_name}."
    
    def _process_area_calculation_result(self, result_data: Dict) -> str:
        """Process area calculation result into user-friendly text"""
        if not result_data.get("success"):
            return "The area calculation was not successful."
        
        total_area = result_data.get("total_area", 0)
        unit = result_data.get("unit", "square units")
        layer_name = result_data.get("layer_name", "layer")
        feature_count = result_data.get("feature_count", 0)
        
        if feature_count == 0:
            return f"No features found for area calculation in {layer_name}."
        
        # Format area with appropriate units
        if "square meters" in unit.lower() or "sq m" in unit.lower():
            if total_area >= 1000000:  # Convert to km²
                area_km2 = total_area / 1000000
                return f"Total area of {feature_count:,} feature{'s' if feature_count > 1 else ''} in {layer_name}: {area_km2:.2f} km²"
            elif total_area >= 10000:  # Convert to hectares
                area_ha = total_area / 10000
                return f"Total area of {feature_count:,} feature{'s' if feature_count > 1 else ''} in {layer_name}: {area_ha:.2f} hectares"
        
        return f"Total area of {feature_count:,} feature{'s' if feature_count > 1 else ''} in {layer_name}: {total_area:,.2f} {unit}"
    
    def _process_generic_result(self, function_name: str, result_data: Dict) -> str:
        """Process generic function result into user-friendly text"""
        if not result_data.get("success"):
            return f"The {function_name.replace('_', ' ')} operation was not successful."
        
        # Check for common result patterns
        if "message" in result_data:
            return result_data["message"]
        elif "summary" in result_data:
            return result_data["summary"]
        elif "result" in result_data:
            return f"✓ {function_name.replace('_', ' ').title()}: {result_data['result']}"
        else:
            return f"✓ {function_name.replace('_', ' ').title()}: Completed successfully"
    
    def _is_raw_function_result(self, content: str) -> bool:
        """Check if content appears to be a raw function result that needs processing"""
        if not content:
            return False
        
        stripped = content.strip()
        
        # Check for JSON-like structure
        if (stripped.startswith('{') and stripped.endswith('}')) or (stripped.startswith('[') and stripped.endswith(']')):
            return True
        
        # Check for function result patterns
        if any(pattern in stripped for pattern in ['"success":', '"function_executed":', '"layers":', '"result":']):
            return True
        
        # Check if it's just repeating the raw function result
        if stripped.startswith("Based on the function results:") and "✓" in stripped:
            return True
        
        return False
