# -*- coding: utf-8 -*-
"""  
ArcGIS Pro Smart Assistant Connector - Portable Version
This script connects ArcGIS Pro to the FastAPI-based Smart Assistant server
Works both within ArcGIS Pro environment and standalone
"""

import asyncio
import websockets
import json
import logging
import traceback
import time
import webbrowser
import sys
import os
from typing import Dict, Optional, Any
import concurrent.futures
from pathlib import Path

# Add the project directory to Python path for imports
PROJECT_DIR = Path(__file__).parent
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

# Try to import arcpy, handle gracefully if not available
try:
    import arcpy
    ARCPY_AVAILABLE = True
    logger = logging.getLogger(__name__)
    logger.info("ArcPy is available - full GIS functionality enabled")
except ImportError:
    ARCPY_AVAILABLE = False
    
    # Create a mock arcpy for non-ArcGIS environments
    class MockArcpy:
        """Mock ArcPy class for environments without ArcGIS Pro"""
        
        class mp:
            @staticmethod
            def ArcGISProject(path):
                raise ImportError("ArcPy not available - please run from ArcGIS Pro")
        
        @staticmethod
        def AddMessage(msg):
            print(f"[ArcGIS] {msg}")
            
        @staticmethod
        def AddError(msg):
            print(f"[ERROR] {msg}")
            
        env = type('obj', (object,), {'workspace': None})()
    
    arcpy = MockArcpy()
    print("[WARNING] ArcPy not available - limited functionality")
    print("[INFO] For full GIS functionality, run this script from within ArcGIS Pro")

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
        self.arcpy_available = ARCPY_AVAILABLE
        
        # Initialize ArcGIS Pro environment if available
        if self.arcpy_available:
            self.initialize_arcgis_environment()
        else:
            logger.warning("Running in standalone mode - ArcGIS Pro features limited")
    
    def initialize_arcgis_environment(self):
        """Initialize ArcGIS Pro project and map references"""
        if not self.arcpy_available:
            logger.warning("Cannot initialize ArcGIS environment - ArcPy not available")
            return
            
        try:
            # Set workspace to current project's default geodatabase
            self.project = arcpy.mp.ArcGISProject("CURRENT")
            self.active_map = self.project.activeMap
            
            if self.project.defaultGeodatabase:
                arcpy.env.workspace = self.project.defaultGeodatabase
            
            logger.info("ArcGIS Pro environment initialized successfully")
            
        except Exception as e:
            logger.error(f"Error initializing ArcGIS Pro environment: {str(e)}")
            if self.arcpy_available:
                arcpy.AddError(f"Error initializing ArcGIS Pro environment: {str(e)}")
            self.arcpy_available = False  # Disable ArcPy features if initialization fails

    def get_layer_type_name(self, layer) -> str:
        """Get human-readable layer type name"""
        if not self.arcpy_available:
            return "Unknown (ArcPy not available)"
            
        try:
            if hasattr(layer, 'isFeatureLayer') and layer.isFeatureLayer:
                return "Feature Layer"
            elif hasattr(layer, 'isRasterLayer') and layer.isRasterLayer:
                return "Raster Layer"
            elif hasattr(layer, 'isBasemapLayer') and layer.isBasemapLayer:
                return "Basemap Layer"
            elif hasattr(layer, 'isGroupLayer') and layer.isGroupLayer:
                return "Group Layer"
            else:
                return "Layer"
        except:
            return "Unknown"

    def decode_arabic_text(self, obj):
        """Recursively handle Arabic text in objects"""
        if isinstance(obj, dict):
            return {key: self.decode_arabic_text(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [self.decode_arabic_text(item) for item in obj]
        elif isinstance(obj, str):
            try:
                # Try to properly encode/decode Arabic text
                return obj.encode('utf-8').decode('utf-8')
            except:
                return obj
        else:
            return obj

    def get_software_context(self) -> Dict:
        """Get current ArcGIS Pro software context"""
        if not self.arcpy_available:
            return {
                "error": "ArcPy not available",
                "message": "Please run from ArcGIS Pro for full functionality",
                "mode": "standalone"
            }
            
        try:
            if not self.active_map:
                return {"error": "No active map found"}
            
            # Get basic project info
            context = {
                "project_path": self.project.filePath if self.project else "",
                "default_gdb": self.project.defaultGeodatabase if self.project else "",
                "map_name": self.active_map.name if self.active_map else "",
                "mode": "arcgis_pro"
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

    async def execute_function(self, function_data: Dict) -> Dict:
        """Execute a spatial function and return results"""
        function_name = None
        try:
            function_name = function_data.get("function_name")
            parameters = function_data.get("parameters", {})
            
            if not function_name:
                raise Exception("Function name is required")
            
            logger.info(f"Executing function: {function_name} with parameters: {parameters}")
            if self.arcpy_available:
                arcpy.AddMessage(f"Executing function: {function_name}")
            
            # Check if ArcPy is required for this function
            if not self.arcpy_available:
                return {
                    "status": "error",
                    "function_name": function_name,
                    "message": "ArcPy not available - please run from ArcGIS Pro for spatial functions",
                    "software_context": self.get_software_context()
                }
            
            # Import spatial functions dynamically
            app_dir = PROJECT_DIR / "app"
            if str(app_dir) not in sys.path:
                sys.path.append(str(app_dir))
            
            from spatial_functions import SpatialFunctions
            
            # Create spatial functions instance
            spatial_functions = SpatialFunctions()
            
            # Check if function exists
            if not hasattr(spatial_functions, function_name):
                raise Exception(f"Function '{function_name}' not found")
            
            # Get the function
            func = getattr(spatial_functions, function_name)
            
            # Execute the function
            result = func(**parameters)
            
            # Decode any Arabic text
            result = self.decode_arabic_text(result)
            
            logger.info(f"Function {function_name} executed successfully")
            if self.arcpy_available:
                arcpy.AddMessage(f"Function {function_name} completed successfully")
            
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
            if self.arcpy_available:
                arcpy.AddError(error_msg)
            
            return {
                "status": "error",
                "function_name": function_name_safe,
                "message": error_msg,
                "software_context": self.get_software_context()
            }

    async def connect_and_listen(self):
        """Connect to the FastAPI server and listen for messages"""
        max_retries = 5
        retry_delay = 2
        
        for attempt in range(max_retries):
            try:
                logger.info(f"Attempting to connect to server... (attempt {attempt + 1}/{max_retries})")
                
                async with websockets.connect(
                    self.server_url,
                    ping_interval=20,
                    ping_timeout=10,
                    close_timeout=10
                ) as websocket:
                    self.websocket = websocket
                    logger.info("Connected to FastAPI server successfully!")
                    
                    # Send initial connection message with software context
                    await self.send_message({
                        "type": "arcgis_connected",
                        "software_context": self.get_software_context(),
                        "arcpy_available": self.arcpy_available,
                        "timestamp": time.time()
                    })
                    
                    # Listen for messages
                    async for message in websocket:
                        try:
                            data = json.loads(message)
                            await self.handle_message(data)
                        except json.JSONDecodeError:
                            logger.error(f"Invalid JSON received: {message}")
                        except Exception as e:
                            logger.error(f"Error handling message: {str(e)}")
                            
            except websockets.exceptions.ConnectionClosed:
                logger.warning("Connection closed by server")
                break
            except Exception as e:
                logger.error(f"Connection attempt {attempt + 1} failed: {str(e)}")
                if attempt < max_retries - 1:
                    logger.info(f"Retrying in {retry_delay} seconds...")
                    await asyncio.sleep(retry_delay)
                    retry_delay *= 2  # Exponential backoff
                else:
                    logger.error("Max retries exceeded. Unable to connect to server.")
                    raise

    async def send_message(self, message: Dict):
        """Send message to the FastAPI server"""
        if self.websocket:
            try:
                await self.websocket.send(json.dumps(message))
            except Exception as e:
                logger.error(f"Error sending message: {str(e)}")

    async def handle_message(self, message: Dict):
        """Handle incoming messages from the server"""
        try:
            message_type = message.get("type")
            
            if message_type == "execute_function":
                # Execute spatial function
                result = await self.execute_function(message.get("data", {}))
                
                # Send result back to server
                await self.send_message({
                    "type": "function_result",
                    "data": result,
                    "request_id": message.get("request_id"),
                    "timestamp": time.time()
                })
                
            elif message_type == "get_context":
                # Send current software context
                await self.send_message({
                    "type": "context_update",
                    "data": self.get_software_context(),
                    "request_id": message.get("request_id"),
                    "timestamp": time.time()
                })
                
            elif message_type == "ping":
                # Respond to ping
                await self.send_message({
                    "type": "pong",
                    "request_id": message.get("request_id"),
                    "timestamp": time.time()
                })
                
            else:
                logger.warning(f"Unknown message type: {message_type}")
                
        except Exception as e:
            logger.error(f"Error handling message: {str(e)}")
            error_response = {
                "type": "error",
                "message": str(e),
                "request_id": message.get("request_id"),
                "timestamp": time.time()
            }
            await self.send_message(error_response)

    def run(self):
        """Main execution method"""
        try:
            logger.info("Starting ArcGIS Pro Smart Assistant Connector")
            logger.info(f"Server URL: {self.server_url}")
            logger.info(f"ArcPy Available: {self.arcpy_available}")
            
            if not self.arcpy_available:
                logger.warning("Running in limited mode - some features may not be available")
                print("\n" + "="*60)
                print("  WARNING: ArcPy not available")
                print("  For full functionality, run this script from ArcGIS Pro")
                print("="*60 + "\n")
            
            # Try to open the web interface
            try:
                webbrowser.open(self.chatbot_url)
                logger.info(f"Opened web interface: {self.chatbot_url}")
            except Exception as e:
                logger.warning(f"Could not open web browser: {str(e)}")
                logger.info(f"Please manually open: {self.chatbot_url}")
            
            # Run the connection loop
            asyncio.run(self.connect_and_listen())
            
        except KeyboardInterrupt:
            logger.info("Connection interrupted by user")
        except Exception as e:
            logger.error(f"Error in main execution: {str(e)}")
            logger.error(traceback.format_exc())
        finally:
            logger.info("ArcGIS Pro Smart Assistant Connector stopped")

# Main execution
if __name__ == "__main__":
    # Check if we're running from the correct directory
    if not (PROJECT_DIR / "app").exists():
        print(f"[ERROR] Cannot find app directory in {PROJECT_DIR}")
        print("[INFO] Please run this script from the SmartAssistant project root directory")
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Check if server is likely running
    import socket
    def check_server_running(host='localhost', port=8000):
        try:
            with socket.create_connection((host, port), timeout=3):
                return True
        except:
            return False
    
    if not check_server_running():
        print("\n" + "="*60)
        print("  WARNING: Server doesn't appear to be running")
        print("  Please start the server first:")
        print("  - Run start_smartassistant.bat")
        print("  - Or: python run.py")
        print("="*60)
        
        choice = input("\nContinue anyway? (y/N): ").strip().lower()
        if choice != 'y':
            sys.exit(0)
    
    connector = ArcGISProConnector()
    connector.run()
