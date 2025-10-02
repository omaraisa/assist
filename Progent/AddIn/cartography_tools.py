# Corrected ArcGIS Pro cartography Progent Functions
# Generated on 2025-10-01T13:54:58.197668
# Total tools: 51

import arcpy
import os

class CartographyTools:
    """Corrected cartography functions in progent.pyt format"""

    def _add_to_map(self, path):
        try:
            aprx = arcpy.mp.ArcGISProject('CURRENT')
            map_obj = aprx.activeMap
            if map_obj:
                map_obj.addDataFromPath(path)
        except Exception as e:
            print(f'Could not add {path} to map: {e}')

    def annotate_selected_features(self, params):
        """Annotate Selected Features

Creates annotation for the selected features of a layer. The labeling properties defined in the annotation class properties of  the specified related annotation feature classes are used.

        params: {"in_map": <Map>, "in_layer": <Feature Layer>, "anno_layers": <Value Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_map = params.get("in_map")
            if in_map is None:
                return {"success": False, "error": "in_map parameter is required"}
            in_layer = params.get("in_layer")
            if in_layer is None:
                return {"success": False, "error": "in_layer parameter is required"}
            anno_layers = params.get("anno_layers")
            if anno_layers is None:
                return {"success": False, "error": "anno_layers parameter is required"}
            generate_unplaced = params.get("generate_unplaced")

            # No output path is created by this tool. It modifies annotation feature classes.

            arcpy.cartography.AnnotateSelectedFeatures(in_map, in_layer, anno_layers, generate_unplaced)

            return {"success": True, "message": "Annotate Selected Features completed successfully."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def contour_annotation(self, params):
        """Contour Annotation

