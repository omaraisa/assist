from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import json
import logging
import random
from pathlib import Path
from typing import Dict, List
import uuid
import asyncio

from .websocket_manager import WebSocketManager
from .ai_service import AIService
from .ai.function_declarations import FunctionDeclaration
from .ai.ai_response_handler import AIResponseHandler
from .spatial_functions import SpatialFunctions
from .config import settings
from .monitoring import monitoring_service

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="ArcGIS Pro Smart Assistant",
    description="Smart assistant for ArcGIS Pro with AI-powered analysis",
    version="2.0.0"
)

# Get the directory of this file
BASE_DIR = Path(__file__).parent.parent

# Mount static files
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Setup templates
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Initialize services
websocket_manager = WebSocketManager()
ai_service = AIService(initial_model_key=settings.DEFAULT_AI_MODEL, websocket_manager=websocket_manager)
spatial_functions = SpatialFunctions(websocket_manager=websocket_manager)

@app.get("/", response_class=HTMLResponse)
async def get_chatbot(request: Request):
    """Serve the main chatbot interface"""
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request,
            "available_functions": spatial_functions.AVAILABLE_FUNCTIONS
        }
    )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "version": "2.0.0"}

@app.get("/metrics")
async def get_metrics():
    """Get system performance metrics"""
    return monitoring_service.get_system_health()

@app.get("/stats")
async def get_statistics():
    """Get detailed usage statistics"""
    return monitoring_service.get_usage_statistics()

@app.get("/admin/dashboard")
async def admin_dashboard(request: Request):
    """Admin dashboard for monitoring (future enhancement)"""
    return templates.TemplateResponse(
        "admin_dashboard.html", 
        {
            "request": request,
            "metrics": monitoring_service.get_system_health(),
            "stats": monitoring_service.get_usage_statistics()
        }
    )

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """Main WebSocket endpoint for all clients"""
    client_id = str(uuid.uuid4())
    await websocket_manager.connect(websocket, client_id)
    
    try:
        # Send initial configuration to client
        await websocket_manager.send_to_client(client_id, {
            "type": "config",
            "data": {
                "available_functions": spatial_functions.AVAILABLE_FUNCTIONS,
                "ai_models": settings.AI_MODELS,
                "current_model": settings.DEFAULT_AI_MODEL
            }
        })
        
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            message = json.loads(data)
            
            await handle_websocket_message(client_id, message)
            
    except WebSocketDisconnect:
        logger.info(f"Client {client_id} disconnected")
        await websocket_manager.disconnect(client_id)
    except Exception as e:
        logger.error(f"Error in websocket connection {client_id}: {str(e)}")
        await websocket_manager.disconnect(client_id)

async def handle_websocket_message(client_id: str, message: Dict):
    """Handle incoming WebSocket messages with proper routing"""
    message_type = message.get("type")
    
    try:
        if message_type == "client_register":
            # Register client type (arcgis_pro or chatbot)
            client_type = message.get("client_type")
            if client_type:
                await websocket_manager.register_client_type(client_id, client_type)
                
                if client_type == "arcgis_pro":
                    # Request initial software state
                    await websocket_manager.send_to_client(client_id, {
                        "type": "get_software_state"
                    })
            
        elif message_type == "user_message":
            # Handle user chat message
            await handle_user_message(client_id, message.get("content", ""))
            
        elif message_type == "function_request":
            # Handle function execution request
            await handle_function_request(client_id, message)
            
        elif message_type == "software_state":
            # Handle software state update from ArcGIS Pro
            state_data = message.get("data")
            if state_data:
                await handle_software_state_update(client_id, state_data)
            
        elif message_type == "function_response":
            # Handle function execution response from ArcGIS Pro
            await handle_function_response(client_id, message)
            
        elif message_type == "heartbeat":
            # Handle heartbeat
            await websocket_manager.send_to_client(client_id, {
                "type": "heartbeat_ack"
            })
            
        elif message_type == "change_model":
            # Handle AI model change
            model_key = message.get("model")
            if model_key:
                await handle_model_change(client_id, model_key)
            else:
                await websocket_manager.send_to_client(client_id, {
                    "type": "error",
                    "message": "Model key is required for model change"
                })
                
        elif message_type == "cancel_request":
            # Handle cancel/stop request
            await handle_cancel_request(client_id)
            
        else:
            logger.warning(f"Unknown message type: {message_type}")
            
    except Exception as e:
        logger.error(f"Error handling message {message_type}: {str(e)}")
        await websocket_manager.send_to_client(client_id, {
            "type": "error",
            "message": f"Error processing message: {str(e)}"
        })

async def handle_user_message(client_id: str, user_message: str):
    """Handle user chat messages and generate AI responses"""
    try:
        # Clear any existing cancel flag for new requests
        websocket_manager.clear_cancel_flag(client_id)
        
        # Get current conversation history for this client
        history = websocket_manager.get_conversation_history(client_id)
        
        # Add user message to history
        websocket_manager.add_to_history(client_id, "user", user_message)
        
        # Get current ArcGIS Pro state
        arcgis_state = websocket_manager.get_arcgis_state()        # Generate AI response
        ai_response = await ai_service.generate_response(
            user_message=user_message,
            conversation_history=history,
            arcgis_state=arcgis_state,
            client_id=client_id
        )
        
        # Check for cancellation before processing response
        if websocket_manager.is_cancelled(client_id):
            websocket_manager.clear_cancel_flag(client_id)
            await websocket_manager.send_to_client(client_id, {
                "type": "cancelled",
                "message": "Request was cancelled by user"
            })
            return
        
        # Process AI response for function calling or final response
        await process_ai_response_with_functions(client_id, ai_response)
        
    except Exception as e:
        logger.error(f"Error handling user message: {str(e)}")
        await websocket_manager.send_to_client(client_id, {
            "type": "error",
            "message": f"Error processing your message: {str(e)}"
        })

