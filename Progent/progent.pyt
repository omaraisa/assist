import arcpy
import os
import json
import math
import statistics

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
        arcpy.analysis.Buffer(layer_name, output_fc, f"{distance} {arcpy_units}")
        self._add_to_map(output_fc)
        return {"success": True, "output_layer": output_name, "output_path": output_fc}

    def select_by_attribute(self, params):
        layer_name = params.get("layer_name")
        where_clause = params.get("where_clause")
        selection_type = params.get("selection_type", "NEW_SELECTION")
        arcpy.SelectLayerByAttribute_management(layer_name, selection_type, where_clause)
        selected_count = int(arcpy.GetCount_management(layer_name)[0])
        return {"success": True, "selected_features": selected_count}

    def select_by_location(self, params):
        input_layer = params.get("input_layer")
        select_layer = params.get("select_layer")
        relationship = params.get("relationship", "INTERSECT")
        arcpy.SelectLayerByLocation_management(input_layer, relationship, select_layer)
        selected_count = int(arcpy.GetCount_management(input_layer)[0])
        return {"success": True, "selected_features": selected_count}

    def get_layer_summary(self, params):
        layer_name = params.get("layer_name")
        desc = arcpy.Describe(layer_name)
        feature_count = int(arcpy.GetCount_management(layer_name)[0])
        field_names = [f.name for f in arcpy.ListFields(layer_name)]
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
        for row in arcpy.da.SearchCursor(layer_name, ["SHAPE@AREA"]):
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
        for row in arcpy.da.SearchCursor(layer_name, ["SHAPE@LENGTH"]):
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
        for row in arcpy.da.SearchCursor(layer_name, ["OID@", "SHAPE@"]):
            if row[1]:
                centroid = row[1].centroid
                centroids.append({"id": row[0], "x": centroid.X, "y": centroid.Y})
        return {"success": True, "centroids": centroids}

    def spatial_join(self, params):
        target_layer = params.get("target_layer")
        join_layer = params.get("join_layer")
        output_name = f"{target_layer.replace(' ', '_')}_joined"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        output_path = os.path.join(aprx.defaultGeodatabase, output_name)
        output_path = arcpy.CreateUniqueName(output_path)
        arcpy.analysis.SpatialJoin(target_layer, join_layer, output_path)
        self._add_to_map(output_path)
        return {"success": True, "output_layer": output_name, "output_path": output_path}

    def clip_layer(self, params):
        input_layer = params.get("input_layer")
        clip_layer = params.get("clip_layer")
        output_name = f"{input_layer.replace(' ', '_')}_clipped"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        output_path = os.path.join(aprx.defaultGeodatabase, output_name)
        output_path = arcpy.CreateUniqueName(output_path)
        arcpy.analysis.Clip(input_layer, clip_layer, output_path)
        self._add_to_map(output_path)
        return {"success": True, "output_layer": output_name, "output_path": output_path}

    # Raster Functions
    def raster_to_point(self, params):
        in_raster = params.get("in_raster")
        output_name = f"{in_raster.replace(' ', '_')}_points"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_point_features = os.path.join(aprx.defaultGeodatabase, output_name)
        out_point_features = arcpy.CreateUniqueName(out_point_features)
        arcpy.conversion.RasterToPoint(in_raster, out_point_features)
        self._add_to_map(out_point_features)
        return {"success": True, "output_layer": out_point_features}

    def raster_to_polygon(self, params):
        in_raster = params.get("in_raster")
        output_name = f"{in_raster.replace(' ', '_')}_polygons"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_polygon_features = os.path.join(aprx.defaultGeodatabase, output_name)
        out_polygon_features = arcpy.CreateUniqueName(out_polygon_features)
        arcpy.conversion.RasterToPolygon(in_raster, out_polygon_features)
        self._add_to_map(out_polygon_features)
        return {"success": True, "output_layer": out_polygon_features}

    def raster_to_polyline(self, params):
        in_raster = params.get("in_raster")
        output_name = f"{in_raster.replace(' ', '_')}_polylines"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_polyline_features = os.path.join(aprx.defaultGeodatabase, output_name)
        out_polyline_features = arcpy.CreateUniqueName(out_polyline_features)
        arcpy.conversion.RasterToPolyline(in_raster, out_polyline_features)
        self._add_to_map(out_polyline_features)
        return {"success": True, "output_layer": out_polyline_features}

    def feature_to_raster(self, params):
        in_features = params.get("in_features")
        field = params.get("field")
        output_name = f"{in_features.replace(' ', '_')}_raster"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.conversion.FeatureToRaster(in_features, field, out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def polygon_to_raster(self, params):
        in_features = params.get("in_features")
        value_field = params.get("value_field")
        output_name = f"{in_features.replace(' ', '_')}_raster"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.conversion.PolygonToRaster(in_features, value_field, out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def point_to_raster(self, params):
        in_features = params.get("in_features")
        value_field = params.get("value_field")
        output_name = f"{in_features.replace(' ', '_')}_raster"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.conversion.PointToRaster(in_features, value_field, out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def idw_interpolation(self, params):
        in_point_features = params.get("in_point_features")
        z_field = params.get("z_field")
        output_name = f"{in_point_features.replace(' ', '_')}_idw"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.Idw(in_point_features, z_field).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def kriging_interpolation(self, params):
        in_point_features = params.get("in_point_features")
        z_field = params.get("z_field")
        output_name = f"{in_point_features.replace(' ', '_')}_kriging"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.Kriging(in_point_features, z_field).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def spline_interpolation(self, params):
        in_point_features = params.get("in_point_features")
        z_field = params.get("z_field")
        output_name = f"{in_point_features.replace(' ', '_')}_spline"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.Spline(in_point_features, z_field).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def natural_neighbor(self, params):
        in_point_features = params.get("in_point_features")
        z_field = params.get("z_field")
        output_name = f"{in_point_features.replace(' ', '_')}_natural_neighbor"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.NaturalNeighbor(in_point_features, z_field).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def euclidean_distance(self, params):
        in_source_data = params.get("in_source_data")
        output_name = f"euclidean_dist"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.EucDistance(in_source_data).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def euclidean_allocation(self, params):
        in_source_data = params.get("in_source_data")
        output_name = f"euclidean_alloc"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.EucAllocation(in_source_data).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def euclidean_direction(self, params):
        in_source_data = params.get("in_source_data")
        output_name = f"euclidean_dir"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.EucDirection(in_source_data).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def cost_distance(self, params):
        in_source_data = params.get("in_source_data")
        in_cost_raster = params.get("in_cost_raster")
        output_name = f"cost_dist"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.CostDistance(in_source_data, in_cost_raster).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def cost_allocation(self, params):
        in_source_data = params.get("in_source_data")
        in_cost_raster = params.get("in_cost_raster")
        output_name = f"cost_alloc"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.CostAllocation(in_source_data, in_cost_raster).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def cost_path(self, params):
        in_destination_data = params.get("in_destination_data")
        in_cost_distance_raster = params.get("in_cost_distance_raster")
        in_cost_backlink_raster = params.get("in_cost_backlink_raster")
        output_name = f"cost_path"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.CostPath(in_destination_data, in_cost_distance_raster, in_cost_backlink_raster).save(out_raster)
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
        output_name = f"extract_by_attr"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.ExtractByAttributes(in_raster, where_clause).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

    def mosaic_to_new_raster(self, params):
        input_rasters = params.get("input_rasters")
        output_location = params.get("output_location")
        raster_dataset_name_with_extension = params.get("raster_dataset_name_with_extension")
        pixel_type = params.get("pixel_type")
        number_of_bands = params.get("number_of_bands")
        arcpy.management.MosaicToNewRaster(input_rasters, output_location, raster_dataset_name_with_extension,
                                           pixel_type=pixel_type, number_of_bands=number_of_bands)
        out_path = os.path.join(output_location, raster_dataset_name_with_extension)
        self._add_to_map(out_path)
        return {"success": True, "output_raster": out_path}

    def combine_rasters(self, params):
        in_rasters = params.get("in_rasters")
        output_name = f"combined_raster"
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        out_raster = os.path.join(aprx.defaultGeodatabase, output_name)
        out_raster = arcpy.CreateUniqueName(out_raster)
        arcpy.sa.Combine(in_rasters).save(out_raster)
        self._add_to_map(out_raster)
        return {"success": True, "output_raster": out_raster}

class Toolbox(object):
    def __init__(self):
        self.label = "Progent Toolbox"
        self.alias = "progent"
        self.tools = [RunPythonCode]
