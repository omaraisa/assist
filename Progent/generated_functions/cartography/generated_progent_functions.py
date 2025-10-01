# Generated ArcGIS Pro cartography Progent Functions
# Generated on 2025-10-01T13:54:58.197668
# Total tools: 51

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

    def annotate_selected_features(self, params):
        """Annotate Selected Features

Creates annotation for the selected features of a layer. The labeling properties defined in the annotation class properties of  the specified related annotation feature classes are used.

        params: {"in_map": <Map>, "in_layer": <Feature Layer>, "anno_layersannotation_layer_sublayer_sublayer": <Value Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_map = params.get("in_map")
    if in_map is None:
        return {"success": False, "error": "in_map parameter is required"}
    in_layer = params.get("in_layer")
    if in_layer is None:
        return {"success": False, "error": "in_layer parameter is required"}
    anno_layersannotation_layer_sublayer_sublayer = params.get("anno_layersannotation_layer_sublayer_sublayer")
    if anno_layersannotation_layer_sublayer_sublayer is None:
        return {"success": False, "error": "anno_layersannotation_layer_sublayer_sublayer parameter is required"}
    generate_unplaced = params.get("generate_unplaced")

            # Generate output name and path
            output_name = f"{in_map.replace(' ', '_')}_Annotate_Selected_Features"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Annotate Selected Features
            arcpy.AnnotateSelectedFeatures(in_map, in_layer, anno_layersannotation_layer_sublayer_sublayer, generate_unplaced)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Contour_Annotation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Contour Annotation
            arcpy.ContourAnnotation(in_features, out_geodatabase, contour_label_field, reference_scale_value, out_layer, contour_color, contour_type_field, contour_alignment, enable_laddering)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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

            # Generate output name and path
            output_name = f"{input_map.replace(' ', '_')}_Convert_Labels_To_Annotation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Convert Labels To Annotation
            arcpy.ConvertLabelsToAnnotation(input_map, conversion_scale, output_geodatabase, anno_suffix, extent, generate_unplaced, require_symbol_id, feature_linked, auto_create, update_on_shape_change, output_group_layer, which_layers, single_layer, multiple_feature_classes, merge_label_classes)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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

            # Generate output name and path
            output_name = f"{input_map.replace(' ', '_')}_Convert_Labels_To_Graphics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Convert Labels To Graphics
            arcpy.ConvertLabelsToGraphics(input_map, conversion_scale, which_layers, single_layer, graphics_suffix, extent, multiple_graphics_layers, generate_unplaced, output_group_layer)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def map_server_cache_tiling_scheme_to_polygons(self, params):
        """Map Server Cache Tiling Scheme To Polygons

Creates a polygon feature class from an existing tiling scheme. This tool subdivides a map extent using the same scales as an existing map service cache tiling scheme and creates tiles over a large area, or supertile. Since the supertile extent is larger than the actual tiles defined in the tiling scheme, tiles used as input to the Tiled Labels To Annotation tool can convert labels to annotation over a larger area at a time. This process minimizes annotation duplication across tiles.

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
    levelslevel = params.get("levelslevel")

            # Generate output name and path
            output_name = f"{input_map.replace(' ', '_')}_Map_Server_Cache_Tiling_Scheme_To_Polygons"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Map Server Cache Tiling Scheme To Polygons
            arcpy.MapServerCacheTilingSchemeToPolygons(input_map, tiling_scheme, output_feature_class, use_map_extent, clip_to_horizon, antialiasing, levelslevel)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def tiled_labels_to_annotation(self, params):
        """Tiled Labels To Annotation

Converts labels to annotation for layers in a map based on a polygon index layer. The tool divides a map into tiles and creates annotation for each tile in turn. This is useful for converting a large number of labels to annotation. The polygon index layer can be generated using the Map Server Cache Tiling Scheme To Polygons or Grid Index Features tool or any other polygon feature class that covers the area where you want to create annotation.

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

            # Generate output name and path
            output_name = f"{input_map.replace(' ', '_')}_Tiled_Labels_To_Annotation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Tiled Labels To Annotation
            arcpy.TiledLabelsToAnnotation(input_map, polygon_index_layer, out_geodatabase, out_layer, anno_suffix, reference_scale_value, reference_scale_field, tile_id_field, coordinate_sys_field, map_rotation_field, feature_linked, generate_unplaced_annotation, which_layers, single_layer, require_symbol_id, auto_create, update_on_shape_change, multiple_feature_classes, merge_label_classes)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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

            # Generate output name and path
            output_name = f"{in_anno_features.replace(' ', '_')}_Update_Annotation_Reference_Scale"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Update Annotation Reference Scale
            arcpy.UpdateAnnotationReferenceScale(in_anno_features, reference_scale)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
        return {"success": False, "error": "out_features parameter is required"}
    method = params.get("method")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Generate_Contiguous_Cartogram"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Contiguous Cartogram
            arcpy.GenerateContiguousCartogram(in_features, field_name, out_features, method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def align_marker_to_stroke_or_fill(self, params):
        """Align Marker To Stroke Or Fill