async def process_ai_response_with_functions(client_id: str, ai_response: Dict):
    """Process AI response with function calling support"""
    try:
        # Check for cancellation before processing
        if websocket_manager.is_cancelled(client_id):
            websocket_manager.clear_cancel_flag(client_id)
            await websocket_manager.send_to_client(client_id, {
                "type": "cancelled",
                "message": "Request was cancelled by user"
            })
            return
            
        response_type = ai_response.get("type")
        
        if response_type == "function_calls":
            # AI wants to call functions
            function_calls = AIResponseHandler.parse_function_calls(ai_response, ai_service.current_model)
            
            if function_calls:
                # CRITICAL: Add assistant message with function calls to conversation history
                # This is required for Gemini API to properly match function calls with responses
                assistant_content = ai_response.get("content", "")
                
                # Create special assistant message that includes function call information
                assistant_message = {
                    "role": "assistant",
                    "content": assistant_content,
                    "function_calls": function_calls  # Store for Gemini API
                }
                
                # Add to conversation history
                websocket_manager.add_to_history_with_metadata(client_id, assistant_message)
                
                # For Gemini API, log that we've added this special message
                if ai_service.current_model.startswith("GEMINI"):
                    logger.info(f"Added assistant message with function_calls to history for Gemini: {json.dumps(function_calls, indent=2)}")
                
                # Execute functions via ArcGIS Pro
                await execute_function_calls(client_id, function_calls, ai_response)
            else:
                # Fallback to text response
                content = ai_response.get("content", "I encountered an issue processing your request.")
                await send_final_response(client_id, content)
                
        elif response_type == "text":
            # Direct text response
            content = ai_response.get("content", "")
            await send_final_response(client_id, content)
            
        else:
            # Fallback for unexpected response types
            logger.warning(f"Unexpected AI response type: {response_type}")
            await send_final_response(client_id, "I encountered an issue processing your request.")
            
    except Exception as e:
        logger.error(f"Error processing AI response with functions: {str(e)}")
        await websocket_manager.send_to_client(client_id, {            "type": "error",
            "message": f"Error processing AI response: {str(e)}"
        })

async def execute_function_calls(client_id: str, function_calls: List[Dict], original_response: Dict):
    """Execute function calls via ArcGIS Pro - handles chains by batching all results"""
    try:
        # Check for cancellation before starting function execution
        if websocket_manager.is_cancelled(client_id):
            await websocket_manager.send_to_client(client_id, {
                "type": "cancelled",
                "message": "Request cancelled before function execution"
            })
            return
            
        # Check if this is a chain of multiple function calls
        is_function_chain = len(function_calls) > 1
        
        if is_function_chain:
            logger.info(f"Detected function chain with {len(function_calls)} functions. Will batch results.")
            # For chains, we'll collect all results before sending to LLM
            chain_context = {
                "client_id": client_id,
                "original_response": original_response,
                "total_functions": len(function_calls),
                "completed_functions": 0,
                "function_results": [],
                "is_chain": True
            }
            websocket_manager.store_chain_context(client_id, chain_context)
          # Send function call request to ArcGIS Pro
        for func_call in function_calls:
            # Check for cancellation before each function call
            if websocket_manager.is_cancelled(client_id):
                await websocket_manager.send_to_client(client_id, {
                    "type": "cancelled",
                    "message": "Request cancelled during function execution"
                })
                return
                
            # Handle get_functions_declaration locally instead of sending to ArcGIS Pro
            if func_call["name"] == "get_functions_declaration":
                function_ids_param = func_call.get("parameters", {}).get("function_ids", "unknown")
                logger.info(f"Handling get_functions_declaration locally with IDs: {function_ids_param}")
                await handle_local_function_declaration(client_id, func_call, original_response, is_function_chain)
                continue
            # Create function execution request
            function_request = {
                "type": "execute_function",
                "session_id": f"func_{uuid.uuid4().hex[:8]}",
                "source_client": client_id,
                "function_name": func_call["name"],
                "parameters": func_call["parameters"]
            }
            
            logger.info(f"Sending function request to ArcGIS Pro: {func_call['name']}")
            
            # Send to ArcGIS Pro client
            arcgis_clients = websocket_manager.get_clients_by_type("arcgis_pro")
            if arcgis_clients:
                await websocket_manager.send_to_client(arcgis_clients[0], function_request)
                
                # Store function call context for response handling
                context = {
                    "client_id": client_id,
                    "function_call": func_call,
                    "original_response": original_response,
                    "is_function_calling": True,
                    "is_chain": is_function_chain
                }
                
                websocket_manager.store_function_context(
                    function_request["session_id"], 
                    context
                )
            else:
                logger.error("No ArcGIS Pro client connected for function execution")
                await websocket_manager.send_to_client(client_id, {
                    "type": "error",
                    "message": "ArcGIS Pro is not connected. Please ensure ArcGIS Pro is running and connected."
                })
                return
                
    except Exception as e:
        logger.error(f"Error executing function calls: {str(e)}")
        await websocket_manager.send_to_client(client_id, {
            "type": "error",
            "message": f"Error executing functions: {str(e)}"        })

