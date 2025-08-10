"""
Spatial Functions Module - GIS analysis operations
"""

import os
import logging
import math
import json
import asyncio
import statistics
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
        34: "get_current_dashboard_layout"
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
        Returns detailed field metadata including data types, unique values, null percentages, etc.
        """
        logger.info(f"Starting field analysis for layer: {layer_name}")
        
        try:
            # Get current project and map
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            
            # Find the layer
            target_layer = None
            for layer in map_obj.listLayers():
                if layer.name == layer_name:
                    target_layer = layer
                    break
            
            if not target_layer:
                return {"success": False, "error": f"Layer '{layer_name}' not found"}
            
            if not target_layer.isFeatureLayer:
                return {"success": False, "error": f"Layer '{layer_name}' is not a feature layer"}
            
            # Get field definitions
            fields = arcpy.ListFields(target_layer)
            field_analysis = {}
            
            # Get total feature count
            total_count = int(arcpy.GetCount_management(target_layer)[0])
            
            # Analyze each field
            for field in fields:
                # Skip system fields like OBJECTID, Shape, etc.
                if field.name.upper() in ['OBJECTID', 'SHAPE', 'SHAPE_LENGTH', 'SHAPE_AREA', 'GLOBALID']:
                    continue
                
                field_info = {
                    "field_name": field.name,
                    "field_type": field.type,
                    "field_length": field.length if hasattr(field, 'length') else None,
                    "field_precision": field.precision if hasattr(field, 'precision') else None,
                    "field_scale": field.scale if hasattr(field, 'scale') else None,
                    "total_records": total_count
                }
                
                # Calculate field statistics based on type
                if field.type in ['SmallInteger', 'Integer', 'Single', 'Double']:
                    # Numeric field analysis
                    field_info.update(self._analyze_numeric_field(target_layer, field.name, total_count))
                elif field.type in ['String', 'Text']:
                    # Text field analysis
                    field_info.update(self._analyze_text_field(target_layer, field.name, total_count))
                elif field.type == 'Date':
                    # Date field analysis
                    field_info.update(self._analyze_date_field(target_layer, field.name, total_count))
                else:
                    # Generic analysis for other types
                    field_info.update(self._analyze_generic_field(target_layer, field.name, total_count))
                
                # Step 2 Enhancement: Add AI-ready insights for better chart selection
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
        
        # Define grid dimensions
        grid_width = 12
        grid_height = 6
        layout = []
        
        # Place charts on the grid
        current_x = 0
        current_y = 0
        
        for field_name, recs in sorted_fields:
            chart_type = recs["recommended_charts"][0] if recs["recommended_charts"] else "indicator"
            
            # Define default widget sizes
            widget_size = {"w": 3, "h": 2} # Default size (reduced)
            if chart_type in ["bar", "column", "line_chart", "timeline"]:
                widget_size = {"w": 4, "h": 2}
            elif chart_type in ["pie", "donut"]:
                widget_size = {"w": 2, "h": 2}
            elif chart_type == "indicator":
                widget_size = {"w": 2, "h": 2}
            
            # Check if widget fits in the current row
            if current_x + widget_size["w"] > grid_width:
                current_x = 0
                current_y += widget_size["h"] # Move to next row
            
            # Check if widget fits on the grid at all
            if current_y + widget_size["h"] > grid_height:
                continue # Skip if it doesn't fit
            
            # Add widget to layout
            layout.append({
                "id": f"widget_{field_name}",
                "x": current_x,
                "y": current_y,
                "w": widget_size["w"],
                "h": widget_size["h"],
                "field": field_name,
                "chart_type": chart_type
            })
            
            # Update current position
            current_x += widget_size["w"]
            
        return {"dashboard_layout": layout}

    def optimize_dashboard_layout(self, layout) -> Dict:
        """
        Validates and applies AI-suggested dashboard layout.
        Takes the AI's exact positioning and validates it fits in a 12x6 grid without overlaps.
        Returns validation results and the layout if valid.
        """
        # Handle different input formats
        if isinstance(layout, dict):
            widget_list = layout.get("layout", layout.get("dashboard_layout", []))
        elif isinstance(layout, list):
            widget_list = layout
        else:
            logger.error(f"Invalid layout input type: {type(layout)}")
            return {"success": False, "error": f"Invalid layout input type: {type(layout)}"}
        
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
                    "h": widget.get("h")
                })
            return {"success": True, "widgets": minimal_widgets}
        except Exception as e:
            logger.error(f"Failed to load dashboard layout: {e}")
            return {"success": False, "error": str(e)}
