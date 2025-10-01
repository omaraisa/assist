# Generated ArcGIS Pro 3d-analyst AI Function Declarations
# Generated on 2025-10-01T14:32:45.605277
# Total tools: 40

functions_declarations = {
    "enclose_multipatch": {
        "name": "enclose_multipatch",
        "description": "Creates  closed multipatch features from open multipatch features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The multipatch features that will be used to construct closed multipatches."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output closed multipatch features."
                },
                "grid_size": {
                        "type": "string",
                        "description": "The resolution that will be used to construct the closed multipatch features.\r\nThis value is defined using the linear units of the input feature's spatial reference.",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "enforce_river_monotonicity": {
        "name": "enforce_river_monotonicity",
        "description": "Creates height adjusted breaklines from 3D polygons representing river banks.",
        "parameters": {
                "in_rivers": {
                        "type": "string",
                        "description": "The 3D polygons delineating the river banks that will be processed."
                },
                "in_flow_direction": {
                        "type": "string",
                        "description": "The line features that indicate the flow direction of the river bank polygons."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output river boundary lines."
                },
                "max_sample_distance": {
                        "type": "string",
                        "description": "The regular sampling distance of the polygon's boundary that will be used to establish monotonicity along the river banks.",
                        "default": null
                },
                "simplification_tolerance": {
                        "type": "string",
                        "description": "The z-range that will be used to simplify the resulting river boundary line.",
                        "default": null
                }
        },
        "required": [
                "in_rivers",
                "in_flow_direction",
                "out_feature_class"
        ]
},
    "generate_points_along_3d_lines": {
        "name": "generate_points_along_3d_lines",
        "description": "Creates 3D point features along 3D lines using three-dimensional distances.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The 3D line features that will be used to create points."
                },
                "out_features": {
                        "type": "string",
                        "description": "The 3D point features that will be created from the input lines."
                },
                "point_placement": {
                        "type": "string",
                        "description": "Specifies the method that will be used to sample the points along the 3D line features.PERCENTAGE\u2014The percentage parameter value will be used to place points along the features by percentage.DISTANCE\u2014...",
                        "default": null
                },
                "distance": {
                        "type": "string",
                        "description": "The interval from the beginning of the feature \r\nat which points will be placed.This parameter is active when the point_placement parameter is set to DISTANCE_FIELD.",
                        "default": null
                },
                "percentage": {
                        "type": "string",
                        "description": "The percentage from the beginning of the feature at which points will be placed. For example, if a percentage of 40 is used, \r\npoints will be placed at 40 percent and 80 percent of the feature's dista...",
                        "default": null
                },
                "include_end_points": {
                        "type": "string",
                        "description": "Specifies whether additional points will be included at the start point and end point of the feature.END_POINTS\u2014Additional points will be included at the start point and end point of the feature.NO_EN...",
                        "default": null
                },
                "add_chainage_fields": {
                        "type": "string",
                        "description": "Specifies whether the accumulated distance and sequence fields will be added to the output.ADD_CHAINAGE\u2014The accumulated distance (ORIG_LEN) and sequence (ORIG_SEQ) fields will be added to the output. ...",
                        "default": null
                },
                "distance_field": {
                        "type": "string",
                        "description": "A field from the input features that will be used to place output points.If the field is a numeric type, the field value will be used to place points at that interval.If the field is a string type, th...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_features"
        ]
},
    "is_closed_3d": {
        "name": "is_closed_3d",
        "description": "Evaluates multipatch features to determine whether each feature completely encloses a volume of space.",
        "parameters": {
                "in_feature_class": {
                        "type": "string",
                        "description": "The multipatch features to be tested."
                }
        },
        "required": [
                "in_feature_class"
        ]
},
    "simplify_3d_line": {
        "name": "simplify_3d_line",
        "description": "Generalizes 3D line features to reduce the overall number of vertices while approximating the original shape in horizontal and vertical directions within a specified tolerance.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The line features to be simplified."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The simplified output line features."
                },
                "tolerance": {
                        "type": "string",
                        "description": "The 3D distance threshold from the input lines that the simplified output must remain \r\nwithin."
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "tolerance"
        ]
},
    "ascii_3d_to_feature_class": {
        "name": "ascii_3d_to_feature_class",
        "description": "Imports 3D features from one or more ASCII files stored in XYZ, XYZI, or GENERATE formats into a new feature class.",
        "parameters": {
                "input": {
                        "type": "string",
                        "description": "The ASCII files or folders containing data in XYZ, XYZI (with lidar intensity), or 3D GENERATE format. All input files must be in the same format.  If a folder is specified, the File Suffix parameter ..."
                },
                "in_file_type": {
                        "type": "string",
                        "description": "The format of the ASCII files that will be converted to a feature class.XYZ\u2014Text file that contain geometry information stored as XYZ coordinates.XYZI\u2014Text files that contain XYZ coordinates alongside..."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class that will be produced."
                },
                "out_geometry_type": {
                        "type": "string",
                        "description": "The geometry type of the output feature class.\r\nMULTIPOINT\u2014Multipoints are recommended the input data contains a large number of points and attributes per feature are not required.POINT\u2014Each XYZ coord..."
                },
                "z_factor": {
                        "type": "string",
                        "description": "The factor by which z-values will be multiplied. This is typically used to convert z linear units to match x,y linear units. The default is 1, which leaves elevation values unchanged. This parameter i...",
                        "default": null
                },
                "input_coordinate_system": {
                        "type": "string",
                        "description": "The coordinate system of the input data. The default is an Unknown Coordinate System. If specified, the output may or may not be projected into a different coordinate system. This depends the whether ...",
                        "default": null
                },
                "average_point_spacing": {
                        "type": "string",
                        "description": "The average planimetric distance between points of the input. This parameter is only used when the output geometry is set to MULTIPOINT, and its function is to provide a means for grouping the points ...",
                        "default": null
                },
                "file_suffix": {
                        "type": "string",
                        "description": "The suffix of the files that will be imported from an input folder. This parameter is required when a folder is specified as input.",
                        "default": null
                },
                "decimal_separator": {
                        "type": "string",
                        "description": "The decimal character that will be used in the text file to differentiate the integer of a number from its fractional part.\t\t\t\t\tDECIMAL_POINT\u2014A point will be used as the decimal character. This is the...",
                        "default": null
                }
        },
        "required": [
                "input",
                "in_file_type",
                "out_feature_class",
                "out_geometry_type"
        ]
},
    "feature_class_z_to_ascii": {
        "name": "feature_class_z_to_ascii",
        "description": "Exports 3D features to ASCII text files storing GENERATE, XYZ, or profile data.",
        "parameters": {
                "in_feature_class": {
                        "type": "string",
                        "description": "The 3D point, multipoint, polyline, or polygon feature class that will be exported to an ASCII file."
                },
                "output_location": {
                        "type": "string",
                        "description": "The folder to which output files will be written."
                },
                "out_file": {
                        "type": "string",
                        "description": "The name of the resulting ASCII file. If a line or polygon feature class is exported to XYZ format, the file name is used as a base name. Each feature will have a unique file output, since the XYZ for..."
                },
                "format": {
                        "type": "string",
                        "description": "Specifies the format of the ASCII file being created.GENERATE\u2014Writes output in the GENERATE format. This is the default.XYZ\u2014Writes XYZ information of input features. One file will be created for each ...",
                        "default": null
                },
                "delimiter": {
                        "type": "string",
                        "description": "Specifies the delimiter that will indicate the separation of entries in the columns of the text file table.SPACE\u2014A space will be used to delimit field values. This is the default.COMMA\u2014A comma will be...",
                        "default": null
                },
                "decimal_format": {
                        "type": "string",
                        "description": "Specifies the method that will determine the number of significant digits stored in the output files.AUTOMATIC\u2014The number of significant digits needed to preserve the available precision, while removi...",
                        "default": null
                },
                "digits_after_decimal": {
                        "type": "string",
                        "description": "The number of digits written after the decimal for floating-point values written to the output files. This parameter is used when the Decimal Notation parameter is set to Specified Number (decimal_for...",
                        "default": null
                },
                "decimal_separator": {
                        "type": "string",
                        "description": "Specifies the decimal character that will differentiate the integer of a number from its fractional part.DECIMAL_POINT\u2014A point is used as the decimal character. This is the default.DECIMAL_COMMA\u2014A com...",
                        "default": null
                }
        },
        "required": [
                "in_feature_class",
                "output_location",
                "out_file"
        ]
},
    "feature_to_3d_by_attribute": {
        "name": "feature_to_3d_by_attribute",
        "description": "Creates 3D features using height values derived from the attribute of the input features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The features that will be used to create 3D features."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class that will be produced."
                },
                "height_field": {
                        "type": "string",
                        "description": "The field whose values will define the height of the resulting 3D features."
                },
                "to_height_field": {
                        "type": "string",
                        "description": "An optional second height field used for lines. When using two height fields, each line will start at the first height and end at the second (sloped).",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "height_field"
        ]
},
    "features_from_cityengine_rules": {
        "name": "features_from_cityengine_rules",
        "description": "Generates 3D geometries  from existing 2D and 3D input features using rules authored in ArcGIS CityEngine.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point, polygon, or multipatch features. \r\nInput features can be procedurally symbolized feature layers. Field mapping (attribute-driven symbol properties) will be honored."
                },
                "in_rule_package": {
                        "type": "string",
                        "description": "The CityEngine rule package file (*.rpk) containing CGA rule information and assets. The rule annotated with @StartRule in the .rpk file should be annotated @InPoint for a rule package intended for po..."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing multipatch features with CGA rules applied. An OriginalOID field is added to the output feature classes to contain the ObjectID of the input feature from which each..."
                },
                "in_existing_fields": {
                        "type": "string",
                        "description": "Specifies whether the output feature class will include the attribute fields of the input feature class. This parameter is not considered when the in_leaf_shapes parameter is used. INCLUDE_EXISTING_FI...",
                        "default": null
                },
                "in_include_reports": {
                        "type": "string",
                        "description": "Depending on how the rule package has been authored, it may contain logic that generates one or more reports as the models are created. These reports can contain a variety of information about the fea...",
                        "default": null
                },
                "in_leaf_shapes": {
                        "type": "string",
                        "description": "Specifies whether each input feature will be convert to a single, merged multipatch feature or become a set of many features that can be points, line, or multipatches.CityEngine rule packages construc...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "in_rule_package",
                "out_feature_class"
        ]
},
    "import_3d_files": {
        "name": "import_3d_files",
        "description": "Imports one or more 3D models into a multipatch feature class.",
        "parameters": {
                "in_files": {
                        "type": "string",
                        "description": "One or more 3D models or folders containing such files in the\r\nsupported formats, which  are 3D Studio Max (*.3ds), VRML and GeoVRML (*.wrl), OpenFlight (*.flt),  COLLADA (*.dae), and Wavefront OBJ mo..."
                },
                "out_featureclass": {
                        "type": "string",
                        "description": "The multipatch that will be created from the input files."
                },
                "root_per_feature": {
                        "type": "string",
                        "description": "Indicates whether to produce one feature per file or one feature for every root node in the  file. This option only applies to VRML models.ONE_ROOT_ONE_FEATURE\u2014The generated output will contain one fe...",
                        "default": null
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The coordinate system of the input data. For the majority of formats, this is unknown. Only the GeoVRML format stores its coordinate system, and its default will be obtained from the first file in the...",
                        "default": null
                },
                "y_is_up": {
                        "type": "string",
                        "description": "Identifies the axis that defines the vertical orientation of the input files.Z_IS_UP\u2014Indicates that z is up. This is the default.Y_IS_UP\u2014Indicated that y is up.",
                        "default": null
                },
                "file_suffix": {
                        "type": "string",
                        "description": "The file extension of the files to import from an input folder. This parameter is required when at least one folder is specified as an input.*\u2014All supported files. This is the default.3DS\u20143D Studio Ma..."
                },
                "in_featureclass": {
                        "type": "string",
                        "description": "The point features whose coordinates define the real-world position of the input files. Each input file will be matched to its corresponding point based on the file names stored in the Symbol Field. T...",
                        "default": null
                },
                "symbol_field": {
                        "type": "string",
                        "description": "The field in the point features containing the name of the 3D file associated with each point.",
                        "default": null
                }
        },
        "required": [
                "in_files",
                "out_featureclass",
                "file_suffix"
        ]
},
    "layer_3d_to_feature_class": {
        "name": "layer_3d_to_feature_class",
        "description": "Exports feature layers with 3D display properties to 3D lines or multipatch features.",
        "parameters": {
                "in_feature_layer": {
                        "type": "string",
                        "description": "The input feature layer with 3D display properties defined."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class with 3D features. Extruded points will be exported as 3D lines. Points with 3D symbols, extruded lines, and polygons will be exported as multipatch features."
                },
                "group_field": {
                        "type": "string",
                        "description": "The input feature's text field that will be used to merge multiple input features into the same output feature.  The resulting output's remaining attributes will be inherited from one of the input rec...",
                        "default": null
                },
                "disable_materials": {
                        "type": "string",
                        "description": "Specifies whether color and texture properties will be maintained when exporting a 3D layer to a multipatch feature class.DISABLE_COLORS_AND_TEXTURES\u2014Colors and textures will not be stored as part of ...",
                        "default": null
                }
        },
        "required": [
                "in_feature_layer",
                "out_feature_class"
        ]
},
    "extract_lod2_buildings": {
        "name": "extract_lod2_buildings",
        "description": "Creates 3D models of LOD2 buildings using building footprint polygons and a raster elevation surface.",
        "parameters": {
                "in_height_source": {
                        "type": "string",
                        "description": "The raster or mosaic layer that provides the height information for the buildings being modeled."
                },
                "in_features": {
                        "type": "string",
                        "description": "The polygon features that represent the footprint of the buildings that will be extracted."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output multipatch features that will contain the 3D building models."
                },
                "level_of_detail": {
                        "type": "string",
                        "description": "Specifies the level of detail that will be used to generate the rooftop in the building models. Each building will extend from the rooftop to the surrounding ground level.\r\nLOD1.2\u2014The building rooftop...",
                        "default": null
                },
                "smoothness_level": {
                        "type": "string",
                        "description": "A value between 0.0 and 1.0 that impacts the extent to which details in the building will be preserved or generalized. A higher value will result in a more simplified output, and a smaller value will ...",
                        "default": null
                },
                "extraction_accuracy": {
                        "type": "string",
                        "description": "Specifies the broader accuracy of the resulting building model.\r\nLOW\u2014A broader tolerance for the resulting 3D models will be used, which may lose some details in the building. This option has the shor...",
                        "default": null
                }
        },
        "required": [
                "in_height_source",
                "in_features",
                "out_feature_class"
        ]
},
    "extract_mesh_features_using_point_cloud": {
        "name": "extract_mesh_features_using_point_cloud",
        "description": "Extracts multipatch features representing objects in an integrated mesh based on a classified point cloud.",
        "parameters": {
                "in_mesh": {
                        "type": "string",
                        "description": "The integrated mesh I3S service or scene layer package that will be processed."
                },
                "in_point_cloud": {
                        "type": "string",
                        "description": "The LAS dataset, I3S point cloud, or point cloud scene layer package with classified points that will be used to extract features from the integrated mesh."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output multipatch features that represent the objects detected from the integrated mesh."
                },
                "class_codes": {
                        "type": "string",
                        "description": "The class code values from the point cloud that will be used to identify the objects in the integrated mesh. Each code will have a default group ID of the same value. A common group ID can be assigned..."
                },
                "point_distance_threshold": {
                        "type": "string",
                        "description": "The maximum distance between the centers of the subdivided mesh triangles and the points representing a given object. The mesh elements that are within this distance will be created as an object in th..."
                },
                "maximum_triangle_area": {
                        "type": "string",
                        "description": "The maximum area of the subdivided mesh triangles. The input mesh triangles are subdivided to optimize the quality of the output.",
                        "default": null
                },
                "cluster_distance": {
                        "type": "string",
                        "description": "The distance that will be used to cluster the points within each object group. When no value is specified, the point_distance_threshold parameter value will be used as the clustering distance.",
                        "default": null
                },
                "minimum_cluster_area": {
                        "type": "string",
                        "description": "The minimum surface area of the mesh triangles that are within the specified proximity from  a given object cluster. Any mesh object  cluster that is smaller than the specified value will be ignored. ...",
                        "default": null
                },
                "boundary": {
                        "type": "string",
                        "description": "A boundary that represents the 2D area that will be processed.\r\nWhen the expected data is in a subset of the integrated mesh, providing a boundary feature can optimize performance of the tool by limit...",
                        "default": null
                }
        },
        "required": [
                "in_mesh",
                "in_point_cloud",
                "out_feature_class",
                "class_codes",
                "point_distance_threshold"
        ]
},
    "extract_multipatch_from_mesh": {
        "name": "extract_multipatch_from_mesh",
        "description": "Creates a multipatch feature from the portion of an integrated mesh that overlaps a polygon.",
        "parameters": {
                "source_mesh": {
                        "type": "string",
                        "description": "The integrated mesh that will be processed."
                },
                "footprint_features": {
                        "type": "string",
                        "description": "The polygon features defining the area \r\nthat will be clipped."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output multipatch feature class."
                }
        },
        "required": [
                "source_mesh",
                "footprint_features",
                "out_feature_class"
        ]
},
    "extract_power_lines_from_point_cloud": {
        "name": "extract_power_lines_from_point_cloud",
        "description": "Extracts 3D line features modeling power lines \r\nfrom classified point cloud data.",
        "parameters": {
                "in_point_cloud": {
                        "type": "string",
                        "description": "The LAS dataset layer containing points classified as power lines."
                },
                "class_codes": {
                        "type": "string",
                        "description": "The class code values for the points representing the power lines."
                },
                "out_3d_lines": {
                        "type": "string",
                        "description": "The \r\n3D lines modeling the power lines."
                },
                "point_tolerance": {
                        "type": "string",
                        "description": "The distance used to establish the points that belong to a given power line. The default is 80 centimeters.",
                        "default": null
                },
                "separation_distance": {
                        "type": "string",
                        "description": "The distance apart points must be to determine if they belong to different power lines. The default is 1 meter.",
                        "default": null
                },
                "max_sampling_gap": {
                        "type": "string",
                        "description": "The largest gap that can exist in a given span\r\nof a power line. The catenary curve being modeled from a set of power line points will be extended by this distance to find other points that fit the sa...",
                        "default": null
                },
                "line_tolerance": {
                        "type": "string",
                        "description": "The distance that will be used to establish the accuracy of the output power line. A larger distance will result in the creation of less vertices per line, yielding a more coarse representation of the...",
                        "default": null
                },
                "wind_correction": {
                        "type": "string",
                        "description": "Specifies whether the output power lines will be adjusted for the influence of wind. When wind correction is applied, it can be used to either improve the fitting of wind modified points or model the ...",
                        "default": null
                },
                "min_wind_span": {
                        "type": "string",
                        "description": "The shortest distance a power line span can be to apply wind correction when generating the output power line. The default is 60 meters.",
                        "default": null
                },
                "max_wind_deviation": {
                        "type": "string",
                        "description": "The maximum angle that the wind is expected to deviate a given power line.\r\nThe default is 10 degrees.",
                        "default": null
                },
                "end_point_search_radius": {
                        "type": "string",
                        "description": "The distance that will be used to identify a common suspension point for power line segments connected to the same distribution pole or transmission tower. The default is 10 meters.",
                        "default": null
                },
                "min_length": {
                        "type": "string",
                        "description": "The shortest wire length that can be used to determine the presence of a common end point. The default is 5 meters.",
                        "default": null
                },
                "eliminate_wind": {
                        "type": "string",
                        "description": "Specifies how wind correction will be applied to the output power lines. Wind correction will only be applied for catenary curves that span a distance longer than the value specified in the min_wind_s...",
                        "default": null
                },
                "min_line_length": {
                        "type": "string",
                        "description": "The minimum 3D length of the output wires. Lines that have a length shorter than the value specified for this parameter will be omitted from the output.",
                        "default": null
                }
        },
        "required": [
                "in_point_cloud",
                "class_codes",
                "out_3d_lines"
        ]
},
    "extract_rails_from_point_cloud": {
        "name": "extract_rails_from_point_cloud",
        "description": "Extracts rail track lines and center lines from classified \r\nrailroad tracks in a LAS dataset, point cloud scene layer package, or I3S point cloud layer.",
        "parameters": {
                "in_point_cloud": {
                        "type": "string",
                        "description": "The input LAS dataset or point cloud scene layer containing the classified railway points."
                },
                "class_codes": {
                        "type": "string",
                        "description": "The class codes that will be used for rail points."
                },
                "out_3d_lines": {
                        "type": "string",
                        "description": "The output 3D rail lines that will be extracted from the point cloud."
                },
                "rail_standard": {
                        "type": "string",
                        "description": "Specifies the rail standard that will be used. The standard describes the measurements of the track gauge and rail thickness. The specification will impact the algorithm that will be used for extracti...",
                        "default": null
                },
                "out_3d_centerlines": {
                        "type": "string",
                        "description": "The output 3D center line that represents the middle of the rail track.",
                        "default": null
                },
                "track_gauge": {
                        "type": "string",
                        "description": "The track gauge that describes the inner distance between the two rails of a railway track. The default is 1435 millimeters, which corresponds to the US 115 RE standard, but this value will be updated...",
                        "default": null
                },
                "rail_thickness": {
                        "type": "string",
                        "description": "The width of the top part of each rail. The default value  is 66.675 millimeters, which corresponds to the US 115 RE standard, but this value will be updated to match the specified rail standard.",
                        "default": null
                },
                "horizontal_smoothing_kernel_distance": {
                        "type": "string",
                        "description": "The x,y distance that will be used to apply a weighted average-based smoothing function in the horizontal direction onto the output rail lines. This parameter will help to overcome the distortions of ...",
                        "default": null
                },
                "vertical_smoothing_kernel_distance": {
                        "type": "string",
                        "description": "The z-distance that will be used to apply a weighted average-based smoothing function in the vertical direction onto the output rail lines. This parameter will help to overcome the distortions of inco...",
                        "default": null
                },
                "horizontal_rail_tolerance": {
                        "type": "string",
                        "description": "The distance that will be used in the x,y direction to identify points that belong to the same rail in a given track. The default is 10 centimeters.",
                        "default": null
                },
                "vertical_rail_tolerance": {
                        "type": "string",
                        "description": "The distance that will be used in the z-direction to identify points that belong to the same rail in a given track. The default is 3 centimeters.",
                        "default": null
                },
                "centerline_alignment_tolerance": {
                        "type": "string",
                        "description": "The tolerance distance that will be used to align the centerline feature between the rails of a given track. The default is 50 millimeters.",
                        "default": null
                },
                "rail_crown_detection_radius": {
                        "type": "string",
                        "description": "The search radius that will be used to identify continuous points that define the rail crown, which is the topmost portion of a given rail track. The default is 20 meters.",
                        "default": null
                },
                "horizontal_simplification_tolerance": {
                        "type": "string",
                        "description": "The distance that will be used to simplify the output rail line in the x,y direction. The horizontal position of the simplified rail will not deviate from the original by more than this amount. The de...",
                        "default": null
                },
                "vertical_simplification_tolerance": {
                        "type": "string",
                        "description": "The distance that will be used to simplify the output rail line in the z-direction. The height of the simplified rail will not deviate from the original by more than this amount. The default is 2 mill...",
                        "default": null
                },
                "min_line_length": {
                        "type": "string",
                        "description": "The minimum three-dimensional length that a detected line must have to be included in the output line features. Any detected line that is shorter than this length will be ignored. The default is 1 met...",
                        "default": null
                }
        },
        "required": [
                "in_point_cloud",
                "class_codes",
                "out_3d_lines"
        ]
},
    "las_building_multipatch": {
        "name": "las_building_multipatch",
        "description": "Creates building models using rooftop points in a LAS dataset.",
        "parameters": {
                "in_las_dataset": {
                        "type": "string",
                        "description": "The LAS dataset containing the points that will define the building rooftop."
                },
                "in_features": {
                        "type": "string",
                        "description": "The polygon features that define the building footprint."
                },
                "ground": {
                        "type": "string",
                        "description": "The source of ground height values can be either a numeric field in the building footprint attribute table or a raster or TIN surface. A field-based ground source will be processed faster than a surfa..."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The multipatch feature class that will store the output building models."
                },
                "point_selection": {
                        "type": "string",
                        "description": "Specifies the LAS points that will be used to define the building rooftop.BUILDING_CLASSIFIED_POINTS\u2014LAS points assigned a class code value of 6 will be used. This is the default.LAYER_FILTERED_POINTS...",
                        "default": null
                },
                "simplification": {
                        "type": "string",
                        "description": "A z-tolerance value that will be used to simplify the rooftop geometry. This value defines the maximum deviation of the output rooftop model from the TIN surface created using the LAS points.",
                        "default": null
                },
                "sampling_resolution": {
                        "type": "string",
                        "description": "The binning size used to thin the point cloud before constructing the rooftop surface.",
                        "default": null
                },
                "min_height_field": {
                        "type": "string",
                        "description": "The numeric field containing the minimum height of the points that will be used to define the rooftop.  Any numeric field can be specified. Points that are lower than the value in this field will be i...",
                        "default": null
                },
                "max_height_field": {
                        "type": "string",
                        "description": "The numeric field containing the maximum height of the points that will be used to define the rooftop.  Any numeric field can be specified. Points that are higher than the value in this field will be ...",
                        "default": null
                }
        },
        "required": [
                "in_las_dataset",
                "in_features",
                "ground",
                "out_feature_class"
        ]
},
    "multipatch_footprint": {
        "name": "multipatch_footprint",
        "description": "Creates polygon footprints representing the two-dimensional  area of multipatch features.",
        "parameters": {
                "in_feature_class": {
                        "type": "string",
                        "description": "The multipatch feature whose footprint will be generated."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The resulting footprint polygon feature class."
                },
                "group_field": {
                        "type": "string",
                        "description": "The field that will be used for combining multipatch features so that they \r\ncontribute to the same footprint polygon.",
                        "default": null
                }
        },
        "required": [
                "in_feature_class",
                "out_feature_class"
        ]
},
    "regularize_adjacent_building_footprint": {
        "name": "regularize_adjacent_building_footprint",
        "description": "Regularizes building footprints that have common boundaries.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features that will be processed."
                },
                "group": {
                        "type": "string",
                        "description": "The field that will be used to determine which features share coincident, non-overlapping boundaries."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class that will be produced."
                },
                "method": {
                        "type": "string",
                        "description": "The method that will be used to regularize the input features.RIGHT_ANGLES\u2014Identifies the best line segments that fit the input feature vertices along 90\u00b0 and 180\u00b0 angles.RIGHT_ANGLES_AND_DIAGONALS\u2014Id..."
                },
                "tolerance": {
                        "type": "string",
                        "description": "The maximum distance that the regularized footprint can deviate from the boundary of its originating feature."
                },
                "precision": {
                        "type": "string",
                        "description": "The precision of the spatial grid that will be used in the regularization process. Valid values range from 0.05 to 0.25."
                },
                "angular_limit": {
                        "type": "string",
                        "description": "The maximum deviation of the best fit line's interior angles that will be tolerated when using the Right Angles and Diagonals (RIGHT_ANGLES_AND_DIAGONALS) method.\r\nThis value should generally be kept ..."
                }
        },
        "required": [
                "in_features",
                "group",
                "out_feature_class",
                "method",
                "tolerance",
                "precision",
                "angular_limit"
        ]
},
    "regularize_building_footprint": {
        "name": "regularize_building_footprint",
        "description": "Normalizes the footprint of building polygons by eliminating undesirable artifacts in their geometry.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The polygons that represent the building footprints to be regularized."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class that will be produced."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the regularization method that will be used in processing the input features.\r\nRIGHT_ANGLES\u2014Shapes composed of 90\u00b0 angles between adjoining edges will be constructed.RIGHT_ANGLES_AND_DIAGONA..."
                },
                "tolerance": {
                        "type": "string",
                        "description": "For most methods, this value represents the maximum distance that the regularized footprint can deviate from the boundary of its originating feature. The specified value will be based on the linear un..."
                },
                "densification": {
                        "type": "string",
                        "description": "The sampling interval that will be used to evaluate whether the regularized feature will be straight or bent. The densification must be equal to or less than the tolerance value. This parameter is onl..."
                },
                "precision": {
                        "type": "string",
                        "description": "The precision of the spatial grid that will be used in the regularization process. Valid values range from 0.05 to 0.25."
                },
                "diagonal_penalty": {
                        "type": "string",
                        "description": "When the RIGHT_ANGLES_AND_DIAGONALS method is used, this value identifies the likelihood of constructing right angles or diagonal edges between two adjoining segments. When the ANY_ANGLES method is us..."
                },
                "min_radius": {
                        "type": "string",
                        "description": "The smallest radius allowed for a regularized circle. A value of 0 implies that there is no minimum size limit. This option is only available with the CIRCLE method."
                },
                "max_radius": {
                        "type": "string",
                        "description": "The largest radius allowed for a regularized circle. This option is only available with the CIRCLE method."
                },
                "alignment_feature": {
                        "type": "string",
                        "description": "The line feature that will be used to align the orientation of the regularized polygons. Each polygon will only be aligned to one line feature.",
                        "default": null
                },
                "alignment_tolerance": {
                        "type": "string",
                        "description": "The maximum distance threshold that will be used for finding the nearest alignment feature. For example, a value of 20 meters means the nearest line that is within 20 meters will be used to align the ...",
                        "default": null
                },
                "tolerance_type": {
                        "type": "string",
                        "description": "Specifies how tolerance will be applied when the method parameter is set to CIRCLE.DISTANCE\u2014The tolerance will represent the maximum distance from the boundary of the feature being processed. This is ...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "method",
                "tolerance",
                "densification",
                "precision",
                "diagonal_penalty",
                "min_radius",
                "max_radius"
        ]
},
    "interpolate_polygon_to_multipatch": {
        "name": "interpolate_polygon_to_multipatch",
        "description": "Creates surface-conforming  multipatch features by draping polygon features over a surface.",
        "parameters": {
                "in_surface": {
                        "type": "string",
                        "description": "The input triangulated irregular network (TIN) or terrain dataset surface."
                },
                "in_feature_class": {
                        "type": "string",
                        "description": "The input polygon feature."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output multipatch feature class."
                },
                "max_strip_size": {
                        "type": "string",
                        "description": "Controls the maximum number of points used to create an individual triangle strip. Note that each multipatch is usually composed of multiple strips. The default value is 1,024.",
                        "default": null
                },
                "z_factor": {
                        "type": "string",
                        "description": "The factor by which z-values will be multiplied. This is typically used to convert z linear units to match x,y linear units. The default is 1, which leaves elevation values unchanged. This parameter i...",
                        "default": null
                },
                "area_field": {
                        "type": "string",
                        "description": "The name of the output field containing the planimetric, or 2D, area of the resulting multipatches.",
                        "default": null
                },
                "surface_area_field": {
                        "type": "string",
                        "description": "The name of the output field containing the 3D area of the resulting multipatches. This area takes the surface undulations into consideration and is always larger than the planimetric area unless the ...",
                        "default": null
                },
                "pyramid_level_resolution": {
                        "type": "string",
                        "description": "The z-tolerance or window-size resolution of the terrain pyramid level that will be used. The default is 0, or full resolution.",
                        "default": null
                }
        },
        "required": [
                "in_surface",
                "in_feature_class",
                "out_feature_class"
        ]
},
    "interpolate_shape": {
        "name": "interpolate_shape",
        "description": "Creates 3D features by interpolating z-values from a surface. Learn more about how Interpolate Shape works",
        "parameters": {
                "in_surface": {
                        "type": "string",
                        "description": "The surface that will be used for interpolating z-values."
                },
                "in_feature_class": {
                        "type": "string",
                        "description": "The input features that will be processed."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class that will be produced."
                },
                "sample_distance": {
                        "type": "string",
                        "description": "The spacing at which z-values will be interpolated. By default, this is a raster dataset's cell size or a triangulated surface's natural densification.",
                        "default": null
                },
                "z_factor": {
                        "type": "string",
                        "description": "The factor by which z-values will be multiplied. This is typically used to convert z linear units to match x,y linear units. The default is 1, which leaves elevation values unchanged. This parameter i...",
                        "default": null
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the interpolation method that will be used to determine elevation values for the output features. The available options depend on the surface type.\r\nBILINEAR\u2014The value of the query point wil...",
                        "default": null
                },
                "vertices_only": {
                        "type": "string",
                        "description": "Specifies whether the interpolation will only occur along the vertices of an input feature, ignoring the sample distance option.DENSIFY\u2014Interpolation will occur using the sampling distance. This is th...",
                        "default": null
                },
                "pyramid_level_resolution": {
                        "type": "string",
                        "description": "The z-tolerance or window-size resolution of the terrain pyramid level that will be used. The default is 0, or full resolution.",
                        "default": null
                },
                "preserve_features": {
                        "type": "string",
                        "description": "Specifies whether features with one or more vertices that fall outside the raster's data area will be retained in the output. This parameter is only available when the input surface is a raster and th...",
                        "default": null
                }
        },
        "required": [
                "in_surface",
                "in_feature_class",
                "out_feature_class"
        ]
},
    "update_feature_z": {
        "name": "update_feature_z",
        "description": "Updates the z-coordinates of 3D feature vertices using a surface.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The 3D features whose vertex z-values will be modified."
                },
                "in_surface": {
                        "type": "string",
                        "description": "The surface that will be used to  \r\ndetermine the new z-value for the 3D feature vertices."
                },
                "method": {
                        "type": "string",
                        "description": "Interpolation method used in determining information about the surface. The available options depend on the data type of the input surface:BILINEAR\u2014An interpolation method  exclusive to the raster sur...",
                        "default": null
                },
                "status_field": {
                        "type": "string",
                        "description": "An existing numeric field that will be populated with values to reflect whether the feature's vertices were successfully updated.  A value of 1 would be specified for updated features and 0 for featur...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "in_surface"
        ]
},
    "calculate_missing_z_values": {
        "name": "calculate_missing_z_values",
        "description": "Creates features that update the z-values of 3D line or polygon vertices with placeholder values that represent missing z-value information.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The 3D line or polygon features with missing z-values."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output features whose placeholder z-values will be updated."
                },
                "placeholder": {
                        "type": "string",
                        "description": "The z-value that represents missing or unknown information in the feature's geometry."
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "placeholder"
        ]
},
    "locate_outliers": {
        "name": "locate_outliers",
        "description": "Identifies anomalous elevation measurements from terrain, TIN, or LAS datasets that exceed a defined range of elevation values or have slope characteristics that are inconsistent with the surrounding surface.",
        "parameters": {
                "in_surface": {
                        "type": "string",
                        "description": "The terrain, TIN, or LAS  dataset that will be analyzed."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class that will be produced."
                },
                "apply_hard_limit": {
                        "type": "string",
                        "description": "Specifies use of absolute z minimum and maximum to find outliers. \r\nAPPLY_HARD_LIMIT\u2014Use the absolute z minimum and maximum to find outliers.NO_APPLY_HARD_LIMIT\u2014Do not use the absolute z minimum and m...",
                        "default": null
                },
                "absolute_z_min": {
                        "type": "string",
                        "description": "If hard limits are applied, any point with an elevation below this value will be considered an outlier.  The default is 0.",
                        "default": null
                },
                "absolute_z_max": {
                        "type": "string",
                        "description": "If hard limits are applied, any point with an elevation above this value will be considered an outlier.   The default is 0.",
                        "default": null
                },
                "apply_comparison_filter": {
                        "type": "string",
                        "description": "The comparison filter consists of three parameters for determining outliers: z_tolerance, slope_tolerance, and exceed_tolerance_ratio.APPLY_COMPARISON_FILTER\u2014Use the three comparison parameters (z_tol...",
                        "default": null
                },
                "z_tolerance": {
                        "type": "string",
                        "description": "Compares z-values of neighboring points if the comparison filter is applied.   The default is 0.",
                        "default": null
                },
                "slope_tolerance": {
                        "type": "string",
                        "description": "The threshold of slope variance between consecutive points that will be used to identify outlier points. Slope is expressed as a percentage, with the default being 150.",
                        "default": null
                },
                "exceed_tolerance_ratio": {
                        "type": "string",
                        "description": "Defines the criteria for determining each outlier point as a function of the ratio of points in its natural neighborhood that  must exceed the specified comparison filters. For example, the default va...",
                        "default": null
                },
                "outlier_cap": {
                        "type": "string",
                        "description": "The maximum number of outlier points that can be written to the output. Once this value is reached, no further outliers are sought.   The default is 2,500.",
                        "default": null
                }
        },
        "required": [
                "in_surface",
                "out_feature_class"
        ]
},
    "surface_aspect": {
        "name": "surface_aspect",
        "description": "Creates polygon features that represent aspect measurements derived  from a TIN, terrain, or LAS dataset surface.",
        "parameters": {
                "in_surface": {
                        "type": "string",
                        "description": "The TIN,  terrain, or LAS dataset surface that will be processed."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class that will be produced."
                },
                "class_breaks_table": {
                        "type": "string",
                        "description": "A table containing the classification breaks that will be used to define the aspect ranges in the output feature class.",
                        "default": null
                },
                "aspect_field": {
                        "type": "string",
                        "description": "The field containing aspect code values.",
                        "default": null
                },
                "pyramid_level_resolution": {
                        "type": "string",
                        "description": "The z-tolerance or window-size resolution of the terrain pyramid level that will be used. The default is 0, or full resolution.",
                        "default": null
                }
        },
        "required": [
                "in_surface",
                "out_feature_class"
        ]
},
    "surface_contour": {
        "name": "surface_contour",
        "description": "Creates contour lines derived from a terrain, TIN, or LAS dataset surface. Learn more about how Surface Contour works",
        "parameters": {
                "in_surface": {
                        "type": "string",
                        "description": "The TIN,  terrain, or LAS dataset surface that will be processed."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class that will be produced."
                },
                "interval": {
                        "type": "string",
                        "description": "The interval between the contours."
                },
                "base_contour": {
                        "type": "string",
                        "description": "Defines the starting Z value from which the contour interval is either added or subtracted to delineate contours. The default value is 0.0.",
                        "default": null
                },
                "contour_field": {
                        "type": "string",
                        "description": "The field that stores  the contour value associated with each line in the output feature class.",
                        "default": null
                },
                "contour_field_precision": {
                        "type": "string",
                        "description": "The precision of the contour field. Zero specifies an integer, and the numbers 1\u20139 indicate how many decimal places the field will contain. By default, the field will be an integer (0).",
                        "default": null
                },
                "index_interval": {
                        "type": "string",
                        "description": "Index contours are commonly used as a cartographic aid for assisting in the visualization of contour lines. The index interval is typically five times larger than the contour interval. Use of this par...",
                        "default": null
                },
                "index_interval_field": {
                        "type": "string",
                        "description": "The name of the field used to identify index contours. This will only be used if the index_interval is defined. By default, the field name is Index.",
                        "default": null
                },
                "z_factor": {
                        "type": "string",
                        "description": "The factor by which z-values will be multiplied. This is typically used to convert z linear units to match x,y linear units. The default is 1, which leaves elevation values unchanged. This parameter i...",
                        "default": null
                },
                "pyramid_level_resolution": {
                        "type": "string",
                        "description": "The z-tolerance or window-size resolution of the terrain pyramid level that will be used. The default is 0, or full resolution.",
                        "default": null
                }
        },
        "required": [
                "in_surface",
                "out_feature_class",
                "interval"
        ]
},
    "surface_slope": {
        "name": "surface_slope",
        "description": "Creates polygon features that represent ranges of slope values for triangulated surfaces.",
        "parameters": {
                "in_surface": {
                        "type": "string",
                        "description": "The TIN, terrain, or LAS dataset whose slope measurements will be written to the output polygon feature."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class that will be produced."
                },
                "units": {
                        "type": "string",
                        "description": "The units of measure to be used in calculating slope.PERCENT\u2014Slope is expressed as a percentage value. This is the default.DEGREE\u2014Slope is expressed as the angle of inclination from a horizontal plane...",
                        "default": null
                },
                "class_breaks_table": {
                        "type": "string",
                        "description": "A table containing classification breaks that will be used to group the output features. The first column of this table will indicate the break point, whereas the second will provide the classificatio...",
                        "default": null
                },
                "slope_field": {
                        "type": "string",
                        "description": "The field containing slope values.",
                        "default": null
                },
                "z_factor": {
                        "type": "string",
                        "description": "The factor by which z-values will be multiplied. This is typically used to convert z linear units to match x,y linear units. The default is 1, which leaves elevation values unchanged. This parameter i...",
                        "default": null
                },
                "pyramid_level_resolution": {
                        "type": "string",
                        "description": "The z-tolerance or window-size resolution of the terrain pyramid level that will be used. The default is 0, or full resolution.",
                        "default": null
                }
        },
        "required": [
                "in_surface",
                "out_feature_class"
        ]
},
    "construct_sight_lines": {
        "name": "construct_sight_lines",
        "description": "Creates line features that represent sight lines from one or more observer points to features in a  target feature class.",
        "parameters": {
                "in_observer_points": {
                        "type": "string",
                        "description": "The single-point features that represent observer points. Multipoint features are not supported."
                },
                "in_target_features": {
                        "type": "string",
                        "description": "The target features (points, multipoints, lines, and polygons)."
                },
                "out_line_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing the  sight lines."
                },
                "observer_height_field": {
                        "type": "string",
                        "description": "The source of the height values for the observer points obtained  from its attribute table.A default Observer Height Field field is selected from among the options listed below  by order of priority. ...",
                        "default": null
                },
                "target_height_field": {
                        "type": "string",
                        "description": "The height field for the target.    A default Target Height Field field is selected from among the options listed below  by order of priority. If multiple fields exist, and the desired field does not ...",
                        "default": null
                },
                "join_field": {
                        "type": "string",
                        "description": "The join field is used to match observers to specific targets.   &lt;None&gt;\u2014No Z values will be assigned to the resulting sight line features.",
                        "default": null
                },
                "sample_distance": {
                        "type": "string",
                        "description": "The distance between samples when the target is either a line or polygon feature class.   The Sampling Distance units  are interpreted in the XY units of the output feature class.",
                        "default": null
                },
                "output_the_direction": {
                        "type": "string",
                        "description": "Specifies whether to add direction attributes to the output sight lines.  Two additional fields will be added and populated to indicate direction: AZIMUTH and VERT_ANGLE (vertical angle).NOT_OUTPUT_TH...",
                        "default": null
                },
                "sampling_method": {
                        "type": "string",
                        "description": "Specifies how the sampling distance will be used to establish sight lines along the target feature.2D_DISTANCE\u2014The distance will be evaluated in two-dimensional Cartesian space. This is the default.3D...",
                        "default": null
                }
        },
        "required": [
                "in_observer_points",
                "in_target_features",
                "out_line_feature_class"
        ]
},
    "geodesic_viewshed": {
        "name": "geodesic_viewshed",
        "description": "Determines the raster surface locations visible to a set of observer features using geodesic methods. Learn more about how the Geodesic Viewshed tool works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster. It can be an integer or a floating-point raster.The input raster is transformed into a 3D geocentric coordinate system during the visibility calculation. NoData cells on the ..."
                },
                "in_observer_features": {
                        "type": "string",
                        "description": "The input feature class that identifies the observer locations. It can be point, multipoint, or polyline features.The input feature class is transformed into a 3D geocentric coordinate system during t..."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster.For the FREQUENCY analysis type, when the vertical error parameter is 0 or not specified, the output raster records the number of times that each cell location in the input surface r..."
                },
                "out_agl_raster": {
                        "type": "string",
                        "description": "The output above ground level (AGL) raster.The AGL result is a raster in which each cell value is the minimum height that must be added to a cell that is not visible to make it visible by at least one...",
                        "default": null
                },
                "analysis_type": {
                        "type": "string",
                        "description": "Specifies the type of visibility analysis that will be performed, either determining how visible each cell is to the observers or identifying the observers that are visible for each surface location.F...",
                        "default": null
                },
                "vertical_error": {
                        "type": "string",
                        "description": "The amount of uncertainty (the root mean square [RMS] error) in the surface elevation values. It is a floating-point value representing the expected error of the input elevation values. When this para...",
                        "default": null
                },
                "out_observer_region_relationship_table": {
                        "type": "string",
                        "description": "The output table for identifying the regions that are visible to each observer. This table can be related to the input observer feature class and the output visibility raster for identifying the regio...",
                        "default": null
                },
                "refractivity_coefficient": {
                        "type": "string",
                        "description": "The coefficient of the refraction of visible light in air.The default value is 0.13.",
                        "default": null
                },
                "surface_offset": {
                        "type": "string",
                        "description": "A vertical distance that will be added to the z-value of each cell as it is considered for visibility. It must be a positive integer or floating-point value.You can select a field in the input observe...",
                        "default": null
                },
                "observer_elevation": {
                        "type": "string",
                        "description": "The surface elevations of the observer points or vertices.You can select a field in the input observers dataset, or you can specify a numerical value.When this parameter is not specified, the observer...",
                        "default": null
                },
                "observer_offset": {
                        "type": "string",
                        "description": "A vertical distance that will be added to the observer elevation. It must be a positive integer or floating-point value.You can select a field in the input observers dataset, or you can specify a nume...",
                        "default": null
                },
                "inner_radius": {
                        "type": "string",
                        "description": "The start distance from which visibility will be determined. Cells closer than this distance will not be visible in the output but can still block visibility of the cells between inner radius and oute...",
                        "default": null
                },
                "inner_radius_is_3d": {
                        "type": "string",
                        "description": "Specifies the type of distance that will be used for the inner radius parameter.GROUND\u2014The inner radius will be interpreted as a 2D distance. This is the default.3D\u2014The inner radius will be interprete...",
                        "default": null
                },
                "outer_radius": {
                        "type": "string",
                        "description": "The maximum distance from which visibility will be determined. Cells beyond this distance will be excluded from the analysis.You can select a field in the input observers dataset, or you can specify a...",
                        "default": null
                },
                "outer_radius_is_3d": {
                        "type": "string",
                        "description": "Specifies the type of distance that will be used for the outer radius parameter.GROUND\u2014The outer radius will be interpreted as a 2D distance. This is the default.3D\u2014The outer radius will be interprete...",
                        "default": null
                },
                "horizontal_start_angle": {
                        "type": "string",
                        "description": "The start angle of the horizontal scan range. Provide the value in degrees from 0 to 360 with 0 oriented to north. The value can be integer or floating point. The default value is 0.You can select a f...",
                        "default": null
                },
                "horizontal_end_angle": {
                        "type": "string",
                        "description": "The end angle of the horizontal scan range. Provide the value in degrees from 0 to 360 with 0 oriented to north. The value can be integer or floating point. The default value is 360.You can select a f...",
                        "default": null
                },
                "vertical_upper_angle": {
                        "type": "string",
                        "description": "The upper vertical angle limit of the scan relative to the horizontal plane. Provide the value in degrees from above -90 up to and including 90. The value can be integer or floating point. The default...",
                        "default": null
                },
                "vertical_lower_angle": {
                        "type": "string",
                        "description": "The lower vertical angle limit of the scan relative to the horizontal plane. Provide the value in degrees from -90 up to but not including 90. The value can be integer or floating point. The default v...",
                        "default": null
                },
                "analysis_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to calculate visibility. This parameter allows you to decide on performance level.ALL_SIGHTLINES\u2014A sightline will be run to every cell on the raster to establish...",
                        "default": null
                },
                "analysis_target_device": {
                        "type": "string",
                        "description": "Specifies the device that will be used to perform the calculation.GPU_THEN_CPU\u2014If a compatible GPU is found, it will be used to perform the calculation. Otherwise, the CPU will be used. This is the de...",
                        "default": null
                }
        },
        "required": [
                "in_raster",
                "in_observer_features",
                "out_raster"
        ]
},
    "intervisibility": {
        "name": "intervisibility",
        "description": "Determines the visibility of sight lines using  potential obstructions defined by any combination of  3D features and surfaces.",
        "parameters": {
                "sight_lines": {
                        "type": "string",
                        "description": "The 3D sight lines whose visibility will be determined."
                },
                "obstructions": {
                        "type": "string",
                        "description": "The mesh and surface datasets that provide potential obstructions for sight lines. Obstructions can be defined by any combination of multipatch features, integrated mesh scene layers,  TIN datasets, a..."
                },
                "visible_field": {
                        "type": "string",
                        "description": "The name of the field that will store the visibility results.  A resulting value of 0 indicates that the sight line's start and end points are not visible to one another.   A value of 1 indicates that...",
                        "default": null
                }
        },
        "required": [
                "sight_lines",
                "obstructions"
        ]
},
    "line_of_sight": {
        "name": "line_of_sight",
        "description": "Determines the visibility of sight lines over obstructions consisting of a surface and an optional multipatch dataset. Learn more about how Line Of Sight works",
        "parameters": {
                "in_surface": {
                        "type": "string",
                        "description": "The integrated mesh scene layer, LAS dataset, raster, TIN, or terrain  surface that will be used to determine visibility."
                },
                "in_line_feature_class": {
                        "type": "string",
                        "description": "The sight line features whose first vertex defines the observation point and last vertex identifies the target location. When the sight lines are 2D features, the observer and target heights will be d..."
                },
                "out_los_feature_class": {
                        "type": "string",
                        "description": "The output line feature class along which visibility will be determined"
                },
                "out_obstruction_feature_class": {
                        "type": "string",
                        "description": "An optional point feature class identifying the location of the first obstruction on  the observer's sight line  to its target.",
                        "default": null
                },
                "use_curvature": {
                        "type": "string",
                        "description": "Specifies whether the earth's curvature will be taken into consideration for the line-of-sight analysis.   For this parameter to be enabled, the surface must have a defined spatial reference in projec...",
                        "default": null
                },
                "use_refraction": {
                        "type": "string",
                        "description": "Specifies whether atmospheric refraction will be taken into consideration when generating a  line of sight  from a functional surface. This parameter does not apply if multipatch features are used.REF...",
                        "default": null
                },
                "refraction_factor": {
                        "type": "string",
                        "description": "The value that will be used as the refraction factor. The default value is 0.13.",
                        "default": null
                },
                "pyramid_level_resolution": {
                        "type": "string",
                        "description": "The z-tolerance or window-size resolution of the terrain pyramid level that will be used. The default value is 0, which is full resolution.",
                        "default": null
                },
                "in_features": {
                        "type": "string",
                        "description": "A multipatch feature that may define additional obstructing elements, such as buildings.  Refraction options are not honored for this input.",
                        "default": null
                },
                "output_graphing_attributes": {
                        "type": "string",
                        "description": "Specifies whether the output sight line attributes will include additional fields with information that can be used in a profile graph.The values in these fields provide the  information for generatin...",
                        "default": null
                }
        },
        "required": [
                "in_surface",
                "in_line_feature_class",
                "out_los_feature_class"
        ]
},
    "observer_points": {
        "name": "observer_points",
        "description": "Identifies which observer points are visible from each raster surface location. The Geodesic Viewshed tool provides enhanced functionality or performance. Learn more about how Observer Points works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "in_observer_point_features": {
                        "type": "string",
                        "description": "The point feature class that identifies the observer locations.The maximum number of points allowed is 16."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster.The output identifies exactly which observer points are visible from each raster surface location."
                },
                "z_factor": {
                        "type": "string",
                        "description": "The number of ground x,y units in one surface z-unit.The z-factor adjusts the units of measure for the z-units when they are different from the x,y units of the input surface. The z-values of the inpu...",
                        "default": null
                },
                "curvature_correction": {
                        "type": "string",
                        "description": "Specifies whether correction for the earth's curvature will be applied.FLAT_EARTH\u2014No curvature correction will be applied. This is the default.CURVED_EARTH\u2014Curvature correction will be applied.",
                        "default": null
                },
                "refractivity_coefficient": {
                        "type": "string",
                        "description": "The coefficient of the refraction of visible light in air.The default value is 0.13.",
                        "default": null
                },
                "out_agl_raster": {
                        "type": "string",
                        "description": "The output above ground level (AGL) raster.The AGL result is a raster where each cell value is the minimum height that must be added to an otherwise nonvisible cell to make it visible by at least one ...",
                        "default": null
                }
        },
        "required": [
                "in_raster",
                "in_observer_point_features",
                "out_raster"
        ]
},
    "skyline": {
        "name": "skyline",
        "description": "Generates a line or multipatch feature class containing the results from a skyline or silhouette analysis. Learn more about how Skyline works",
        "parameters": {
                "in_observer_point_features": {
                        "type": "string",
                        "description": "The 3D points representing observers.  Each feature will have its own output."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The 3D features that will either be lines that represent the skyline or multipatches that represent silhouettes."
                },
                "in_surface": {
                        "type": "string",
                        "description": "The topographic surface that will be used to define the horizon. If no surface is provided, a virtual surface\r\nwill be used, defined by the  virtual_surface_radius and  virtual_surface_elevation param...",
                        "default": null
                },
                "virtual_surface_radius": {
                        "type": "string",
                        "description": "The radius of the virtual surface that will be used  to define the horizon when no input surface is provided. The default is 1,000 meters.",
                        "default": null
                },
                "virtual_surface_elevation": {
                        "type": "string",
                        "description": "The elevation of the virtual surface that will be used to define the horizon in lieu of an actual surface. This parameter is ignored if an actual surface is provided. The default is 0.",
                        "default": null
                },
                "in_features": {
                        "type": "string",
                        "description": "The features that will be used to determine the skyline. If no features are specified, the skyline will consist\r\nsolely of the horizon line as defined by the topographic or virtual surface.",
                        "default": null
                },
                "feature_lod": {
                        "type": "string",
                        "description": "Specifies the level of detail at which each feature will be examined.FULL_DETAIL\u2014Every edge in the feature will be considered in the skyline analysis (only edges of triangles and exterior rings are co...",
                        "default": null
                },
                "from_azimuth_value_or_field": {
                        "type": "string",
                        "description": "The direction from which the skyline analysis will start. This value is a  geometric angle in degrees in the range of -360\u00b0 to 360\u00b0. The default is 0\u00b0, which is due north. Angular values increment in ...",
                        "default": null
                },
                "to_azimuth_value_or_field": {
                        "type": "string",
                        "description": "The direction at which the skyline analysis will complete. This value is a  geometric angle in degrees in the range of -360\u00b0 to 360\u00b0.  The analysis starts from the observer point and increments from t...",
                        "default": null
                },
                "azimuth_increment_value_or_field": {
                        "type": "string",
                        "description": "The angular interval, in degrees, at which the horizon will be evaluated while conducting the skyline analysis between the from_azimuth_value_or_field and to_azimuth_value_or_field parameter values. T...",
                        "default": null
                },
                "max_horizon_radius": {
                        "type": "string",
                        "description": "The maximum distance from the observer location that a horizon will be sought. A value of zero indicates that no limit will be imposed.  The default is 0.",
                        "default": null
                },
                "segment_skyline": {
                        "type": "string",
                        "description": "Specifies whether the resulting skyline will have one feature for each observer point or each observer's skyline will be segmented by the unique elements that contribute to the skyline. This parameter...",
                        "default": null
                },
                "scale_to_percent": {
                        "type": "string",
                        "description": "The percent of the original vertical angle (angle above the horizon or angle of elevation) or elevation each skyline vertex will be placed. If a value of 0 or 100 is used, scaling will not occur. The ...",
                        "default": null
                },
                "scale_according_to": {
                        "type": "string",
                        "description": "Specifies how scaling will be performed.VERTICAL_ANGLE\u2014Scaling will be performed based on the vertical angle of each vertex relative to the observer point. This is the default.ELEVATION\u2014Scaling will b...",
                        "default": null
                },
                "scale_method": {
                        "type": "string",
                        "description": "Specifies the vertex that will be used for scale calculation.SKYLINE_MAXIMUM\u2014Vertices will be scaled relative to the vertical angle (or elevation) of the vertex with the highest vertical angle (or ele...",
                        "default": null
                },
                "use_curvature": {
                        "type": "string",
                        "description": "Specifies whether the curvature of the earth will be used when generating the ridgeline from a functional surface. This parameter is only available when a raster surface is specified for the in_surfac...",
                        "default": null
                },
                "use_refraction": {
                        "type": "string",
                        "description": "Specifies whether atmospheric refraction will be applied when generating the ridgeline from a functional surface. This option is only available when a raster surface is specified for the in_surface pa...",
                        "default": null
                },
                "refraction_factor": {
                        "type": "string",
                        "description": "The refraction coefficient that will be used if atmospheric refraction is applied. The default is 0.13.",
                        "default": null
                },
                "pyramid_level_resolution": {
                        "type": "string",
                        "description": "The z-tolerance or window-size resolution of the terrain pyramid level that will be used. The default is 0, or full resolution.",
                        "default": null
                },
                "create_silhouettes": {
                        "type": "string",
                        "description": "Specifies whether output features will represent skylines defining the barrier between the input data and the open sky or silhouettes representing the facade of observable input features. This option ...",
                        "default": null
                },
                "apply_max_radius_to_features": {
                        "type": "string",
                        "description": "Specifies whether the max_horizon_radius parameter value will be applied to the input features.NO_APPLY_MAX_RADIUS_TO_FEATURES\u2014The radius will not apply to the input features. This is the default.APPL...",
                        "default": null
                },
                "vertical_offset": {
                        "type": "string",
                        "description": "The height offset in z-units that will be applied to each observer when determining its skyline. The offset can be defined by a numeric value that is applied to all observers or by a numeric field in ...",
                        "default": null
                }
        },
        "required": [
                "in_observer_point_features",
                "out_feature_class"
        ]
},
    "skyline_barrier": {
        "name": "skyline_barrier",
        "description": "Generates a multipatch feature class representing a skyline barrier or shadow volume. Learn more about how Skyline Barrier works",
        "parameters": {
                "in_observer_point_features": {
                        "type": "string",
                        "description": "The point feature class containing the observer points."
                },
                "in_features": {
                        "type": "string",
                        "description": "The input line feature class that represents the skylines, or the input multipatch feature class that represents the silhouettes."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class into which the skyline barrier or shadow volume will be placed."
                },
                "min_radius_value_or_field": {
                        "type": "string",
                        "description": "The minimum radius that the triangle edges will be extended from the observer point. For example, value of 10 meters means that all output barrier features will extend at least 10 meters from their po...",
                        "default": null
                },
                "max_radius_value_or_field": {
                        "type": "string",
                        "description": "The maximum radius that the triangle edges will be extended from the observer point. The default is 0, meaning no maximum distance is enforced.",
                        "default": null
                },
                "closed": {
                        "type": "string",
                        "description": "Specifies whether a skirt and a base will be added to the skyline barrier so that the resulting multipatch will appear to be a closed solid.NO_CLOSED\u2014No skirt or base will be added to the multipatch; ...",
                        "default": null
                },
                "base_elevation": {
                        "type": "string",
                        "description": "The elevation of the base of the closed multipatch. This parameter is ignored if the closed parameter is set to NO_CLOSED.   The default is 0.",
                        "default": null
                },
                "project_to_plane": {
                        "type": "string",
                        "description": "Specifies whether the front (nearer to the observer) and back (farther from the observer) ends of the barrier should each be projected onto a vertical plane. This is typically set to PROJECT_TO_PLANE ...",
                        "default": null
                }
        },
        "required": [
                "in_observer_point_features",
                "in_features",
                "out_feature_class"
        ]
},
    "skyline_graph": {
        "name": "skyline_graph",
        "description": "Calculates the sky visibility ratio and generates an optional table and a polar graph.",
        "parameters": {
                "in_observer_point_features": {
                        "type": "string",
                        "description": "The input features containing one or more observer points."
                },
                "in_line_features": {
                        "type": "string",
                        "description": "The line features that represent the skyline."
                },
                "base_visibility_angle": {
                        "type": "string",
                        "description": "The baseline vertical angle that will be used to calculate the percentage of visible sky. Zero is the horizon, 90 is straight up, and -90 is straight down. The default is 0.",
                        "default": null
                },
                "additional_fields": {
                        "type": "string",
                        "description": "Specifies whether additional fields will be included in the angles table.NO_ADDITIONAL_FIELDS\u2014Additional fields will not be included. This is the default.ADDITIONAL_FIELDS\u2014Additional fields will be in...",
                        "default": null
                },
                "out_angles_table": {
                        "type": "string",
                        "description": "The table that will be created for outputting the horizontal and vertical angles from the observer point to each of the vertices on the skyline.",
                        "default": null
                },
                "out_graph": {
                        "type": "string",
                        "description": "This parameter is not supported.",
                        "default": null
                },
                "out_image_file": {
                        "type": "string",
                        "description": "The image of the polar chart depicting the radial view of the visible skyline.\r\nThe image can be created in PNG, JPG, JPEG, or SVG format.",
                        "default": null
                }
        },
        "required": [
                "in_observer_point_features",
                "in_line_features"
        ]
},
    "sun_shadow_frequency": {
        "name": "sun_shadow_frequency",
        "description": "Calculates the number of times a fixed position on a surface has its direct sight line to the sun obstructed by multipatch features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The multipatch features that will constitute the source of obstruction for sunlight."
                },
                "ground": {
                        "type": "string",
                        "description": "The raster ground surface that will define the \r\npositions where sunlight obstruction will be evaluated."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster whose cell values reflect the number of times the corresponding ground height position was obstructed by the input features."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output raster.",
                        "default": null
                },
                "start_time": {
                        "type": "string",
                        "description": "The date and time sun position calculations will begin. The default value is the date and time the tool is initialized.",
                        "default": null
                },
                "end_time": {
                        "type": "string",
                        "description": "The date and time sun position calculations will end. The time_interval parameter is used to iteratively evaluate each day from the start time to the end time. For this reason, the end time cannot be ...",
                        "default": null
                },
                "time_interval": {
                        "type": "string",
                        "description": "The interval that will be used to calculate sun positions from the start date and time to the end \r\ndate and time.",
                        "default": null
                },
                "time_zone": {
                        "type": "string",
                        "description": "Specifies the time zone that corresponds to the specified input times that will be used to determine the relative position of the sun.UTC\u2014The time zone will be UTC.Dateline_Standard_Time\u2014The time zone...",
                        "default": null
                },
                "dst": {
                        "type": "string",
                        "description": "Specifies whether the input times will be adjusted for daylight saving time.\r\nDST\u2014The input times will be adjusted for daylight saving time.NO_DST\u2014The input times will not be adjusted for daylight sav...",
                        "default": null
                },
                "max_shadow_length": {
                        "type": "string",
                        "description": "The maximum distance that a shadow will be cast from an input feature during calculation.\r\nConsider defining this value when the sun position has a low altitude angle, as the resulting shadows will be...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "ground",
                "out_raster"
        ]
},
    "sun_shadow_volume": {
        "name": "sun_shadow_volume",
        "description": "Creates closed volumes that model shadows cast by each feature using sunlight for a given date and time.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The multipatch features that will be used to model shadows."
                },
                "start_date_and_time": {
                        "type": "string",
                        "description": "The date and time from which sun positions will be determined. Both a date and a time must be provided, and only the times when the sun is above the horizon will produce an output shadow volume."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The multipatch feature class that will store the resulting shadow volumes."
                },
                "adjusted_for_dst": {
                        "type": "string",
                        "description": "Specifies whether the time value will be adjusted for daylight saving time (DST).ADJUSTED_FOR_DST\u2014The time value will be adjusted for DST.NOT_ADJUSTED_FOR_DST\u2014The time value will not be adjusted for D...",
                        "default": null
                },
                "time_zone": {
                        "type": "string",
                        "description": "The time zone in which the participating input is located. The default setting is the time zone to which the operating system is set.UTC\u2014The time zone will be UTC.Dateline_Standard_Time\u2014The time zone ...",
                        "default": null
                },
                "end_date_and_time": {
                        "type": "string",
                        "description": "The final date and time that will be used for calculating sun position. A time can be specified without a date, in which case the end date will be the same as the start date. If a date is provided, a ...",
                        "default": null
                },
                "iteration_interval": {
                        "type": "string",
                        "description": "The value that will be used to define the iteration of time from the start date.",
                        "default": null
                },
                "iteration_unit": {
                        "type": "string",
                        "description": "Specifies the unit that will define the iteration value applied to the start_date_and_time parameter value.DAYS\u2014The iteration value will represent days. This is the default.HOURS\u2014The iteration value w...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "start_date_and_time",
                "out_feature_class"
        ]
},
    "viewshed": {
        "name": "viewshed",
        "description": "Determines the raster surface locations visible to a set of observer features. The Geodesic Viewshed tool provides enhanced functionality or performance. Learn more about how Viewshed works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "in_observer_features": {
                        "type": "string",
                        "description": "The feature class that identifies the observer locations.The input can be point or polyline features."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster.The output will only record the number of times that each cell location in the input surface raster can be seen by the input observation points (or vertices for polylines). The obser..."
                },
                "z_factor": {
                        "type": "string",
                        "description": "The number of ground x,y units in one surface z-unit.The z-factor adjusts the units of measure for the z-units when they are different from the x,y units of the input surface. The z-values of the inpu...",
                        "default": null
                },
                "curvature_correction": {
                        "type": "string",
                        "description": "Specifies whether correction for the earth's curvature will be applied.FLAT_EARTH\u2014No curvature correction will be applied. This is the default.CURVED_EARTH\u2014Curvature correction will be applied.",
                        "default": null
                },
                "refractivity_coefficient": {
                        "type": "string",
                        "description": "The coefficient of the refraction of visible light in air.The default value is 0.13.",
                        "default": null
                },
                "out_agl_raster": {
                        "type": "string",
                        "description": "The output above ground level (AGL) raster.The AGL result is a raster where each cell value is the minimum height that must be added to an otherwise nonvisible cell to make it visible by at least one ...",
                        "default": null
                }
        },
        "required": [
                "in_raster",
                "in_observer_features",
                "out_raster"
        ]
},
    "visibility": {
        "name": "visibility",
        "description": "Determines the raster surface locations visible to a set of observer features, or identifies which observer points are visible from each raster surface location. The Geodesic Viewshed tool provides enhanced functionality or performance.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input surface raster."
                },
                "in_observer_features": {
                        "type": "string",
                        "description": "The feature class that identifies the observer locations.The input can be point or polyline features."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster.The output will either record the number of times that each cell location in the input surface raster can be seen by the input observation locations (the frequency analysis type), or..."
                },
                "out_agl_raster": {
                        "type": "string",
                        "description": "The output above-ground-level (AGL) raster.The AGL result is a raster where each cell value is the minimum height that must be added to an otherwise nonvisible cell to make it visible by at least one ...",
                        "default": null
                },
                "analysis_type": {
                        "type": "string",
                        "description": "The visibility analysis type.FREQUENCY\u2014The output records the number of times that each cell location in the input surface raster can be seen by the input observation locations (as points, or as verti...",
                        "default": null
                },
                "nonvisible_cell_value": {
                        "type": "string",
                        "description": "Value assigned to non-visible cells.ZERO\u20140 is assigned to nonvisible cells. This is the default.NODATA\u2014NoData is assigned to nonvisible cells.",
                        "default": null
                },
                "z_factor": {
                        "type": "string",
                        "description": "Number of ground x,y units in one surface z unit.The z-factor adjusts the units of measure for the z units when they are different from the x,y units of the input surface. The z-values of the input su...",
                        "default": null
                },
                "curvature_correction": {
                        "type": "string",
                        "description": "Specifies whether correction for the earth's curvature will be applied.FLAT_EARTH\u2014No curvature correction will be applied. This is the default.CURVED_EARTH\u2014Curvature correction will be applied.",
                        "default": null
                },
                "refractivity_coefficient": {
                        "type": "string",
                        "description": "The coefficient of the refraction of visible light in air.The default value is 0.13.",
                        "default": null
                },
                "surface_offset": {
                        "type": "string",
                        "description": "A vertical distance that will be added to the z-value of each cell as it is considered for visibility. It must be a positive integer or floating-point value.You can select a field in the input observe...",
                        "default": null
                },
                "observer_elevation": {
                        "type": "string",
                        "description": "The surface elevations of the observer points or vertices.You can select a field in the input observers dataset, or you can specify a numerical value.By default, a numerical field SPOT is used if it e...",
                        "default": null
                },
                "observer_offset": {
                        "type": "string",
                        "description": "A vertical distance that will be added to the observer elevation. It must be a positive integer or floating-point value.You can select a field in the input observers dataset, or you can specify a nume...",
                        "default": null
                },
                "inner_radius": {
                        "type": "string",
                        "description": "The start distance from which visibility will be determined. Cells closer than this distance will not be visible in the output but can still block visibility of the cells between inner radius and oute...",
                        "default": null
                },
                "outer_radius": {
                        "type": "string",
                        "description": "The maximum distance from which visibility will be determined. Cells beyond this distance will be excluded from the analysis.It can be a positive or negative integer or floating point value. If it is ...",
                        "default": null
                },
                "horizontal_start_angle": {
                        "type": "string",
                        "description": "The start angle of the horizontal scan range. Provide the value in degrees from 0 to 360 with 0 oriented to north. The value can be integer or floating point. The default value is 0.You can select a f...",
                        "default": null
                },
                "horizontal_end_angle": {
                        "type": "string",
                        "description": "The end angle of the horizontal scan range. Provide the value in degrees from 0 to 360 with 0 oriented to north. The value can be integer or floating point. The default value is 360.You can select a f...",
                        "default": null
                },
                "vertical_upper_angle": {
                        "type": "string",
                        "description": "The upper vertical angle limit of the scan relative to the horizontal plane. Provide the value in degrees from above -90 up to and including 90. The value can be integer or floating point. The default...",
                        "default": null
                },
                "vertical_lower_angle": {
                        "type": "string",
                        "description": "The lower vertical angle limit of the scan relative to the horizontal plane. Provide the value in degrees from -90 up to but not including 90. The value can be integer or floating point. The default v...",
                        "default": null
                }
        },
        "required": [
                "in_raster",
                "in_observer_features",
                "out_raster"
        ]
}
}
