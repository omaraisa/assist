
"""
Spatial Functions Module - GIS analysis operations
"""

import os
import logging
import math
import json
import asyncio
import statistics
import re
from typing import Dict, Tuple, List
from .ai.function_declarations import FunctionDeclaration
from copy import deepcopy

# Import arcpy only when available (in ArcGIS Pro environment)
try:
    import arcpy
    ARCPY_AVAILABLE = True
except ImportError:
    ARCPY_AVAILABLE = False
    # Create a mock arcpy for testing purposes
    class MockArcpy:
        def __getattr__(self, name):
            def mock_method(*args, **kwargs):
                raise ImportError("ArcPy is not available in this environment")
            return mock_method
    arcpy = MockArcpy()

# Configure logging to write to the functions_log.txt file
from pathlib import Path
LOG_FILE_PATH = Path(__file__).parent.parent / "logs" / "system.log"
LOG_FILE_PATH.parent.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH, encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SpatialFunctions:
    # Class variable for available functions - accessible without instance
    AVAILABLE_FUNCTIONS = {
        1: "select_by_attribute",
        2: "select_by_location",
        3: "get_field_statistics",
        4: "get_layer_summary",
        5: "calculate_area",
        6: "calculate_length",
        7: "get_centroid",
        8: "create_buffer",
        9: "spatial_join",
        10: "clip_layer",
        11: "calculate_distance",
        12: "get_current_project_path",
        13: "get_default_db_path",
        14: "get_field_definitions",
        15: "get_layer_type",
        16: "get_list_of_layer_fields",
        17: "get_data_source_info",
        18: "create_nearest_neighbor_layer",
        19: "get_unique_values_count",
        20: "calculate_empty_values",
        21: "get_map_layers_info",
        22: "get_map_tables_info",
        23: "get_values_frequency",
        24: "get_value_frequency",
        25: "get_coordinate_system",
        26: "get_attribute_table",
        27: "get_field_domain_values",
        28: "calculate_new_field",
        29: "analyze_layer_fields",
        30: "generate_smart_dashboard_layout",
        31: "optimize_dashboard_layout",
        32: "recommend_chart_types",
        33: "plan_dashboard_layout",
        34: "get_current_dashboard_layout",
        35: "get_field_stories_and_samples",
        36: "get_current_dashboard_charts",
        37: "update_dashboard_charts"
    }
    
    def __init__(self, websocket_manager=None):
        self.websocket_manager = websocket_manager
        self.supported_formats = ['.shp', '.geojson', '.kml', '.gpx', '.gml']
        

    def get_functions_declaration(self, function_ids: list[int]) -> dict:
        """
        Returns the signature and description of another function by providing its function_id (integer).
        """
        functions_declaration = FunctionDeclaration.functions_declarations
        
        # Filter and return only the requested function declarations
        result = {}
        for func_id in function_ids:
            if func_id in self.AVAILABLE_FUNCTIONS:
                func_name = self.AVAILABLE_FUNCTIONS[func_id]
                if func_name in functions_declaration:
                    result[func_name] = functions_declaration[func_name]
            
        return result
        
        
    def select_by_attribute(self, layer_name, where_clause, selection_type="NEW_SELECTION"):
        """Execute attribute-based selection"""
        logger.info(f"Executing select_by_attribute with layer: {layer_name}, where: {where_clause}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            
            # Execute selection
            arcpy.SelectLayerByAttribute_management(lyr, selection_type, where_clause)
            
            # Get selection count
            selected_count = int(arcpy.GetCount_management(lyr)[0])
            
            result = {
                "function_executed": "select_by_attribute",
                "layer_name": layer_name,
                "selected_features": selected_count,
                "success": True
            }
            logger.info(f"select_by_attribute result: {result}")
            return result
        except Exception as e:
            logger.error(f"select_by_attribute error: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def select_by_location(self, input_layer, select_layer, relationship="INTERSECT"):
        """Execute spatial selection"""
        logger.info(f"Executing select_by_location with input: {input_layer}, select: {select_layer}, relationship: {relationship}")
        try:
            # List of supported spatial relationships in arcpy.SelectLayerByLocation_management
            supported_relationships = [
                "INTERSECT", "WITHIN", "CONTAINS", "WITHIN_A_DISTANCE", 
                "WITHIN_A_DISTANCE_GEODESIC", "HAVE_THEIR_CENTER_IN", 
                "COMPLETELY_CONTAINS", "COMPLETELY_WITHIN", "CLOSEST", 
                "BOUNDARY_TOUCHES", "SHARE_A_LINE_SEGMENT_WITH", "CROSSED_BY_THE_OUTLINE_OF", 
                "CONTAINS_CLEMENTINI", "WITHIN_CLEMENTINI"
            ]
            
            # Check if provided relationship is supported, otherwise use default
            if relationship.upper() not in supported_relationships:
                logger.warning(f"Relationship '{relationship}' not supported. Falling back to 'INTERSECT'")
                relationship = "INTERSECT"
            else:
                relationship = relationship.upper()
                
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            
            input_lyr = None
            select_lyr = None
            
            for lyr in map_obj.listLayers():
                if lyr.name == input_layer:
                    input_lyr = lyr
                if lyr.name == select_layer:
                    select_lyr = lyr
            
            if not input_lyr:
                return {"success": False, "error": f"Input layer {input_layer} not found"}
            if not select_lyr:
                return {"success": False, "error": f"Select layer {select_layer} not found"}
            
            # Execute spatial selection
            arcpy.SelectLayerByLocation_management(input_lyr, relationship, select_lyr)
            
            # Get selection count
            selected_count = int(arcpy.GetCount_management(input_lyr)[0])
            
            result = {
                "function_executed": "select_by_location",
                "input_layer": input_layer,
                "select_layer": select_layer,
                "relationship": relationship,
                "selected_features": selected_count,
                "success": True
            }
            logger.info(f"select_by_location result: {result}")
            return result
        except Exception as e:
            logger.error(f"select_by_location error: {str(e)}")
            return {"success": False, "error": str(e)}

    def get_field_statistics(self, layer_name, field_name, where_clause=None):
        """Calculate field statistics"""
        logger.info(f"Executing get_field_statistics with layer: {layer_name}, field: {field_name}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            
            # Check if field exists
            field_names = [field.name for field in arcpy.ListFields(lyr)]
            if field_name not in field_names:
                return {"success": False, "error": f"Field {field_name} not found"}
            
            # Collect values
            values = []
            cursor_fields = [field_name]
            
            for row in arcpy.da.SearchCursor(lyr, cursor_fields, where_clause):
                if row[0] is not None:
                    try:
                        values.append(float(row[0]))
                    except (ValueError, TypeError):
                        continue
            
            if not values:
                return {"success": False, "error": "No numeric values found"}
            
            # Calculate statistics
            import statistics
            result = {
                "function_executed": "get_field_statistics",
                "layer_name": layer_name,
                "field_name": field_name,
                "where_clause": where_clause,
                "success": True,
                "statistics": {
                    "count": len(values),
                    "total": sum(values),
                    "mean": statistics.mean(values),
                    "min": min(values),
                    "max": max(values),
                    "std_dev": statistics.stdev(values) if len(values) > 1 else 0,
                    "median": statistics.median(values)
                }
            }
            logger.info(f"get_field_statistics result: {result}")
            return result
        except Exception as e:
            logger.error(f"get_field_statistics error: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def get_layer_summary(self, layer_name):
        """Get comprehensive layer summary"""
        logger.info(f"Executing get_layer_summary with layer: {layer_name}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            
            desc = arcpy.Describe(lyr)
            fields = arcpy.ListFields(lyr)
            feature_count = int(arcpy.GetCount_management(lyr)[0])
            
            field_info = []
            for field in fields:
                field_info.append({
                    "name": field.name,
                    "type": field.type,
                    "alias": field.aliasName
                })
            
            result = {
                "function_executed": "get_layer_summary",
                "layer_name": layer_name,
                "success": True,
                "summary": {
                    "geometry_type": desc.shapeType if hasattr(desc, 'shapeType') else "Table",
                    "feature_count": feature_count,
                    "field_count": len(field_info),
                    "data_source": desc.catalogPath,
                    "spatial_reference": desc.spatialReference.name if hasattr(desc, 'spatialReference') else None,
                    "fields": field_info
                }
            }
            logger.info(f"get_layer_summary result: {result}")
            return result
        except Exception as e:
            logger.error(f"get_layer_summary error: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def calculate_area(self, layer_name: str, units: str = "square_meters") -> Dict:
        """Calculate area for polygon features"""
        logger.info(f"Calculating area for layer: {layer_name}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            
            desc = arcpy.Describe(lyr)
            if desc.shapeType != "Polygon":
                return {"success": False, "error": f"Layer {layer_name} is not a polygon layer"}
            
            areas = []
            for row in arcpy.da.SearchCursor(lyr, ["SHAPE@AREA"]):
                if row[0] is not None:
                    area = row[0]
                    # Convert units if needed
                    if units == "square_kilometers":
                        area = area / 1000000
                    elif units == "acres":
                        area = area * 0.000247105
                    elif units == "hectares":
                        area = area * 0.0001
                    areas.append(area)
            
            if not areas:
                return {"success": False, "error": "No area values found"}
            
            result = {
                "function_executed": "calculate_area",
                "layer_name": layer_name,
                "units": units,
                "success": True,
                "areas": {
                    "total_area": sum(areas),
                    "average_area": sum(areas) / len(areas),
                    "min_area": min(areas),
                    "max_area": max(areas),
                    "feature_count": len(areas)
                }
            }
            logger.info(f"Area calculation completed: {result}")
            return result
        except Exception as e:
            logger.error(f"calculate_area error: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def calculate_length(self, layer_name: str, units: str = "meters") -> Dict:
        """Calculate length for line features"""
        logger.info(f"Calculating length for layer: {layer_name}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            
            desc = arcpy.Describe(lyr)
            if desc.shapeType != "Polyline":
                return {"success": False, "error": f"Layer {layer_name} is not a polyline layer"}
            
            lengths = []
            for row in arcpy.da.SearchCursor(lyr, ["SHAPE@LENGTH"]):
                if row[0] is not None:
                    length = row[0]
                    # Convert units if needed
                    if units == "kilometers":
                        length = length / 1000
                    elif units == "feet":
                        length = length * 3.28084
                    elif units == "miles":
                        length = length / 1609.34
                    lengths.append(length)
            
            if not lengths:
                return {"success": False, "error": "No length values found"}
            
            result = {
                "function_executed": "calculate_length",
                "layer_name": layer_name,
                "units": units,
                "success": True,
                "lengths": {
                    "total_length": sum(lengths),
                    "average_length": sum(lengths) / len(lengths),
                    "min_length": min(lengths),
                    "max_length": max(lengths),
                    "feature_count": len(lengths)
                }
            }
            logger.info(f"Length calculation completed: {result}")
            return result
        except Exception as e:
            logger.error(f"calculate_length error: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def get_centroid(self, layer_name: str) -> Dict:
        """Get centroid coordinates for all features in a layer"""
        logger.info(f"Getting centroids for all features in layer: {layer_name}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            
            centroids = []
            
            for row in arcpy.da.SearchCursor(lyr, ["OBJECTID", "SHAPE@"]):
                centroid = row[1].centroid
                centroids.append({
                    "objectid": row[0],
                    "x": centroid.X,
                    "y": centroid.Y
                })
            
            result = {
                "function_executed": "get_centroid",
                "layer_name": layer_name,
                "success": True,
                "feature_count": len(centroids),
                "centroids": centroids
            }
            logger.info(f"Centroid calculation completed: {len(centroids)} features")
            return result
        except Exception as e:
            logger.error(f"get_centroid error: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def create_buffer(self, layer_name: str, distance: float, units: str = "meters") -> Dict:
        """Create buffer around features"""
        logger.info(f"Creating buffer for layer: {layer_name}, distance: {distance} {units}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            
            # Find the target layer
            target_layer = None
            for layer in map_obj.listLayers():
                if layer.name == layer_name:
                    target_layer = layer
                    break
            
            if not target_layer:
                return {"success": False, "error": f"Layer '{layer_name}' not found in the map"}
            
            # Create output feature class name
            output_name = f"{layer_name.replace(' ', '_')}_Buffer_{int(distance)}{units}"
            output_fc = os.path.join(aprx.defaultGeodatabase, output_name)
            output_fc = arcpy.CreateUniqueName(output_fc)
            
            # Convert units to arcpy format
            unit_mapping = {
                "meters": "METERS",
                "kilometers": "KILOMETERS", 
                "feet": "FEET",
                "miles": "MILES"
            }
            arcpy_units = unit_mapping.get(units.lower(), "METERS")
            
            # Create buffer
            arcpy.analysis.Buffer(
                in_features=target_layer,
                out_feature_class=output_fc,
                buffer_distance_or_field=f"{distance} {arcpy_units}",
                line_side="FULL",
                line_end_type="ROUND",
                dissolve_option="NONE"
            )
            
            # Add the buffer layer to the map
            buffer_layer = map_obj.addDataFromPath(output_fc)
            
            result = {
                "function_executed": "create_buffer",
                "layer_name": layer_name,
                "success": True,
                "output_layer": output_name,
                "output_path": output_fc,
                "buffer_distance": distance,
                "buffer_units": units
            }
            
            logger.info(f"Buffer created successfully: {result}")
            return result
            
        except Exception as e:
            logger.error(f"create_buffer error: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def spatial_join(self, target_layer: str, join_layer: str, join_operation: str = "intersect") -> Dict:
        """Perform spatial join between two layers"""
        logger.info(f"Performing spatial join: {target_layer} with {join_layer}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            
            target_lyr = None
            join_lyr = None
            
            for lyr in map_obj.listLayers():
                if lyr.name == target_layer:
                    target_lyr = lyr
                if lyr.name == join_layer:
                    join_lyr = lyr
            
            if not target_lyr:
                return {"success": False, "error": f"Target layer {target_layer} not found"}
            if not join_lyr:
                return {"success": False, "error": f"Join layer {join_layer} not found"}
            
            # Map join operation to arcpy parameter
            join_op_map = {
                "intersect": "INTERSECT",
                "within": "WITHIN",
                "contains": "CONTAINS",
                "closest": "CLOSEST"
            }
            arcpy_join_op = join_op_map.get(join_operation.lower(), "INTERSECT")
              # Create output path
            output_name = f"{target_layer.replace(' ', '_')}_ai"
            default_gdb = aprx.defaultGeodatabase
            output_path = os.path.join(default_gdb, output_name)
            # Perform spatial join
            arcpy.SpatialJoin_analysis(target_lyr, join_lyr, output_path, 
                                     match_option=arcpy_join_op)
            
            # Count results
            joined_count = int(arcpy.GetCount_management(output_path)[0])
            original_count = int(arcpy.GetCount_management(target_lyr)[0])
            unmatched_count = original_count - joined_count
            # Add the joined layer to the map
            joined_layer = map_obj.addDataFromPath(output_path)
            
            result = {
                "function_executed": "spatial_join",
                "target_layer": target_layer,
                "join_layer": join_layer,
                "join_operation": join_operation,
                "success": True,
                "output": {
                    "joined_features": joined_count,
                    "unmatched_features": unmatched_count,
                    "output_layer": output_name,
                    "output_path": output_path
                }
            }
            logger.info(f"Spatial join completed: {result}")
            return result
        except Exception as e:
            logger.error(f"spatial_join error: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def clip_layer(self, input_layer: str, clip_layer: str) -> Dict:
        """Clip input layer by clip layer boundary"""
        logger.info(f"Clipping layer: {input_layer} with {clip_layer}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            
            input_lyr = None
            clip_lyr = None
            
            for lyr in map_obj.listLayers():
                if lyr.name == input_layer:
                    input_lyr = lyr
                if lyr.name == clip_layer:
                    clip_lyr = lyr
            
            if not input_lyr:
                return {"success": False, "error": f"Input layer {input_layer} not found"}
            if not clip_lyr:
                return {"success": False, "error": f"Clip layer {clip_layer} not found"}
              # Create output path
            output_name = f"{input_layer.replace(' ', '_')}_ai"
            default_gdb = aprx.defaultGeodatabase
            output_path = os.path.join(default_gdb, output_name)
            # Add the joined layer to the map
            clipped_layer = map_obj.addDataFromPath(output_path)
            
            # Get original feature count
            original_count = int(arcpy.GetCount_management(input_lyr)[0])
            
            # Perform clip
            arcpy.Clip_analysis(input_lyr, clip_lyr, output_path)
            
            # Get clipped feature count
            clipped_count = int(arcpy.GetCount_management(output_path)[0])
            
            result = {
                "function_executed": "clip_layer",
                "input_layer": input_layer,
                "clip_layer": clip_layer,
                "success": True,
                "output": {
                    "clipped_features": clipped_count,
                    "original_features": original_count,
                    "output_layer": output_name,
                    "output_path": output_path
                }
            }
            logger.info(f"Clipping completed: {result}")
            return result
        except Exception as e:
            logger.error(f"clip_layer error: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def calculate_distance(self, point1: Tuple[float, float], point2: Tuple[float, float], units: str = "meters") -> float:
        """
        Calculate distance between two points using Haversine formula.
        
        Args:
            point1: Tuple of (longitude, latitude) for first point
            point2: Tuple of (longitude, latitude) for second point
            units: Output units ('meters', 'kilometers', 'miles')
        
        Returns:
            float: Distance between points
        """
        try:
            import math
            
            lon1, lat1 = point1
            lon2, lat2 = point2
            
            # Convert to radians
            lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
            
            # Haversine formula
            dlat = lat2 - lat1
            dlon = lon2 - lon1
            a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
            c = 2 * math.asin(math.sqrt(a))
            
            # Earth radius in meters
            r = 6371000
            distance = c * r
            
            # Convert units
            if units == "kilometers":
                distance = distance / 1000
            elif units == "miles":
                distance = distance / 1609.34
            
            return distance
            
        except Exception as e:
            logger.error(f"calculate_distance error: {str(e)}")
            return 0.0

        
    def get_current_project_path(self) -> Dict:
        """Get the current ArcGIS Pro project path"""
        logger.info("Getting current ArcGIS Pro project path")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            path = aprx.filePath
            result = {
                "function_executed": "get_current_project_path",
                "success": True,
                "project_path": path
            }
            logger.info(f"Current project path: {path}")
            return result
        except Exception as e:
            logger.error(f"get_current_project_path error: {str(e)}")
            return {"success": False, "error": str(e)}

    def get_default_db_path(self) -> Dict:
        """Get the default geodatabase path for the current ArcGIS Pro project"""
        logger.info("Getting default geodatabase path")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            default_gdb = aprx.defaultGeodatabase
            result = {
                "function_executed": "get_default_db_path",
                "success": True,
                "default_geodatabase": default_gdb
            }
            logger.info(f"Default geodatabase: {default_gdb}")
            return result
        except Exception as e:
            logger.error(f"get_default_db_path error: {str(e)}")
            return {"success": False, "error": str(e)}

    def get_field_definitions(self, layer_name: str) -> Dict:
        """Get field definitions for a given layer"""
        logger.info(f"Getting field definitions for layer: {layer_name}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            
            fields = []
            for field in arcpy.ListFields(lyr):
                fields.append({
                    "name": field.name,
                    "type": field.type,
                    "length": field.length,
                    "alias": field.aliasName,
                    "nullable": field.isNullable
                })
            
            result = {
                "function_executed": "get_field_definitions",
                "layer_name": layer_name,
                "success": True,
                "fields": fields
            }
            logger.info(f"Field definitions: {fields}")
            return result
        except Exception as e:
            logger.error(f"get_field_definitions error: {str(e)}")
            return {"success": False, "error": str(e)}

    def get_layer_type(self, layer_name: str) -> Dict:
        """
        Get the type of a layer (Feature Layer, Raster, LAS, CAD, KML, Table, Service, etc.)
        """
        logger.info(f"Getting layer type for: {layer_name}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break

            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}

            desc = arcpy.Describe(lyr)
            # Try to detect type
            layer_type = None

            # LAS Dataset
            if hasattr(desc, "datasetType") and desc.datasetType == "LAS Dataset":
                layer_type = "LAS Dataset"
            # Raster
            elif hasattr(desc, "dataType") and desc.dataType in ["RasterLayer", "MosaicLayer"]:
                layer_type = "Raster"
            # CAD
            elif hasattr(desc, "dataType") and "CAD" in desc.dataType:
                layer_type = "CAD"
            # KML
            elif hasattr(desc, "dataType") and desc.dataType == "KMLLayer":
                layer_type = "KML"
            # Feature Layer (vector)
            elif hasattr(desc, "shapeType"):
                layer_type = f"Feature Layer ({desc.shapeType})"
            # Table
            elif hasattr(desc, "dataType") and desc.dataType == "Table":
                layer_type = "Table"
            # Service Layer
            elif hasattr(desc, "serviceProperties"):
                layer_type = "Service Layer"
            # Imagery
            elif hasattr(desc, "dataType") and desc.dataType == "RasterDataset":
                layer_type = "Imagery"
            # Fallback to dataType or datasetType
            elif hasattr(desc, "dataType"):
                layer_type = desc.dataType
            elif hasattr(desc, "datasetType"):
                layer_type = desc.datasetType
            else:
                layer_type = "Unknown"

            result = {
                "function_executed": "get_layer_type",
                "layer_name": layer_name,
                "success": True,
                "layer_type": layer_type
            }
            logger.info(f"Layer type: {layer_type}")
            return result
        except Exception as e:
            logger.error(f"get_layer_type error: {str(e)}")
            return {"success": False, "error": str(e)}

    def get_list_of_layer_fields(self, layer_name: str) -> Dict:
        """Get a list of field names for a given layer"""
        logger.info(f"Getting list of fields for layer: {layer_name}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            
            field_names = [field.name for field in arcpy.ListFields(lyr)]
            
            result = {
                "function_executed": "get_list_of_layer_fields",
                "layer_name": layer_name,
                "success": True,
                "fields": field_names
            }
            logger.info(f"Field names: {field_names}")
            return result
        except Exception as e:
            logger.error(f"get_list_of_layer_fields error: {str(e)}")
            return {"success": False, "error": str(e)}
        
    def get_data_source_info(self, layer_name: str) -> Dict:
        """Get data source information for a given layer"""
        logger.info(f"Getting data source info for: {layer_name}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            
            desc = arcpy.Describe(lyr)
            data_source = desc.dataSource if hasattr(desc, 'dataSource') else desc.catalogPath
            
            result = {
                "function_executed": "get_data_source_info",
                "layer_name": layer_name,
                "success": True,
                "data_source": data_source
            }
            logger.info(f"Data source: {data_source}")
            return result
        except Exception as e:
            logger.error(f"get_data_source_info error: {str(e)}")
            return {"success": False, "error": str(e)}
        
    def create_nearest_neighbor_layer(self, layer_name: str, id_field: str = "OBJECTID") -> Dict:
        """
        Creates a new layer with nearest neighbor distance and nearest neighbor id fields.
        Returns statistics on the nearest distance field.
        """

        logger.info(f"Creating nearest neighbor layer for: {layer_name}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}            # Prepare output
            output_name = f"{layer_name.replace(' ', '_')}_ai"
            default_gdb = aprx.defaultGeodatabase
            output_path = os.path.join(default_gdb, output_name)
            # Add the layer to the map
            ouput_layer = map_obj.addDataFromPath(output_path)

            # Copy features to new layer
            arcpy.CopyFeatures_management(lyr, output_path)

            # Add fields for nearest neighbor id and distance
            nn_id_field = "NEAREST_ID"
            nn_dist_field = "NEAREST_DIST"
            arcpy.AddField_management(output_path, nn_id_field, "LONG")
            arcpy.AddField_management(output_path, nn_dist_field, "DOUBLE")

            # Build centroid dictionary
            coords = {row[0]: row[1].centroid for row in arcpy.da.SearchCursor(output_path, [id_field, "SHAPE@"])}

            def haversine(p1, p2):
                lon1, lat1 = p1.X, p1.Y
                lon2, lat2 = p2.X, p2.Y
                lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
                dlat = lat2 - lat1
                dlon = lon2 - lon1
                a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
                c = 2 * math.asin(math.sqrt(a))
                r = 6371000
                return c * r

            # Calculate nearest neighbor for each feature
            nn_results = {}
            for oid, pt in coords.items():
                min_dist = None
                min_oid = None
                for oid2, pt2 in coords.items():
                    if oid == oid2:
                        continue
                    dist = haversine(pt, pt2)
                    if min_dist is None or dist < min_dist:
                        min_dist = dist
                        min_oid = oid2
                if min_dist is not None:
                    nn_results[oid] = (min_oid, min_dist)

            # Write results to new fields
            with arcpy.da.UpdateCursor(output_path, [id_field, nn_id_field, nn_dist_field]) as cursor:
                for row in cursor:
                    oid = row[0]
                    if oid in nn_results:
                        row[1] = nn_results[oid][0]
                        row[2] = nn_results[oid][1]
                        cursor.updateRow(row)

            # Get statistics on the nearest distance field
            # Try to get the layer name from the output path for statistics
            output_layer_name = os.path.basename(output_path)
            stats = self.get_field_statistics(output_layer_name, nn_dist_field)

            result = {
                "function_executed": "create_nearest_neighbor_layer",
                "layer_name": layer_name,
                "output_layer": output_name,
                "output_path": output_path,
                "nearest_id_field": nn_id_field,
                "nearest_distance_field": nn_dist_field,
                "success": True,
                "statistics": stats.get("statistics", {}),
                "feature_count": len(nn_results)
            }
            logger.info(f"Nearest neighbor layer created: {result}")
            return result
        except Exception as e:
            logger.error(f"create_nearest_neighbor_layer error: {str(e)}")
            return {"success": False, "error": str(e)}
        
    def get_unique_values_count(self, layer_name: str, field_name: str) -> Dict:
        """
        Get the count of unique values in a field for a given layer.
        """
        logger.info(f"Getting unique values count for {field_name} in {layer_name}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            values = set()
            for row in arcpy.da.SearchCursor(lyr, [field_name]):
                values.add(row[0])
            result = {
                "function_executed": "get_unique_values_count",
                "layer_name": layer_name,
                "field_name": field_name,
                "success": True,
                "unique_count": len(values)
            }
            logger.info(f"Unique values count: {result}")
            return result
        except Exception as e:
            logger.error(f"get_unique_values_count error: {str(e)}")
            return {"success": False, "error": str(e)}

    def calculate_empty_values(self, layer_name: str, field_name: str) -> Dict:
        """
        Calculate the number of empty (null or blank) values in a field for a given layer.
        """
        logger.info(f"Calculating empty values for {field_name} in {layer_name}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            empty_count = 0
            total = 0
            for row in arcpy.da.SearchCursor(lyr, [field_name]):
                total += 1
                val = row[0]
                if val is None or (isinstance(val, str) and val.strip() == ""):
                    empty_count += 1
            result = {
                "function_executed": "calculate_empty_values",
                "layer_name": layer_name,
                "field_name": field_name,
                "success": True,
                "empty_count": empty_count,
                "total_count": total
            }
            logger.info(f"Empty values calculation: {result}")
            return result
        except Exception as e:
            logger.error(f"calculate_empty_values error: {str(e)}")
            return {"success": False, "error": str(e)}
        
    def get_map_layers_info(self) -> Dict:
        """
        Get information about all layers in the current ArcGIS Pro map.
        Returns a list of dictionaries with layer name, type, visibility, and data source.
        """
        logger.info("Getting map layers info")
        try:
            if not ARCPY_AVAILABLE or not hasattr(arcpy, 'mp'):
                return {"success": False, "error": "ArcGIS Pro environment not detected or arcpy.mp is not available. Please ensure ArcGIS Pro is running and the script is executed within its Python environment."}
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            layers_info = []
            for lyr in map_obj.listLayers():
                try:
                    desc = arcpy.Describe(lyr)
                    layer_info = {
                        "name": lyr.name,
                        "visible": lyr.visible,
                        "type": desc.shapeType if hasattr(desc, "shapeType") else "Unknown",
                        "data_source": desc.dataSource if hasattr(desc, "dataSource") else ""
                    }
                except Exception as e:
                    layer_info = {
                        "name": lyr.name,
                        "visible": lyr.visible,
                        "type": "Unknown",
                        "data_source": "",
                        "error": str(e)
                    }
                layers_info.append(layer_info)
            result = {
                "function_executed": "get_map_layers_info",
                "success": True,
                "layers": layers_info
            }
            logger.info(f"Map layers info: {result}")
            return result
        except Exception as e:
            logger.error(f"get_map_layers_info error: {str(e)}")
            return {"success": False, "error": str(e)}

    def get_map_tables_info(self) -> Dict:
        """
        Get information about all standalone tables in the current ArcGIS Pro map.
        Returns a list of dictionaries with table name and data source.
        """
        logger.info("Getting map tables info")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            tables_info = []
            for tbl in map_obj.listTables():
                try:
                    desc = arcpy.Describe(tbl)
                    table_info = {
                        "name": tbl.name,
                        "data_source": desc.dataSource if hasattr(desc, "dataSource") else ""
                    }
                except Exception as e:
                    table_info = {
                        "name": tbl.name,
                        "data_source": "",
                        "error": str(e)
                    }
                tables_info.append(table_info)
            result = {
                "function_executed": "get_map_tables_info",
                "success": True,
                "tables": tables_info
            }
            logger.info(f"Map tables info: {result}")
            return result
        except Exception as e:
            logger.error(f"get_map_tables_info error: {str(e)}")
            return {"success": False, "error": str(e)}
            
    def get_values_frequency(self, layer_name: str, field_name: str) -> Dict:
        """
        Gets frequency distribution of field values.
        Returns value-count pairs sorted by frequency.
        """
        logger.info(f"Getting values frequency for field {field_name} in layer {layer_name}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            
            frequency_dict = {}
            total_count = 0
            
            for row in arcpy.da.SearchCursor(lyr, [field_name]):
                value = row[0]
                total_count += 1
                if value in frequency_dict:
                    frequency_dict[value] += 1
                else:
                    frequency_dict[value] = 1
            
            # Sort by frequency (descending)
            sorted_frequencies = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
            
            result = {
                "function_executed": "get_values_frequency",
                "layer_name": layer_name,
                "field_name": field_name,
                "success": True,
                "total_features": total_count,
                "unique_values": len(frequency_dict),
                "frequency_distribution": sorted_frequencies
            }
            
            logger.info(f"Values frequency: {result}")
            return result
        except Exception as e:
            logger.error(f"get_values_frequency error: {str(e)}")
            return {"success": False, "error": str(e)}

    def get_value_frequency(self, layer_name: str, field_name: str, lookup_value: str) -> Dict:
        """
        Gets frequency distribution of a specific field value.
        Returns count for the specific lookup value.
        """
        logger.info(f"Getting frequency for value '{lookup_value}' in field {field_name} of layer {layer_name}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            
            value_count = 0
            total_count = 0
            
            for row in arcpy.da.SearchCursor(lyr, [field_name]):
                value = row[0]
                total_count += 1
                if str(value) == str(lookup_value):
                    value_count += 1
            
            result = {
                "function_executed": "get_value_frequency",
                "layer_name": layer_name,
                "field_name": field_name,
                "lookup_value": lookup_value,
                "success": True,
                "value_count": value_count,
                "total_count": total_count,
                "percentage": (value_count / total_count * 100) if total_count > 0 else 0
            }
            
            logger.info(f"Value frequency: {result}")
            return result
        except Exception as e:
            logger.error(f"get_value_frequency error: {str(e)}")
            return {"success": False, "error": str(e)}

    def get_coordinate_system(self, layer_name: str) -> Dict:
        """
        Gets coordinate system information for a layer.
        Returns CRS name, code, and units.
        """
        logger.info(f"Getting coordinate system info for layer {layer_name}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            
            desc = arcpy.Describe(lyr)
            spatial_ref = desc.spatialReference
            
            result = {
                "function_executed": "get_coordinate_system",
                "layer_name": layer_name,
                "success": True,
                "crs_name": spatial_ref.name,
                "crs_code": spatial_ref.factoryCode,
                "crs_type": spatial_ref.type,
                "linear_unit": spatial_ref.linearUnitName,
                "angular_unit": spatial_ref.angularUnitName if hasattr(spatial_ref, 'angularUnitName') else None,
                "datum": spatial_ref.datumName if hasattr(spatial_ref, 'datumName') else None
            }
            
            logger.info(f"Coordinate system info: {result}")
            return result
        except Exception as e:
            logger.error(f"get_coordinate_system error: {str(e)}")
            return {"success": False, "error": str(e)}

    def get_attribute_table(self, layer_name: str, start_row: int = 0, row_count: int = 100) -> Dict:
        """
        Gets attribute table data with pagination.
        Returns tabular data array with specified rows.
        """
        logger.info(f"Getting attribute table for layer {layer_name}, rows {start_row}-{start_row + row_count}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            
            # Get field names
            field_names = [field.name for field in arcpy.ListFields(lyr)]
            
            # Get data with pagination
            table_data = []
            current_row = 0
            
            for row in arcpy.da.SearchCursor(lyr, field_names):
                if current_row >= start_row and current_row < start_row + row_count:
                    row_dict = {}
                    for i, field_name in enumerate(field_names):
                        row_dict[field_name] = row[i]
                    table_data.append(row_dict)
                current_row += 1
                if current_row >= start_row + row_count:
                    break
            
            result = {
                "function_executed": "get_attribute_table",
                "layer_name": layer_name,
                "success": True,
                "start_row": start_row,
                "row_count": len(table_data),
                "total_features": current_row,
                "field_names": field_names,
                "data": table_data
            }
            
            logger.info(f"Attribute table retrieved: {len(table_data)} rows")
            return result
        except Exception as e:
            logger.error(f"get_attribute_table error: {str(e)}")
            return {"success": False, "error": str(e)}

    def get_field_domain_values(self, layer_name: str, field_name: str) -> Dict:
        """
        Gets domain values for coded value fields.
        Returns code-description pairs.
        """
        logger.info(f"Getting domain values for field {field_name} in layer {layer_name}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            
            # Get field info
            field_obj = None
            for field in arcpy.ListFields(lyr):
                if field.name == field_name:
                    field_obj = field
                    break
            
            if not field_obj:
                return {"success": False, "error": f"Field {field_name} not found"}
            
            domain_values = []
            if field_obj.domain:
                desc = arcpy.Describe(lyr)
                workspace = desc.path
                domains = arcpy.da.ListDomains(workspace)
                
                for domain in domains:
                    if domain.name == field_obj.domain:
                        if domain.domainType == 'CodedValue':
                            for coded_value in domain.codedValues:
                                domain_values.append({
                                    "code": coded_value,
                                    "description": domain.codedValues[coded_value]
                                })
                        break
            
            result = {
                "function_executed": "get_field_domain_values",
                "layer_name": layer_name,
                "field_name": field_name,
                "success": True,
                "has_domain": bool(field_obj.domain),
                "domain_name": field_obj.domain if field_obj.domain else None,
                "domain_values": domain_values
            }
            
            logger.info(f"Field domain values: {result}")
            return result
        except Exception as e:
            logger.error(f"get_field_domain_values error: {str(e)}")
            return {"success": False, "error": str(e)}

    def calculate_new_field(self, layer_name: str, new_field_name: str, field_value: str, field_type: str = "TEXT") -> Dict:
        """
        Adds a new field to a layer and calculates its values using a Python expression.
        Returns new field name and processed feature count.
        """
        logger.info(f"Adding and calculating new field {new_field_name} in layer {layer_name}")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            
            # Check if field already exists
            existing_fields = [field.name for field in arcpy.ListFields(lyr)]
            if new_field_name in existing_fields:
                return {"success": False, "error": f"Field {new_field_name} already exists"}
            
            # Add new field with specified type
            if field_type.upper() == "TEXT":
                arcpy.AddField_management(lyr, new_field_name, "TEXT", field_length=255)
            else:
                arcpy.AddField_management(lyr, new_field_name, field_type.upper())
            
            # Create the full Python equation
            python_equation = f'"{field_value}"' if field_type.upper() == "TEXT" else field_value
            
            # Calculate field values
            arcpy.CalculateField_management(lyr, new_field_name, python_equation, "PYTHON3")
            
            # Count processed features
            feature_count = int(arcpy.GetCount_management(lyr)[0])
            
            result = {
                "function_executed": "calculate_new_field",
                "layer_name": layer_name,
                "new_field_name": new_field_name,
                "field_type": field_type,
                "field_value": field_value,
                "python_equation": python_equation,
                "success": True,
                "processed_features": feature_count,
                "field_added": True
            }
            
            logger.info(f"New field calculated: {result}")
            return result
        except Exception as e:
            logger.error(f"calculate_new_field error: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def analyze_layer_fields(self, layer_name: str) -> Dict:
        """
        Analyze all fields in a layer to understand their characteristics for dashboard generation.
        Skips system fields and numeric fields where most values are unique (likely IDs).
        Returns detailed field metadata including data types, unique values, null percentages, etc.
        """
        logger.info(f"Starting field analysis for layer: {layer_name}")

        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap

            # Find the target layer
            target_layer = next((lyr for lyr in map_obj.listLayers() if lyr.name == layer_name), None)
            if not target_layer:
                return {"success": False, "error": f"Layer '{layer_name}' not found"}
            if not target_layer.isFeatureLayer:
                return {"success": False, "error": f"Layer '{layer_name}' is not a feature layer"}

            # Get total feature count
            total_count = int(arcpy.GetCount_management(target_layer)[0])
            if total_count == 0:
                return {"success": False, "error": f"Layer '{layer_name}' has no features"}

            fields = arcpy.ListFields(target_layer)
            field_analysis = {}

            # Cursor for checking uniqueness without loading all values into memory at once
            with arcpy.da.SearchCursor(target_layer, [f.name for f in fields]) as cursor:
                rows = list(cursor)  # safe since we have total_count from above

            # Build a name->index map once
            field_index = {fld.name: idx for idx, fld in enumerate(fields)}

            for field in fields:
                # Skip system OBJECTID/geometry fields and common system fields
                if field.type in ['Geometry'] or field.name.upper() in ['OBJECTID', 'SHAPE_LENGTH', 'SHAPE_AREA', 'GLOBALID']:
                    continue

                # Values for this field
                col_idx = field_index[field.name]
                all_values = [r[col_idx] for r in rows]  # Include nulls for proper ratio calculation
                values = [v for v in all_values if v is not None]  # Non-null values for analysis

                # Smart skip for numeric unique-ID-like fields
                if field.type in ['SmallInteger', 'Integer', 'Single', 'Double'] and values:
                    # Name-assisted early skip (soft signal)
                    name_l = field.name.lower()
                    name_hint = any(substr in name_l for substr in ["id", "code", "guid"])
                    n = len(values)
                    uniq = len(set(values)) / n if n else 0
                    # Integer-like ratio
                    def _int_like(x: float, eps: float = 1e-9) -> bool:
                        try:
                            return abs(x - round(x)) <= eps
                        except Exception:
                            return False
                    int_like_ratio = sum(1 for v in values if _int_like(v)) / n
                    if name_hint and uniq >= 0.85 and int_like_ratio >= 0.85:
                        logger.debug(f"Skipping {field.name} as ID-like numeric field (name hint)")
                        continue
                    # Heuristic skip for numeric ID-like fields
                    if self._is_id_like_numeric(values):
                        logger.debug(f"Skipping {field.name} as ID-like numeric field")
                        continue

                # Smart skip for text fields that look like IDs (e.g., GUIDs, codes, numeric-as-text)
                if field.type in ['String', 'Text'] and values:
                    text_values = [str(v).strip() for v in values]
                    if self._is_id_like_text(text_values):
                        logger.debug(f"Skipping {field.name} as ID-like text field")
                        continue

                field_info = {
                    "field_name": field.name,
                    "field_type": field.type,
                    "field_length": getattr(field, 'length', None),
                    "field_precision": getattr(field, 'precision', None),
                    "field_scale": getattr(field, 'scale', None),
                    "total_records": total_count
                }

                # Calculate field statistics based on type
                if field.type in ['SmallInteger', 'Integer', 'Single', 'Double']:
                    field_info.update(self._analyze_numeric_field(target_layer, field.name, total_count))
                elif field.type in ['String', 'Text']:
                    field_info.update(self._analyze_text_field(target_layer, field.name, total_count))
                elif field.type == 'Date':
                    field_info.update(self._analyze_date_field(target_layer, field.name, total_count))
                else:
                    field_info.update(self._analyze_generic_field(target_layer, field.name, total_count))

                # AI-ready insights
                field_info.update(self._generate_ai_insights(field_info, field.name))

                field_analysis[field.name] = field_info

            result = {
                "success": True,
                "layer_name": layer_name,
                "total_features": total_count,
                "fields_analyzed": len(field_analysis),
                "field_insights": field_analysis,
                "analysis_timestamp": self._get_timestamp()
            }

            logger.info(f"Field analysis completed for {layer_name}: {len(field_analysis)} fields analyzed")
            return result

        except Exception as e:
            logger.error(f"analyze_layer_fields error: {str(e)}")
            return {"success": False, "error": str(e)}

    
    def _analyze_numeric_field(self, layer, field_name: str, total_count: int) -> Dict:
        """Analyze numeric field characteristics"""
        try:
            # Get all values using SearchCursor
            values = []
            null_count = 0
            
            with arcpy.da.SearchCursor(layer, [field_name]) as cursor:
                for row in cursor:
                    value = row[0]
                    if value is None:
                        null_count += 1
                    else:
                        values.append(value)
            
            if not values:
                return {
                    "data_category": "numeric",
                    "unique_count": 0,
                    "null_count": null_count,
                    "null_percentage": 100.0,
                    "sample_values": []
                }
            
            # Calculate statistics
            unique_values = list(set(values))
            min_val = min(values)
            max_val = max(values)
            avg_val = sum(values) / len(values)
            
            # Step 2 Enhancement: Add advanced statistical measures for AI insights
            median_val = self._calculate_median(values)
            std_dev = self._calculate_std_dev(values, avg_val) if len(values) > 1 else 0
            value_range = max_val - min_val
            
            # Detect outliers using IQR method
            outlier_info = self._detect_outliers(values) if len(values) >= 4 else {"outlier_count": 0, "outlier_percentage": 0}
            
            # Calculate skewness indicator (simplified)
            skew_indicator = "symmetric"
            if len(values) > 2:
                if avg_val > median_val + (std_dev * 0.5):
                    skew_indicator = "right_skewed"
                elif avg_val < median_val - (std_dev * 0.5):
                    skew_indicator = "left_skewed"
            
            # Determine if it's categorical (low unique count) or continuous
            unique_count = len(unique_values)
            is_categorical = unique_count <= 20 and unique_count < total_count * 0.1
            
            analysis = {
                "data_category": "categorical_numeric" if is_categorical else "continuous_numeric",
                "unique_count": unique_count,
                "null_count": null_count,
                "null_percentage": round((null_count / total_count) * 100, 2),
                "min_value": min_val,
                "max_value": max_val,
                "average_value": round(avg_val, 3),
                "median_value": round(median_val, 3),
                "standard_deviation": round(std_dev, 3),
                "value_range": round(value_range, 3),
                "coefficient_of_variation": round((std_dev / avg_val * 100), 2) if avg_val != 0 else 0,
                "distribution_shape": skew_indicator,
                "outlier_count": outlier_info["outlier_count"],
                "outlier_percentage": round(outlier_info["outlier_percentage"], 2),
                "sample_values": unique_values[:10] if is_categorical else [min_val, max_val, round(avg_val, 3)]
            }
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error analyzing numeric field {field_name}: {str(e)}")
            return {"data_category": "numeric", "error": str(e)}
    
    def _analyze_text_field(self, layer, field_name: str, total_count: int) -> Dict:
        """Analyze text field characteristics"""
        try:
            # Get all values using SearchCursor
            values = []
            null_count = 0
            
            with arcpy.da.SearchCursor(layer, [field_name]) as cursor:
                for row in cursor:
                    value = row[0]
                    # Treat None, empty string, and whitespace-only as null
                    if value is None or str(value).strip() == '':
                        null_count += 1
                    else:
                        values.append(str(value).strip())
            
            if not values:
                return {
                    "data_category": "text",
                    "unique_count": 0,
                    "null_count": null_count,
                    "null_percentage": 100.0,
                    "sample_values": []
                }
            
            # Calculate statistics
            unique_values = list(set(values))
            unique_count = len(unique_values)
            
            # Step 2 Enhancement: Add detailed text analysis for AI insights
            text_lengths = [len(v) for v in values]
            avg_length = sum(text_lengths) / len(text_lengths) if text_lengths else 0
            min_length = min(text_lengths) if text_lengths else 0
            max_length = max(text_lengths) if text_lengths else 0
            
            # Analyze text patterns
            text_patterns = self._analyze_text_patterns(values, unique_values)
            
            # Determine if it's categorical or free text
            is_categorical = unique_count <= 50 and unique_count < total_count * 0.3
            
            # Enhanced categorization based on text characteristics
            if is_categorical and avg_length <= 20 and text_patterns["has_consistent_format"]:
                data_category = "categorical_text"
            elif is_categorical and text_patterns["likely_codes"]:
                data_category = "categorical_codes"
            elif avg_length > 100 or text_patterns["has_varied_length"]:
                data_category = "free_text"
            elif text_patterns["likely_names"]:
                data_category = "name_field"
            else:
                data_category = "categorical_text" if is_categorical else "free_text"
            
            analysis = {
                "data_category": data_category,
                "unique_count": unique_count,
                "null_count": null_count,
                "null_percentage": round((null_count / total_count) * 100, 2),
                "sample_values": unique_values[:10],
                "avg_length": round(avg_length, 1),
                "min_length": min_length,
                "max_length": max_length,
                "length_variability": round((max_length - min_length) / avg_length * 100, 1) if avg_length > 0 else 0,
                "text_patterns": text_patterns
            }
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error analyzing text field {field_name}: {str(e)}")
            return {"data_category": "text", "error": str(e)}
    
    def _analyze_date_field(self, layer, field_name: str, total_count: int) -> Dict:
        """Analyze date field characteristics"""
        try:
            # Get all values using SearchCursor
            values = []
            null_count = 0
            
            with arcpy.da.SearchCursor(layer, [field_name]) as cursor:
                for row in cursor:
                    value = row[0]
                    if value is None:
                        null_count += 1
                    else:
                        values.append(value)
            
            if not values:
                return {
                    "data_category": "date",
                    "unique_count": 0,
                    "null_count": null_count,
                    "null_percentage": 100.0,
                    "sample_values": []
                }
            
            # Calculate statistics
            unique_count = len(set(values))
            min_date = min(values)
            max_date = max(values)
            
            analysis = {
                "data_category": "date",
                "unique_count": unique_count,
                "null_count": null_count,
                "null_percentage": round((null_count / total_count) * 100, 2),
                "min_date": str(min_date),
                "max_date": str(max_date),
                "sample_values": [str(v) for v in sorted(set(values))[:5]]
            }
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error analyzing date field {field_name}: {str(e)}")
            return {"data_category": "date", "error": str(e)}
    
    def _analyze_generic_field(self, layer, field_name: str, total_count: int) -> Dict:
        """Generic analysis for other field types"""
        try:
            # Get basic statistics
            null_count = 0
            value_count = 0
            
            with arcpy.da.SearchCursor(layer, [field_name]) as cursor:
                for row in cursor:
                    if row[0] is None:
                        null_count += 1
                    else:
                        value_count += 1
            
            analysis = {
                "data_category": "other",
                "null_count": null_count,
                "value_count": value_count,
                "null_percentage": round((null_count / total_count) * 100, 2)
            }
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error analyzing generic field {field_name}: {str(e)}")
            return {"data_category": "other", "error": str(e)}

    def _is_id_like_numeric(self, values: List[float]) -> bool:
        """
        Heuristically determine if a numeric vector looks like an identifier:
        - High uniqueness (>= 0.9 of non-null values are unique)
        - Mostly integer-like values
        - Dense coverage across min..max (unique_count / value_range >= 0.5 for meaningful ranges)
        - Common step pattern ~1 when sorted (median diff == 1 or close)
        """
        try:
            if not values:
                return False
            n = len(values)
            unique_vals = sorted(set(values))
            unique_count = len(unique_vals)
            # Uniqueness ratio
            uniq_ratio = unique_count / n if n > 0 else 0
            if uniq_ratio < 0.9 or n < 10:
                return False
            # Integer-likeness: allow small float noise (e.g., cast to int within epsilon)
            def is_int_like(x: float, eps: float = 1e-9) -> bool:
                try:
                    return abs(x - round(x)) <= eps
                except Exception:
                    return False
            int_like_ratio = sum(1 for v in values if is_int_like(v)) / n
            if int_like_ratio < 0.9:
                # If many are true floats, likely measurement data, not ID
                return False
            vmin, vmax = unique_vals[0], unique_vals[-1]
            value_range = vmax - vmin
            if value_range <= 0:
                return False
            density = unique_count / (value_range + 1)  # +1 to handle inclusive integer range
            # Compute median step
            diffs = [unique_vals[i+1] - unique_vals[i] for i in range(len(unique_vals)-1)]
            diffs_sorted = sorted(diffs)
            mid = len(diffs_sorted)//2
            median_step = (diffs_sorted[mid] if len(diffs_sorted)%2==1 else (diffs_sorted[mid-1]+diffs_sorted[mid])/2)
            # ID-like if dense and step ~1
            if density >= 0.5 and 0.9 <= median_step <= 1.1:
                return True
            # Also treat strictly consecutive sequences as ID-like
            if all(abs(d - 1) <= 1e-9 for d in diffs):
                return True
            return False
        except Exception:
            return False

    def _is_id_like_text(self, values: List[str]) -> bool:
        """
        Heuristically determine if a text vector looks like an identifier/code:
        - High uniqueness
        - Mostly constrained character set (alnum, -, _)
        - Consistent length or matches GUID/UUID patterns
        - Numeric-as-text (e.g., "000123", "101", "987654")
        """
        try:
            if not values:
                return False
            n = len(values)
            unique_vals = list({v for v in values if v != ''})
            unique_count = len(unique_vals)
            if n < 10:
                return False
            uniq_ratio = unique_count / n if n > 0 else 0
            if uniq_ratio < 0.85:
                return False

            # Quick GUID/UUID detection
            uuid_regex = re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$")
            hex32_regex = re.compile(r"^[0-9a-fA-F]{32}$")
            def is_uuid_like(s: str) -> bool:
                s = s.strip()
                return bool(uuid_regex.match(s) or hex32_regex.match(s))
            uuid_ratio = sum(1 for v in values if is_uuid_like(v)) / n
            if uuid_ratio >= 0.8:
                return True

            # Numeric-as-text detection
            digits_regex = re.compile(r"^\d+$")
            digits_ratio = sum(1 for v in values if digits_regex.match(v)) / n
            if digits_ratio >= 0.8 and uniq_ratio >= 0.9:
                # Try numeric ID-like heuristic on parsed ints
                ints = [int(v) for v in values if digits_regex.match(v)]
                if self._is_id_like_numeric(ints):
                    return True
                # Even if not dense, very high uniqueness numeric codes are often IDs
                if uniq_ratio >= 0.98:
                    return True

            # Alphanumeric codes: mostly alnum/_/- and consistent length
            code_regex = re.compile(r"^[A-Za-z0-9_-]+$")
            code_ratio = sum(1 for v in values if code_regex.match(v)) / n
            if code_ratio >= 0.9:
                lengths = [len(v) for v in values if v]
                if lengths:
                    avg_len = sum(lengths) / len(lengths)
                    var = sum((l - avg_len)**2 for l in lengths) / len(lengths)
                    # Low variance in lengths suggests formatted codes
                    if var <= 1.0 and uniq_ratio >= 0.9:
                        return True
                    # If many look like hex-ish strings with high uniqueness
                    hexish_ratio = sum(1 for v in values if re.fullmatch(r"[0-9A-Fa-f]+", v) is not None) / n
                    if hexish_ratio >= 0.9 and uniq_ratio >= 0.9:
                        return True

            return False
        except Exception:
            return False
    
    def _generate_ai_insights(self, field_info: Dict, field_name: str) -> Dict:
        """
        Step 2 Enhancement: Generate AI-ready insights for better chart selection
        Provides rich, descriptive analysis that enables intelligent chart recommendations
        """
        try:
            data_category = field_info.get("data_category", "unknown")
            unique_count = field_info.get("unique_count", 0)
            total_records = field_info.get("total_records", 1)
            null_percentage = field_info.get("null_percentage", 0)
            
            ai_insights = {
                "data_story": "",
                "visualization_potential": "low",
                "chart_suitability": {},
                "data_patterns": {},
                "analytical_value": "medium",
                "distribution_characteristics": "",
                "visualization_priority": 5  # 1-10 scale
            }
            
            # Generate data story based on field characteristics
            if data_category == "categorical_text":
                diversity_ratio = unique_count / total_records if total_records > 0 else 0
                
                if unique_count <= 5:
                    ai_insights["data_story"] = f"'{field_name}' contains {unique_count} distinct categories with clear groupings, ideal for showing proportional relationships."
                    ai_insights["visualization_potential"] = "high"
                    ai_insights["visualization_priority"] = 9
                    ai_insights["chart_suitability"] = {
                        "pie": 0.95, "donut": 0.90, "bar": 0.85, "column": 0.80
                    }
                elif unique_count <= 15:
                    ai_insights["data_story"] = f"'{field_name}' has {unique_count} categories, suitable for comparative analysis and ranking visualizations."
                    ai_insights["visualization_potential"] = "high"
                    ai_insights["visualization_priority"] = 8
                    ai_insights["chart_suitability"] = {
                        "bar": 0.90, "column": 0.85, "horizontal_bar": 0.80, "pie": 0.70
                    }
                elif unique_count <= 30:
                    ai_insights["data_story"] = f"'{field_name}' contains {unique_count} categories, best visualized with scrollable or grouped displays."
                    ai_insights["visualization_potential"] = "medium"
                    ai_insights["visualization_priority"] = 6
                    ai_insights["chart_suitability"] = {
                        "bar": 0.75, "treemap": 0.70, "grouped_bar": 0.65
                    }
                else:
                    ai_insights["data_story"] = f"'{field_name}' has high cardinality ({unique_count} categories), requiring aggregation or filtering for effective visualization."
                    ai_insights["visualization_potential"] = "low"
                    ai_insights["visualization_priority"] = 3
                    ai_insights["chart_suitability"] = {
                        "word_cloud": 0.60, "top_n_bar": 0.55
                    }
                    
            elif data_category == "continuous_numeric":
                value_range = field_info.get("max_value", 0) - field_info.get("min_value", 0)
                avg_value = field_info.get("average_value", 0)
                min_val = field_info.get("min_value", 0)
                max_val = field_info.get("max_value", 0)
                
                # Analyze distribution characteristics
                if value_range > 0:
                    cv = (value_range / 4) / avg_value if avg_value != 0 else 0  # Approximate coefficient of variation
                    
                    if cv < 0.3:
                        ai_insights["distribution_characteristics"] = "Low variability - values clustered around the mean"
                        ai_insights["data_story"] = f"'{field_name}' shows consistent values (range: {min_val:.2f} to {max_val:.2f}), good for trend analysis."
                    elif cv < 1.0:
                        ai_insights["distribution_characteristics"] = "Moderate variability - normal distribution likely"
                        ai_insights["data_story"] = f"'{field_name}' displays moderate variation (range: {min_val:.2f} to {max_val:.2f}), suitable for distribution analysis."
                    else:
                        ai_insights["distribution_characteristics"] = "High variability - potential outliers present"
                        ai_insights["data_story"] = f"'{field_name}' shows high variation (range: {min_val:.2f} to {max_val:.2f}), may contain outliers worth investigating."
                else:
                    ai_insights["data_story"] = f"'{field_name}' contains constant or near-constant values, limited visualization value."
                
                ai_insights["visualization_potential"] = "high" if value_range > 0 else "low"
                ai_insights["visualization_priority"] = 8 if value_range > 0 else 2
                ai_insights["chart_suitability"] = {
                    "histogram": 0.90, "box_plot": 0.85, "density_plot": 0.80, "violin_plot": 0.75
                } if value_range > 0 else {"summary_stats": 0.30}
                
            elif data_category == "categorical_numeric":
                ai_insights["data_story"] = f"'{field_name}' represents discrete numeric categories ({unique_count} values), ideal for count-based visualizations."
                ai_insights["visualization_potential"] = "high"
                ai_insights["visualization_priority"] = 7
                ai_insights["chart_suitability"] = {
                    "bar": 0.85, "column": 0.80, "pie": 0.75 if unique_count <= 8 else 0.50
                }
                
            elif data_category == "free_text":
                ai_insights["data_story"] = f"'{field_name}' contains free-form text with {unique_count} unique entries, suitable for text analysis."
                ai_insights["visualization_potential"] = "low"
                ai_insights["visualization_priority"] = 2
                ai_insights["chart_suitability"] = {
                    "word_cloud": 0.60, "text_length_histogram": 0.40
                }
                
            elif data_category == "date":
                ai_insights["data_story"] = f"'{field_name}' contains temporal data spanning from {field_info.get('min_date', 'unknown')} to {field_info.get('max_date', 'unknown')}."
                ai_insights["visualization_potential"] = "high"
                ai_insights["visualization_priority"] = 8
                ai_insights["chart_suitability"] = {
                    "timeline": 0.90, "line_chart": 0.85, "date_histogram": 0.80
                }
            
            # Add data quality insights
            if null_percentage > 50:
                ai_insights["data_story"] += f" Data quality concern: {null_percentage:.1f}% missing values."
                ai_insights["visualization_priority"] = max(1, ai_insights["visualization_priority"] - 3)
            elif null_percentage > 20:
                ai_insights["data_story"] += f" Note: {null_percentage:.1f}% missing values present."
                ai_insights["visualization_priority"] = max(1, ai_insights["visualization_priority"] - 1)
            
            # Determine analytical value
            if ai_insights["visualization_priority"] >= 8:
                ai_insights["analytical_value"] = "high"
            elif ai_insights["visualization_priority"] >= 5:
                ai_insights["analytical_value"] = "medium"
            else:
                ai_insights["analytical_value"] = "low"
            
            # Add pattern detection for numeric fields
            if data_category in ["continuous_numeric", "categorical_numeric"]:
                ai_insights["data_patterns"] = self._detect_numeric_patterns(field_info)
            
            return {"ai_insights": ai_insights}
            
        except Exception as e:
            logger.error(f"Error generating AI insights for {field_name}: {str(e)}")
            return {"ai_insights": {"error": str(e), "data_story": "Analysis unavailable"}}
    
    def _detect_numeric_patterns(self, field_info: Dict) -> Dict:
        """Detect patterns in numeric data for enhanced AI insights"""
        try:
            patterns = {}
            min_val = field_info.get("min_value", 0)
            max_val = field_info.get("max_value", 0)
            avg_val = field_info.get("average_value", 0)
            unique_count = field_info.get("unique_count", 0)
            total_records = field_info.get("total_records", 1)
            
            # Range analysis
            if min_val >= 0:
                patterns["value_type"] = "positive_values"
                if min_val == 0:
                    patterns["includes_zero"] = True
            elif max_val <= 0:
                patterns["value_type"] = "negative_values"
            else:
                patterns["value_type"] = "mixed_values"
            
            # Detect potential count/measurement data
            if min_val >= 0 and all(isinstance(sample, int) for sample in field_info.get("sample_values", [])[:3]):
                patterns["potential_type"] = "count_data"
            else:
                patterns["potential_type"] = "measurement_data"
            
            return patterns
            
        except Exception as e:
            logger.error(f"Error detecting numeric patterns: {str(e)}")
            return {"error": str(e)}
    
    def _calculate_median(self, values: List[float]) -> float:
        """Calculate median of a list of numbers"""
        sorted_values = sorted(values)
        n = len(sorted_values)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_values[mid - 1] + sorted_values[mid]) / 2
        else:
            return sorted_values[mid]
    
    def _calculate_std_dev(self, values: List[float], mean: float) -> float:
        """Calculate standard deviation"""
        return math.sqrt(sum((x - mean) ** 2 for x in values) / (len(values) - 1))
    
    def _detect_outliers(self, values: List[float]) -> Dict:
        """Detect outliers using the IQR method"""
        sorted_values = sorted(values)
        q1 = self._calculate_quartile(sorted_values, 1)
        q3 = self._calculate_quartile(sorted_values, 3)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        outliers = [v for v in values if v < lower_bound or v > upper_bound]
        return {
            "outlier_count": len(outliers),
            "outlier_percentage": (len(outliers) / len(values)) * 100 if values else 0
        }
    
    def _calculate_quartile(self, sorted_values: List[float], quartile: int) -> float:
        """Calculate the specified quartile (1 or 3)"""
        n = len(sorted_values)
        index = (n + 1) * (quartile / 4)
        if index.is_integer():
            return sorted_values[int(index) - 1]
        else:
            lower = sorted_values[int(index) - 1]
            upper = sorted_values[int(index)]
            return lower + (upper - lower) * (index - int(index))
    
    def _analyze_text_patterns(self, values: List[str], unique_values: List[str]) -> Dict:
        """Analyze text patterns for AI insights"""
        patterns = {"has_consistent_format": False, "likely_codes": False, "has_varied_length": False, "likely_names": False}
        
        # Check for consistent formatting (e.g., all uppercase, all lowercase)
        if all(v.isupper() for v in unique_values) or all(v.islower() for v in unique_values):
            patterns["has_consistent_format"] = True
        
        # Check for code-like patterns (alphanumeric, short, consistent length)
        lengths = [len(v) for v in unique_values]
        if lengths and max(lengths) < 15 and (max(lengths) - min(lengths)) < 5:
            if all(v.isalnum() for v in unique_values):
                patterns["likely_codes"] = True
        
        # Check for varied length
        if lengths and (max(lengths) - min(lengths)) > 20:
            patterns["has_varied_length"] = True
        
        # Check for name-like patterns (capitalized words)
        if all(all(word.istitle() or word.isspace() for word in v.split()) for v in unique_values):
            patterns["likely_names"] = True
            
        return patterns

    def _get_timestamp(self) -> str:
        """Get current timestamp in ISO format"""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def generate_multi_field_statistics(self, layer_name: str, fields: List[str], chart_type: str) -> Dict:
        """
        Generate statistics for multi-field charts based on chart type.
        This is the main function you need for Chart.js data preparation.
        
        Args:
            layer_name: Name of the ArcGIS layer
            fields: List of field names to analyze together
            chart_type: Type of chart (scatter, bar, pie, histogram, etc.)
            
        Returns:
            Dictionary with processed data ready for Chart.js
        """
        logger.info(f"Generating multi-field statistics for {chart_type} chart with fields: {fields}")
        
        try:
            # Get the layer
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            target_layer = next((lyr for lyr in map_obj.listLayers() if lyr.name == layer_name), None)
            
            if not target_layer or not target_layer.isFeatureLayer:
                return {"success": False, "error": f"Layer '{layer_name}' not found or not a feature layer"}
            
            # Route to appropriate statistics generator based on chart type
            if chart_type == "scatter":
                return self._generate_scatter_statistics(target_layer, fields)
            elif chart_type in ["bar", "column"]:
                return self._generate_bar_statistics(target_layer, fields)
            elif chart_type == "pie":
                return self._generate_pie_statistics(target_layer, fields)
            elif chart_type == "histogram":
                return self._generate_histogram_statistics(target_layer, fields)
            elif chart_type == "line":
                return self._generate_line_statistics(target_layer, fields)
            else:
                return {"success": False, "error": f"Unsupported chart type: {chart_type}"}
                
        except Exception as e:
            logger.error(f"Error generating multi-field statistics: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _generate_scatter_statistics(self, layer, fields: List[str]) -> Dict:
        """
        Generate data for scatter plot (requires exactly 2 numeric fields).
        Returns x,y coordinate pairs and correlation analysis.
        """
        try:
            if len(fields) != 2:
                return {"success": False, "error": "Scatter plot requires exactly 2 fields"}
            
            field_x, field_y = fields[0], fields[1]
            
            # Get data
            data_points = []
            with arcpy.da.SearchCursor(layer, [field_x, field_y]) as cursor:
                for row in cursor:
                    x_val, y_val = row[0], row[1]
                    # Skip null values
                    if x_val is not None and y_val is not None:
                        data_points.append({"x": float(x_val), "y": float(y_val)})
            
            if len(data_points) < 2:
                return {"success": False, "error": "Insufficient valid data points for scatter plot"}
            
            # Calculate correlation
            x_values = [p["x"] for p in data_points]
            y_values = [p["y"] for p in data_points]
            correlation = self._calculate_correlation(x_values, y_values)
            
            # Chart.js format
            result = {
                "success": True,
                "chart_type": "scatter",
                "data": {
                    "datasets": [{
                        "label": f"{field_x} vs {field_y}",
                        "data": data_points,
                        "backgroundColor": "rgba(54, 162, 235, 0.6)",
                        "borderColor": "rgba(54, 162, 235, 1)",
                        "pointRadius": 3
                    }]
                },
                "options": {
                    "scales": {
                        "x": {"title": {"display": True, "text": field_x}},
                        "y": {"title": {"display": True, "text": field_y}}
                    },
                    "plugins": {
                        "title": {
                            "display": True,
                            "text": f"{field_x} vs {field_y} (r={correlation:.3f})"
                        }
                    }
                },
                "statistics": {
                    "correlation": correlation,
                    "total_points": len(data_points),
                    "x_field": field_x,
                    "y_field": field_y
                }
            }
            
            return result
            
        except Exception as e:
            logger.error(f"Error generating scatter statistics: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _generate_bar_statistics(self, layer, fields: List[str]) -> Dict:
        """
        Generate data for bar chart. Supports:
        - 1 field: categorical counts
        - 2 fields: categorical field grouped by another field (categorical or numeric aggregated)
        """
        try:
            if len(fields) == 1:
                return self._generate_single_field_bar(layer, fields[0])
            elif len(fields) == 2:
                return self._generate_grouped_bar(layer, fields[0], fields[1])
            else:
                return {"success": False, "error": "Bar chart supports 1-2 fields only"}
                
        except Exception as e:
            logger.error(f"Error generating bar statistics: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _generate_single_field_bar(self, layer, field_name: str) -> Dict:
        """Generate bar chart for single categorical field (value counts)"""
        try:
            # Get value counts
            value_counts = {}
            with arcpy.da.SearchCursor(layer, [field_name]) as cursor:
                for row in cursor:
                    value = row[0]
                    if value is not None:
                        value_str = str(value)
                        value_counts[value_str] = value_counts.get(value_str, 0) + 1
            
            if not value_counts:
                return {"success": False, "error": "No valid data for bar chart"}
            
            # Sort by count (descending)
            sorted_items = sorted(value_counts.items(), key=lambda x: x[1], reverse=True)
            
            # Limit to top 20 categories for readability
            if len(sorted_items) > 20:
                sorted_items = sorted_items[:20]
            
            labels = [item[0] for item in sorted_items]
            data = [item[1] for item in sorted_items]
            
            result = {
                "success": True,
                "chart_type": "bar",
                "data": {
                    "labels": labels,
                    "datasets": [{
                        "label": f"Count of {field_name}",
                        "data": data,
                        "backgroundColor": "rgba(75, 192, 192, 0.6)",
                        "borderColor": "rgba(75, 192, 192, 1)",
                        "borderWidth": 1
                    }]
                },
                "options": {
                    "scales": {
                        "y": {"title": {"display": True, "text": "Count"}}
                    },
                    "plugins": {
                        "title": {"display": True, "text": f"Distribution of {field_name}"}
                    }
                },
                "statistics": {
                    "total_categories": len(sorted_items),
                    "total_records": sum(data),
                    "field": field_name
                }
            }
            
            return result
            
        except Exception as e:
            logger.error(f"Error generating single field bar chart: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _generate_grouped_bar(self, layer, field1: str, field2: str) -> Dict:
        """Generate grouped bar chart for 2 fields (category + value or category + category)"""
        try:
            # Determine field types from existing field insights
            field1_info = self._get_field_basic_type(layer, field1)
            field2_info = self._get_field_basic_type(layer, field2)
            
            if field1_info["is_categorical"] and field2_info["is_numeric"]:
                # Category grouped by numeric values (aggregated)
                return self._generate_category_numeric_bar(layer, field1, field2)
            elif field1_info["is_categorical"] and field2_info["is_categorical"]:
                # Category grouped by category (cross-tabulation)
                return self._generate_category_category_bar(layer, field1, field2)
            else:
                return {"success": False, "error": "Grouped bar chart requires at least one categorical field"}
                
        except Exception as e:
            logger.error(f"Error generating grouped bar chart: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _generate_category_numeric_bar(self, layer, cat_field: str, num_field: str) -> Dict:
        """Generate bar chart: categories with aggregated numeric values"""
        try:
            # Aggregate numeric values by category
            category_values = {}
            with arcpy.da.SearchCursor(layer, [cat_field, num_field]) as cursor:
                for row in cursor:
                    category, value = row[0], row[1]
                    if category is not None and value is not None:
                        cat_str = str(category)
                        if cat_str not in category_values:
                            category_values[cat_str] = []
                        category_values[cat_str].append(float(value))
            
            if not category_values:
                return {"success": False, "error": "No valid data for grouped bar chart"}
            
            # Calculate aggregated values (mean by default)
            aggregated_data = {}
            for category, values in category_values.items():
                aggregated_data[category] = {
                    "mean": sum(values) / len(values),
                    "count": len(values),
                    "sum": sum(values)
                }
            
            # Sort by mean value (descending)
            sorted_items = sorted(aggregated_data.items(), key=lambda x: x[1]["mean"], reverse=True)
            
            # Limit categories
            if len(sorted_items) > 15:
                sorted_items = sorted_items[:15]
            
            labels = [item[0] for item in sorted_items]
            mean_data = [round(item[1]["mean"], 2) for item in sorted_items]
            
            result = {
                "success": True,
                "chart_type": "bar",
                "data": {
                    "labels": labels,
                    "datasets": [{
                        "label": f"Average {num_field}",
                        "data": mean_data,
                        "backgroundColor": "rgba(153, 102, 255, 0.6)",
                        "borderColor": "rgba(153, 102, 255, 1)",
                        "borderWidth": 1
                    }]
                },
                "options": {
                    "scales": {
                        "y": {"title": {"display": True, "text": f"Average {num_field}"}}
                    },
                    "plugins": {
                        "title": {"display": True, "text": f"Average {num_field} by {cat_field}"}
                    }
                },
                "statistics": {
                    "categories": len(sorted_items),
                    "categorical_field": cat_field,
                    "numeric_field": num_field,
                    "aggregation": "mean"
                }
            }
            
            return result
            
        except Exception as e:
            logger.error(f"Error generating category-numeric bar chart: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _generate_category_category_bar(self, layer, field1: str, field2: str) -> Dict:
        """Generate stacked bar chart for two categorical fields (cross-tabulation)"""
        try:
            # Cross-tabulation
            cross_tab = {}
            with arcpy.da.SearchCursor(layer, [field1, field2]) as cursor:
                for row in cursor:
                    val1, val2 = row[0], row[1]
                    if val1 is not None and val2 is not None:
                        val1_str, val2_str = str(val1), str(val2)
                        if val1_str not in cross_tab:
                            cross_tab[val1_str] = {}
                        cross_tab[val1_str][val2_str] = cross_tab[val1_str].get(val2_str, 0) + 1
            
            if not cross_tab:
                return {"success": False, "error": "No valid data for cross-tabulation"}
            
            # Get all unique values for field2 (for consistent datasets)
            all_field2_values = set()
            for field1_values in cross_tab.values():
                all_field2_values.update(field1_values.keys())
            all_field2_values = sorted(list(all_field2_values))
            
            # Limit field1 categories
            sorted_field1 = sorted(cross_tab.keys(), key=lambda k: sum(cross_tab[k].values()), reverse=True)
            if len(sorted_field1) > 10:
                sorted_field1 = sorted_field1[:10]
            
            # Prepare datasets for stacked bar
            datasets = []
            colors = ["rgba(255, 99, 132, 0.6)", "rgba(54, 162, 235, 0.6)", "rgba(255, 205, 86, 0.6)", 
                     "rgba(75, 192, 192, 0.6)", "rgba(153, 102, 255, 0.6)", "rgba(255, 159, 64, 0.6)"]
            
            for i, field2_val in enumerate(all_field2_values[:6]):  # Limit to 6 series
                data = []
                for field1_val in sorted_field1:
                    count = cross_tab[field1_val].get(field2_val, 0)
                    data.append(count)
                
                datasets.append({
                    "label": field2_val,
                    "data": data,
                    "backgroundColor": colors[i % len(colors)],
                    "borderColor": colors[i % len(colors)].replace("0.6", "1"),
                    "borderWidth": 1
                })
            
            result = {
                "success": True,
                "chart_type": "bar",
                "data": {
                    "labels": sorted_field1,
                    "datasets": datasets
                },
                "options": {
                    "scales": {
                        "x": {"stacked": True},
                        "y": {"stacked": True, "title": {"display": True, "text": "Count"}}
                    },
                    "plugins": {
                        "title": {"display": True, "text": f"{field1} by {field2}"}
                    }
                },
                "statistics": {
                    "field1": field1,
                    "field2": field2,
                    "field1_categories": len(sorted_field1),
                    "field2_categories": len(all_field2_values)
                }
            }
            
            return result
            
        except Exception as e:
            logger.error(f"Error generating category-category bar chart: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _generate_pie_statistics(self, layer, fields: List[str]) -> Dict:
        """Generate pie chart data (supports only 1 categorical field)"""
        try:
            if len(fields) != 1:
                return {"success": False, "error": "Pie chart supports only 1 field"}
            
            field_name = fields[0]
            return self._generate_single_field_pie(layer, field_name)
            
        except Exception as e:
            logger.error(f"Error generating pie statistics: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _generate_single_field_pie(self, layer, field_name: str) -> Dict:
        """Generate pie chart for single categorical field"""
        try:
            # Get value counts (same as single bar, but formatted for pie)
            value_counts = {}
            with arcpy.da.SearchCursor(layer, [field_name]) as cursor:
                for row in cursor:
                    value = row[0]
                    if value is not None:
                        value_str = str(value)
                        value_counts[value_str] = value_counts.get(value_str, 0) + 1
            
            if not value_counts:
                return {"success": False, "error": "No valid data for pie chart"}
            
            # Sort by count and limit to avoid cluttered pie
            sorted_items = sorted(value_counts.items(), key=lambda x: x[1], reverse=True)
            if len(sorted_items) > 8:
                # Keep top 7 and group the rest as "Others"
                top_items = sorted_items[:7]
                others_count = sum(item[1] for item in sorted_items[7:])
                if others_count > 0:
                    top_items.append(("Others", others_count))
                sorted_items = top_items
            
            labels = [item[0] for item in sorted_items]
            data = [item[1] for item in sorted_items]
            
            # Generate colors
            colors = [
                "rgba(255, 99, 132, 0.8)", "rgba(54, 162, 235, 0.8)", "rgba(255, 205, 86, 0.8)",
                "rgba(75, 192, 192, 0.8)", "rgba(153, 102, 255, 0.8)", "rgba(255, 159, 64, 0.8)",
                "rgba(199, 199, 199, 0.8)", "rgba(83, 102, 255, 0.8)"
            ]
            
            result = {
                "success": True,
                "chart_type": "pie",
                "data": {
                    "labels": labels,
                    "datasets": [{
                        "data": data,
                        "backgroundColor": colors[:len(data)],
                        "borderColor": [color.replace("0.8", "1") for color in colors[:len(data)]],
                        "borderWidth": 1
                    }]
                },
                "options": {
                    "plugins": {
                        "title": {"display": True, "text": f"Distribution of {field_name}"},
                        "legend": {"position": "right"}
                    }
                },
                "statistics": {
                    "total_categories": len(sorted_items),
                    "total_records": sum(data),
                    "field": field_name
                }
            }
            
            return result
            
        except Exception as e:
            logger.error(f"Error generating pie chart: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _generate_histogram_statistics(self, layer, fields: List[str]) -> Dict:
        """Generate histogram data (supports only 1 numeric field)"""
        try:
            if len(fields) != 1:
                return {"success": False, "error": "Histogram supports only 1 field"}
            
            field_name = fields[0]
            
            # Get all numeric values
            values = []
            with arcpy.da.SearchCursor(layer, [field_name]) as cursor:
                for row in cursor:
                    value = row[0]
                    if value is not None:
                        values.append(float(value))
            
            if len(values) < 2:
                return {"success": False, "error": "Insufficient data for histogram"}
            
            # Calculate histogram bins
            num_bins = min(30, max(5, int(len(values) ** 0.5)))  # Square root rule with limits
            min_val, max_val = min(values), max(values)
            
            if min_val == max_val:
                return {"success": False, "error": "All values are identical, cannot create histogram"}
            
            bin_width = (max_val - min_val) / num_bins
            bins = [min_val + i * bin_width for i in range(num_bins + 1)]
            
            # Count values in each bin
            bin_counts = [0] * num_bins
            for value in values:
                bin_index = min(num_bins - 1, int((value - min_val) / bin_width))
                bin_counts[bin_index] += 1
            
            # Create labels for bins (midpoints)
            bin_labels = [f"{bins[i]:.2f}-{bins[i+1]:.2f}" for i in range(num_bins)]
            
            result = {
                "success": True,
                "chart_type": "bar",  # Chart.js uses bar chart for histograms
                "data": {
                    "labels": bin_labels,
                    "datasets": [{
                        "label": f"Frequency of {field_name}",
                        "data": bin_counts,
                        "backgroundColor": "rgba(75, 192, 192, 0.6)",
                        "borderColor": "rgba(75, 192, 192, 1)",
                        "borderWidth": 1
                    }]
                },
                "options": {
                    "scales": {
                        "x": {"title": {"display": True, "text": field_name}},
                        "y": {"title": {"display": True, "text": "Frequency"}}
                    },
                    "plugins": {
                        "title": {"display": True, "text": f"Distribution of {field_name}"}
                    }
                },
                "statistics": {
                    "field": field_name,
                    "num_bins": num_bins,
                    "min_value": min_val,
                    "max_value": max_val,
                    "total_values": len(values)
                }
            }
            
            return result
            
        except Exception as e:
            logger.error(f"Error generating histogram: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _generate_line_statistics(self, layer, fields: List[str]) -> Dict:
        """Generate line chart data (typically for time series or ordered data)"""
        try:
            if len(fields) < 1 or len(fields) > 3:
                return {"success": False, "error": "Line chart supports 1-3 fields"}
            
            # For simplicity, treat as multiple series line chart
            # First field is x-axis (or index), rest are y-series
            
            if len(fields) == 1:
                # Single field line chart (value vs index)
                return self._generate_single_field_line(layer, fields[0])
            else:
                # Multi-field line chart (first field as x, others as y series)
                return self._generate_multi_field_line(layer, fields)
                
        except Exception as e:
            logger.error(f"Error generating line statistics: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _generate_single_field_line(self, layer, field_name: str) -> Dict:
        """Generate line chart for single field (value vs index/order)"""
        try:
            values = []
            with arcpy.da.SearchCursor(layer, [field_name]) as cursor:
                for i, row in enumerate(cursor):
                    value = row[0]
                    if value is not None:
                        values.append({"x": i, "y": float(value)})
            
            if len(values) < 2:
                return {"success": False, "error": "Insufficient data for line chart"}
            
            result = {
                "success": True,
                "chart_type": "line",
                "data": {
                    "datasets": [{
                        "label": field_name,
                        "data": values,
                        "borderColor": "rgba(75, 192, 192, 1)",
                        "backgroundColor": "rgba(75, 192, 192, 0.2)",
                        "fill": False,
                        "tension": 0.1
                    }]
                },
                "options": {
                    "scales": {
                        "x": {"title": {"display": True, "text": "Index"}},
                        "y": {"title": {"display": True, "text": field_name}}
                    },
                    "plugins": {
                        "title": {"display": True, "text": f"{field_name} Trend"}
                    }
                },
                "statistics": {
                    "field": field_name,
                    "total_points": len(values)
                }
            }
            
            return result
            
        except Exception as e:
            logger.error(f"Error generating single field line chart: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _generate_multi_field_line(self, layer, fields: List[str]) -> Dict:
        """Generate multi-series line chart"""
        try:
            # Get data for all fields
            all_data = []
            with arcpy.da.SearchCursor(layer, fields) as cursor:
                for i, row in enumerate(cursor):
                    if all(val is not None for val in row):
                        data_point = {"index": i}
                        for j, field in enumerate(fields):
                            data_point[field] = float(row[j])
                        all_data.append(data_point)
            
            if len(all_data) < 2:
                return {"success": False, "error": "Insufficient data for multi-field line chart"}
            
            # Create datasets for each field
            colors = ["rgba(75, 192, 192, 1)", "rgba(255, 99, 132, 1)", "rgba(54, 162, 235, 1)"]
            datasets = []
            
            for i, field in enumerate(fields):
                data_points = [{"x": point["index"], "y": point[field]} for point in all_data]
                datasets.append({
                    "label": field,
                    "data": data_points,
                    "borderColor": colors[i % len(colors)],
                    "backgroundColor": colors[i % len(colors)].replace("1)", "0.2)"),
                    "fill": False,
                    "tension": 0.1
                })
            
            result = {
                "success": True,
                "chart_type": "line",
                "data": {"datasets": datasets},
                "options": {
                    "scales": {
                        "x": {"title": {"display": True, "text": "Index"}},
                        "y": {"title": {"display": True, "text": "Value"}}
                    },
                    "plugins": {
                        "title": {"display": True, "text": f"Trend Comparison: {', '.join(fields)}"}
                    }
                },
                "statistics": {
                    "fields": fields,
                    "total_points": len(all_data)
                }
            }
            
            return result
            
        except Exception as e:
            logger.error(f"Error generating multi-field line chart: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _get_field_basic_type(self, layer, field_name: str) -> Dict:
        """Helper function to determine if a field is categorical or numeric"""
        try:
            # Get field info from ArcGIS
            fields = arcpy.ListFields(layer)
            target_field = next((f for f in fields if f.name == field_name), None)
            
            if not target_field:
                return {"is_categorical": False, "is_numeric": False, "error": "Field not found"}
            
            # Determine type based on ArcGIS field type
            numeric_types = ['SmallInteger', 'Integer', 'Single', 'Double']
            text_types = ['String', 'Text']
            
            is_numeric = target_field.type in numeric_types
            is_categorical = target_field.type in text_types
            
            # For numeric fields, check if they're actually categorical (low unique count)
            if is_numeric:
                # Quick sample to check uniqueness
                unique_values = set()
                sample_count = 0
                with arcpy.da.SearchCursor(layer, [field_name]) as cursor:
                    for row in cursor:
                        if row[0] is not None:
                            unique_values.add(row[0])
                            sample_count += 1
                        if sample_count >= 100:  # Sample first 100 records
                            break
                
                # If few unique values relative to sample, treat as categorical
                if sample_count > 0 and len(unique_values) <= min(20, sample_count * 0.1):
                    is_categorical = True
                    is_numeric = False  # Treat as categorical for grouping purposes
            
            return {
                "is_categorical": is_categorical,
                "is_numeric": is_numeric,
                "field_type": target_field.type
            }
            
        except Exception as e:
            logger.error(f"Error determining field type for {field_name}: {str(e)}")
            return {"is_categorical": False, "is_numeric": False, "error": str(e)}
    
    def _calculate_correlation(self, x_values: List[float], y_values: List[float]) -> float:
        """Calculate Pearson correlation coefficient between two numeric arrays"""
        try:
            if len(x_values) != len(y_values) or len(x_values) < 2:
                return 0.0
            
            n = len(x_values)
            sum_x = sum(x_values)
            sum_y = sum(y_values)
            sum_xy = sum(x * y for x, y in zip(x_values, y_values))
            sum_x2 = sum(x * x for x in x_values)
            sum_y2 = sum(y * y for y in y_values)
            
            numerator = n * sum_xy - sum_x * sum_y
            denominator = math.sqrt((n * sum_x2 - sum_x * sum_x) * (n * sum_y2 - sum_y * sum_y))
            
            if denominator == 0:
                return 0.0
            
            return numerator / denominator
            
        except Exception:
            return 0.0
    
    def generate_widget_chart_data(self, layer_name: str, widget_id: str = None, fields: List[str] = None, chart_type: str = None) -> Dict:
        """
        Main function to generate Chart.js-ready data for a specific widget or field combination.
        Can work with existing dashboard layout or custom field/chart combinations.
        
        Args:
            layer_name: Name of the ArcGIS layer
            widget_id: ID of widget from dashboard layout (optional)
            fields: List of field names (optional, used if widget_id not provided)
            chart_type: Chart type (optional, used if widget_id not provided)
            
        Returns:
            Dictionary with Chart.js-ready data structure
        """
        logger.info(f"Generating chart data for layer: {layer_name}, widget: {widget_id}, fields: {fields}, type: {chart_type}")
        
        try:
            # If widget_id provided, get fields and chart_type from dashboard layout
            if widget_id:
                widget_info = self._get_widget_info(widget_id)
                if not widget_info.get("success"):
                    return widget_info
                fields = widget_info.get("fields", [])
                chart_type = widget_info.get("chart_type")
            
            # Validate inputs
            if not fields or not chart_type:
                return {"success": False, "error": "Both fields and chart_type are required"}
            
            # Generate statistics using the multi-field system
            stats_result = self.generate_multi_field_statistics(layer_name, fields, chart_type)
            
            if not stats_result.get("success"):
                return stats_result
            
            # Add widget metadata
            stats_result["widget_info"] = {
                "widget_id": widget_id,
                "fields": fields,
                "chart_type": chart_type,
                "layer_name": layer_name
            }
            
            logger.info(f"Successfully generated chart data for {chart_type} chart with {len(fields)} fields")
            return stats_result
            
        except Exception as e:
            logger.error(f"Error generating widget chart data: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _get_widget_info(self, widget_id: str) -> Dict:
        """Get widget configuration from dashboard layout"""
        try:
            dashboard_layout = self.get_current_dashboard_layout()
            if not dashboard_layout.get("success"):
                return dashboard_layout
            
            widgets = dashboard_layout.get("widgets", [])
            target_widget = next((w for w in widgets if w.get("id") == widget_id), None)
            
            if not target_widget:
                return {"success": False, "error": f"Widget '{widget_id}' not found in dashboard layout"}
            
            return {
                "success": True,
                "fields": target_widget.get("fields", []),
                "chart_type": target_widget.get("chart_type"),
                "widget_config": target_widget
            }
            
        except Exception as e:
            logger.error(f"Error getting widget info for {widget_id}: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def generate_all_dashboard_data(self, layer_name: str) -> Dict:
        """
        Generate Chart.js data for all widgets in the current dashboard layout.
        Returns a complete data package for the frontend.
        """
        logger.info(f"Generating data for all dashboard widgets for layer: {layer_name}")
        
        try:
            # Get current dashboard layout
            layout_result = self.get_current_dashboard_layout()
            if not layout_result.get("success"):
                return layout_result
            
            widgets = layout_result.get("widgets", [])
            if not widgets:
                return {"success": False, "error": "No widgets found in dashboard layout"}
            
            # Generate data for each widget
            widget_data = {}
            errors = []
            
            for widget in widgets:
                widget_id = widget.get("id")
                fields = widget.get("fields", [])
                chart_type = widget.get("chart_type")
                
                if not widget_id or not fields or not chart_type:
                    errors.append(f"Invalid widget configuration: {widget_id}")
                    continue
                
                try:
                    chart_data = self.generate_multi_field_statistics(layer_name, fields, chart_type)
                    if chart_data.get("success"):
                        widget_data[widget_id] = chart_data
                    else:
                        errors.append(f"Failed to generate data for widget {widget_id}: {chart_data.get('error')}")
                        
                except Exception as widget_error:
                    errors.append(f"Error processing widget {widget_id}: {str(widget_error)}")
            
            result = {
                "success": True,
                "layer_name": layer_name,
                "total_widgets": len(widgets),
                "successful_widgets": len(widget_data),
                "widget_data": widget_data,
                "dashboard_layout": widgets,
                "generation_timestamp": self._get_timestamp()
            }
            
            if errors:
                result["errors"] = errors
                result["error_count"] = len(errors)
            
            logger.info(f"Generated data for {len(widget_data)}/{len(widgets)} widgets")
            return result
            
        except Exception as e:
            logger.error(f"Error generating all dashboard data: {str(e)}")
            return {"success": False, "error": str(e)}
    def generate_smart_dashboard_layout(self, layer_name: str) -> Dict:
        """
        Analyzes a layer and generates a smart dashboard layout with recommended chart types.
        Returns a JSON object with the dashboard layout and saves it to smart_dashboard.json.
        """
        logger.info(f"Generating smart dashboard layout for layer: {layer_name}")
        
        try:
            # Step 1: Analyze the layer fields
            analysis_result = self.analyze_layer_fields(layer_name)
            if not analysis_result.get("success"):
                return analysis_result
            
            field_insights = analysis_result.get("field_insights", {})
            
            # Step 2: Recommend chart types based on field analysis
            chart_recommendations = self.recommend_chart_types(field_insights)
            
            # Step 3: Plan the dashboard layout
            dashboard_layout = self.plan_dashboard_layout(chart_recommendations)
            
            # Step 4: Build complete dashboard data with field insights
            complete_dashboard = {
                "layer_name": layer_name,
                "analysis_timestamp": analysis_result.get("analysis_timestamp"),
                "total_features": analysis_result.get("total_features"),
                "fields_analyzed": analysis_result.get("fields_analyzed"),
                "field_insights": field_insights,
                "chart_recommendations": chart_recommendations,
                "dashboard_layout": dashboard_layout.get("dashboard_layout", [])
            }
            
            # Save complete dashboard data to JSON file
            dashboard_file = "smart_dashboard.json"
            with open(dashboard_file, "w") as f:
                json.dump(complete_dashboard, f, indent=4)
            
            result = {
                "success": True,
                "layer_name": layer_name,
                # "dashboard_layout": dashboard_layout,
                "field_insights": field_insights,
                # "chart_recommendations": chart_recommendations,
                "output_file": dashboard_file,
                "message": f"Smart dashboard layout with field analysis generated and saved to {dashboard_file}"
            }

            # Notify frontend via websocket if available
            if self.websocket_manager is not None:
                try:
                    self.websocket_manager.send_dashboard_update(complete_dashboard)
                    logger.info("Complete dashboard data sent to frontend via websocket_manager.")
                except Exception as ws_e:
                    logger.error(f"Failed to send dashboard update via websocket_manager: {ws_e}")

            logger.info(f"Smart dashboard layout generated: {result}")
            return result
            
        except Exception as e:
            logger.error(f"generate_smart_dashboard_layout error: {str(e)}")
            return {"success": False, "error": str(e)}

    def recommend_chart_types(self, field_insights: Dict) -> Dict:
        """
        Recommends chart types for each field based on its AI-generated insights.
        Returns a dictionary of field names and their recommended chart types.
        """
        recommendations = {}
        for field_name, insights in field_insights.items():
            ai_insights = insights.get("ai_insights", {})
            chart_suitability = ai_insights.get("chart_suitability", {})
            
            # Sort charts by suitability score
            sorted_charts = sorted(chart_suitability.items(), key=lambda item: item[1], reverse=True)
            
            # Recommend the top 1-2 charts
            recommended_charts = [chart for chart, score in sorted_charts[:2] if score > 0.6]
            
            if recommended_charts:
                recommendations[field_name] = {
                    "recommended_charts": recommended_charts,
                    "visualization_potential": ai_insights.get("visualization_potential", "low"),
                    "visualization_priority": ai_insights.get("visualization_priority", 5)
                }
        
        return recommendations

    def plan_dashboard_layout(self, chart_recommendations: Dict) -> Dict:
        """
        Plans the layout of a 12x6 grid dashboard based on chart recommendations.
        Returns a JSON object representing the grid layout with chart placements.
        """
        # Sort fields by visualization priority (descending)
        sorted_fields = sorted(
            chart_recommendations.items(), 
            key=lambda item: item[1].get("visualization_priority", 5), 
            reverse=True
        )
        grid_width = 12
        grid_height = 6
        layout = []
        current_x = 0
        current_y = 0
        for field_name, recs in sorted_fields:
            chart_type = recs["recommended_charts"][0] if recs["recommended_charts"] else "indicator"
            widget_size = {"w": 3, "h": 2}
            if chart_type in ["bar", "column", "line_chart", "timeline"]:
                widget_size = {"w": 4, "h": 2}
            elif chart_type in ["pie", "donut"]:
                widget_size = {"w": 2, "h": 2}
            elif chart_type == "indicator":
                widget_size = {"w": 2, "h": 2}
            if current_x + widget_size["w"] > grid_width:
                current_x = 0
                current_y += widget_size["h"]
            if current_y + widget_size["h"] > grid_height:
                continue
            layout.append({
                "id": f"widget_{field_name}",
                "x": current_x,
                "y": current_y,
                "w": widget_size["w"],
                "h": widget_size["h"],
                "fields": [field_name],  # Changed to array for multi-field support
                "chart_type": chart_type
            })
            current_x += widget_size["w"]
        layout = self._expand_last_widget_in_row(layout, grid_width)
        return {"dashboard_layout": layout}

    def _expand_last_widget_in_row(self, layout, grid_width):
        """
        For each row, if the total width is less than grid_width, expand the last widget in the row to fill the row.
        """
        if not layout:
            return layout
        # Group widgets by row (y)
        from collections import defaultdict
        rows = defaultdict(list)
        for widget in layout:
            rows[widget["y"]].append(widget)
        for y, widgets in rows.items():
            # Sort widgets in row by x
            widgets.sort(key=lambda w: w["x"])
            total_w = sum(w["w"] for w in widgets)
            if total_w < grid_width and widgets:
                widgets[-1]["w"] += grid_width - total_w
        # Flatten back to list, preserving order
        new_layout = []
        for y in sorted(rows.keys()):
            new_layout.extend(sorted(rows[y], key=lambda w: w["x"]))
        return new_layout


    def optimize_dashboard_layout(self, widget_list) -> Dict:
        """
        Validates and arranges the dashboard layout (positions, sizes) for a list of widgets.
        Only checks/optimizes layout (coordinates, size, overlap, grid fit).
        Returns validation results and the layout if valid.
        """
        if not isinstance(widget_list, list):
            logger.error(f"Expected list of widgets, got: {type(widget_list)}")
            return {"success": False, "error": "Layout must be a list of widget objects"}

        if not widget_list:
            return {"success": True, "optimized_layout": []}

        grid_width = 12
        grid_height = 6
        errors = []

        # Check each widget for bounds and overlaps
        occupied = [[False]*grid_width for _ in range(grid_height)]

        for i, widget in enumerate(widget_list):
            x, y = widget.get("x", 0), widget.get("y", 0)
            w, h = widget.get("w", 1), widget.get("h", 1)
            widget_id = widget.get("id", f"widget_{i}")

            # Check bounds
            if x + w > grid_width or y + h > grid_height:
                errors.append(f"Widget {widget_id} exceeds grid bounds: ({x},{y}) size {w}x{h}")
                continue

            if x < 0 or y < 0:
                errors.append(f"Widget {widget_id} has negative coordinates: ({x},{y})")
                continue

            # Check overlaps
            overlap = False
            for dy in range(h):
                for dx in range(w):
                    if occupied[y+dy][x+dx]:
                        errors.append(f"Widget {widget_id} overlaps at position ({x+dx},{y+dy})")
                        overlap = True
                        break
                if overlap:
                    break

            if not overlap:
                # Mark as occupied
                for dy in range(h):
                    for dx in range(w):
                        occupied[y+dy][x+dx] = True

        if errors:
            return {"success": False, "errors": errors, "optimized_layout": widget_list}
        else:
            # Save the optimized layout to smart_dashboard.json while preserving all existing data
            import json
            from pathlib import Path
            dashboard_path = Path(__file__).parent.parent / "smart_dashboard.json"
            try:
                dashboard_data = {}
                if dashboard_path.exists():
                    with open(dashboard_path, "r", encoding="utf-8") as f:
                        dashboard_data = json.load(f)
                dashboard_data["dashboard_layout"] = widget_list
                with open(dashboard_path, "w", encoding="utf-8") as f:
                    json.dump(dashboard_data, f, indent=4)
                logger.info(f"Successfully saved optimized layout with {len(widget_list)} widgets while preserving field insights.")
            except Exception as e:
                logger.error(f"Failed to save optimized dashboard layout: {e}")
                return {"success": False, "error": f"Failed to save optimized layout: {e}", "optimized_layout": widget_list}
            return {"success": True, "optimized_layout": widget_list}


    def get_current_dashboard_layout(self) -> Dict:
        """
        Get the current dashboard layout from the smart_dashboard.json file.
        Returns the dashboard layout as a dictionary.
        """
        import json
        from pathlib import Path
        dashboard_path = Path(__file__).parent.parent / "smart_dashboard.json"
        try:
            with open(dashboard_path, "r", encoding="utf-8") as f:
                dashboard_data = json.load(f)
            # Try to find the layout list
            layout = []
            if isinstance(dashboard_data, dict):
                layout = dashboard_data.get("dashboard_layout") or dashboard_data.get("layout") or []
            elif isinstance(dashboard_data, list):
                layout = dashboard_data
            # Only return minimal widget info
            minimal_widgets = []
            for widget in layout:
                minimal_widgets.append({
                    "id": widget.get("id"),
                    "x": widget.get("x"),
                    "y": widget.get("y"),
                    "w": widget.get("w"),
                    "h": widget.get("h"),
                    "fields": widget.get("fields", [widget.get("field")] if widget.get("field") else [])  # Convert legacy field to fields array
                })
            return {"success": True, "widgets": minimal_widgets}
        except Exception as e:
            logger.error(f"Failed to load dashboard layout: {e}")
            return {"success": False, "error": str(e)}
        
    def get_field_stories_and_samples(self) -> dict:
        """
        Returns a summary for each field: field_name, data_story, and sample_values from smart_dashboard.json.
        Handles empty or invalid JSON files gracefully.
        """
        import json
        from pathlib import Path
        dashboard_path = Path(__file__).parent.parent / "smart_dashboard.json"
        try:
            if not dashboard_path.exists() or dashboard_path.stat().st_size == 0:
                return {"success": False, "error": "Dashboard file is missing or empty."}
            with open(dashboard_path, "r", encoding="utf-8") as f:
                try:
                    dashboard_data = json.load(f)
                except json.JSONDecodeError:
                    return {"success": False, "error": "Dashboard file is not valid JSON."}
            field_insights = dashboard_data.get("field_insights", {})
            if not isinstance(field_insights, dict) or not field_insights:
                return {"success": False, "error": "No field insights found in dashboard."}
            result = []
            for field, info in field_insights.items():
                if not isinstance(info, dict):
                    continue
                story = None
                if "ai_insights" in info and isinstance(info["ai_insights"], dict):
                    story = info["ai_insights"].get("data_story")
                result.append({
                    "field_name": info.get("field_name", field),
                    "data_story": story,
                    "sample_values": info.get("sample_values", [])
                })
            return {"success": True, "fields": result}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    
    def get_current_dashboard_charts(self) -> dict:
        """
        Get the current [fields, chart_type] pairs from the dashboard layout in smart_dashboard.json.
        Returns a list of dicts: {"fields": [...], "chart_type": ...}
        """
        from pathlib import Path
        import json
        dashboard_path = Path(__file__).parent.parent / "smart_dashboard.json"
        try:
            with open(dashboard_path, "r", encoding="utf-8") as f:
                dashboard_data = json.load(f)
            layout = []
            if isinstance(dashboard_data, dict):
                layout = dashboard_data.get("dashboard_layout") or dashboard_data.get("layout") or []
            elif isinstance(dashboard_data, list):
                layout = dashboard_data
            chart_list = []
            for widget in layout:
                # Support both legacy "field" and new "fields" array format
                fields = widget.get("fields", [widget.get("field")] if widget.get("field") else [])
                chart_type = widget.get("chart_type")
                if fields and chart_type:
                    chart_list.append({"fields": fields, "chart_type": chart_type})
            return {"success": True, "charts": chart_list}
        except Exception as e:
            return {"success": False, "error": str(e)}
        
        
        
    def update_dashboard_charts(self, layer_name: str, charts: List[dict], generate_data: bool = True) -> dict:
        """
            Enhanced function that updates dashboard charts with fields/chart_types AND generates Chart.js data.
            Combines layout updates with multi-field statistics generation for complete chart updates.

            Note:
                All chart types currently support at most two fields. If more than two fields are provided for any chart,
                only the first two fields will be used for data generation and layout updates.

            Args:
                layer_name: Name of the ArcGIS layer to generate data from
                charts: List of {fields, chart_type} dicts (as from get_current_dashboard_charts)
                generate_data: Whether to generate Chart.js data for the updated charts (default: True)

            Returns:
                Dictionary with success status, updated layout, and optionally generated chart data
            """
        from pathlib import Path
        import json
        dashboard_path = Path(__file__).parent.parent / "smart_dashboard.json"
        
        try:
            if not isinstance(charts, list) or not charts:
                return {"success": False, "error": "Input must be a non-empty list of chart dicts"}
            if not dashboard_path.exists():
                return {"success": False, "error": "Dashboard file not found"}
                
            # Load current dashboard data
            with open(dashboard_path, "r", encoding="utf-8") as f:
                dashboard_data = json.load(f)
                
            original_is_dict = isinstance(dashboard_data, dict)
            if original_is_dict:
                layout = dashboard_data.get("dashboard_layout") or dashboard_data.get("layout") or []
            else:
                layout = dashboard_data if isinstance(dashboard_data, list) else []
                
            if not isinstance(layout, list) or not layout:
                return {"success": False, "error": "No dashboard layout found to update"}
            
            # Update layout with new chart configurations
            updated = 0
            chart_data_results = {}
            generation_errors = []
            
            for i, chart in enumerate(charts):
                if i >= len(layout):
                    break
                    
                fields = chart.get("fields")
                chart_type = chart.get("chart_type")
                
                if not fields or not chart_type:
                    continue
                
                # Update the layout
                widget_id = layout[i].get("id", f"widget_{i}")
                layout[i]["fields"] = fields
                layout[i].pop("field", None)  # Remove legacy field property
                layout[i]["chart_type"] = chart_type
                updated += 1
                
                # Generate Chart.js data if requested
                if generate_data:
                    try:
                        logger.info(f"Generating chart data for widget {widget_id}: {fields} -> {chart_type}")
                        chart_stats = self.generate_multi_field_statistics(layer_name, fields, chart_type)
                        
                        if chart_stats.get("success"):
                            # Add widget metadata
                            chart_stats["widget_info"] = {
                                "widget_id": widget_id,
                                "fields": fields,
                                "chart_type": chart_type,
                                "layer_name": layer_name,
                                "position": {"x": layout[i].get("x"), "y": layout[i].get("y")},
                                "size": {"w": layout[i].get("w"), "h": layout[i].get("h")}
                            }
                            chart_data_results[widget_id] = chart_stats
                            logger.info(f"✅ Generated data for {widget_id}: {chart_type} with {len(fields)} fields")
                        else:
                            error_msg = f"Failed to generate data for widget {widget_id}: {chart_stats.get('error')}"
                            generation_errors.append(error_msg)
                            logger.error(error_msg)
                            
                    except Exception as chart_error:
                        error_msg = f"Error generating data for widget {widget_id}: {str(chart_error)}"
                        generation_errors.append(error_msg)
                        logger.error(error_msg)
            
            # Save updated layout
            if updated:
                if original_is_dict:
                    dashboard_data["dashboard_layout"] = layout
                    # Update timestamp
                    dashboard_data["last_updated"] = self._get_timestamp()
                else:
                    dashboard_data = layout
                    
                with open(dashboard_path, "w", encoding="utf-8") as f:
                    json.dump(dashboard_data, f, indent=4)
                logger.info(f"Successfully updated {updated} widgets in dashboard layout")
            
            # Build result
            result = {
                "success": True,
                "updated_count": updated,
                # "charts": charts,
                "layer_name": layer_name
            }
            
            if generate_data:
                result["chart_data"] = chart_data_results
                result["successful_data_generation"] = len(chart_data_results)
                result["total_data_attempts"] = len([c for c in charts if c.get("fields") and c.get("chart_type")])
                
                if generation_errors:
                    result["generation_errors"] = generation_errors
                    result["error_count"] = len(generation_errors)
                
                # Notify frontend via websocket if available and data was generated
                if chart_data_results and self.websocket_manager is not None:
                    try:
                        websocket_data = {
                            "type": "dashboard_charts_updated",
                            "layer_name": layer_name,
                            "updated_widgets": list(chart_data_results.keys()),
                            "chart_data": chart_data_results,
                            "layout": layout
                        }
                        self.websocket_manager.send_dashboard_update(websocket_data)
                        logger.info(f"Sent updated chart data to frontend via websocket for {len(chart_data_results)} widgets")
                    except Exception as ws_error:
                        logger.error(f"Failed to send websocket update: {ws_error}")
            
            return result
            
        except Exception as e:
            logger.error(f"Error in update_dashboard_charts: {str(e)}")
            return {"success": False, "error": str(e)}
    