Aligns the marker symbol layers of a point feature class to the nearest stroke or fill symbol layers in a line or polygon feature class within a specified search distance.

        params: {"in_point_features": <Layer>, "in_line_or_polygon_features": <Layer>, "search_distance": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
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

            # Generate output name and path
            output_name = f"{in_point_features.replace(' ', '_')}_Align_Marker_To_Stroke_Or_Fill"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Align Marker To Stroke Or Fill
            arcpy.AlignMarkerToStrokeOrFill(in_point_features, in_line_or_polygon_features, search_distance, marker_orientation)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_color_theorem_field(self, params):
        """Calculate Color Theorem Field

Populates an integer field to use for symbolizing polygons with a small number of colors and ensuring no two adjacent polygons are the same color. Values are assigned to each polygon based on the theorem that only a small number of colors, often four or five, are needed to ensure no two adjacent polygons in a 2-dimensional map are the same color. Overlapping and multipart polygons can increase the number of colors required. The assigned values will be integers ranging from 1 to the number of unique values assigned.

        params: {"in_features": <Feature Layer>, "field_name": <Field>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    field_name = params.get("field_name")
    if field_name is None:
        return {"success": False, "error": "field_name parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Calculate_Color_Theorem_Field"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Color Theorem Field
            arcpy.CalculateColorTheoremField(in_features, field_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_line_caps(self, params):
        """Calculate Line Caps

Modifies the cap type for stroke symbol layers in the line symbols of the input layer.

        params: {"in_features": <Layer>, "cap_type": <String>, "dangle_option": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    cap_type = params.get("cap_type")
    dangle_option = params.get("dangle_option")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Calculate_Line_Caps"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Line Caps
            arcpy.CalculateLineCaps(in_features, cap_type, dangle_option)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_polygon_main_angle(self, params):
        """Calculate Polygon Main Angle

Calculates the dominant angles of  input polygon features and assigns the values to a field to use to orient symbology such as markers or hatch lines within the polygons.

        params: {"in_features": <Feature Layer>, "angle_field": <Field>, "rotation_method": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    angle_field = params.get("angle_field")
    if angle_field is None:
        return {"success": False, "error": "angle_field parameter is required"}
    rotation_method = params.get("rotation_method")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Calculate_Polygon_Main_Angle"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Polygon Main Angle
            arcpy.CalculatePolygonMainAngle(in_features, angle_field, rotation_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def convert_control_points_to_vertices(self, params):
        """Convert Control Points To Vertices

Converts control points in a line or polygon feature layer to vertices.

        params: {"in_features": <Feature Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Convert_Control_Points_To_Vertices"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Convert Control Points To Vertices
            arcpy.ConvertControlPointsToVertices(in_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def convert_marker_placement_to_points(self, params):
        """Convert Marker Placement To Points

Creates points from the markers of a marker placement in a symbolized  polygon feature.

        params: {"in_layer": <Layer>, "out_feature_class": <Feature Class>, "create_multipoints": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_layer = params.get("in_layer")
    if in_layer is None:
        return {"success": False, "error": "in_layer parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    create_multipoints = params.get("create_multipoints")
    boundary_option = params.get("boundary_option")
    boundary_distance = params.get("boundary_distance")
    boundary_distance_field = params.get("boundary_distance_field")
    boundary_distance_unit = params.get("boundary_distance_unit")
    in_barriersbarrier_layer_barrier_distance_barrier_distance_field_barrier_distance_unit = params.get("in_barriersbarrier_layer_barrier_distance_barrier_distance_field_barrier_distance_unit")
    keep_at_least_one_marker = params.get("keep_at_least_one_marker")
    displacement_method = params.get("displacement_method")
    minimum_marker_distance = params.get("minimum_marker_distance")

            # Generate output name and path
            output_name = f"{in_layer.replace(' ', '_')}_Convert_Marker_Placement_To_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Convert Marker Placement To Points
            arcpy.ConvertMarkerPlacementToPoints(in_layer, out_feature_class, create_multipoints, boundary_option, boundary_distance, boundary_distance_field, boundary_distance_unit, in_barriersbarrier_layer_barrier_distance_barrier_distance_field_barrier_distance_unit, keep_at_least_one_marker, displacement_method, minimum_marker_distance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
    if in_above_features is None:
        return {"success": False, "error": "in_above_features parameter is required"}
    in_below_features = params.get("in_below_features")
    if in_below_features is None:
        return {"success": False, "error": "in_below_features parameter is required"}
    margin_along = params.get("margin_along")
    if margin_along is None:
        return {"success": False, "error": "margin_along parameter is required"}
    margin_across = params.get("margin_across")
    if margin_across is None:
        return {"success": False, "error": "margin_across parameter is required"}
    out_overpass_feature_class = params.get("out_overpass_feature_class")
    if out_overpass_feature_class is None:
        return {"success": False, "error": "out_overpass_feature_class parameter is required"}
    out_mask_relationship_class = params.get("out_mask_relationship_class")
    if out_mask_relationship_class is None:
        return {"success": False, "error": "out_mask_relationship_class parameter is required"}
    where_clause = params.get("where_clause")
    out_decoration_feature_class = params.get("out_decoration_feature_class")
    wing_type = params.get("wing_type")
    wing_tick_length = params.get("wing_tick_length")

            # Generate output name and path
            output_name = f"{in_above_features.replace(' ', '_')}_Create_Overpass"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Overpass
            arcpy.CreateOverpass(in_above_features, in_below_features, margin_along, margin_across, out_overpass_feature_class, out_mask_relationship_class, where_clause, out_decoration_feature_class, wing_type, wing_tick_length)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
    if in_above_features is None:
        return {"success": False, "error": "in_above_features parameter is required"}
    in_below_features = params.get("in_below_features")
    if in_below_features is None:
        return {"success": False, "error": "in_below_features parameter is required"}
    margin_along = params.get("margin_along")
    if margin_along is None:
        return {"success": False, "error": "margin_along parameter is required"}
    margin_across = params.get("margin_across")
    if margin_across is None:
        return {"success": False, "error": "margin_across parameter is required"}
    out_underpass_feature_class = params.get("out_underpass_feature_class")
    if out_underpass_feature_class is None:
        return {"success": False, "error": "out_underpass_feature_class parameter is required"}
    out_mask_relationship_class = params.get("out_mask_relationship_class")
    if out_mask_relationship_class is None:
        return {"success": False, "error": "out_mask_relationship_class parameter is required"}
    where_clause = params.get("where_clause")
    out_decoration_feature_class = params.get("out_decoration_feature_class")
    wing_type = params.get("wing_type")
    wing_tick_length = params.get("wing_tick_length")

            # Generate output name and path
            output_name = f"{in_above_features.replace(' ', '_')}_Create_Underpass"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Underpass
            arcpy.CreateUnderpass(in_above_features, in_below_features, margin_along, margin_across, out_underpass_feature_class, out_mask_relationship_class, where_clause, out_decoration_feature_class, wing_type, wing_tick_length)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def disperse_markers(self, params):
        """Disperse Markers

Finds point symbols that overlap or are too close to one another based on symbology at reference scale and spreads them apart based on a minimum spacing and dispersal pattern.

        params: {"in_point_features": <Layer>, "minimum_spacing": <Linear Unit>, "dispersal_pattern": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_point_features = params.get("in_point_features")
    if in_point_features is None:
        return {"success": False, "error": "in_point_features parameter is required"}
    minimum_spacing = params.get("minimum_spacing")
    if minimum_spacing is None:
        return {"success": False, "error": "minimum_spacing parameter is required"}
    dispersal_pattern = params.get("dispersal_pattern")

            # Generate output name and path
            output_name = f"{in_point_features.replace(' ', '_')}_Disperse_Markers"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Disperse Markers
            arcpy.DisperseMarkers(in_point_features, minimum_spacing, dispersal_pattern)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
    if upper_lines is None:
        return {"success": False, "error": "upper_lines parameter is required"}
    lower_lines = params.get("lower_lines")
    if lower_lines is None:
        return {"success": False, "error": "lower_lines parameter is required"}
    output_feature_class = params.get("output_feature_class")
    if output_feature_class is None:
        return {"success": False, "error": "output_feature_class parameter is required"}
    output_type = params.get("output_type")
    fully_connected = params.get("fully_connected")
    search_distance = params.get("search_distance")
    interval = params.get("interval")
    minimum_length = params.get("minimum_length")
    alternate_hachures = params.get("alternate_hachures")
    perpendicular = params.get("perpendicular")
    polygon_base_width = params.get("polygon_base_width")

            # Generate output name and path
            output_name = f"{upper_lines.replace(' ', '_')}_Generate_Hachures_For_Defined_Slopes"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Hachures For Defined Slopes
            arcpy.GenerateHachuresForDefinedSlopes(upper_lines, lower_lines, output_feature_class, output_type, fully_connected, search_distance, interval, minimum_length, alternate_hachures, perpendicular, polygon_base_width)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_control_point_at_intersect(self, params):
        """Set Control Point At Intersect

Creates a control point at vertices that are shared by one or more line or polygon features. This tool is commonly used to synchronize boundary symbology on adjacent polygons.

        params: {"in_line_or_polygon_features": <Feature Layer>, "in_features": <Feature Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_line_or_polygon_features = params.get("in_line_or_polygon_features")
    if in_line_or_polygon_features is None:
        return {"success": False, "error": "in_line_or_polygon_features parameter is required"}
    in_features = params.get("in_features")

            # Generate output name and path
            output_name = f"{in_line_or_polygon_features.replace(' ', '_')}_Set_Control_Point_At_Intersect"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Set Control Point At Intersect
            arcpy.SetControlPointAtIntersect(in_line_or_polygon_features, in_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_control_point_by_angle(self, params):
        """Set Control Point By Angle

Places a control point at vertices along a line or polygon outline where the angle created by a change in line direction is less than or equal to a specified maximum angle.

        params: {"in_features": <Feature Layer>, "maximum_angle": <Double>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    maximum_angle = params.get("maximum_angle")
    if maximum_angle is None:
        return {"success": False, "error": "maximum_angle parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Set_Control_Point_By_Angle"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Set Control Point By Angle
            arcpy.SetControlPointByAngle(in_features, maximum_angle)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    aggregation_distance = params.get("aggregation_distance")
    if aggregation_distance is None:
        return {"success": False, "error": "aggregation_distance parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Aggregate_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Aggregate Points
            arcpy.AggregatePoints(in_features, out_feature_class, aggregation_distance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    aggregation_distance = params.get("aggregation_distance")
    if aggregation_distance is None:
        return {"success": False, "error": "aggregation_distance parameter is required"}
    minimum_area = params.get("minimum_area")
    minimum_hole_size = params.get("minimum_hole_size")
    orthogonality_option = params.get("orthogonality_option")
    barrier_features = params.get("barrier_features")
    out_table = params.get("out_table")
    aggregate_field = params.get("aggregate_field")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Aggregate_Polygons"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Aggregate Polygons
            arcpy.AggregatePolygons(in_features, out_feature_class, aggregation_distance, minimum_area, minimum_hole_size, orthogonality_option, barrier_features, out_table, aggregate_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    maximum_width = params.get("maximum_width")
    if maximum_width is None:
        return {"success": False, "error": "maximum_width parameter is required"}
    minimum_width = params.get("minimum_width")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Collapse_Dual_Lines_To_Centerline"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Collapse Dual Lines To Centerline
            arcpy.CollapseDualLinesToCenterline(in_features, out_feature_class, maximum_width, minimum_width)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def collapse_hydro_polygon(self, params):
        """Collapse Hydro Polygon

Collapses or partially collapses hydro polygons to a 

centerline based on a collapse width.

        params: {"in_features": <Feature Layer>, "out_line_feature_class": <Feature Class>, "merge_adjacent_input_polygons": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_line_feature_class = params.get("out_line_feature_class")
    if out_line_feature_class is None:
        return {"success": False, "error": "out_line_feature_class parameter is required"}
    merge_adjacent_input_polygons = params.get("merge_adjacent_input_polygons")
    connecting_features = params.get("connecting_features")
    collapse_width = params.get("collapse_width")
    collapse_width_tolerance = params.get("collapse_width_tolerance")
    minimum_length = params.get("minimum_length")
    out_poly_feature_class = params.get("out_poly_feature_class")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Collapse_Hydro_Polygon"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Collapse Hydro Polygon
            arcpy.CollapseHydroPolygon(in_features, out_line_feature_class, merge_adjacent_input_polygons, connecting_features, collapse_width, collapse_width_tolerance, minimum_length, out_poly_feature_class)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def collapse_road_detail(self, params):
        """Collapse Road Detail

Collapses small, open  configurations of road segments that interrupt the general trend of a road network, such as traffic circles, and replaces them with a simplified depiction. Configurations are collapsed regardless of  road class if the diameter across the open area is less than or equal to the Collapse Distance   parameter value. All roads from the input collection that are not collapsed will be copied to the output feature class. Learn more about how Collapse Road Detail works This tool is generally used to simplify a relatively large-scale road collection at a smaller scale when it is appropriate to depict traffic circles or other small interruptions to the network as a simple intersection. At medium scales, it may be preferable to retain these configurations as separate features and possibly exaggerate them. In that case,  consider using the Resolve Road Conflicts tool instead to ensure that symbolized lines are displayed without symbol conflicts.  If both Resolve Road Conflicts and Collapse Road Detail tools will be run on the same collection of roads, it is recommended that you run Collapse Road Detail first.

        params: {"in_features": <Feature Layer>, "collapse_distance": <Linear Unit>, "output_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    collapse_distance = params.get("collapse_distance")
    if collapse_distance is None:
        return {"success": False, "error": "collapse_distance parameter is required"}
    output_feature_class = params.get("output_feature_class")
    if output_feature_class is None:
        return {"success": False, "error": "output_feature_class parameter is required"}
    locking_field = params.get("locking_field")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Collapse_Road_Detail"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Collapse Road Detail
            arcpy.CollapseRoadDetail(in_features, collapse_distance, output_feature_class, locking_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_cartographic_partitions(self, params):
        """Create Cartographic Partitions

Creates a mesh of polygon features that cover the input feature class in which each output polygon encloses no more than a specified number of  input features or input vertices. as determined by the density and distribution of the input features. The resulting  partition feature class is ideally suited for the  Cartographic Partitions geoprocessing environment setting. The Cartographic Partitions environment setting causes certain geoprocessing tools to load and process input features by partition. These tools operate contextually, meaning that multiple features, possibly from multiple themes, must be loaded simultaneously. Memory limitations are encountered with large datasets. Partitioning allows large datasets to be processed by these tools in portions sequentially.

        params: {"in_features": <Feature Layer>, "out_features": <Feature Class>, "feature_count": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_features = params.get("out_features")
    if out_features is None:
        return {"success": False, "error": "out_features parameter is required"}
    feature_count = params.get("feature_count")
    if feature_count is None:
        return {"success": False, "error": "feature_count parameter is required"}
    partition_method = params.get("partition_method")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Create_Cartographic_Partitions"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Cartographic Partitions
            arcpy.CreateCartographicPartitions(in_features, out_features, feature_count, partition_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delineate_built_up_areas(self, params):
        """Delineate Built-Up Areas

Creates polygons to represent built-up areas by delineating densely clustered arrangements of buildings on small-scale maps. The boundaries—or edges—of the output polygons can be based on the location of other features such as roads or hydrology. Input buildings can be  attributed to identify those that can be replaced in maps by the built-up area polygons for a more generalized depiction.

        params: {"in_buildings": <Feature Layer>, "identifier_field": <String>, "edge_features": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_buildings = params.get("in_buildings")
    if in_buildings is None:
        return {"success": False, "error": "in_buildings parameter is required"}
    identifier_field = params.get("identifier_field")
    edge_features = params.get("edge_features")
    grouping_distance = params.get("grouping_distance")
    if grouping_distance is None:
        return {"success": False, "error": "grouping_distance parameter is required"}
    minimum_detail_size = params.get("minimum_detail_size")
    if minimum_detail_size is None:
        return {"success": False, "error": "minimum_detail_size parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    minimum_building_count = params.get("minimum_building_count")

            # Generate output name and path
            output_name = f"{in_buildings.replace(' ', '_')}_Delineate_Built-Up_Areas"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Delineate Built-Up Areas
            arcpy.DelineateBuiltUpAreas(in_buildings, identifier_field, edge_features, grouping_distance, minimum_detail_size, out_feature_class, minimum_building_count)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def merge_divided_roads(self, params):
        """Merge Divided Roads

Generates single-line road features in place of matched pairs of  divided road lanes. Matched pairs of roads or lanes are merged if they are the same road class, trend generally parallel to one another, and are within the merge distance apart. The road class is specified by the Merge  Field parameter. All nonmerged roads from the input collection are copied to the output feature class. Learn more about how Merge Divided Roads works This tool is frequently used to simplify a larger-scale road collection at a smaller scale when it is appropriate to depict divided highways and boulevards as a single line. At medium scales, it may be preferable to retain divided roads as separate features. In this case, you can use the Resolve Road Conflicts tool instead to ensure that symbolized lanes are displayed without symbol conflicts. If both the Resolve Road Conflicts and Merge Divided Roads tools will be run on the same collection of roads, use the Merge Divided Roads tool first.

        params: {"in_features": <Feature Layer>, "merge_field": <Field>, "merge_distance": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    merge_field = params.get("merge_field")
    if merge_field is None:
        return {"success": False, "error": "merge_field parameter is required"}
    merge_distance = params.get("merge_distance")
    if merge_distance is None:
        return {"success": False, "error": "merge_distance parameter is required"}
    out_features = params.get("out_features")
    if out_features is None:
        return {"success": False, "error": "out_features parameter is required"}
    out_displacement_features = params.get("out_displacement_features")
    character_field = params.get("character_field")
    out_table = params.get("out_table")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Merge_Divided_Roads"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Merge Divided Roads
            arcpy.MergeDividedRoads(in_features, merge_field, merge_distance, out_features, out_displacement_features, character_field, out_table)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    simplification_tolerance = params.get("simplification_tolerance")
    if simplification_tolerance is None:
        return {"success": False, "error": "simplification_tolerance parameter is required"}
    minimum_area = params.get("minimum_area")
    conflict_option = params.get("conflict_option")
    in_barriers = params.get("in_barriers")
    collapsed_point_option = params.get("collapsed_point_option")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Simplify_Building"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Simplify Building
            arcpy.SimplifyBuilding(in_features, out_feature_class, simplification_tolerance, minimum_area, conflict_option, in_barriers, collapsed_point_option)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    algorithm = params.get("algorithm")
    if algorithm is None:
        return {"success": False, "error": "algorithm parameter is required"}
    tolerance = params.get("tolerance")
    if tolerance is None:
        return {"success": False, "error": "tolerance parameter is required"}
    error_resolving_option = params.get("error_resolving_option")
    collapsed_point_option = params.get("collapsed_point_option")
    error_checking_option = params.get("error_checking_option")
    in_barriers = params.get("in_barriers")
    error_option = params.get("error_option")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Simplify_Line"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Simplify Line
            arcpy.SimplifyLine(in_features, out_feature_class, algorithm, tolerance, error_resolving_option, collapsed_point_option, error_checking_option, in_barriers, error_option)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    algorithm = params.get("algorithm")
    if algorithm is None:
        return {"success": False, "error": "algorithm parameter is required"}
    tolerance = params.get("tolerance")
    if tolerance is None:
        return {"success": False, "error": "tolerance parameter is required"}
    minimum_area = params.get("minimum_area")
    error_option = params.get("error_option")
    collapsed_point_option = params.get("collapsed_point_option")
    in_barriers = params.get("in_barriers")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Simplify_Polygon"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Simplify Polygon
            arcpy.SimplifyPolygon(in_features, out_feature_class, algorithm, tolerance, minimum_area, error_option, collapsed_point_option, in_barriers)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def simplify_shared_edges(self, params):
        """Simplify Shared Edges

Simplifies the edges of input features while maintaining the topological relationship with edges shared with other features.

        params: {"in_features": <Feature Layer>, "algorithm": <String>, "tolerance": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    algorithm = params.get("algorithm")
    if algorithm is None:
        return {"success": False, "error": "algorithm parameter is required"}
    tolerance = params.get("tolerance")
    if tolerance is None:
        return {"success": False, "error": "tolerance parameter is required"}
    shared_edge_features = params.get("shared_edge_features")
    minimum_area = params.get("minimum_area")
    in_barriers = params.get("in_barriers")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Simplify_Shared_Edges"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Simplify Shared Edges
            arcpy.SimplifySharedEdges(in_features, algorithm, tolerance, shared_edge_features, minimum_area, in_barriers)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def smooth_line(self, params):
        """Smooth Line

Smooths sharp angles in lines to improve aesthetic or cartographic quality. Learn more about how the Smooth Line and Smooth Polygon tools work.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "algorithm": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    algorithm = params.get("algorithm")
    if algorithm is None:
        return {"success": False, "error": "algorithm parameter is required"}
    tolerance = params.get("tolerance")
    if tolerance is None:
        return {"success": False, "error": "tolerance parameter is required"}
    endpoint_option = params.get("endpoint_option")
    error_option = params.get("error_option")
    in_barriers = params.get("in_barriers")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Smooth_Line"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Smooth Line
            arcpy.SmoothLine(in_features, out_feature_class, algorithm, tolerance, endpoint_option, error_option, in_barriers)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def smooth_polygon(self, params):
        """Smooth Polygon

Smooths sharp angles in polygon outlines to improve aesthetic or cartographic quality. Learn more about how the Smooth Line and Smooth Polygon tools work.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "algorithm": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    algorithm = params.get("algorithm")
    if algorithm is None:
        return {"success": False, "error": "algorithm parameter is required"}
    tolerance = params.get("tolerance")
    if tolerance is None:
        return {"success": False, "error": "tolerance parameter is required"}
    endpoint_option = params.get("endpoint_option")
    error_option = params.get("error_option")
    in_barriers = params.get("in_barriers")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Smooth_Polygon"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Smooth Polygon
            arcpy.SmoothPolygon(in_features, out_feature_class, algorithm, tolerance, endpoint_option, error_option, in_barriers)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def smooth_shared_edges(self, params):
        """Smooth Shared Edges

Smooths the edges of the input features while maintaining the topological relationship with edges shared with other features.

        params: {"in_features": <Feature Layer>, "algorithm": <String>, "tolerance": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    algorithm = params.get("algorithm")
    if algorithm is None:
        return {"success": False, "error": "algorithm parameter is required"}
    tolerance = params.get("tolerance")
    if tolerance is None:
        return {"success": False, "error": "tolerance parameter is required"}
    shared_edge_features = params.get("shared_edge_features")
    in_barriers = params.get("in_barriers")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Smooth_Shared_Edges"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Smooth Shared Edges
            arcpy.SmoothSharedEdges(in_features, algorithm, tolerance, shared_edge_features, in_barriers)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def thin_road_network(self, params):
        """Thin Road Network

Generates a simplified road network that retains connectivity and general character for display at a smaller scale. This tool does not generate new output. It assigns values in the input data's Invisibility Field parameter value to identify features that are extraneous. These features can then be removed from view to result in a simplified, yet representative, collection of roads. No feature geometry is altered or deleted. Features are not actually deleted by Thin Road Network. To actually remove features, consider using the Trim Line tool. The resulting simplified road collection  is determined by feature significance, importance, and density. Segments that participate in very long itineraries across the extent of the data  are more significant than those required only for local travel. Road classification, or importance, is specified by the Hierarchy Field parameter. The density of the resulting street network is determined by the Minimum Length parameter, which corresponds to the shortest segment that is visually sensible to show at scale. See How Thin Road Network works to learn more and review a table of recommended minimum length values to use as a starting point. A warning is issued if the input features are not in a projected coordinate system. This tool relies on  linear distance units, which will create unexpected results in an unprojected coordinate system. It is recommended that you run this tool on data in a projected coordinate system to ensure valid results. An error occurs and the tool will not process if the coordinate system is missing or unknown.

        params: {"in_features": <Feature Layer>, "minimum_length": <Linear Unit>, "invisibility_field": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    minimum_length = params.get("minimum_length")
    if minimum_length is None:
        return {"success": False, "error": "minimum_length parameter is required"}
    invisibility_field = params.get("invisibility_field")
    if invisibility_field is None:
        return {"success": False, "error": "invisibility_field parameter is required"}
    hierarchy_field = params.get("hierarchy_field")
    if hierarchy_field is None:
        return {"success": False, "error": "hierarchy_field parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Thin_Road_Network"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Thin Road Network
            arcpy.ThinRoadNetwork(in_features, minimum_length, invisibility_field, hierarchy_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    conflict_features = params.get("conflict_features")
    if conflict_features is None:
        return {"success": False, "error": "conflict_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    conflict_distance = params.get("conflict_distance")
    line_connection_allowance = params.get("line_connection_allowance")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Detect_Graphic_Conflict"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Detect Graphic Conflict
            arcpy.DetectGraphicConflict(in_features, conflict_features, out_feature_class, conflict_distance, line_connection_allowance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def propagate_displacement(self, params):
        """Propagate Displacement

Propagates the displacement resulting from road adjustment in the Resolve Road Conflicts  and Merge Divided Roads tools to adjacent features to reestablish spatial relationships. An optional output of both the Resolve Road Conflicts  and Merge Divided Roads tools is a displacement feature class. Displacement features store the amount and direction of change from the initial state of the data before these tools are run. Displacement information can then be  applied to nearby features from different themes to ensure that spatial relationships are retained using this tool. For example, if roadways are separated by the Resolve Road Conflicts tool, it is often necessary to shift adjacent buildings along the roads accordingly.

        params: {"in_features": <Feature Layer>, "displacement_features": <Feature Layer>, "adjustment_style": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    displacement_features = params.get("displacement_features")
    if displacement_features is None:
        return {"success": False, "error": "displacement_features parameter is required"}
    adjustment_style = params.get("adjustment_style")
    if adjustment_style is None:
        return {"success": False, "error": "adjustment_style parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Propagate_Displacement"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Propagate Displacement
            arcpy.PropagateDisplacement(in_features, displacement_features, adjustment_style)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def resolve_road_conflicts(self, params):
        """Resolve Road Conflicts

Resolves graphic conflicts among symbolized road features by adjusting portions of line segments. Learn more about how Resolve Road Conflicts works Caution:This tool does not produce output layers. Instead, it alters the geometry of the source feature classes of the input  layers. It is recommended that you make a copy of the input features before you run this tool.

        params: {"in_layers": <Layer>, "hierarchy_field": <String>, "out_displacement_features": <Feature Class>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_layers = params.get("in_layers")
    if in_layers is None:
        return {"success": False, "error": "in_layers parameter is required"}
    hierarchy_field = params.get("hierarchy_field")
    if hierarchy_field is None:
        return {"success": False, "error": "hierarchy_field parameter is required"}
    out_displacement_features = params.get("out_displacement_features")

            # Generate output name and path
            output_name = f"{in_layers.replace(' ', '_')}_Resolve_Road_Conflicts"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Resolve Road Conflicts
            arcpy.ResolveRoadConflicts(in_layers, hierarchy_field, out_displacement_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def merge_divided_roads(self, params):
        """Merge Divided Roads

Generates single-line road features in place of matched pairs of  divided road lanes. Matched pairs of roads or lanes are merged if they are the same road class, trend generally parallel to one another, and are within the merge distance apart. The road class is specified by the Merge  Field parameter. All nonmerged roads from the input collection are copied to the output feature class. Learn more about how Merge Divided Roads works This tool is frequently used to simplify a larger-scale road collection at a smaller scale when it is appropriate to depict divided highways and boulevards as a single line. At medium scales, it may be preferable to retain divided roads as separate features. In this case, you can use the Resolve Road Conflicts tool instead to ensure that symbolized lanes are displayed without symbol conflicts. If both the Resolve Road Conflicts and Merge Divided Roads tools will be run on the same collection of roads, use the Merge Divided Roads tool first.

        params: {"in_features": <Feature Layer>, "merge_field": <Field>, "merge_distance": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    merge_field = params.get("merge_field")
    if merge_field is None:
        return {"success": False, "error": "merge_field parameter is required"}
    merge_distance = params.get("merge_distance")
    if merge_distance is None:
        return {"success": False, "error": "merge_distance parameter is required"}
    out_features = params.get("out_features")
    if out_features is None:
        return {"success": False, "error": "out_features parameter is required"}
    out_displacement_features = params.get("out_displacement_features")
    character_field = params.get("character_field")
    out_table = params.get("out_table")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Merge_Divided_Roads"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Merge Divided Roads
            arcpy.MergeDividedRoads(in_features, merge_field, merge_distance, out_features, out_displacement_features, character_field, out_table)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def resolve_building_conflicts(self, params):
        """Resolve Building Conflicts

Resolves symbol conflicts among buildings with respect to linear barrier features by moving, resizing, or hiding buildings.

        params: {"in_buildings": <Layer>, "invisibility_field": <String>, "in_barrierslayer_boolean_linear_unit": <Value Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_buildings = params.get("in_buildings")
    if in_buildings is None:
        return {"success": False, "error": "in_buildings parameter is required"}
    invisibility_field = params.get("invisibility_field")
    if invisibility_field is None:
        return {"success": False, "error": "invisibility_field parameter is required"}
    in_barrierslayer_boolean_linear_unit = params.get("in_barrierslayer_boolean_linear_unit")
    if in_barrierslayer_boolean_linear_unit is None:
        return {"success": False, "error": "in_barrierslayer_boolean_linear_unit parameter is required"}
    building_gap = params.get("building_gap")
    if building_gap is None:
        return {"success": False, "error": "building_gap parameter is required"}
    minimum_size = params.get("minimum_size")
    if minimum_size is None:
        return {"success": False, "error": "minimum_size parameter is required"}
    hierarchy_field = params.get("hierarchy_field")

            # Generate output name and path
            output_name = f"{in_buildings.replace(' ', '_')}_Resolve_Building_Conflicts"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Resolve Building Conflicts
            arcpy.ResolveBuildingConflicts(in_buildings, invisibility_field, in_barrierslayer_boolean_linear_unit, building_gap, minimum_size, hierarchy_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_adjacent_fields(self, params):
        """Calculate Adjacent Fields

Creates fields and calculates values for the neighboring pages (polygon) of a grid polygon feature class. The most common use case for this tool is to populate fields that can be used to label the adjacent pages in a map book. This tool appends eight new fields (each field representing one of the eight points of the compass: North, Northeast, East, Southeast, South, Southwest, West, and Northwest) to the input feature class and calculates values that identify the adjacent (neighboring) polygons, in each cardinal direction, for each feature in the input feature class.

        params: {"in_features": <Feature Layer>, "in_field": <Field>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    in_field = params.get("in_field")
    if in_field is None:
        return {"success": False, "error": "in_field parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Calculate_Adjacent_Fields"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Adjacent Fields
            arcpy.CalculateAdjacentFields(in_features, in_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_central_meridian_and_parallels(self, params):
        """Calculate Central Meridian and Parallels

Calculates the central meridian and optional standard parallels based on the center point of a feature's extent; stores this coordinate system as a spatial reference string in a specified text field; and repeats this for a set, or subset, of features. This field can be used with a spatial map series  to update the data frame coordinate system for each page.

        params: {"in_features": <Feature Layer>, "in_field": <Field>, "standard_offset": <Double>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    in_field = params.get("in_field")
    if in_field is None:
        return {"success": False, "error": "in_field parameter is required"}
    standard_offset = params.get("standard_offset")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Calculate_Central_Meridian_and_Parallels"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Central Meridian and Parallels
            arcpy.CalculateCentralMeridianandParallels(in_features, in_field, standard_offset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_grid_convergence_angle(self, params):
        """Calculate Grid Convergence Angle

Calculates the rotation angle for true north based on the center point of each feature in a feature class and populates this value in a specified field. This field can be used in conjunction with a spatial map series to rotate each map to true north.

        params: {"in_features": <Feature Layer>, "angle_field": <Field>, "rotation_method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    angle_field = params.get("angle_field")
    if angle_field is None:
        return {"success": False, "error": "angle_field parameter is required"}
    rotation_method = params.get("rotation_method")
    coordinate_sys_field = params.get("coordinate_sys_field")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Calculate_Grid_Convergence_Angle"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Grid Convergence Angle
            arcpy.CalculateGridConvergenceAngle(in_features, angle_field, rotation_method, coordinate_sys_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_utm_zone(self, params):
        """Calculate UTM Zone

Calculates the UTM zone of each feature based on the center point and stores this spatial reference string in a specified field. This field can be used with a spatial map series  to update the spatial reference to the correct UTM zone for each map.

        params: {"in_features": <Feature Layer>, "in_field": <Field>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    in_field = params.get("in_field")
    if in_field is None:
        return {"success": False, "error": "in_field parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Calculate_UTM_Zone"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate UTM Zone
            arcpy.CalculateUTMZone(in_features, in_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def grid_index_features(self, params):
        """Grid Index Features

Creates a grid of rectangular polygon features that can be used as an index to specify pages in a spatial map series. A grid can be created that includes only polygon features that intersect another feature layer.

        params: {"out_feature_class": <Feature Class>, "in_features": <Feature Layer; Raster Layer>, "intersect_feature": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
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

            # Generate output name and path
            output_name = f"{out_feature_class.replace(' ', '_')}_Grid_Index_Features"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Grid Index Features
            arcpy.GridIndexFeatures(out_feature_class, in_features, intersect_feature, use_page_unit, scale, polygon_width, polygon_height, origin_coord, number_rows, number_columns, starting_page_number, label_from_origin)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def strip_map_index_features(self, params):
        """Strip Map Index Features

Creates a series of rectangular polygons, or index features, that follow a single linear feature or a group of linear features. These index features can be used with spatial map series to define pages in a strip map or a set of maps that follow a linear feature. The resulting index features contain attributes that can be used to rotate and orient the map on the page and determine which index features, or pages, are next to the current page (to the left and right or to the top and bottom).

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "use_page_unit": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    out_feature_class = params.get("out_feature_class")
    if out_feature_class is None:
        return {"success": False, "error": "out_feature_class parameter is required"}
    use_page_unit = params.get("use_page_unit")
    scale = params.get("scale")
    length_along_line = params.get("length_along_line")
    page_orientation = params.get("page_orientation")
    overlap_percentage = params.get("overlap_percentage")
    starting_page_number = params.get("starting_page_number")
    direction_type = params.get("direction_type")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Strip_Map_Index_Features"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Strip Map Index Features
            arcpy.StripMapIndexFeatures(in_features, out_feature_class, use_page_unit, scale, length_along_line, page_orientation, overlap_percentage, starting_page_number, direction_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_central_meridian_and_parallels(self, params):
        """Calculate Central Meridian And Parallels

Calculates the central meridian and optional standard parallels based on the center point of a feature's extent; stores this coordinate system as a spatial reference string in a specified text field; and repeats this for a set, or subset, of features. This field can be used with a spatial map series  to update the data frame coordinate system for each page.

        params: {"in_features": <Feature Layer>, "in_field": <Field>, "standard_offset": <Double>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    in_features = params.get("in_features")
    if in_features is None:
        return {"success": False, "error": "in_features parameter is required"}
    in_field = params.get("in_field")
    if in_field is None:
        return {"success": False, "error": "in_field parameter is required"}
    standard_offset = params.get("standard_offset")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Calculate_Central_Meridian_And_Parallels"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Central Meridian And Parallels
            arcpy.CalculateCentralMeridianAndParallels(in_features, in_field, standard_offset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
    if input_layer is None:
        return {"success": False, "error": "input_layer parameter is required"}
    output_fc = params.get("output_fc")
    if output_fc is None:
        return {"success": False, "error": "output_fc parameter is required"}
    reference_scale = params.get("reference_scale")
    if reference_scale is None:
        return {"success": False, "error": "reference_scale parameter is required"}
    spatial_reference = params.get("spatial_reference")
    if spatial_reference is None:
        return {"success": False, "error": "spatial_reference parameter is required"}
    margin = params.get("margin")
    if margin is None:
        return {"success": False, "error": "margin parameter is required"}
    attributes = params.get("attributes")

            # Generate output name and path
            output_name = f"{input_layer.replace(' ', '_')}_Cul-De-Sac_Masks"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Cul-De-Sac Masks
            arcpy.CulDeSacMasks(input_layer, output_fc, reference_scale, spatial_reference, margin, attributes)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def feature_outline_masks(self, params):
        """Feature Outline Masks

Creates mask polygons at a specified distance and shape around the symbolized features in the input layer. Learn more about how Feature Outline Masks and Intersecting Layers Masks work

        params: {"input_layer": <Annotation Layer>, "output_fc": <Feature Class>, "reference_scale": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    input_layer = params.get("input_layer")
    if input_layer is None:
        return {"success": False, "error": "input_layer parameter is required"}
    output_fc = params.get("output_fc")
    if output_fc is None:
        return {"success": False, "error": "output_fc parameter is required"}
    reference_scale = params.get("reference_scale")
    if reference_scale is None:
        return {"success": False, "error": "reference_scale parameter is required"}
    spatial_reference = params.get("spatial_reference")
    if spatial_reference is None:
        return {"success": False, "error": "spatial_reference parameter is required"}
    margin = params.get("margin")
    if margin is None:
        return {"success": False, "error": "margin parameter is required"}
    method = params.get("method")
    if method is None:
        return {"success": False, "error": "method parameter is required"}
    mask_for_non_placed_anno = params.get("mask_for_non_placed_anno")
    if mask_for_non_placed_anno is None:
        return {"success": False, "error": "mask_for_non_placed_anno parameter is required"}
    attributes = params.get("attributes")
    preserve_small_sized_features = params.get("preserve_small_sized_features")

            # Generate output name and path
            output_name = f"{input_layer.replace(' ', '_')}_Feature_Outline_Masks"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Feature Outline Masks
            arcpy.FeatureOutlineMasks(input_layer, output_fc, reference_scale, spatial_reference, margin, method, mask_for_non_placed_anno, attributes, preserve_small_sized_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def intersecting_layers_masks(self, params):
        """Intersecting Layers Masks

Creates masking polygons at a specified shape and size at the intersection of two symbolized input layers: the masking layer and the masked layer. Learn more about how Feature Outline Masks and Intersecting Layers Masks work

        params: {"masking_layer": <Annotation Layer>, "masked_layer": <Annotation Layer>, "output_fc": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
    masking_layer = params.get("masking_layer")
    if masking_layer is None:
        return {"success": False, "error": "masking_layer parameter is required"}
    masked_layer = params.get("masked_layer")
    if masked_layer is None:
        return {"success": False, "error": "masked_layer parameter is required"}
    output_fc = params.get("output_fc")
    if output_fc is None:
        return {"success": False, "error": "output_fc parameter is required"}
    reference_scale = params.get("reference_scale")
    if reference_scale is None:
        return {"success": False, "error": "reference_scale parameter is required"}
    spatial_reference = params.get("spatial_reference")
    if spatial_reference is None:
        return {"success": False, "error": "spatial_reference parameter is required"}
    margin = params.get("margin")
    if margin is None:
        return {"success": False, "error": "margin parameter is required"}
    method = params.get("method")
    if method is None:
        return {"success": False, "error": "method parameter is required"}
    mask_for_non_placed_anno = params.get("mask_for_non_placed_anno")
    if mask_for_non_placed_anno is None:
        return {"success": False, "error": "mask_for_non_placed_anno parameter is required"}
    attributes = params.get("attributes")

            # Generate output name and path
            output_name = f"{masking_layer.replace(' ', '_')}_Intersecting_Layers_Masks"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Intersecting Layers Masks
            arcpy.IntersectingLayersMasks(masking_layer, masked_layer, output_fc, reference_scale, spatial_reference, margin, method, mask_for_non_placed_anno, attributes)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}
