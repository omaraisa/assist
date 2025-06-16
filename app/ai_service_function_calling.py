import asyncio
import json
import re
import logging
from typing import Dict, List, Optional, Any
import aiohttp
from .config import settings, get_model_config
from .function_declarations import openai_functions, gemini_functions, claude_tools, functions_summary

logger = logging.getLogger(__name__)

class AIService:
    """Service for handling AI model interactions with function calling support"""
    
    def __init__(self):
        self.current_model = settings.DEFAULT_AI_MODEL
        self.session = None
    
    async def initialize(self):
        """Initialize the AI service"""
        self.session = aiohttp.ClientSession()
        logger.info(f"AI Service initialized with model: {self.current_model}")
    
    async def cleanup(self):
        """Cleanup resources"""
        if self.session:
            await self.session.close()
    
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
        available_functions: str = None  # Legacy parameter, now unused
    ) -> Dict[str, Any]:
        """Generate AI response with function calling support"""
        try:
            model_config = get_model_config(self.current_model)
            
            # Prepare the conversation context
            messages = self._prepare_messages(
                user_message, 
                conversation_history, 
                arcgis_state
            )
            
            # Generate response based on model type with function calling
            if self.current_model.startswith("GEMINI"):
                return await self._generate_gemini_response_with_functions(messages, model_config)
            elif self.current_model.startswith("GPT"):
                return await self._generate_openai_response_with_functions(messages, model_config)
            elif self.current_model.startswith("CLAUDE"):
                return await self._generate_claude_response_with_functions(messages, model_config)
            else:
                raise ValueError(f"Unsupported model: {self.current_model}")
                
        except Exception as e:
            logger.error(f"Error generating AI response: {str(e)}")
            return {
                "type": "text",
                "content": f"I apologize, but I encountered an error while processing your request: {str(e)}. Please try again."
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

    # Function calling methods for each AI provider
    
    async def _generate_openai_response_with_functions(self, messages: List[Dict], model_config: Dict) -> Dict[str, Any]:
        """Generate OpenAI response with function calling support"""
        try:
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
    
    async def _generate_gemini_response_with_functions(self, messages: List[Dict], model_config: Dict) -> Dict[str, Any]:
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
    
    async def _generate_claude_response_with_functions(self, messages: List[Dict], model_config: Dict) -> Dict[str, Any]:
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
    
    # Function execution and response handling methods
    
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
        """Handle OpenAI function calling response"""
        # Add assistant message with tool calls
        assistant_message = {
            "role": "assistant",
            "content": None,
            "tool_calls": []
        }
        
        # Add tool call results as user messages
        for result in function_results:
            assistant_message["tool_calls"].append({
                "id": result["id"],
                "type": "function",
                "function": {
                    "name": result["name"],
                    "arguments": json.dumps(result["parameters"])
                }
            })
            
            messages.append({
                "role": "tool",
                "tool_call_id": result["id"],
                "content": json.dumps(result["result"])
            })
        
        messages.append(assistant_message)
        
        # Get final response
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
        
        async with self.session.post(model_config["endpoint"], json=payload, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return {
                    "type": "text",
                    "content": data["choices"][0]["message"]["content"]
                }
            else:
                error_text = await response.text()
                raise Exception(f"OpenAI API error {response.status}: {error_text}")
    
    async def _handle_gemini_function_response(
        self, 
        messages: List[Dict], 
        function_results: List[Dict], 
        model_config: Dict
    ) -> Dict[str, Any]:
        """Handle Gemini function calling response"""
        # Convert messages to Gemini format and add function responses
        contents = []
        for msg in messages:
            role = "user" if msg["role"] == "user" else "model"
            contents.append({
                "role": role,
                "parts": [{"text": msg["content"]}]
            })
        
        # Add function call results
        function_response_parts = []
        for result in function_results:
            function_response_parts.append({
                "functionResponse": {
                    "name": result["name"],
                    "response": result["result"]
                }
            })
        
        contents.append({
            "role": "user",
            "parts": function_response_parts
        })
        
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
        
        async with self.session.post(url, json=payload) as response:
            if response.status == 200:
                data = await response.json()
                candidate = data["candidates"][0]
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
                raise Exception(f"Gemini API error {response.status}: {error_text}")
    
    async def _handle_claude_function_response(
        self, 
        messages: List[Dict], 
        function_results: List[Dict], 
        model_config: Dict
    ) -> Dict[str, Any]:
        """Handle Claude function calling response"""
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
            tool_result_content.append({
                "type": "tool_result",
                "tool_use_id": result["id"],
                "content": json.dumps(result["result"])
            })
        
        claude_messages.append({
            "role": "user",
            "content": tool_result_content
        })
        
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
        
        async with self.session.post(model_config["endpoint"], json=payload, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                content = data["content"]
                
                text_content = ""
                for item in content:
                    if item["type"] == "text":
                        text_content += item["text"]
                
                return {
                    "type": "text",
                    "content": text_content
                }
            else:
                error_text = await response.text()
                raise Exception(f"Claude API error {response.status}: {error_text}")

    def _get_model_identity(self) -> str:
        """Get model-specific identity string"""
        if self.current_model.startswith("GEMINI"):
            return "Gemini AI (Google)"
        elif self.current_model.startswith("GPT"):
            return "GPT (OpenAI)"
        elif self.current_model.startswith("CLAUDE"):
            return "Claude (Anthropic)"
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