async def handle_local_function_declaration(client_id: str, func_call: Dict, original_response: Dict, is_function_chain: bool):
    """Handle get_functions_declaration function call locally without sending to ArcGIS Pro"""
    try:
        logger.info(f"Processing get_functions_declaration locally for client {client_id}")
        
        # Get function IDs from parameters and handle both array and string formats
        function_ids_raw = func_call["parameters"]["function_ids"]
        
        # Handle case where function_ids comes as a string like "[30,31]" instead of array
        if isinstance(function_ids_raw, str):
            try:
                # Remove brackets and split by comma, then convert to integers
                if function_ids_raw.startswith('[') and function_ids_raw.endswith(']'):
                    function_ids_raw = function_ids_raw[1:-1]  # Remove brackets
                function_ids = [int(id.strip()) for id in function_ids_raw.split(',') if id.strip()]
            except (ValueError, AttributeError) as e:
                logger.error(f"Error parsing function_ids string '{function_ids_raw}': {e}")
                function_ids = []
        elif isinstance(function_ids_raw, list):
            function_ids = [int(id) for id in function_ids_raw if str(id).isdigit()]
        else:
            logger.error(f"Unexpected function_ids format: {type(function_ids_raw)} - {function_ids_raw}")
            function_ids = []
        
        logger.info(f"Parsed function IDs: {function_ids}")
        
        if not function_ids:
            logger.error("No valid function IDs provided")
            await websocket_manager.send_to_client(client_id, {
                "type": "error",
                "message": "No valid function IDs provided"
            })
            return
        
        # Create spatial functions instance to get the raw function declarations
        spatial_functions = SpatialFunctions()
        try:
            raw_declarations = spatial_functions.get_functions_declaration(function_ids)
            logger.info(f"Successfully retrieved {len(raw_declarations)} function declarations")
        except Exception as e:
            logger.error(f"Error retrieving function declarations: {e}")
            await websocket_manager.send_to_client(client_id, {
                "type": "error",
                "message": f"Error retrieving function declarations: {str(e)}"
            })
            return
        
        # Process the raw declarations based on the AI model to format them correctly
        ai_model = original_response.get("model", "gemini")  # Default to gemini if not specified
        
        # Convert raw declarations to appropriate format for the AI model
        formatted_declarations = {}
        if "openai" in ai_model.lower():
            # Convert to OpenAI format
            for func_name, func_def in raw_declarations.items():
                openai_func = {
                    "type": "function",
                    "function": {
                        "name": func_def["name"],
                        "description": func_def["description"],
                        "parameters": {
                            "type": "object",
                            "properties": {},
                            "required": func_def["required"]
                        }
                    }
                }
                
                # Convert parameters to OpenAI format
                for param_name, param_def in func_def["parameters"].items():
                    openai_param = {
                        "type": param_def["type"],
                        "description": param_def["description"]
                    }
                    
                    if "enum" in param_def:
                        openai_param["enum"] = param_def["enum"]
                    if "items" in param_def:
                        openai_param["items"] = param_def["items"]
                    
                    openai_func["function"]["parameters"]["properties"][param_name] = openai_param
                
                formatted_declarations[func_name] = openai_func
                
        elif "claude" in ai_model.lower():
            # Convert to Claude format
            for func_name, func_def in raw_declarations.items():
                claude_tool = {
                    "name": func_def["name"],
                    "description": func_def["description"],
                    "input_schema": {
                        "type": "object",
                        "properties": {},
                        "required": func_def["required"]
                    }
                }
                
                # Convert parameters to Claude format
                for param_name, param_def in func_def["parameters"].items():
                    claude_param = {
                        "type": param_def["type"],
                        "description": param_def["description"]
                    }
                    
                    if "enum" in param_def:
                        claude_param["enum"] = param_def["enum"]
                    if "items" in param_def:
                        claude_param["items"] = param_def["items"]
                    
                    claude_tool["input_schema"]["properties"][param_name] = claude_param
                
                formatted_declarations[func_name] = claude_tool
        else:
            # Default to Gemini format or keep raw format
            for func_name, func_def in raw_declarations.items():
                gemini_func = {
                    "name": func_def["name"],
                    "description": func_def["description"],
                    "parameters": {
                        "type": "object",
                        "properties": {},
                        "required": func_def["required"]
                    }
                }
                
                # Convert parameters to Gemini format
                for param_name, param_def in func_def["parameters"].items():
                    gemini_param = {
                        "type": param_def["type"],
                        "description": param_def["description"]
                    }
                    
                    if "enum" in param_def:
                        gemini_param["enum"] = param_def["enum"]
                    if "items" in param_def:
                        gemini_param["items"] = param_def["items"]
                    
                    gemini_func["parameters"]["properties"][param_name] = gemini_param
                
                formatted_declarations[func_name] = gemini_func
        
        # Create the function result
        function_result = {
            "id": func_call["id"],
            "name": func_call["name"],
            "parameters": func_call["parameters"],
            "result": {
                "success": True,
                "function_declarations": formatted_declarations,
                "requested_function_ids": function_ids
            }
        }
          # Handle the result the same way as other function results
        if is_function_chain:
            # This is part of a function chain - add to chain context
            chain_context = websocket_manager.get_chain_context(client_id)
            if chain_context:
                chain_context["completed_functions"] += 1
                chain_context["function_results"].append(function_result)
                
                logger.info(f"Function chain progress: {chain_context['completed_functions']}/{chain_context['total_functions']}")
                
                # CRITICAL: Dynamically inject discovered functions into AI's available functions
                # This allows the AI to call the functions it just discovered
                await inject_discovered_functions_for_client(client_id, raw_declarations)
                
                # Check if all functions in the chain are complete
                if chain_context["completed_functions"] >= chain_context["total_functions"]:
                    logger.info("All functions in chain completed. Sending batch results to LLM.")
                    await handle_chain_completion(client_id, chain_context)                
                else:
                    logger.info(f"Waiting for {chain_context['total_functions'] - chain_context['completed_functions']} more functions to complete.")
            else:
                logger.error("Chain context not found - falling back to single function handling")
                await handle_single_function_result_with_retry(client_id, function_result, original_response)
        else:
            # Single function call - inject discovered functions and handle immediately
            await inject_discovered_functions_for_client(client_id, raw_declarations)
            await handle_single_function_result_with_retry(client_id, function_result, original_response)
            
    except Exception as e:
        logger.error(f"Error handling local function declaration: {str(e)}")
        await websocket_manager.send_to_client(client_id, {
            "type": "error",
            "message": f"Error processing function declaration request: {str(e)}"
        })

