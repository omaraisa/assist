import arcpy
import os
import json
import math
import statistics
import re
import traceback
import random
from datetime import datetime
from typing import Dict, Tuple, List
from copy import deepcopy

class RunPythonCode(object):
    def __init__(self):
        self.label = "RunPythonCode"
        self.description = "Test access to ArcGIS Pro's CURRENT project."
        self.canRunInBackground = False

    def getParameterInfo(self):
        function_name = arcpy.Parameter(
            displayName="Function Name",
            name="function_name",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        parameters_json = arcpy.Parameter(
            displayName="Parameters JSON",
            name="parameters_json",
            datatype="GPString",
            parameterType="Optional",
            direction="Input"
        )
        return [function_name, parameters_json]

    def execute(self, parameters, messages):
        try:
            function_name = parameters[0].valueAsText
            parameters_json = parameters[1].valueAsText
            messages.addMessage(f"Function name: {function_name}")
            messages.addMessage(f"Parameters JSON: {parameters_json}")

            if not function_name:
                messages.addMessage("No function name provided.")
                return

            params = json.loads(parameters_json) if parameters_json else {}
            messages.addMessage(f"Parsed params: {params}")

            result = self.execute_spatial_function(function_name, params, messages)

            if result:
                messages.addMessage(json.dumps({"status": "success", "data": result}))
            else:
                messages.addMessage(json.dumps({"status": "error", "message": f"Function {function_name} not implemented or failed"}))
        except Exception as e:
            import traceback
            tb = traceback.format_exc()
            messages.addMessage(f"Top-level error: {str(e)}")
            messages.addMessage(f"Traceback: {tb}")
            messages.addMessage(json.dumps({"status": "error", "message": str(e), "trace": tb}))

    def execute_spatial_function(self, function_name, params, messages):
        try:
            func = getattr(self, function_name, None)
            if func:
                return func(params)
            else:
                messages.addMessage(f"Function {function_name} not found.")
                return None
        except Exception as e:
            messages.addMessage(f"Error in {function_name}: {str(e)}")
            return None

    def _add_to_map(self, path):
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            map_obj.addDataFromPath(path)
        except Exception as e:
            # Log error but don't fail the function
            print(f"Could not add {path} to map: {e}")

    # Vector Functions
    def create_buffer(self, params):
        layer_name = params.get("layer_name")
        distance = params.get("distance")
        units = params.get("units", "meters")
        output_name = f"{layer_name.replace(' ', '_')}_Buffer_{int(distance)}{units}"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        output_fc = os.path.join(aprx.defaultGeodatabase, output_name)
        output_fc = arcpy.CreateUniqueName(output_fc)
        unit_mapping = {"meters": "METERS", "kilometers": "KILOMETERS", "feet": "FEET", "miles": "MILES"}
        arcpy_units = unit_mapping.get(units.lower(), "METERS")
        arcpy.analysis.Buffer(r"{}".format(layer_name), output_fc, f"{distance} {arcpy_units}")
        self._add_to_map(output_fc)
        return {"success": True, "output_layer": output_name, "output_path": output_fc}

    def invert_selection(self, params):
        """Invert the current selection on a layer.

        params: { "layer_name": <layer name or layer object> }
        Returns: {"success": True, "selected_features": <count>} or error
        """
        layer_name = params.get("layer_name")
        try:
            # Use ArcPy to switch/invert the selection on the provided layer
            # If the layer is a layer object or name, SelectLayerByAttribute_management accepts it.
            arcpy.SelectLayerByAttribute_management(r"{}".format(layer_name), "SWITCH_SELECTION")
            selected_count = int(arcpy.GetCount_management(r"{}".format(layer_name))[0])
            return {"success": True, "selected_features": selected_count}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def select_by_attribute(self, params):
        layer_name = params.get("layer_name")
        where_clause = params.get("where_clause")
        selection_type = params.get("selection_type", "NEW_SELECTION")
        arcpy.SelectLayerByAttribute_management(r"{}".format(layer_name), selection_type, where_clause)
        selected_count = int(arcpy.GetCount_management(r"{}".format(layer_name))[0])
        return {"success": True, "selected_features": selected_count}

    def select_by_location(self, params):
        input_layer = params.get("input_layer")
        select_layer = params.get("select_layer")
        relationship = params.get("relationship", "INTERSECT")
        arcpy.SelectLayerByLocation_management(r"{}".format(input_layer), relationship, r"{}".format(select_layer))
        selected_count = int(arcpy.GetCount_management(r"{}".format(input_layer))[0])
        return {"success": True, "selected_features": selected_count}

    def get_layer_summary(self, params):
        layer_name = params.get("layer_name")
        desc = arcpy.Describe(r"{}".format(layer_name))
        feature_count = int(arcpy.GetCount_management(r"{}".format(layer_name))[0])
        field_names = [f.name for f in arcpy.ListFields(r"{}".format(layer_name))]
        return {
            "success": True,
            "summary": {
                "geometry_type": desc.shapeType if hasattr(desc, 'shapeType') else "Table",
                "feature_count": feature_count,
                "fields": field_names,
                "data_source": desc.catalogPath,
                "spatial_reference": desc.spatialReference.name if hasattr(desc, 'spatialReference') else None
            }
        }
    
    def calculate_area(self, params):
        layer_name = params.get("layer_name")
        units = params.get("units", "square_meters")
        areas = []
        for row in arcpy.da.SearchCursor(r"{}".format(layer_name), ["SHAPE@AREA"]):
            if row[0] is not None:
                area = row[0]
                if units == "square_kilometers": area /= 1000000
                elif units == "acres": area *= 0.000247105
                elif units == "hectares": area *= 0.0001
                areas.append(area)
        return {"success": True, "total_area": sum(areas), "average_area": statistics.mean(areas)}

    def calculate_length(self, params):
        layer_name = params.get("layer_name")
        units = params.get("units", "meters")
        lengths = []
        for row in arcpy.da.SearchCursor(r"{}".format(layer_name), ["SHAPE@LENGTH"]):
            if row[0] is not None:
                length = row[0]
                if units == "kilometers": length /= 1000
                elif units == "feet": length *= 3.28084
                elif units == "miles": length /= 1609.34
                lengths.append(length)
        return {"success": True, "total_length": sum(lengths), "average_length": statistics.mean(lengths)}

    def get_centroid(self, params):
        layer_name = params.get("layer_name")
        centroids = []
        for row in arcpy.da.SearchCursor(r"{}".format(layer_name), ["OID@", "SHAPE@"]):
            if row[1]:
                centroid = row[1].centroid
                centroids.append({"id": row[0], "x": centroid.X, "y": centroid.Y})
        return {"success": True, "centroids": centroids}

    def spatial_join(self, params):
        """
        Perform a spatial join between two layers.
        Supports different join operations and provides detailed error messages.
        """
        try:
            target_layer = params.get("target_layer")
            join_layer = params.get("join_layer")
            join_operation = params.get("join_operation", "INTERSECT")  # Default to INTERSECT
            output_name_param = params.get("output_name")
            match_option = params.get("match_option", "CLOSEST")  # Default match option

            # Validate required parameters
            if not target_layer:
                return {"success": False, "error": "target_layer parameter is required"}
            if not join_layer:
                return {"success": False, "error": "join_layer parameter is required"}

            # Validate that layers exist and are accessible
            try:
                target_desc = arcpy.Describe(target_layer)
                join_desc = arcpy.Describe(join_layer)
            except Exception as e:
                return {"success": False, "error": f"Cannot access layers: {str(e)}. Please ensure both '{target_layer}' and '{join_layer}' exist and are loaded in the current ArcGIS Pro project."}

            # Generate output name
            if output_name_param:
                output_name = output_name_param
            else:
                output_name = f"{target_layer.replace(' ', '_')}_{join_layer.replace(' ', '_')}_joined"

            # Get current project and default geodatabase
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Map join_operation to ArcGIS spatial relationship
            operation_mapping = {
                "intersects": "INTERSECT",
                "contains": "CONTAINS",
                "within": "WITHIN",
                "touches": "TOUCHES",
                "overlaps": "OVERLAP",
                "crosses": "CROSSES",
                "closest": "CLOSEST"
            }

            spatial_relationship = operation_mapping.get(join_operation.lower(), "INTERSECT")

            # Perform the spatial join with proper parameters
            try:
                if spatial_relationship == "CLOSEST":
                    # For closest operation, we need additional parameters
                    arcpy.analysis.SpatialJoin(
                        target_features=r"{}".format(target_layer),
                        join_features=r"{}".format(join_layer),
                        out_feature_class=output_path,
                        join_operation="JOIN_ONE_TO_ONE",
                        join_type="KEEP_ALL",
                        match_option=spatial_relationship,
                        search_radius=None,
                        distance_field_name="DISTANCE"
                    )
                else:
                    # Standard spatial join for other operations
                    arcpy.analysis.SpatialJoin(
                        target_features=r"{}".format(target_layer),
                        join_features=r"{}".format(join_layer),
                        out_feature_class=output_path,
                        join_operation="JOIN_ONE_TO_ONE",
                        join_type="KEEP_ALL",
                        match_option=spatial_relationship
                    )

                # Add the result to the map
                self._add_to_map(output_path)

                # Get result statistics
                result_count = int(arcpy.GetCount_management(output_path)[0])

                return {
                    "success": True,
                    "output_layer": output_name,
                    "feature_count": result_count,
                    "spatial_relationship": spatial_relationship,
                    "target_layer": target_layer,
                    "join_layer": join_layer
                }

            except arcpy.ExecuteError as e:
                return {
                    "success": False,
                    "error": f"ArcGIS spatial join execution failed: {str(e)}",
                    "details": {
                        "target_layer": target_layer,
                        "join_layer": join_layer,
                        "spatial_relationship": spatial_relationship,
                        "arcgis_error": arcpy.GetMessages(2)  # Get detailed ArcGIS error messages
                    }
                }

        except Exception as e:
            return {
                "success": False,
                "error": f"Spatial join failed: {str(e)}",
                "troubleshooting": [
                    "Ensure both layers exist in the current ArcGIS Pro project",
                    "Check that layers have valid geometries",
                    "Verify coordinate systems are compatible",
                    "Make sure you have write permissions to the default geodatabase"
                ]
            }

    def clip_layer(self, params):
        input_layer = params.get("input_layer")
        clip_layer = params.get("clip_layer")
        output_name = f"{input_layer.replace(' ', '_')}_clipped"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        output_path = os.path.join(aprx.defaultGeodatabase, output_name)
        output_path = arcpy.CreateUniqueName(output_path)
        arcpy.analysis.Clip(r"{}".format(input_layer), r"{}".format(clip_layer), output_path)
        self._add_to_map(output_path)
        return {"success": True, "output_layer": output_name, "output_path": output_path}

    # Additional helper / missing functions
    def get_field_statistics(self, params):
        layer_name = params.get("layer_name")
        field_name = params.get("field_name")
        where_clause = params.get("where_clause")
        try:
            values = []
            for row in arcpy.da.SearchCursor(r"{}".format(layer_name), [field_name], where_clause):
                v = row[0]
                if v is None:
                    continue
                # accept numeric types only
                try:
                    nv = float(v)
                    values.append(nv)
                except Exception:
                    continue
            if not values:
                return {"success": False, "error": "No numeric values found"}
            return {
                "success": True,
                "count": len(values),
                "total": sum(values),
                "mean": statistics.mean(values),
                "min": min(values),
                "max": max(values),
                "std_dev": statistics.stdev(values) if len(values) > 1 else 0,
                "median": statistics.median(values)
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    def calculate_distance(self, params):
        point1 = params.get("point1")
        point2 = params.get("point2")
        units = params.get("units", "meters")
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
        
        return {"success": True, "distance": distance}


    def get_current_project_path(self, params=None):
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            path = getattr(aprx, 'filePath', None)
            return {"success": True, "project_path": path}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_default_db_path(self, params=None):
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            return {"success": True, "default_geodatabase": aprx.defaultGeodatabase}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_field_definitions(self, params):
        layer_name = params.get("layer_name")
        try:
            fields = arcpy.ListFields(r"{}".format(layer_name))
            info = [{"name": f.name, "type": f.type, "length": getattr(f, 'length', None), "alias": getattr(f, 'aliasName', None)} for f in fields]
            return {"success": True, "fields": info}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_layer_type(self, params):
        layer_name = params.get("layer_name")
        try:
            desc = arcpy.Describe(r"{}".format(layer_name))
            dtype = getattr(desc, 'dataType', None)
            shape = getattr(desc, 'shapeType', None)
            return {"success": True, "data_type": dtype, "shape_type": shape}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_list_of_layer_fields(self, params):
        return self.get_field_definitions(params)

    def get_data_source_info(self, params):
        layer_name = params.get("layer_name")
        try:
            desc = arcpy.Describe(r"{}".format(layer_name))
            return {"success": True, "data_source": getattr(desc, 'catalogPath', None)}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def create_nearest_neighbor_layer(self, params):
        layer_name = params.get("layer_name")
        id_field = params.get("id_field", "OBJECTID")
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
            stats = self.get_field_statistics({'layer_name': output_layer_name, 'field_name': nn_dist_field})

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
            return result
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_unique_values_count(self, params):
        layer_name = params.get("layer_name")
        field_name = params.get("field_name")
        try:
            vals = set()
            for row in arcpy.da.SearchCursor(r"{}".format(layer_name), [field_name]):
                vals.add(row[0])
            return {"success": True, "unique_count": len(vals)}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def calculate_empty_values(self, params):
        layer_name = params.get("layer_name")
        field_name = params.get("field_name")
        try:
            empty = 0
            total = 0
            for row in arcpy.da.SearchCursor(r"{}".format(layer_name), [field_name]):
                total += 1
                if row[0] is None:
                    empty += 1
            return {"success": True, "empty": empty, "total": total}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_map_layers_info(self, params=None):
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            map_obj = aprx.activeMap
            layers = []
            
            # Get all layers (including rasters)
            for lyr in map_obj.listLayers():
                try:
                    layer_info = {
                        "name": lyr.name,
                        "is_group": lyr.isGroupLayer if hasattr(lyr, 'isGroupLayer') else False,
                        "data_source": getattr(lyr, 'dataSource', None),
                        "visible": lyr.visible if hasattr(lyr, 'visible') else True
                    }
                    
                    # Determine layer type
                    if hasattr(lyr, 'isFeatureLayer') and lyr.isFeatureLayer:
                        layer_info["type"] = "Feature Layer"
                        try:
                            desc = arcpy.Describe(lyr.dataSource)
                            layer_info["geometry_type"] = getattr(desc, 'shapeType', 'Unknown')
                        except:
                            layer_info["geometry_type"] = "Unknown"
                    elif hasattr(lyr, 'isRasterLayer') and lyr.isRasterLayer:
                        layer_info["type"] = "Raster Layer"
                    else:
                        layer_info["type"] = "Other Layer"
                    
                    layers.append(layer_info)
                except Exception as e:
                    layers.append({
                        "name": getattr(lyr, 'name', 'Unknown'),
                        "error": str(e)
                    })
            
            # Get standalone tables
            tables = []
            for table in map_obj.listTables():
                try:
                    tables.append({
                        "name": table.name,
                        "type": "Standalone Table",
                        "data_source": getattr(table, 'dataSource', None)
                    })
                except Exception as e:
                    tables.append({
                        "name": getattr(table, 'name', 'Unknown'),
                        "error": str(e)
                    })
            
            return {
                "success": True, 
                "layers": layers,
                "tables": tables,
                "total_layers": len(layers),
                "total_tables": len(tables)
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_map_tables_info(self, params=None):
        # Tables are treated similarly to layers in ArcGIS Pro
        return self.get_map_layers_info(params)

    def get_values_frequency(self, params):
        layer_name = params.get("layer_name")
        field_name = params.get("field_name")
        try:
            freq = {}
            for row in arcpy.da.SearchCursor(r"{}".format(layer_name), [field_name]):
                k = row[0]
                # Handle None values and ensure proper string conversion for Unicode support
                if k is not None:
                    # Convert to string to handle any data type and preserve Unicode
                    k = str(k)
                    freq[k] = freq.get(k, 0) + 1
                else:
                    # Handle null values
                    null_key = "Null/Empty"
                    freq[null_key] = freq.get(null_key, 0) + 1
            return {"success": True, "frequency": freq}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_value_frequency(self, params):
        # Single value frequency
        layer_name = params.get("layer_name")
        field_name = params.get("field_name")
        value = params.get("value")
        res = self.get_values_frequency({'layer_name': layer_name, 'field_name': field_name})
        if not res.get('success'):
            return res
        return {"success": True, "value": value, "count": res['frequency'].get(value, 0)}

    def get_coordinate_system(self, params):
        layer_name = params.get("layer_name")
        try:
            desc = arcpy.Describe(r"{}".format(layer_name))
            sr = getattr(desc, 'spatialReference', None)
            if sr:
                return {"success": True, "name": sr.name, "wkid": getattr(sr, 'factoryCode', None)}
            return {"success": False, "error": "No spatial reference found"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def clear_selection(self, params):
        """Clears the current selection for a given layer."""
        layer_name = params.get("layer_name")
        try:
            arcpy.SelectLayerByAttribute_management(r"{}".format(layer_name), "CLEAR_SELECTION")
            return {"success": True, "message": f"Selection cleared for layer: {layer_name}"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_field_domain_values(self, params):
        workspace = params.get("workspace")
        field_domain = params.get("field_domain")
        try:
            domains = arcpy.da.ListDomains(r"{}".format(workspace))
            for d in domains:
                if d.name == field_domain and hasattr(d, 'codedValues'):
                    return {"success": True, "domain": d.name, "codedValues": d.codedValues}
            return {"success": False, "error": "Domain not found"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def calculate_new_field(self, params):
        layer = params.get("layer")
        field_name = params.get("field_name")
        field_type = params.get("field_type", "DOUBLE")
        expression = params.get("expression")
        try:
            arcpy.AddField_management(r"{}".format(layer), field_name, field_type)
            if expression:
                arcpy.CalculateField_management(r"{}".format(layer), field_name, expression, "PYTHON3")
            return {"success": True, "field_added": field_name}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def analyze_layer_fields(self, params):
        layer_name = params.get("layer")
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
            total_count = int(arcpy.GetCount_management(r"{}".format(layer_name))[0])
            if total_count == 0:
                return {"success": False, "error": f"Layer '{layer_name}' has no features"}

            fields = arcpy.ListFields(r"{}".format(layer_name))
            field_analysis = {}

            # Cursor for checking uniqueness without loading all values into memory at once
            with arcpy.da.SearchCursor(r"{}".format(layer_name), [f.name for f in fields]) as cursor:
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
                        continue
                    # Heuristic skip for numeric ID-like fields
                    if self._is_id_like_numeric(values):
                        continue

                # Smart skip for text fields that look like IDs (e.g., GUIDs, codes, numeric-as-text)
                if field.type in ['String', 'Text'] and values:
                    text_values = [str(v).strip() for v in values]
                    if self._is_id_like_text(text_values):
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
            return result

        except Exception as e:
            return {"success": False, "error": str(e)}

    # Raster-analysis stubs
    def raster_calculator(self, params):
        expression = params.get("expression")
        output_raster = params.get("output_raster")
        try:
            if arcpy.CheckExtension("Spatial") == "Available":
                arcpy.CheckOutExtension("Spatial")
            else:
                return {"success": False, "error": "Spatial Analyst extension is not available."}

            aprx = arcpy.mp.ArcGISProject("CURRENT")
            if not os.path.isabs(output_raster) and not os.path.sep in output_raster:
                out_path = os.path.join(aprx.defaultGeodatabase, output_raster)
                out_path = arcpy.CreateUniqueName(out_path)
            else:
                out_path = output_raster

            # The expression is evaluated directly. This is powerful but requires the input
            # from the AI to be trusted. The function declaration explicitly states that the
            # expression will contain `Raster` objects.

            # Import necessary arcpy.sa functions for eval context
            from arcpy.sa import Raster

            # Execute the map algebra expression
            result_raster = eval(expression)
            result_raster.save(out_path)

            self._add_to_map(out_path)

            return {"success": True, "output_raster": out_path, "message": f"Raster calculation executed successfully. Output saved to {out_path}"}
        except Exception as e:
            tb = traceback.format_exc()
            return {"success": False, "error": str(e), "traceback": tb}
        finally:
            arcpy.CheckInExtension("Spatial")

    def reclassify(self, params):
        in_raster = params.get("in_raster")
        reclass_field = params.get("reclass_field")
        remap_str = params.get("remap")
        out_raster = params.get("out_raster")
        try:
            if arcpy.CheckExtension("Spatial") == "Available":
                arcpy.CheckOutExtension("Spatial")
            else:
                return {"success": False, "error": "Spatial Analyst extension is not available."}

            aprx = arcpy.mp.ArcGISProject("CURRENT")
            if not os.path.isabs(out_raster) and not os.path.sep in out_raster:
                output_name = f"{in_raster.replace(' ', '_')}_reclassified"
                out_path = os.path.join(aprx.defaultGeodatabase, output_name)
                out_path = arcpy.CreateUniqueName(out_path)
            else:
                out_path = out_raster

            # The remap parameter is a string representation of a Remap object (e.g., RemapRange, RemapValue)
            # which needs to be evaluated. This requires trusting the AI-generated input.
            from arcpy.sa import RemapRange, RemapValue

            remap_obj = eval(remap_str)

            # Perform the reclassification
            result_raster = arcpy.sa.Reclassify(r"{}".format(in_raster), reclass_field, remap_obj, "DATA")
            result_raster.save(out_path)

            self._add_to_map(out_path)

            return {"success": True, "output_raster": out_path, "message": f"Reclassify completed successfully. Output saved to {out_path}"}
        except Exception as e:
            tb = traceback.format_exc()
            return {"success": False, "error": str(e), "traceback": tb}
        finally:
            arcpy.CheckInExtension("Spatial")

    def zonal_statistics_as_table(self, params):
        in_zone_data = params.get("in_zone_data")
        zone_field = params.get("zone_field")
        in_value_raster = params.get("in_value_raster")
        out_table = params.get("out_table")
        statistics_type = params.get("statistics_type", "MEAN")
        try:
            if arcpy.CheckExtension("Spatial") == "Available":
                arcpy.CheckOutExtension("Spatial")
            else:
                return {"success": False, "error": "Spatial Analyst extension is not available."}

            aprx = arcpy.mp.ArcGISProject("CURRENT")
            if not os.path.isabs(out_table) and not os.path.sep in out_table:
                output_name = f"{in_zone_data.replace(' ', '_')}_zonal_stats"
                out_path = os.path.join(aprx.defaultGeodatabase, output_name)
                out_path = arcpy.CreateUniqueName(out_path)
            else:
                out_path = out_table

            from arcpy.sa import ZonalStatisticsAsTable

            # Perform the zonal statistics
            ZonalStatisticsAsTable(r"{}".format(in_zone_data), zone_field, r"{}".format(in_value_raster), out_path, "DATA", statistics_type)

            # Add the resulting table to the map
            self._add_to_map(out_path)

            return {"success": True, "output_table": out_path, "message": f"Zonal statistics table created successfully at {out_path}"}
        except Exception as e:
            tb = traceback.format_exc()
            return {"success": False, "error": str(e), "traceback": tb}
        finally:
            arcpy.CheckInExtension("Spatial")

    def slope(self, params):
        in_raster = params.get("in_raster")
        out_raster = params.get("out_raster")
        output_measurement = params.get("output_measurement", "DEGREE")
        try:
            if arcpy.CheckExtension("Spatial") == "Available":
                arcpy.CheckOutExtension("Spatial")
            else:
                return {"success": False, "error": "Spatial Analyst extension is not available."}

            aprx = arcpy.mp.ArcGISProject("CURRENT")
            if not os.path.isabs(out_raster) and not os.path.sep in out_raster:
                output_name = f"{in_raster.replace(' ', '_')}_slope"
                out_path = os.path.join(aprx.defaultGeodatabase, output_name)
                out_path = arcpy.CreateUniqueName(out_path)
            else:
                out_path = out_raster

            from arcpy.sa import Slope

            # Perform the slope analysis
            result_raster = Slope(r"{}".format(in_raster), output_measurement)
            result_raster.save(out_path)

            self._add_to_map(out_path)

            return {"success": True, "output_raster": out_path, "message": f"Slope analysis completed successfully. Output saved to {out_path}"}
        except Exception as e:
            tb = traceback.format_exc()
            return {"success": False, "error": str(e), "traceback": tb}
        finally:
            arcpy.CheckInExtension("Spatial")

    def aspect(self, params):
        in_raster = params.get("in_raster")
        out_raster = params.get("out_raster")
        try:
            if arcpy.CheckExtension("Spatial") == "Available":
                arcpy.CheckOutExtension("Spatial")
            else:
                return {"success": False, "error": "Spatial Analyst extension is not available."}

            aprx = arcpy.mp.ArcGISProject("CURRENT")
            if not os.path.isabs(out_raster) and not os.path.sep in out_raster:
                output_name = f"{in_raster.replace(' ', '_')}_aspect"
                out_path = os.path.join(aprx.defaultGeodatabase, output_name)
                out_path = arcpy.CreateUniqueName(out_path)
            else:
                out_path = out_raster

            from arcpy.sa import Aspect

            # Perform the aspect analysis
            result_raster = Aspect(r"{}".format(in_raster))
            result_raster.save(out_path)

            self._add_to_map(out_path)

            return {"success": True, "output_raster": out_path, "message": f"Aspect analysis completed successfully. Output saved to {out_path}"}
        except Exception as e:
            tb = traceback.format_exc()
            return {"success": False, "error": str(e), "traceback": tb}
        finally:
            arcpy.CheckInExtension("Spatial")

    def hillshade(self, params):
        in_raster = params.get("in_raster")
        out_raster = params.get("out_raster")
        azimuth = params.get("azimuth", 315)
        altitude = params.get("altitude", 45)
        try:
            if arcpy.CheckExtension("Spatial") == "Available":
                arcpy.CheckOutExtension("Spatial")
            else:
                return {"success": False, "error": "Spatial Analyst extension is not available."}

            aprx = arcpy.mp.ArcGISProject("CURRENT")
            if not os.path.isabs(out_raster) and not os.path.sep in out_raster:
                output_name = f"{in_raster.replace(' ', '_')}_hillshade"
                out_path = os.path.join(aprx.defaultGeodatabase, output_name)
                out_path = arcpy.CreateUniqueName(out_path)
            else:
                out_path = out_raster

            from arcpy.sa import Hillshade

            # Perform the hillshade analysis
            result_raster = Hillshade(r"{}".format(in_raster), azimuth, altitude)
            result_raster.save(out_path)

            self._add_to_map(out_path)

            return {"success": True, "output_raster": out_path, "message": f"Hillshade analysis completed successfully. Output saved to {out_path}"}
        except Exception as e:
            tb = traceback.format_exc()
            return {"success": False, "error": str(e), "traceback": tb}
        finally:
            arcpy.CheckInExtension("Spatial")


    def clip_raster(self, params):
        in_raster = params.get("in_raster")
        out_raster = params.get("out_raster")
        in_template_dataset = params.get("in_template_dataset")
        clipping_geometry = params.get("clipping_geometry", "ClippingGeometry")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            if not os.path.isabs(out_raster) and not os.path.sep in out_raster:
                output_name = f"{in_raster.replace(' ', '_')}_clipped"
                out_path = os.path.join(aprx.defaultGeodatabase, output_name)
                out_path = arcpy.CreateUniqueName(out_path)
            else:
                out_path = out_raster

            # Perform the clip analysis
            arcpy.management.Clip(
                r"{}".format(in_raster),
                "#", # rectangle
                out_path,
                r"{}".format(in_template_dataset),
                "#", # nodata_value
                clipping_geometry,
                "MAINTAIN_EXTENT" # maintain_clipping_extent
            )

            self._add_to_map(out_path)

            return {"success": True, "output_raster": out_path, "message": f"Raster clip completed successfully. Output saved to {out_path}"}
        except Exception as e:
            tb = traceback.format_exc()
            return {"success": False, "error": str(e), "traceback": tb}

    def resample(self, params):
        in_raster = params.get("in_raster")
        out_raster = params.get("out_raster")
        cell_size = params.get("cell_size")
        resampling_type = params.get("resampling_type", "NEAREST")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            if not os.path.isabs(out_raster) and not os.path.sep in out_raster:
                output_name = f"{in_raster.replace(' ', '_')}_resampled"
                out_path = os.path.join(aprx.defaultGeodatabase, output_name)
                out_path = arcpy.CreateUniqueName(out_path)
            else:
                out_path = out_raster

            # Perform the resample
            arcpy.management.Resample(r"{}".format(in_raster), out_path, cell_size, resampling_type)

            self._add_to_map(out_path)

            return {"success": True, "output_raster": out_path, "message": f"Resample completed successfully. Output saved to {out_path}"}
        except Exception as e:
            tb = traceback.format_exc()
            return {"success": False, "error": str(e), "traceback": tb}

    def get_raster_properties(self, params):
        raster = params.get("raster")
        try:
            props = {}
            ras = arcpy.Describe(r"{}".format(raster))
            props['pixelType'] = getattr(ras, 'pixelType', None)
            props['width'] = getattr(ras, 'width', None)
            props['height'] = getattr(ras, 'height', None)
            props['spatialReference'] = getattr(getattr(ras, 'spatialReference', None), 'name', None)
            return {"success": True, "properties": props}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def extract_by_mask(self, params):
        in_raster = params.get("in_raster")
        in_mask_data = params.get("in_mask_data")
        out_raster = params.get("out_raster")
        try:
            # Check if Spatial Analyst extension is available
            if arcpy.CheckExtension("Spatial") == "Available":
                arcpy.CheckOutExtension("Spatial")
            else:
                return {"success": False, "error": "Spatial Analyst extension is not available"}

            aprx = arcpy.mp.ArcGISProject("CURRENT")

            # If caller provided a simple name (no path separator), save to default geodatabase
            if out_raster and not (os.path.isabs(out_raster) or os.path.sep in out_raster):
                output_name = out_raster
                out_path = os.path.join(aprx.defaultGeodatabase, output_name)
                out_path = arcpy.CreateUniqueName(out_path)
            elif out_raster:
                out_path = out_raster
            else:
                # Build a reasonable default name
                import re
                safe_name = re.sub(r'[^\w\-_\.]', '_', str(in_raster))
                output_name = f"{safe_name}_extracted_by_mask"
                out_path = os.path.join(aprx.defaultGeodatabase, output_name)
                out_path = arcpy.CreateUniqueName(out_path)

            # Perform extract by mask using Spatial Analyst
            from arcpy.sa import ExtractByMask
            result_ras = ExtractByMask(r"{}".format(in_raster), r"{}".format(in_mask_data))
            result_ras.save(out_path)

            try:
                self._add_to_map(out_path)
            except Exception:
                pass

            return {"success": True, "output_raster": out_path, "message": f"Extract by mask completed successfully. Output saved to {out_path}"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    # Raster Functions
    def raster_to_point(self, params):
        in_raster = params.get("in_raster")
        output_name = f"{in_raster.replace(' ', '_')}_points"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_point_features = os.path.join(aprx.defaultGeodatabase, output_name)
        out_point_features = arcpy.CreateUniqueName(out_point_features)
        arcpy.conversion.RasterToPoint(r"{}".format(in_raster), out_point_features)
        self._add_to_map(out_point_features)
        return {"success": True, "output_layer": out_point_features}

    def raster_to_polygon(self, params):
        in_raster = params.get("in_raster")
        output_name = f"{in_raster.replace(' ', '_')}_polygons"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_polygon_features = os.path.join(aprx.defaultGeodatabase, output_name)
        out_polygon_features = arcpy.CreateUniqueName(out_polygon_features)
        arcpy.conversion.RasterToPolygon(r"{}".format(in_raster), out_polygon_features)
        self._add_to_map(out_polygon_features)
        return {"success": True, "output_layer": out_polygon_features}

    def raster_to_polyline(self, params):
        in_raster = params.get("in_raster")
        output_name = f"{in_raster.replace(' ', '_')}_polylines"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_polyline_features = os.path.join(aprx.defaultGeodatabase, output_name)
        out_polyline_features = arcpy.CreateUniqueName(out_polyline_features)
        arcpy.conversion.RasterToPolyline(r"{}".format(in_raster), out_polyline_features)
        self._add_to_map(out_polyline_features)
        return {"success": True, "output_layer": out_polyline_features}

    def feature_to_raster(self, params):
        in_features = params.get("in_features")
        field = params.get("field")
        try:
            # Handle special characters in layer names
            if in_features:
                import re
                safe_name = re.sub(r'[^\w\-_\.]', '_', str(in_features))
                output_name = f"{safe_name}_raster"
            else:
                output_name = "feature_raster"
            
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
            out_raster = arcpy.CreateUniqueName(out_raster)
            arcpy.conversion.FeatureToRaster(r"{}".format(in_features), field, out_raster)
            self._add_to_map(out_raster)
            return {"success": True, "output_raster": out_raster}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def polygon_to_raster(self, params):
        in_features = params.get("in_features")
        value_field = params.get("value_field")
        out_raster_param = params.get("out_raster")
        cell_size = params.get("cell_size")
        try:
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            
            # Use provided output path or create default one
            if out_raster_param and (os.path.isabs(out_raster_param) or os.path.sep in out_raster_param):
                out_raster = out_raster_param
            else:
                # Handle Arabic or special characters in layer names for default name
                if in_features:
                    import re
                    safe_name = re.sub(r'[^\w\-_\.]', '_', str(in_features))
                    output_name = f"{safe_name}_polygon_raster"
                else:
                    output_name = "polygon_raster"
                
                out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
                out_raster = arcpy.CreateUniqueName(out_raster)
            
            # Execute conversion with optional cell size
            if cell_size:
                arcpy.conversion.PolygonToRaster(r"{}".format(in_features), value_field, out_raster, cell_assignment="CELL_CENTER", priority_field=None, cellsize=cell_size)
            else:
                arcpy.conversion.PolygonToRaster(r"{}".format(in_features), value_field, out_raster)
            
            self._add_to_map(out_raster)
            return {"success": True, "output_raster": out_raster}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def point_to_raster(self, params):
        in_features = params.get("in_features")
        value_field = params.get("value_field")
        try:
            # Handle special characters in layer names
            if in_features:
                import re
                safe_name = re.sub(r'[^\w\-_\.]', '_', str(in_features))
                output_name = f"{safe_name}_raster"
            else:
                output_name = "point_raster"
            
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
            out_raster = arcpy.CreateUniqueName(out_raster)
            arcpy.conversion.PointToRaster(r"{}".format(in_features), value_field, out_raster)
            self._add_to_map(out_raster)
            return {"success": True, "output_raster": out_raster}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def idw_interpolation(self, params):
        in_point_features = params.get("in_point_features")
        z_field = params.get("z_field")
        out_raster = params.get("out_raster")
        try:
            # Check if Spatial Analyst extension is available
            if arcpy.CheckExtension("Spatial") == "Available":
                arcpy.CheckOutExtension("Spatial")
            else:
                return {"success": False, "error": "Spatial Analyst extension is not available"}

            aprx = arcpy.mp.ArcGISProject("CURRENT")

            # Convert inputs to raw strings to handle spaces properly
            if in_point_features:
                in_point_features = r"{}".format(in_point_features)
            if z_field:
                z_field = r"{}".format(z_field)

            # Handle output path - if provided use it, otherwise create default name
            if out_raster and (os.path.isabs(out_raster) or os.path.sep in out_raster):
                out_path = r"{}".format(out_raster)
            else:
                # Build a reasonable default name
                if in_point_features:
                    safe_name = re.sub(r'[^\w\-_\.]', '_', str(in_point_features))
                    output_name = f"{safe_name}_idw"
                else:
                    output_name = "idw_interpolation"
                
                out_path = os.path.join(aprx.defaultGeodatabase, output_name)
                out_path = arcpy.CreateUniqueName(out_path)

            # Perform IDW interpolation
            from arcpy.sa import Idw
            result_raster = Idw(in_point_features, z_field)
            result_raster.save(out_path)

            try:
                self._add_to_map(out_path)
            except Exception:
                pass

            return {"success": True, "output_raster": out_path, "message": f"IDW interpolation completed successfully. Output saved to {out_path}"}
        except Exception as e:
            tb = traceback.format_exc()
            return {"success": False, "error": str(e), "traceback": tb}
        finally:
            try:
                arcpy.CheckInExtension("Spatial")
            except:
                pass

    def kriging_interpolation(self, params):
        in_point_features = params.get("in_point_features")
        z_field = params.get("z_field")
        out_raster = params.get("out_raster")
        try:
            # Check if Spatial Analyst extension is available
            if arcpy.CheckExtension("Spatial") == "Available":
                arcpy.CheckOutExtension("Spatial")
            else:
                return {"success": False, "error": "Spatial Analyst extension is not available"}

            aprx = arcpy.mp.ArcGISProject("CURRENT")

            # Handle output path - if provided use it, otherwise create default name
            if out_raster and (os.path.isabs(out_raster) or os.path.sep in out_raster):
                out_path = out_raster
            else:
                # Build a reasonable default name
                if in_point_features:
                    safe_name = re.sub(r'[^\w\-_\.]', '_', str(in_point_features))
                    output_name = f"{safe_name}_kriging"
                else:
                    output_name = "kriging_interpolation"
                
                out_path = os.path.join(aprx.defaultGeodatabase, output_name)
                out_path = arcpy.CreateUniqueName(out_path)

            # Perform Kriging interpolation
            from arcpy.sa import Kriging
            result_raster = Kriging(r"{}".format(in_point_features), z_field)
            result_raster.save(out_path)

            try:
                self._add_to_map(out_path)
            except Exception:
                pass

            return {"success": True, "output_raster": out_path, "message": f"Kriging interpolation completed successfully. Output saved to {out_path}"}
        except Exception as e:
            tb = traceback.format_exc()
            return {"success": False, "error": str(e), "traceback": tb}
        finally:
            try:
                arcpy.CheckInExtension("Spatial")
            except:
                pass

    def spline_interpolation(self, params):
        in_point_features = params.get("in_point_features")
        z_field = params.get("z_field")
        out_raster = params.get("out_raster")
        try:
            # Check if Spatial Analyst extension is available
            if arcpy.CheckExtension("Spatial") == "Available":
                arcpy.CheckOutExtension("Spatial")
            else:
                return {"success": False, "error": "Spatial Analyst extension is not available"}

            aprx = arcpy.mp.ArcGISProject("CURRENT")

            # Handle output path - if provided use it, otherwise create default name
            if out_raster and (os.path.isabs(out_raster) or os.path.sep in out_raster):
                out_path = out_raster
            else:
                # Build a reasonable default name
                if in_point_features:
                    safe_name = re.sub(r'[^\w\-_\.]', '_', str(in_point_features))
                    output_name = f"{safe_name}_spline"
                else:
                    output_name = "spline_interpolation"
                
                out_path = os.path.join(aprx.defaultGeodatabase, output_name)
                out_path = arcpy.CreateUniqueName(out_path)

            # Perform Spline interpolation
            from arcpy.sa import Spline
            result_raster = Spline(r"{}".format(in_point_features), z_field)
            result_raster.save(out_path)

            try:
                self._add_to_map(out_path)
            except Exception:
                pass

            return {"success": True, "output_raster": out_path, "message": f"Spline interpolation completed successfully. Output saved to {out_path}"}
        except Exception as e:
            tb = traceback.format_exc()
            return {"success": False, "error": str(e), "traceback": tb}
        finally:
            try:
                arcpy.CheckInExtension("Spatial")
            except:
                pass

    def natural_neighbor(self, params):
        in_point_features = params.get("in_point_features")
        z_field = params.get("z_field")
        out_raster = params.get("out_raster")
        try:
            # Check if Spatial Analyst extension is available
            if arcpy.CheckExtension("Spatial") == "Available":
                arcpy.CheckOutExtension("Spatial")
            else:
                return {"success": False, "error": "Spatial Analyst extension is not available"}

            aprx = arcpy.mp.ArcGISProject("CURRENT")

            # Handle output path - if provided use it, otherwise create default name
            if out_raster and (os.path.isabs(out_raster) or os.path.sep in out_raster):
                out_path = out_raster
            else:
                # Build a reasonable default name
                if in_point_features:
                    safe_name = re.sub(r'[^\w\-_\.]', '_', str(in_point_features))
                    output_name = f"{safe_name}_natural_neighbor"
                else:
                    output_name = "natural_neighbor_interpolation"
                
                out_path = os.path.join(aprx.defaultGeodatabase, output_name)
                out_path = arcpy.CreateUniqueName(out_path)

            # Perform Natural Neighbor interpolation
            from arcpy.sa import NaturalNeighbor
            result_raster = NaturalNeighbor(r"{}".format(in_point_features), z_field)
            result_raster.save(out_path)

            try:
                self._add_to_map(out_path)
            except Exception:
                pass

            return {"success": True, "output_raster": out_path, "message": f"Natural Neighbor interpolation completed successfully. Output saved to {out_path}"}
        except Exception as e:
            tb = traceback.format_exc()
            return {"success": False, "error": str(e), "traceback": tb}
        finally:
            try:
                arcpy.CheckInExtension("Spatial")
            except:
                pass

    def euclidean_distance(self, params):
        in_source_data = params.get("in_source_data")
        output_name = f"{in_source_data.replace(' ', '_')}_euclidean_dist"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.EucDistance(r"{}".format(in_source_data)).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def euclidean_allocation(self, params):
        in_source_data = params.get("in_source_data")
        output_name = f"{in_source_data.replace(' ', '_')}_euclidean_alloc"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.EucAllocation(r"{}".format(in_source_data)).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def euclidean_direction(self, params):
        in_source_data = params.get("in_source_data")
        output_name = f"{in_source_data.replace(' ', '_')}_euclidean_dir"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.EucDirection(r"{}".format(in_source_data)).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def cost_distance(self, params):
        in_source_data = params.get("in_source_data")
        in_cost_raster = params.get("in_cost_raster")
        output_name = f"{in_source_data.replace(' ', '_')}_cost_dist"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.CostDistance(r"{}".format(in_source_data), r"{}".format(in_cost_raster)).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def cost_allocation(self, params):
        in_source_data = params.get("in_source_data")
        in_cost_raster = params.get("in_cost_raster")
        output_name = f"{in_source_data.replace(' ', '_')}_cost_alloc"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.CostAllocation(r"{}".format(in_source_data), r"{}".format(in_cost_raster)).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def cost_path(self, params):
        in_destination_data = params.get("in_destination_data")
        in_cost_distance_raster = params.get("in_cost_distance_raster")
        in_cost_backlink_raster = params.get("in_cost_backlink_raster")
        output_name = f"{in_destination_data.replace(' ', '_')}_cost_path"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.CostPath(r"{}".format(in_destination_data), r"{}".format(in_cost_distance_raster), r"{}".format(in_cost_backlink_raster)).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def weighted_overlay(self, params):
        overlay_table = params.get("overlay_table")
        output_name = f"weighted_overlay"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.WeightedOverlay(overlay_table).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def weighted_sum(self, params):
        in_rasters = params.get("in_rasters")
        output_name = f"weighted_sum"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.WeightedSum(in_rasters).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def extract_by_attribute(self, params):
        in_raster = params.get("in_raster")
        where_clause = params.get("where_clause")
        output_name = f"{in_raster.replace(' ', '_')}_extract_by_attr"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.ExtractByAttributes(r"{}".format(in_raster), where_clause).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def mosaic_to_new_raster(self, params):
        input_rasters = params.get("input_rasters")
        output_location = params.get("output_location")
        raster_dataset_name_with_extension = params.get("raster_dataset_name_with_extension")
        pixel_type = params.get("pixel_type")
        number_of_bands = params.get("number_of_bands")

        # Handle spaces in input raster paths
        input_rasters_list = [fr"{r.strip()}" for r in input_rasters.split(';') if r.strip()]

        arcpy.management.MosaicToNewRaster(input_rasters_list, r"{}".format(output_location), raster_dataset_name_with_extension,
                                           pixel_type=pixel_type, number_of_bands=number_of_bands)
        out_path = os.path.join(output_location, raster_dataset_name_with_extension)
        self._add_to_map(out_path)
        return {"success": True, "output_raster": out_path}

    def combine_rasters(self, params):
        in_rasters = params.get("in_rasters")

        # Handle spaces in input raster paths and create a list
        in_rasters_list = [fr"{r.strip()}" for r in in_rasters.split(';') if r.strip()]

        if not in_rasters_list:
            return {"success": False, "error": "No input rasters provided for combine."}

        output_name = f"{os.path.basename(in_rasters_list[0]).replace(' ', '_')}_combined"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.Combine(in_rasters_list).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

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

            return ai_insights
            
        except Exception as e:
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
        n = len(sorted_values)
        q1 = sorted_values[n // 4]
        q3 = sorted_values[3 * n // 4]
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        outliers = [v for v in values if v < lower_bound or v > upper_bound]
        outlier_count = len(outliers)
        outlier_percentage = (outlier_count / n) * 100 if n > 0 else 0
        
        return {"outlier_count": outlier_count, "outlier_percentage": outlier_percentage}
    
    def _analyze_text_patterns(self, values: List[str], unique_values: List[str]) -> Dict:
        """Analyze patterns in text data"""
        patterns = {
            "has_consistent_format": False,
            "has_varied_length": False,
            "likely_codes": False,
            "likely_names": False
        }
        
        if not values:
            return patterns
        
        lengths = [len(v) for v in values]
        avg_length = sum(lengths) / len(lengths)
        
        # Check for consistent format (low length variance)
        length_variance = sum((l - avg_length) ** 2 for l in lengths) / len(lengths)
        if length_variance < 5:
            patterns["has_consistent_format"] = True
        
        # Check for varied length
        if max(lengths) > avg_length * 2:
            patterns["has_varied_length"] = True
        
        # Check for likely codes (alphanumeric, short)
        if avg_length <= 15 and all(re.match(r'^[a-zA-Z0-9\s_-]+$', v) for v in unique_values[:10]):
            patterns["likely_codes"] = True
        
        # Check for likely names (capitalized words)
        name_like_count = sum(1 for v in unique_values[:20] if ' ' in v and all(w.istitle() for w in v.split()))
        if name_like_count / min(20, len(unique_values)) > 0.5:
            patterns["likely_names"] = True
            
        return patterns
    
    def _get_timestamp(self) -> str:
        """Get current timestamp in ISO format"""
        from datetime import datetime
        return datetime.now().isoformat()

    def _create_chart_from_field(self, field_info: Dict, theme: str) -> Dict:
        """
        Creates a histogram chart configuration for numerical fields.
        This creates metadata only - the frontend will handle data visualization.
        """
        try:
            field_name = field_info.get("field_name", "unknown")
            data_category = field_info.get("data_category", "")
            
            print(f"DEBUG: Creating histogram chart for field: {field_name}")
            
            # For numerical fields, create histogram charts
            if data_category in ["continuous_numeric", "categorical_numeric"]:
                chart_config = {
                    "id": f"chart_{field_name}",
                    "field_name": field_name,
                    "chart_type": "histogram",
                    "data_category": data_category,
                    "title": field_info.get("data_story", f"Distribution of {field_name}"),
                    "visualization_potential": field_info.get("visualization_potential", "high"),
                    "chart_suitability": field_info.get("chart_suitability", {"histogram": 0.9}),
                    "theme": theme
                }
                
                print(f"DEBUG: Created histogram chart config for {field_name}")
                return chart_config
            else:
                print(f"DEBUG: Field {field_name} is not numerical, skipping")
                return None
            
        except Exception as e:
            print(f"DEBUG: Exception in _create_chart_from_field: {str(e)}")
            return None
    
    def _get_chart_options(self, chart_type: str, theme: str) -> Dict:
        """
        Provides default chart options based on chart type and theme.
        """
        options = {
            "color_palette": "default_palette",
            "show_legend": True,
            "show_labels": True
        }
        
        if chart_type in ["bar", "column", "line_chart"]:
            options["axis_titles"] = {"x": "Category", "y": "Value"}
        
        if chart_type == "histogram":
            options["bin_count"] = "auto"
        
        if theme == "dark":
            options["color_palette"] = "dark_palette"
            options["font_color"] = "#FFFFFF"
        
        return options
    
    def _arrange_charts_in_layout(self, charts: List[Dict]) -> Dict:
        """
        Arranges charts into a grid-based layout.
        """
        layout = {
            "grid_template_columns": "1fr 1fr 1fr",
            "gap": "20px",
            "items": []
        }
        
        for i, chart in enumerate(charts):
            layout["items"].append({
                "id": chart["id"],
                "chart_type": chart.get("chart_type", "bar"),
                "field_name": chart.get("field_name", ""),
                "grid_area": f"chart-{i+1}"
            })
            
        return layout

    def _create_count_chart_from_text_field(self, field_info: Dict, chart_type: str, theme: str) -> Dict:
        """
        Creates a count-based chart from a textual field.
        This creates metadata only - the frontend will handle data visualization.
        """
        try:
            field_name = field_info.get("field_name", "unknown")
            unique_count = field_info.get("unique_count", 0)
            data_category = field_info.get("data_category", "categorical_text")

            # Create chart configuration matching the expected dashboard format
            chart_config = {
                "id": f"chart_{field_name}",
                "field_name": field_name,
                "chart_type": chart_type,
                "data_category": data_category,
                "title": field_info.get("data_story", f"Distribution of {field_name}"),
                "visualization_potential": field_info.get("visualization_potential", "high"),
                "chart_suitability": field_info.get("chart_suitability", {chart_type: 0.9}),
                "theme": theme
            }

            print(f"DEBUG: Created {chart_type} chart config for textual field {field_name}")
            return chart_config

        except Exception as e:
            print(f"DEBUG: Exception in _create_count_chart_from_text_field: {str(e)}")
            return None

    def _create_aggregation_chart_from_data(self, layer_name: str, num_field_info: Dict, category_field_info: Dict, theme: str) -> Dict:
        """
        Creates an aggregation chart by combining a numerical field with a textual category field.
        Uses the working aggregation logic from add_chart_to_dashboard.
        """
        print(f"DEBUG: _create_aggregation_chart_from_data called for {num_field_info.get('field_name')} by {category_field_info.get('field_name')}")
        try:
            num_field_name = num_field_info.get("field_name", "unknown")
            category_field_name = category_field_info.get("field_name", "unknown")
            data_category = num_field_info.get("data_category", "")
            
            # Determine aggregation type based on numerical field characteristics
            if data_category == "continuous_numeric":
                aggregation = "mean"  # Mean for continuous values
            else:
                aggregation = "sum"  # Sum for categorical numeric
            
            # Use ArcPy to get aggregated data
            data = {}
            cursor_fields = [category_field_name, num_field_name]
            
            with arcpy.da.SearchCursor(layer_name, cursor_fields) as cursor:
                for row in cursor:
                    category = row[0]
                    value = row[1]
                    
                    if category is not None:
                        category = str(category)
                    else:
                        category = "Null/Empty"
                    
                    if category not in data:
                        data[category] = []
                    
                    # Only add numeric values, skip nulls and non-numeric
                    if value is not None and isinstance(value, (int, float)):
                        data[category].append(value)
            
            # Create chart data
            chart_data = {"labels": [], "values": []}
            
            for category, values in data.items():
                if values:  # Only proceed if we have values
                    chart_data["labels"].append(category)
                    
                    if aggregation == "sum":
                        chart_data["values"].append(sum(values))
                    elif aggregation in ["mean", "avg", "average"]:
                        chart_data["values"].append(statistics.mean(values))
                    elif aggregation == "count":
                        chart_data["values"].append(len(values))
                    elif aggregation == "min":
                        chart_data["values"].append(min(values))
                    elif aggregation == "max":
                        chart_data["values"].append(max(values))
                else:
                    chart_data["labels"].append(category)
                    chart_data["values"].append(0)
            
            # Create chart configuration matching dashboard format
            chart_config = {
                "id": f"chart_{num_field_name}_by_{category_field_name}",
                "field_name": num_field_name,
                "chart_type": "bar",
                "data_category": "aggregation",
                "title": f"{aggregation.title()} of {num_field_name} by {category_field_name}",
                "visualization_potential": "high",
                "chart_suitability": {"bar": 0.95, "column": 0.90},
                "theme": theme,
                "category_field": category_field_name,
                "series": [
                    {
                        "field": num_field_name,
                        "name": num_field_name
                    }
                ],
                "fields": [
                    category_field_name,
                    num_field_name
                ],
                "aggregation_info": {
                    "numeric_field": num_field_name,
                    "category_field": category_field_name,
                    "aggregation_type": aggregation,
                    "data": chart_data
                }
            }
            
            return chart_config
            
        except Exception as e:
            return None

    def generate_dashboard_for_target_layer(self, params):
        """
        Generate a smart dashboard layout based on field insights.
        Enhanced to prioritize textual fields for count-based charts and
        create aggregation charts combining numerical and textual fields.
        """
        print("DEBUG: generate_dashboard_for_target_layer called with enhanced aggregation logic")
        try:
            layer_name = params.get("layer_name") or params.get("layer")
            field_insights = params.get("field_insights", {})
            theme = params.get("theme", "default")
            analysis_type = params.get("analysis_type", "overview")

            if not layer_name:
                return {"success": False, "error": "layer_name parameter is required"}

            if not field_insights:
                return {"success": False, "error": "field_insights parameter is required"}

            # Enhanced field categorization and filtering
            textual_fields = []
            numerical_fields = []
            excluded_fields = []

            for field_name, field_info in field_insights.items():
                data_category = field_info.get("data_category", "")
                unique_count = field_info.get("unique_count", 0)
                total_records = field_info.get("total_records", 1)
                field_name_lower = field_name.lower()

                # Skip system fields and problematic fields
                if any(skip_field in field_name_lower for skip_field in [
                    'objectid', 'shape', 'globalid', 'fid', 'oid', 'geometry'
                ]):
                    excluded_fields.append(field_info)
                    continue

                # Skip coordinate-like fields and basic system fields
                if data_category in ["continuous_numeric", "categorical_numeric"]:
                    field_name_lower = field_name.lower()
                    is_coordinate_name = any(coord in field_name_lower for coord in ['lat', 'lon', 'x', 'y', 'coord', 'longitude', 'latitude'])
                    
                    # Only exclude coordinate fields and constant values
                    if is_coordinate_name or unique_count == 1:
                        excluded_fields.append(field_info)
                        continue
                    else:
                        numerical_fields.append(field_info)

                # Include textual fields (keep it simple)
                elif data_category in ["categorical_text", "text", "name_field"]:
                    textual_fields.append(field_info)

            # Sort fields by quality (unique count for textual, visualization priority for numerical)
            textual_fields.sort(key=lambda x: x.get("unique_count", 0), reverse=True)
            numerical_fields.sort(key=lambda x: x.get("visualization_priority", 0), reverse=True)

            charts = []
            used_textual_fields = []
            used_numerical_fields = []

            # Find suitable category fields first (textual fields with 2-8 unique values)
            suitable_category_fields = []
            for field_info in textual_fields:
                unique_count = field_info.get("unique_count", 0)
                field_name = field_info.get("field_name", "unknown")
                if unique_count > 1 and unique_count < 9:  # Between 2 and 8 unique values
                    suitable_category_fields.append(field_info)
                    print(f"DEBUG: Found suitable category field: {field_name} ({unique_count} unique values)")
            
            print(f"DEBUG: Total suitable category fields found: {len(suitable_category_fields)}")
            print(f"DEBUG: Available numerical fields: {len(numerical_fields)}")

            # Phase 1: Prioritize aggregation charts if suitable category fields exist
            if suitable_category_fields and numerical_fields:
                print("DEBUG: Creating aggregation charts as priority")
                
                # Create aggregation charts for numerical fields using category fields
                charts_created = 0
                for num_field_info in numerical_fields:
                    if charts_created >= 4:  # Limit aggregation charts to make room for others
                        break
                        
                    num_field_name = num_field_info.get("field_name", "unknown")
                    print(f"DEBUG: Creating aggregation chart for numerical field '{num_field_name}'")
                    
                    # Select the best category field (prefer fields with more unique values for better distribution)
                    category_field_info = max(suitable_category_fields, key=lambda x: x.get("unique_count", 0))
                    category_field_name = category_field_info.get("field_name", "unknown")
                    
                    print(f"DEBUG: Using '{category_field_name}' as category field ({category_field_info.get('unique_count', 0)} unique values)")
                    
                    # Create aggregation chart using real data
                    chart_config = self._create_aggregation_chart_from_data(
                        layer_name, num_field_info, category_field_info, theme
                    )
                    
                    if chart_config:
                        charts.append(chart_config)
                        used_numerical_fields.append(num_field_info)
                        charts_created += 1
                        print(f"DEBUG: Successfully created aggregation chart: {chart_config.get('title', 'Unknown')}")
                    else:
                        print(f"DEBUG: Failed to create aggregation chart for {num_field_name}")
                
                # Mark category fields as used
                used_textual_fields.extend(suitable_category_fields)

            # Phase 2: Fill remaining slots with individual field charts
            remaining_slots = 6 - len(charts)
            print(f"DEBUG: Phase 2 - filling {remaining_slots} remaining slots with individual charts")
            
            if remaining_slots > 0:
                # First, add textual field charts for fields not used as categories
                unused_textual = [f for f in textual_fields if f not in used_textual_fields]
                for field_info in unused_textual:
                    if len(charts) >= 6:
                        break
                        
                    field_name = field_info.get("field_name", "unknown")
                    unique_count = field_info.get("unique_count", 0)
                    
                    # Determine chart type based on unique count
                    if unique_count <= 4:
                        chart_type = "pie"
                    elif unique_count <= 20:  # Allow bar charts for fields with up to 20 unique values
                        chart_type = "bar"
                    else:
                        continue  # Skip fields with too many unique values (>20)
                    
                    chart_config = self._create_count_chart_from_text_field(field_info, chart_type, theme)
                    if chart_config:
                        charts.append(chart_config)
                        used_textual_fields.append(field_info)
                
                # Then add numerical field histograms if no suitable category fields exist
                if not suitable_category_fields or len(charts) < 6:
                    unused_numerical = [f for f in numerical_fields if f not in used_numerical_fields]
                    for field_info in unused_numerical:
                        if len(charts) >= 6:
                            break
                            
                        # Create histogram chart for numerical field
                        chart_config = self._create_chart_from_field(field_info, theme)
                        if chart_config:
                            charts.append(chart_config)
                            used_numerical_fields.append(field_info)
            
            print(f"DEBUG: Final chart count: {len(charts)}")

            # Limit to 6 charts maximum
            charts = charts[:6]

            # Create layout
            layout = self._arrange_charts_in_layout(charts)

            # Build complete dashboard structure
            dashboard_data = {
                "layer_name": layer_name,
                "dashboard_title": f"{analysis_type.title()} Dashboard for {layer_name}",
                "theme": theme,
                "charts": charts,
                "layout": layout,
                "field_insights": field_insights,
                "generation_timestamp": self._get_timestamp(),
                "field_stats": {
                    "textual_fields_used": len(used_textual_fields),
                    "numerical_fields_used": len(used_numerical_fields),
                    "excluded_fields": len(excluded_fields),
                    "total_charts": len(charts)
                }
            }

            return {
                "success": True,
                "is_dashboard_update": True,
                "message": f"Enhanced dashboard generated for '{layer_name}' with {len(charts)} charts",
                "data": dashboard_data,
                "chart_count": len(charts)
            }

        except Exception as e:
            return {"success": False, "error": str(e)}

    def mission_generate_dashboard(self, params):
        """
        Generate a new dashboard for a layer.
        This function runs in ArcGIS Pro and has access to real layer data.
        """
        try:
            layer_name = params.get("layer_name") or params.get("layer")
            if not layer_name:
                return {"success": False, "error": "layer_name parameter is required"}
            
            # First analyze the layer fields to get real data
            analysis_result = self.analyze_layer_fields({"layer": layer_name})
            if not analysis_result.get("success"):
                return analysis_result
            
            # Generate dashboard using the field insights
            dashboard_params = {
                "layer_name": layer_name,
                "field_insights": analysis_result.get("field_insights", {}),
                "theme": params.get("theme", "default"),
                "analysis_type": params.get("analysis_type", "overview")
            }
            
            return self.generate_dashboard_for_target_layer(dashboard_params)
            
        except Exception as e:
            return {"success": False, "error": str(e)}

    def add_chart_to_dashboard(self, params: Dict) -> Dict:
        """
        Adds a new chart to the existing dashboard.
        This function computes data on the fly and returns a structure
        that the server can use to append to the dashboard JSON.
        Supports any layer type and handles Unicode text (Arabic, English, etc.)
        Enhanced to handle count charts and aggregation charts.
        """
        try:
            layer_name = params.get("layer_name")
            chart_type = params.get("chart_type", "bar")
            fields = params.get("fields", [])
            category_field = params.get("category_field")
            aggregation = params.get("aggregation", "SUM").lower()  # Convert to lowercase for consistent comparison
            title = params.get("title")
            theme = params.get("theme", "default")
            where_clause = params.get("where_clause")

            # Handle enhanced chart types
            is_count_chart = params.get("is_count_chart", False)
            is_aggregation_chart = params.get("is_aggregation_chart", False)

            if not layer_name:
                return {"success": False, "error": "layer_name is required"}

            # Handle count chart (textual field with unique value counts)
            if is_count_chart:
                if not fields:
                    return {"success": False, "error": "fields are required for count chart"}
                text_field = fields[0]  # First field is the textual field to count

                # Get frequency data for the textual field
                freq_result = self.get_values_frequency({
                    'layer_name': layer_name,
                    'field_name': text_field
                })

                if not freq_result.get('success'):
                    return freq_result

                frequency_data = freq_result.get('frequency', {})

                # Convert to chart data format
                chart_data = {
                    "labels": list(frequency_data.keys()),
                    "values": list(frequency_data.values())
                }

                # Create chart configuration
                chart_id = f"chart_{text_field}_count_{datetime.now().strftime('%Y%m%d%H%M%S')}"
                new_chart = {
                    "id": chart_id,
                    "title": title or f"Count of {text_field}",
                    "chart_type": chart_type,  # Use chart_type instead of type for consistency
                    "field_name": text_field,  # Use field_name instead of field for consistency
                    "primary_field": text_field,  # Add primary_field for backend processing
                    "data": chart_data,
                    "theme": theme,
                    "is_count_chart": True
                }

                layout_item = {
                    "id": chart_id,
                    "chart_type": chart_type,
                    "field_name": text_field,
                    "grid_area": f"chart-{chart_id}"
                }

                return {
                    "success": True,
                    "is_dashboard_update": True,
                    "is_chart_addition": True,
                    "new_chart": new_chart,
                    "layout_item": layout_item,
                    "message": f"Count chart for '{text_field}' prepared for addition to the dashboard."
                }

            # Handle aggregation chart (numerical field aggregated by textual field)
            if is_aggregation_chart:
                if not fields or not category_field:
                    return {"success": False, "error": "fields and category_field are required for aggregation chart"}
                numeric_field = fields[0]  # First field is the numerical field to aggregate

                # Use the existing aggregation logic but with specific parameters
                aggregation_params = {
                    "layer_name": layer_name,
                    "chart_type": chart_type,
                    "fields": [numeric_field],
                    "category_field": category_field,
                    "aggregation": aggregation,
                    "title": title,
                    "theme": theme,
                    "where_clause": where_clause
                }

                return self.add_chart_to_dashboard(aggregation_params)

            # Original logic for regular charts
            if not fields:
                return {"success": False, "error": "fields are required"}

            # Initialize numeric_fields for use in layout_item
            numeric_fields = fields

            # Validate layer exists and is accessible
            try:
                desc = arcpy.Describe(layer_name)
                if not desc:
                    return {"success": False, "error": f"Layer '{layer_name}' not found or not accessible"}
            except Exception as e:
                return {"success": False, "error": f"Cannot access layer '{layer_name}': {str(e)}"}

            # --- Data Aggregation using ArcPy ---
            if category_field:
                if category_field in fields:
                    numeric_fields = [f for f in fields if f != category_field]
                    if not numeric_fields:
                        return {"success": False, "error": "No numeric fields provided besides category_field"}
                else:
                    numeric_fields = fields
                cursor_fields = [category_field] + numeric_fields
                data = {}

                # Use proper encoding for Unicode support (Arabic, etc.)
                with arcpy.da.SearchCursor(layer_name, cursor_fields, where_clause) as cursor:
                    for row in cursor:
                        # Handle category field - ensure it's properly encoded
                        category = row[0]
                        if category is not None:
                            category = str(category)  # Convert to string to handle any data type
                        else:
                            category = "Null/Empty"

                        if category not in data:
                            data[category] = {}

                        for i, field in enumerate(numeric_fields):
                            value = row[i + 1]
                            if field not in data[category]:
                                data[category][field] = []
                            # Only add numeric values, skip nulls and non-numeric
                            if value is not None:
                                try:
                                    # Try to convert to float to handle various numeric types
                                    numeric_value = float(value)
                                    data[category][field].append(numeric_value)
                                except (ValueError, TypeError):
                                    # Skip non-numeric values
                                    pass

                if len(numeric_fields) == 1:
                    # Single series
                    chart_data = {"labels": [], "values": []}
                    for category, field_data in data.items():
                        chart_data["labels"].append(category)
                        values = field_data.get(numeric_fields[0], [])
                        if values:  # Only proceed if we have values
                            if aggregation == "sum":
                                chart_data["values"].append(sum(values))
                            elif aggregation in ["mean", "avg", "average"]:
                                chart_data["values"].append(statistics.mean(values))
                            elif aggregation == "count":
                                chart_data["values"].append(len(values))
                            elif aggregation == "min":
                                chart_data["values"].append(min(values))
                            elif aggregation == "max":
                                chart_data["values"].append(max(values))
                        else:
                            chart_data["values"].append(0)  # Default to 0 if no values
                else:
                    # Multiple series
                    chart_data = {"labels": [], "datasets": []}
                    # Get all categories
                    categories = list(data.keys())
                    chart_data["labels"] = categories

                    for field in numeric_fields:
                        dataset = {"label": field, "data": []}
                        for category in categories:
                            values = data.get(category, {}).get(field, [])
                            if values:  # Only proceed if we have values
                                if aggregation == "sum":
                                    dataset["data"].append(sum(values))
                                elif aggregation in ["mean", "avg", "average"]:
                                    dataset["data"].append(statistics.mean(values))
                                elif aggregation == "count":
                                    dataset["data"].append(len(values))
                                elif aggregation == "min":
                                    dataset["data"].append(min(values))
                                elif aggregation == "max":
                                    dataset["data"].append(max(values))
                            else:
                                dataset["data"].append(0)  # Default to 0 if no values
                        chart_data["datasets"].append(dataset)
            else:
                # No aggregation, just use field values directly
                chart_data = {"labels": [], "values": []}
                with arcpy.da.SearchCursor(layer_name, fields, where_clause) as cursor:
                    for row in cursor:
                        # Handle potential None values and ensure proper string conversion
                        label = row[0]
                        if label is not None:
                            label = str(label)  # Convert to string for Unicode support
                        else:
                            label = "Null/Empty"

                        chart_data["labels"].append(label)
                        # Use second field if available, otherwise use count
                        if len(row) > 1 and row[1] is not None and isinstance(row[1], (int, float)):
                            chart_data["values"].append(row[1])
                        else:
                            chart_data["values"].append(1)

            # --- Chart Configuration ---
            chart_id = f"chart_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            if len(numeric_fields) == 1:
                # Safe title creation to avoid recursion issues
                safe_title = title
                if not safe_title:
                    try:
                        field_name = str(numeric_fields[0]) if numeric_fields[0] is not None else "Field"
                        category_name = str(category_field) if category_field is not None else "Category"
                        agg_name = str(aggregation).title() if aggregation is not None else "Value"
                        safe_title = f"{agg_name} of {field_name} by {category_name}"
                    except:
                        safe_title = "Chart"
                
                new_chart = {
                    "id": chart_id,
                    "title": safe_title,
                    "chart_type": chart_type,  # Use chart_type instead of type for consistency
                    "field_name": numeric_fields[0],  # Use field_name instead of field for consistency
                    "primary_field": numeric_fields[0],  # Add primary_field for backend processing
                    "category_field": category_field,
                    "data": chart_data,
                    "theme": theme,
                }
            else:
                series = [{"field": f, "name": f} for f in numeric_fields]
                # Safe title creation to avoid recursion issues
                safe_title = title
                if not safe_title:
                    try:
                        field_names = ', '.join(str(f) for f in numeric_fields if f is not None)
                        category_name = str(category_field) if category_field is not None else "Category"
                        agg_name = str(aggregation).title() if aggregation is not None else "Value"
                        safe_title = f"{agg_name} of {field_names} by {category_name}"
                    except:
                        safe_title = "Multi-Series Chart"
                
                new_chart = {
                    "id": chart_id,
                    "title": safe_title,
                    "chart_type": chart_type,  # Use chart_type instead of type for consistency
                    "field_name": numeric_fields[0] if numeric_fields else fields[0],  # Use field_name for consistency
                    "primary_field": numeric_fields[0] if numeric_fields else fields[0],  # Add primary_field for backend processing
                    "category_field": category_field,
                    "series": series,
                    "fields": fields,
                    "data": chart_data,
                    "theme": theme,
                }

            # --- Layout Item Configuration ---
            # Safe field name extraction to avoid recursion issues
            safe_field_name = fields[0] if fields else "unknown"
            try:
                if numeric_fields and len(numeric_fields) > 0:
                    safe_field_name = str(numeric_fields[0])
                elif fields and len(fields) > 0:
                    safe_field_name = str(fields[0])
            except:
                safe_field_name = "chart_field"
            
            layout_item = {
                "id": chart_id,
                "chart_type": chart_type,
                "field_name": safe_field_name,
                # Default position, server might need to recalculate
                "grid_area": f"chart-{chart_id}"
            }

            return {
                "success": True,
                "is_dashboard_update": True,
                "is_chart_addition": True,
                "new_chart": new_chart,
                "layout_item": layout_item,
                "message": f"Chart '{title or 'New Chart'}' prepared for addition to the dashboard."
            }

        except Exception as e:
            return {"success": False, "error": str(e)}


class Toolbox(object):
    def __init__(self):
        self.label = "Progent Toolbox"
        self.alias = "progent"
        self.tools = [RunPythonCode]