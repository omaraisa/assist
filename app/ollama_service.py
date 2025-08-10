"""
Ollama Service for ArcGIS Pro Smart Assistant
Handles local LLM interactions through Ollama API
"""

import aiohttp
import json
import logging
from typing import Dict, List, Optional, Any
from .config import settings

logger = logging.getLogger(__name__)

class OllamaService:
    """Service for interacting with Ollama local LLMs"""
    
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url
        self.session = None
        self.available_models = []
        
    async def initialize(self):
        """Initialize Ollama service"""
        try:
            self.session = aiohttp.ClientSession()
            
            # Check if Ollama is running and get available models
            await self._check_connection()
            await self._load_available_models()
            
            logger.info(f"Ollama service initialized with {len(self.available_models)} models")
            
        except Exception as e:
            logger.error(f"Failed to initialize Ollama service: {e}")
            raise
    
    async def cleanup(self):
        """Cleanup resources"""
        if self.session:
            await self.session.close()
    
    async def _check_connection(self):
        """Check if Ollama is running"""
        try:
            async with self.session.get(f"{self.base_url}/api/tags") as response:
                if response.status == 200:
                    logger.info("Successfully connected to Ollama")
                    return True
                else:
                    raise Exception(f"Ollama returned status {response.status}")
                    
        except Exception as e:
            logger.error(f"Cannot connect to Ollama at {self.base_url}: {e}")
            raise Exception(f"Ollama is not running at {self.base_url}. Please start Ollama with 'ollama serve'")
    
    async def _load_available_models(self):
        """Load list of available models from Ollama"""
        try:
            async with self.session.get(f"{self.base_url}/api/tags") as response:
                if response.status == 200:
                    data = await response.json()
                    self.available_models = [model["name"] for model in data.get("models", [])]
                    logger.info(f"Found Ollama models: {self.available_models}")
                else:
                    logger.warning("Could not load Ollama models")
                    
        except Exception as e:
            logger.error(f"Error loading Ollama models: {e}")
    
    def get_available_models(self) -> List[str]:
        """Get list of available models"""
        return self.available_models
    
    async def generate_response(
        self, 
        messages: List[Dict], 
        model: str = "llama3.1:8b",
        temperature: float = 0.7,
        max_tokens: int = 2000
    ) -> Dict[str, Any]:
        """Generate response using Ollama model"""
        try:
            # Convert messages to Ollama format
            prompt = self._convert_messages_to_prompt(messages)
            
            # Prepare request data
            request_data = {
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": temperature,
                    "num_predict": max_tokens,
                }
            }
            
            # Make request to Ollama
            async with self.session.post(
                f"{self.base_url}/api/generate",
                json=request_data,
                headers={"Content-Type": "application/json"}
            ) as response:
                
                if response.status == 200:
                    data = await response.json()
                    
                    return {
                        "type": "text",
                        "content": data.get("response", ""),
                        "model": model,
                        "usage": {
                            "prompt_tokens": len(prompt.split()),
                            "completion_tokens": len(data.get("response", "").split()),
                            "total_tokens": len(prompt.split()) + len(data.get("response", "").split())
                        }
                    }
                else:
                    error_text = await response.text()
                    raise Exception(f"Ollama API error {response.status}: {error_text}")
                    
        except Exception as e:
            logger.error(f"Error generating Ollama response: {e}")
            return {
                "type": "error",
                "content": f"Error generating response with Ollama: {str(e)}",
                "model": model
            }
    
    def _convert_messages_to_prompt(self, messages: List[Dict]) -> str:
        """Convert OpenAI-style messages to a single prompt for Ollama"""
        prompt_parts = []
        
        for message in messages:
            role = message.get("role", "")
            content = message.get("content", "")
            
            if role == "system":
                prompt_parts.append(f"System: {content}")
            elif role == "user":
                prompt_parts.append(f"Human: {content}")
            elif role == "assistant":
                prompt_parts.append(f"Assistant: {content}")
        
        # Add final prompt for assistant response
        prompt_parts.append("Assistant:")
        
        return "\n\n".join(prompt_parts)
    
    async def generate_with_functions(
        self, 
        messages: List[Dict], 
        functions: List[Dict],
        model: str = "llama3.2:latest"
    ) -> Dict[str, Any]:
        """Generate response with function calling capability"""
        try:
            logger.info(f"Generating Ollama response with functions for model: {model}")
            
            # Add function definitions to system message
            system_message = self._create_function_calling_prompt(messages, functions)
            
            logger.info(f"Created function calling prompt with {len(system_message)} messages")
            
            # Generate response
            response = await self.generate_response(system_message, model)
            
            logger.info(f"Generated response type: {response.get('type', 'unknown')}")
            
            # Check if response contains function calls
            if response["type"] == "text":
                function_calls = self._parse_function_calls(response["content"])
                if function_calls:
                    logger.info(f"Parsed {len(function_calls)} function calls")
                    return {
                        "type": "function_calls",
                        "function_calls": function_calls,
                        "model": model
                    }
            
            return response
            
        except Exception as e:
            logger.error(f"Error generating Ollama response with functions: {e}", exc_info=True)
            return {
                "type": "error",
                "content": f"Error generating function response: {str(e)}",
                "model": model
            }
    
    def _create_function_calling_prompt(self, messages: List[Dict], functions: List[Dict]) -> List[Dict]:
        """Create a prompt that includes function definitions for function calling"""
          # Create function descriptions
        function_descriptions = []
        for func in functions:
            # Handle OpenAI function format (nested structure)
            if func.get('type') == 'function' and 'function' in func:
                func_def = func['function']
                func_name = func_def['name']
                func_description = func_def['description']
                func_parameters = func_def.get('parameters', {})
            else:
                # Handle direct function format
                func_name = func['name']
                func_description = func['description']
                func_parameters = func.get('parameters', {})
            
            func_desc = f"Function: {func_name}\n"
            func_desc += f"Description: {func_description}\n"
            
            if 'properties' in func_parameters:
                func_desc += "Parameters:\n"
                for param, details in func_parameters['properties'].items():
                    required = param in func_parameters.get('required', [])
                    func_desc += f"  - {param} ({'required' if required else 'optional'}): {details.get('description', '')}\n"
            
            function_descriptions.append(func_desc)
        
        # Add simple function calling instructions to system message
        function_prompt = (
            "You have access to the following functions. "
            "When you need to call a function, respond with a JSON object in this format: "
            '{ "function_calls": [ { "name": "function_name", "arguments": { ... } } ] }\n\n'
            "Do not write any extra text or explanations. Just output the JSON function call.\n\n"
            "Available functions:\n\n" + "\n\n".join(function_descriptions)
        )
        
        # Modify the system message to include function calling instructions
        modified_messages = []
        system_found = False
        
        for message in messages:
            if message["role"] == "system" and not system_found:
                modified_messages.append({
                    "role": "system",
                    "content": message["content"] + "\n\n" + function_prompt
                })
                system_found = True
            else:
                modified_messages.append(message)
        
        # If no system message found, add one
        if not system_found:
            modified_messages.insert(0, {
                "role": "system",
                "content": function_prompt
            })
        
        return modified_messages
    
    def _parse_function_calls(self, response_text: str) -> List[Dict]:
        """Parse function calls from response text"""
        function_calls = []
        
        try:
            import re
            json_pattern = r'(\{.*?"function_calls".*?\})'
            matches = re.findall(json_pattern, response_text, re.DOTALL)

            for match in matches:
                try:
                    parsed = json.loads(match)
                    if "function_calls" in parsed:
                        function_calls.extend(parsed["function_calls"])
                except json.JSONDecodeError:
                    continue
            
            # Also try to parse the entire response as JSON
            if not function_calls:
                try:
                    parsed = json.loads(response_text.strip())
                    if "function_calls" in parsed:
                        function_calls.extend(parsed["function_calls"])
                except json.JSONDecodeError:
                    pass
            
            # Enhanced parsing for common AI response patterns
            if not function_calls:
                # Look for function call patterns like "Function: function_name(param="value")"
                function_pattern = r'Function:\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\(\s*([^)]*)\s*\)'
                matches = re.findall(function_pattern, response_text)
                
                for func_name, params_str in matches:
                    try:
                        # Parse parameters from string like 'layer_name="District"'
                        params = {}
                        if params_str.strip():
                            # Simple parameter parsing for key="value" format
                            param_pattern = r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*["\']([^"\']*)["\']'
                            param_matches = re.findall(param_pattern, params_str)
                            for key, value in param_matches:
                                params[key] = value
                        
                        function_calls.append({
                            "name": func_name,
                            "arguments": params
                        })
                        logger.info(f"Parsed function call from text pattern: {func_name}")
                    except Exception as e:
                        logger.error(f"Error parsing function parameters: {e}")
                        
        except Exception as e:
            logger.error(f"Error parsing function calls: {e}")
        
        return function_calls
    
    async def handle_function_response(
        self, 
        messages: List[Dict], 
        function_results: List[Dict],
        model: str = "llama3.1:8b"
    ) -> Dict[str, Any]:
        """Handle function execution results and generate final response"""
        try:
            # Add function results to messages
            modified_messages = messages.copy()
            
            # Add function results as a user message
            results_text = "Function execution results:\n\n"
            for result in function_results:
                results_text += f"Function: {result.get('name', 'unknown')}\n"
                results_text += f"Result: {json.dumps(result.get('result', {}), indent=2)}\n\n"
            
            results_text += "Based on these results, please provide a clear, user-friendly response that summarizes the findings and answers the user's question."
            
            modified_messages.append({
                "role": "user",
                "content": results_text
            })
            
            # Generate final response
            return await self.generate_response(modified_messages, model)
            
        except Exception as e:
            logger.error(f"Error handling function response: {e}")
            return {
                "type": "error",
                "content": f"Error processing function results: {str(e)}",
                "model": model
            }
