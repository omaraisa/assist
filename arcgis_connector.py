# -*- coding: utf-8 -*-

import asyncio
import websockets
import json
import logging
import traceback
import time
import webbrowser
from typing import Dict
import arcpy

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ArcGISProConnector:
    """Connector class for ArcGIS Pro to FastAPI Smart Assistant"""
    
    def __init__(self, server_url="ws://localhost:8000/ws", chatbot_url="http://localhost:8000"):
        self.server_url = server_url
        self.chatbot_url = chatbot_url
        self.websocket = None
        self.project = None
        self.active_map = None
        
        # Initialize ArcGIS Pro environment
        self.initialize_arcgis_environment()
    
    def initialize_arcgis_environment(self):
        """Initialize ArcGIS Pro project and map references"""
        try:
            # Set workspace to current project's default geodatabase
            self.project = arcpy.mp.ArcGISProject("CURRENT")
            self.active_map = self.project.activeMap
            
            if self.project.defaultGeodatabase:
                arcpy.env.workspace = self.project.defaultGeodatabase
            
            logger.info("ArcGIS Pro environment initialized successfully")
            
        except Exception as e:
            logger.error(f"Error initializing ArcGIS Pro environment: {str(e)}")
            arcpy.AddError(f"Error initializing ArcGIS Pro environment: {str(e)}")
    
    def get_software_context(self) -> Dict:
        """Get current ArcGIS Pro software context"""
        try:
            if not self.active_map:
                return {"error": "No active map found"}
            
            # Get basic project info
            context = {
                "project_path": self.project.filePath if self.project else "",
                "default_gdb": self.project.defaultGeodatabase if self.project else "",
                "map_name": self.active_map.name if self.active_map else ""
            }
            
            # Get layer information (simplified for reduced payload)
            layers_info = {}
            layer_types = {}
            
            for layer in self.active_map.listLayers():
                layer_name = layer.name
                layer_types[layer_name] = self.get_layer_type_name(layer)
                
                if layer.isFeatureLayer:
                    try:
                        # Only include essential field information
                        fields = {}
                        for field in arcpy.ListFields(layer):
                            # Only include basic field info to reduce payload
                            fields[field.name] = field.type
                        
                        layers_info[layer_name] = {
                            "fields": fields,
                            "definition_query": getattr(layer, 'definitionQuery', ''),
                            "visible": layer.visible
                        }
                    except Exception as e:
                        logger.warning(f"Error getting fields for layer {layer_name}: {str(e)}")
                        layers_info[layer_name] = {
                            "fields": {},
                            "definition_query": '',
                            "visible": layer.visible
                        }
            
            # Get table information
            tables_info = {}
            for table in self.active_map.listTables():
                layer_types[table.name] = "Table"
                tables_info[table.name] = {"name": table.name}
            
            # Get basemap information
            basemap_layers = [layer.name for layer in self.active_map.listLayers() if layer.isBasemapLayer]
            
            context.update({
                "layers_info": layers_info,
                "tables_info": tables_info,
                "layer_types": layer_types,
                "basemap": basemap_layers
            })
            
            return context
            
        except Exception as e:
            logger.error(f"Error getting software context: {str(e)}")
            return {"error": f"Error getting software context: {str(e)}"}
    
    def get_layer_type_name(self, layer) -> str:
        """Get human-readable layer type name"""
        if layer.isFeatureLayer:
            return "Feature Layer"
        elif layer.isRasterLayer:
            return "Raster Layer"
        elif layer.isBasemapLayer:
            return "Basemap Layer"
        elif layer.isWebLayer:
            return "Web Layer"
        else:
            return "Other Layer"
    
    def decode_arabic_text(self, obj):
        """Recursively handle Arabic text in objects"""
        if isinstance(obj, dict):
            return {k: self.decode_arabic_text(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self.decode_arabic_text(i) for i in obj]
        elif isinstance(obj, str):
            return obj
        else:
            return obj
    
    async def execute_function(self, function_data: Dict) -> Dict:
        """Execute a spatial function and return results"""
        function_name = None
        try:
            function_name = function_data.get("function_name")
            parameters = function_data.get("parameters", {})
            
            if not function_name:
                raise Exception("Function name is required")
            
            logger.info(f"Executing function: {function_name} with parameters: {parameters}")
            arcpy.AddMessage(f"Executing function: {function_name} with parameters: {parameters}")
            
            # Import spatial functions dynamically
            import sys
            import os
            
            # Add the app directory to Python path to import spatial_functions
            app_dir = os.path.join(os.path.dirname(__file__), "app")
            logger.info(f"Determined app_dir: {app_dir}")
            if app_dir not in sys.path:
                sys.path.append(app_dir)
                logger.info(f"Added '{app_dir}' to sys.path")
            else:
                logger.info(f"'{app_dir}' already in sys.path")

            from app.spatial_functions import SpatialFunctions
            logger.info("Imported SpatialFunctions from app.spatial_functions")

            # Create spatial functions instance
            spatial_functions = SpatialFunctions()
            logger.info("Created SpatialFunctions instance")

            # Check if function exists
            if not hasattr(spatial_functions, function_name):
                logger.error(f"Function '{function_name}' not found in SpatialFunctions")
                raise Exception(f"Function '{function_name}' not found")
            logger.info(f"Function '{function_name}' found in SpatialFunctions")

            # Get the function
            func = getattr(spatial_functions, function_name)
            logger.info(f"Obtained function '{function_name}' from SpatialFunctions")

            # Execute the function
            logger.info(f"Executing '{function_name}' with parameters: {parameters}")
            result = func(**parameters)
            logger.info(f"Executed '{function_name}', result: {result}")

            # Decode any Arabic text
            result = self.decode_arabic_text(result)
            
            logger.info(f"Function {function_name} executed successfully")
            arcpy.AddMessage(f"Function {function_name} completed successfully. Result: {result}")
            
            return {
                "status": "success",
                "function_name": function_name,
                "data": result,
                "software_context": self.get_software_context()
            }
            
        except Exception as e:
            function_name_safe = function_name or "unknown"
            error_msg = f"Error executing function {function_name_safe}: {str(e)}"
            logger.error(error_msg)
            arcpy.AddError(error_msg)
            
            return {
                "status": "error",
                "function_name": function_name_safe,
                "message": error_msg,
                "software_context": self.get_software_context()
            }
    
    async def connect_and_listen(self):
        """Connect to the FastAPI server and listen for messages"""
        max_retries = 2
        retry_delay = 1
        # max_retries = 5
        # retry_delay = 3
        
        for attempt in range(1, max_retries + 1):
            try:
                logger.info(f"Connecting to FastAPI server at {self.server_url} (attempt {attempt}/{max_retries})")
                arcpy.AddMessage(f"Connecting to Smart Assistant server (attempt {attempt}/{max_retries})")
                
                async with websockets.connect(self.server_url) as websocket:
                    self.websocket = websocket
                    logger.info("Successfully connected to FastAPI server")
                    arcpy.AddMessage("Successfully connected to Smart Assistant server")
                    
                    # Register as ArcGIS Pro client
                    await self.send_message({
                        "type": "client_register",
                        "client_type": "arcgis_pro"
                    })
                    
                    # Listen for messages
                    async for message in websocket:
                        await self.handle_message(json.loads(message))
                        
                return  # Successfully connected and processed
                
            except (ConnectionRefusedError, websockets.exceptions.WebSocketException) as e:
                logger.warning(f"Connection attempt {attempt} failed: {str(e)}")
                arcpy.AddWarning(f"Connection attempt {attempt} failed: {str(e)}")
                
                if attempt < max_retries:
                    logger.info(f"Retrying in {retry_delay} seconds...")
                    await asyncio.sleep(retry_delay)
                    retry_delay *= 1.5  # Exponential backoff
                else:
                    error_msg = "Failed to connect to Smart Assistant server after multiple attempts"
                    logger.error(error_msg)
                    arcpy.AddError(error_msg)
                    raise
            
            except Exception as e:
                error_msg = f"Unexpected error during connection: {str(e)}"
                logger.error(error_msg)
                arcpy.AddError(error_msg)
                raise
    
    async def send_message(self, message: Dict):
        """Send message to the FastAPI server"""
        if self.websocket:
            try:
                await self.websocket.send(json.dumps(message))
                logger.debug(f"Sent message: {message.get('type', 'unknown')}")
            except Exception as e:
                logger.error(f"Error sending message: {str(e)}")
    
    async def handle_message(self, message: Dict):
        """Handle incoming messages from the FastAPI server"""
        try:
            message_type = message.get("type")
            logger.debug(f"Received message type: {message_type}")
            
            if message_type == "get_software_state":
                # Send current software state
                software_state = self.get_software_context()
                await self.send_message({
                    "type": "software_state",
                    "data": software_state                })
                logger.info("Sent software state to server")
                
            elif message_type == "execute_function":
                # Execute spatial function
                logger.info(f"Received execute_function request: {message}")
                result = await self.execute_function(message)
                
                # Send result back
                response = {
                    "type": "function_response",
                    "session_id": message.get("session_id"),
                    "source_client": message.get("source_client"),
                    **result
                }
                
                logger.info(f"Sending function response: session_id={response.get('session_id')}, source_client={response.get('source_client')}")
                await self.send_message(response)
                
            elif message_type == "heartbeat":
                # Respond to heartbeat
                await self.send_message({"type": "heartbeat_ack"})
                
            else:
                logger.warning(f"Unknown message type: {message_type}")
                
        except Exception as e:
            error_msg = f"Error handling message: {str(e)}"
            logger.error(error_msg)
            arcpy.AddError(error_msg)
            
            # Send error response
            await self.send_message({
                "type": "error",
                "message": error_msg
            })
    
    def run(self):
        """Main method to run the connector"""
        try:
            # Open the chatbot interface in browser
            logger.info(f"Opening Smart Assistant interface at {self.chatbot_url}")
            arcpy.AddMessage(f"Opening Smart Assistant interface at {self.chatbot_url}")
            webbrowser.open(self.chatbot_url)
            
            # Give the server time to start
            time.sleep(3)
            
            # Run the WebSocket connection
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            try:
                loop.run_until_complete(self.connect_and_listen())
            finally:
                loop.close()
                
        except Exception as e:
            error_msg = f"Error running ArcGIS Pro connector: {str(e)}"
            logger.error(error_msg)
            arcpy.AddError(error_msg)
            arcpy.AddError(traceback.format_exc())

# Main execution
if __name__ == "__main__":
    connector = ArcGISProConnector()
    connector.run()