Creates annotation for contour features. The tool creates an annotation feature class with corresponding mask polygons based on input contour features.

        params: {"in_features": <Feature Layer>, "out_geodatabase": <Workspace; Feature Dataset>, "contour_label_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            out_geodatabase = params.get("out_geodatabase")
            if out_geodatabase is None:
                return {"success": False, "error": "out_geodatabase parameter is required"}
            contour_label_field = params.get("contour_label_field")
            if contour_label_field is None:
                return {"success": False, "error": "contour_label_field parameter is required"}
            reference_scale_value = params.get("reference_scale_value")
            if reference_scale_value is None:
                return {"success": False, "error": "reference_scale_value parameter is required"}
            out_layer = params.get("out_layer")
            if out_layer is None:
                return {"success": False, "error": "out_layer parameter is required"}
            contour_color = params.get("contour_color")
            if contour_color is None:
                return {"success": False, "error": "contour_color parameter is required"}
            contour_type_field = params.get("contour_type_field")
            contour_alignment = params.get("contour_alignment")
            enable_laddering = params.get("enable_laddering")

            arcpy.cartography.ContourAnnotation(in_features, out_geodatabase, contour_label_field, reference_scale_value, out_layer, contour_color, contour_type_field, contour_alignment, enable_laddering)

            # Output is the out_layer, which is a Feature Layer, not a path
            self._add_to_map(out_layer)
            return {"success": True, "output_layer": out_layer}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def convert_labels_to_annotation(self, params):
        """Convert Labels To Annotation

Converts labels to annotation for a single layer or the entire map. Both standard annotation and feature-linked annotation can be created.

        params: {"input_map": <Map>, "conversion_scale": <Double>, "output_geodatabase": <Workspace; Feature Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            input_map = params.get("input_map")
            if input_map is None:
                return {"success": False, "error": "input_map parameter is required"}
            conversion_scale = params.get("conversion_scale")
            if conversion_scale is None:
                return {"success": False, "error": "conversion_scale parameter is required"}
            output_geodatabase = params.get("output_geodatabase")
            if output_geodatabase is None:
                return {"success": False, "error": "output_geodatabase parameter is required"}
            anno_suffix = params.get("anno_suffix")
            extent = params.get("extent")
            generate_unplaced = params.get("generate_unplaced")
            require_symbol_id = params.get("require_symbol_id")
            feature_linked = params.get("feature_linked")
            auto_create = params.get("auto_create")
            update_on_shape_change = params.get("update_on_shape_change")
            output_group_layer = params.get("output_group_layer")
            which_layers = params.get("which_layers")
            single_layer = params.get("single_layer")
            multiple_feature_classes = params.get("multiple_feature_classes")
            merge_label_classes = params.get("merge_label_classes")

            result = arcpy.cartography.ConvertLabelsToAnnotation(input_map, conversion_scale, output_geodatabase, anno_suffix, extent, generate_unplaced, require_symbol_id, feature_linked, auto_create, update_on_shape_change, output_group_layer, which_layers, single_layer, multiple_feature_classes, merge_label_classes)

            # The tool returns a list of output group layers.
            # We will add the first one to the map.
            if result and result.outputCount > 0:
                out_layer_path = result.getOutput(0)
                self._add_to_map(out_layer_path)
                return {"success": True, "output_layer": out_layer_path}

            return {"success": True, "message": "Convert Labels to Annotation completed."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def convert_labels_to_graphics(self, params):
        """Convert Labels To Graphics

Converts labels to graphics for a single layer or an entire map.

        params: {"input_map": <Map>, "conversion_scale": <Double>, "which_layers": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            input_map = params.get("input_map")
            if input_map is None:
                return {"success": False, "error": "input_map parameter is required"}
            conversion_scale = params.get("conversion_scale")
            if conversion_scale is None:
                return {"success": False, "error": "conversion_scale parameter is required"}
            which_layers = params.get("which_layers")
            single_layer = params.get("single_layer")
            graphics_suffix = params.get("graphics_suffix")
            extent = params.get("extent")
            multiple_graphics_layers = params.get("multiple_graphics_layers")
            generate_unplaced = params.get("generate_unplaced")
            output_group_layer = params.get("output_group_layer")

            result = arcpy.cartography.ConvertLabelsToGraphics(input_map, conversion_scale, which_layers, single_layer, graphics_suffix, extent, multiple_graphics_layers, generate_unplaced, output_group_layer)

            if result and result.outputCount > 0:
                out_layer_path = result.getOutput(0)
                self._add_to_map(out_layer_path)
                return {"success": True, "output_layer": out_layer_path}

            return {"success": True, "message": "Convert Labels to Graphics completed."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def map_server_cache_tiling_scheme_to_polygons(self, params):
        """Map Server Cache Tiling Scheme To Polygons

Creates a polygon feature class from an existing tiling scheme.

        params: {"input_map": <Map>, "tiling_scheme": <File>, "output_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            input_map = params.get("input_map")
            if input_map is None:
                return {"success": False, "error": "input_map parameter is required"}
            tiling_scheme = params.get("tiling_scheme")
            if tiling_scheme is None:
                return {"success": False, "error": "tiling_scheme parameter is required"}
            output_feature_class = params.get("output_feature_class")
            if output_feature_class is None:
                return {"success": False, "error": "output_feature_class parameter is required"}
            use_map_extent = params.get("use_map_extent")
            if use_map_extent is None:
                return {"success": False, "error": "use_map_extent parameter is required"}
            clip_to_horizon = params.get("clip_to_horizon")
            if clip_to_horizon is None:
                return {"success": False, "error": "clip_to_horizon parameter is required"}
            antialiasing = params.get("antialiasing")
            levels = params.get("levels")

            arcpy.cartography.MapServerCacheTilingSchemeToPolygons(input_map, tiling_scheme, output_feature_class, use_map_extent, clip_to_horizon, antialiasing, levels)

            output_name = os.path.basename(output_feature_class)
            self._add_to_map(output_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": output_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def tiled_labels_to_annotation(self, params):
        """Tiled Labels To Annotation

Converts labels to annotation for layers in a map based on a polygon index layer.

        params: {"input_map": <Map>, "polygon_index_layer": <Table View>, "out_geodatabase": <Workspace; Feature Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            input_map = params.get("input_map")
            if input_map is None:
                return {"success": False, "error": "input_map parameter is required"}
            polygon_index_layer = params.get("polygon_index_layer")
            if polygon_index_layer is None:
                return {"success": False, "error": "polygon_index_layer parameter is required"}
            out_geodatabase = params.get("out_geodatabase")
            if out_geodatabase is None:
                return {"success": False, "error": "out_geodatabase parameter is required"}
            out_layer = params.get("out_layer")
            if out_layer is None:
                return {"success": False, "error": "out_layer parameter is required"}
            anno_suffix = params.get("anno_suffix")
            if anno_suffix is None:
                return {"success": False, "error": "anno_suffix parameter is required"}
            reference_scale_value = params.get("reference_scale_value")
            reference_scale_field = params.get("reference_scale_field")
            tile_id_field = params.get("tile_id_field")
            coordinate_sys_field = params.get("coordinate_sys_field")
            map_rotation_field = params.get("map_rotation_field")
            feature_linked = params.get("feature_linked")
            generate_unplaced_annotation = params.get("generate_unplaced_annotation")
            which_layers = params.get("which_layers")
            single_layer = params.get("single_layer")
            require_symbol_id = params.get("require_symbol_id")
            auto_create = params.get("auto_create")
            update_on_shape_change = params.get("update_on_shape_change")
            multiple_feature_classes = params.get("multiple_feature_classes")
            merge_label_classes = params.get("merge_label_classes")

            result = arcpy.cartography.TiledLabelsToAnnotation(input_map, polygon_index_layer, out_geodatabase, out_layer, anno_suffix, reference_scale_value, reference_scale_field, tile_id_field, coordinate_sys_field, map_rotation_field, feature_linked, generate_unplaced_annotation, which_layers, single_layer, require_symbol_id, auto_create, update_on_shape_change, multiple_feature_classes, merge_label_classes)

            if result and result.outputCount > 0:
                out_layer_path = result.getOutput(0)
                self._add_to_map(out_layer_path)
                return {"success": True, "output_layer": out_layer_path}

            return {"success": True, "message": "Tiled Labels to Annotation completed."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def update_annotation_reference_scale(self, params):
        """Update Annotation Reference Scale

Updates the reference scale of an existing annotation or dimension feature class.

        params: {"in_anno_features": <Annotation Layer; Dimension Layer>, "reference_scale": <Double>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_anno_features = params.get("in_anno_features")
            if in_anno_features is None:
                return {"success": False, "error": "in_anno_features parameter is required"}
            reference_scale = params.get("reference_scale")
            if reference_scale is None:
                return {"success": False, "error": "reference_scale parameter is required"}

            arcpy.cartography.UpdateAnnotationReferenceScale(in_anno_features, reference_scale)

            return {"success": True, "message": f"Updated reference scale for {in_anno_features}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_contiguous_cartogram(self, params):
        """Generate Contiguous Cartogram

Generates a cartogram by distorting the area of polygons to be proportional to each other based on a numeric field while preserving shared boundaries.

        params: {"in_features": <Feature Layer>, "field_name": <Field>, "out_features": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            field_name = params.get("field_name")
            if field_name is None:
                return {"success": False, "error": "field_name parameter is required"}
            out_features = params.get("out_features")
            if out_features is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_features).name
                out_features = arcpy.CreateUniqueName(f"{in_name}_Cartogram", aprx.defaultGeodatabase)

            method = params.get("method")

            arcpy.cartography.GenerateContiguousCartogram(in_features, field_name, out_features, method)

            output_name = os.path.basename(out_features)
            self._add_to_map(out_features)
            return {"success": True, "output_layer": output_name, "output_path": out_features}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def align_marker_to_stroke_or_fill(self, params):
        """Align Marker To Stroke Or Fill

Aligns the marker symbol layers of a point feature class to the nearest stroke or fill symbol layers in a line or polygon feature class within a specified search distance.

        params: {"in_point_features": <Layer>, "in_line_or_polygon_features": <Layer>, "search_distance": <Linear Unit>, ...}
        Returns: {"success": True, "message": "Alignment complete."} or error
        """
        try:
            in_point_features = params.get("in_point_features")
            if in_point_features is None:
                return {"success": False, "error": "in_point_features parameter is required"}
            in_line_or_polygon_features = params.get("in_line_or_polygon_features")
            if in_line_or_polygon_features is None:
                return {"success": False, "error": "in_line_or_polygon_features parameter is required"}
            search_distance = params.get("search_distance")
            if search_distance is None:
                return {"success": False, "error": "search_distance parameter is required"}
            marker_orientation = params.get("marker_orientation")

            arcpy.cartography.AlignMarkerToStrokeOrFill(in_point_features, in_line_or_polygon_features, search_distance, marker_orientation)

            return {"success": True, "message": "Align Marker To Stroke Or Fill completed successfully."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_color_theorem_field(self, params):
        """Calculate Color Theorem Field

Populates an integer field to use for symbolizing polygons with a small number of colors and ensuring no two adjacent polygons are the same color.

        params: {"in_features": <Feature Layer>, "field_name": <Field>}
        Returns: {"success": True, "message": "Field calculation complete."} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            field_name = params.get("field_name")
            if field_name is None:
                return {"success": False, "error": "field_name parameter is required"}

            arcpy.cartography.CalculateColorTheoremField(in_features, field_name)

            return {"success": True, "message": f"Calculated color theorem field '{field_name}' for {in_features}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_line_caps(self, params):
        """Calculate Line Caps

Modifies the cap type for stroke symbol layers in the line symbols of the input layer.

        params: {"in_features": <Layer>, "cap_type": <String>, "dangle_option": <String>}
        Returns: {"success": True, "message": "Line caps calculated."} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            cap_type = params.get("cap_type")
            dangle_option = params.get("dangle_option")

            arcpy.cartography.CalculateLineCaps(in_features, cap_type, dangle_option)

            return {"success": True, "message": f"Calculated line caps for {in_features}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_polygon_main_angle(self, params):
        """Calculate Polygon Main Angle

Calculates the dominant angles of input polygon features and assigns the values to a field to use to orient symbology.

        params: {"in_features": <Feature Layer>, "angle_field": <Field>, "rotation_method": <String>}
        Returns: {"success": True, "message": "Angle calculation complete."} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            angle_field = params.get("angle_field")
            if angle_field is None:
                return {"success": False, "error": "angle_field parameter is required"}
            rotation_method = params.get("rotation_method")

            arcpy.cartography.CalculatePolygonMainAngle(in_features, angle_field, rotation_method)

            return {"success": True, "message": f"Calculated polygon main angle into field '{angle_field}' for {in_features}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def convert_control_points_to_vertices(self, params):
        """Convert Control Points To Vertices

Converts control points in a line or polygon feature layer to vertices.

        params: {"in_features": <Feature Layer>}
        Returns: {"success": True, "message": "Conversion complete."} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}

            arcpy.cartography.ConvertControlPointsToVertices(in_features)

            return {"success": True, "message": f"Converted control points to vertices for {in_features}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def convert_marker_placement_to_points(self, params):
        """Convert Marker Placement To Points

Creates points from the markers of a marker placement in a symbolized polygon feature.

        params: {"in_layer": <Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_layer = params.get("in_layer")
            if in_layer is None:
                return {"success": False, "error": "in_layer parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_layer).name
                out_feature_class = arcpy.CreateUniqueName(f"{in_name}_MarkerPoints", aprx.defaultGeodatabase)

            create_multipoints = params.get("create_multipoints")
            boundary_option = params.get("boundary_option")
            boundary_distance = params.get("boundary_distance")
            boundary_distance_field = params.get("boundary_distance_field")
            boundary_distance_unit = params.get("boundary_distance_unit")
            in_barriers = params.get("in_barriers")
            keep_at_least_one_marker = params.get("keep_at_least_one_marker")
            displacement_method = params.get("displacement_method")
            minimum_marker_distance = params.get("minimum_marker_distance")

            arcpy.cartography.ConvertMarkerPlacementToPoints(in_layer, out_feature_class, create_multipoints, boundary_option, boundary_distance, boundary_distance_field, boundary_distance_unit, in_barriers, keep_at_least_one_marker, displacement_method, minimum_marker_distance)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_overpass(self, params):
        """Create Overpass

Creates bridge parapets and polygon masks at line intersections to indicate overpasses.

        params: {"in_above_features": <Layer>, "in_below_features": <Layer>, "margin_along": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_above_features = params.get("in_above_features")
            if in_above_features is None: return {"success": False, "error": "in_above_features is required"}
            in_below_features = params.get("in_below_features")
            if in_below_features is None: return {"success": False, "error": "in_below_features is required"}
            margin_along = params.get("margin_along")
            if margin_along is None: return {"success": False, "error": "margin_along is required"}
            margin_across = params.get("margin_across")
            if margin_across is None: return {"success": False, "error": "margin_across is required"}
            out_overpass_feature_class = params.get("out_overpass_feature_class")
            if out_overpass_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_above_features).name
                out_overpass_feature_class = arcpy.CreateUniqueName(f"{in_name}_Overpass", aprx.defaultGeodatabase)
            out_mask_relationship_class = params.get("out_mask_relationship_class")
            if out_mask_relationship_class is None: return {"success": False, "error": "out_mask_relationship_class is required"}

            where_clause = params.get("where_clause")
            out_decoration_feature_class = params.get("out_decoration_feature_class")
            wing_type = params.get("wing_type")
            wing_tick_length = params.get("wing_tick_length")

            arcpy.cartography.CreateOverpass(in_above_features, in_below_features, margin_along, margin_across, out_overpass_feature_class, out_mask_relationship_class, where_clause, out_decoration_feature_class, wing_type, wing_tick_length)

            output_name = os.path.basename(out_overpass_feature_class)
            self._add_to_map(out_overpass_feature_class)
            if out_decoration_feature_class:
                self._add_to_map(out_decoration_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_overpass_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_underpass(self, params):
        """Create Underpass

Creates bridge parapets and polygon masks at line intersections to indicate underpasses.

        params: {"in_above_features": <Layer>, "in_below_features": <Layer>, "margin_along": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_above_features = params.get("in_above_features")
            if in_above_features is None: return {"success": False, "error": "in_above_features is required"}
            in_below_features = params.get("in_below_features")
            if in_below_features is None: return {"success": False, "error": "in_below_features is required"}
            margin_along = params.get("margin_along")
            if margin_along is None: return {"success": False, "error": "margin_along is required"}
            margin_across = params.get("margin_across")
            if margin_across is None: return {"success": False, "error": "margin_across is required"}
            out_underpass_feature_class = params.get("out_underpass_feature_class")
            if out_underpass_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_below_features).name
                out_underpass_feature_class = arcpy.CreateUniqueName(f"{in_name}_Underpass", aprx.defaultGeodatabase)
            out_mask_relationship_class = params.get("out_mask_relationship_class")
            if out_mask_relationship_class is None: return {"success": False, "error": "out_mask_relationship_class is required"}

            where_clause = params.get("where_clause")
            out_decoration_feature_class = params.get("out_decoration_feature_class")
            wing_type = params.get("wing_type")
            wing_tick_length = params.get("wing_tick_length")

            arcpy.cartography.CreateUnderpass(in_above_features, in_below_features, margin_along, margin_across, out_underpass_feature_class, out_mask_relationship_class, where_clause, out_decoration_feature_class, wing_type, wing_tick_length)

            output_name = os.path.basename(out_underpass_feature_class)
            self._add_to_map(out_underpass_feature_class)
            if out_decoration_feature_class:
                self._add_to_map(out_decoration_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_underpass_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def disperse_markers(self, params):
        """Disperse Markers

Finds point symbols that overlap or are too close to one another and spreads them apart.

        params: {"in_point_features": <Layer>, "minimum_spacing": <Linear Unit>, "dispersal_pattern": <String>}
        Returns: {"success": True, "message": "Markers dispersed."} or error
        """
        try:
            in_point_features = params.get("in_point_features")
            if in_point_features is None:
                return {"success": False, "error": "in_point_features parameter is required"}
            minimum_spacing = params.get("minimum_spacing")
            if minimum_spacing is None:
                return {"success": False, "error": "minimum_spacing parameter is required"}
            dispersal_pattern = params.get("dispersal_pattern")

            arcpy.cartography.DisperseMarkers(in_point_features, minimum_spacing, dispersal_pattern)

            return {"success": True, "message": f"Dispersed markers for {in_point_features}."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_hachures_for_defined_slopes(self, params):
        """Generate Hachures For Defined Slopes

Creates multipart lines or polygons representing the slope between the lines representing the upper and lower parts of a slope.

        params: {"upper_lines": <Feature Layer>, "lower_lines": <Feature Layer>, "output_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            upper_lines = params.get("upper_lines")
            if upper_lines is None: return {"success": False, "error": "upper_lines is required"}
            lower_lines = params.get("lower_lines")
            if lower_lines is None: return {"success": False, "error": "lower_lines is required"}
            output_feature_class = params.get("output_feature_class")
            if output_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(upper_lines).name
                output_feature_class = arcpy.CreateUniqueName(f"{in_name}_Hachures", aprx.defaultGeodatabase)

            output_type = params.get("output_type")
            fully_connected = params.get("fully_connected")
            search_distance = params.get("search_distance")
            interval = params.get("interval")
            minimum_length = params.get("minimum_length")
            alternate_hachures = params.get("alternate_hachures")
            perpendicular = params.get("perpendicular")
            polygon_base_width = params.get("polygon_base_width")

            arcpy.cartography.GenerateHachuresForDefinedSlopes(upper_lines, lower_lines, output_feature_class, output_type, fully_connected, search_distance, interval, minimum_length, alternate_hachures, perpendicular, polygon_base_width)

            output_name = os.path.basename(output_feature_class)
            self._add_to_map(output_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": output_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_control_point_at_intersect(self, params):
        """Set Control Point At Intersect

Creates a control point at vertices that are shared by one or more line or polygon features.

        params: {"in_line_or_polygon_features": <Feature Layer>, "in_features": <Feature Layer>}
        Returns: {"success": True, "message": "Control points set."} or error
        """
        try:
            in_line_or_polygon_features = params.get("in_line_or_polygon_features")
            if in_line_or_polygon_features is None:
                return {"success": False, "error": "in_line_or_polygon_features parameter is required"}
            in_features = params.get("in_features")

            arcpy.cartography.SetControlPointAtIntersect(in_line_or_polygon_features, in_features)

            return {"success": True, "message": "Set control points at intersections successfully."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_control_point_by_angle(self, params):
        """Set Control Point By Angle

Places a control point at vertices along a line or polygon outline where the angle created by a change in line direction is less than or equal to a specified maximum angle.

        params: {"in_features": <Feature Layer>, "maximum_angle": <Double>}
        Returns: {"success": True, "message": "Control points set."} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            maximum_angle = params.get("maximum_angle")
            if maximum_angle is None:
                return {"success": False, "error": "maximum_angle parameter is required"}

            arcpy.cartography.SetControlPointByAngle(in_features, maximum_angle)

            return {"success": True, "message": "Set control points by angle successfully."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def aggregate_points(self, params):
        """Aggregate Points

Creates polygon features around clusters of proximate point features.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "aggregation_distance": <Linear Unit>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_features).name
                out_feature_class = arcpy.CreateUniqueName(f"{in_name}_Aggregated", aprx.defaultGeodatabase)
            aggregation_distance = params.get("aggregation_distance")
            if aggregation_distance is None: return {"success": False, "error": "aggregation_distance is required"}

            arcpy.cartography.AggregatePoints(in_features, out_feature_class, aggregation_distance)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def aggregate_polygons(self, params):
        """Aggregate Polygons

Combines polygons that are within a specified distance of each other into new polygons.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "aggregation_distance": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_features).name
                out_feature_class = arcpy.CreateUniqueName(f"{in_name}_Aggregated", aprx.defaultGeodatabase)
            aggregation_distance = params.get("aggregation_distance")
            if aggregation_distance is None: return {"success": False, "error": "aggregation_distance is required"}

            minimum_area = params.get("minimum_area")
            minimum_hole_size = params.get("minimum_hole_size")
            orthogonality_option = params.get("orthogonality_option")
            barrier_features = params.get("barrier_features")
            out_table = params.get("out_table")
            aggregate_field = params.get("aggregate_field")

            arcpy.cartography.AggregatePolygons(in_features, out_feature_class, aggregation_distance, minimum_area, minimum_hole_size, orthogonality_option, barrier_features, out_table, aggregate_field)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def collapse_dual_lines_to_centerline(self, params):
        """Collapse Dual Lines To Centerline

Derives centerlines from dual-line (double-line) features, such as road casings, based on specified width tolerances.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "maximum_width": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_features).name
                out_feature_class = arcpy.CreateUniqueName(f"{in_name}_Centerline", aprx.defaultGeodatabase)
            maximum_width = params.get("maximum_width")
            if maximum_width is None: return {"success": False, "error": "maximum_width is required"}
            minimum_width = params.get("minimum_width")

            arcpy.cartography.CollapseDualLinesToCenterline(in_features, out_feature_class, maximum_width, minimum_width)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def collapse_hydro_polygon(self, params):
        """Collapse Hydro Polygon

Collapses or partially collapses hydro polygons to a centerline based on a collapse width.

        params: {"in_features": <Feature Layer>, "out_line_feature_class": <Feature Class>, "merge_adjacent_input_polygons": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            out_line_feature_class = params.get("out_line_feature_class")
            if out_line_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_features).name
                out_line_feature_class = arcpy.CreateUniqueName(f"{in_name}_Hydro_Centerline", aprx.defaultGeodatabase)

            merge_adjacent_input_polygons = params.get("merge_adjacent_input_polygons")
            connecting_features = params.get("connecting_features")
            collapse_width = params.get("collapse_width")
            collapse_width_tolerance = params.get("collapse_width_tolerance")
            minimum_length = params.get("minimum_length")
            out_poly_feature_class = params.get("out_poly_feature_class")

            arcpy.cartography.CollapseHydroPolygon(in_features, out_line_feature_class, merge_adjacent_input_polygons, connecting_features, collapse_width, collapse_width_tolerance, minimum_length, out_poly_feature_class)

            output_name = os.path.basename(out_line_feature_class)
            self._add_to_map(out_line_feature_class)
            if out_poly_feature_class:
                self._add_to_map(out_poly_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_line_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def collapse_road_detail(self, params):
        """Collapse Road Detail

Collapses small, open configurations of road segments that interrupt the general trend of a road network.

        params: {"in_features": <Feature Layer>, "collapse_distance": <Linear Unit>, "output_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            collapse_distance = params.get("collapse_distance")
            if collapse_distance is None: return {"success": False, "error": "collapse_distance is required"}
            output_feature_class = params.get("output_feature_class")
            if output_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_features).name
                output_feature_class = arcpy.CreateUniqueName(f"{in_name}_Collapsed", aprx.defaultGeodatabase)

            locking_field = params.get("locking_field")

            arcpy.cartography.CollapseRoadDetail(in_features, collapse_distance, output_feature_class, locking_field)

            output_name = os.path.basename(output_feature_class)
            self._add_to_map(output_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": output_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_cartographic_partitions(self, params):
        """Create Cartographic Partitions

Creates a mesh of polygon features that cover the input feature class.

        params: {"in_features": <Feature Layer>, "out_features": <Feature Class>, "feature_count": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            out_features = params.get("out_features")
            if out_features is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_features).name
                out_features = arcpy.CreateUniqueName(f"{in_name}_Partitions", aprx.defaultGeodatabase)
            feature_count = params.get("feature_count")
            if feature_count is None: return {"success": False, "error": "feature_count is required"}
            partition_method = params.get("partition_method")

            arcpy.cartography.CreateCartographicPartitions(in_features, out_features, feature_count, partition_method)

            output_name = os.path.basename(out_features)
            self._add_to_map(out_features)
            return {"success": True, "output_layer": output_name, "output_path": out_features}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delineate_built_up_areas(self, params):
        """Delineate Built-Up Areas

Creates polygons to represent built-up areas by delineating densely clustered arrangements of buildings on small-scale maps.

        params: {"in_buildings": <Feature Layer>, "identifier_field": <String>, "edge_features": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_buildings = params.get("in_buildings")
            if in_buildings is None: return {"success": False, "error": "in_buildings is required"}
            identifier_field = params.get("identifier_field")
            edge_features = params.get("edge_features")
            grouping_distance = params.get("grouping_distance")
            if grouping_distance is None: return {"success": False, "error": "grouping_distance is required"}
            minimum_detail_size = params.get("minimum_detail_size")
            if minimum_detail_size is None: return {"success": False, "error": "minimum_detail_size is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_buildings).name
                out_feature_class = arcpy.CreateUniqueName(f"{in_name}_BuiltUpAreas", aprx.defaultGeodatabase)

            minimum_building_count = params.get("minimum_building_count")

            arcpy.cartography.DelineateBuiltUpAreas(in_buildings, identifier_field, edge_features, grouping_distance, minimum_detail_size, out_feature_class, minimum_building_count)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def merge_divided_roads(self, params):
        """Merge Divided Roads

Generates single-line road features in place of matched pairs of divided road lanes.

        params: {"in_features": <Feature Layer>, "merge_field": <Field>, "merge_distance": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            merge_field = params.get("merge_field")
            if merge_field is None: return {"success": False, "error": "merge_field is required"}
            merge_distance = params.get("merge_distance")
            if merge_distance is None: return {"success": False, "error": "merge_distance is required"}
            out_features = params.get("out_features")
            if out_features is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_features).name
                out_features = arcpy.CreateUniqueName(f"{in_name}_Merged", aprx.defaultGeodatabase)

            out_displacement_features = params.get("out_displacement_features")
            character_field = params.get("character_field")
            out_table = params.get("out_table")

            arcpy.cartography.MergeDividedRoads(in_features, merge_field, merge_distance, out_features, out_displacement_features, character_field, out_table)

            output_name = os.path.basename(out_features)
            self._add_to_map(out_features)
            return {"success": True, "output_layer": output_name, "output_path": out_features}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def simplify_building(self, params):
        """Simplify Building

Simplifies the boundary or footprint of building polygons while maintaining their essential shape and size.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "simplification_tolerance": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_features).name
                out_feature_class = arcpy.CreateUniqueName(f"{in_name}_Simplified", aprx.defaultGeodatabase)
            simplification_tolerance = params.get("simplification_tolerance")
            if simplification_tolerance is None: return {"success": False, "error": "simplification_tolerance is required"}

            minimum_area = params.get("minimum_area")
            conflict_option = params.get("conflict_option")
            in_barriers = params.get("in_barriers")
            collapsed_point_option = params.get("collapsed_point_option")

            arcpy.cartography.SimplifyBuilding(in_features, out_feature_class, simplification_tolerance, minimum_area, conflict_option, in_barriers, collapsed_point_option)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def simplify_line(self, params):
        """Simplify Line

Simplifies lines by removing relatively extraneous vertices while preserving essential shape.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "algorithm": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_features).name
                out_feature_class = arcpy.CreateUniqueName(f"{in_name}_Simplified", aprx.defaultGeodatabase)
            algorithm = params.get("algorithm")
            if algorithm is None: return {"success": False, "error": "algorithm is required"}
            tolerance = params.get("tolerance")
            if tolerance is None: return {"success": False, "error": "tolerance is required"}

            error_resolving_option = params.get("error_resolving_option")
            collapsed_point_option = params.get("collapsed_point_option")
            error_checking_option = params.get("error_checking_option")
            in_barriers = params.get("in_barriers")
            error_option = params.get("error_option")

            arcpy.cartography.SimplifyLine(in_features, out_feature_class, algorithm, tolerance, error_resolving_option, collapsed_point_option, error_checking_option, in_barriers, error_option)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def simplify_polygon(self, params):
        """Simplify Polygon

Simplifies polygons by removing relatively extraneous vertices while preserving essential shape.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "algorithm": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_features).name
                out_feature_class = arcpy.CreateUniqueName(f"{in_name}_Simplified", aprx.defaultGeodatabase)
            algorithm = params.get("algorithm")
            if algorithm is None: return {"success": False, "error": "algorithm is required"}
            tolerance = params.get("tolerance")
            if tolerance is None: return {"success": False, "error": "tolerance is required"}

            minimum_area = params.get("minimum_area")
            error_option = params.get("error_option")
            collapsed_point_option = params.get("collapsed_point_option")
            in_barriers = params.get("in_barriers")

            arcpy.cartography.SimplifyPolygon(in_features, out_feature_class, algorithm, tolerance, minimum_area, error_option, collapsed_point_option, in_barriers)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def simplify_shared_edges(self, params):
        """Simplify Shared Edges

Simplifies the edges of input features while maintaining the topological relationship with edges shared with other features.

        params: {"in_features": <Feature Layer>, "algorithm": <String>, "tolerance": <Linear Unit>, ...}
        Returns: {"success": True, "message": "Simplification complete."} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            algorithm = params.get("algorithm")
            if algorithm is None: return {"success": False, "error": "algorithm is required"}
            tolerance = params.get("tolerance")
            if tolerance is None: return {"success": False, "error": "tolerance is required"}

            shared_edge_features = params.get("shared_edge_features")
            minimum_area = params.get("minimum_area")
            in_barriers = params.get("in_barriers")

            arcpy.cartography.SimplifySharedEdges(in_features, algorithm, tolerance, shared_edge_features, minimum_area, in_barriers)

            return {"success": True, "message": "Simplify Shared Edges completed successfully."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def smooth_line(self, params):
        """Smooth Line

Smooths sharp angles in lines to improve aesthetic or cartographic quality.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "algorithm": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_features).name
                out_feature_class = arcpy.CreateUniqueName(f"{in_name}_Smoothed", aprx.defaultGeodatabase)
            algorithm = params.get("algorithm")
            if algorithm is None: return {"success": False, "error": "algorithm is required"}
            tolerance = params.get("tolerance")
            if tolerance is None: return {"success": False, "error": "tolerance is required"}

            endpoint_option = params.get("endpoint_option")
            error_option = params.get("error_option")
            in_barriers = params.get("in_barriers")

            arcpy.cartography.SmoothLine(in_features, out_feature_class, algorithm, tolerance, endpoint_option, error_option, in_barriers)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def smooth_polygon(self, params):
        """Smooth Polygon

Smooths sharp angles in polygon outlines to improve aesthetic or cartographic quality.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "algorithm": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_features).name
                out_feature_class = arcpy.CreateUniqueName(f"{in_name}_Smoothed", aprx.defaultGeodatabase)
            algorithm = params.get("algorithm")
            if algorithm is None: return {"success": False, "error": "algorithm is required"}
            tolerance = params.get("tolerance")
            if tolerance is None: return {"success": False, "error": "tolerance is required"}

            endpoint_option = params.get("endpoint_option")
            error_option = params.get("error_option")
            in_barriers = params.get("in_barriers")

            arcpy.cartography.SmoothPolygon(in_features, out_feature_class, algorithm, tolerance, endpoint_option, error_option, in_barriers)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def smooth_shared_edges(self, params):
        """Smooth Shared Edges

Smooths the edges of the input features while maintaining the topological relationship with edges shared with other features.

        params: {"in_features": <Feature Layer>, "algorithm": <String>, "tolerance": <Linear Unit>, ...}
        Returns: {"success": True, "message": "Smoothing complete."} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            algorithm = params.get("algorithm")
            if algorithm is None: return {"success": False, "error": "algorithm is required"}
            tolerance = params.get("tolerance")
            if tolerance is None: return {"success": False, "error": "tolerance is required"}

            shared_edge_features = params.get("shared_edge_features")
            in_barriers = params.get("in_barriers")

            arcpy.cartography.SmoothSharedEdges(in_features, algorithm, tolerance, shared_edge_features, in_barriers)

            return {"success": True, "message": "Smooth Shared Edges completed successfully."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def thin_road_network(self, params):
        """Thin Road Network

Generates a simplified road network that retains connectivity and general character for display at a smaller scale.

        params: {"in_features": <Feature Layer>, "minimum_length": <Linear Unit>, "invisibility_field": <String>, ...}
        Returns: {"success": True, "message": "Thinning complete."} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            minimum_length = params.get("minimum_length")
            if minimum_length is None: return {"success": False, "error": "minimum_length is required"}
            invisibility_field = params.get("invisibility_field")
            if invisibility_field is None: return {"success": False, "error": "invisibility_field is required"}
            hierarchy_field = params.get("hierarchy_field")
            if hierarchy_field is None: return {"success": False, "error": "hierarchy_field is required"}

            arcpy.cartography.ThinRoadNetwork(in_features, minimum_length, invisibility_field, hierarchy_field)

            return {"success": True, "message": "Thin Road Network completed successfully."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def detect_graphic_conflict(self, params):
        """Detect Graphic Conflict

Creates polygons where two or more symbolized features graphically conflict.

        params: {"in_features": <Layer>, "conflict_features": <Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            conflict_features = params.get("conflict_features")
            if conflict_features is None: return {"success": False, "error": "conflict_features is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_features).name
                out_feature_class = arcpy.CreateUniqueName(f"{in_name}_Conflicts", aprx.defaultGeodatabase)

            conflict_distance = params.get("conflict_distance")
            line_connection_allowance = params.get("line_connection_allowance")

            arcpy.cartography.DetectGraphicConflict(in_features, conflict_features, out_feature_class, conflict_distance, line_connection_allowance)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def propagate_displacement(self, params):
        """Propagate Displacement

Propagates the displacement resulting from road adjustment to adjacent features to reestablish spatial relationships.

        params: {"in_features": <Feature Layer>, "displacement_features": <Feature Layer>, "adjustment_style": <String>}
        Returns: {"success": True, "message": "Displacement propagated."} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            displacement_features = params.get("displacement_features")
            if displacement_features is None: return {"success": False, "error": "displacement_features is required"}
            adjustment_style = params.get("adjustment_style")
            if adjustment_style is None: return {"success": False, "error": "adjustment_style is required"}

            arcpy.cartography.PropagateDisplacement(in_features, displacement_features, adjustment_style)

            return {"success": True, "message": "Propagate Displacement completed successfully."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def resolve_road_conflicts(self, params):
        """Resolve Road Conflicts

Resolves graphic conflicts among symbolized road features by adjusting portions of line segments.

        params: {"in_layers": <Layer>, "hierarchy_field": <String>, "out_displacement_features": <Feature Class>}
        Returns: {"success": True, "message": "Road conflicts resolved."} or error
        """
        try:
            in_layers = params.get("in_layers")
            if in_layers is None: return {"success": False, "error": "in_layers is required"}
            hierarchy_field = params.get("hierarchy_field")
            if hierarchy_field is None: return {"success": False, "error": "hierarchy_field is required"}
            out_displacement_features = params.get("out_displacement_features")

            arcpy.cartography.ResolveRoadConflicts(in_layers, hierarchy_field, out_displacement_features)

            if out_displacement_features:
                self._add_to_map(out_displacement_features)

            return {"success": True, "message": "Resolve Road Conflicts completed successfully."}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def resolve_building_conflicts(self, params):
        """Resolve Building Conflicts

Resolves symbol conflicts among buildings with respect to linear barrier features by moving, resizing, or hiding buildings.

        params: {"in_buildings": <Layer>, "invisibility_field": <String>, "in_barriers": <Value Table>, ...}
        Returns: {"success": True, "message": "Building conflicts resolved."} or error
        """
        try:
            in_buildings = params.get("in_buildings")
            if in_buildings is None: return {"success": False, "error": "in_buildings is required"}
            invisibility_field = params.get("invisibility_field")
            if invisibility_field is None: return {"success": False, "error": "invisibility_field is required"}
            in_barriers = params.get("in_barriers")
            if in_barriers is None: return {"success": False, "error": "in_barriers is required"}
            building_gap = params.get("building_gap")
            if building_gap is None: return {"success": False, "error": "building_gap is required"}
            minimum_size = params.get("minimum_size")
            if minimum_size is None: return {"success": False, "error": "minimum_size is required"}

            hierarchy_field = params.get("hierarchy_field")

            arcpy.cartography.ResolveBuildingConflicts(in_buildings, invisibility_field, in_barriers, building_gap, minimum_size, hierarchy_field)

            return {"success": True, "message": "Resolve Building Conflicts completed successfully."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_adjacent_fields(self, params):
        """Calculate Adjacent Fields

Creates fields and calculates values for the neighboring pages (polygon) of a grid polygon feature class.

        params: {"in_features": <Feature Layer>, "in_field": <Field>}
        Returns: {"success": True, "message": "Adjacent fields calculated."} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            in_field = params.get("in_field")
            if in_field is None: return {"success": False, "error": "in_field is required"}

            arcpy.cartography.CalculateAdjacentFields(in_features, in_field)

            return {"success": True, "message": "Calculate Adjacent Fields completed successfully."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_central_meridian_and_parallels(self, params):
        """Calculate Central Meridian and Parallels

Calculates the central meridian and optional standard parallels based on the center point of a feature's extent.

        params: {"in_features": <Feature Layer>, "in_field": <Field>, "standard_offset": <Double>}
        Returns: {"success": True, "message": "Calculation complete."} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            in_field = params.get("in_field")
            if in_field is None: return {"success": False, "error": "in_field is required"}
            standard_offset = params.get("standard_offset")

            # Note: The tool name in arcpy is CalculateCentralMeridianAndParallels, not ...and_Parallels
            arcpy.cartography.CalculateCentralMeridianAndParallels(in_features, in_field, standard_offset)

            return {"success": True, "message": "Calculate Central Meridian and Parallels completed successfully."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_grid_convergence_angle(self, params):
        """Calculate Grid Convergence Angle

Calculates the rotation angle for true north based on the center point of each feature in a feature class.

        params: {"in_features": <Feature Layer>, "angle_field": <Field>, "rotation_method": <String>, ...}
        Returns: {"success": True, "message": "Angle calculation complete."} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            angle_field = params.get("angle_field")
            if angle_field is None: return {"success": False, "error": "angle_field is required"}
            rotation_method = params.get("rotation_method")
            coordinate_sys_field = params.get("coordinate_sys_field")

            arcpy.cartography.CalculateGridConvergenceAngle(in_features, angle_field, rotation_method, coordinate_sys_field)

            return {"success": True, "message": "Calculate Grid Convergence Angle completed successfully."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_utm_zone(self, params):
        """Calculate UTM Zone

Calculates the UTM zone of each feature based on the center point and stores this spatial reference string in a specified field.

        params: {"in_features": <Feature Layer>, "in_field": <Field>}
        Returns: {"success": True, "message": "UTM Zone calculated."} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            in_field = params.get("in_field")
            if in_field is None: return {"success": False, "error": "in_field is required"}

            arcpy.cartography.CalculateUTMZone(in_features, in_field)

            return {"success": True, "message": "Calculate UTM Zone completed successfully."}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def grid_index_features(self, params):
        """Grid Index Features

Creates a grid of rectangular polygon features that can be used as an index to specify pages in a spatial map series.

        params: {"out_feature_class": <Feature Class>, "in_features": <Feature Layer; Raster Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("GridIndex", aprx.defaultGeodatabase)

            in_features = params.get("in_features")
            intersect_feature = params.get("intersect_feature")
            use_page_unit = params.get("use_page_unit")
            scale = params.get("scale")
            polygon_width = params.get("polygon_width")
            polygon_height = params.get("polygon_height")
            origin_coord = params.get("origin_coord")
            number_rows = params.get("number_rows")
            number_columns = params.get("number_columns")
            starting_page_number = params.get("starting_page_number")
            label_from_origin = params.get("label_from_origin")

            arcpy.cartography.GridIndexFeatures(out_feature_class, in_features, intersect_feature, use_page_unit, scale, polygon_width, polygon_height, origin_coord, number_rows, number_columns, starting_page_number, label_from_origin)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def strip_map_index_features(self, params):
        """Strip Map Index Features

Creates a series of rectangular polygons, or index features, that follow a single linear feature or a group of linear features.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "use_page_unit": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(in_features).name
                out_feature_class = arcpy.CreateUniqueName(f"{in_name}_StripMapIndex", aprx.defaultGeodatabase)

            use_page_unit = params.get("use_page_unit")
            scale = params.get("scale")
            length_along_line = params.get("length_along_line")
            page_orientation = params.get("page_orientation")
            overlap_percentage = params.get("overlap_percentage")
            starting_page_number = params.get("starting_page_number")
            direction_type = params.get("direction_type")

            arcpy.cartography.StripMapIndexFeatures(in_features, out_feature_class, use_page_unit, scale, length_along_line, page_orientation, overlap_percentage, starting_page_number, direction_type)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def cul_de_sac_masks(self, params):
        """Cul-De-Sac Masks

Creates a feature class of polygon masks from a symbolized input line layer.

        params: {"input_layer": <Layer>, "output_fc": <Feature Class>, "reference_scale": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            input_layer = params.get("input_layer")
            if input_layer is None: return {"success": False, "error": "input_layer is required"}
            output_fc = params.get("output_fc")
            if output_fc is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(input_layer).name
                output_fc = arcpy.CreateUniqueName(f"{in_name}_CulDeSacMasks", aprx.defaultGeodatabase)
            reference_scale = params.get("reference_scale")
            if reference_scale is None: return {"success": False, "error": "reference_scale is required"}
            spatial_reference = params.get("spatial_reference")
            if spatial_reference is None: return {"success": False, "error": "spatial_reference is required"}
            margin = params.get("margin")
            if margin is None: return {"success": False, "error": "margin is required"}

            attributes = params.get("attributes")

            arcpy.cartography.CulDeSacMasks(input_layer, output_fc, reference_scale, spatial_reference, margin, attributes)

            output_name = os.path.basename(output_fc)
            self._add_to_map(output_fc)
            return {"success": True, "output_layer": output_name, "output_path": output_fc}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def feature_outline_masks(self, params):
        """Feature Outline Masks

Creates mask polygons at a specified distance and shape around the symbolized features in the input layer.

        params: {"input_layer": <Annotation Layer>, "output_fc": <Feature Class>, "reference_scale": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            input_layer = params.get("input_layer")
            if input_layer is None: return {"success": False, "error": "input_layer is required"}
            output_fc = params.get("output_fc")
            if output_fc is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(input_layer).name
                output_fc = arcpy.CreateUniqueName(f"{in_name}_OutlineMasks", aprx.defaultGeodatabase)
            reference_scale = params.get("reference_scale")
            if reference_scale is None: return {"success": False, "error": "reference_scale is required"}
            spatial_reference = params.get("spatial_reference")
            if spatial_reference is None: return {"success": False, "error": "spatial_reference is required"}
            margin = params.get("margin")
            if margin is None: return {"success": False, "error": "margin is required"}
            method = params.get("method")
            if method is None: return {"success": False, "error": "method is required"}
            mask_for_non_placed_anno = params.get("mask_for_non_placed_anno")
            if mask_for_non_placed_anno is None: return {"success": False, "error": "mask_for_non_placed_anno is required"}

            attributes = params.get("attributes")
            preserve_small_sized_features = params.get("preserve_small_sized_features")

            arcpy.cartography.FeatureOutlineMasks(input_layer, output_fc, reference_scale, spatial_reference, margin, method, mask_for_non_placed_anno, attributes, preserve_small_sized_features)

            output_name = os.path.basename(output_fc)
            self._add_to_map(output_fc)
            return {"success": True, "output_layer": output_name, "output_path": output_fc}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def intersecting_layers_masks(self, params):
        """Intersecting Layers Masks

Creates masking polygons at a specified shape and size at the intersection of two symbolized input layers.

        params: {"masking_layer": <Annotation Layer>, "masked_layer": <Annotation Layer>, "output_fc": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            masking_layer = params.get("masking_layer")
            if masking_layer is None: return {"success": False, "error": "masking_layer is required"}
            masked_layer = params.get("masked_layer")
            if masked_layer is None: return {"success": False, "error": "masked_layer is required"}
            output_fc = params.get("output_fc")
            if output_fc is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                in_name = arcpy.Describe(masking_layer).name
                output_fc = arcpy.CreateUniqueName(f"{in_name}_IntersectingMasks", aprx.defaultGeodatabase)
            reference_scale = params.get("reference_scale")
            if reference_scale is None: return {"success": False, "error": "reference_scale is required"}
            spatial_reference = params.get("spatial_reference")
            if spatial_reference is None: return {"success": False, "error": "spatial_reference is required"}
            margin = params.get("margin")
            if margin is None: return {"success": False, "error": "margin is required"}
            method = params.get("method")
            if method is None: return {"success": False, "error": "method is required"}
            mask_for_non_placed_anno = params.get("mask_for_non_placed_anno")
            if mask_for_non_placed_anno is None: return {"success": False, "error": "mask_for_non_placed_anno is required"}

            attributes = params.get("attributes")

            arcpy.cartography.IntersectingLayersMasks(masking_layer, masked_layer, output_fc, reference_scale, spatial_reference, margin, method, mask_for_non_placed_anno, attributes)

            output_name = os.path.basename(output_fc)
            self._add_to_map(output_fc)
            return {"success": True, "output_layer": output_name, "output_path": output_fc}

        except Exception as e:
            return {"success": False, "error": str(e)}