async def process_ai_response(client_id: str, ai_response: str):
    """Process AI response for investigation commands or final responses"""
    try:
        # Parse for INVESTIGATE commands
        investigate_commands = ai_service.extract_investigate_commands(ai_response)
        complete_response = ai_service.extract_complete_response(ai_response)
        
        if investigate_commands:
            # Start investigation session
            session_id = websocket_manager.start_investigation_session(client_id)
            
            # Execute investigation commands
            for command in investigate_commands:
                await execute_investigation_command(client_id, session_id, command)
                
            # If there's also a complete response, save it for later
            if complete_response:
                websocket_manager.set_pending_response(client_id, complete_response)
                
        elif complete_response:
            # Direct response without investigation
            await send_final_response(client_id, complete_response)
            
        else:
            # Fallback - treat entire response as final
            await send_final_response(client_id, ai_response)
            
    except Exception as e:
        logger.error(f"Error processing AI response: {str(e)}")
        await websocket_manager.send_to_client(client_id, {
            "type": "error",
            "message": f"Error processing AI response: {str(e)}"
        })

async def execute_investigation_command(client_id: str, session_id: str, command: str):
    """Execute a single investigation command"""
    try:
        # Parse the function call
        function_call = ai_service.parse_function_call(command)
        
        if not function_call:
            logger.error(f"Failed to parse function call: {command}")
            return
            
        # Send function request to ArcGIS Pro
        arcgis_client = websocket_manager.get_arcgis_client()
        if not arcgis_client:
            raise Exception("ArcGIS Pro is not connected")
              # Prepare function execution message
        function_message = {
            "type": "execute_function",
            "session_id": session_id,
            "source_client": client_id,  # Add this crucial field!
            "function_name": function_call["function_name"],
            "parameters": function_call["parameters"]
        }
        
        await websocket_manager.send_to_client(arcgis_client, function_message)
        
    except Exception as e:
        logger.error(f"Error executing investigation command: {str(e)}")

async def handle_function_request(client_id: str, message: Dict):
    """Handle direct function execution requests"""
    try:
        function_name = message.get("function_name")
        parameters = message.get("parameters", {})
        
        # Validate function name and exists
        if not function_name:
            raise Exception("Function name is required")
        if not hasattr(spatial_functions, function_name):
            raise Exception(f"Function '{function_name}' not found")
            
        # Get ArcGIS Pro client
        arcgis_client = websocket_manager.get_arcgis_client()
        if not arcgis_client:
            raise Exception("ArcGIS Pro is not connected")
            
        # Send function execution request
        function_message = {
            "type": "execute_function",
            "function_name": function_name,
            "parameters": parameters,
            "source_client": client_id
        }
        
        await websocket_manager.send_to_client(arcgis_client, function_message)
        
    except Exception as e:
        logger.error(f"Error handling function request: {str(e)}")
        await websocket_manager.send_to_client(client_id, {
            "type": "error",
            "message": str(e)
        })

async def handle_software_state_update(client_id: str, state_data: Dict):
    """Handle software state updates from ArcGIS Pro"""
    try:
        # Update the global ArcGIS state
        websocket_manager.update_arcgis_state(state_data)
        
        # Notify all chatbot clients about the state update
        chatbot_clients = websocket_manager.get_chatbot_clients()
        for chatbot_client in chatbot_clients:
            await websocket_manager.send_to_client(chatbot_client, {
                "type": "software_state_updated",
                "data": state_data
            })
            
    except Exception as e:
        logger.error(f"Error handling software state update: {str(e)}")

async def handle_function_calling_response(session_id: str, message: Dict, context: Dict):
    """Handle function calling response and generate final AI response"""
    try:
        client_id = context["client_id"]
        function_call = context["function_call"]
        original_response = context["original_response"]
        is_chain = context.get("is_chain", False)
        
        # Prepare function result
        function_result = {
            "id": function_call["id"],
            "name": function_call["name"],
            "parameters": function_call["parameters"],
            "result": message.get("data", {})
        }
        
        # Handle chain vs single function call differently
        if is_chain:
            # This is part of a function chain - collect the result
            chain_context = websocket_manager.get_chain_context(client_id)
            if chain_context:
                chain_context["completed_functions"] += 1
                chain_context["function_results"].append(function_result)
                logger.info(f"Function chain progress: {chain_context['completed_functions']}/{chain_context['total_functions']}")
                
                # Check if all functions in the chain are complete
                if chain_context["completed_functions"] >= chain_context["total_functions"]:
                    logger.info("All functions in chain completed. Sending batch results to LLM.")
                    await handle_chain_completion(client_id, chain_context)
                else:
                    # Still waiting for more functions to complete - don't send anything to user yet
                    logger.info(f"Waiting for {chain_context['total_functions'] - chain_context['completed_functions']} more functions to complete.")
            else:
                logger.error("Chain context not found - falling back to single function handling")
                await handle_single_function_result_with_retry(client_id, function_result, original_response)
        else:
            # Single function call - handle immediately
            await handle_single_function_result_with_retry(client_id, function_result, original_response)
        
    except Exception as e:
        logger.error(f"Error handling function calling response: {str(e)}")
        await websocket_manager.send_to_client(client_id, {
            "type": "error",
            "message": f"Error processing function result: {str(e)}"
        })

async def handle_single_function_result(client_id: str, function_result: Dict, original_response: Dict):
    """Handle a single function result"""
    try:
        # Get conversation history and prepare messages for AI
        history = websocket_manager.get_conversation_history(client_id)
        arcgis_state = websocket_manager.get_arcgis_state()
        
        # Build messages for function response
        messages = ai_service._prepare_messages(
            original_response.get("content", ""),
            history,
            arcgis_state
        )
        
        # Add the function call response to conversation
        logger.info(f"Sending single function result to AI: {function_result['name']}")
        final_response = await ai_service.handle_function_response(messages, [function_result])
        
        # Check if this function result should trigger dashboard update
        await check_and_update_dashboard(client_id, function_result)
        
        # Send final response to user
        if final_response.get("type") == "text":
            content = final_response.get("content", "I processed your request successfully.")
            await send_final_response(client_id, content)
            
            # Add to conversation history
            websocket_manager.add_to_history(client_id, "assistant", content)
        else:
            # Handle unexpected response type
            await send_final_response(client_id, "I processed your request successfully.")
            
    except Exception as e:
        logger.error(f"Error handling single function result: {str(e)}")
        await websocket_manager.send_to_client(client_id, {
            "type": "error", 
            "message": f"Error processing function result: {str(e)}"
        })

