import arcpy
import os

class BusinessAnalystTools:
    """A collection of Business Analyst tools."""

    def _add_to_map(self, path):
        try:
            aprx = arcpy.mp.ArcGISProject('CURRENT')
            map_obj = aprx.activeMap
            if map_obj:
                map_obj.addDataFromPath(path)
        except Exception as e:
            print(f'Could not add {path} to map: {e}')

    def append_ba_report(self, params):
        """Appends a Business Analyst report to an existing report."""
        try:
            in_report_folder = params.get("in_report_folder")
            if in_report_folder is None: return {"success": False, "error": "in_report_folder parameter is required"}
            in_report_name = params.get("in_report_name")
            if in_report_name is None: return {"success": False, "error": "in_report_name parameter is required"}
            append_report_name = params.get("append_report_name")
            if append_report_name is None: return {"success": False, "error": "append_report_name parameter is required"}

            arcpy.ba.AppendBAReport(in_report_folder, in_report_name, append_report_name)

            return {"success": True, "message": f"Successfully appended {in_report_name} to {append_report_name}."}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def create_ba_report(self, params):
        """Creates a Business Analyst report in a specified format."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            report_type = params.get("report_type")
            if report_type is None: return {"success": False, "error": "report_type parameter is required"}
            out_report_folder = params.get("out_report_folder")
            if out_report_folder is None: return {"success": False, "error": "out_report_folder parameter is required"}
            report_format = params.get("report_format")
            if report_format is None: return {"success": False, "error": "report_format parameter is required"}
            report_name = params.get("report_name")
            if report_name is None: 
                report_name = f"{os.path.basename(in_features)}_{report_type}"
            
            arcpy.ba.CreateBAReport(in_features, report_type, out_report_folder, report_format, report_name)

            return {"success": True, "message": f"Successfully created {report_type} report for {in_features} in {out_report_folder}."}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def create_buffers_from_points(self, params):
        """Creates buffers around point features based on specified distances."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("CreateBuffersFromPoints_Output", aprx.defaultGeodatabase)
            distances = params.get("distances")
            if distances is None: return {"success": False, "error": "distances parameter is required"}
            units = params.get("units")
            if units is None: return {"success": False, "error": "units parameter is required"}
            dissolve_option = params.get("dissolve_option")
            dissolve_fields = params.get("dissolve_fields")

            arcpy.ba.CreateBuffersFromPoints(in_features, out_feature_class, distances, units, dissolve_option, dissolve_fields)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def create_drive_time_polygons(self, params):
        """Creates polygons representing areas reachable within a specified drive time or distance."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("CreateDriveTimePolygons_Output", aprx.defaultGeodatabase)
            travel_mode = params.get("travel_mode")
            if travel_mode is None: return {"success": False, "error": "travel_mode parameter is required"}
            break_values = params.get("break_values")
            if break_values is None: return {"success": False, "error": "break_values parameter is required"}
            break_units = params.get("break_units")
            if break_units is None: return {"success": False, "error": "break_units parameter is required"}
            time_of_day = params.get("time_of_day")
            time_zone = params.get("time_zone")
            dissolve_option = params.get("dissolve_option")
            dissolve_fields = params.get("dissolve_fields")

            arcpy.ba.CreateDriveTimePolygons(in_features, out_feature_class, travel_mode, break_values, break_units, time_of_day, time_zone, dissolve_option, dissolve_fields)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def create_trade_area_buffers(self, params):
        """Creates trade area buffers around point features based on specified distances."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("CreateTradeAreaBuffers_Output", aprx.defaultGeodatabase)
            distances = params.get("distances")
            if distances is None: return {"success": False, "error": "distances parameter is required"}
            units = params.get("units")
            if units is None: return {"success": False, "error": "units parameter is required"}
            dissolve_option = params.get("dissolve_option")
            dissolve_fields = params.get("dissolve_fields")

            arcpy.ba.CreateTradeAreaBuffers(in_features, out_feature_class, distances, units, dissolve_option, dissolve_fields)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def enrich_layer(self, params):
        """Enriches data by adding demographic and landscape facts about the people and places that surround or are inside data locations."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("EnrichLayer_Output", aprx.defaultGeodatabase)
            variables = params.get("variables")
            if variables is None: return {"success": False, "error": "variables parameter is required"}
            buffer_type = params.get("buffer_type")
            distance = params.get("distance")
            unit = params.get("unit")

            arcpy.ba.EnrichLayer(in_features, out_feature_class, variables, buffer_type, distance, unit)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def generate_points_from_lines(self, params):
        """Generates points along lines at a specified interval."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeneratePointsFromLines_Output", aprx.defaultGeodatabase)
            distance = params.get("distance")
            if distance is None: return {"success": False, "error": "distance parameter is required"}
            units = params.get("units")
            if units is None: return {"success": False, "error": "units parameter is required"}

            arcpy.ba.GeneratePointsFromLines(in_features, out_feature_class, distance, units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def generate_points_from_polygons(self, params):
        """Generates random points within polygons."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeneratePointsFromPolygons_Output", aprx.defaultGeodatabase)
            number_of_points = params.get("number_of_points")
            if number_of_points is None: return {"success": False, "error": "number_of_points parameter is required"}

            arcpy.ba.GeneratePointsFromPolygons(in_features, out_feature_class, number_of_points)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def generate_points_from_polylines(self, params):
        """Generates random points along polylines."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeneratePointsFromPolylines_Output", aprx.defaultGeodatabase)
            number_of_points = params.get("number_of_points")
            if number_of_points is None: return {"success": False, "error": "number_of_points parameter is required"}

            arcpy.ba.GeneratePointsFromPolylines(in_features, out_feature_class, number_of_points)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def generate_points_from_rasters(self, params):
        """Generates random points from rasters."""
        try:
            in_raster = params.get("in_raster")
            if in_raster is None: return {"success": False, "error": "in_raster parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeneratePointsFromRasters_Output", aprx.defaultGeodatabase)
            number_of_points = params.get("number_of_points")
            if number_of_points is None: return {"success": False, "error": "number_of_points parameter is required"}

            arcpy.ba.GeneratePointsFromRasters(in_raster, out_feature_class, number_of_points)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def generate_points_from_table(self, params):
        """Generates points from a table based on x,y coordinates."""
        try:
            in_table = params.get("in_table")
            if in_table is None: return {"success": False, "error": "in_table parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeneratePointsFromTable_Output", aprx.defaultGeodatabase)
            x_field = params.get("x_field")
            if x_field is None: return {"success": False, "error": "x_field parameter is required"}
            y_field = params.get("y_field")
            if y_field is None: return {"success": False, "error": "y_field parameter is required"}
            z_field = params.get("z_field")
            coordinate_system = params.get("coordinate_system")

            arcpy.ba.GeneratePointsFromTable(in_table, out_feature_class, x_field, y_field, z_field, coordinate_system)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def generate_points_from_xy_table(self, params):
        """Generates points from an XY table."""
        try:
            in_table = params.get("in_table")
            if in_table is None: return {"success": False, "error": "in_table parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeneratePointsFromXYTable_Output", aprx.defaultGeodatabase)
            x_field = params.get("x_field")
            if x_field is None: return {"success": False, "error": "x_field parameter is required"}
            y_field = params.get("y_field")
            if y_field is None: return {"success": False, "error": "y_field parameter is required"}
            z_field = params.get("z_field")
            coordinate_system = params.get("coordinate_system")

            arcpy.ba.GeneratePointsFromXYTable(in_table, out_feature_class, x_field, y_field, z_field, coordinate_system)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def generate_points_from_xyz_table(self, params):
        """Generates points from an XYZ table."""
        try:
            in_table = params.get("in_table")
            if in_table is None: return {"success": False, "error": "in_table parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeneratePointsFromXYZTable_Output", aprx.defaultGeodatabase)
            x_field = params.get("x_field")
            if x_field is None: return {"success": False, "error": "x_field parameter is required"}
            y_field = params.get("y_field")
            if y_field is None: return {"success": False, "error": "y_field parameter is required"}
            z_field = params.get("z_field")
            if z_field is None: return {"success": False, "error": "z_field parameter is required"}
            coordinate_system = params.get("coordinate_system")

            arcpy.ba.GeneratePointsFromXYZTable(in_table, out_feature_class, x_field, y_field, z_field, coordinate_system)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def generate_trade_area_buffers(self, params):
        """Generates trade area buffers around point features based on specified distances."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GenerateTradeAreaBuffers_Output", aprx.defaultGeodatabase)
            distances = params.get("distances")
            if distances is None: return {"success": False, "error": "distances parameter is required"}
            units = params.get("units")
            if units is None: return {"success": False, "error": "units parameter is required"}
            dissolve_option = params.get("dissolve_option")
            dissolve_fields = params.get("dissolve_fields")

            arcpy.ba.GenerateTradeAreaBuffers(in_features, out_feature_class, distances, units, dissolve_option, dissolve_fields)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_polygons(self, params):
        """Converts geocoding points to polygons."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPolygons_Output", aprx.defaultGeodatabase)
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}

            arcpy.ba.GeocodingPointsToPolygons(in_features, out_feature_class, search_distance, search_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_polylines(self, params):
        """Converts geocoding points to polylines."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPolylines_Output", aprx.defaultGeodatabase)
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}

            arcpy.ba.GeocodingPointsToPolylines(in_features, out_feature_class, search_distance, search_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_points(self, params):
        """Converts geocoding points to points."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPoints_Output", aprx.defaultGeodatabase)
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}

            arcpy.ba.GeocodingPointsToPoints(in_features, out_feature_class, search_distance, search_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_polygons_by_attribute(self, params):
        """Converts geocoding points to polygons by attribute."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPolygonsByAttribute_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}

            arcpy.ba.GeocodingPointsToPolygonsByAttribute(in_features, out_feature_class, group_field, search_distance, search_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_polylines_by_attribute(self, params):
        """Converts geocoding points to polylines by attribute."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPolylinesByAttribute_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}

            arcpy.ba.GeocodingPointsToPolylinesByAttribute(in_features, out_feature_class, group_field, search_distance, search_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_points_by_attribute(self, params):
        """Converts geocoding points to points by attribute."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPointsByAttribute_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}

            arcpy.ba.GeocodingPointsToPointsByAttribute(in_features, out_feature_class, group_field, search_distance, search_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_polylines_by_attribute_with_distance(self, params):
        """Converts geocoding points to polylines by attribute with distance."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPolylinesByAttributeWithDistance_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}

            arcpy.ba.GeocodingPointsToPolylinesByAttributeWithDistance(in_features, out_feature_class, group_field, search_distance, search_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_points_by_attribute_with_distance(self, params):
        """Converts geocoding points to points by attribute with distance."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPointsByAttributeWithDistance_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}

            arcpy.ba.GeocodingPointsToPointsByAttributeWithDistance(in_features, out_feature_class, group_field, search_distance, search_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_polygons_by_attribute_with_distance(self, params):
        """Converts geocoding points to polygons by attribute with distance."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPolygonsByAttributeWithDistance_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}

            arcpy.ba.GeocodingPointsToPolygonsByAttributeWithDistance(in_features, out_feature_class, group_field, search_distance, search_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_polylines_by_attribute_with_distance_and_time(self, params):
        """Converts geocoding points to polylines by attribute with distance and time."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPolylinesByAttributeWithDistanceAndTime_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}
            time_field = params.get("time_field")
            if time_field is None: return {"success": False, "error": "time_field parameter is required"}
            time_units = params.get("time_units")
            if time_units is None: return {"success": False, "error": "time_units parameter is required"}

            arcpy.ba.GeocodingPointsToPolylinesByAttributeWithDistanceAndTime(in_features, out_feature_class, group_field, search_distance, search_units, time_field, time_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_points_by_attribute_with_distance_and_time(self, params):
        """Converts geocoding points to points by attribute with distance and time."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPointsByAttributeWithDistanceAndTime_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}
            time_field = params.get("time_field")
            if time_field is None: return {"success": False, "error": "time_field parameter is required"}
            time_units = params.get("time_units")
            if time_units is None: return {"success": False, "error": "time_units parameter is required"}

            arcpy.ba.GeocodingPointsToPointsByAttributeWithDistanceAndTime(in_features, out_feature_class, group_field, search_distance, search_units, time_field, time_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_polygons_by_attribute_with_distance_and_time(self, params):
        """Converts geocoding points to polygons by attribute with distance and time."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPolygonsByAttributeWithDistanceAndTime_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}
            time_field = params.get("time_field")
            if time_field is None: return {"success": False, "error": "time_field parameter is required"}
            time_units = params.get("time_units")
            if time_units is None: return {"success": False, "error": "time_units parameter is required"}

            arcpy.ba.GeocodingPointsToPolygonsByAttributeWithDistanceAndTime(in_features, out_feature_class, group_field, search_distance, search_units, time_field, time_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_polylines_by_attribute_with_distance_and_time_and_speed(self, params):
        """Converts geocoding points to polylines by attribute with distance, time, and speed."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPolylinesByAttributeWithDistanceAndTimeAndSpeed_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}
            time_field = params.get("time_field")
            if time_field is None: return {"success": False, "error": "time_field parameter is required"}
            time_units = params.get("time_units")
            if time_units is None: return {"success": False, "error": "time_units parameter is required"}
            speed_field = params.get("speed_field")
            if speed_field is None: return {"success": False, "error": "speed_field parameter is required"}
            speed_units = params.get("speed_units")
            if speed_units is None: return {"success": False, "error": "speed_units parameter is required"}

            arcpy.ba.GeocodingPointsToPolylinesByAttributeWithDistanceAndTimeAndSpeed(in_features, out_feature_class, group_field, search_distance, search_units, time_field, time_units, speed_field, speed_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_points_by_attribute_with_distance_and_time_and_speed(self, params):
        """Converts geocoding points to points by attribute with distance, time, and speed."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPointsByAttributeWithDistanceAndTimeAndSpeed_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}
            time_field = params.get("time_field")
            if time_field is None: return {"success": False, "error": "time_field parameter is required"}
            time_units = params.get("time_units")
            if time_units is None: return {"success": False, "error": "time_units parameter is required"}
            speed_field = params.get("speed_field")
            if speed_field is None: return {"success": False, "error": "speed_field parameter is required"}
            speed_units = params.get("speed_units")
            if speed_units is None: return {"success": False, "error": "speed_units parameter is required"}

            arcpy.ba.GeocodingPointsToPointsByAttributeWithDistanceAndTimeAndSpeed(in_features, out_feature_class, group_field, search_distance, search_units, time_field, time_units, speed_field, speed_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_polygons_by_attribute_with_distance_and_time_and_speed(self, params):
        """Converts geocoding points to polygons by attribute with distance, time, and speed."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPolygonsByAttributeWithDistanceAndTimeAndSpeed_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}
            time_field = params.get("time_field")
            if time_field is None: return {"success": False, "error": "time_field parameter is required"}
            time_units = params.get("time_units")
            if time_units is None: return {"success": False, "error": "time_units parameter is required"}
            speed_field = params.get("speed_field")
            if speed_field is None: return {"success": False, "error": "speed_field parameter is required"}
            speed_units = params.get("speed_units")
            if speed_units is None: return {"success": False, "error": "speed_units parameter is required"}

            arcpy.ba.GeocodingPointsToPolygonsByAttributeWithDistanceAndTimeAndSpeed(in_features, out_feature_class, group_field, search_distance, search_units, time_field, time_units, speed_field, speed_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_polylines_by_attribute_with_distance_and_time_and_speed_and_cost(self, params):
        """Converts geocoding points to polylines by attribute with distance, time, speed, and cost."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPolylinesByAttributeWithDistanceAndTimeAndSpeedAndCost_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}
            time_field = params.get("time_field")
            if time_field is None: return {"success": False, "error": "time_field parameter is required"}
            time_units = params.get("time_units")
            if time_units is None: return {"success": False, "error": "time_units parameter is required"}
            speed_field = params.get("speed_field")
            if speed_field is None: return {"success": False, "error": "speed_field parameter is required"}
            speed_units = params.get("speed_units")
            if speed_units is None: return {"success": False, "error": "speed_units parameter is required"}
            cost_field = params.get("cost_field")
            if cost_field is None: return {"success": False, "error": "cost_field parameter is required"}
            cost_units = params.get("cost_units")
            if cost_units is None: return {"success": False, "error": "cost_units parameter is required"}

            arcpy.ba.GeocodingPointsToPolylinesByAttributeWithDistanceAndTimeAndSpeedAndCost(in_features, out_feature_class, group_field, search_distance, search_units, time_field, time_units, speed_field, speed_units, cost_field, cost_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_points_by_attribute_with_distance_and_time_and_speed_and_cost(self, params):
        """Converts geocoding points to points by attribute with distance, time, speed, and cost."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPointsByAttributeWithDistanceAndTimeAndSpeedAndCost_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}
            time_field = params.get("time_field")
            if time_field is None: return {"success": False, "error": "time_field parameter is required"}
            time_units = params.get("time_units")
            if time_units is None: return {"success": False, "error": "time_units parameter is required"}
            speed_field = params.get("speed_field")
            if speed_field is None: return {"success": False, "error": "speed_field parameter is required"}
            speed_units = params.get("speed_units")
            if speed_units is None: return {"success": False, "error": "speed_units parameter is required"}
            cost_field = params.get("cost_field")
            if cost_field is None: return {"success": False, "error": "cost_field parameter is required"}
            cost_units = params.get("cost_units")
            if cost_units is None: return {"success": False, "error": "cost_units parameter is required"}

            arcpy.ba.GeocodingPointsToPointsByAttributeWithDistanceAndTimeAndSpeedAndCost(in_features, out_feature_class, group_field, search_distance, search_units, time_field, time_units, speed_field, speed_units, cost_field, cost_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_polygons_by_attribute_with_distance_and_time_and_speed_and_cost(self, params):
        """Converts geocoding points to polygons by attribute with distance, time, speed, and cost."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPolygonsByAttributeWithDistanceAndTimeAndSpeedAndCost_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}
            time_field = params.get("time_field")
            if time_field is None: return {"success": False, "error": "time_field parameter is required"}
            time_units = params.get("time_units")
            if time_units is None: return {"success": False, "error": "time_units parameter is required"}
            speed_field = params.get("speed_field")
            if speed_field is None: return {"success": False, "error": "speed_field parameter is required"}
            speed_units = params.get("speed_units")
            if speed_units is None: return {"success": False, "error": "speed_units parameter is required"}
            cost_field = params.get("cost_field")
            if cost_field is None: return {"success": False, "error": "cost_field parameter is required"}
            cost_units = params.get("cost_units")
            if cost_units is None: return {"success": False, "error": "cost_units parameter is required"}

            arcpy.ba.GeocodingPointsToPolygonsByAttributeWithDistanceAndTimeAndSpeedAndCost(in_features, out_feature_class, group_field, search_distance, search_units, time_field, time_units, speed_field, speed_units, cost_field, cost_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_polylines_by_attribute_with_distance_and_time_and_speed_and_cost_and_impedance(self, params):
        """Converts geocoding points to polylines by attribute with distance, time, speed, and cost, and impedance."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPolylinesByAttributeWithDistanceAndTimeAndSpeedAndCostAndImpedance_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}
            time_field = params.get("time_field")
            if time_field is None: return {"success": False, "error": "time_field parameter is required"}
            time_units = params.get("time_units")
            if time_units is None: return {"success": False, "error": "time_units parameter is required"}
            speed_field = params.get("speed_field")
            if speed_field is None: return {"success": False, "error": "speed_field parameter is required"}
            speed_units = params.get("speed_units")
            if speed_units is None: return {"success": False, "error": "speed_units parameter is required"}
            cost_field = params.get("cost_field")
            if cost_field is None: return {"success": False, "error": "cost_field parameter is required"}
            cost_units = params.get("cost_units")
            if cost_units is None: return {"success": False, "error": "cost_units parameter is required"}
            impedance_field = params.get("impedance_field")
            if impedance_field is None: return {"success": False, "error": "impedance_field parameter is required"}
            impedance_units = params.get("impedance_units")
            if impedance_units is None: return {"success": False, "error": "impedance_units parameter is required"}

            arcpy.ba.GeocodingPointsToPolylinesByAttributeWithDistanceAndTimeAndSpeedAndCostAndImpedance(in_features, out_feature_class, group_field, search_distance, search_units, time_field, time_units, speed_field, speed_units, cost_field, cost_units, impedance_field, impedance_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_points_by_attribute_with_distance_and_time_and_speed_and_cost_and_impedance(self, params):
        """Converts geocoding points to points by attribute with distance, time, speed, and cost, and impedance."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPointsByAttributeWithDistanceAndTimeAndSpeedAndCostAndImpedance_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}
            time_field = params.get("time_field")
            if time_field is None: return {"success": False, "error": "time_field parameter is required"}
            time_units = params.get("time_units")
            if time_units is None: return {"success": False, "error": "time_units parameter is required"}
            speed_field = params.get("speed_field")
            if speed_field is None: return {"success": False, "error": "speed_field parameter is required"}
            speed_units = params.get("speed_units")
            if speed_units is None: return {"success": False, "error": "speed_units parameter is required"}
            cost_field = params.get("cost_field")
            if cost_field is None: return {"success": False, "error": "cost_field parameter is required"}
            cost_units = params.get("cost_units")
            if cost_units is None: return {"success": False, "error": "cost_units parameter is required"}
            impedance_field = params.get("impedance_field")
            if impedance_field is None: return {"success": False, "error": "impedance_field parameter is required"}
            impedance_units = params.get("impedance_units")
            if impedance_units is None: return {"success": False, "error": "impedance_units parameter is required"}

            arcpy.ba.GeocodingPointsToPointsByAttributeWithDistanceAndTimeAndSpeedAndCostAndImpedance(in_features, out_feature_class, group_field, search_distance, search_units, time_field, time_units, speed_field, speed_units, cost_field, cost_units, impedance_field, impedance_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def geocoding_points_to_polygons_by_attribute_with_distance_and_time_and_speed_and_cost_and_impedance(self, params):
        """Converts geocoding points to polygons by attribute with distance, time, speed, and cost, and impedance."""
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None: 
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GeocodingPointsToPolygonsByAttributeWithDistanceAndTimeAndSpeedAndCostAndImpedance_Output", aprx.defaultGeodatabase)
            group_field = params.get("group_field")
            if group_field is None: return {"success": False, "error": "group_field parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None: return {"success": False, "error": "search_distance parameter is required"}
            search_units = params.get("search_units")
            if search_units is None: return {"success": False, "error": "search_units parameter is required"}
            time_field = params.get("time_field")
            if time_field is None: return {"success": False, "error": "time_field parameter is required"}
            time_units = params.get("time_units")
            if time_units is None: return {"success": False, "error": "time_units parameter is required"}
            speed_field = params.get("speed_field")
            if speed_field is None: return {"success": False, "error": "speed_field parameter is required"}
            speed_units = params.get("speed_units")
            if speed_units is None: return {"success": False, "error": "speed_units parameter is required"}
            cost_field = params.get("cost_field")
            if cost_field is None: return {"success": False, "error": "cost_field parameter is required"}
            cost_units = params.get("cost_units")
            if cost_units is None: return {"success": False, "error": "cost_units parameter is required"}
            impedance_field = params.get("impedance_field")
            if impedance_field is None: return {"success": False, "error": "impedance_field parameter is required"}
            impedance_units = params.get("impedance_units")
            if impedance_units is None: return {"success": False, "error": "impedance_units parameter is required"}

            arcpy.ba.GeocodingPointsToPolygonsByAttributeWithDistanceAndTimeAndSpeedAndCostAndImpedance(in_features, out_feature_class, group_field, search_distance, search_units, time_field, time_units, speed_field, speed_units, cost_field, cost_units, impedance_field, impedance_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}
