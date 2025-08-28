from fastapi import WebSocket
import json
import uuid
import asyncio
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime

logger = logging.getLogger(__name__)

class WebSocketManager:
    """Manages WebSocket connections and message routing"""
    
    def __init__(self):
        # Store active connections
        self.active_connections: Dict[str, WebSocket] = {}
        
        # Store client types (arcgis_pro, chatbot)
        self.client_types: Dict[str, str] = {}
          # Store conversation histories per client
        self.conversation_histories: Dict[str, List[Dict]] = {}
        
        # Store investigation sessions
        self.investigation_sessions: Dict[str, Dict[str, Any]] = {}
        
        # Store global ArcGIS Pro state
        self.arcgis_state: Dict = {}
        
        # Store pending responses for investigation sessions
        self.pending_responses: Dict[str, str] = {}
        
        # Store function execution results
        self.function_results: Dict[str, Dict] = {}
        
        # Store function calling contexts (for new function calling system)
        self.function_contexts: Dict[str, Dict] = {}
        
        # Chain context management for function calling chains
        self.chain_contexts: Dict[str, Dict] = {}
        
        # Store cancel flags for clients
        self.cancel_flags: Dict[str, bool] = {}
    
    async def connect(self, websocket: WebSocket, client_id: str):
        """Accept a new WebSocket connection"""
        await websocket.accept()
        self.active_connections[client_id] = websocket
        self.conversation_histories[client_id] = []
        logger.info(f"Client {client_id} connected")
    
    async def disconnect(self, client_id: str):
        """Disconnect a client"""
        if client_id in self.active_connections:
            del self.active_connections[client_id]
        if client_id in self.client_types:
            del self.client_types[client_id]
        if client_id in self.conversation_histories:
            del self.conversation_histories[client_id]
        if client_id in self.pending_responses:
            del self.pending_responses[client_id]
        if client_id in self.cancel_flags:
            del self.cancel_flags[client_id]
        logger.info(f"Client {client_id} disconnected")
    
    async def disconnect_all(self):
        """Disconnect all clients"""
        for client_id in list(self.active_connections.keys()):
            await self.disconnect(client_id)
    
    async def register_client_type(self, client_id: str, client_type: str):
        """Register the type of client (arcgis_pro or chatbot)"""
        self.client_types[client_id] = client_type
        logger.info(f"Client {client_id} registered as {client_type}")
    
    async def send_to_client(self, client_id: str, message: Dict):
        """Send message to a specific client"""
        if client_id in self.active_connections:
            try:
                websocket = self.active_connections[client_id]
                await websocket.send_text(json.dumps(message))
            except Exception as e:
                logger.error(f"Error sending message to {client_id}: {str(e)}")
                await self.disconnect(client_id)
    
    async def broadcast_to_type(self, client_type: str, message: Dict):
        """Broadcast message to all clients of a specific type"""
        clients_to_notify = [
            client_id for client_id, c_type in self.client_types.items() 
            if c_type == client_type
        ]
        
        for client_id in clients_to_notify:
            await self.send_to_client(client_id, message)
    
    def get_arcgis_client(self) -> Optional[str]:
        """Get the first available ArcGIS Pro client ID"""
        for client_id, client_type in self.client_types.items():
            if client_type == "arcgis_pro":
                return client_id
        return None
    
    def get_chatbot_clients(self) -> List[str]:
        """Get all chatbot client IDs"""
        return [
            client_id for client_id, client_type in self.client_types.items()
            if client_type == "chatbot"
        ]
    
    def get_conversation_history(self, client_id: str) -> List[Dict]:
        """Get conversation history for a client"""
        return self.conversation_histories.get(client_id, [])
    
    def add_to_history(self, client_id: str, role: str, content: str):
        """Add message to conversation history"""
        if client_id not in self.conversation_histories:
            self.conversation_histories[client_id] = []
        
        self.conversation_histories[client_id].append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
        
        # Keep only last N messages to prevent memory issues
        max_history = 20
        if len(self.conversation_histories[client_id]) > max_history:
            self.conversation_histories[client_id] = self.conversation_histories[client_id][-max_history:]
    
    def add_to_history_with_metadata(self, client_id: str, message: Dict):
        """Add message with metadata to conversation history (for function calls)"""
        if client_id not in self.conversation_histories:
            self.conversation_histories[client_id] = []
        
        # Add timestamp to the message
        message_with_timestamp = message.copy()
        message_with_timestamp["timestamp"] = datetime.now().isoformat()
        
        self.conversation_histories[client_id].append(message_with_timestamp)
        
        # Keep only last N messages to prevent memory issues
        max_history = 20
        if len(self.conversation_histories[client_id]) > max_history:
            self.conversation_histories[client_id] = self.conversation_histories[client_id][-max_history:]
    
    def get_arcgis_state(self) -> Dict:
        """Get current ArcGIS Pro state"""
        return self.arcgis_state
    
    def update_arcgis_state(self, state: Dict):
        """Update ArcGIS Pro state"""
        self.arcgis_state = state
        logger.info("ArcGIS Pro state updated")
    
    def start_investigation_session(self, client_id: str) -> str:
        """Start a new investigation session"""
        session_id = str(uuid.uuid4())
        
        self.investigation_sessions[f"{client_id}_{session_id}"] = {
            "id": session_id,
            "client_id": client_id,
            "start_time": datetime.now().isoformat(),
            "steps": [],
            "status": "active",
            "remaining_commands": []
        }
        
        logger.info(f"Started investigation session {session_id} for client {client_id}")
        return session_id
    
    def get_investigation_session(self, client_id: str, session_id: str) -> Optional[Dict]:
        """Get investigation session"""
        session_key = f"{client_id}_{session_id}"
        return self.investigation_sessions.get(session_key)
    
    def add_investigation_step(self, client_id: str, session_id: str, step_data: Dict):
        """Add step to investigation session"""
        session_key = f"{client_id}_{session_id}"
        if session_key in self.investigation_sessions:
            self.investigation_sessions[session_key]["steps"].append({
                "timestamp": datetime.now().isoformat(),
                "data": step_data
            })
    
    def end_investigation_session(self, client_id: str, session_id: str):
        """End investigation session"""
        session_key = f"{client_id}_{session_id}"
        if session_key in self.investigation_sessions:
            self.investigation_sessions[session_key]["status"] = "completed"
            self.investigation_sessions[session_key]["end_time"] = datetime.now().isoformat()
            logger.info(f"Ended investigation session {session_id} for client {client_id}")
    
    def set_pending_response(self, client_id: str, response: str):
        """Set pending response for client"""
        self.pending_responses[client_id] = response
    
    def get_pending_response(self, client_id: str) -> Optional[str]:
        """Get and clear pending response for client"""
        return self.pending_responses.pop(client_id, None)
    
    def store_function_result(self, function_id: str, result: Dict):
        """Store function execution result"""
        self.function_results[function_id] = result
        logger.info(f"Stored result for function {function_id}")
    
    def get_function_result(self, function_id: str) -> Optional[Dict]:
        """Get and remove function execution result"""
        return self.function_results.pop(function_id, None)
    
    def has_function_result(self, function_id: str) -> bool:
        """Check if function result is available"""
        return function_id in self.function_results
    
    def store_function_context(self, session_id: str, context: Dict):
        """Store function calling context"""
        self.function_contexts[session_id] = context
        logger.info(f"Stored function context for session {session_id}")
    
    def get_function_context(self, session_id: str) -> Optional[Dict]:
        """Get function calling context"""
        return self.function_contexts.get(session_id)
    
    def remove_function_context(self, session_id: str):
        """Remove function calling context"""
        if session_id in self.function_contexts:
            del self.function_contexts[session_id]
            logger.info(f"Removed function context for session {session_id}")
    
    def store_chain_context(self, client_id: str, context: Dict):
        """Store context for a function calling chain"""
        self.chain_contexts[client_id] = context
        logger.info(f"Stored chain context for client {client_id}")

    def get_chain_context(self, client_id: str) -> Optional[Dict]:
        """Get context for a function calling chain"""
        return self.chain_contexts.get(client_id)

    def clear_chain_context(self, client_id: str):
        """Clear context for a function calling chain"""
        if client_id in self.chain_contexts:
            del self.chain_contexts[client_id]
            logger.info(f"Cleared chain context for client {client_id}")
    
    def get_clients_by_type(self, client_type: str) -> List[str]:
        """Get all client IDs of a specific type"""
        return [client_id for client_id, ctype in self.client_types.items() if ctype == client_type]
    
    def get_active_connections_count(self) -> int:
        """Get number of active connections"""
        return len(self.active_connections)
    
    def get_client_info(self) -> Dict:
        """Get information about all connected clients"""
        return {
            "total_connections": len(self.active_connections),
            "arcgis_clients": len([c for c in self.client_types.values() if c == "arcgis_pro"]),
            "chatbot_clients": len([c for c in self.client_types.values() if c == "chatbot"]),
            "client_details": [
                {
                    "client_id": client_id[:8] + "...",  # Truncate for privacy
                    "client_type": self.client_types.get(client_id, "unknown"),
                    "history_length": len(self.conversation_histories.get(client_id, []))
                }
                for client_id in self.active_connections.keys()
            ]
        }
    
    # Cancel flag management
    def set_cancel_flag(self, client_id: str):
        """Set cancel flag for a client"""
        self.cancel_flags[client_id] = True
    
    def clear_cancel_flag(self, client_id: str):
        """Clear cancel flag for a client"""
        self.cancel_flags[client_id] = False
    
    def is_cancelled(self, client_id: str) -> bool:
        """Check if client has requested cancellation"""
        return self.cancel_flags.get(client_id, False)
    
    def send_dashboard_update(self, dashboard_layout: dict):
        """Send dashboard update to all chatbot clients."""
        import asyncio
        # Extract the dashboard_layout array and format for frontend
        charts = dashboard_layout.get("dashboard_layout", []) if isinstance(dashboard_layout, dict) else dashboard_layout
        message = {
            "type": "dashboard_update",
            "data": {"charts": charts}  # Frontend expects data.charts
        }
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        if loop.is_running():
            asyncio.ensure_future(self.broadcast_to_type("chatbot", message))
        else:
            loop.run_until_complete(self.broadcast_to_type("chatbot", message))