async def check_and_update_dashboard(client_id: str, function_result: Dict):
    """Check if function result requires dashboard update and send update to frontend"""
    try:
        function_name = function_result.get("name", "")
        dashboard_functions = [
            "analyze_layer_fields",
            "generate_smart_dashboard_layout",
            "recommend_chart_types", 
            "plan_dashboard_layout",
            "optimize_dashboard_layout"
        ]
        
        if function_name in dashboard_functions:
            logger.info(f"Dashboard function {function_name} completed, checking for dashboard data")
            
            # Try to load latest dashboard data
            dashboard_files = [
                BASE_DIR / "optimized_dashboard.json",
                BASE_DIR / "smart_dashboard.json", 
                BASE_DIR / "dashboard.json"
            ]
            
            for dashboard_file in dashboard_files:
                if dashboard_file.exists():
                    try:
                        with open(dashboard_file, 'r', encoding='utf-8') as f:
                            dashboard_data = json.load(f)
                            
                        # Transform to frontend format
                        frontend_data = transform_dashboard_for_frontend(dashboard_data)
                        
                        if "error" not in frontend_data:
                            # Send dashboard update to all chatbot clients
                            chatbot_clients = websocket_manager.get_clients_by_type("chatbot")
                            for chatbot_client in chatbot_clients:
                                await websocket_manager.send_to_client(chatbot_client, {
                                    "type": "dashboard_update",
                                    "data": frontend_data
                                })
                            
                            logger.info(f"Dashboard update sent to {len(chatbot_clients)} clients")
                            break
                    except Exception as e:
                        logger.error(f"Error loading dashboard file {dashboard_file}: {str(e)}")
                        continue
                        
    except Exception as e:
        logger.error(f"Error checking dashboard update: {str(e)}")

async def handle_single_function_result_with_retry(client_id: str, function_result: Dict, original_response: Dict):
    """Handle a single function result with retry logic for function declarations"""
    try:
        # Check if this is a get_functions_declaration response
        is_discovery_response = function_result.get("name") == "get_functions_declaration"
        
        # Get conversation history and prepare messages for AI
        history = websocket_manager.get_conversation_history(client_id)
        arcgis_state = websocket_manager.get_arcgis_state()
        
        # Build messages for function response
        messages = ai_service._prepare_messages(
            original_response.get("content", ""),
            history,
            arcgis_state
        )
        
        # Add the function call response to conversation
        logger.info(f"Sending single function result to AI: {function_result['name']}")
        final_response = await ai_service.handle_function_response(messages, [function_result])
        
        # Special handling for function discovery responses
        if is_discovery_response:
            response_type = final_response.get("type", "")
            content = final_response.get("content", "").strip()
            
            # Check if AI provided an empty or non-functional response
            if response_type == "text" and (not content or len(content) < 50):
                logger.warning("AI provided empty/minimal response after function discovery. Implementing retry logic.")
                
                # Add system message to encourage function execution
                retry_message = {
                    "role": "system",
                    "content": "IMPORTANT: You have received function declarations. You MUST now execute the appropriate GIS functions to complete the user's task. DO NOT provide a text response - make the necessary function calls immediately to fulfill the user's request."
                }
                
                # Add to conversation history
                websocket_manager.add_to_history_with_metadata(client_id, retry_message)
                
                # Wait 2 seconds and try again
                logger.info("Waiting 2 seconds before retry...")
                await asyncio.sleep(2)
                
                # Retry with the enhanced messages
                enhanced_messages = messages + [retry_message]
                logger.info("Retrying AI call with enhanced prompt after function discovery")
                retry_response = await ai_service.generate_response(
                    user_message=original_response.get("content", ""),
                    conversation_history=websocket_manager.get_conversation_history(client_id),
                    arcgis_state=arcgis_state,
                    client_id=client_id
                )
                
                # Process the retry response
                await process_ai_response_with_functions(client_id, retry_response)
                return
        
        # Normal response handling
        if final_response.get("type") == "text":
            content = final_response.get("content", "I processed your request successfully.")
            await send_final_response(client_id, content)
            
            # Add to conversation history
            websocket_manager.add_to_history(client_id, "assistant", content)
        else:
            # Handle unexpected response type
            await send_final_response(client_id, "I processed your request successfully.")
            
    except Exception as e:
        logger.error(f"Error handling single function result with retry: {str(e)}")
        await websocket_manager.send_to_client(client_id, {
            "type": "error", 
            "message": f"Error processing function result: {str(e)}"
        })

async def handle_chain_completion(client_id: str, chain_context: Dict):
    """Handle completion of a function chain by sending all results to LLM at once"""
    try:
        # Get conversation history 
        history = websocket_manager.get_conversation_history(client_id)
        original_response = chain_context["original_response"]
        function_results = chain_context["function_results"]
        
        # Build messages for function response - no need for ArcGIS state for chain completion
        messages = ai_service._prepare_messages(
            original_response.get("content", ""),
            history,
            {}  # Empty state - we only need history + function results
        )
        
        logger.info(f"Sending {len(function_results)} function results to AI for chain completion")
        
        # Send all function results together to AI for final response
        final_response = await ai_service.handle_function_response(messages, function_results)
        
        # Check if any function in the chain should trigger dashboard update
        for function_result in function_results:
            await check_and_update_dashboard(client_id, function_result)
        
        # Send final response to user
        if final_response.get("type") == "text":
            content = final_response.get("content", "I completed all the requested tasks successfully.")
            await send_final_response(client_id, content)
            
            # Add to conversation history
            websocket_manager.add_to_history(client_id, "assistant", content)
        else:
            # Handle unexpected response type
            await send_final_response(client_id, "I completed all the requested tasks successfully.")
        
        # Clean up chain context
        websocket_manager.clear_chain_context(client_id)
        
    except Exception as e:
        logger.error(f"Error handling chain completion: {str(e)}")
        websocket_manager.clear_chain_context(client_id)
        await websocket_manager.send_to_client(client_id, {            "type": "error",
            "message": f"Error completing function chain: {str(e)}"
        })

