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
        self.client_dynamic_functions = {}
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
            execution_mode = self.websocket_manager.get_execution_mode(client_id)
            logger.info(f"Generating response for client {client_id} in '{execution_mode}' mode.")

            if execution_mode == 'expert':
                # Expert mode: Generate raw Python code for any model
                return await self.generate_expert_code_response(user_message, conversation_history, arcgis_state, client_id)
            
            # Safe mode: Use function calling for all models
            logger.info(f"Generating response for model: {self.current_model} in Safe Mode")
            logger.info(f"User message: {user_message[:100]}...")

            # Safe mode: Use LangChain agent for all models
            logger.info(f"Generating response for model: {self.current_model} in Safe Mode")

            response = await self.langchain_agent.generate_response(
                user_message,
                conversation_history,
                arcgis_state,
                client_id
            )

            logger.info(f"AI generated response type: {response.get('type')}")

            # Sanitize the response content
            if "content" in response and isinstance(response["content"], str):
                from .security import sanitize_output
                response["content"] = sanitize_output(response["content"])

            return response

        except Exception as e:
            logger.error(f"Error generating AI response: {str(e)}", exc_info=True)
            return {
                "type": "error",
                "content": f"Error generating response: {str(e)}",
                "model": self.current_model
            }    
            
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

    def _get_expert_mode_system_prompt(self, arcgis_state: Dict) -> str:
        """Get the system prompt for expert mode, instructing the AI to return raw Python code."""
        simplified_state = self._simplify_arcgis_state(arcgis_state)
        return (
            "You are an expert-level GIS Python programming assistant for ArcGIS Pro. "
            "Your task is to respond to the user's request by generating a single, complete, and executable Python script. "
            "DO NOT use function calls or tools. You MUST write the full Python code to accomplish the task. "
            "The code will be executed directly in the ArcGIS Pro Python environment. "
            "Assume standard libraries like 'arcpy' are available. "
            "Enclose the final Python code in a single markdown block: ```python\n[your code here]\n```. "
            "Do not include any other text, explanations, or apologies outside of this code block. "
            "\n\n--- SECURITY GUIDELINES ---\n"
            "1.  **Do not** write code that reveals the file system structure, lists files, or reads file contents, unless explicitly asked by the user for a specific, non-sensitive file.\n"
            "2.  **Do not** write code that reveals API keys, secrets, or any other sensitive configuration details.\n"
            "3.  **Do not** write code that modifies or deletes files on the user's system without explicit confirmation.\n"
            "4.  **Do not** write code that makes network requests to unknown or untrusted domains.\n"
            "5.  **Always** prioritize user data privacy and security.\n"
            f"Current ArcGIS Pro state: {json.dumps(simplified_state)}"
        )

    async def generate_expert_code_response(
        self,
        user_message: str,
        conversation_history: List[Dict],
        arcgis_state: Dict,
        client_id: str
    ) -> Dict[str, Any]:
        """Generates a raw Python code response from the AI in expert mode."""
        logger.info("Generating expert mode code response.")

        system_prompt = self._get_expert_mode_system_prompt(arcgis_state)
        messages = [{"role": "system", "content": system_prompt}]
        for msg in conversation_history[-10:]:
            if msg["role"] != "system":
                messages.append(msg)

        # This is a simplified call that doesn't use the full _prepare_messages logic
        # because we don't want the function calling prompts.
        messages.append({"role": "user", "content": user_message})

        model_config = get_model_config(self.current_model)

        # We need to call the underlying AI handlers but without providing tools
        # to force a text-based response.
        text_response = ""
        # This logic is simplified. A real implementation might need to adapt the handlers.
        # For now, let's assume a simplified path for text generation.
        # This is a placeholder for what would be a more complex call.
        # A proper implementation would likely involve creating new methods in the response
        # handler like `_generate_openai_text_response`.

        # For now, we'll just get a text response. This part of the code is simplified for brevity.
        # Let's mock a text response generation for now.
        # In a real scenario, you'd call the respective API for a text-only response.
        from .ai.ai_response_handler import AIResponseHandler
        handler = AIResponseHandler(self.session, None)

        # This is a conceptual simplification. The actual API calls would be more direct.
        # We'll just get the text content from the response.
        response_data = {}
        if self.current_model.startswith("GPT"):
            payload = { "model": model_config.get("model"), "messages": messages, "temperature": model_config["temperature"], "max_tokens": model_config["max_tokens"] }
            headers = { "Authorization": f"Bearer {model_config['api_key']}", "Content-Type": "application/json" }
            async with self.session.post(model_config["endpoint"], json=payload, headers=headers) as response:
                if response.status == 200:
                    response_data = await response.json()
                    text_response = response_data["choices"][0]["message"]["content"]
                else:
                    raise Exception(f"OpenAI API error {response.status}: {await response.text()}")

        elif self.current_model.startswith("CLAUDE"):
             payload = { "model": model_config.get("model"), "messages": messages, "temperature": model_config["temperature"], "max_tokens": model_config["max_tokens"], "system": system_prompt }
             headers = { "x-api-key": model_config['api_key'], "Content-Type": "application/json", "anthropic-version": "2023-06-01" }
             async with self.session.post(model_config["endpoint"], json=payload, headers=headers) as response:
                if response.status == 200:
                    response_data = await response.json()
                    text_response = response_data["content"][0]["text"]
                else:
                    raise Exception(f"Claude API error {response.status}: {await response.text()}")

        # Extract code from the response
        code_match = re.search(r"```python\n(.*?)\n```", text_response, re.DOTALL)
        extracted_code = code_match.group(1).strip() if code_match else ""

        if not extracted_code:
            logger.warning("Expert mode response did not contain a Python code block.")
            # If no code block, we might take the whole response as code, or handle as an error
            extracted_code = text_response.strip()

        from .security import sanitize_output
        return {
            "type": "expert_code",
            "code": sanitize_output(extracted_code),
            "original_content": sanitize_output(text_response)
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
