"""
Spatial Functions Module - GIS analysis operations
"""

import os
import logging
import math
import json
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
LOG_FILE_PATH = Path(__file__).parent.parent / "logs" / "spatial_functions.log"
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
    def __init__(self):
        self.supported_formats = ['.shp', '.geojson', '.kml', '.gpx', '.gml']
        self.AVAILABLE_FUNCTIONS = {
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
            33: "plan_dashboard_layout"
        }
        

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

        # ... Rest of functions 
        

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
            lyr = None
            for l in map_obj.listLayers():
                if l.name == layer_name:
                    lyr = l
                    break
            
            if not lyr:
                return {"success": False, "error": f"Layer {layer_name} not found"}
            
            # Convert distance to appropriate units for arcpy
            buffer_distance = f"{distance} {units.title()}"
            if units.lower() == "meters":
                buffer_distance = f"{distance} Meters"
            elif units.lower() == "kilometers":
                buffer_distance = f"{distance} Kilometers"
            elif units.lower() == "feet":
                buffer_distance = f"{distance} Feet"
            elif units.lower() == "miles":
                buffer_distance = f"{distance} Miles"
            
            # Create output path
            output_buffer = f"{layer_name}_ai"
            default_gdb = aprx.defaultGeodatabase
            output_path = os.path.join(default_gdb, output_buffer)
            
            # Create buffer
            arcpy.PairwiseBuffer_analysis(lyr, output_path, buffer_distance)
            
            # Add the buffer layer to the map
            buffer_layer = map_obj.addDataFromPath(output_path)
            
            # Get feature count
            features_processed = int(arcpy.GetCount_management(lyr)[0])
            
            result = {
                "function_executed": "create_buffer",
                "layer_name": layer_name,
                "distance": distance,
                "units": units,
                "success": True,
                "output": {
                    "buffer_layer": output_buffer,
                    "features_processed": features_processed,
                    "output_path": output_path,
                    "added_to_map": True
                }
            }
            logger.info(f"Buffer creation completed: {result}")
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
            output_name = f"{target_layer}_ai"
            default_gdb = aprx.defaultGeodatabase
            output_path = os.path.join(default_gdb, output_name)
            # Add the joined layer to the map
            joined_layer = map_obj.addDataFromPath(output_path)
            # Perform spatial join
            arcpy.SpatialJoin_analysis(target_lyr, join_lyr, output_path, 
                                     match_option=arcpy_join_op)
            
            # Count results
            joined_count = int(arcpy.GetCount_management(output_path)[0])
            original_count = int(arcpy.GetCount_management(target_lyr)[0])
            unmatched_count = original_count - joined_count
            
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
            output_name = f"{input_layer}_ai"
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
            output_name = f"{layer_name}_ai"
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
                patterns["likely_counts"] = True
            
            # Detect percentage-like data
            if 0 <= min_val <= 1 and 0 <= max_val <= 1:
                patterns["likely_percentage"] = True
            elif 0 <= min_val <= 100 and 0 <= max_val <= 100:
                patterns["likely_percentage_scale"] = True
            
            # Uniqueness patterns
            uniqueness_ratio = unique_count / total_records if total_records > 0 else 0
            if uniqueness_ratio > 0.9:
                patterns["high_uniqueness"] = True
            elif uniqueness_ratio < 0.1:
                patterns["low_uniqueness"] = True
                patterns["categorical_potential"] = True
            
            return patterns
            
        except Exception as e:
            logger.error(f"Error detecting numeric patterns: {str(e)}")
            return {"error": str(e)}
    
    def _calculate_median(self, values: List) -> float:
        """Calculate median value from a list of numbers"""
        try:
            sorted_values = sorted(values)
            n = len(sorted_values)
            if n % 2 == 0:
                return (sorted_values[n//2 - 1] + sorted_values[n//2]) / 2
            else:
                return sorted_values[n//2]
        except Exception:
            return 0.0
    
    def _calculate_std_dev(self, values: List, mean: float) -> float:
        """Calculate standard deviation"""
        try:
            variance = sum((x - mean) ** 2 for x in values) / len(values)
            return variance ** 0.5
        except Exception:
            return 0.0
    
    def _detect_outliers(self, values: List) -> Dict:
        """Detect outliers using IQR method"""
        try:
            sorted_values = sorted(values)
            n = len(sorted_values)
            
            q1_idx = n // 4
            q3_idx = 3 * n // 4
            q1 = sorted_values[q1_idx]
            q3 = sorted_values[q3_idx]
            iqr = q3 - q1
            
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            
            outliers = [v for v in values if v < lower_bound or v > upper_bound]
            
            return {
                "outlier_count": len(outliers),
                "outlier_percentage": (len(outliers) / len(values)) * 100 if values else 0,
                "lower_bound": lower_bound,
                "upper_bound": upper_bound
            }
        except Exception:
            return {"outlier_count": 0, "outlier_percentage": 0}
    
    def _analyze_text_patterns(self, values: List[str], unique_values: List[str]) -> Dict:
        """Analyze text patterns to provide better categorization insights"""
        try:
            import re
            
            patterns = {
                "has_consistent_format": False,
                "has_varied_length": False,
                "likely_codes": False,
                "likely_names": False,
                "contains_numbers": False,
                "contains_special_chars": False,
                "common_prefixes": [],
                "common_suffixes": []
            }
            
            if not values:
                return patterns
            
            # Analyze length consistency
            lengths = [len(v) for v in values]
            length_std = self._calculate_std_dev(lengths, sum(lengths) / len(lengths))
            patterns["has_consistent_format"] = length_std < 3.0  # Low variation in length
            patterns["has_varied_length"] = max(lengths) - min(lengths) > 50
            
            # Check for code-like patterns (alphanumeric, consistent format)
            code_pattern = re.compile(r'^[A-Za-z0-9_-]+$')
            code_like_count = sum(1 for v in unique_values[:20] if code_pattern.match(v))
            patterns["likely_codes"] = code_like_count / min(len(unique_values), 20) > 0.8
            
            # Check for name-like patterns (title case, spaces)
            name_patterns = [
                re.compile(r'^[A-Z][a-z]+ [A-Z][a-z]+'),  # "First Last"
                re.compile(r'^[A-Z][a-z]+$'),              # "Name"
                re.compile(r'^[A-Z][a-z]+ [a-z]+ [A-Z][a-z]+')  # "First middle Last"
            ]
            name_like_count = 0
            for v in unique_values[:20]:
                if any(pattern.match(v) for pattern in name_patterns):
                    name_like_count += 1
            patterns["likely_names"] = name_like_count / min(len(unique_values), 20) > 0.6
            
            # Check for numbers and special characters
            has_numbers = sum(1 for v in unique_values[:20] if any(c.isdigit() for c in v))
            patterns["contains_numbers"] = has_numbers / min(len(unique_values), 20) > 0.3
            
            special_char_pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
            has_special = sum(1 for v in unique_values[:20] if special_char_pattern.search(v))
            patterns["contains_special_chars"] = has_special / min(len(unique_values), 20) > 0.2
            
            # Find common prefixes and suffixes (if categorical)
            if len(unique_values) <= 50 and len(unique_values) > 1:
                # Common prefixes
                prefixes = {}
                for value in unique_values:
                    if len(value) >= 2:
                        prefix = value[:2]
                        prefixes[prefix] = prefixes.get(prefix, 0) + 1
                
                common_prefixes = [prefix for prefix, count in prefixes.items() 
                                 if count >= max(2, len(unique_values) * 0.3)]
                patterns["common_prefixes"] = common_prefixes[:3]
                
                # Common suffixes
                suffixes = {}
                for value in unique_values:
                    if len(value) >= 2:
                        suffix = value[-2:]
                        suffixes[suffix] = suffixes.get(suffix, 0) + 1
                
                common_suffixes = [suffix for suffix, count in suffixes.items() 
                                 if count >= max(2, len(unique_values) * 0.3)]
                patterns["common_suffixes"] = common_suffixes[:3]
            
            return patterns
            
        except Exception as e:
            logger.error(f"Error analyzing text patterns: {str(e)}")
            return {
                "has_consistent_format": False,
                "has_varied_length": False,
                "likely_codes": False,
                "likely_names": False,
                "contains_numbers": False,
                "contains_special_chars": False,
                "common_prefixes": [],
                "common_suffixes": []
            }
    
   
    def _generate_chart_recommendations(self, field_insights: Dict) -> List[Dict]:
        """Generate chart recommendations based on field analysis"""
        recommendations = []
        
        numeric_fields = []
        categorical_fields = []
        date_fields = []
        
        # Categorize fields
        for field_name, field_info in field_insights.items():
            category = field_info.get("data_category", "other")
            
            if "numeric" in category:
                numeric_fields.append((field_name, field_info))
            elif "categorical" in category:
                categorical_fields.append((field_name, field_info))
            elif category == "date":
                date_fields.append((field_name, field_info))
        
        # Generate recommendations
        
        # 1. Pie charts for categorical fields with reasonable unique counts
        for field_name, field_info in categorical_fields:
            if field_info.get("unique_count", 0) <= 10 and field_info.get("null_percentage", 100) < 50:
                recommendations.append({
                    "chart_type": "pie",
                    "title": f"Distribution of {field_name}",
                    "field": field_name,
                    "description": f"Pie chart showing the distribution of {field_info.get('unique_count', 0)} unique values in {field_name}",
                    "suitability_score": 0.9
                })
        
        # 2. Bar charts for categorical fields with more unique values
        for field_name, field_info in categorical_fields:
            if 10 < field_info.get("unique_count", 0) <= 20 and field_info.get("null_percentage", 100) < 50:
                recommendations.append({
                    "chart_type": "bar",
                    "title": f"Count by {field_name}",
                    "field": field_name,
                    "description": f"Bar chart showing counts for {field_info.get('unique_count', 0)} categories in {field_name}",
                    "suitability_score": 0.8
                })
        
        # 3. Histograms for continuous numeric fields
        for field_name, field_info in numeric_fields:
            if field_info.get("data_category") == "continuous_numeric" and field_info.get("null_percentage", 100) < 50:
                recommendations.append({
                    "chart_type": "histogram",
                    "title": f"Distribution of {field_name}",
                    "field": field_name,
                    "description": f"Histogram showing the distribution of values in {field_name}",
                    "range": f"{field_info.get('min_value', 'N/A')} to {field_info.get('max_value', 'N/A')}",
                    "suitability_score": 0.85
                })
        
        # 4. Scatter plots for pairs of numeric fields
        if len(numeric_fields) >= 2:
            for i, (field1_name, field1_info) in enumerate(numeric_fields):
                for field2_name, field2_info in numeric_fields[i+1:]:
                    if (field1_info.get("null_percentage", 100) < 30 and 
                        field2_info.get("null_percentage", 100) < 30):
                        recommendations.append({
                            "chart_type": "scatter",
                            "title": f"{field1_name} vs {field2_name}",
                            "x_field": field1_name,
                            "y_field": field2_name,
                            "description": f"Scatter plot comparing {field1_name} and {field2_name}",
                            "suitability_score": 0.7
                        })
        
        # 5. Time series for date fields
        for field_name, field_info in date_fields:
            if field_info.get("null_percentage", 100) < 50:
                recommendations.append({
                    "chart_type": "timeline",
                    "title": f"Timeline of {field_name}",
                    "field": field_name,
                    "description": f"Timeline visualization of {field_name}",
                    "date_range": f"{field_info.get('min_date', 'N/A')} to {field_info.get('max_date', 'N/A')}",
                    "suitability_score": 0.75
                })
        
        # Sort by suitability score
        recommendations.sort(key=lambda x: x.get("suitability_score", 0), reverse=True)
        
        return recommendations[:10]  # Return top 10 recommendations
    
    def generate_smart_dashboard_layout(self, layer_name: str) -> Dict:
        """
        Stage 2: Enhanced Chart Recommendation Engine with Layout Planning
        Generates intelligent chart recommendations with 12x9 grid layout planning
        """
        logger.info(f"Generating smart dashboard layout for layer: {layer_name}")
        
        try:
            # First get the field analysis
            field_analysis_result = self.analyze_layer_fields(layer_name)
            if not field_analysis_result.get("success", True):
                return field_analysis_result
            
            # Apply smart field filtering (Step 1)
            filter_result = self._filter_relevant_fields(field_analysis_result["field_insights"])
            filtered_field_insights = filter_result["filtered_insights"]
            classification_summary = filter_result["classification_summary"]
            
            logger.info(f"Field filtering: {classification_summary['relevant_fields']}/{classification_summary['total_fields']} fields retained")
            
            # Generate intelligent chart recommendations using filtered fields
            smart_recommendations = self._generate_intelligent_chart_recommendations(filtered_field_insights)
            
            # Create layout plan for 12x9 grid
            layout_plan = self._create_dashboard_layout_plan(smart_recommendations)
            
            # Generate chart configurations
            chart_configurations = self._generate_chart_configurations(smart_recommendations, filtered_field_insights)
            
            # Create the enhanced dashboard structure
            dashboard_structure = {
                "layer_name": layer_name,
                "analysis_timestamp": self._get_timestamp(),
               
                "dashboard_metadata": {
                    "grid_system": "12x9",
                    "total_charts": len(smart_recommendations),
                    "layout_strategy": "priority_based",
                    "version": "2.1",
                    "field_filtering": classification_summary
                },
                "field_insights": filtered_field_insights,  # Use filtered fields
                "chart_recommendations": smart_recommendations,
                "layout_plan": layout_plan,
                "chart_configurations": chart_configurations,
                "dashboard_themes": self._get_dashboard_themes()
            }
            
            # Save to enhanced dashboard file
            dashboard_file = os.path.join(os.getcwd(), "smart_dashboard.json")
            with open(dashboard_file, 'w', encoding='utf-8') as f:
                json.dump(dashboard_structure, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Smart dashboard layout saved to: {dashboard_file}")
            
            return {
                "success": True,
                "message": f"Smart dashboard layout generated successfully for layer '{layer_name}'",
                "charts_recommended": len(smart_recommendations),
                "layout_grid": "12x9",
                "dashboard_file": dashboard_file,
                "dashboard_structure": dashboard_structure
            }
            
        except Exception as e:
            logger.error(f"Error generating smart dashboard layout: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _generate_intelligent_chart_recommendations(self, field_insights: Dict) -> List[Dict]:
        """Generate intelligent chart recommendations based on field characteristics"""
        recommendations = []
        chart_id = 1
        
        # Categorize fields by type and characteristics
        categorical_fields = []
        numeric_fields = []
        binary_fields = []
        text_fields = []
        
        for field_name, field_info in field_insights.items():
            data_category = field_info.get("data_category", "unknown")
            unique_count = field_info.get("unique_count", 0)
            
            if data_category == "categorical_text" and unique_count <= 30:
                categorical_fields.append(field_info)
            elif data_category == "categorical_numeric" and unique_count <= 10:
                if unique_count == 2:
                    binary_fields.append(field_info)
                else:
                    categorical_fields.append(field_info)
            elif data_category in ["continuous_numeric", "categorical_numeric"]:
                numeric_fields.append(field_info)
            elif data_category == "free_text":
                text_fields.append(field_info)
        
        # 1. Single-field visualizations (high priority)
        for field in categorical_fields:
            if field["unique_count"] <= 20:  # Good for pie/donut charts
                recommendations.append({
                    "chart_id": chart_id,
                    "chart_type": "pie",
                    "priority": 1,
                    "title": f"Distribution of {field['field_name']}",
                    "primary_field": field['field_name'],
                    "description": f"Pie chart showing the distribution of {field['unique_count']} categories in {field['field_name']}",
                    "suitability_score": 0.9,
                    "data_insight": f"Categorical breakdown with {field['unique_count']} unique values",
                    "recommended_size": "medium"
                })
                chart_id += 1
                
                # Also recommend bar chart for same data
                recommendations.append({
                    "chart_id": chart_id,
                    "chart_type": "bar",
                    "priority": 2,
                    "title": f"Count by {field['field_name']}",
                    "primary_field": field['field_name'],
                    "description": f"Bar chart showing counts for {field['unique_count']} categories in {field['field_name']}",
                    "suitability_score": 0.85,
                    "data_insight": f"Frequency analysis of {field['field_name']} categories",
                    "recommended_size": "large"
                })
                chart_id += 1
        
        # 2. Numeric field distributions
        for field in numeric_fields:
            if field.get("data_category") == "continuous_numeric":
                recommendations.append({
                    "chart_id": chart_id,
                    "chart_type": "histogram",
                    "priority": 1,
                    "title": f"Distribution of {field['field_name']}",
                    "primary_field": field['field_name'],
                    "description": f"Histogram showing the distribution of {field['field_name']} values",
                    "suitability_score": 0.9,
                    "data_insight": f"Value distribution from {field.get('min_value', 'N/A')} to {field.get('max_value', 'N/A')}",
                    "recommended_size": "medium"
                })
                chart_id += 1
        
        # 3. Binary field analysis
        for field in binary_fields:
            recommendations.append({
                "chart_id": chart_id,
                "chart_type": "donut",
                "priority": 1,
                "title": f"{field['field_name']} Status",
                "primary_field": field['field_name'],
                "description": f"Donut chart showing binary distribution of {field['field_name']}",
                "suitability_score": 0.85,
                "data_insight": f"Binary indicator with {field.get('average_value', 0):.1%} positive rate",
                "recommended_size": "small"
            })
            chart_id += 1
        
        # 4. Cross-field relationships (medium priority)
        for i, field1 in enumerate(categorical_fields):
            for field2 in categorical_fields[i+1:]:
                if field1["unique_count"] <= 15 and field2["unique_count"] <= 15:
                    recommendations.append({
                        "chart_id": chart_id,
                        "chart_type": "heatmap",
                        "priority": 3,
                        "title": f"{field1['field_name']} vs {field2['field_name']}",
                        "primary_field": field1['field_name'],
                        "secondary_field": field2['field_name'],
                        "description": f"Heatmap showing relationship between {field1['field_name']} and {field2['field_name']}",
                        "suitability_score": 0.75,
                        "data_insight": "Cross-tabulation analysis",
                        "recommended_size": "large"
                    })
                    chart_id += 1
        
        # 5. Numeric correlations
        for i, field1 in enumerate(numeric_fields):
            for field2 in numeric_fields[i+1:]:
                recommendations.append({
                    "chart_id": chart_id,
                    "chart_type": "scatter",
                    "priority": 4,
                    "title": f"{field1['field_name']} vs {field2['field_name']}",
                    "x_field": field1['field_name'],
                    "y_field": field2['field_name'],
                    "description": f"Scatter plot comparing {field1['field_name']} and {field2['field_name']}",
                    "suitability_score": 0.7,
                    "data_insight": "Correlation analysis between numeric variables",
                    "recommended_size": "medium"
                })
                chart_id += 1
        
        # 6. Mixed-type relationships
        for cat_field in categorical_fields[:3]:  # Limit to top 3 categorical
            for num_field in numeric_fields[:2]:  # Limit to top 2 numeric
                recommendations.append({
                    "chart_id": chart_id,
                    "chart_type": "box_plot",
                    "priority": 3,
                    "title": f"{num_field['field_name']} by {cat_field['field_name']}",
                    "primary_field": num_field['field_name'],
                    "group_by_field": cat_field['field_name'],
                    "description": f"Box plot showing {num_field['field_name']} distribution across {cat_field['field_name']} categories",
                    "suitability_score": 0.8,
                    "data_insight": "Statistical distribution by category",
                    "recommended_size": "large"
                })
                chart_id += 1
        
        # Sort by priority and suitability score
        recommendations.sort(key=lambda x: (x["priority"], -x["suitability_score"]))
        
        # Return top 8 recommendations for optimal dashboard
        return recommendations[:8]
    
    def _create_dashboard_layout_plan(self, recommendations: List[Dict]) -> Dict:
        """Create a 12x9 grid layout plan for the dashboard"""
        layout_plan = {
            "grid_dimensions": {"width": 12, "height": 9},
            "chart_positions": [],
            "layout_strategy": "priority_and_size_optimized"
        }
        
        # Define size templates
        size_templates = {
            "small": {"width": 3, "height": 3},
            "medium": {"width": 4, "height": 3},
            "large": {"width": 6, "height": 3},
            "wide": {"width": 8, "height": 3},
            "tall": {"width": 4, "height": 4}
        }
        
        # Current position tracker
        current_x, current_y = 0, 0
        
        for rec in recommendations:
            size_template = size_templates.get(rec.get("recommended_size", "medium"))
            
            # Check if chart fits in current row
            if current_x + size_template["width"] > 12:
                current_x = 0
                current_y += 3  # Move to next row
            
            # Check if we have vertical space
            if current_y + size_template["height"] > 9:
                break  # Dashboard is full
            
            chart_position = {
                "chart_id": rec["chart_id"],
                "chart_type": rec["chart_type"],
                "title": rec["title"],
                "recommended_size": rec.get("recommended_size", "medium"),
                "grid_position": {
                    "x": current_x,
                    "y": current_y,
                    "width": size_template["width"],
                    "height": size_template["height"]
                },
                "priority": rec["priority"],
                "z_index": rec["priority"]
            }
            
            layout_plan["chart_positions"].append(chart_position)
            current_x += size_template["width"]
        
        return layout_plan
    
    def _generate_chart_configurations(self, recommendations: List[Dict], field_insights: Dict) -> Dict:
        """Generate detailed chart configurations for rendering"""
        configurations = {}
        
        color_palettes = {
            "categorical": ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7", "#DDA0DD", "#98D8C8"],
            "sequential": ["#FFF5F0", "#FEE0D2", "#FCBBA1", "#FC9272", "#FB6A4A", "#EF3B2C", "#CB181D"],
            "diverging": ["#d73027", "#f46d43", "#fdae61", "#fee08b", "#e6f598", "#abdda4", "#66c2a5"]
        }
        
        for rec in recommendations:
            chart_config = {
                "chart_id": rec["chart_id"],
                "chart_type": rec["chart_type"],
                "title": rec["title"],
                "data_source": {
                    "primary_field": rec.get("primary_field"),
                    "secondary_field": rec.get("secondary_field"),
                    "x_field": rec.get("x_field"),
                    "y_field": rec.get("y_field"),
                    "group_by_field": rec.get("group_by_field")
                },
                "styling": {
                    "color_palette": color_palettes["categorical"],
                    "theme": "modern",
                    "show_legend": True,
                    "show_grid": rec["chart_type"] in ["scatter", "line", "bar"],
                    "animation": True
                },
                "interactivity": {
                    "hover_enabled": True,
                    "click_enabled": True,
                    "zoom_enabled": rec["chart_type"] in ["scatter", "histogram"],
                    "filter_enabled": True
                }
            }
            
            # Chart-specific configurations
            if rec["chart_type"] in ["pie", "donut"]:
                chart_config["styling"]["show_percentages"] = True
                chart_config["styling"]["inner_radius"] = 40 if rec["chart_type"] == "donut" else 0
                
            elif rec["chart_type"] == "histogram":
                field_info = field_insights.get(rec.get("primary_field", ""), {})
                chart_config["histogram_config"] = {
                    "bins": min(20, max(10, int(field_info.get("unique_count", 20) / 10))),
                    "x_axis_title": rec.get("primary_field", "Value"),
                    "y_axis_title": "Frequency"
                }
                
            elif rec["chart_type"] == "bar":
                chart_config["bar_config"] = {
                    "orientation": "vertical",
                    "sort_by": "value",
                    "show_values": True
                }
                
            elif rec["chart_type"] == "scatter":
                chart_config["scatter_config"] = {
                    "point_size": 6,
                    "opacity": 0.7,
                    "trend_line": True
                }
                
            elif rec["chart_type"] == "heatmap":
                chart_config["heatmap_config"] = {
                    "color_scale": "viridis",
                    "show_values": True,
                    "normalize": True
                }
            
            configurations[f"chart_{rec['chart_id']}"] = chart_config
        
        return configurations
    
    def _get_dashboard_themes(self) -> Dict:
        """Get available dashboard themes"""
        return {
            "default": {
                "background_color": "#ffffff",
                "text_color": "#333333",
                "grid_color": "#e0e0e0",
                "accent_color": "#007acc"
            },
            "dark": {
                "background_color": "#1e1e1e",
                "text_color": "#ffffff",
                "grid_color": "#404040",
                "accent_color": "#00d4ff"
            },
            "professional": {
                "background_color": "#f8f9fa",
                "text_color": "#212529",
                "grid_color": "#dee2e6",
                "accent_color": "#0d6efd"
            }
        }
    
    def _get_timestamp(self) -> str:
        """Get current timestamp in ISO format"""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def optimize_dashboard_layout(self, layer_name: str, layout_template: str = "auto", 
                            target_size: str = "desktop") -> Dict:
        """
        Stage 3: Advanced Layout Planner with dynamic optimization and templates
        Optimizes existing dashboard layouts with smart positioning and templates
        """
        logger.info(f"Optimizing dashboard layout for layer: {layer_name}")
        
        try:
            # Load existing smart dashboard
            dashboard_file = os.path.join(os.getcwd(), "smart_dashboard.json")
            if not os.path.exists(dashboard_file):
                return {"success": False, "error": "No existing smart dashboard found. Run generate_smart_dashboard_layout first."}
            
            with open(dashboard_file, 'r', encoding='utf-8') as f:
                existing_dashboard = json.load(f)
            
            # Apply layout optimization
            optimized_layout = self._optimize_layout_with_template(
                existing_dashboard["layout_plan"], 
                existing_dashboard["chart_recommendations"],
                layout_template,
                target_size
            )
            
            # Generate responsive variations
            responsive_layouts = self._generate_responsive_layouts(optimized_layout)
            
            # Validate and resolve conflicts
            validated_layout = self._validate_and_resolve_layout_conflicts(optimized_layout)
            
            # Create optimized dashboard structure
            optimized_dashboard = {
                **existing_dashboard,
                "layout_optimization": {
                    "template_applied": layout_template,
                    "target_size": target_size,
                    "optimization_timestamp": self._get_timestamp(),
                    "version": "3.0"
                },
                "optimized_layout_plan": validated_layout,
                "responsive_layouts": responsive_layouts,
                "layout_analytics": self._analyze_layout_performance(validated_layout)
            }
            
            # Save optimized dashboard
            optimized_file = os.path.join(os.getcwd(), "optimized_dashboard.json")
            with open(optimized_file, 'w', encoding='utf-8') as f:
                json.dump(optimized_dashboard, f, indent=2, ensure_ascii=False)
            
            return {
                "success": True,
                "message": f"Dashboard layout optimized with template: {layout_template}",
                "template_applied": layout_template,
                "charts_repositioned": len(validated_layout["chart_positions"]),
                "optimization_file": optimized_file,
                "layout_score": optimized_dashboard["layout_analytics"]["overall_score"]
            }
            
        except Exception as e:
            logger.error(f"Error optimizing dashboard layout: {str(e)}")
            return {"success": False, "error": str(e)}

    def _optimize_layout_with_template(self, current_layout: Dict, recommendations: List[Dict], 
                                 template: str, target_size: str) -> Dict:
        """Apply layout template optimization"""
        
        layout_templates = {
            "focus": self._apply_focus_template,
            "comparison": self._apply_comparison_template, 
            "overview": self._apply_overview_template,
            "analytical": self._apply_analytical_template,
            "auto": self._apply_auto_template
        }
        
        template_func = layout_templates.get(template, self._apply_auto_template)
        return template_func(current_layout, recommendations, target_size)

    def _apply_focus_template(self, layout: Dict, recommendations: List[Dict], target_size: str) -> Dict:
        """Focus template: Emphasizes the most important chart"""
        optimized = deepcopy(layout)
        
        # Find highest priority chart
        top_chart = min(recommendations, key=lambda x: x["priority"])
        
        # Make it larger and central
        for pos in optimized["chart_positions"]:
            if pos["chart_id"] == top_chart["chart_id"]:
                pos["grid_position"].update({
                    "x": 2, "y": 0, "width": 8, "height": 5
                })
                pos["emphasis"] = "primary"
            else:
                # Arrange others in smaller sizes below
                idx = optimized["chart_positions"].index(pos) - 1
                pos["grid_position"].update({
                    "x": (idx % 4) * 3, "y": 5,
                    "width": 3, "height": 2
                })
                pos["emphasis"] = "secondary"
        
        optimized["template_type"] = "focus"
        return optimized

    def _apply_comparison_template(self, layout: Dict, recommendations: List[Dict], target_size: str) -> Dict:
        """Comparison template: Side-by-side comparisons of key metrics"""
        optimized = deepcopy(layout)
        
        # Select top 4 charts for comparison
        top_charts = sorted(recommendations, key=lambda x: x["priority"])[:4]
        
        # Arrange in 2x2 grid
        for idx, rec in enumerate(top_charts):
            pos = optimized["chart_positions"][idx]
            pos["grid_position"].update({
                "x": (idx % 2) * 6, "y": 0,
                "width": 6, "height": 4
            })
            pos["emphasis"] = "primary"
        
        # Add a summary chart below if space permits
        if len(top_charts) == 4:
            summary_chart = top_charts[0]  # Just an example, could be a dedicated summary chart
            pos = optimized["chart_positions"][4]
            pos["grid_position"].update({
                "x": 0, "y": 4,
                "width": 12, "height": 3
            })
            pos["emphasis"] = "secondary"
        
        optimized["template_type"] = "comparison"
        return optimized

    def _apply_overview_template(self, layout: Dict, recommendations: List[Dict], target_size: str) -> Dict:
        """Overview template: High-level overview with key metrics and trends"""
        optimized = deepcopy(layout)
        
        # Select key metrics (top 3 charts)
        key_metrics = sorted(recommendations, key=lambda x: x["priority"])[:3]
        
        # Arrange in a single row
        for idx, rec in enumerate(key_metrics):
            pos = optimized["chart_positions"][idx]
            pos["grid_position"].update({
                "x": idx * 4, "y": 0,
                "width": 4, "height": 3
            })
            pos["emphasis"] = "primary"
        
        # Add trend chart below (if available)
        if len(recommendations) > 3:
            trend_chart = recommendations[3]  # Assuming the 4th chart is a trend chart
            pos = optimized["chart_positions"][3]
            pos["grid_position"].update({
                "x": 0, "y": 3,
                "width": 12, "height": 3
            })
            pos["emphasis"] = "secondary"
        
        optimized["template_type"] = "overview"
        return optimized

    def _apply_analytical_template(self, layout: Dict, recommendations: List[Dict], target_size: str) -> Dict:
        """Analytical template: Detailed analysis with multiple charts"""
        optimized = deepcopy(layout)
        
        # Select top 6 charts for analysis
        analysis_charts = sorted(recommendations, key=lambda x: x["priority"])[:6]
        
        # Arrange in 3x2 grid
        for idx, rec in enumerate(analysis_charts):
            pos = optimized["chart_positions"][idx]
            pos["grid_position"].update({
                "x": (idx % 3) * 4, "y": (idx // 3) * 3,
                "width": 4, "height": 3
            })
            pos["emphasis"] = "primary"
        
        optimized["template_type"] = "analytical"
        return optimized

    def _apply_auto_template(self, layout: Dict, recommendations: List[Dict], target_size: str) -> Dict:
        """Auto template: Let CSS grid auto-placement handle positioning based on size classes"""
        optimized = deepcopy(layout)
        
        # For auto template, we primarily rely on CSS grid auto-placement
        # Just ensure charts have appropriate sizes based on priority
        for rec in recommendations:
            pos = optimized["chart_positions"][rec["chart_id"] - 1] # Assuming chart_id starts from 1
            
            # Assign sizes based on priority, but let CSS handle positioning
            if rec["priority"] == 1:
                # Highest priority gets large size
                pos["recommended_size"] = "large"
                pos["grid_position"].update({"width": 6, "height": 4})
            elif rec["priority"] == 2:
                # Second priority gets medium size
                pos["recommended_size"] = "medium"  
                pos["grid_position"].update({"width": 4, "height": 3})
            elif rec["priority"] == 3:
                # Third priority gets medium size
                pos["recommended_size"] = "medium"
                pos["grid_position"].update({"width": 4, "height": 3})
            else:
                # Lower priority gets small size
                pos["recommended_size"] = "small"
                pos["grid_position"].update({"width": 3, "height": 2})
            
            # Remove explicit x,y positioning for auto template to enable CSS auto-placement
            if "x" in pos["grid_position"]:
                del pos["grid_position"]["x"]
            if "y" in pos["grid_position"]:
                del pos["grid_position"]["y"]
        
        optimized["template_type"] = "auto"
        return optimized

    def _generate_responsive_layouts(self, layout: Dict) -> Dict:
        """Generate responsive layouts for different screen sizes"""
        responsive_layouts = {}
        
        # Break down the main layout into sections
        sections = {
            "header": layout["chart_positions"][:1],
            "main": layout["chart_positions"][1:],
            "footer": layout["chart_positions"][-1:]
        }
        
        # Define responsive behavior
        for size in ["mobile", "tablet", "desktop"]:
            responsive_layout = {
                "grid_dimensions": {"width": 12, "height": 9},
                "chart_positions": [],
                "layout_strategy": "responsive"
            }
            
            # Header: Full width on top
            if sections["header"]:
                header_pos = sections["header"][0]["grid_position"]
                responsive_layout["chart_positions"].append({
                    "chart_id": sections["header"][0]["chart_id"],
                    "chart_type": sections["header"][0]["chart_type"],
                    "title": sections["header"][0]["title"],
                    "grid_position": {
                        "x": 0,
                        "y": 0,
                        "width": 12,
                        "height": header_pos["height"]
                    },
                    "priority": sections["header"][0]["priority"],
                    "z_index": sections["header"][0]["priority"]
                })
            
            # Main: Responsive columns
            if sections["main"]:
                column_count = 2 if size in ["tablet", "desktop"] else 1
                for idx, pos in enumerate(sections["main"]):
                    x_pos = (idx % column_count) * 6
                    y_pos = (idx // column_count) * 3 + (1 if sections["header"] else 0)
                    
                    responsive_layout["chart_positions"].append({
                        "chart_id": pos["chart_id"],
                        "chart_type": pos["chart_type"],
                        "title": pos["title"],
                        "grid_position": {
                            "x": x_pos,
                            "y": y_pos,
                            "width": 6,
                            "height": 3
                        },
                        "priority": pos["priority"],
                        "z_index": pos["priority"]
                    })
            
            # Footer: Full width at the bottom
            if sections["footer"]:
                footer_pos = sections["footer"][0]["grid_position"]
                responsive_layout["chart_positions"].append({
                    "chart_id": sections["footer"][0]["chart_id"],
                    "chart_type": sections["footer"][0]["chart_type"],
                    "title": sections["footer"][0]["title"],
                    "grid_position": {
                        "x": 0,
                        "y": 9 - footer_pos["height"],
                        "width": 12,
                        "height": footer_pos["height"]
                    },
                    "priority": sections["footer"][0]["priority"],
                    "z_index": sections["footer"][0]["priority"]
                })
            
            responsive_layouts[size] = responsive_layout
        
        return responsive_layouts

    def _validate_and_resolve_layout_conflicts(self, layout: Dict) -> Dict:
        """Validate and resolve any conflicts in the layout"""
        validated = deepcopy(layout)
        
        # Check for overlapping positions
        positions = [pos["grid_position"] for pos in validated["chart_positions"]]
        unique_positions = [dict(t) for t in {tuple(p.items()) for p in positions}]
        
        if len(unique_positions) < len(positions):
            logger.warning("Overlapping chart positions detected, resolving...")
            # Simple resolution: Offset overlapping charts
            for pos in positions:
                if positions.count(pos) > 1:
                    idx = positions.index(pos)
                    pos["y"] += 1  # Move down
                    # Ensure it stays within bounds
                    if pos["y"] + pos["height"] > validated["grid_dimensions"]["height"]:
                        pos["y"] = validated["grid_dimensions"]["height"] - pos["height"]
        
        validated["chart_positions"] = [{
            **pos,
            "grid_position": {
                "x": pos["grid_position"]["x"],
                "y": pos["grid_position"]["y"],
                "width": pos["grid_position"]["width"],
                "height": pos["grid_position"]["height"]
            }
        } for pos in validated["chart_positions"]]
        
        return validated

    def _analyze_layout_performance(self, layout: Dict) -> Dict:
        """Analyze the layout for performance insights"""
        total_charts = len(layout["chart_positions"])
        filled_positions = sum(1 for pos in layout["chart_positions"] if pos["grid_position"]["y"] >= 0)
        
        return {
            "success": True,
            "total_charts": total_charts,
            "filled_positions": filled_positions,
            "empty_positions": total_charts - filled_positions,
            "overall_score": round((filled_positions / total_charts) * 100, 2) if total_charts > 0 else 0
        }

    def recommend_chart_types(self, layer_name: str, target_field: str = None) -> Dict:
        """
        Enhanced AI-Powered Chart Type Recommendation (Step 3)
        Analyzes both single-field characteristics and multi-field relationships 
        to recommend diverse chart types, addressing the "too many histograms" problem.
        Uses token-efficient prompts and leverages existing retry mechanisms.
        """
        logger.info(f"Enhanced AI-powered chart type recommendation for layer: {layer_name}")
        
        try:
            # Get enhanced field analysis with AI insights
            field_analysis_result = self.analyze_layer_fields(layer_name)
            if not field_analysis_result.get("success", True):
                return field_analysis_result
            
            field_insights = field_analysis_result["field_insights"]
            
            # Filter relevant fields for visualization
            filter_result = self._filter_relevant_fields(field_insights)
            relevant_fields = filter_result["filtered_insights"]
            
            if not relevant_fields:
                return {
                    "success": False, 
                    "error": "No relevant fields found for chart recommendations"
                }
            
            # NEW: Analyze field relationships for multi-field charts
            field_relationships = self._analyze_field_relationships(relevant_fields)
            
            # NEW: Create token-efficient field summaries
            field_summaries = self._create_field_summaries(relevant_fields)
            
            # Build enhanced AI prompt with relationships and token optimization
            ai_prompt = self._build_enhanced_chart_recommendation_prompt(
                field_summaries, field_relationships, target_field
            )
            
            # Store enhanced context for AI response handling
            recommendation_context = {
                "function_type": "enhanced_chart_recommendation",
                "layer_name": layer_name,
                "target_field": target_field,
                "field_count": len(relevant_fields),
                "relationship_count": len(field_relationships),
                "field_summaries": field_summaries,
                "field_relationships": field_relationships,
                "timestamp": self._get_timestamp()
            }
            
            # Return structured data for AI processing with retry mechanisms
            result = {
                "success": True,
                "message": "Enhanced chart recommendation analysis ready for AI processing",
                "layer_name": layer_name,
                "relevant_fields_count": len(relevant_fields),
                "relationship_count": len(field_relationships),
                "ai_prompt": ai_prompt,
                "context": recommendation_context,
                "field_summaries": field_summaries,
                "field_relationships": field_relationships,
                "requires_ai_processing": True,  # Flag for main.py to handle with AI
                "analysis_timestamp": self._get_timestamp(),
                "enhancement_features": [
                    "multi_field_relationships",
                    "token_optimization", 
                    "chart_diversity_focus"
                ]
            }
            
            # Save enhanced analysis for AI processing
            temp_file = os.path.join(os.getcwd(), f"enhanced_chart_analysis_{layer_name}.json")
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Enhanced chart recommendation analysis saved: {temp_file}")
            logger.info(f"Analysis includes {len(field_relationships)} field relationships for diverse charts")
            return result
            
        except Exception as e:
            logger.error(f"Error in enhanced recommend_chart_types: {str(e)}")
            return {"success": False, "error": str(e)}

    def plan_dashboard_layout(self, layer_name: str, chart_recommendations: List[Dict] = None) -> Dict:
        """
        AI-Powered Dashboard Layout Planning (Step 5)
        Uses AI to create optimal dashboard layouts that maximize space utilization.
        Works with existing retry mechanisms for reliable AI interactions.
        """
        logger.info(f"AI-powered dashboard layout planning for layer: {layer_name}")
        
        try:
            # Get chart recommendations if not provided
            if not chart_recommendations:
                chart_rec_result = self.recommend_chart_types(layer_name)
                if not chart_rec_result.get("success", True):
                    return chart_rec_result
                chart_recommendations = chart_rec_result.get("chart_recommendations", [])
            
            # If still no recommendations, try to load from existing files
            if not chart_recommendations:
                dashboard_files = [
                    os.path.join(os.getcwd(), "smart_dashboard.json"),
                    os.path.join(os.getcwd(), "dashboard.json")
                ]
                
                for file_path in dashboard_files:
                    if os.path.exists(file_path):
                        with open(file_path, 'r', encoding='utf-8') as f:
                            dashboard_data = json.load(f)
                        chart_recommendations = dashboard_data.get("chart_recommendations", [])
                        if chart_recommendations:
                            break
            
            if not chart_recommendations:
                return {
                    "success": False, 
                    "error": "No chart recommendations available for layout planning"
                }
            
            # Build AI prompt for layout optimization
            layout_prompt = self._build_layout_planning_prompt(chart_recommendations, layer_name)
            
            # Prepare layout context for AI processing
            layout_context = {
                "function_type": "layout_planning",
                "layer_name": layer_name,
                "chart_count": len(chart_recommendations),
                "grid_system": "12x9",
                "chart_recommendations": chart_recommendations,
                "timestamp": self._get_timestamp()
            }
            
            # Return structured data for AI processing with retry mechanisms
            result = {
                "success": True,
                "message": "Dashboard layout analysis ready for AI processing",
                "layer_name": layer_name,
                "chart_count": len(chart_recommendations),
                "ai_prompt": layout_prompt,
                "context": layout_context,
                "chart_recommendations": chart_recommendations,
                "requires_ai_processing": True,  # Flag for main.py to handle with AI
                "analysis_timestamp": self._get_timestamp()
            }
            
            # Save layout planning data
            temp_file = os.path.join(os.getcwd(), f"layout_analysis_{layer_name}.json")
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Layout planning analysis saved for AI processing: {temp_file}")
            return result
            
        except Exception as e:
            logger.error(f"Error in plan_dashboard_layout: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _build_chart_recommendation_prompt(self, field_insights: Dict, target_field: str = None) -> str:
        """Legacy chart recommendation prompt - deprecated in favor of enhanced version"""
        logger.warning("Using legacy chart recommendation prompt. Consider using enhanced version.")
        return self._build_enhanced_chart_recommendation_prompt(
            self._create_field_summaries(field_insights), 
            [], 
            target_field
        )
    
    def _build_layout_planning_prompt(self, chart_recommendations: List[Dict], layer_name: str) -> str:
        """Build comprehensive AI prompt for dashboard layout planning"""
        try:
            prompt = f"""# Dashboard Layout Planning Analysis

## Objective
Create an optimal 12x9 grid layout for {len(chart_recommendations)} charts that maximizes space utilization and visual effectiveness.

## Dashboard Specifications
- **Grid System**: 12 columns x 9 rows
- **Layer**: {layer_name}
- **Chart Count**: {len(chart_recommendations)}

## Chart Requirements:
"""
            
            for i, chart in enumerate(chart_recommendations, 1):
                prompt += f"""
### Chart {i}: {chart.get('title', f'Chart {i}')}
- **Type**: {chart.get('chart_type', 'unknown')}
- **Priority**: {chart.get('priority', 5)}/10
- **Recommended Size**: {chart.get('size_recommendation', chart.get('recommended_size', 'medium'))}
- **Effectiveness**: {chart.get('effectiveness_score', chart.get('suitability_score', 0.5))}
- **Field**: {chart.get('field_name', chart.get('primary_field', 'unknown'))}
"""
            
            prompt += """
## Layout Optimization Guidelines
1. **Priority Placement**: High-priority charts get prominent positions (top-left area)
2. **Size Efficiency**: Balance chart sizes to fill the 12x9 grid optimally
3. **Visual Hierarchy**: Create clear reading flow (left-to-right, top-to-bottom)
4. **Space Utilization**: Minimize empty grid cells
5. **Chart Relationships**: Place related charts near each other

## Size Templates Available
- **small**: 3x3 (9 grid cells)
- **medium**: 4x3 (12 grid cells)  
- **large**: 6x3 (18 grid cells)
- **wide**: 8x3 (24 grid cells)
- **tall**: 4x4 (16 grid cells)

## Required Output Format
Provide layout recommendations as JSON:
```json
{
  "layout_strategy": "description of approach",
  "grid_utilization": "percentage of cells used",
  "chart_positions": [
    {
      "chart_id": 1,
      "title": "Chart Title",
      "position": {
        "x": 0,
        "y": 0,
        "width": 4,
        "height": 3
      },
      "size_template": "medium",
      "justification": "why placed here"
    }
  ],
  "optimization_notes": "key decisions made"
}
```

**Important**: Ensure no chart positions overlap and all positions fit within the 12x9 grid.
"""
            
            return prompt
            
        except Exception as e:
            logger.error(f"Error building layout planning prompt: {str(e)}")
            return "Error building prompt"

    def _classify_field_importance(self, field_name: str, field_info: Dict) -> Dict:
        """
        Classify fields by their analytical importance and filter out irrelevant ones.
        Returns classification with importance score (0-100).
        """
        field_name_lower = field_name.lower()
        field_type = field_info.get('field_type', '').lower()
        unique_count = field_info.get('unique_count', 0)
        total_records = field_info.get('total_records', 1)
        null_percentage = field_info.get('null_percentage', 0)
        
        # Calculate uniqueness ratio
        uniqueness_ratio = unique_count / total_records if total_records > 0 else 0
        
        # Initialize classification
        classification = {
            'field_name': field_name,
            'category': 'unknown',
            'importance_score': 0,
            'is_relevant': False,
            'filter_reason': None,
            'analytical_value': 'none'
        }
        
        # Technical/System fields (EXCLUDE)
        technical_patterns = [
            'objectid', 'oid', 'fid', 'globalid', 'created_user', 'created_date',
            'last_edited_user', 'last_edited_date', 'shape_length', 'shape_area',
            'shape_leng', 'shape.stlength', 'shape.starea'
        ]
        
        if any(pattern in field_name_lower for pattern in technical_patterns):
            classification.update({
                'category': 'technical',
                'importance_score': 0,
                'is_relevant': False,
                'filter_reason': 'Technical/system field',
                'analytical_value': 'none'
            })
            return classification
        
        # ID fields with high uniqueness (EXCLUDE if purely sequential)
        id_patterns = ['id', '_id', 'code', '_code', 'key', '_key']
        if any(pattern in field_name_lower for pattern in id_patterns):
            if uniqueness_ratio > 0.9:  # Mostly unique values
                classification.update({
                    'category': 'identifier',
                    'importance_score': 10,
                    'is_relevant': False,
                    'filter_reason': 'Identifier field with high uniqueness',
                    'analytical_value': 'low'
                })
                return classification
        
        # Fields with very low variance (EXCLUDE)
        if unique_count <= 1:
            classification.update({
                'category': 'constant',
                'importance_score': 0,
                'is_relevant': False,
                'filter_reason': 'Constant or near-constant values',
                'analytical_value': 'none'
            })
            return classification
        
        # Fields with too many nulls (EXCLUDE)
        if null_percentage > 70:
            classification.update({
                'category': 'sparse',
                'importance_score': 5,
                'is_relevant': False,
                'filter_reason': f'Too many null values ({null_percentage:.1f}%)',
                'analytical_value': 'low'
            })
            return classification
        
        # Now classify RELEVANT fields based on DATA CHARACTERISTICS (language-agnostic)
        
        # Calculate data-driven scores based on statistical characteristics
        base_score = 50
        analytical_value = 'medium'
        category = 'general'
        
        # 1. Uniqueness-based scoring (language-agnostic)
        if 0.05 <= uniqueness_ratio <= 0.3:  # Good categorical distribution (5-30% unique)
            base_score += 25
            category = 'categorical'
            analytical_value = 'high'
        elif 0.3 < uniqueness_ratio <= 0.8:  # Moderate distribution
            base_score += 15
            category = 'mixed'
            analytical_value = 'medium'
        elif uniqueness_ratio > 0.95:  # Too unique (likely ID or text)
            base_score -= 20
            analytical_value = 'low'
        
        # 2. Data type scoring (language-agnostic)
        if field_type in ['integer', 'double', 'float', 'single']:
            base_score += 20  # Numeric fields are generally more analytical
            if category == 'general':
                category = 'numeric'
        elif field_type in ['string', 'text']:
            if unique_count < total_records * 0.2:  # Limited unique values = categorical
                base_score += 15
                category = 'categorical_text'
            else:
                base_score -= 10  # Free text is less analytical
                category = 'free_text'
        elif field_type == 'date':
            base_score += 10
            category = 'temporal'
            analytical_value = 'medium'
        
        # 3. Data completeness scoring (language-agnostic)
        if null_percentage < 5:
            base_score += 10  # Complete data is better
        elif null_percentage > 50:
            base_score -= 15  # Incomplete data is worse
        
        # 4. Value range scoring for numeric fields (language-agnostic)
        if field_type in ['integer', 'double', 'float', 'single']:
            min_val = field_info.get('min_value', 0)
            max_val = field_info.get('max_value', 0)
            
            # Check for meaningful numeric ranges
            if max_val > min_val:
                value_range = max_val - min_val
                if value_range > 0:
                    base_score += 5  # Has meaningful range
                    
                # Bonus for positive counts/measurements
                if min_val >= 0 and max_val > 10:
                    base_score += 5  # Likely count or measurement
        
        # 5. Sample value analysis (language-agnostic pattern detection)
        sample_values = field_info.get('sample_values', [])
        if sample_values:
            # Check for numeric patterns
            numeric_samples = [v for v in sample_values if isinstance(v, (int, float))]
            if len(numeric_samples) > 0:
                base_score += 5
                
            # Check for reasonable categorical size
            if 2 <= len(sample_values) <= 20:
                base_score += 10  # Good categorical size
        
        # Final classification
        final_score = max(0, min(100, base_score))
        is_relevant = final_score >= 40  # Threshold for relevance
        
        if final_score >= 70:
            analytical_value = 'high'
        elif final_score >= 50:
            analytical_value = 'medium'
        else:
            analytical_value = 'low'
        
        classification.update({
            'category': category,
            'importance_score': final_score,
            'is_relevant': is_relevant,
            'analytical_value': analytical_value
        })
        
        return classification

    def _analyze_field_relationships(self, relevant_fields: Dict) -> List[Dict]:
        """
        Analyze relationships between fields to identify opportunities for multi-field charts.
        Returns a list of field relationship patterns suitable for diverse chart types.
        """
        relationships = []
        field_names = list(relevant_fields.keys())
        
        try:
            for i, field1 in enumerate(field_names):
                field1_data = relevant_fields[field1]
                field1_category = field1_data.get('data_category', 'unknown')
                field1_uniqueness = field1_data.get('unique_count', 0) / field1_data.get('total_records', 1)
                
                for field2 in field_names[i+1:]:
                    field2_data = relevant_fields[field2]
                    field2_category = field2_data.get('data_category', 'unknown')
                    field2_uniqueness = field2_data.get('unique_count', 0) / field2_data.get('total_records', 1)
                    
                    # Detect relationship patterns for different chart types
                    relationship = self._detect_field_relationship_pattern(
                        field1, field1_data, field1_category, field1_uniqueness,
                        field2, field2_data, field2_category, field2_uniqueness
                    )
                    
                    if relationship:
                        relationships.append(relationship)
            
            logger.info(f"Detected {len(relationships)} field relationships for multi-field charts")
            return relationships
            
        except Exception as e:
            logger.error(f"Error analyzing field relationships: {str(e)}")
            return []
    
    def _detect_field_relationship_pattern(self, field1, field1_data, field1_cat, field1_uniq, 
                                         field2, field2_data, field2_cat, field2_uniq) -> Dict:
        """
        Detect specific relationship patterns between two fields that suggest optimal chart types.
        """
        try:
            # Pattern 1: Numeric vs Categorical (ideal for grouped bar/column charts)
            if ((field1_cat in ['continuous_numeric', 'categorical_numeric'] and 
                 field2_cat in ['categorical_numeric'] and field2_uniq < 0.3) or
                (field2_cat in ['continuous_numeric', 'categorical_numeric'] and 
                 field1_cat in ['categorical_numeric'] and field1_uniq < 0.3)):
                
                numeric_field = field1 if field1_cat in ['continuous_numeric', 'categorical_numeric'] else field2
                category_field = field2 if numeric_field == field1 else field1
                
                return {
                    "relationship_type": "numeric_vs_categorical",
                    "primary_field": numeric_field,
                    "secondary_field": category_field,
                    "recommended_charts": ["grouped_bar", "grouped_column", "box_plot"],
                    "chart_suitability": {
                        "grouped_bar": 0.85,
                        "grouped_column": 0.80,
                        "box_plot": 0.75
                    },
                    "relationship_strength": 0.8,
                    "description": f"Compare {numeric_field} distribution across {category_field} categories"
                }
            
            # Pattern 2: Two continuous numeric fields (ideal for scatter plots)
            if (field1_cat == 'continuous_numeric' and field2_cat == 'continuous_numeric' and
                field1_uniq > 0.3 and field2_uniq > 0.3):
                
                return {
                    "relationship_type": "numeric_correlation",
                    "primary_field": field1,
                    "secondary_field": field2,
                    "recommended_charts": ["scatter", "line_chart", "bubble"],
                    "chart_suitability": {
                        "scatter": 0.90,
                        "line_chart": 0.70,
                        "bubble": 0.65
                    },
                    "relationship_strength": 0.85,
                    "description": f"Explore correlation between {field1} and {field2}"
                }
            
            # Pattern 3: Two categorical fields (ideal for heatmap/cross-tabulation)
            if (field1_cat in ['categorical_numeric', 'categorical'] and 
                field2_cat in ['categorical_numeric', 'categorical'] and
                field1_uniq < 0.4 and field2_uniq < 0.4):
                
                return {
                    "relationship_type": "categorical_cross_analysis",
                    "primary_field": field1,
                    "secondary_field": field2,
                    "recommended_charts": ["heatmap", "stacked_bar", "cross_table"],
                    "chart_suitability": {
                        "heatmap": 0.80,
                        "stacked_bar": 0.75,
                        "cross_table": 0.70
                    },
                    "relationship_strength": 0.75,
                    "description": f"Cross-analysis of {field1} vs {field2} categories"
                }
            
            # Pattern 4: Multiple numeric fields suitable for multi-series comparison
            if (field1_cat in ['continuous_numeric', 'categorical_numeric'] and 
                field2_cat in ['continuous_numeric', 'categorical_numeric']):
                
                return {
                    "relationship_type": "multi_series_comparison",
                    "primary_field": field1,
                    "secondary_field": field2,
                    "recommended_charts": ["dual_axis", "combo_chart", "parallel_coordinates"],
                    "chart_suitability": {
                        "dual_axis": 0.70,
                        "combo_chart": 0.65,
                        "parallel_coordinates": 0.60
                    },
                    "relationship_strength": 0.65,
                    "description": f"Multi-series comparison of {field1} and {field2}"
                }
            
            return None
            
        except Exception as e:
            logger.error(f"Error detecting relationship pattern between {field1} and {field2}: {str(e)}")
            return None
    
    def _create_field_summaries(self, relevant_fields: Dict) -> Dict:
        """
        Create token-efficient field summaries for AI processing.
        Condenses field insights while preserving key characteristics.
        """
        summaries = {}
        
        try:
            for field_name, field_data in relevant_fields.items():
                # Extract key insights efficiently
                ai_insights = field_data.get('ai_insights', {})
                
                summary = {
                    "name": field_name,
                    "type": field_data.get('data_category', 'unknown'),
                    "uniqueness": round(field_data.get('unique_count', 0) / field_data.get('total_records', 1), 2),
                    "completeness": round(100 - field_data.get('null_percentage', 0), 1),
                    "viz_potential": ai_insights.get('visualization_potential', 'unknown'),
                    "analytical_value": ai_insights.get('analytical_value', 'unknown'),
                    "priority": ai_insights.get('visualization_priority', 5),
                    "story": ai_insights.get('data_story', '')[:100] + "..." if len(ai_insights.get('data_story', '')) > 100 else ai_insights.get('data_story', ''),
                    "top_charts": list(ai_insights.get('chart_suitability', {}).keys())[:3]  # Top 3 chart types
                }
                
                # Add specific characteristics based on data type
                if field_data.get('data_category') in ['continuous_numeric', 'categorical_numeric']:
                    summary.update({
                        "range": f"{field_data.get('min_value', 0):.1f}-{field_data.get('max_value', 0):.1f}",
                        "distribution": ai_insights.get('distribution_characteristics', 'unknown')[:50]
                    })
                elif field_data.get('data_category') in ['categorical', 'categorical_text']:
                    summary.update({
                        "categories": field_data.get('unique_count', 0),
                        "sample_values": field_data.get('sample_values', [])[:3]
                    })
                
                summaries[field_name] = summary
            
            logger.info(f"Created token-efficient summaries for {len(summaries)} fields")
            return summaries
            
        except Exception as e:
            logger.error(f"Error creating field summaries: {str(e)}")
            return {}
    
    def _build_enhanced_chart_recommendation_prompt(self, field_summaries: Dict, 
                                                  field_relationships: List[Dict], 
                                                  target_field: str = None) -> str:
        """
        Build token-efficient AI prompt focusing on chart diversity and field relationships.
        """
        try:
            prompt = f"""# Enhanced Chart Recommendation Analysis

## Mission: Diversify Dashboard Charts
**Primary Goal**: Recommend 5-8 diverse chart types that avoid the "too many histograms" problem.
**Data Fields**: {len(field_summaries)} relevant fields
**Field Relationships**: {len(field_relationships)} multi-field opportunities identified

## Token-Optimized Field Summaries:
"""
            
            # Add condensed field information
            for field_name, summary in field_summaries.items():
                prompt += f"• **{field_name}** ({summary['type']}): {summary['viz_potential']} potential, "
                prompt += f"Priority={summary['priority']}, Top charts: {', '.join(summary['top_charts'][:2])}\n"
            
            prompt += f"\n## Multi-Field Chart Opportunities ({len(field_relationships)} detected):\n"
            
            # Add relationship-based chart suggestions
            for i, rel in enumerate(field_relationships[:4], 1):  # Limit to top 4 relationships
                prompt += f"{i}. **{rel['relationship_type']}**: {rel['primary_field']} × {rel['secondary_field']} "
                prompt += f"→ {', '.join(rel['recommended_charts'][:2])}\n"
            
            prompt += """
## Chart Diversity Strategy:
1. **Single-Field Charts** (40%): Best fields get histogram/bar/pie
2. **Multi-Field Charts** (60%): Use relationships for scatter/grouped/heatmap
3. **Avoid Redundancy**: Maximum 2 histograms, 1 pie chart
4. **Prioritize Impact**: High-potential fields get prominent chart types

## Required JSON Output:
```json
[
  {
    "chart_id": 1,
    "chart_type": "scatter|grouped_bar|heatmap|box_plot|pie|histogram|line",
    "primary_field": "field_name",
    "secondary_field": "optional_for_multi_field_charts", 
    "title": "Concise descriptive title",
    "reasoning": "Why this chart type (max 50 chars)",
    "diversity_impact": "high|medium|low",
    "priority": 1-10,
    "size": "small|medium|large"
  }
]
```

**CRITICAL**: Recommend exactly 5-8 charts with maximum diversity. Avoid chart type repetition.
"""
            
            if target_field:
                prompt += f"\n**FOCUS**: Ensure {target_field} gets a prominent, suitable chart.\n"
            
            return prompt
            
        except Exception as e:
            logger.error(f"Error building enhanced chart recommendation prompt: {str(e)}")
            return "Error building enhanced prompt"

    def _filter_relevant_fields(self, field_insights: Dict) -> Dict:
        """
        Filter field insights to include only analytically relevant fields.
        Returns filtered insights with classification metadata.
        """
        filtered_insights = {}
        classification_summary = {
            'total_fields': len(field_insights),
            'relevant_fields': 0,
            'filtered_out': 0,
            'categories': {},
            'filter_reasons': {}
        }
        
        for field_name, field_info in field_insights.items():
            classification = self._classify_field_importance(field_name, field_info)
            
            # Track statistics
            category = classification['category']
            if category not in classification_summary['categories']:
                classification_summary['categories'][category] = 0
            classification_summary['categories'][category] += 1
            
            if classification['is_relevant']:
                # Add the field with its classification
                filtered_insights[field_name] = {
                    **field_info,
                    'classification': classification
                }
                classification_summary['relevant_fields'] += 1
            else:
                # Track why it was filtered out
                reason = classification.get('filter_reason', 'Low analytical value')
                if reason not in classification_summary['filter_reasons']:
                    classification_summary['filter_reasons'][reason] = 0
                classification_summary['filter_reasons'][reason] += 1
                classification_summary['filtered_out'] += 1
        
        logger.info(f"Field filtering results: {classification_summary['relevant_fields']}/{classification_summary['total_fields']} fields retained")
        
        return {
            'filtered_insights': filtered_insights,
            'classification_summary': classification_summary
        }
