from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import json
import logging
from pathlib import Path
from typing import Dict, List
import uuid

from .websocket_manager import WebSocketManager
from .ai_service import AIService
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
ai_service = AIService()
spatial_functions = SpatialFunctions()

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
        # Get current conversation history for this client
        history = websocket_manager.get_conversation_history(client_id)
        
        # Add user message to history
        websocket_manager.add_to_history(client_id, "user", user_message)
        
        # Get current ArcGIS Pro state
        arcgis_state = websocket_manager.get_arcgis_state()
          # Generate AI response
        ai_response = await ai_service.generate_response(
            user_message=user_message,
            conversation_history=history,
            arcgis_state=arcgis_state,
        )
        
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
        await websocket_manager.send_to_client(client_id, {
            "type": "error",
            "message": f"Error processing AI response: {str(e)}"
        })

async def execute_function_calls(client_id: str, function_calls: List[Dict], original_response: Dict):
    """Execute function calls via ArcGIS Pro - handles chains by batching all results"""
    try:
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
            "message": f"Error executing functions: {str(e)}"
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
                await handle_single_function_result(client_id, function_result, original_response)
        else:
            # Single function call - handle immediately
            await handle_single_function_result(client_id, function_result, original_response)
        
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
