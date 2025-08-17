import json
from typing import Dict, List, Any
from ..config import  get_model_config
from .function_declarations import functions_declarations
import logging
logger = logging.getLogger(__name__)



class AIResponseHandler:
    """
    Handles AI response generation and function calling for multiple providers.
    """
    def __init__(self, session=None, ollama_service=None):
        self.session = session
        self.ollama_service = ollama_service
        self.current_model = None  # Will be set by AI service when needed
        self.client_id = None  # Will be set when needed for dynamic functions
        self.ai_service = None  # Reference to AI service for dynamic functions
    
    def set_client_context(self, client_id: str, ai_service):
        """Set client context for dynamic function access"""
        self.client_id = client_id
        self.ai_service = ai_service
    
    def get_functions_for_current_client(self, format_type: str):
        """Get functions in the specified format for the current client"""
        # For now, we are not using dynamic functions per client, so we use the global declarations.
        # This can be extended later to support dynamic functions.
        if format_type == "openai":
            return self._format_for_openai(functions_declarations)
        elif format_type == "gemini":
            return self._format_for_gemini(functions_declarations)
        elif format_type == "claude":
            return self._format_for_claude(functions_declarations)
        
        return []

    def _format_for_openai(self, declarations: Dict) -> List[Dict]:
        """Formats function declarations for the OpenAI API."""
        functions = []
        for func_name, func_def in declarations.items():
            functions.append({
                "type": "function",
                "function": {
                    "name": func_def["name"],
                    "description": func_def["description"],
                    "parameters": {
                        "type": "object",
                        "properties": func_def.get("parameters", {}),
                        "required": func_def.get("required", [])
                    }
                }
            })
        return functions

    def _format_for_gemini(self, declarations: Dict) -> List[Dict]:
        """Formats function declarations for the Gemini API."""
        functions = []
        for func_name, func_def in declarations.items():
            functions.append({
                "name": func_def["name"],
                "description": func_def["description"],
                "parameters": {
                    "type": "object",
                    "properties": func_def.get("parameters", {}),
                    "required": func_def.get("required", [])
                }
            })
        return functions

    def _format_for_claude(self, declarations: Dict) -> List[Dict]:
        """Formats function declarations for the Claude API."""
        tools = []
        for func_name, func_def in declarations.items():
            tools.append({
                "name": func_def["name"],
                "description": func_def["description"],
                "input_schema": {
                    "type": "object",
                    "properties": func_def.get("parameters", {}),
                    "required": func_def.get("required", [])
                }
            })
        return tools

    async def _generate_openai_response_with_functions(self, messages: List[Dict], model_config: Dict, user_message: str) -> Dict[str, Any]:
        """Generate OpenAI response with function calling support"""
        try:
            openai_functions = self.get_functions_for_current_client("openai")
            # Use all available functions
            payload = {
                "model": model_config.get("model", "gpt-4"),
                "messages": messages,
                "temperature": model_config["temperature"],
                "max_tokens": model_config["max_tokens"],
                "tools": openai_functions,                "tool_choice": "auto"
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
            gemini_functions = self.get_functions_for_current_client("gemini")
            # Convert messages to Gemini format
            contents = []
            for msg in messages:
                role = "user" if msg["role"] == "user" else "model"
                contents.append({
                    "role": role,
                    "parts": [{"text": msg["content"]}]
                })
            # Use all available Gemini functions
            payload = {
                "contents": contents,
                "tools": [{
                    "function_declarations": gemini_functions
                }],
                "generationConfig": {
                    "temperature": model_config["temperature"],
                    "maxOutputTokens": model_config["max_tokens"]                }
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
        try:            # Claude API format - system message separate
            system_message = ""
            claude_messages = []
            
            for msg in messages:
                if msg["role"] == "system":
                    system_message = msg["content"]
                else:
                    claude_messages.append(msg)
              # Use client-specific Claude tools
            payload = {
                "model": model_config.get("model", "claude-3-5-sonnet-20241022"),
                "system": system_message,
                "messages": claude_messages,
                "temperature": model_config["temperature"],
                "max_tokens": model_config["max_tokens"],
                "tools": self.get_functions_for_current_client("claude")
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
                functions=self.get_functions_for_current_client("openai"),  # Use client-specific functions
                model=model_name
            )
            
            logger.info(f"Ollama response type: {result.get('type', 'unknown')}")
            return result
            
        except Exception as e:
            logger.error(f"Error calling Ollama API: {str(e)}", exc_info=True)
            return {
                "type": "error",
                "content": f"Error with Ollama model: {str(e)}",
                "model": model_config.get("model", "ollama")            }
    
    # Function execution and response handling methods
    
    @staticmethod
    def parse_function_calls(response: Dict[str, Any], current_model: str) -> List[Dict]:
        """Parse function calls from AI response into standardized format"""
        if response["type"] != "function_calls":
            return []
        
        function_calls = []
        
        if current_model.startswith("GPT"):
            # OpenAI format
            for tool_call in response["function_calls"]:
                if tool_call["type"] == "function":
                    function_calls.append({
                        "id": tool_call["id"],
                        "name": tool_call["function"]["name"],
                        "parameters": json.loads(tool_call["function"]["arguments"])
                    })
        
        elif current_model.startswith("GEMINI"):
            # Gemini format
            for func_call in response["function_calls"]:
                function_calls.append({
                    "id": f"gemini_{func_call['name']}_{len(function_calls)}",
                    "name": func_call["name"],
                    "parameters": func_call.get("args", {})
                })
        
        elif current_model.startswith("CLAUDE"):
            # Claude format
            for func_call in response["function_calls"]:
                function_calls.append({
                    "id": func_call["id"],
                    "name": func_call["name"],
                    "parameters": func_call["input"]
                })
        
        elif current_model.startswith("OLLAMA"):
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
            openai_functions = self.get_functions_for_current_client("openai")
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
            gemini_functions = self.get_functions_for_current_client("gemini")
          
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
                    break            # Use client-specific Claude tools for follow-up
            payload = {
                "model": model_config.get("model", "claude-3-5-sonnet-20241022"),
                "system": system_message,
                "messages": claude_messages,
                "temperature": model_config["temperature"],
                "max_tokens": model_config["max_tokens"],
                "tools": self.get_functions_for_current_client("claude")
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
