# Generated ArcGIS Pro 3d-analyst Progent Functions
# Generated on 2025-10-01T14:32:45.604280
# Total tools: 40

import arcpy
import os

class GeneratedSpatialFunctions:
    """Generated spatial analysis functions in progent.pyt format"""

    def _add_to_map(self, path):
        try:
            aprx = arcpy.mp.ArcGISProject('CURRENT')
            map_obj = aprx.activeMap
            map_obj.addDataFromPath(path)
        except Exception as e:
            print(f'Could not add {path} to map: {e}')

    def enclose_multipatch(self, params):
        """Enclose Multipatch

Creates  closed multipatch features from open multipatch features.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "grid_size": <Double>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        grid_size = params.get("grid_size")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Enclose_Multipatch"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Enclose Multipatch
            arcpy.EncloseMultipatch(in_features, out_feature_class, grid_size)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def enforce_river_monotonicity(self, params):
        """Enforce River Monotonicity

Creates height adjusted breaklines from 3D polygons representing river banks.

        params: {"in_rivers": <Feature Layer>, "in_flow_direction": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rivers = params.get("in_rivers")
        if in_rivers is None:
            return {"success": False, "error": "in_rivers parameter is required"}
        in_flow_direction = params.get("in_flow_direction")
        if in_flow_direction is None:
            return {"success": False, "error": "in_flow_direction parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        max_sample_distance = params.get("max_sample_distance")
        simplification_tolerance = params.get("simplification_tolerance")

            # Generate output name and path
            output_name = f"{in_rivers.replace(' ', '_')}_Enforce_River_Monotonicity"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Enforce River Monotonicity
            arcpy.EnforceRiverMonotonicity(in_rivers, in_flow_direction, out_feature_class, max_sample_distance, simplification_tolerance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_points_along_3d_lines(self, params):
        """Generate Points Along 3D Lines

Creates 3D point features along 3D lines using three-dimensional distances.

        params: {"in_features": <Feature Layer>, "out_features": <Feature Class>, "point_placement": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_features = params.get("out_features")
        if out_features is None:
            return {"success": False, "error": "out_features parameter is required"}
        point_placement = params.get("point_placement")
        distance = params.get("distance")
        percentage = params.get("percentage")
        include_end_points = params.get("include_end_points")
        add_chainage_fields = params.get("add_chainage_fields")
        distance_field = params.get("distance_field")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Generate_Points_Along_3D_Lines"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Points Along 3D Lines
            arcpy.GeneratePointsAlong3DLines(in_features, out_features, point_placement, distance, percentage, include_end_points, add_chainage_fields, distance_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def is_closed_3d(self, params):
        """Is Closed 3D

Evaluates multipatch features to determine whether each feature completely encloses a volume of space.

        params: {"in_feature_class": <Feature Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_feature_class = params.get("in_feature_class")
        if in_feature_class is None:
            return {"success": False, "error": "in_feature_class parameter is required"}

            # Generate output name and path
            output_name = f"{in_feature_class.replace(' ', '_')}_Is_Closed_3D"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Is Closed 3D
            arcpy.IsClosed3D(in_feature_class)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def simplify_3d_line(self, params):
        """Simplify 3D Line

Generalizes 3D line features to reduce the overall number of vertices while approximating the original shape in horizontal and vertical directions within a specified tolerance.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "tolerance": <Linear Unit>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        tolerance = params.get("tolerance")
        if tolerance is None:
            return {"success": False, "error": "tolerance parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Simplify_3D_Line"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Simplify 3D Line
            arcpy.Simplify3DLine(in_features, out_feature_class, tolerance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def ascii_3d_to_feature_class(self, params):
        """ASCII 3D To Feature Class

Imports 3D features from one or more ASCII files stored in XYZ, XYZI, or GENERATE formats into a new feature class.

        params: {"input": <Folder; File>, "in_file_type": <String>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input = params.get("input")
        if input is None:
            return {"success": False, "error": "input parameter is required"}
        in_file_type = params.get("in_file_type")
        if in_file_type is None:
            return {"success": False, "error": "in_file_type parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        out_geometry_type = params.get("out_geometry_type")
        if out_geometry_type is None:
            return {"success": False, "error": "out_geometry_type parameter is required"}
        z_factor = params.get("z_factor")
        input_coordinate_system = params.get("input_coordinate_system")
        average_point_spacing = params.get("average_point_spacing")
        file_suffix = params.get("file_suffix")
        decimal_separator = params.get("decimal_separator")

            # Generate output name and path
            output_name = f"{input.replace(' ', '_')}_ASCII_3D_To_Feature_Class"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute ASCII 3D To Feature Class
            arcpy.ASCII3DToFeatureClass(input, in_file_type, out_feature_class, out_geometry_type, z_factor, input_coordinate_system, average_point_spacing, file_suffix, decimal_separator)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def feature_class_z_to_ascii(self, params):
        """Feature Class Z To ASCII

Exports 3D features to ASCII text files storing GENERATE, XYZ, or profile data.

        params: {"in_feature_class": <Feature Layer>, "output_location": <Folder>, "out_file": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_feature_class = params.get("in_feature_class")
        if in_feature_class is None:
            return {"success": False, "error": "in_feature_class parameter is required"}
        output_location = params.get("output_location")
        if output_location is None:
            return {"success": False, "error": "output_location parameter is required"}
        out_file = params.get("out_file")
        if out_file is None:
            return {"success": False, "error": "out_file parameter is required"}
        format = params.get("format")
        delimiter = params.get("delimiter")
        decimal_format = params.get("decimal_format")
        digits_after_decimal = params.get("digits_after_decimal")
        decimal_separator = params.get("decimal_separator")

            # Generate output name and path
            output_name = f"{in_feature_class.replace(' ', '_')}_Feature_Class_Z_To_ASCII"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Feature Class Z To ASCII
            arcpy.FeatureClassZToASCII(in_feature_class, output_location, out_file, format, delimiter, decimal_format, digits_after_decimal, decimal_separator)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def feature_to_3d_by_attribute(self, params):
        """Feature To 3D By Attribute

Creates 3D features using height values derived from the attribute of the input features.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "height_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        height_field = params.get("height_field")
        if height_field is None:
            return {"success": False, "error": "height_field parameter is required"}
        to_height_field = params.get("to_height_field")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Feature_To_3D_By_Attribute"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Feature To 3D By Attribute
            arcpy.FeatureTo3DByAttribute(in_features, out_feature_class, height_field, to_height_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def features_from_cityengine_rules(self, params):
        """Features From CityEngine Rules

Generates 3D geometries  from existing 2D and 3D input features using rules authored in ArcGIS CityEngine.

        params: {"in_features": <Feature Layer>, "in_rule_package": <File>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        in_rule_package = params.get("in_rule_package")
        if in_rule_package is None:
            return {"success": False, "error": "in_rule_package parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        in_existing_fields = params.get("in_existing_fields")
        in_include_reports = params.get("in_include_reports")
        in_leaf_shapes = params.get("in_leaf_shapes")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Features_From_CityEngine_Rules"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Features From CityEngine Rules
            arcpy.FeaturesFromCityEngineRules(in_features, in_rule_package, out_feature_class, in_existing_fields, in_include_reports, in_leaf_shapes)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def import_3d_files(self, params):
        """Import 3D Files

Imports one or more 3D models into a multipatch feature class.

        params: {"in_files": <File; Folder>, "out_featureclass": <Feature Class>, "root_per_feature": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_files = params.get("in_files")
        if in_files is None:
            return {"success": False, "error": "in_files parameter is required"}
        out_featureclass = params.get("out_featureclass")
        if out_featureclass is None:
            return {"success": False, "error": "out_featureclass parameter is required"}
        root_per_feature = params.get("root_per_feature")
        spatial_reference = params.get("spatial_reference")
        y_is_up = params.get("y_is_up")
        file_suffix = params.get("file_suffix")
        if file_suffix is None:
            return {"success": False, "error": "file_suffix parameter is required"}
        in_featureclass = params.get("in_featureclass")
        symbol_field = params.get("symbol_field")

            # Generate output name and path
            output_name = f"{in_files.replace(' ', '_')}_Import_3D_Files"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Import 3D Files
            arcpy.Import3DFiles(in_files, out_featureclass, root_per_feature, spatial_reference, y_is_up, file_suffix, in_featureclass, symbol_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def layer_3d_to_feature_class(self, params):
        """Layer 3D To Feature Class

Exports feature layers with 3D display properties to 3D lines or multipatch features.

        params: {"in_feature_layer": <Feature Layer>, "out_feature_class": <Feature Class>, "group_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_feature_layer = params.get("in_feature_layer")
        if in_feature_layer is None:
            return {"success": False, "error": "in_feature_layer parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        group_field = params.get("group_field")
        disable_materials = params.get("disable_materials")

            # Generate output name and path
            output_name = f"{in_feature_layer.replace(' ', '_')}_Layer_3D_To_Feature_Class"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Layer 3D To Feature Class
            arcpy.Layer3DToFeatureClass(in_feature_layer, out_feature_class, group_field, disable_materials)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_lod2_buildings(self, params):
        """Extract LOD2 Buildings

Creates 3D models of LOD2 buildings using building footprint polygons and a raster elevation surface.

        params: {"in_height_source": <Raster Layer; Mosaic Layer>, "in_features": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_height_source = params.get("in_height_source")
        if in_height_source is None:
            return {"success": False, "error": "in_height_source parameter is required"}
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        level_of_detail = params.get("level_of_detail")
        smoothness_level = params.get("smoothness_level")
        extraction_accuracy = params.get("extraction_accuracy")

            # Generate output name and path
            output_name = f"{in_height_source.replace(' ', '_')}_Extract_LOD2_Buildings"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract LOD2 Buildings
            arcpy.ExtractLOD2Buildings(in_height_source, in_features, out_feature_class, level_of_detail, smoothness_level, extraction_accuracy)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_mesh_features_using_point_cloud(self, params):
        """Extract Mesh Features Using Point Cloud

Extracts multipatch features representing objects in an integrated mesh based on a classified point cloud.

        params: {"in_mesh": <Scene Layer; File>, "in_point_cloud": <LAS Dataset Layer; Scene Layer; File>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mesh = params.get("in_mesh")
        if in_mesh is None:
            return {"success": False, "error": "in_mesh parameter is required"}
        in_point_cloud = params.get("in_point_cloud")
        if in_point_cloud is None:
            return {"success": False, "error": "in_point_cloud parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        class_codes = params.get("class_codes")
        if class_codes is None:
            return {"success": False, "error": "class_codes parameter is required"}
        point_distance_threshold = params.get("point_distance_threshold")
        if point_distance_threshold is None:
            return {"success": False, "error": "point_distance_threshold parameter is required"}
        maximum_triangle_area = params.get("maximum_triangle_area")
        cluster_distance = params.get("cluster_distance")
        minimum_cluster_area = params.get("minimum_cluster_area")
        boundary = params.get("boundary")

            # Generate output name and path
            output_name = f"{in_mesh.replace(' ', '_')}_Extract_Mesh_Features_Using_Point_Cloud"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract Mesh Features Using Point Cloud
            arcpy.ExtractMeshFeaturesUsingPointCloud(in_mesh, in_point_cloud, out_feature_class, class_codes, point_distance_threshold, maximum_triangle_area, cluster_distance, minimum_cluster_area, boundary)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_multipatch_from_mesh(self, params):
        """Extract Multipatch From Mesh

Creates a multipatch feature from the portion of an integrated mesh that overlaps a polygon.

        params: {"source_mesh": <File; Scene Layer>, "footprint_features": <Feature Layer>, "out_feature_class": <Feature Class>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        source_mesh = params.get("source_mesh")
        if source_mesh is None:
            return {"success": False, "error": "source_mesh parameter is required"}
        footprint_features = params.get("footprint_features")
        if footprint_features is None:
            return {"success": False, "error": "footprint_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}

            # Generate output name and path
            output_name = f"{source_mesh.replace(' ', '_')}_Extract_Multipatch_From_Mesh"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract Multipatch From Mesh
            arcpy.ExtractMultipatchFromMesh(source_mesh, footprint_features, out_feature_class)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_power_lines_from_point_cloud(self, params):
        """Extract Power Lines From Point Cloud

Extracts 3D line features modeling power lines 
from classified point cloud data.

        params: {"in_point_cloud": <LAS Dataset Layer>, "class_codes": <Long>, "out_3d_lines": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_point_cloud = params.get("in_point_cloud")
        if in_point_cloud is None:
            return {"success": False, "error": "in_point_cloud parameter is required"}
        class_codes = params.get("class_codes")
        if class_codes is None:
            return {"success": False, "error": "class_codes parameter is required"}
        out_3d_lines = params.get("out_3d_lines")
        if out_3d_lines is None:
            return {"success": False, "error": "out_3d_lines parameter is required"}
        point_tolerance = params.get("point_tolerance")
        separation_distance = params.get("separation_distance")
        max_sampling_gap = params.get("max_sampling_gap")
        line_tolerance = params.get("line_tolerance")
        wind_correction = params.get("wind_correction")
        min_wind_span = params.get("min_wind_span")
        max_wind_deviation = params.get("max_wind_deviation")
        end_point_search_radius = params.get("end_point_search_radius")
        min_length = params.get("min_length")
        eliminate_wind = params.get("eliminate_wind")
        min_line_length = params.get("min_line_length")

            # Generate output name and path
            output_name = f"{in_point_cloud.replace(' ', '_')}_Extract_Power_Lines_From_Point_Cloud"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract Power Lines From Point Cloud
            arcpy.ExtractPowerLinesFromPointCloud(in_point_cloud, class_codes, out_3d_lines, point_tolerance, separation_distance, max_sampling_gap, line_tolerance, wind_correction, min_wind_span, max_wind_deviation, end_point_search_radius, min_length, eliminate_wind, min_line_length)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_rails_from_point_cloud(self, params):
        """Extract Rails From Point Cloud

Extracts rail track lines and center lines from classified 
railroad tracks in a LAS dataset, point cloud scene layer package, or I3S point cloud layer.

        params: {"in_point_cloud": <LAS Dataset Layer; Scene Layer>, "class_codes": <Long>, "out_3d_lines": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_point_cloud = params.get("in_point_cloud")
        if in_point_cloud is None:
            return {"success": False, "error": "in_point_cloud parameter is required"}
        class_codes = params.get("class_codes")
        if class_codes is None:
            return {"success": False, "error": "class_codes parameter is required"}
        out_3d_lines = params.get("out_3d_lines")
        if out_3d_lines is None:
            return {"success": False, "error": "out_3d_lines parameter is required"}
        rail_standard = params.get("rail_standard")
        out_3d_centerlines = params.get("out_3d_centerlines")
        track_gauge = params.get("track_gauge")
        rail_thickness = params.get("rail_thickness")
        horizontal_smoothing_kernel_distance = params.get("horizontal_smoothing_kernel_distance")
        vertical_smoothing_kernel_distance = params.get("vertical_smoothing_kernel_distance")
        horizontal_rail_tolerance = params.get("horizontal_rail_tolerance")
        vertical_rail_tolerance = params.get("vertical_rail_tolerance")
        centerline_alignment_tolerance = params.get("centerline_alignment_tolerance")
        rail_crown_detection_radius = params.get("rail_crown_detection_radius")
        horizontal_simplification_tolerance = params.get("horizontal_simplification_tolerance")
        vertical_simplification_tolerance = params.get("vertical_simplification_tolerance")
        min_line_length = params.get("min_line_length")

            # Generate output name and path
            output_name = f"{in_point_cloud.replace(' ', '_')}_Extract_Rails_From_Point_Cloud"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract Rails From Point Cloud
            arcpy.ExtractRailsFromPointCloud(in_point_cloud, class_codes, out_3d_lines, rail_standard, out_3d_centerlines, track_gauge, rail_thickness, horizontal_smoothing_kernel_distance, vertical_smoothing_kernel_distance, horizontal_rail_tolerance, vertical_rail_tolerance, centerline_alignment_tolerance, rail_crown_detection_radius, horizontal_simplification_tolerance, vertical_simplification_tolerance, min_line_length)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def las_building_multipatch(self, params):
        """LAS Building Multipatch

Creates building models using rooftop points in a LAS dataset.

        params: {"in_las_dataset": <LAS Dataset Layer>, "in_features": <Feature Layer>, "ground": <Field; Raster Layer; TIN Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_las_dataset = params.get("in_las_dataset")
        if in_las_dataset is None:
            return {"success": False, "error": "in_las_dataset parameter is required"}
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        ground = params.get("ground")
        if ground is None:
            return {"success": False, "error": "ground parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        point_selection = params.get("point_selection")
        simplification = params.get("simplification")
        sampling_resolution = params.get("sampling_resolution")
        min_height_field = params.get("min_height_field")
        max_height_field = params.get("max_height_field")

            # Generate output name and path
            output_name = f"{in_las_dataset.replace(' ', '_')}_LAS_Building_Multipatch"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute LAS Building Multipatch
            arcpy.LASBuildingMultipatch(in_las_dataset, in_features, ground, out_feature_class, point_selection, simplification, sampling_resolution, min_height_field, max_height_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def multipatch_footprint(self, params):
        """Multipatch Footprint

Creates polygon footprints representing the two-dimensional  area of multipatch features.

        params: {"in_feature_class": <Feature Layer>, "out_feature_class": <Feature Class>, "group_field": <Field>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_feature_class = params.get("in_feature_class")
        if in_feature_class is None:
            return {"success": False, "error": "in_feature_class parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        group_field = params.get("group_field")

            # Generate output name and path
            output_name = f"{in_feature_class.replace(' ', '_')}_Multipatch_Footprint"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Multipatch Footprint
            arcpy.MultipatchFootprint(in_feature_class, out_feature_class, group_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def regularize_adjacent_building_footprint(self, params):
        """Regularize Adjacent Building Footprint

Regularizes building footprints that have common boundaries.

        params: {"in_features": <Feature Layer>, "group": <Field>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        group = params.get("group")
        if group is None:
            return {"success": False, "error": "group parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        method = params.get("method")
        if method is None:
            return {"success": False, "error": "method parameter is required"}
        tolerance = params.get("tolerance")
        if tolerance is None:
            return {"success": False, "error": "tolerance parameter is required"}
        precision = params.get("precision")
        if precision is None:
            return {"success": False, "error": "precision parameter is required"}
        angular_limit = params.get("angular_limit")
        if angular_limit is None:
            return {"success": False, "error": "angular_limit parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Regularize_Adjacent_Building_Footprint"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Regularize Adjacent Building Footprint
            arcpy.RegularizeAdjacentBuildingFootprint(in_features, group, out_feature_class, method, tolerance, precision, angular_limit)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def regularize_building_footprint(self, params):
        """Regularize Building Footprint

Normalizes the footprint of building polygons by eliminating undesirable artifacts in their geometry.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        method = params.get("method")
        if method is None:
            return {"success": False, "error": "method parameter is required"}
        tolerance = params.get("tolerance")
        if tolerance is None:
            return {"success": False, "error": "tolerance parameter is required"}
        densification = params.get("densification")
        if densification is None:
            return {"success": False, "error": "densification parameter is required"}
        precision = params.get("precision")
        if precision is None:
            return {"success": False, "error": "precision parameter is required"}
        diagonal_penalty = params.get("diagonal_penalty")
        if diagonal_penalty is None:
            return {"success": False, "error": "diagonal_penalty parameter is required"}
        min_radius = params.get("min_radius")
        if min_radius is None:
            return {"success": False, "error": "min_radius parameter is required"}
        max_radius = params.get("max_radius")
        if max_radius is None:
            return {"success": False, "error": "max_radius parameter is required"}
        alignment_feature = params.get("alignment_feature")
        alignment_tolerance = params.get("alignment_tolerance")
        tolerance_type = params.get("tolerance_type")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Regularize_Building_Footprint"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Regularize Building Footprint
            arcpy.RegularizeBuildingFootprint(in_features, out_feature_class, method, tolerance, densification, precision, diagonal_penalty, min_radius, max_radius, alignment_feature, alignment_tolerance, tolerance_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def interpolate_polygon_to_multipatch(self, params):
        """Interpolate Polygon To Multipatch

Creates surface-conforming  multipatch features by draping polygon features over a surface.

        params: {"in_surface": <Terrain Layer; TIN Layer>, "in_feature_class": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_surface = params.get("in_surface")
        if in_surface is None:
            return {"success": False, "error": "in_surface parameter is required"}
        in_feature_class = params.get("in_feature_class")
        if in_feature_class is None:
            return {"success": False, "error": "in_feature_class parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        max_strip_size = params.get("max_strip_size")
        z_factor = params.get("z_factor")
        area_field = params.get("area_field")
        surface_area_field = params.get("surface_area_field")
        pyramid_level_resolution = params.get("pyramid_level_resolution")

            # Generate output name and path
            output_name = f"{in_surface.replace(' ', '_')}_Interpolate_Polygon_To_Multipatch"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Interpolate Polygon To Multipatch
            arcpy.InterpolatePolygonToMultipatch(in_surface, in_feature_class, out_feature_class, max_strip_size, z_factor, area_field, surface_area_field, pyramid_level_resolution)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def interpolate_shape(self, params):
        """Interpolate Shape

Creates 3D features by interpolating z-values from a surface. Learn more about how Interpolate Shape works

        params: {"in_surface": <LAS Dataset Layer; Mosaic Layer; Raster Layer; Terrain Layer; TIN Layer; Image Service>, "in_feature_class": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_surface = params.get("in_surface")
        if in_surface is None:
            return {"success": False, "error": "in_surface parameter is required"}
        in_feature_class = params.get("in_feature_class")
        if in_feature_class is None:
            return {"success": False, "error": "in_feature_class parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        sample_distance = params.get("sample_distance")
        z_factor = params.get("z_factor")
        method = params.get("method")
        vertices_only = params.get("vertices_only")
        pyramid_level_resolution = params.get("pyramid_level_resolution")
        preserve_features = params.get("preserve_features")

            # Generate output name and path
            output_name = f"{in_surface.replace(' ', '_')}_Interpolate_Shape"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Interpolate Shape
            arcpy.InterpolateShape(in_surface, in_feature_class, out_feature_class, sample_distance, z_factor, method, vertices_only, pyramid_level_resolution, preserve_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def update_feature_z(self, params):
        """Update Feature Z

Updates the z-coordinates of 3D feature vertices using a surface.

        params: {"in_features": <Feature Layer>, "in_surface": <LAS Dataset Layer; Mosaic Layer; Raster Layer; TIN Layer>, "method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        in_surface = params.get("in_surface")
        if in_surface is None:
            return {"success": False, "error": "in_surface parameter is required"}
        method = params.get("method")
        status_field = params.get("status_field")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Update_Feature_Z"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Update Feature Z
            arcpy.UpdateFeatureZ(in_features, in_surface, method, status_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_missing_z_values(self, params):
        """Calculate Missing Z Values

Creates features that update the z-values of 3D line or polygon vertices with placeholder values that represent missing z-value information.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "placeholder": <Double>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        placeholder = params.get("placeholder")
        if placeholder is None:
            return {"success": False, "error": "placeholder parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Calculate_Missing_Z_Values"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Missing Z Values
            arcpy.CalculateMissingZValues(in_features, out_feature_class, placeholder)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def locate_outliers(self, params):
        """Locate Outliers

Identifies anomalous elevation measurements from terrain, TIN, or LAS datasets that exceed a defined range of elevation values or have slope characteristics that are inconsistent with the surrounding surface.

        params: {"in_surface": <LAS Dataset Layer; Terrain Layer; TIN Layer>, "out_feature_class": <Feature Class>, "apply_hard_limit": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_surface = params.get("in_surface")
        if in_surface is None:
            return {"success": False, "error": "in_surface parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        apply_hard_limit = params.get("apply_hard_limit")
        absolute_z_min = params.get("absolute_z_min")
        absolute_z_max = params.get("absolute_z_max")
        apply_comparison_filter = params.get("apply_comparison_filter")
        z_tolerance = params.get("z_tolerance")
        slope_tolerance = params.get("slope_tolerance")
        exceed_tolerance_ratio = params.get("exceed_tolerance_ratio")
        outlier_cap = params.get("outlier_cap")

            # Generate output name and path
            output_name = f"{in_surface.replace(' ', '_')}_Locate_Outliers"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Locate Outliers
            arcpy.LocateOutliers(in_surface, out_feature_class, apply_hard_limit, absolute_z_min, absolute_z_max, apply_comparison_filter, z_tolerance, slope_tolerance, exceed_tolerance_ratio, outlier_cap)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def surface_aspect(self, params):
        """Surface Aspect

Creates polygon features that represent aspect measurements derived  from a TIN, terrain, or LAS dataset surface.

        params: {"in_surface": <LAS Dataset Layer; Terrain Layer; TIN Layer>, "out_feature_class": <Feature Class>, "class_breaks_table": <Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_surface = params.get("in_surface")
        if in_surface is None:
            return {"success": False, "error": "in_surface parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        class_breaks_table = params.get("class_breaks_table")
        aspect_field = params.get("aspect_field")
        pyramid_level_resolution = params.get("pyramid_level_resolution")

            # Generate output name and path
            output_name = f"{in_surface.replace(' ', '_')}_Surface_Aspect"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Surface Aspect
            arcpy.SurfaceAspect(in_surface, out_feature_class, class_breaks_table, aspect_field, pyramid_level_resolution)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def surface_contour(self, params):
        """Surface Contour

Creates contour lines derived from a terrain, TIN, or LAS dataset surface. Learn more about how Surface Contour works

        params: {"in_surface": <LAS Dataset Layer; Terrain Layer; TIN Layer>, "out_feature_class": <Feature Class>, "interval": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_surface = params.get("in_surface")
        if in_surface is None:
            return {"success": False, "error": "in_surface parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        interval = params.get("interval")
        if interval is None:
            return {"success": False, "error": "interval parameter is required"}
        base_contour = params.get("base_contour")
        contour_field = params.get("contour_field")
        contour_field_precision = params.get("contour_field_precision")
        index_interval = params.get("index_interval")
        index_interval_field = params.get("index_interval_field")
        z_factor = params.get("z_factor")
        pyramid_level_resolution = params.get("pyramid_level_resolution")

            # Generate output name and path
            output_name = f"{in_surface.replace(' ', '_')}_Surface_Contour"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Surface Contour
            arcpy.SurfaceContour(in_surface, out_feature_class, interval, base_contour, contour_field, contour_field_precision, index_interval, index_interval_field, z_factor, pyramid_level_resolution)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def surface_slope(self, params):
        """Surface Slope

Creates polygon features that represent ranges of slope values for triangulated surfaces.

        params: {"in_surface": <LAS Dataset Layer; Terrain Layer; TIN Layer>, "out_feature_class": <Feature Class>, "units": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_surface = params.get("in_surface")
        if in_surface is None:
            return {"success": False, "error": "in_surface parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        units = params.get("units")
        class_breaks_table = params.get("class_breaks_table")
        slope_field = params.get("slope_field")
        z_factor = params.get("z_factor")
        pyramid_level_resolution = params.get("pyramid_level_resolution")

            # Generate output name and path
            output_name = f"{in_surface.replace(' ', '_')}_Surface_Slope"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Surface Slope
            arcpy.SurfaceSlope(in_surface, out_feature_class, units, class_breaks_table, slope_field, z_factor, pyramid_level_resolution)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def construct_sight_lines(self, params):
        """Construct Sight Lines

Creates line features that represent sight lines from one or more observer points to features in a  target feature class.

        params: {"in_observer_points": <Feature Layer>, "in_target_features": <Feature Layer>, "out_line_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_observer_points = params.get("in_observer_points")
        if in_observer_points is None:
            return {"success": False, "error": "in_observer_points parameter is required"}
        in_target_features = params.get("in_target_features")
        if in_target_features is None:
            return {"success": False, "error": "in_target_features parameter is required"}
        out_line_feature_class = params.get("out_line_feature_class")
        if out_line_feature_class is None:
            return {"success": False, "error": "out_line_feature_class parameter is required"}
        observer_height_field = params.get("observer_height_field")
        target_height_field = params.get("target_height_field")
        join_field = params.get("join_field")
        sample_distance = params.get("sample_distance")
        output_the_direction = params.get("output_the_direction")
        sampling_method = params.get("sampling_method")

            # Generate output name and path
            output_name = f"{in_observer_points.replace(' ', '_')}_Construct_Sight_Lines"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Construct Sight Lines
            arcpy.ConstructSightLines(in_observer_points, in_target_features, out_line_feature_class, observer_height_field, target_height_field, join_field, sample_distance, output_the_direction, sampling_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def geodesic_viewshed(self, params):
        """Geodesic Viewshed

Determines the raster surface locations visible to a set of observer features using geodesic methods. Learn more about how the Geodesic Viewshed tool works

        params: {"in_raster": <Raster Layer>, "in_observer_features": <Feature Layer>, "out_raster": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_observer_features = params.get("in_observer_features")
        if in_observer_features is None:
            return {"success": False, "error": "in_observer_features parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        out_agl_raster = params.get("out_agl_raster")
        analysis_type = params.get("analysis_type")
        vertical_error = params.get("vertical_error")
        out_observer_region_relationship_table = params.get("out_observer_region_relationship_table")
        refractivity_coefficient = params.get("refractivity_coefficient")
        surface_offset = params.get("surface_offset")
        observer_elevation = params.get("observer_elevation")
        observer_offset = params.get("observer_offset")
        inner_radius = params.get("inner_radius")
        inner_radius_is_3d = params.get("inner_radius_is_3d")
        outer_radius = params.get("outer_radius")
        outer_radius_is_3d = params.get("outer_radius_is_3d")
        horizontal_start_angle = params.get("horizontal_start_angle")
        horizontal_end_angle = params.get("horizontal_end_angle")
        vertical_upper_angle = params.get("vertical_upper_angle")
        vertical_lower_angle = params.get("vertical_lower_angle")
        analysis_method = params.get("analysis_method")
        analysis_target_device = params.get("analysis_target_device")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Geodesic_Viewshed"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Geodesic Viewshed
            arcpy.GeodesicViewshed(in_raster, in_observer_features, out_raster, out_agl_raster, analysis_type, vertical_error, out_observer_region_relationship_table, refractivity_coefficient, surface_offset, observer_elevation, observer_offset, inner_radius, inner_radius_is_3d, outer_radius, outer_radius_is_3d, horizontal_start_angle, horizontal_end_angle, vertical_upper_angle, vertical_lower_angle, analysis_method, analysis_target_device)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def intervisibility(self, params):
        """Intervisibility

Determines the visibility of sight lines using  potential obstructions defined by any combination of  3D features and surfaces.

        params: {"sight_lines": <Feature Layer>, "obstructions": <Feature Layer; TIN Layer; Raster Layer; Mosaic Layer; Scene Layer; File>, "visible_field": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        sight_lines = params.get("sight_lines")
        if sight_lines is None:
            return {"success": False, "error": "sight_lines parameter is required"}
        obstructions = params.get("obstructions")
        if obstructions is None:
            return {"success": False, "error": "obstructions parameter is required"}
        visible_field = params.get("visible_field")

            # Generate output name and path
            output_name = f"{sight_lines.replace(' ', '_')}_Intervisibility"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Intervisibility
            arcpy.Intervisibility(sight_lines, obstructions, visible_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def line_of_sight(self, params):
        """Line Of Sight

Determines the visibility of sight lines over obstructions consisting of a surface and an optional multipatch dataset. Learn more about how Line Of Sight works

        params: {"in_surface": <TIN Layer; Raster Layer; Mosaic Layer; Terrain Layer; LAS Dataset Layer; Scene Layer; File>, "in_line_feature_class": <Feature Layer>, "out_los_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_surface = params.get("in_surface")
        if in_surface is None:
            return {"success": False, "error": "in_surface parameter is required"}
        in_line_feature_class = params.get("in_line_feature_class")
        if in_line_feature_class is None:
            return {"success": False, "error": "in_line_feature_class parameter is required"}
        out_los_feature_class = params.get("out_los_feature_class")
        if out_los_feature_class is None:
            return {"success": False, "error": "out_los_feature_class parameter is required"}
        out_obstruction_feature_class = params.get("out_obstruction_feature_class")
        use_curvature = params.get("use_curvature")
        use_refraction = params.get("use_refraction")
        refraction_factor = params.get("refraction_factor")
        pyramid_level_resolution = params.get("pyramid_level_resolution")
        in_features = params.get("in_features")
        output_graphing_attributes = params.get("output_graphing_attributes")

            # Generate output name and path
            output_name = f"{in_surface.replace(' ', '_')}_Line_Of_Sight"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Line Of Sight
            arcpy.LineOfSight(in_surface, in_line_feature_class, out_los_feature_class, out_obstruction_feature_class, use_curvature, use_refraction, refraction_factor, pyramid_level_resolution, in_features, output_graphing_attributes)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def observer_points(self, params):
        """Observer Points

Identifies which observer points are visible from each raster surface location. The Geodesic Viewshed tool provides enhanced functionality or performance. Learn more about how Observer Points works

        params: {"in_raster": <Raster Layer>, "in_observer_point_features": <Feature Layer>, "out_raster": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_observer_point_features = params.get("in_observer_point_features")
        if in_observer_point_features is None:
            return {"success": False, "error": "in_observer_point_features parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        z_factor = params.get("z_factor")
        curvature_correction = params.get("curvature_correction")
        refractivity_coefficient = params.get("refractivity_coefficient")
        out_agl_raster = params.get("out_agl_raster")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Observer_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Observer Points
            arcpy.ObserverPoints(in_raster, in_observer_point_features, out_raster, z_factor, curvature_correction, refractivity_coefficient, out_agl_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def skyline(self, params):
        """Skyline

Generates a line or multipatch feature class containing the results from a skyline or silhouette analysis. Learn more about how Skyline works

        params: {"in_observer_point_features": <Feature Layer>, "out_feature_class": <Feature Class>, "in_surface": <LAS Dataset Layer; Mosaic Layer; Raster Layer; TIN Layer; Terrain Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_observer_point_features = params.get("in_observer_point_features")
        if in_observer_point_features is None:
            return {"success": False, "error": "in_observer_point_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        in_surface = params.get("in_surface")
        virtual_surface_radius = params.get("virtual_surface_radius")
        virtual_surface_elevation = params.get("virtual_surface_elevation")
        in_features = params.get("in_features")
        feature_lod = params.get("feature_lod")
        from_azimuth_value_or_field = params.get("from_azimuth_value_or_field")
        to_azimuth_value_or_field = params.get("to_azimuth_value_or_field")
        azimuth_increment_value_or_field = params.get("azimuth_increment_value_or_field")
        max_horizon_radius = params.get("max_horizon_radius")
        segment_skyline = params.get("segment_skyline")
        scale_to_percent = params.get("scale_to_percent")
        scale_according_to = params.get("scale_according_to")
        scale_method = params.get("scale_method")
        use_curvature = params.get("use_curvature")
        use_refraction = params.get("use_refraction")
        refraction_factor = params.get("refraction_factor")
        pyramid_level_resolution = params.get("pyramid_level_resolution")
        create_silhouettes = params.get("create_silhouettes")
        apply_max_radius_to_features = params.get("apply_max_radius_to_features")
        vertical_offset = params.get("vertical_offset")

            # Generate output name and path
            output_name = f"{in_observer_point_features.replace(' ', '_')}_Skyline"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Skyline
            arcpy.Skyline(in_observer_point_features, out_feature_class, in_surface, virtual_surface_radius, virtual_surface_elevation, in_features, feature_lod, from_azimuth_value_or_field, to_azimuth_value_or_field, azimuth_increment_value_or_field, max_horizon_radius, segment_skyline, scale_to_percent, scale_according_to, scale_method, use_curvature, use_refraction, refraction_factor, pyramid_level_resolution, create_silhouettes, apply_max_radius_to_features, vertical_offset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def skyline_barrier(self, params):
        """Skyline Barrier

Generates a multipatch feature class representing a skyline barrier or shadow volume. Learn more about how Skyline Barrier works

        params: {"in_observer_point_features": <Feature Layer>, "in_features": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_observer_point_features = params.get("in_observer_point_features")
        if in_observer_point_features is None:
            return {"success": False, "error": "in_observer_point_features parameter is required"}
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        min_radius_value_or_field = params.get("min_radius_value_or_field")
        max_radius_value_or_field = params.get("max_radius_value_or_field")
        closed = params.get("closed")
        base_elevation = params.get("base_elevation")
        project_to_plane = params.get("project_to_plane")

            # Generate output name and path
            output_name = f"{in_observer_point_features.replace(' ', '_')}_Skyline_Barrier"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Skyline Barrier
            arcpy.SkylineBarrier(in_observer_point_features, in_features, out_feature_class, min_radius_value_or_field, max_radius_value_or_field, closed, base_elevation, project_to_plane)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def skyline_graph(self, params):
        """Skyline Graph

Calculates the sky visibility ratio and generates an optional table and a polar graph.

        params: {"in_observer_point_features": <Feature Layer>, "in_line_features": <Feature Layer>, "base_visibility_angle": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_observer_point_features = params.get("in_observer_point_features")
        if in_observer_point_features is None:
            return {"success": False, "error": "in_observer_point_features parameter is required"}
        in_line_features = params.get("in_line_features")
        if in_line_features is None:
            return {"success": False, "error": "in_line_features parameter is required"}
        base_visibility_angle = params.get("base_visibility_angle")
        additional_fields = params.get("additional_fields")
        out_angles_table = params.get("out_angles_table")
        out_graph = params.get("out_graph")
        out_image_file = params.get("out_image_file")

            # Generate output name and path
            output_name = f"{in_observer_point_features.replace(' ', '_')}_Skyline_Graph"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Skyline Graph
            arcpy.SkylineGraph(in_observer_point_features, in_line_features, base_visibility_angle, additional_fields, out_angles_table, out_graph, out_image_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def sun_shadow_frequency(self, params):
        """Sun Shadow Frequency

Calculates the number of times a fixed position on a surface has its direct sight line to the sun obstructed by multipatch features.

        params: {"in_features": <Feature Layer>, "ground": <Raster Layer>, "out_raster": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        ground = params.get("ground")
        if ground is None:
            return {"success": False, "error": "ground parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        cell_size = params.get("cell_size")
        start_time = params.get("start_time")
        end_time = params.get("end_time")
        time_interval = params.get("time_interval")
        time_zone = params.get("time_zone")
        dst = params.get("dst")
        max_shadow_length = params.get("max_shadow_length")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Sun_Shadow_Frequency"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Sun Shadow Frequency
            arcpy.SunShadowFrequency(in_features, ground, out_raster, cell_size, start_time, end_time, time_interval, time_zone, dst, max_shadow_length)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def sun_shadow_volume(self, params):
        """Sun Shadow Volume

Creates closed volumes that model shadows cast by each feature using sunlight for a given date and time.

        params: {"in_features": <Feature Layer>, "start_date_and_time": <Date>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        start_date_and_time = params.get("start_date_and_time")
        if start_date_and_time is None:
            return {"success": False, "error": "start_date_and_time parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        adjusted_for_dst = params.get("adjusted_for_dst")
        time_zone = params.get("time_zone")
        end_date_and_time = params.get("end_date_and_time")
        iteration_interval = params.get("iteration_interval")
        iteration_unit = params.get("iteration_unit")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Sun_Shadow_Volume"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Sun Shadow Volume
            arcpy.SunShadowVolume(in_features, start_date_and_time, out_feature_class, adjusted_for_dst, time_zone, end_date_and_time, iteration_interval, iteration_unit)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def viewshed(self, params):
        """Viewshed

Determines the raster surface locations visible to a set of observer features. The Geodesic Viewshed tool provides enhanced functionality or performance. Learn more about how Viewshed works

        params: {"in_raster": <Raster Layer>, "in_observer_features": <Feature Layer>, "out_raster": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_observer_features = params.get("in_observer_features")
        if in_observer_features is None:
            return {"success": False, "error": "in_observer_features parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        z_factor = params.get("z_factor")
        curvature_correction = params.get("curvature_correction")
        refractivity_coefficient = params.get("refractivity_coefficient")
        out_agl_raster = params.get("out_agl_raster")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Viewshed"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Viewshed
            arcpy.Viewshed(in_raster, in_observer_features, out_raster, z_factor, curvature_correction, refractivity_coefficient, out_agl_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def visibility(self, params):
        """Visibility

Determines the raster surface locations visible to a set of observer features, or identifies which observer points are visible from each raster surface location. The Geodesic Viewshed tool provides enhanced functionality or performance.

        params: {"in_raster": <Raster Layer>, "in_observer_features": <Feature Layer>, "out_raster": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_observer_features = params.get("in_observer_features")
        if in_observer_features is None:
            return {"success": False, "error": "in_observer_features parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        out_agl_raster = params.get("out_agl_raster")
        analysis_type = params.get("analysis_type")
        nonvisible_cell_value = params.get("nonvisible_cell_value")
        z_factor = params.get("z_factor")
        curvature_correction = params.get("curvature_correction")
        refractivity_coefficient = params.get("refractivity_coefficient")
        surface_offset = params.get("surface_offset")
        observer_elevation = params.get("observer_elevation")
        observer_offset = params.get("observer_offset")
        inner_radius = params.get("inner_radius")
        outer_radius = params.get("outer_radius")
        horizontal_start_angle = params.get("horizontal_start_angle")
        horizontal_end_angle = params.get("horizontal_end_angle")
        vertical_upper_angle = params.get("vertical_upper_angle")
        vertical_lower_angle = params.get("vertical_lower_angle")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Visibility"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Visibility
            arcpy.Visibility(in_raster, in_observer_features, out_raster, out_agl_raster, analysis_type, nonvisible_cell_value, z_factor, curvature_correction, refractivity_coefficient, surface_offset, observer_elevation, observer_offset, inner_radius, outer_radius, horizontal_start_angle, horizontal_end_angle, vertical_upper_angle, vertical_lower_angle)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}