async def handle_function_response(client_id: str, message: Dict):
    """Handle function execution responses from ArcGIS Pro"""
    try:
        session_id = message.get("session_id")
        source_client = message.get("source_client")
        
        logger.info(f"Received function response: session_id={session_id}, source_client={source_client}, from_client={client_id}")
        
        # Check for cancellation before processing function response
        if source_client and websocket_manager.is_cancelled(source_client):
            logger.info(f"Function response ignored - request was cancelled for client {source_client}")
            return
        
        # Store function response for LangChain agent if session_id exists (regardless of other conditions)
        if session_id:
            websocket_manager.store_function_result(session_id, message)
            logger.info(f"Stored function response for session {session_id}")
        
        # Check if this is a function calling response
        if session_id:
            context = websocket_manager.get_function_context(session_id)
            if context and context.get("is_function_calling"):
                logger.info(f"Processing function calling response for session {session_id}")
                await handle_function_calling_response(session_id, message, context)
                return
        
        if session_id and source_client:
            # This is part of an investigation session (legacy)
            logger.info(f"Continuing investigation session {session_id} for client {source_client}")
            await continue_investigation_session(source_client, session_id, message)
        elif source_client:
            # Direct function response (legacy)
            logger.info(f"Sending direct function result to client {source_client}")
            await websocket_manager.send_to_client(source_client, {
                "type": "function_result",
                "data": message.get("data")
            })
        else:
            logger.warning(f"Function response missing session_id and source_client: {message}")
            
    except Exception as e:
        logger.error(f"Error handling function response: {str(e)}")

async def continue_investigation_session(client_id: str, session_id: str, response: Dict):
    """Continue investigation session with AI after receiving function response"""
    try:
        # Add response to investigation history
        websocket_manager.add_investigation_step(client_id, session_id, response)
        
        # Check if investigation is complete
        session = websocket_manager.get_investigation_session(client_id, session_id)
        if not session:
            return
            
        # Get pending commands
        remaining_commands = session.get("remaining_commands", [])
        
        if remaining_commands:
            # Execute next command
            next_command = remaining_commands.pop(0)
            await execute_investigation_command(client_id, session_id, next_command)
        else:
            # Investigation complete, generate final response
            await complete_investigation_session(client_id, session_id)
            
    except Exception as e:
        logger.error(f"Error continuing investigation session: {str(e)}")

async def complete_investigation_session(client_id: str, session_id: str):
    """Complete investigation session and generate final response"""
    try:
        # Get investigation history
        session = websocket_manager.get_investigation_session(client_id, session_id)
        
        if not session:
            logger.error(f"Investigation session {session_id} not found for client {client_id}")
            return
        
        # Generate final response using AI
        final_response = await ai_service.generate_investigation_summary(session)
        
        # Send final response to user
        await send_final_response(client_id, final_response)
        
        # Clean up investigation session
        websocket_manager.end_investigation_session(client_id, session_id)
        
    except Exception as e:
        logger.error(f"Error completing investigation session: {str(e)}")
        await websocket_manager.send_to_client(client_id, {
            "type": "error",
            "message": f"Error completing investigation: {str(e)}"
        })
        logger.error(f"Error completing investigation session: {str(e)}")

async def send_final_response(client_id: str, response: str):
    """Send final response to chatbot client"""
    try:
        # Add to conversation history
        websocket_manager.add_to_history(client_id, "assistant", response)
        
        # Send to client
        await websocket_manager.send_to_client(client_id, {
            "type": "assistant_message",
            "content": response
        })
        
    except Exception as e:
        logger.error(f"Error sending final response: {str(e)}")

async def handle_model_change(client_id: str, model_key: str):
    """Handle AI model change requests from clients"""
    try:
        if not model_key:
            raise ValueError("Model key is required")
            
        # Validate model exists
        if model_key not in settings.AI_MODELS:
            available_models = list(settings.AI_MODELS.keys())
            raise ValueError(f"Unknown model '{model_key}'. Available models: {available_models}")
        
        # Change the AI service model
        ai_service.set_model(model_key)
        
        # Confirm model change to client
        await websocket_manager.send_to_client(client_id, {
            "type": "model_changed",
            "model": model_key,
            "model_name": settings.AI_MODELS[model_key]["name"]
        })
        
        logger.info(f"AI model changed to {model_key} for client {client_id}")
        
    except Exception as e:
        logger.error(f"Error changing AI model: {str(e)}")
        await websocket_manager.send_to_client(client_id, {
            "type": "error", 
            "message": f"Failed to change AI model: {str(e)}"
        })

async def handle_cancel_request(client_id: str):
    """Handle cancel/stop request from client"""
    try:
        # Set cancel flag for this client
        websocket_manager.set_cancel_flag(client_id)
        
        # Send immediate acknowledgment
        await websocket_manager.send_to_client(client_id, {
            "type": "cancelled",
            "message": "Request cancelled successfully"
        })
        
        logger.info(f"Cancel request processed for client {client_id}")
        
    except Exception as e:
        logger.error(f"Error handling cancel request: {str(e)}")

