# Generated ArcGIS Pro cartography AI Function Declarations
# Generated on 2025-10-01T13:54:58.198666
# Total tools: 51

functions_declarations = {
    "annotate_selected_features": {
        "name": "annotate_selected_features",
        "description": "Creates annotation for the selected features of a layer. The labeling properties defined in the annotation class properties of  the specified related annotation feature classes are used.",
        "parameters": {
                "in_map": {
                        "type": "string",
                        "description": "The input map."
                },
                "in_layer": {
                        "type": "string",
                        "description": "The layer for which the selected features will have annotation created."
                },
                "anno_layersannotation_layer_sublayer_sublayer": {
                        "type": "string",
                        "description": "The feature-linked annotation layers and the specified sublayers that will have annotation converted into them."
                },
                "generate_unplaced": {
                        "type": "string",
                        "description": "Specifies whether to create unplaced annotation\r\nfrom unplaced labels.\r\n\r\n\r\nONLY_PLACED\u2014Annotation will only be created\r\nfor features that are currently labeled. This is the\r\ndefault.GENERATE_UNPLACED...",
                        "default": null
                }
        },
        "required": [
                "in_map",
                "in_layer",
                "anno_layersannotation_layer_sublayer_sublayer"
        ]
},
    "contour_annotation": {
        "name": "contour_annotation",
        "description": "Creates annotation for contour features. The tool creates an annotation feature class with corresponding mask polygons based on input contour features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The contour line feature class for which the annotation will be created."
                },
                "out_geodatabase": {
                        "type": "string",
                        "description": "The workspace where the output feature classes will be saved. The workspace can be an existing geodatabase or an existing feature dataset."
                },
                "contour_label_field": {
                        "type": "string",
                        "description": "The field in the input layer attribute table on which the annotation text will be based."
                },
                "reference_scale_value": {
                        "type": "string",
                        "description": "The scale that will be used as a reference for the annotation. This sets the scale on which all symbol and text sizes in the annotation will be based."
                },
                "out_layer": {
                        "type": "string",
                        "description": "The group layer that will contain the contour layer, the annotation, and the mask layer. When working in the Catalog pane, you can use the Save To Layer File tool to write the output group layer to a ..."
                },
                "contour_color": {
                        "type": "string",
                        "description": "Specifies the color of the output contour layer and annotation features.\r\nBLACK\u2014The output contour layer and annotation features will be drawn in black.  This is the default.BROWN\u2014The output contour l..."
                },
                "contour_type_field": {
                        "type": "string",
                        "description": "The field in the input layer attribute table containing a value for the type of contour feature.  An annotation class will be created for each type value.",
                        "default": null
                },
                "contour_alignment": {
                        "type": "string",
                        "description": "Specifies how the annotation will be aligned to contour elevations.\r\nThe annotation can be aligned to the contour elevations so that\r\nthe top of the text is always placed uphill or downhill. These opt...",
                        "default": null
                },
                "enable_laddering": {
                        "type": "string",
                        "description": "Specifies whether annotation will be placed in ladders. Placing annotation in ladders will place the text so it appears to\r\nstep up and step down the contours in a straight  path.\r\nThese ladders will ...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_geodatabase",
                "contour_label_field",
                "reference_scale_value",
                "out_layer",
                "contour_color"
        ]
},
    "convert_labels_to_annotation": {
        "name": "convert_labels_to_annotation",
        "description": "Converts labels to annotation for a single layer or the entire map. Both standard annotation and feature-linked annotation can be created.",
        "parameters": {
                "input_map": {
                        "type": "string",
                        "description": "The input map."
                },
                "conversion_scale": {
                        "type": "string",
                        "description": "The scale at which labels will be converted. If a reference scale is set on the map, the reference scale will be used for symbol sizing and annotation feature class creation, but conversion will occur..."
                },
                "output_geodatabase": {
                        "type": "string",
                        "description": "The workspace where the output feature classes will be saved. The workspace can be an existing geodatabase or an existing feature dataset. If this is not the same database used by all the layers in th..."
                },
                "anno_suffix": {
                        "type": "string",
                        "description": "The suffix that will be added to each new annotation feature class. This suffix will be appended to the name of the source feature class for each new annotation feature class.",
                        "default": null
                },
                "extent": {
                        "type": "string",
                        "description": "Specifies the extent that contains the labels to convert to annotation.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPLAY\u2014The extent i...",
                        "default": null
                },
                "generate_unplaced": {
                        "type": "string",
                        "description": "Specifies whether unplaced annotation\r\nwill be created from unplaced labels.\r\n\r\n\r\nONLY_PLACED\u2014Annotation will only be created\r\nfor features that are currently labeled. This is the\r\ndefault.GENERATE_UN...",
                        "default": null
                },
                "require_symbol_id": {
                        "type": "string",
                        "description": "Specifies whether all\r\ntext symbol properties can be edited.NO_REQUIRE_ID\u2014All text symbol properties can be edited. This is the default.REQUIRE_ID\u2014Only symbol properties that enable\r\nannotation featur...",
                        "default": null
                },
                "feature_linked": {
                        "type": "string",
                        "description": "Specifies whether the output annotation feature\r\nclass will be linked to the features in another feature\r\nclass.STANDARD\u2014The output annotation feature class\r\nwill not be linked to the features in anot...",
                        "default": null
                },
                "auto_create": {
                        "type": "string",
                        "description": "Specifies whether annotation will be created when new\r\nfeatures are added to the linked feature class and the feature_linked parameter is set to FEATURE_LINKED.AUTO_CREATE\u2014Feature-linked annotation wi...",
                        "default": null
                },
                "update_on_shape_change": {
                        "type": "string",
                        "description": "Specifies whether the position of annotation will be updated when the shape of the linked feature is modified and the feature_linked parameter is set to FEATURE_LINKED.SHAPE_UPDATE\u2014The position of the...",
                        "default": null
                },
                "output_group_layer": {
                        "type": "string",
                        "description": "The group layer that will contain the generated annotation. You can use the Save To Layer File tool to write the output group layer to a layer file.",
                        "default": null
                },
                "which_layers": {
                        "type": "string",
                        "description": "Specifies whether annotation will be converted for all layers in the map or for a single layer. The single layer must be specified.\r\n\r\n\r\nALL_LAYERS\u2014Labels will be converted to annotation for all layer...",
                        "default": null
                },
                "single_layer": {
                        "type": "string",
                        "description": "The layer with the annotation that will be converted when the which_layers parameter is set to SINGLE_LAYER. This layer must be in the map.",
                        "default": null
                },
                "multiple_feature_classes": {
                        "type": "string",
                        "description": "Specifies whether labels will be converted to individual annotation feature classes or to a single annotation feature class. If converting to a single annotation feature class, the annotation cannot b...",
                        "default": null
                },
                "merge_label_classes": {
                        "type": "string",
                        "description": "Specifies whether similar label classes will be merged when the multiple_feature_classes parameter is set to SINGLE_FEATURE_CLASS.MERGE_LABEL_CLASS\u2014Label classes with similar properties will be merged...",
                        "default": null
                }
        },
        "required": [
                "input_map",
                "conversion_scale",
                "output_geodatabase"
        ]
},
    "convert_labels_to_graphics": {
        "name": "convert_labels_to_graphics",
        "description": "Converts labels to graphics for a single layer or an entire map.",
        "parameters": {
                "input_map": {
                        "type": "string",
                        "description": "The input map object."
                },
                "conversion_scale": {
                        "type": "string",
                        "description": "The scale at which to convert labels. If a reference scale is set on the map, the reference scale will be used for symbol sizing and graphics layer creation, but conversion will happen at this scale."
                },
                "which_layers": {
                        "type": "string",
                        "description": "Specifies whether to convert graphics for all layers in the map or for a single layer. ALL_LAYERS\u2014Labels will be converted to graphics for all layers in the map.\r\n\r\nThis is the default.SINGLE_LAYER\u2014La...",
                        "default": null
                },
                "single_layer": {
                        "type": "string",
                        "description": "The layer with the labels to convert when the which_layers parameter is set to SINGLE_LAYER. This layer must be in the map.",
                        "default": null
                },
                "graphics_suffix": {
                        "type": "string",
                        "description": "The suffix that will be added to each new graphics layer. This suffix will be appended to the name of the source feature class for each new graphics layer.",
                        "default": null
                },
                "extent": {
                        "type": "string",
                        "description": "Specifies the extent that contains the labels to convert to graphics.MAXOF\u2014The maximum extent of all inputs will be used.MINOF\u2014The minimum area common to all inputs will be used.DISPLAY\u2014The extent is ...",
                        "default": null
                },
                "multiple_graphics_layers": {
                        "type": "string",
                        "description": "Specifies whether labels will be converted to individual graphics layers or to a single graphics layer. SINGLE_GRAPHICS_LAYER\u2014Labels from all layers will be converted to a single graphics layer.GRAPHI...",
                        "default": null
                },
                "generate_unplaced": {
                        "type": "string",
                        "description": "Specifies whether graphics\r\nwill be created from unplaced labels.\r\n\r\n\r\nONLY_PLACED\u2014Graphics will only be created\r\nfor features that are currently labeled. This is the\r\ndefault.GENERATE_UNPLACED\u2014Unplac...",
                        "default": null
                },
                "output_group_layer": {
                        "type": "string",
                        "description": "The group layer that will contain the generated graphics. You can use the Save To Layer File tool to write the output group layer to a layer file.",
                        "default": null
                }
        },
        "required": [
                "input_map",
                "conversion_scale"
        ]
},
    "map_server_cache_tiling_scheme_to_polygons": {
        "name": "map_server_cache_tiling_scheme_to_polygons",
        "description": "Creates a polygon feature class from an existing tiling scheme. This tool subdivides a map extent using the same scales as an existing map service cache tiling scheme and creates tiles over a large area, or supertile. Since the supertile extent is larger than the actual tiles defined in the tiling scheme, tiles used as input to the Tiled Labels To Annotation tool can convert labels to annotation over a larger area at a time. This process minimizes annotation duplication across tiles.",
        "parameters": {
                "input_map": {
                        "type": "string",
                        "description": "The current map with the extent that will be used."
                },
                "tiling_scheme": {
                        "type": "string",
                        "description": "A predefined tiling scheme .xml file."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "The output polygon feature class."
                },
                "use_map_extent": {
                        "type": "string",
                        "description": "Specifies whether polygon features will be  created for the entire extent of the tiling scheme or only those tiles that intersect the full extent of the map.  USE_MAP_EXTENT\u2014Polygon features will be c..."
                },
                "clip_to_horizon": {
                        "type": "string",
                        "description": "Specifies whether polygons will be constrained to the valid area of use for the geographic or projected coordinate system of the map. CLIP_TO_HORIZON\u2014Polygon features will only be created within the v..."
                },
                "antialiasing": {
                        "type": "string",
                        "description": "Specifies whether polygons that match map service caches with antialiasing enabled will be generated.\r\nA map service cache supertile is 2048 x 2048 pixels with antialiasing or 4096 x 4096\r\npixels with...",
                        "default": null
                },
                "levelslevel": {
                        "type": "string",
                        "description": "The scale levels at which polygons will be created.  To create polygons for all scale levels included in a tiling scheme, leave this parameter blank. You can create polygons for some or all of the sca...",
                        "default": null
                }
        },
        "required": [
                "input_map",
                "tiling_scheme",
                "output_feature_class",
                "use_map_extent",
                "clip_to_horizon"
        ]
},
    "tiled_labels_to_annotation": {
        "name": "tiled_labels_to_annotation",
        "description": "Converts labels to annotation for layers in a map based on a polygon index layer. The tool divides a map into tiles and creates annotation for each tile in turn. This is useful for converting a large number of labels to annotation. The polygon index layer can be generated using the Map Server Cache Tiling Scheme To Polygons or Grid Index Features tool or any other polygon feature class that covers the area where you want to create annotation.",
        "parameters": {
                "input_map": {
                        "type": "string",
                        "description": "The map that contains the labels to convert to annotation."
                },
                "polygon_index_layer": {
                        "type": "string",
                        "description": "The polygon layer that contains tile features."
                },
                "out_geodatabase": {
                        "type": "string",
                        "description": "The workspace where the output feature classes will be saved. The workspace can be an existing geodatabase or an existing feature dataset."
                },
                "out_layer": {
                        "type": "string",
                        "description": "The group layer that will contain the generated annotation. You can use the Save To Layer File tool to write the output group layer to a layer file."
                },
                "anno_suffix": {
                        "type": "string",
                        "description": "The suffix that will be added to each new annotation feature class. This suffix will be appended to the name of the source feature class for each new annotation feature class. The reference scale for ..."
                },
                "reference_scale_value": {
                        "type": "string",
                        "description": "The scale value that will be used as a reference for the annotation. This is the scale on which all symbol and text sizes in the annotation will be based.",
                        "default": null
                },
                "reference_scale_field": {
                        "type": "string",
                        "description": "The field in the polygon index layer that will determine the reference scale of the annotation. This is the scale on which all symbol and text sizes in the annotation will be based.",
                        "default": null
                },
                "tile_id_field": {
                        "type": "string",
                        "description": "A field in the polygon index layer that uniquely identifies the tiled area. These values will populate the TileID field in the annotation feature class attribute table.",
                        "default": null
                },
                "coordinate_sys_field": {
                        "type": "string",
                        "description": "A field in the polygon index layer that contains the coordinate system information for each tile. Due to the length required for a field to store coordinate system information, a polygon index layer t...",
                        "default": null
                },
                "map_rotation_field": {
                        "type": "string",
                        "description": "A field in the polygon index layer that contains the angle by which the map will be rotated.",
                        "default": null
                },
                "feature_linked": {
                        "type": "string",
                        "description": "Specifies whether the output annotation feature\r\nclass will be linked to the features in another feature\r\nclass.STANDARD\u2014 The output annotation feature class will not be linked to the features in anot...",
                        "default": null
                },
                "generate_unplaced_annotation": {
                        "type": "string",
                        "description": "Specifies whether unplaced annotation\r\nwill be created from unplaced labels.NOT_GENERATE_UNPLACED_ANNOTATION\u2014Annotation will only be created for features that are currently labeled. This is the defaul...",
                        "default": null
                },
                "which_layers": {
                        "type": "string",
                        "description": "Specifies whether annotation will be converted for all layers in the map or for a single layer. The single layer must be specified.\r\n\r\n\r\nALL_LAYERS\u2014Labels will be converted to annotation for all layer...",
                        "default": null
                },
                "single_layer": {
                        "type": "string",
                        "description": "The layer with the annotation that will be converted when the which_layers parameter is set to SINGLE_LAYER. This layer must be in the map.",
                        "default": null
                },
                "require_symbol_id": {
                        "type": "string",
                        "description": "Specifies whether all\r\ntext symbol properties can be edited.NO_REQUIRE_ID\u2014All text symbol properties can be edited. This is the default.REQUIRE_ID\u2014Only symbol properties that enable\r\nannotation featur...",
                        "default": null
                },
                "auto_create": {
                        "type": "string",
                        "description": "Specifies whether annotation will be created when new\r\nfeatures are added to the linked feature class if the feature_linked parameter is set to FEATURE_LINKED.AUTO_CREATE\u2014Feature-linked annotation wil...",
                        "default": null
                },
                "update_on_shape_change": {
                        "type": "string",
                        "description": "Specifies whether the position of annotation will be updated when the shape of the linked feature is modified if the feature_linked parameter is set to FEATURE_LINKED.SHAPE_UPDATE\u2014The position of the ...",
                        "default": null
                },
                "multiple_feature_classes": {
                        "type": "string",
                        "description": "Specifies whether labels will be converted to individual annotation feature classes or to a single annotation feature class. If converting to a single annotation feature class, the annotation cannot b...",
                        "default": null
                },
                "merge_label_classes": {
                        "type": "string",
                        "description": "Specifies whether similar label classes will be merged if the multiple_feature_classes parameter is set to SINGLE_FEATURE_CLASS.MERGE_LABEL_CLASS\u2014Label classes with similar properties will be merged w...",
                        "default": null
                }
        },
        "required": [
                "input_map",
                "polygon_index_layer",
                "out_geodatabase",
                "out_layer",
                "anno_suffix"
        ]
},
    "update_annotation_reference_scale": {
        "name": "update_annotation_reference_scale",
        "description": "Updates the reference scale of an existing annotation or dimension feature class.",
        "parameters": {
                "in_anno_features": {
                        "type": "string",
                        "description": "The input annotation or dimension features."
                },
                "reference_scale": {
                        "type": "string",
                        "description": "The feature class reference scale that will be updated."
                }
        },
        "required": [
                "in_anno_features",
                "reference_scale"
        ]
},
    "generate_contiguous_cartogram": {
        "name": "generate_contiguous_cartogram",
        "description": "Generates a cartogram by distorting the area of polygons to be proportional to each other based on a numeric field while preserving shared boundaries.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input polygon features that will be used to generate the cartogram."
                },
                "field_name": {
                        "type": "string",
                        "description": "The numeric field containing the values that will determine the area of the polygon features in the output cartogram. \r\nAny features with a negative value or a value of 0 will be omitted from the outp..."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output polygons with the cartogram transformation applied."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to transform the input and create the cartogram.FLOW-BASED\u2014An evolution of the diffusion method that is often faster will be used, which may increase distortion....",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "field_name",
                "out_features"
        ]
},
    "align_marker_to_stroke_or_fill": {
        "name": "align_marker_to_stroke_or_fill",
        "description": "Aligns the marker symbol layers of a point feature class to the nearest stroke or fill symbol layers in a line or polygon feature class within a specified search distance.",
        "parameters": {
                "in_point_features": {
                        "type": "string",
                        "description": "The input point feature layer containing point symbols to be aligned to nearby lines or polygons. Symbols are aligned by storing an angle in the  attribute connected to the angle property of the marke..."
                },
                "in_line_or_polygon_features": {
                        "type": "string",
                        "description": "The input line or polygon feature layer to which the input point symbols will be aligned."
                },
                "search_distance": {
                        "type": "string",
                        "description": "The search distance from graphical marker edge to graphical stroke or fill edge. A distance greater than or equal to zero must be specified."
                },
                "marker_orientation": {
                        "type": "string",
                        "description": "Specifies how the marker symbol layer will be oriented relative to the stroke or fill symbol layer's edge.PERPENDICULAR\u2014Marker symbol layers will be aligned perpendicularly to the stroke or fill edge....",
                        "default": null
                }
        },
        "required": [
                "in_point_features",
                "in_line_or_polygon_features",
                "search_distance"
        ]
},
    "calculate_color_theorem_field": {
        "name": "calculate_color_theorem_field",
        "description": "Populates an integer field to use for symbolizing polygons with a small number of colors and ensuring no two adjacent polygons are the same color. Values are assigned to each polygon based on the theorem that only a small number of colors, often four or five, are needed to ensure no two adjacent polygons in a 2-dimensional map are the same color. Overlapping and multipart polygons can increase the number of colors required. The assigned values will be integers ranging from 1 to the number of unique values assigned.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input polygons that will use the tool results to symbolize features."
                },
                "field_name": {
                        "type": "string",
                        "description": "The field that will store the tool results. Each feature will be assigned an integer between 1 and the number of unique values created to ensure no two adjacent polygons have the same value.If the fie..."
                }
        },
        "required": [
                "in_features",
                "field_name"
        ]
},
    "calculate_line_caps": {
        "name": "calculate_line_caps",
        "description": "Modifies the cap type for stroke symbol layers in the line symbols of the input layer.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature layer containing line symbols. Stroke symbol layers must have the Cap Type property connected to a single attribute field with no expression applied. The values in this field are upd..."
                },
                "cap_type": {
                        "type": "string",
                        "description": "Specifies how the ends of stroke symbol layers will be drawn. The default cap type of strokes is round; the symbol is terminated with a semicircle of radius equal to stroke width centered at the line ...",
                        "default": null
                },
                "dangle_option": {
                        "type": "string",
                        "description": "Specifies how line caps will be calculated for adjoining line features that share an endpoint but are drawn with different symbology. CASED_LINE_DANGLE\u2014The cap style will be modified for dangling line...",
                        "default": null
                }
        },
        "required": [
                "in_features"
        ]
},
    "calculate_polygon_main_angle": {
        "name": "calculate_polygon_main_angle",
        "description": "Calculates the dominant angles of  input polygon features and assigns the values to a field to use to orient symbology such as markers or hatch lines within the polygons.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input polygon features."
                },
                "angle_field": {
                        "type": "string",
                        "description": "The field that will be updated with the polygon main angle values."
                },
                "rotation_method": {
                        "type": "string",
                        "description": "Specifies the method and origin point of rotation that will be used.. \r\nGEOGRAPHIC\u2014The angle will be calculated clockwise with 0 at the top (north).ARITHMETIC\u2014The angle will be calculated counterclock...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "angle_field"
        ]
},
    "convert_control_points_to_vertices": {
        "name": "convert_control_points_to_vertices",
        "description": "Converts control points in a line or polygon feature layer to vertices.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The line or polygon input features containing control point geometry that will be converted to vertices."
                }
        },
        "required": [
                "in_features"
        ]
},
    "convert_marker_placement_to_points": {
        "name": "convert_marker_placement_to_points",
        "description": "Creates points from the markers of a marker placement in a symbolized  polygon feature.",
        "parameters": {
                "in_layer": {
                        "type": "string",
                        "description": "A polygon layer symbolized with a marker placement."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "A point feature class containing points created from markers in the input layer's marker placement settings. The points will be added to the active map as a layer symbolized with a unique value render..."
                },
                "create_multipoints": {
                        "type": "string",
                        "description": "Specifies whether output point features will be multipoint.\r\nCREATE_MULTIPOINTS\u2014A multipoint feature will be created for the markers in each input polygon. This is the default.CREATE_POINTS\u2014A point fe...",
                        "default": null
                },
                "boundary_option": {
                        "type": "string",
                        "description": "Specifies whether output points will be created for input markers that cross polygon boundaries.MAY_CROSS_BOUNDARY\u2014Output points will be created for input markers that cross polygon boundaries. This i...",
                        "default": null
                },
                "boundary_distance": {
                        "type": "string",
                        "description": "The minimum distance between the output point symbols and the polygon boundaries. This parameter is applied only when the boundary_option parameter is set to FIXED_DISTANCE. The default value is 0.",
                        "default": null
                },
                "boundary_distance_field": {
                        "type": "string",
                        "description": "A numeric field from the input polygons that will be used to determine the boundary distance .This parameter is applied only when the boundary_option parameter is set to VALUE_FROM_FIELD.",
                        "default": null
                },
                "boundary_distance_unit": {
                        "type": "string",
                        "description": "Specifies the linear unit that will be used for boundary distance values.Kilometers\u2014The unit will be kilometers.Meters\u2014The unit will be meters.Decimeters\u2014The unit will be decimeters.Centimeters\u2014The un...",
                        "default": null
                },
                "in_barriersbarrier_layer_barrier_distance_barrier_distance_field_barrier_distance_unit": {
                        "type": "string",
                        "description": "The layers containing points, lines, or polygon features that are conflict barriers for input markers. Markers that conflict with barriers will not be created. The symbology of the barrier layers will...",
                        "default": null
                },
                "keep_at_least_one_marker": {
                        "type": "string",
                        "description": "Specifies whether a single marker will be created for input polygons when all markers conflict with boundaries or barriers.\r\nKEEP_AT_LEAST_ONE_MARKER\u2014One marker will be created for input polygons when...",
                        "default": null
                },
                "displacement_method": {
                        "type": "string",
                        "description": "Specifies the displacement method that will be used to move markers that are too close to each other. This parameter is applied only when markers are positioned randomly inside the polygons.\r\nDO_NOT_D...",
                        "default": null
                },
                "minimum_marker_distance": {
                        "type": "string",
                        "description": "The minimum distance between individual markers. This parameter is applied only when markers are positioned randomly inside the polygons. The default value is 0.",
                        "default": null
                }
        },
        "required": [
                "in_layer",
                "out_feature_class"
        ]
},
    "create_overpass": {
        "name": "create_overpass",
        "description": "Creates bridge parapets and polygon masks at line intersections to indicate overpasses.",
        "parameters": {
                "in_above_features": {
                        "type": "string",
                        "description": "The input line feature layer containing lines that intersect\u2014and will be symbolized as passing above\u2014lines in the in_below_features parameter value."
                },
                "in_below_features": {
                        "type": "string",
                        "description": "The input line feature layer containing lines that intersect\u2014and will be symbolized as passing below\u2014lines in the in_above_features parameter value. These features will be masked by the polygons creat..."
                },
                "margin_along": {
                        "type": "string",
                        "description": "The length of the mask polygons along the in_above_features parameter, which is the distance in page units that the mask will extend beyond the width of the stroke symbol of the in_below_features para..."
                },
                "margin_across": {
                        "type": "string",
                        "description": "The width of the mask polygons across the in_above_features parameter value, which is the distance in page units that the mask will extend beyond the width of the stroke symbol of the in_above_feature..."
                },
                "out_overpass_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will be created to store polygons to mask the in_below_features parameter value."
                },
                "out_mask_relationship_class": {
                        "type": "string",
                        "description": "The output relationship class that will be created to store links between overpass mask polygons and the lines of the in_below_features parameter value."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression that will be used to select a subset of features from the in_above_features parameter valueUse quotation marks for field names, for example, \"MY_FIELD\".\r\n\r\n\r\n\r\nSee SQL reference for ...",
                        "default": null
                },
                "out_decoration_feature_class": {
                        "type": "string",
                        "description": "The output line feature class that will be created to store parapet features.",
                        "default": null
                },
                "wing_type": {
                        "type": "string",
                        "description": "Specifies the wing style that will be used for the parapet features.ANGLED\u2014The wing tick of the parapet will be angled between the in_above_features parameter value and the in_below_features parameter...",
                        "default": null
                },
                "wing_tick_length": {
                        "type": "string",
                        "description": "The length of the parapet wings in page units. The length must be greater than or equal to zero; the default length is 1. Choose a page unit (points, millimeters, and so on) for the length; the defaul...",
                        "default": null
                }
        },
        "required": [
                "in_above_features",
                "in_below_features",
                "margin_along",
                "margin_across",
                "out_overpass_feature_class",
                "out_mask_relationship_class"
        ]
},
    "create_underpass": {
        "name": "create_underpass",
        "description": "Creates bridge parapets and polygon masks at line intersections to indicate underpasses.",
        "parameters": {
                "in_above_features": {
                        "type": "string",
                        "description": "The input line feature layer containing lines that intersect\u2014and will be symbolized as passing above\u2014lines in the in_below_features parameter value."
                },
                "in_below_features": {
                        "type": "string",
                        "description": "The input line feature layer containing lines that intersect\u2014and will be symbolized as passing below\u2014lines in the in_above_features parameter value. These features will be masked by the polygons creat..."
                },
                "margin_along": {
                        "type": "string",
                        "description": "The length of the mask polygons along the in_above_features parameter value, which is the distance in page units that the mask will extend beyond the width of the stroke symbol of the in_below_feature..."
                },
                "margin_across": {
                        "type": "string",
                        "description": "The width of the mask polygons across the in_above_features parameter value, which is the distance in page units that the mask will extend beyond the width of the stroke symbol of the in_above_feature..."
                },
                "out_underpass_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will be created to store polygons to mask the in_below_features parameter value."
                },
                "out_mask_relationship_class": {
                        "type": "string",
                        "description": "The output relationship class that will be created to store links between underpass mask polygons and the lines of the in_below_features parameter value."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression used to select a subset of features from the in_above_features parameter value.Use quotation marks for field names, for example, \"MY_FIELD\".\r\n\r\n\r\n\r\nSee SQL reference for query expres...",
                        "default": null
                },
                "out_decoration_feature_class": {
                        "type": "string",
                        "description": "The output line feature class that will be created to store parapet features.",
                        "default": null
                },
                "wing_type": {
                        "type": "string",
                        "description": "Specifies the wing style that will be used for the parapet features.ANGLED\u2014The wing tick of the parapet will be angled between the in_above_features parameter value and the in_below_features parameter...",
                        "default": null
                },
                "wing_tick_length": {
                        "type": "string",
                        "description": "The length of the parapet wings in page units. The length must be greater than or equal to zero; the default length is 1. Choose a page unit (points, millimeters, and so on) for the length; the defaul...",
                        "default": null
                }
        },
        "required": [
                "in_above_features",
                "in_below_features",
                "margin_along",
                "margin_across",
                "out_underpass_feature_class",
                "out_mask_relationship_class"
        ]
},
    "disperse_markers": {
        "name": "disperse_markers",
        "description": "Finds point symbols that overlap or are too close to one another based on symbology at reference scale and spreads them apart based on a minimum spacing and dispersal pattern.",
        "parameters": {
                "in_point_features": {
                        "type": "string",
                        "description": "The input point feature layer to be dispersed."
                },
                "minimum_spacing": {
                        "type": "string",
                        "description": "The minimum separation distance between individual point symbols in page units. A distance must be specified and must be greater than or equal to zero. When a positive value is specified, markers will..."
                },
                "dispersal_pattern": {
                        "type": "string",
                        "description": "Specifies the pattern that will be used to place the dispersed point symbols. A group of point symbols will have a center of mass derived from the locations of all points in the group. The center of m...",
                        "default": null
                }
        },
        "required": [
                "in_point_features",
                "minimum_spacing"
        ]
},
    "generate_hachures_for_defined_slopes": {
        "name": "generate_hachures_for_defined_slopes",
        "description": "Creates multipart lines or polygons representing the slope between the lines representing the upper and lower parts of a slope.",
        "parameters": {
                "upper_lines": {
                        "type": "string",
                        "description": "The line features that represent the top of a slope."
                },
                "lower_lines": {
                        "type": "string",
                        "description": "The line features that represent the bottom of a slope."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing multipart line or polygon hachures representing the slope area."
                },
                "output_type": {
                        "type": "string",
                        "description": "Specifies whether polygon triangles or tick lines  will be created to represent the slope.POLYGON_TRIANGLES\u2014Multipart polygon features will be created in which a triangular polygon is created for each...",
                        "default": null
                },
                "fully_connected": {
                        "type": "string",
                        "description": "Specifies whether the upper and lower lines in the input data form fully connected areas.  If the upper and lower lines are not fully connected, choose NOT_CONNECTED to create hachures inside areas th...",
                        "default": null
                },
                "search_distance": {
                        "type": "string",
                        "description": "The distance used when deriving connections between the upper and lower features. When the extremities for the upper and lower feature are within this distance, the area between the features is used f...",
                        "default": null
                },
                "interval": {
                        "type": "string",
                        "description": "The distance between the hachure ticks or triangles within the slope area. The default value is 10 meters.",
                        "default": null
                },
                "minimum_length": {
                        "type": "string",
                        "description": "The length a hachure tick or triangle must be to be created. Hachures that are shorter than this length will not  be created. The default value is 0 meters.",
                        "default": null
                },
                "alternate_hachures": {
                        "type": "string",
                        "description": "Specifies whether the length of every other hachure triangle or tick will differ.UNIFORM_HACHURES\u2014All hachures will be of uniform  length, which is the distance between the upper and lower slope lines...",
                        "default": null
                },
                "perpendicular": {
                        "type": "string",
                        "description": "Specifies whether the hachure ticks or triangles will be perpendicular to the upper slope line.NOT_PERPENDICULAR\u2014 Hachures will be oriented to obtain even spacing. This is the default.PERPENDICULAR\u2014Ha...",
                        "default": null
                },
                "polygon_base_width": {
                        "type": "string",
                        "description": "The width of the base of triangular polygon hachures. This parameter is enabled only when the  output_type parameter is set to polygon_triangles. The default value is 5 meters.",
                        "default": null
                }
        },
        "required": [
                "upper_lines",
                "lower_lines",
                "output_feature_class"
        ]
},
    "set_control_point_at_intersect": {
        "name": "set_control_point_at_intersect",
        "description": "Creates a control point at vertices that are shared by one or more line or polygon features. This tool is commonly used to synchronize boundary symbology on adjacent polygons.",
        "parameters": {
                "in_line_or_polygon_features": {
                        "type": "string",
                        "description": "The  line or polygon feature layer."
                },
                "in_features": {
                        "type": "string",
                        "description": "The line or polygon feature layer with features coincident to the input features.",
                        "default": null
                }
        },
        "required": [
                "in_line_or_polygon_features"
        ]
},
    "set_control_point_by_angle": {
        "name": "set_control_point_by_angle",
        "description": "Places a control point at vertices along a line or polygon outline where the angle created by a change in line direction is less than or equal to a specified maximum angle.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The  feature layer containing line or polygon features."
                },
                "maximum_angle": {
                        "type": "string",
                        "description": "The angle used to determine whether a vertex along a line or polygon outline  will be set as a control point. The angle value must be greater than zero and less than 180 decimal degrees."
                }
        },
        "required": [
                "in_features",
                "maximum_angle"
        ]
},
    "aggregate_points": {
        "name": "aggregate_points",
        "description": "Creates polygon features around clusters of proximate point features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point features that will be assessed for proximity and clustering."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class created to hold the polygons that represent the point clusters."
                },
                "aggregation_distance": {
                        "type": "string",
                        "description": "The distance between points that will be clustered."
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "aggregation_distance"
        ]
},
    "aggregate_polygons": {
        "name": "aggregate_polygons",
        "description": "Combines polygons that are within a specified distance of each other into new polygons.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The polygon features to be aggregated. If this is a layer referencing a representation and shape overrides are present on the input features, the overridden shapes, not the feature shapes, will be con..."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class to be created."
                },
                "aggregation_distance": {
                        "type": "string",
                        "description": "The distance to be satisfied between polygon boundaries for aggregation to occur. A distance must be specified, and it must be greater than zero. You can choose a preferred unit; the default is the fe..."
                },
                "minimum_area": {
                        "type": "string",
                        "description": "The minimum area for an aggregated polygon to be retained. The default value is zero, that is, to keep all polygons. You can specify a preferred unit; the default is the feature unit.",
                        "default": null
                },
                "minimum_hole_size": {
                        "type": "string",
                        "description": "The minimum size of a polygon hole to be retained. The default value is zero, that is, to keep all polygon holes. You can specify a preferred unit; the default is the feature unit.",
                        "default": null
                },
                "orthogonality_option": {
                        "type": "string",
                        "description": "Specifies the characteristic of the output features when constructing the aggregated boundaries.NON_ORTHOGONAL\u2014Organically shaped output features will be created. This is suitable for natural features...",
                        "default": null
                },
                "barrier_features": {
                        "type": "string",
                        "description": "The layers containing the line or polygon features that are aggregation barriers for input features. Features will not be aggregated across barrier features. Barrier features that are in geometric con...",
                        "default": null
                },
                "out_table": {
                        "type": "string",
                        "description": "A one-to-many relationship table that links the aggregated polygons to their source polygon features. This table contains two fields, OUTPUT_FID and INPUT_FID, that store the aggregated feature IDs an...",
                        "default": null
                },
                "aggregate_field": {
                        "type": "string",
                        "description": "The field that contains attributes for aggregation. Features must share the same attribute value to be considered for aggregation. For example, use a building classification field as the aggregate fie...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "aggregation_distance"
        ]
},
    "collapse_dual_lines_to_centerline": {
        "name": "collapse_dual_lines_to_centerline",
        "description": "Derives centerlines from dual-line (double-line) features, such as road casings, based on specified width tolerances.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input dual-line features, such as road casings, from which centerlines will be derived."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will be created."
                },
                "maximum_width": {
                        "type": "string",
                        "description": "The maximum width of the dual-line features that will be used to derive a centerline. A value must be specified, and it must be greater than zero. You can specify a unit; the default is the feature un..."
                },
                "minimum_width": {
                        "type": "string",
                        "description": "The minimum width of the dual-line features that will be used to derive a centerline. The minimum width must be greater than or equal to zero, and it must be less than the maximum width. The default v...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "maximum_width"
        ]
},
    "collapse_hydro_polygon": {
        "name": "collapse_hydro_polygon",
        "description": "Collapses or partially collapses hydro polygons to a \r\ncenterline based on a collapse width.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "One or more feature layers containing hydro polygons."
                },
                "out_line_feature_class": {
                        "type": "string",
                        "description": "The line feature class containing the centerlines of the collapsed polygons. It contains centerlines of all input polygons including those that are not collapsed. This feature class has a COLLAPSED at..."
                },
                "merge_adjacent_input_polygons": {
                        "type": "string",
                        "description": "Specifies whether adjacent input polygons will be merged before calculating the centerlines.\r\n\r\n\r\nMERGE_ADJACENT\u2014Input hydro polygons will be merged before calculating the centerlines. This is the\r\nde...",
                        "default": null
                },
                "connecting_features": {
                        "type": "string",
                        "description": "Input hydro line features that connect to the input hydro polygons to be collapsed. Line features will be created to maintain these connections.",
                        "default": null
                },
                "collapse_width": {
                        "type": "string",
                        "description": "The threshold width of an input hydro polygon to be considered for collapse. All polygons below the specified width will be collapsed. The default value is 0, which will collapse all features.",
                        "default": null
                },
                "collapse_width_tolerance": {
                        "type": "string",
                        "description": "A percentage tolerance within which features will be analyzed and the surrounding context will be considered when determining whether to collapse a feature. This is to minimize oscillations within the...",
                        "default": null
                },
                "minimum_length": {
                        "type": "string",
                        "description": "The minimum length required for a polygon to be retained in the output polygon  feature class. The minimum length is based on the length of the centerline created for the polygon. If the centerline of...",
                        "default": null
                },
                "out_poly_feature_class": {
                        "type": "string",
                        "description": "The polygon feature class containing the portions of the input hydro polygons  that are not collapsed. This parameter is applied only when the collapse_width parameter value is specified.",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_line_feature_class"
        ]
},
    "collapse_road_detail": {
        "name": "collapse_road_detail",
        "description": "Collapses small, open  configurations of road segments that interrupt the general trend of a road network, such as traffic circles, and replaces them with a simplified depiction. Configurations are collapsed regardless of  road class if the diameter across the open area is less than or equal to the Collapse Distance   parameter value. All roads from the input collection that are not collapsed will be copied to the output feature class. Learn more about how Collapse Road Detail works This tool is generally used to simplify a relatively large-scale road collection at a smaller scale when it is appropriate to depict traffic circles or other small interruptions to the network as a simple intersection. At medium scales, it may be preferable to retain these configurations as separate features and possibly exaggerate them. In that case,  consider using the Resolve Road Conflicts tool instead to ensure that symbolized lines are displayed without symbol conflicts.  If both Resolve Road Conflicts and Collapse Road Detail tools will be run on the same collection of roads, it is recommended that you run Collapse Road Detail first.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features containing small enclosed road details, such as traffic circles, to be collapsed."
                },
                "collapse_distance": {
                        "type": "string",
                        "description": "The diameter of, or distance across, the road detail that will be considered for collapse."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing the collapsed features\u2014features that were modified to accommodate the collapse\u2014and all unaffected features."
                },
                "locking_field": {
                        "type": "string",
                        "description": "The field that contains locking information for the features. The data type must be short or long integer. A value of 1 indicates that a feature will not be collapsed.",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "collapse_distance",
                "output_feature_class"
        ]
},
    "create_cartographic_partitions": {
        "name": "create_cartographic_partitions",
        "description": "Creates a mesh of polygon features that cover the input feature class in which each output polygon encloses no more than a specified number of  input features or input vertices. as determined by the density and distribution of the input features. The resulting  partition feature class is ideally suited for the  Cartographic Partitions geoprocessing environment setting. The Cartographic Partitions environment setting causes certain geoprocessing tools to load and process input features by partition. These tools operate contextually, meaning that multiple features, possibly from multiple themes, must be loaded simultaneously. Memory limitations are encountered with large datasets. Partitioning allows large datasets to be processed by these tools in portions sequentially.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature classes or layers with feature distribution and density, or vertex distribution and density, that determine the size and arrangement of output polygons. The input features are typica..."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output polygon feature class of partitions each of which encloses a manageable number of input features or manageable number of input vertices not exceeding the number specified by the feature_cou..."
                },
                "feature_count": {
                        "type": "string",
                        "description": "The ideal number of features or vertices (depending on the partition_method parameter value) to be enclosed by each polygon in the output feature class.\r\n  \r\nThe recommended count for features is 50,0..."
                },
                "partition_method": {
                        "type": "string",
                        "description": "Specifies whether the feature_count parameter references the ideal number of features or the ideal number of vertices in each output polygon. \r\nFEATURES\u2014Partitioning  considers the number and density ...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_features",
                "feature_count"
        ]
},
    "delineate_built_up_areas": {
        "name": "delineate_built_up_areas",
        "description": "Creates polygons to represent built-up areas by delineating densely clustered arrangements of buildings on small-scale maps. The boundaries\u2014or edges\u2014of the output polygons can be based on the location of other features such as roads or hydrology. Input buildings can be  attributed to identify those that can be replaced in maps by the built-up area polygons for a more generalized depiction.",
        "parameters": {
                "in_buildings": {
                        "type": "string",
                        "description": "The layers containing buildings with density and arrangement \r\nthat are used to define appropriate output built-up polygons. Multiple building layers can be assessed simultaneously. Building features ..."
                },
                "identifier_field": {
                        "type": "string",
                        "description": "A  field in the input feature classes that will hold a status code indicating whether the input feature is part of the resulting built-up area .  This field must be either short or long integer type a...",
                        "default": null
                },
                "edge_features": {
                        "type": "string",
                        "description": "The layers that will be used to define the edges of the built-up area polygons. Typically, these are roads, but other common examples are rivers, coastlines, and administrative areas. Built-up area po...",
                        "default": null
                },
                "grouping_distance": {
                        "type": "string",
                        "description": "Buildings closer together than the grouping distance are considered collectively as candidates for representation by an output built-up area polygon. \r\nThis distance is measured from the edges of poly..."
                },
                "minimum_detail_size": {
                        "type": "string",
                        "description": "The relative degree of detail in the output built-up area polygons. This is approximately to the minimum allowable diameter of \r\na hole or cavity in the built-up area polygon. The actual size and shap..."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing built-up area polygons representing clustered arrangements of input buildings."
                },
                "minimum_building_count": {
                        "type": "string",
                        "description": "The minimum number of buildings that must be collectively considered for representation by an output built-up area polygon. The default value is 4. The minimum building count must be greater than or e...",
                        "default": null
                }
        },
        "required": [
                "in_buildings",
                "grouping_distance",
                "minimum_detail_size",
                "out_feature_class"
        ]
},
    "merge_divided_roads": {
        "name": "merge_divided_roads",
        "description": "Generates single-line road features in place of matched pairs of  divided road lanes. Matched pairs of roads or lanes are merged if they are the same road class, trend generally parallel to one another, and are within the merge distance apart. The road class is specified by the Merge  Field parameter. All nonmerged roads from the input collection are copied to the output feature class. Learn more about how Merge Divided Roads works This tool is frequently used to simplify a larger-scale road collection at a smaller scale when it is appropriate to depict divided highways and boulevards as a single line. At medium scales, it may be preferable to retain divided roads as separate features. In this case, you can use the Resolve Road Conflicts tool instead to ensure that symbolized lanes are displayed without symbol conflicts. If both the Resolve Road Conflicts and Merge Divided Roads tools will be run on the same collection of roads, use the Merge Divided Roads tool first.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input linear road features that contain matched pairs of divided road lanes that will be merged into a single output line feature."
                },
                "merge_field": {
                        "type": "string",
                        "description": "The field that contains road classification information. Only parallel, proximate roads of equal classification will be merged. A value of 0 (zero) locks a feature to prevent it from participating in ..."
                },
                "merge_distance": {
                        "type": "string",
                        "description": "The minimum distance apart, in the specified units, for equal-class, relatively parallel road features to be merged. This distance must be greater than zero. If the units are in  points, millimeters, ..."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output feature class containing single-line merged road features and all unmerged road features."
                },
                "out_displacement_features": {
                        "type": "string",
                        "description": "The output polygon features containing the degree and direction of road displacement.",
                        "default": null
                },
                "character_field": {
                        "type": "string",
                        "description": "A short or long integer field that indicate the character of road segments, independent of  their road classification. The tool uses these values to refine the assessment of  candidate feature pairs f...",
                        "default": null
                },
                "out_table": {
                        "type": "string",
                        "description": "A many-to-many relationship table that links the merged  road features to their source features. This table contains two fields, OUTPUT_FID and INPUT_FID, which store the merged feature IDs and their ...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "merge_field",
                "merge_distance",
                "out_features"
        ]
},
    "simplify_building": {
        "name": "simplify_building",
        "description": "Simplifies the boundary or footprint of building polygons while maintaining their essential shape and size.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The building polygons to be simplified."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class to be created."
                },
                "simplification_tolerance": {
                        "type": "string",
                        "description": "The tolerance for building simplification. A tolerance must be specified, and it must be greater than zero. You can choose a preferred unit; the default is the feature unit."
                },
                "minimum_area": {
                        "type": "string",
                        "description": "The minimum area for a simplified building to be retained in feature units. The default value is zero, that is, to keep all buildings. You can specify a preferred unit; the default is the feature unit...",
                        "default": null
                },
                "conflict_option": {
                        "type": "string",
                        "description": "Specifies whether spatial conflicts\u2014that is, overlapping or touching among buildings\u2014will be identified. A SimBldFlag field is added to the output to store conflict flags. A value of 0 means no confli...",
                        "default": null
                },
                "in_barriers": {
                        "type": "string",
                        "description": "The input layers containing features to act as barriers for simplification. Resulting simplified buildings will not touch or cross barrier features. For example, when simplifying buildings, the result...",
                        "default": null
                },
                "collapsed_point_option": {
                        "type": "string",
                        "description": "Specifies whether an output point feature class will be created to store the centers of any buildings that are removed because they are smaller than the minimum_area parameter value. The point output ...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "simplification_tolerance"
        ]
},
    "simplify_line": {
        "name": "simplify_line",
        "description": "Simplifies lines by removing relatively extraneous vertices while preserving essential shape.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input line features that will be simplified."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The simplified output line feature class. It will contain all the fields from the input feature class. The output line feature class is topologically correct. The tool does not introduce topology erro..."
                },
                "algorithm": {
                        "type": "string",
                        "description": "Specifies the line simplification algorithm that will be used.POINT_REMOVE\u2014Critical points that preserve the essential shape of a line will be retained, and all other points will be removed (Douglas-P..."
                },
                "tolerance": {
                        "type": "string",
                        "description": "The degree of simplification that will be used. You can choose a preferred unit; otherwise, the units of the input will be used. The MinSimpTol and MaxSimpTol fields will be added to the output to sto..."
                },
                "error_resolving_option": {
                        "type": "string",
                        "description": "Legacy:This is a legacy parameter that is no longer used. It was formerly used to indicate how topological errors, possibly introduced during processing, were resolved. This parameter is still include...",
                        "default": null
                },
                "collapsed_point_option": {
                        "type": "string",
                        "description": "Specifies whether an output point feature class will be created to store the endpoints of lines that are smaller than the spatial tolerance. The point output is derived; it will use the same name and ...",
                        "default": null
                },
                "error_checking_option": {
                        "type": "string",
                        "description": "Note:This is a legacy parameter that is no longer used. It was formerly used to indicate how topological errors, possibly introduced during processing, were handled. This parameter is still included i...",
                        "default": null
                },
                "in_barriers": {
                        "type": "string",
                        "description": "Inputs containing features to act as barriers for simplification. Resulting simplified lines will not touch or cross barrier features. For example, when simplifying contour lines, spot height features...",
                        "default": null
                },
                "error_option": {
                        "type": "string",
                        "description": "Specifies how topological errors will be handled. Topological errors may be introduced in the simplification process and can include lines crossing or overlapping lines.NO_CHECK\u2014Topological errors wil...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "algorithm",
                "tolerance"
        ]
},
    "simplify_polygon": {
        "name": "simplify_polygon",
        "description": "Simplifies polygons by removing relatively extraneous vertices while preserving essential shape.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input polygon features that will be simplified."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The simplified output polygon feature class. It will contain all the fields from the input feature class. The output polygon feature class is topologically correct. The tool does not introduce topolog..."
                },
                "algorithm": {
                        "type": "string",
                        "description": "Specifies the polygon simplification algorithm that will be used.POINT_REMOVE\u2014Critical points that preserve the essential shape of a polygon outline will be retained, and all other points will be remo..."
                },
                "tolerance": {
                        "type": "string",
                        "description": "The degree of simplification that will be used. You can choose a preferred unit; otherwise, the units of the input will be used. The MinSimpTol and MaxSimpTol fields will be added to the output to sto..."
                },
                "minimum_area": {
                        "type": "string",
                        "description": "The minimum area for a polygon to be retained. The default value is zero, that is, to keep all polygons. You can choose a preferred unit for the specified value; otherwise, the units of the input will...",
                        "default": null
                },
                "error_option": {
                        "type": "string",
                        "description": "Specifies how topological errors will be handled. Topological errors may be introduced in the simplification process and can include lines crossing or overlapping lines.NO_CHECK\u2014Topological errors wil...",
                        "default": null
                },
                "collapsed_point_option": {
                        "type": "string",
                        "description": "Specifies whether an output point feature class will be created to store the centers of polygons that are removed because they are smaller than the minimum_area parameter value. The point output is de...",
                        "default": null
                },
                "in_barriers": {
                        "type": "string",
                        "description": "The inputs containing features to act as barriers for simplification. Resulting simplified polygons will not touch or cross barrier features. For example, when simplifying forested areas, the resultin...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "algorithm",
                "tolerance"
        ]
},
    "simplify_shared_edges": {
        "name": "simplify_shared_edges",
        "description": "Simplifies the edges of input features while maintaining the topological relationship with edges shared with other features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The lines or polygons to be simplified."
                },
                "algorithm": {
                        "type": "string",
                        "description": "Specifies the simplification algorithm.POINT_REMOVE\u2014Retains critical points that preserve the essential shape of a polygon outline and removes all other points (Douglas-Peucker). This is the default. ..."
                },
                "tolerance": {
                        "type": "string",
                        "description": "Determines the degree of simplification. If a unit is not specified, the units of the input will be used.For the POINT_REMOVE algorithm, the tolerance is the maximum allowable perpendicular distance b..."
                },
                "shared_edge_features": {
                        "type": "string",
                        "description": "Line or polygon features that will be simplified along edges shared with input features. Other edges are not simplified.",
                        "default": null
                },
                "minimum_area": {
                        "type": "string",
                        "description": "The minimum area for a polygon to be retained. The default value is zero, which will retain all polygons. A unit can be specified; if no unit is specified, the unit of the input will be used. This par...",
                        "default": null
                },
                "in_barriers": {
                        "type": "string",
                        "description": "Point, line, or polygon features that act as barriers for the simplification. The simplified features will not touch or cross barrier features.",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "algorithm",
                "tolerance"
        ]
},
    "smooth_line": {
        "name": "smooth_line",
        "description": "Smooths sharp angles in lines to improve aesthetic or cartographic quality. Learn more about how the Smooth Line and Smooth Polygon tools work.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The line features to be smoothed."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class to be created."
                },
                "algorithm": {
                        "type": "string",
                        "description": "Specifies the smoothing algorithm.PAEK\u2014This is the acronym for Polynomial Approximation with Exponential Kernel. A smoothed line that will not pass through the input line vertices will be calculated. ..."
                },
                "tolerance": {
                        "type": "string",
                        "description": "A tolerance used by the PAEK algorithm. A tolerance must be specified, and it must be greater than zero. You can choose a preferred unit; the default is the feature unit. You must enter a 0 as a place..."
                },
                "endpoint_option": {
                        "type": "string",
                        "description": "This is a legacy parameter that is no\r\nlonger used. It was formerly used to specify whether endpoints of closed lines would be preserved. This\r\nparameter is still included in the tool's syntax for com...",
                        "default": null
                },
                "error_option": {
                        "type": "string",
                        "description": "Specifies how topological errors (possibly introduced in the process, such as line crossing or overlapping) will be handled.NO_CHECK\u2014Topological errors will not be identified. This is the default. FLA...",
                        "default": null
                },
                "in_barriers": {
                        "type": "string",
                        "description": "Inputs containing features that will act as barriers for smoothing. The resulting smoothed lines will not touch or cross barrier features. For example, when smoothing contour lines, spot height featur...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "algorithm",
                "tolerance"
        ]
},
    "smooth_polygon": {
        "name": "smooth_polygon",
        "description": "Smooths sharp angles in polygon outlines to improve aesthetic or cartographic quality. Learn more about how the Smooth Line and Smooth Polygon tools work.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The polygon features to be smoothed."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output polygon feature class to be created."
                },
                "algorithm": {
                        "type": "string",
                        "description": "Specifies the smoothing algorithm.PAEK\u2014This is the acronym for Polynomial Approximation with Exponential Kernel. A smoothed polygon that will not pass through the input polygon vertices will be calcul..."
                },
                "tolerance": {
                        "type": "string",
                        "description": "Sets a tolerance used by the PAEK algorithm. A tolerance must be specified, and it must be greater than zero. You can choose a preferred unit; the default is the feature unit. You must enter a 0 as a ..."
                },
                "endpoint_option": {
                        "type": "string",
                        "description": "This is a legacy parameter that is no\r\nlonger used. It was formerly used to specify whether the endpoint of an isolated polygon ring would be preserved. This\r\nparameter is still included in the tool's...",
                        "default": null
                },
                "error_option": {
                        "type": "string",
                        "description": "Specifies how topological errors (possibly introduced in the process, such as line crossing or overlapping) will be handled.NO_CHECK\u2014Topological errors will not be identified. This is the default. FLA...",
                        "default": null
                },
                "in_barriers": {
                        "type": "string",
                        "description": "Inputs containing features that will act as barriers for smoothing. The resulting smoothed polygons will not touch or cross barrier features.",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "algorithm",
                "tolerance"
        ]
},
    "smooth_shared_edges": {
        "name": "smooth_shared_edges",
        "description": "Smooths the edges of the input features while maintaining the topological relationship with edges shared with other features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The lines or polygons to be smoothed."
                },
                "algorithm": {
                        "type": "string",
                        "description": "Specifies the smoothing algorithm.PAEK\u2014 Calculates a smoothed polygon that will not pass through the input polygon vertices. It is the acronym for Polynomial Approximation with Exponential Kernel. Thi..."
                },
                "tolerance": {
                        "type": "string",
                        "description": "Determines the degree of smoothing. A unit can be specified; if no unit is specified, the unit of the input will be used. This is only used for the PAEK algorithm. The parameter will not appear on the..."
                },
                "shared_edge_features": {
                        "type": "string",
                        "description": "Line or polygon features that will be smoothed along edges shared with input features. Other edges are not smoothed.",
                        "default": null
                },
                "in_barriers": {
                        "type": "string",
                        "description": "Point, line, or polygon features that act as barriers for smoothing. The smoothed features will not touch or cross barrier features.",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "algorithm",
                "tolerance"
        ]
},
    "thin_road_network": {
        "name": "thin_road_network",
        "description": "Generates a simplified road network that retains connectivity and general character for display at a smaller scale. This tool does not generate new output. It assigns values in the input data's Invisibility Field parameter value to identify features that are extraneous. These features can then be removed from view to result in a simplified, yet representative, collection of roads. No feature geometry is altered or deleted. Features are not actually deleted by Thin Road Network. To actually remove features, consider using the Trim Line tool. The resulting simplified road collection  is determined by feature significance, importance, and density. Segments that participate in very long itineraries across the extent of the data  are more significant than those required only for local travel. Road classification, or importance, is specified by the Hierarchy Field parameter. The density of the resulting street network is determined by the Minimum Length parameter, which corresponds to the shortest segment that is visually sensible to show at scale. See How Thin Road Network works to learn more and review a table of recommended minimum length values to use as a starting point. A warning is issued if the input features are not in a projected coordinate system. This tool relies on  linear distance units, which will create unexpected results in an unprojected coordinate system. It is recommended that you run this tool on data in a projected coordinate system to ensure valid results. An error occurs and the tool will not process if the coordinate system is missing or unknown.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input linear roads that will be thinned to create a simplified collection for display at smaller scales."
                },
                "minimum_length": {
                        "type": "string",
                        "description": "An indication of the shortest road segment that is sensible to display at the output scale. This controls the resolution, or density, of the resulting road collection.  If the units are in points, mil..."
                },
                "invisibility_field": {
                        "type": "string",
                        "description": "The field that stores the results of the tool. Features that participate in the resulting simplified road collection have a  value of 0 (zero). Those that are extraneous have a value of 1. A layer def..."
                },
                "hierarchy_field": {
                        "type": "string",
                        "description": "The field that contains hierarchical ranking of feature importance in which 1 is very important and larger integers reflect decreasing importance. A value of 0 forces the feature to remain visible in ..."
                }
        },
        "required": [
                "in_features",
                "minimum_length",
                "invisibility_field",
                "hierarchy_field"
        ]
},
    "detect_graphic_conflict": {
        "name": "detect_graphic_conflict",
        "description": "Creates polygons where two or more symbolized features graphically conflict.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature layer containing symbolized features. CAD, coverage, or VPF annotation, and dimensions, charts, dot-density or proportional symbols, raster layers, network datasets, and 3D symbols a..."
                },
                "conflict_features": {
                        "type": "string",
                        "description": "The feature layer containing symbolized features potentially in conflict with symbolized features  in the input layer."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class to be created to store conflict polygons. It cannot be one of the feature classes associated with the input layers."
                },
                "conflict_distance": {
                        "type": "string",
                        "description": "The area where input and conflict symbology is closer than a certain distance. Temporary buffers one-half the size of the conflict distance value\r\nare created around symbols in both the\r\ninput and con...",
                        "default": null
                },
                "line_connection_allowance": {
                        "type": "string",
                        "description": "The radius of a circle, centered where lines join, within which graphic overlaps won't be detected. This parameter is only considered when the input layer and the conflict layer are identical. Zero al...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "conflict_features",
                "out_feature_class"
        ]
},
    "propagate_displacement": {
        "name": "propagate_displacement",
        "description": "Propagates the displacement resulting from road adjustment in the Resolve Road Conflicts  and Merge Divided Roads tools to adjacent features to reestablish spatial relationships. An optional output of both the Resolve Road Conflicts  and Merge Divided Roads tools is a displacement feature class. Displacement features store the amount and direction of change from the initial state of the data before these tools are run. Displacement information can then be  applied to nearby features from different themes to ensure that spatial relationships are retained using this tool. For example, if roadways are separated by the Resolve Road Conflicts tool, it is often necessary to shift adjacent buildings along the roads accordingly.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature layer containing features that may be in conflict. May be point, line, or polygon."
                },
                "displacement_features": {
                        "type": "string",
                        "description": "The displacement polygon features created by the Resolve Road Conflicts or the Merge Divided Roads tools that contain the degree and direction of road displacement that took place. These polygons dict..."
                },
                "adjustment_style": {
                        "type": "string",
                        "description": "Defines the type of adjustment that will be used when displacing input features. AUTO\u2014The tool will decide for each input feature whether a SOLID or an ELASTIC adjustment is most appropriate. In gener..."
                }
        },
        "required": [
                "in_features",
                "displacement_features",
                "adjustment_style"
        ]
},
    "resolve_road_conflicts": {
        "name": "resolve_road_conflicts",
        "description": "Resolves graphic conflicts among symbolized road features by adjusting portions of line segments. Learn more about how Resolve Road Conflicts works Caution:This tool does not produce output layers. Instead, it alters the geometry of the source feature classes of the input  layers. It is recommended that you make a copy of the input features before you run this tool.",
        "parameters": {
                "in_layers": {
                        "type": "string",
                        "description": "The input feature layers containing symbolized road features that may be in conflict."
                },
                "hierarchy_field": {
                        "type": "string",
                        "description": "The field that contains hierarchical ranking of feature importance in which 1 is very important and larger integers reflect decreasing importance. A value of 0 (zero) locks the feature to ensure that ..."
                },
                "out_displacement_features": {
                        "type": "string",
                        "description": "The output polygon features containing the degree and direction of road displacement that will be used by the Propagate Displacement tool to preserve spatial relationships.",
                        "default": null
                }
        },
        "required": [
                "in_layers",
                "hierarchy_field"
        ]
},
    "merge_divided_roads": {
        "name": "merge_divided_roads",
        "description": "Generates single-line road features in place of matched pairs of  divided road lanes. Matched pairs of roads or lanes are merged if they are the same road class, trend generally parallel to one another, and are within the merge distance apart. The road class is specified by the Merge  Field parameter. All nonmerged roads from the input collection are copied to the output feature class. Learn more about how Merge Divided Roads works This tool is frequently used to simplify a larger-scale road collection at a smaller scale when it is appropriate to depict divided highways and boulevards as a single line. At medium scales, it may be preferable to retain divided roads as separate features. In this case, you can use the Resolve Road Conflicts tool instead to ensure that symbolized lanes are displayed without symbol conflicts. If both the Resolve Road Conflicts and Merge Divided Roads tools will be run on the same collection of roads, use the Merge Divided Roads tool first.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input linear road features that contain matched pairs of divided road lanes that will be merged into a single output line feature."
                },
                "merge_field": {
                        "type": "string",
                        "description": "The field that contains road classification information. Only parallel, proximate roads of equal classification will be merged. A value of 0 (zero) locks a feature to prevent it from participating in ..."
                },
                "merge_distance": {
                        "type": "string",
                        "description": "The minimum distance apart, in the specified units, for equal-class, relatively parallel road features to be merged. This distance must be greater than zero. If the units are in  points, millimeters, ..."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output feature class containing single-line merged road features and all unmerged road features."
                },
                "out_displacement_features": {
                        "type": "string",
                        "description": "The output polygon features containing the degree and direction of road displacement.",
                        "default": null
                },
                "character_field": {
                        "type": "string",
                        "description": "A short or long integer field that indicate the character of road segments, independent of  their road classification. The tool uses these values to refine the assessment of  candidate feature pairs f...",
                        "default": null
                },
                "out_table": {
                        "type": "string",
                        "description": "A many-to-many relationship table that links the merged  road features to their source features. This table contains two fields, OUTPUT_FID and INPUT_FID, which store the merged feature IDs and their ...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "merge_field",
                "merge_distance",
                "out_features"
        ]
},
    "resolve_building_conflicts": {
        "name": "resolve_building_conflicts",
        "description": "Resolves symbol conflicts among buildings with respect to linear barrier features by moving, resizing, or hiding buildings.",
        "parameters": {
                "in_buildings": {
                        "type": "string",
                        "description": "The input layers containing building features that may be in conflict or smaller than allowable size. Buildings can be either points or polygons. Buildings will be modified to resolve conflicts with o..."
                },
                "invisibility_field": {
                        "type": "string",
                        "description": "The short or long integer field that stores the invisibility values that can be used to remove some buildings from display to resolve symbol conflicts. Buildings with a value of 1 will be removed from..."
                },
                "in_barrierslayer_boolean_linear_unit": {
                        "type": "string",
                        "description": "The layers containing the linear or polygon features that are conflict barriers for input building features. Buildings will be modified to resolve conflicts between buildings and barriers. The orient ..."
                },
                "building_gap": {
                        "type": "string",
                        "description": "The minimum allowable distance between symbolized buildings at scale. Buildings that are closer together will be displaced or hidden to enforce this distance. The minimum allowable distance is set rel..."
                },
                "minimum_size": {
                        "type": "string",
                        "description": "The minimum allowable size of the shortest side of a rotated best-fit bounding box around the symbolized building feature drawn at the reference scale. Buildings with a bounding box side smaller than ..."
                },
                "hierarchy_field": {
                        "type": "string",
                        "description": "The short or long integer field that contains hierarchical ranking of feature importance in which 1 is very important and larger integers reflect decreasing importance. A value of 0 causes the buildin...",
                        "default": null
                }
        },
        "required": [
                "in_buildings",
                "invisibility_field",
                "in_barrierslayer_boolean_linear_unit",
                "building_gap",
                "minimum_size"
        ]
},
    "calculate_adjacent_fields": {
        "name": "calculate_adjacent_fields",
        "description": "Creates fields and calculates values for the neighboring pages (polygon) of a grid polygon feature class. The most common use case for this tool is to populate fields that can be used to label the adjacent pages in a map book. This tool appends eight new fields (each field representing one of the eight points of the compass: North, Northeast, East, Southeast, South, Southwest, West, and Northwest) to the input feature class and calculates values that identify the adjacent (neighboring) polygons, in each cardinal direction, for each feature in the input feature class.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The polygon grid index features that will be appended with adjacent field data."
                },
                "in_field": {
                        "type": "string",
                        "description": "The field whose values will be used to populate adjacent field data."
                }
        },
        "required": [
                "in_features",
                "in_field"
        ]
},
    "calculate_central_meridian_and_parallels": {
        "name": "calculate_central_meridian_and_parallels",
        "description": "Calculates the central meridian and optional standard parallels based on the center point of a feature's extent; stores this coordinate system as a spatial reference string in a specified text field; and repeats this for a set, or subset, of features. This field can be used with a spatial map series  to update the data frame coordinate system for each page.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature layer."
                },
                "in_field": {
                        "type": "string",
                        "description": "The text field where the coordinate system string will be stored."
                },
                "standard_offset": {
                        "type": "string",
                        "description": "The percentage of the height of the input feature used to offset the standard parallels from the center latitude of the input feature. The default is 25 percent or 0.25. Negative values and values gre...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "in_field"
        ]
},
    "calculate_grid_convergence_angle": {
        "name": "calculate_grid_convergence_angle",
        "description": "Calculates the rotation angle for true north based on the center point of each feature in a feature class and populates this value in a specified field. This field can be used in conjunction with a spatial map series to rotate each map to true north.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature class (points, multipoints, lines, and polygons)."
                },
                "angle_field": {
                        "type": "string",
                        "description": "The existing field that will be populated with the true north calculation value in decimal degrees."
                },
                "rotation_method": {
                        "type": "string",
                        "description": "Specifies the method used to calculate the rotation value.GEOGRAPHIC\u2014The angle is calculated clockwise with 0 at the top. This is the default.ARITHMETIC\u2014The angle is calculated counterclockwise with 0...",
                        "default": null
                },
                "coordinate_sys_field": {
                        "type": "string",
                        "description": "The field containing a projection engine string for a projected coordinate system to be used for angle calculation. The angle calculation for each feature will be based on the projected coordinate sys...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "angle_field"
        ]
},
    "calculate_utm_zone": {
        "name": "calculate_utm_zone",
        "description": "Calculates the UTM zone of each feature based on the center point and stores this spatial reference string in a specified field. This field can be used with a spatial map series  to update the spatial reference to the correct UTM zone for each map.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature layer."
                },
                "in_field": {
                        "type": "string",
                        "description": "The string field that stores the spatial reference string for the coordinate system. The field should have sufficient length (more than 600 characters) to hold the spatial reference string."
                }
        },
        "required": [
                "in_features",
                "in_field"
        ]
},
    "grid_index_features": {
        "name": "grid_index_features",
        "description": "Creates a grid of rectangular polygon features that can be used as an index to specify pages in a spatial map series. A grid can be created that includes only polygon features that intersect another feature layer.",
        "parameters": {
                "out_feature_class": {
                        "type": "string",
                        "description": "The resulting feature class of polygon index features. The coordinate system of the output feature class is determined in the following order:If a coordinate system is specified by the Output Coordina..."
                },
                "in_features": {
                        "type": "string",
                        "description": "The input features to be used to define the extent of the polygon grid that will be created.",
                        "default": null
                },
                "intersect_feature": {
                        "type": "string",
                        "description": "Limits the output grid feature class to areas that intersect input feature layers or datasets. The intersection of input features will be used to create index features.INTERSECTFEATURE\u2014Limits the outp...",
                        "default": null
                },
                "use_page_unit": {
                        "type": "string",
                        "description": "Specifies whether index polygon size input is in page units.USEPAGEUNIT\u2014Index polygon height and width are calculated in page units.NO_USEPAGEUNIT\u2014Index polygon height and width are calculated in map ...",
                        "default": null
                },
                "scale": {
                        "type": "string",
                        "description": "The map scale. The scale must be specified if the index polygon height and width are to be calculated in page units. If the tool is used outside an active ArcGIS Pro session, the default scale value i...",
                        "default": null
                },
                "polygon_width": {
                        "type": "string",
                        "description": "The width of the index polygon specified in either map or page units. If page units are used, the default value is 1 inch. If map units are used, the default value is 1 degree.",
                        "default": null
                },
                "polygon_height": {
                        "type": "string",
                        "description": "The height of the index polygon specified in either map or page units. If page units are used, the default value is 1 inch. If map units are used, the default value is 1 degree.",
                        "default": null
                },
                "origin_coord": {
                        "type": "string",
                        "description": "The coordinate value for the lower left origin of the output grid feature class. If input features are specified, the default value is determined by the extent of the union of extents for these featur...",
                        "default": null
                },
                "number_rows": {
                        "type": "string",
                        "description": "The number of rows to create in the y direction from the point of origin. The default is 10.",
                        "default": null
                },
                "number_columns": {
                        "type": "string",
                        "description": "The number of columns to create in the x direction from the point of origin. The default is 10.",
                        "default": null
                },
                "starting_page_number": {
                        "type": "string",
                        "description": "Each grid index feature is assigned a sequential page number starting with a specified starting page number. The default is 1.",
                        "default": null
                },
                "label_from_origin": {
                        "type": "string",
                        "description": "Specifies where page numbers (labels) begin.LABELFROMORIGIN\u2014Page numbers (labels) begin with the polygon feature in the lower left corner of the output grid.NO_LABELFROMORIGIN\u2014Page numbers (labels) be...",
                        "default": null
                }
        },
        "required": [
                "out_feature_class"
        ]
},
    "strip_map_index_features": {
        "name": "strip_map_index_features",
        "description": "Creates a series of rectangular polygons, or index features, that follow a single linear feature or a group of linear features. These index features can be used with spatial map series to define pages in a strip map or a set of maps that follow a linear feature. The resulting index features contain attributes that can be used to rotate and orient the map on the page and determine which index features, or pages, are next to the current page (to the left and right or to the top and bottom).",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input polyline features defining the path of the strip map index features."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class of polygon index features."
                },
                "use_page_unit": {
                        "type": "string",
                        "description": "Specifies whether index feature size input is in page units.USEPAGEUNIT\u2014Index polygon height and width are calculated in page units.NO_USEPAGEUNIT\u2014Index polygon height and width are calculated in map ...",
                        "default": null
                },
                "scale": {
                        "type": "string",
                        "description": "Map scale must be specified if index feature lengths (along the line and perpendicular to the line) are to be calculated in page units. If  you're using ArcGIS Pro, the default value will be the scale...",
                        "default": null
                },
                "length_along_line": {
                        "type": "string",
                        "description": "The length of the polygon index feature along the input line feature specified in either map or page units. The default value is determined by the spatial reference of the input line feature or featur...",
                        "default": null
                },
                "page_orientation": {
                        "type": "string",
                        "description": "Specifies the orientation of the input line features on the layout page.VERTICAL\u2014The direction of the strip map series on the page is top to bottom.HORIZONTAL\u2014The direction of the strip map series on ...",
                        "default": null
                },
                "overlap_percentage": {
                        "type": "string",
                        "description": "The approximate percentage of geographic overlap between an individual map page and its adjoining pages in the series. The default is 10.",
                        "default": null
                },
                "starting_page_number": {
                        "type": "string",
                        "description": "The page number of the starting page. Each grid index feature is assigned a sequential page number beginning with the specified starting page number. The default is 1.",
                        "default": null
                },
                "direction_type": {
                        "type": "string",
                        "description": "Specifies the initial direction of the strip maps.WE_NS\u2014If the line's directional trend is West to East, the starting point will be at the westernmost end of the line, or if the line's direction trend...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "calculate_central_meridian_and_parallels": {
        "name": "calculate_central_meridian_and_parallels",
        "description": "Calculates the central meridian and optional standard parallels based on the center point of a feature's extent; stores this coordinate system as a spatial reference string in a specified text field; and repeats this for a set, or subset, of features. This field can be used with a spatial map series  to update the data frame coordinate system for each page.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature layer."
                },
                "in_field": {
                        "type": "string",
                        "description": "The text field where the coordinate system string will be stored."
                },
                "standard_offset": {
                        "type": "string",
                        "description": "The percentage of the height of the input feature used to offset the standard parallels from the center latitude of the input feature. The default is 25 percent or 0.25. Negative values and values gre...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "in_field"
        ]
},
    "cul_de_sac_masks": {
        "name": "cul_de_sac_masks",
        "description": "Creates a feature class of polygon masks from a symbolized input line layer.",
        "parameters": {
                "input_layer": {
                        "type": "string",
                        "description": "The input line layer from which the masks will be created."
                },
                "output_fc": {
                        "type": "string",
                        "description": "The feature class that will contain the mask features."
                },
                "reference_scale": {
                        "type": "string",
                        "description": "The reference scale used for calculating the masking geometry when masks are specified in page units. This is typically the reference scale of the map."
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference of the map in which the masking polygons will be created. This is not the spatial reference that will be assigned to the output feature class. It is the spatial reference of the ..."
                },
                "margin": {
                        "type": "string",
                        "description": "The space in page units surrounding the symbolized input features used to create the mask polygons. Typically, masking polygons are created with a small margin around the symbol to improve visual appe..."
                },
                "attributes": {
                        "type": "string",
                        "description": "Specifies the attributes that will be transferred from the input features to the output features.ONLY_FID\u2014Only the FID field from the input features will be transferred to the output features. This is...",
                        "default": null
                }
        },
        "required": [
                "input_layer",
                "output_fc",
                "reference_scale",
                "spatial_reference",
                "margin"
        ]
},
    "feature_outline_masks": {
        "name": "feature_outline_masks",
        "description": "Creates mask polygons at a specified distance and shape around the symbolized features in the input layer. Learn more about how Feature Outline Masks and Intersecting Layers Masks work",
        "parameters": {
                "input_layer": {
                        "type": "string",
                        "description": "The symbolized input layer from which the masks will be created."
                },
                "output_fc": {
                        "type": "string",
                        "description": "The feature class that will contain the mask features."
                },
                "reference_scale": {
                        "type": "string",
                        "description": "The reference scale that will be used for calculating the masking geometry when masks are specified in page units. This is typically the reference scale of the map."
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference of the map in which the masking polygons will be created. This is not the spatial reference that will be assigned to the output feature class. It is the spatial reference of the ..."
                },
                "margin": {
                        "type": "string",
                        "description": "The space in page units surrounding the symbolized input features used to create the mask polygons. Typically, masking polygons are created with a small margin around the symbol to improve visual appe..."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the type of masking geometry that will be created. BOX\u2014A polygon representing the extent of the symbolized feature will be created. CONVEX_HULL\u2014The convex hull of the symbolized geometry of ..."
                },
                "mask_for_non_placed_anno": {
                        "type": "string",
                        "description": "Specifies whether masks for unplaced annotation will be created. This parameter is only used when masking geodatabase annotation layers.ALL_FEATURES\u2014Masks will be created for all annotation features. ..."
                },
                "attributes": {
                        "type": "string",
                        "description": "Specifies the attributes that will be transferred from the input features to the output features.ONLY_FID\u2014Only the FID field from the input features will be transferred to the output features. This is...",
                        "default": null
                },
                "preserve_small_sized_features": {
                        "type": "string",
                        "description": "Specifies whether small mask features will be included in the output feature class.DO_NOT_PRESERVE_SMALL_SIZED_FEATURES\u2014Small mask features will not be included in the output feature class. This is th...",
                        "default": null
                }
        },
        "required": [
                "input_layer",
                "output_fc",
                "reference_scale",
                "spatial_reference",
                "margin",
                "method",
                "mask_for_non_placed_anno"
        ]
},
    "intersecting_layers_masks": {
        "name": "intersecting_layers_masks",
        "description": "Creates masking polygons at a specified shape and size at the intersection of two symbolized input layers: the masking layer and the masked layer. Learn more about how Feature Outline Masks and Intersecting Layers Masks work",
        "parameters": {
                "masking_layer": {
                        "type": "string",
                        "description": "The symbolized input layer that will intersect the masked layer to create masking polygons. This is the layer that will be displayed when masking is applied to the masked layer."
                },
                "masked_layer": {
                        "type": "string",
                        "description": "The symbolized input layer that will be masked. This is the layer that will be obscured by the masking polygons."
                },
                "output_fc": {
                        "type": "string",
                        "description": "The feature class that will contain the mask features."
                },
                "reference_scale": {
                        "type": "string",
                        "description": "The reference scale that will be used for calculating the masking geometry when masks are specified in page units. This is typically the reference scale of the map."
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference of the map in which the masking polygons will be created. This is not the spatial reference that will be assigned to the output feature class. It is the spatial reference of the ..."
                },
                "margin": {
                        "type": "string",
                        "description": "The space in page units surrounding the symbolized input features used to create the mask polygons. Typically, masking polygons are created with a small margin around the symbol to improve visual appe..."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the type of masking geometry that will be created. BOX\u2014A polygon representing the extent of the symbolized feature will be created. CONVEX_HULL\u2014The convex hull of the symbolized geometry of ..."
                },
                "mask_for_non_placed_anno": {
                        "type": "string",
                        "description": "Specifies whether masks for unplaced annotation will be created. This parameter is only used when masking geodatabase annotation layers.ALL_FEATURES\u2014Masks will be created for all annotation features. ..."
                },
                "attributes": {
                        "type": "string",
                        "description": "Specifies the attributes that will be transferred from the input features to the output features.ONLY_FID\u2014Only the FID field from the input features will be transferred to the output features. This is...",
                        "default": null
                }
        },
        "required": [
                "masking_layer",
                "masked_layer",
                "output_fc",
                "reference_scale",
                "spatial_reference",
                "margin",
                "method",
                "mask_for_non_placed_anno"
        ]
}
}
