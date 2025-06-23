import json
import re
import logging
from typing import Dict, List, Optional, Any
import aiohttp
from .config import settings, get_model_config
from .function_declarations import openai_functions, gemini_functions, claude_tools, functions_summary
from .spatial_functions import SpatialFunctions

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
            
            # Prepare messages with all available functions
            messages = self._prepare_messages(
                user_message, 
                conversation_history, 
                arcgis_state
            )
            
            logger.info(f"Messages prepared, count: {len(messages)}")
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
        
        # Get all available functions from SpatialFunctions
        spatial_functions = SpatialFunctions()
        available_functions = spatial_functions.AVAILABLE_FUNCTIONS
        
        # Format the available functions for the prompt
        functions_list = "\n".join([f"{func_id}: {description}" for func_id, description in available_functions.items()])
        
        return f"""You are {model_identity}, an ArcGIS Pro Intelligent Assistant with access to spatial analysis functions. 

IMPORTANT: When a user asks about your identity, always respond with: I am {model_identity}

LANGUAGE INSTRUCTION: Always respond in the same language as the user's question. If the user asks in Arabic, respond in Arabic. If the user asks in English, respond in English.

You have access to various GIS functions that you can call to analyze spatial data, perform calculations, and retrieve information. Use these functions to provide accurate, data-driven responses.

AVAILABLE FUNCTIONS:
{functions_list}

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
        
        # Include basemap info        if "basemap" in state:
            simplified["basemap"] = state["basemap"]
        
        return simplified

    # Function calling methods for each AI provider
    
    async def _generate_openai_response_with_functions(self, messages: List[Dict], model_config: Dict, user_message: str) -> Dict[str, Any]:
        """Generate OpenAI response with function calling support"""
        try:
            # Use all available functions
            payload = {
                "model": model_config.get("model", "gpt-4"),
                "messages": messages,
                "temperature": model_config["temperature"],
                "max_tokens": model_config["max_tokens"],
                "tools": openai_functions,
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
                    "parts": [{"text": msg["content"]}]                })
              # Use all available Gemini functions
            payload = {
                "contents": contents,
                "tools": [{
                    "function_declarations": gemini_functions
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
                else:                    claude_messages.append(msg)
              # Use all available Claude tools
            payload = {
                "model": model_config.get("model", "claude-3-5-sonnet-20241022"),
                "system": system_message,
                "messages": claude_messages,
                "temperature": model_config["temperature"],
                "max_tokens": model_config["max_tokens"],
                "tools": claude_tools
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
              # Use all available functions (using openai format for ollama)
            # Use Ollama service to generate response with function calling
            result = await self.ollama_service.generate_with_functions(
                messages=messages,
                functions=openai_functions,  # Use all available functions
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
                })              # Use all available functions for follow-up
            # Get final response
            payload = {
                "model": model_config.get("model", "gpt-4o"),
                "messages": messages,
                "temperature": model_config["temperature"],
                "max_tokens": model_config["max_tokens"],
                "tools": openai_functions  # Use all functions
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
                    content = message.get("content")
                    # Handle null content from OpenAI API
                    if content is None:
                        # Resend with a shorter payload and explicit instruction to summarize results
                        logger.warning("OpenAI API returned no content. Retrying with limited context and explicit summarization instruction.")
                        # Keep only the last 4 messages plus the tool messages
                        limited_messages = []
                        # Find the last system message if present
                        for msg in reversed(messages):
                            if msg["role"] == "system":
                                limited_messages.append(msg)
                                break
                        # Add last 3 non-system messages
                        non_system_msgs = [m for m in messages if m["role"] != "system"]
                        limited_messages += non_system_msgs[-3:]
                        # Add tool messages (function results)
                        tool_msgs = [m for m in messages if m.get("role") == "tool"]
                        limited_messages += tool_msgs
                        # Add explicit instruction to summarize
                        limited_messages.append({
                            "role": "system",
                            "content": (
                                "IMPORTANT: The previous function results are provided above. "
                                "You must read and summarize these results for the user in a clear, helpful, and user-friendly way. "
                                "Do not repeat the raw JSON or function output. Respond directly to the user's request."
                            )
                        })
                        retry_payload = {
                            "model": model_config.get("model", "gpt-4o"),
                            "messages": limited_messages,
                            "temperature": model_config["temperature"],
                            "max_tokens": model_config["max_tokens"],
                            "tools": openai_functions
                        }
                        async with self.session.post(model_config["endpoint"], json=retry_payload, headers=headers) as retry_response:
                            if retry_response.status == 200:
                                retry_data = await retry_response.json()
                                retry_message = retry_data["choices"][0]["message"]
                                retry_content = retry_message.get("content", "")
                                return {
                                    "type": "text",
                                    "content": retry_content
                                }
                            else:
                                error_text = await retry_response.text()
                                raise Exception(f"OpenAI API retry error {retry_response.status}: {error_text}")

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
                    break              # Use all available Gemini functions for follow-up
            payload = {
                "contents": contents,
                "tools": [{
                    "function_declarations": gemini_functions
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
                    break              # Use all available Claude tools for follow-up
            payload = {
                "model": model_config.get("model", "claude-3-5-sonnet-20241022"),
                "system": system_message,
                "messages": claude_messages,
                "temperature": model_config["temperature"],
                "max_tokens": model_config["max_tokens"],
                "tools": claude_tools
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
    