async def inject_discovered_functions_for_client(client_id: str, discovered_functions: Dict):
    """Dynamically inject discovered functions into the AI's available functions for this client"""
    try:
        if discovered_functions:
            logger.info(f"Injecting {len(discovered_functions)} discovered functions for client {client_id}")
            
            # Store the discovered functions in the AI service for this client/conversation
            ai_service.add_dynamic_functions_for_client(client_id, discovered_functions)
            
            logger.info(f"Successfully injected functions: {list(discovered_functions.keys())}")
        else:
            logger.info("No functions to inject")
            
    except Exception as e:
        logger.error(f"Error injecting discovered functions: {str(e)}")

# Startup event
@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    logger.info("Starting ArcGIS Pro Smart Assistant...")
    
    # Initialize AI service
    await ai_service.initialize()
    
    logger.info("Smart Assistant started successfully!")

# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    logger.info("Shutting down ArcGIS Pro Smart Assistant...")
    
    # Close all WebSocket connections
    await websocket_manager.disconnect_all()
    
    logger.info("Smart Assistant shut down successfully!")

@app.get("/api/dashboard/latest")
async def get_latest_dashboard():
    """Get the latest dashboard data"""
    try:
        # Check for optimized dashboard first, then smart dashboard, then basic dashboard
        dashboard_files = [
            BASE_DIR / "optimized_dashboard.json",
            BASE_DIR / "smart_dashboard.json", 
            BASE_DIR / "dashboard.json"
        ]
        
        for dashboard_file in dashboard_files:
            if dashboard_file.exists():
                with open(dashboard_file, 'r', encoding='utf-8') as f:
                    dashboard_data = json.load(f)
                    
                # Transform to frontend format
                frontend_data = transform_dashboard_for_frontend(dashboard_data)
                return frontend_data
        
        return {"error": "No dashboard data available"}
    except Exception as e:
        logger.error(f"Error loading dashboard data: {str(e)}")
        return {"error": f"Failed to load dashboard: {str(e)}"}

def transform_dashboard_for_frontend(dashboard_data):
    """Transform backend dashboard data to frontend-compatible format"""
    try:
        # Check if it's an optimized dashboard
        if "optimized_layout_plan" in dashboard_data:
            # Handle optimized layout structure
            layout_plan = dashboard_data.get("optimized_layout_plan", {})
            chart_positions = layout_plan.get("chart_positions", [])
            layout_template = dashboard_data.get("layout_optimization", {}).get("template_applied", "auto")
            
            # Convert chart positions to chart configs
            chart_configs = []
            for pos in chart_positions:
                chart_config = {
                    "chart_id": pos.get("chart_id"),
                    "chart_type": pos.get("chart_type"),
                    "title": pos.get("title", f"Chart {pos.get('chart_id', 1)}"),
                    "recommended_size": pos.get("recommended_size", "medium"),
                    "priority": pos.get("priority", 1),
                    "position": pos.get("grid_position", {})
                }
                chart_configs.append(chart_config)
        elif "chart_recommendations" in dashboard_data:
            chart_configs = dashboard_data.get("chart_recommendations", [])
            layout_template = "auto"
        elif "dashboard_layout" in dashboard_data:
            # Handle standard dashboard layout format
            dashboard_layout = dashboard_data.get("dashboard_layout", [])
            layout_template = "grid"
            
            # Convert dashboard layout to chart configs
            chart_configs = []
            for widget in dashboard_layout:
                chart_config = {
                    "chart_id": widget.get("id", f"chart_{len(chart_configs)}"),
                    "chart_type": widget.get("chart_type", "bar"),
                    "title": widget.get("field", f"Chart {len(chart_configs) + 1}"),
                    "primary_field": widget.get("field", ""),
                    "recommended_size": "medium",
                    "priority": 1,
                    "position": {
                        "x": widget.get("x", 0),
                        "y": widget.get("y", 0),
                        "width": widget.get("w", 4),
                        "height": widget.get("h", 3)
                    }
                }
                chart_configs.append(chart_config)
        else:
            # Basic dashboard format
            return {"error": "Unsupported dashboard format"}
        
        charts = []
        for i, chart in enumerate(chart_configs):
            # Extract chart data from field insights if available
            chart_data = prepare_chart_data_from_insights(chart, dashboard_data)
            
            frontend_chart = {
                "title": chart.get("title", f"Chart {i+1}"),
                "type": chart.get("chart_type", chart.get("type", "bar")),
                "description": chart.get("description", chart.get("reasoning", "")),
                "x_field": chart.get("primary_field", chart.get("x_field", "")),
                "y_field": chart.get("group_by_field", chart.get("y_field", "")),
                "data": chart_data,
                "layout": {
                    "size": chart.get("recommended_size", chart.get("size", "medium")),
                    "template": layout_template
                }
            }
            
            # Only include explicit positioning for non-auto templates
            if layout_template != "auto" and chart.get("position"):
                position = chart.get("position", {})
                if position.get("x") is not None and position.get("y") is not None:
                    frontend_chart["layout"].update({
                        "column": position.get("x", 1) + 1,  # CSS grid is 1-based
                        "row": position.get("y", 1) + 1,     # CSS grid is 1-based
                        "width": position.get("width", 4),
                        "height": position.get("height", 3)
                    })
            charts.append(frontend_chart)
        
        return {
            "charts": charts,
            "metadata": {
                "layer_name": dashboard_data.get("layer_name", "Unknown"),
                "timestamp": dashboard_data.get("analysis_timestamp", ""),
                "layout_template": layout_template,
                "total_charts": len(charts)
            }
        }
    except Exception as e:
        logger.error(f"Error transforming dashboard data: {str(e)}")
        return {"error": f"Failed to transform dashboard: {str(e)}"}

