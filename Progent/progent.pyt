import arcpy
import os

class RunPythonCode(object):
    def __init__(self):
        self.label = "RunPythonCode"
        self.description = "Test access to ArcGIS Pro's CURRENT project."
        # Ensure the tool runs in-process so arcpy.mp.ArcGISProject('CURRENT') is valid
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Define two string parameters for function name and parameters JSON
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
        # This tool must run in the ArcGIS Pro process so 'CURRENT' works
        try:
            import json, os, sys
            
            # Debug: log parameter information
            messages.addMessage(f"Parameters received: {len(parameters) if parameters else 0}")
            
            # Read parameters - they should now be properly defined
            function_name = parameters[0].valueAsText if parameters and len(parameters) > 0 else None
            parameters_json = parameters[1].valueAsText if parameters and len(parameters) > 1 else None
            
            messages.addMessage(f"Function name: {function_name}")
            messages.addMessage(f"Parameters JSON: {parameters_json}")
            
            # If no valid function name, show default message
            if not function_name or str(function_name).strip() == "":
                messages.addMessage("No function name provided or function name is empty")
                messages.addMessage("Available functions: create_buffer, select_by_attribute, get_layer_summary, etc.")
                print("Incoming Code is not handled correctly")
                messages.addMessage("Incoming Code is not handled correctly")
                return
            
            # Parse parameters JSON
            try:
                params = json.loads(parameters_json) if parameters_json else {}
                messages.addMessage(f"Parsed params: {params}")
            except Exception as json_error:
                messages.addMessage(f"JSON parsing error: {json_error}")
                params = {}
            
            # Execute the spatial function
            messages.addMessage(f"Executing function: {function_name} with parameters: {params}")
            
            result = self.execute_spatial_function(function_name, params, messages)
            
            if result:
                messages.addMessage(json.dumps({"status": "success", "data": result}))
            else:
                messages.addMessage(json.dumps({"status": "error", "message": f"Function {function_name} not implemented or failed"}))

        except Exception as e:
            import traceback, json
            tb = traceback.format_exc()
            messages.addMessage(f"Top-level error: {str(e)}")
            messages.addMessage(f"Traceback: {tb}")
            messages.addMessage(json.dumps({"status": "error", "message": str(e), "trace": tb}))
    
    def execute_spatial_function(self, function_name, params, messages):
        """Execute any spatial function with the same logic as spatial_functions.py"""
        try:
            if function_name == "create_buffer":
                return self.create_buffer(params)
            elif function_name == "select_by_attribute":
                return self.select_by_attribute(params)
            elif function_name == "select_by_location":
                return self.select_by_location(params)
            elif function_name == "get_layer_summary":
                return self.get_layer_summary(params)
            elif function_name == "calculate_area":
                return self.calculate_area(params)
            elif function_name == "calculate_length":
                return self.calculate_length(params)
            elif function_name == "get_centroid":
                return self.get_centroid(params)
            elif function_name == "spatial_join":
                return self.spatial_join(params)
            elif function_name == "clip_layer":
                return self.clip_layer(params)
            elif function_name == "get_current_project_path":
                return self.get_current_project_path(params)
            elif function_name == "get_default_db_path":
                return self.get_default_db_path(params)
            elif function_name == "get_map_layers_info":
                return self.get_map_layers_info(params)
            elif function_name == "get_field_statistics":
                return self.get_field_statistics(params)
            elif function_name == "get_coordinate_system":
                return self.get_coordinate_system(params)
            elif function_name == "analyze_layer_fields":
                return self.analyze_layer_fields(params)
            else:
                return None
        except Exception as e:
            messages.addMessage(f"Error in {function_name}: {str(e)}")
            return None
    
    def create_buffer(self, params):
        """Create buffer around features"""
        layer_name = params.get("layer_name", "")
        distance = params.get("distance", 500)
        units = params.get("units", "meters")
        
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
        unit_mapping = {"meters": "METERS", "kilometers": "KILOMETERS", "feet": "FEET", "miles": "MILES"}
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
        
        return {
            "function_executed": "create_buffer",
            "layer_name": layer_name,
            "success": True,
            "output_layer": output_name,
            "output_path": output_fc,
            "buffer_distance": distance,
            "buffer_units": units
        }
    
    def select_by_attribute(self, params):
        """Execute attribute-based selection"""
        layer_name = params.get("layer_name", "")
        where_clause = params.get("where_clause", "")
        selection_type = params.get("selection_type", "NEW_SELECTION")
        
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
        
        return {
            "function_executed": "select_by_attribute",
            "layer_name": layer_name,
            "selected_features": selected_count,
            "success": True
        }
    
    def get_current_project_path(self, params):
        """Get the current ArcGIS Pro project path"""
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        path = aprx.filePath
        return {
            "function_executed": "get_current_project_path",
            "success": True,
            "project_path": path
        }
    
    def get_map_layers_info(self, params):
        """Get information about all layers in the current ArcGIS Pro map"""
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        map_obj = aprx.activeMap
        layers_info = []
        
        for lyr in map_obj.listLayers():
            layers_info.append({
                "name": lyr.name,
                "visible": lyr.visible,
                "type": "Feature Layer" if lyr.isFeatureLayer else "Other"
            })
        
        return {
            "function_executed": "get_map_layers_info",
            "success": True,
            "layers": layers_info
        }
    
    def select_by_location(self, params):
        """Execute spatial selection"""
        input_layer = params.get("input_layer", "")
        select_layer = params.get("select_layer", "")
        relationship = params.get("relationship", "INTERSECT")
        
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
        
        return {
            "function_executed": "select_by_location",
            "input_layer": input_layer,
            "select_layer": select_layer,
            "relationship": relationship,
            "selected_features": selected_count,
            "success": True
        }
    
    def get_layer_summary(self, params):
        """Get comprehensive layer summary"""
        layer_name = params.get("layer_name", "")
        
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
                "length": field.length
            })
        
        return {
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
    
    def get_field_statistics(self, params):
        """Calculate field statistics"""
        layer_name = params.get("layer_name", "")
        field_name = params.get("field_name", "")
        where_clause = params.get("where_clause", None)
        
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
            return {"success": False, "error": f"Field {field_name} not found in layer"}
        
        # Collect values
        values = []
        for row in arcpy.da.SearchCursor(lyr, [field_name], where_clause):
            if row[0] is not None:
                values.append(row[0])
        
        if not values:
            return {"success": False, "error": "No values found"}
        
        # Calculate statistics
        import statistics
        return {
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
    
    def get_default_db_path(self, params):
        """Get the default geodatabase path for the current ArcGIS Pro project"""
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        default_gdb = aprx.defaultGeodatabase
        return {
            "function_executed": "get_default_db_path",
            "success": True,
            "default_geodatabase": default_gdb
        }
    
    def get_coordinate_system(self, params):
        """Gets coordinate system information for a layer"""
        layer_name = params.get("layer_name", "")
        
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
        
        return {
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
    
    def analyze_layer_fields(self, params):
        """Analyze all fields in a layer to understand their characteristics"""
        layer_name = params.get("layer_name", "")
        
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        map_obj = aprx.activeMap
        
        target_layer = None
        for lyr in map_obj.listLayers():
            if lyr.name == layer_name:
                target_layer = lyr
                break
        
        if not target_layer:
            return {"success": False, "error": f"Layer {layer_name} not found"}
        
        if not target_layer.isFeatureLayer:
            return {"success": False, "error": f"Layer {layer_name} is not a feature layer"}
        
        # Get total feature count
        total_count = int(arcpy.GetCount_management(target_layer)[0])
        if total_count == 0:
            return {"success": False, "error": f"Layer {layer_name} has no features"}
        
        fields = arcpy.ListFields(target_layer)
        field_analysis = {}
        
        for field in fields:
            # Skip system fields
            if field.name.upper() in ['OBJECTID', 'SHAPE', 'SHAPE_LENGTH', 'SHAPE_AREA', 'GLOBALID']:
                continue
            
            try:
                # Basic field info
                field_info = {
                    "name": field.name,
                    "type": field.type,
                    "length": field.length,
                    "nullable": field.isNullable
                }
                
                # Sample some values to understand the data
                values = []
                null_count = 0
                
                with arcpy.da.SearchCursor(target_layer, [field.name]) as cursor:
                    for i, row in enumerate(cursor):
                        if i >= 1000:  # Limit sample size
                            break
                        if row[0] is None:
                            null_count += 1
                        else:
                            values.append(row[0])
                
                # Calculate basic statistics
                unique_values = list(set(values)) if values else []
                
                field_info.update({
                    "sample_count": len(values),
                    "null_count": null_count,
                    "unique_count": len(unique_values),
                    "sample_values": unique_values[:10] if unique_values else []
                })
                
                field_analysis[field.name] = field_info
            except Exception as e:
                field_analysis[field.name] = {"error": str(e)}
        
        return {
            "success": True,
            "layer_name": layer_name,
            "total_features": total_count,
            "fields_analyzed": len(field_analysis),
            "field_insights": field_analysis
        }


class Toolbox(object):
    def __init__(self):
        self.label = "Progent Toolbox"
        self.alias = "progent"
        self.tools = [RunPythonCode]