def prepare_chart_data_from_insights(chart_config, dashboard_data):
    """Prepare chart data from field insights"""
    try:
        field_insights = dashboard_data.get("field_insights", {})
        chart_type = chart_config.get("chart_type", chart_config.get("type", "bar"))
        primary_field = chart_config.get("primary_field", chart_config.get("x_field", ""))
        group_by_field = chart_config.get("group_by_field", chart_config.get("y_field", ""))
        
        # If no field insights available, return error message
        if not field_insights:
            return {
                "labels": ["ERROR: NO FIELD INSIGHTS DATA"],
                "values": [0],
                "error": "Dashboard layout exists but field analysis data is missing. Please run analyze_layer_fields first."
            }
        
        if chart_type in ["pie", "donut"] and primary_field in field_insights:
            # For pie/donut charts, generate distribution based on field characteristics
            field_data = field_insights[primary_field]
            unique_count = field_data.get("unique_count", 0)
            total_records = field_data.get("total_records", 0)
            data_category = field_data.get("data_category", "")
            
            if data_category == "categorical_text" and unique_count <= 50:
                # Use sample values to create realistic distribution
                sample_values = field_data.get("sample_values", [])[:8]
                if sample_values:
                    labels = [str(val) for val in sample_values]
                    # Generate realistic distribution - some categories more common than others
                    values = []
                    remaining_total = total_records
                    for i, _ in enumerate(labels[:-1]):
                        # Use power law distribution for realistic categorical data
                        portion = int(remaining_total * (0.5 ** i) * 0.4)
                        values.append(portion)
                        remaining_total -= portion
                    values.append(max(remaining_total, 0))
                    
                    return {
                        "labels": labels,
                        "values": values
                    }
            elif data_category in ["binary_indicator", "boolean"]:
                # Binary pie chart
                null_pct = field_data.get("null_percentage", 0)
                positive_rate = (100 - null_pct) * 0.5  # Assume 50% split for binary
                negative_rate = 100 - null_pct - positive_rate
                
                return {
                    "labels": ["Yes", "No", "Unknown"],
                    "values": [int(total_records * positive_rate / 100), 
                              int(total_records * negative_rate / 100),
                              int(total_records * null_pct / 100)]
                }
        
        elif chart_type in ["bar", "column"] and primary_field in field_insights:
            # For bar charts
            field_data = field_insights[primary_field]
            unique_count = field_data.get("unique_count", 0)
            total_records = field_data.get("total_records", 0)
            
            if unique_count <= 30:
                # Use sample values for categories
                sample_values = field_data.get("sample_values", [])[:12]
                labels = [str(val) for val in sample_values]
                # Generate decreasing frequency distribution
                values = []
                base_count = int(total_records / unique_count)
                for i in range(len(labels)):
                    count = max(base_count - (i * base_count // 4), 10)
                    values.append(count)
                
                return {
                    "labels": labels,
                    "values": values
                }
            else:
                # Generate range-based histogram for high cardinality
                min_val = field_data.get("min_value", 0)
                max_val = field_data.get("max_value", 100)
                
                # Create 8 bins
                bin_size = (max_val - min_val) / 8
                labels = []
                values = []
                
                for i in range(8):
                    start = min_val + (i * bin_size)
                    end = min_val + ((i + 1) * bin_size)
                    labels.append(f"{start:.0f}-{end:.0f}")
                    # Generate normally distributed counts
                    values.append(int(total_records * (0.2 - abs(i - 3.5) * 0.03)))
                
                return {
                    "labels": labels,
                    "values": values
                }
        
        elif chart_type == "histogram" and primary_field in field_insights:
            # For histograms of numeric data
            field_data = field_insights[primary_field]
            min_val = field_data.get("min_value", 0)
            max_val = field_data.get("max_value", 100)
            total_records = field_data.get("total_records", 0)
            
            # Create 10 bins for histogram
            bin_size = (max_val - min_val) / 10
            labels = []
            values = []
            
            for i in range(10):
                start = min_val + (i * bin_size)
                end = min_val + ((i + 1) * bin_size)
                labels.append(f"{start:.0f}-{end:.0f}")
                # Generate bell curve distribution
                center = 5
                distance = abs(i - center)
                frequency = int(total_records * (0.25 - distance * 0.03))
                values.append(max(frequency, 0))
            
            return {
                "labels": labels,
                "values": values
            }
        
        elif chart_type == "scatter" and primary_field in field_insights and group_by_field in field_insights:
            # For scatter plots, generate sample points
            x_field_data = field_insights[primary_field]
            y_field_data = field_insights[group_by_field]
            
            x_min = x_field_data.get("min_value", 0)
            x_max = x_field_data.get("max_value", 100)
            y_min = y_field_data.get("min_value", 0)
            y_max = y_field_data.get("max_value", 100)
            
            points = []
            for i in range(50):  # Generate 50 sample points
                x = x_min + (x_max - x_min) * (i / 50) + (random.uniform(-0.1, 0.1) * (x_max - x_min))
                y = y_min + (y_max - y_min) * (i / 50) + (random.uniform(-0.1, 0.1) * (y_max - y_min))
                points.append({"x": x, "y": y})
            
            return {"points": points}
        
        elif chart_type == "box_plot":
            # For box plots, generate statistical summary
            field_data = field_insights.get(primary_field, {})
            min_val = field_data.get("min_value", 0)
            max_val = field_data.get("max_value", 100)
            avg_val = field_data.get("average_value", (min_val + max_val) / 2)
            
            # Generate box plot data (simplified)
            range_size = max_val - min_val
            return {
                "labels": ["Data Distribution"],
                "values": [min_val, min_val + range_size * 0.25, avg_val, 
                          min_val + range_size * 0.75, max_val]
            }
        
        # Default fallback data for missing field insights
        if primary_field not in field_insights:
            return {
                "labels": [f"ERROR: FIELD '{primary_field}' NOT ANALYZED"],
                "values": [0],
                "error": f"Field '{primary_field}' was not found in field insights. Dashboard layout references a field that wasn't analyzed."
            }
        
        # If we get here, something went wrong
        return {
            "labels": ["ERROR: CHART DATA GENERATION FAILED"],
            "values": [0],
            "error": f"Failed to generate chart data for field '{primary_field}' with chart type '{chart_type}'"
        }
        
    except Exception as e:
        logger.error(f"Error preparing chart data: {str(e)}")
        return {"labels": ["Error"], "values": [0]}
