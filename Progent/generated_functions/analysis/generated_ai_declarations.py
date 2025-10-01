# Generated ArcGIS Pro Analysis Tools AI Function Declarations
# Generated on 2025-10-01T11:38:01.348956
# Total tools: {len(ai_declarations)}

functions_declarations = {
    "select": {
        "name": "select",
        "description": "Extracts features from an input feature class or input feature layer, typically using a select or SQL expression, and stores them in an output feature class.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature class or layer from which features will be selected."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will be created. If no expression is used, the output will contain all the input features."
                },
                "where_clause": {
                        "type": "string",
                        "description": "The SQL expression that will be used to select a subset of features.  For more information about SQL syntax,  see SQL reference for query expressions used in ArcGIS.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "table_select": {
        "name": "table_select",
        "description": "Selects table records matching a Structured Query Language (SQL) expression and writes them to an output table.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table containing records matching the specified expression that will be written to the output table."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table containing records from the input table that match the specified expression."
                },
                "where_clause": {
                        "type": "string",
                        "description": "An SQL expression used to select a subset of records.  For more information on SQL syntax, see SQL reference for elements used in query expressions.",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "out_table"
        ]
},
    "split_by_attributes": {
        "name": "split_by_attributes",
        "description": "Splits an input dataset by unique attributes.",
        "parameters": {
                "input_table": {
                        "type": "string",
                        "description": "The input feature class or table containing the data that will be split into the target workspace."
                },
                "target_workspace": {
                        "type": "string",
                        "description": "The existing workspace where the output feature classes or tables will be written."
                },
                "split_fields": {
                        "type": "string",
                        "description": "The fields on which the input will be split into new feature classes or tables."
                }
        },
        "required": [
                "input_table",
                "target_workspace",
                "split_fields"
        ]
},
    "clip": {
        "name": "clip",
        "description": "Extracts input features that overlay the clip features. Use this tool to cut out a piece of one dataset using one or more of the features in another dataset as a cookie cutter. This is particularly useful for creating a new dataset\u2014also referred to as a study area or area of interest (AOI)\u2014that contains a geographic subset of the features in another, larger dataset. Clip operations can also be performed using the Pairwise Clip tool.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The features that will be clipped."
                },
                "clip_features": {
                        "type": "string",
                        "description": "The features that will be used to clip the input features."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The dataset that will be created."
                },
                "cluster_tolerance": {
                        "type": "string",
                        "description": "The minimum distance separating all feature coordinates as well as the distance a coordinate can move in x or y (or both). Set the value higher for data with less coordinate accuracy and lower for dat...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "clip_features",
                "out_feature_class"
        ]
},
    "split": {
        "name": "split",
        "description": "Splits an input with overlaying features to  create a subset of output feature classes.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The features to be split."
                },
                "split_features": {
                        "type": "string",
                        "description": "Polygon features containing a tabular field whose unique values are used to split the input features and provide the output feature classes' names."
                },
                "split_field": {
                        "type": "string",
                        "description": "The character field used to split the input features. This field's values identify the split features used to create each output feature class. The split field's unique values provide the names of the..."
                },
                "out_workspace": {
                        "type": "string",
                        "description": "The existing workspace where the output feature classes are stored."
                },
                "cluster_tolerance": {
                        "type": "string",
                        "description": "The minimum distance separating all feature coordinates (nodes and vertices) as well as the distance a coordinate can move in x or y (or both). Set the value higher for data that has less coordinate a...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "split_features",
                "split_field",
                "out_workspace"
        ]
},
    "select": {
        "name": "select",
        "description": "Extracts features from an input feature class or input feature layer, typically using a select or SQL expression, and stores them in an output feature class.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature class or layer from which features will be selected."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will be created. If no expression is used, the output will contain all the input features."
                },
                "where_clause": {
                        "type": "string",
                        "description": "The SQL expression that will be used to select a subset of features.  For more information about SQL syntax,  see SQL reference for query expressions used in ArcGIS.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "assign_weights_by_pairwise_comparison": {
        "name": "assign_weights_by_pairwise_comparison",
        "description": "Calculates the relative weights for a set of input variables by comparing them in pairs. Learn more about how Assign Weights By Pairwise Comparison works",
        "parameters": {
                "input_variables": {
                        "type": "string",
                        "description": "The variable names that will be compared. Any name can be provided.The minimum number of variables is two and the maximum is nine."
                },
                "out_table": {
                        "type": "string",
                        "description": "The name of the output table that will contain calculated weights for the input variables. When the add_comparison_matrix parameter value is ADD_MATRIX, the output table will also include the pairwise..."
                },
                "add_comparison_matrix": {
                        "type": "string",
                        "description": "Specifies whether the out_table parameter value will contain the pairwise comparison matrix.ADD_MATRIX\u2014The output table will contain both the pairwise comparison matrix and the calculated weights. Thi...",
                        "default": None
                },
                "comparison_matrix": {
                        "type": "string",
                        "description": "The pairwise comparison matrix that will be used when calculating the weights.\r\nDefine the pairwise comparisons by doing one of the following:Provide a file containing a valid comparison matrix.Specif...",
                        "default": None
                }
        },
        "required": [
                "input_variables",
                "out_table"
        ]
},
    "select": {
        "name": "select",
        "description": "Extracts features from an input feature class or input feature layer, typically using a select or SQL expression, and stores them in an output feature class.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature class or layer from which features will be selected."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will be created. If no expression is used, the output will contain all the input features."
                },
                "where_clause": {
                        "type": "string",
                        "description": "The SQL expression that will be used to select a subset of features.  For more information about SQL syntax,  see SQL reference for query expressions used in ArcGIS.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "symmetrical_difference": {
        "name": "symmetrical_difference",
        "description": "Computes a geometric intersection of the input and update features, returning the input features and update features that do not overlap. Features or portions of features in the input and update features that do not overlap will be written to the output feature class.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature class or layer."
                },
                "update_features": {
                        "type": "string",
                        "description": "The update feature class or layer. The geometry type must be the same as that of the input feature class or layer."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class to which the results will be written."
                },
                "join_attributes": {
                        "type": "string",
                        "description": "Specifies the attributes that will be transferred to the output feature class.ALL\u2014All the attributes from the input features will be transferred to the output feature class. This is the default. NO_FI...",
                        "default": None
                },
                "cluster_tolerance": {
                        "type": "string",
                        "description": "The minimum distance separating all feature coordinates (nodes and vertices) as well as the distance a coordinate can move in x or y (or both).Caution:  Changing this parameter's value may cause failu...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "update_features",
                "out_feature_class"
        ]
},
    "erase": {
        "name": "erase",
        "description": "Creates a feature class by overlaying the input features with the erase features. Only those portions of the input features falling outside the erase features  are copied to the output feature class. An alternate tool is available for erase operations. See the Pairwise Erase tool documentation for details.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature class or layer."
                },
                "erase_features": {
                        "type": "string",
                        "description": "The features that will be used to erase coincident features in the input."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class that will contain only those input features that are not coincident with the erase features."
                },
                "cluster_tolerance": {
                        "type": "string",
                        "description": "The minimum distance separating all feature coordinates (nodes and vertices) as well as the distance a coordinate can move in x or y (or both). Caution:  Changing this parameter's value may cause fail...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "erase_features",
                "out_feature_class"
        ]
},
    "update": {
        "name": "update",
        "description": "Computes the geometric intersection of the input features and update features. The attributes and geometry of the input features are updated by the update features in the output feature class.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature class or layer. The geometry type must be polygon."
                },
                "update_features": {
                        "type": "string",
                        "description": "The features that will be used to update the input features. The geometry type must be polygon."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class that will contain the results."
                },
                "keep_borders": {
                        "type": "string",
                        "description": "Specifies whether the boundary of the update polygon features will be kept.BORDERS\u2014The outside border of the update_features parameter value will be kept in the out_feature_class parameter value. This...",
                        "default": None
                },
                "cluster_tolerance": {
                        "type": "string",
                        "description": "The minimum distance separating all feature coordinates (nodes and vertices) as well as the distance a coordinate can move in x or y (or both). Caution:  Changing this parameter's value may cause fail...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "update_features",
                "out_feature_class"
        ]
},
    "intersect": {
        "name": "intersect",
        "description": "Computes a geometric intersection of the input features. Features or portions of features that overlap in all layers or feature classes will be written to the output feature class. An alternate tool is available for intersect operations. See the Pairwise Intersect tool documentation for details. The Pairwise Intersect tool is similar to this tool  in that geometric intersections are computed, but it is different in that intersections are computed on pairs of features rather than all combinations of features. Learn more about how Intersect works",
        "parameters": {
                "in_featuresin_features_rank": {
                        "type": "string",
                        "description": "A list of the input feature classes or layers. When the distance between features is less than the cluster tolerance, the features with the lower rank will snap to the feature with the higher rank. Th..."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class."
                },
                "join_attributes": {
                        "type": "string",
                        "description": "Specifies the attributes from the input features that will be transferred to the output feature class.ALL\u2014All the attributes from the input features will be transferred to the output feature class. Th...",
                        "default": None
                },
                "cluster_tolerance": {
                        "type": "string",
                        "description": "The minimum distance separating all feature coordinates (nodes and vertices) as well as the distance a coordinate can move in x or y (or both).Caution:  Changing this parameter's value may cause failu...",
                        "default": None
                },
                "output_type": {
                        "type": "string",
                        "description": "Specifies the type of intersections that will be returned.INPUT\u2014The intersections returned will be the same geometry type as the input features with the lowest dimension geometry. If all inputs are po...",
                        "default": None
                }
        },
        "required": [
                "in_featuresin_features_rank",
                "out_feature_class"
        ]
},
    "apportion_polygon": {
        "name": "apportion_polygon",
        "description": "Summarizes the attributes of an input polygon layer based on the spatial overlay of a target polygon layer and assigns the summarized attributes to the target polygons. The target polygons have summed numeric attributes derived from the input polygons that each target overlaps. This process is typically known as apportioning or apportionment. This tool can be used to estimate the population of one\r\nfeature based on the percentage of that feature that overlays another feature\r\nwith a known population. The Enrich Layer tool uses detailed aggregation and apportionment settings to summarize data.  The Apportion Polygon tool is similar to the Enrich Layer tool. However, Apportion Polygon uses specified apportionment, while Enrich Layer uses U.S. Census Block points or global settlement points for apportionment. For more information, see Data apportionment.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The polygon features with numeric attributes that will be                                                                                                                                               ..."
                },
                "apportion_fieldsfield_statistic_type": {
                        "type": "string",
                        "description": "The numeric fields from the input polygons that will be summarized by each target polygon and recorded in the output feature class.The optional statistic types are as follows:SUM\u2014The values for the sp..."
                },
                "target_features": {
                        "type": "string",
                        "description": "The polygon \r\nfeatures and their apportioned fields that will be copied to the output feature class."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output feature class containing the attribute and geometries of the target polygons as well as the specified apportion fields from the input polygons."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to apportion the fields from the input polygons to the target polygons.\r\nAREA\u2014The amount that each input polygon contributes to the summarized values for each ta..."
                },
                "estimation_features": {
                        "type": "string",
                        "description": "The input point or polyline features that will be used to estimate the percent of the input polygon apportion fields to apportion to the target polygon.  This is the amount of the point or line within...",
                        "default": None
                },
                "weight_field": {
                        "type": "string",
                        "description": "A numeric field from the target polygon layer that  will be used to adjust which target polygons receive larger apportioned values from the input polygons' fields to apportion. Targets with higher wei...",
                        "default": None
                },
                "maintain_geometries": {
                        "type": "string",
                        "description": "Specifies whether the output feature class will maintain the original geometries of the target polygon layer. MAINTAIN_GEOMETRIES\u2014The output feature class will maintain the original geometries of the ...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "apportion_fieldsfield_statistic_type",
                "target_features",
                "out_features",
                "method"
        ]
},
    "count_overlapping_features": {
        "name": "count_overlapping_features",
        "description": "Generates planarized overlapping features from the input features. The count of overlapping features is written to the output features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature classes or layers. The input features can be point, multipoint, line, or polygon. If multiple inputs are provided, they must all be the same geometry type."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing the overlap count."
                },
                "min_overlap_count": {
                        "type": "string",
                        "description": "Limits the output to only locations that meet or exceed the specified number of overlaps. The default value is 1.",
                        "default": None
                },
                "out_overlap_table": {
                        "type": "string",
                        "description": "The output table containing records for each individual overlapping geometry.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "identity": {
        "name": "identity",
        "description": "Computes a geometric intersection of the input features and identity features. The input features or portions thereof that overlap identity features will get the attributes of those identity features.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature class or layer."
                },
                "identity_features": {
                        "type": "string",
                        "description": "The identity feature class or layer. It must be polygon or the same geometry type as the input features."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class that will be created and to which the results will be written."
                },
                "join_attributes": {
                        "type": "string",
                        "description": "Specifies how attributes will be transferred to the output feature class.ALL\u2014All the attributes (including FIDs) from the input features, as well as the identity features, will be transferred to the o...",
                        "default": None
                },
                "cluster_tolerance": {
                        "type": "string",
                        "description": "The minimum distance separating all feature coordinates (nodes and vertices) as well as the distance a coordinate can move in x or y (or both). Caution:  Changing this parameter's value may cause fail...",
                        "default": None
                },
                "relationship": {
                        "type": "string",
                        "description": "Specifies whether additional spatial relationships between the in_features and identity_features parameter values will be written to the output. This only applies when the geometry type of the in_feat...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "identity_features",
                "out_feature_class"
        ]
},
    "spatial_join": {
        "name": "spatial_join",
        "description": "Joins attributes from one feature to another based on the spatial relationship. The target features and the joined attributes from the join features are written to the output feature class. Learn more about Spatial Join relationships by feature type",
        "parameters": {
                "target_features": {
                        "type": "string",
                        "description": "The attributes from the target features and the attributes from the joined features will be transferred to the output feature class. However, a subset of attributes can be defined by the field map par..."
                },
                "join_features": {
                        "type": "string",
                        "description": "The attributes from the join features will be joined to the attributes of the target features. See the explanation of the join_operation parameter for details on how the aggregation of joined attribut..."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "A new feature class containing the attributes of the target and join features. By default, all attributes of the target features and the attributes of the joined features will be written to the output..."
                },
                "join_operation": {
                        "type": "string",
                        "description": "The operation that will join the target features and join features in the output feature class if multiple join features are found that have the same spatial relationship with a single target feature....",
                        "default": None
                },
                "join_type": {
                        "type": "string",
                        "description": "Specifies whether all target features will be maintained in the output feature class (an outer join) or only those that have the specified spatial relationship with the join features (an inner join).K...",
                        "default": None
                },
                "field_mapping": {
                        "type": "string",
                        "description": "The fields that will\r\nbe included in the output feature class with their respective properties and\r\nsource fields. The output includes all fields from the join and\r\ntarget features by default. Use the...",
                        "default": None
                },
                "match_option": {
                        "type": "string",
                        "description": "Specifies the criteria that will be used to match rows.INTERSECT\u2014The features in the join features will be matched if they intersect a target  feature. This is the default. Specify the distance in the...",
                        "default": None
                },
                "search_radius": {
                        "type": "string",
                        "description": "Join features within this distance of a target feature will be considered for the spatial join. A search radius is only valid when the spatial relationship is specified (the match_option parameter is ...",
                        "default": None
                },
                "distance_field_name": {
                        "type": "string",
                        "description": "The name of the field that contains the distance between the target feature and the closest join feature. This field will be added to the output feature class. This parameter is only valid when the sp...",
                        "default": None
                },
                "match_fieldsjoin_field_target_field": {
                        "type": "string",
                        "description": "Pairs of fields from the join features and target features that will be used for attribute matching. Only the records from the join features that share match field values with the target features will...",
                        "default": None
                }
        },
        "required": [
                "target_features",
                "join_features",
                "out_feature_class"
        ]
},
    "union": {
        "name": "union",
        "description": "Computes a geometric union of the input features. All features and their attributes will be written to the output feature class. Learn more about how Union works",
        "parameters": {
                "in_featuresin_features_rank": {
                        "type": "string",
                        "description": "The input feature classes or layers. When the distance between features is less than the cluster tolerance, the features with the lower rank will snap to the feature with the higher rank. The highest ..."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class that will contain the results."
                },
                "join_attributes": {
                        "type": "string",
                        "description": "Specifies which attributes from the input features will be transferred to the output feature class.ALL\u2014All the attributes from the input features will be transferred to the output feature class. This ...",
                        "default": None
                },
                "cluster_tolerance": {
                        "type": "string",
                        "description": "The minimum distance separating all feature coordinates (nodes and vertices) as well as the distance a coordinate can move in x or y (or both). Caution:  Changing this parameter's value may cause fail...",
                        "default": None
                },
                "gaps": {
                        "type": "string",
                        "description": "Specifies whether a feature will be created for areas in the output that are completely enclosed by polygons.Gaps are areas in the output feature class that are completely enclosed by other polygons (...",
                        "default": None
                }
        },
        "required": [
                "in_featuresin_features_rank",
                "out_feature_class"
        ]
},
    "select": {
        "name": "select",
        "description": "Extracts features from an input feature class or input feature layer, typically using a select or SQL expression, and stores them in an output feature class.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature class or layer from which features will be selected."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will be created. If no expression is used, the output will contain all the input features."
                },
                "where_clause": {
                        "type": "string",
                        "description": "The SQL expression that will be used to select a subset of features.  For more information about SQL syntax,  see SQL reference for query expressions used in ArcGIS.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "pairwise_dissolve": {
        "name": "pairwise_dissolve",
        "description": "Aggregates features based on specified attributes using a parallel processing approach. An alternate tool is available for dissolve operations. See the Dissolve tool documentation for details.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The features to be aggregated."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class to be created that will contain the aggregated features."
                },
                "dissolve_field": {
                        "type": "string",
                        "description": "The field or fields on which features will be aggregated.",
                        "default": None
                },
                "statistics_fieldsfield_statistic_type": {
                        "type": "string",
                        "description": "Specifies the field or fields containing the attribute values that will be used to calculate the specified statistic. Multiple statistic and field combinations can be specified. Null values are exclud...",
                        "default": None
                },
                "multi_part": {
                        "type": "string",
                        "description": "Specifies whether multipart features will be included in the output.MULTI_PART\u2014Multipart features will be included in the output. This is the default.SINGLE_PART\u2014Multipart features will not be include...",
                        "default": None
                },
                "concatenation_separator": {
                        "type": "string",
                        "description": "A character or characters that will be used to concatenate values when the CONCATENATION option is used for the statistics_fields parameter. By default, the tool will concatenate values without a sepa...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "pairwise_integrate": {
        "name": "pairwise_integrate",
        "description": "Analyzes the coordinate locations of feature vertices among features in one or more feature classes. Those that fall within a specified distance of one another are assumed to represent the same location and are assigned a common coordinate value (in other words, they are colocated). The tool also adds vertices where feature vertices are within the x,y tolerance of an edge and where line segments intersect. Pairwise Integrate performs\r\nthe following processing tasks: Vertices within the x,y tolerance of one another will be assigned the same coordinate location.When a vertex of one feature is within the x,y tolerance of an edge of any other feature, a new vertex will be inserted on the edge.When line segments intersect, a vertex will be inserted at the point of intersection for each feature involved in the intersection. An alternate tool is available for vector data integration. See the Integrate tool documentation for details.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The feature classes that will be integrated. When the distance between features is small in comparison to the tolerance, the vertices or points will be clustered (moved to be coincident)."
                },
                "cluster_tolerance": {
                        "type": "string",
                        "description": "The distance that determines the range in which feature vertices are made coincident. To minimize undesired movement of vertices, the x,y tolerance should be small. If no value is provided, the x,y to...",
                        "default": None
                }
        },
        "required": [
                "in_features"
        ]
},
    "clip": {
        "name": "clip",
        "description": "Extracts input features that overlay the clip features. Use this tool to cut out a piece of one dataset using one or more of the features in another dataset as a cookie cutter. This is particularly useful for creating a new dataset\u2014also referred to as a study area or area of interest (AOI)\u2014that contains a geographic subset of the features in another, larger dataset. Clip operations can also be performed using the Pairwise Clip tool.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The features that will be clipped."
                },
                "clip_features": {
                        "type": "string",
                        "description": "The features that will be used to clip the input features."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The dataset that will be created."
                },
                "cluster_tolerance": {
                        "type": "string",
                        "description": "The minimum distance separating all feature coordinates as well as the distance a coordinate can move in x or y (or both). Set the value higher for data with less coordinate accuracy and lower for dat...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "clip_features",
                "out_feature_class"
        ]
},
    "pairwise_buffer": {
        "name": "pairwise_buffer",
        "description": "Creates buffer polygons around input features to a specified distance using a parallel processing approach. Alternate tools are available for buffer operations. See the Buffer and Graphic Buffer tool documentation for details.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point, line, or polygon features that will be buffered."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class containing the output buffers."
                },
                "buffer_distance_or_field": {
                        "type": "string",
                        "description": "The distance around the input features that will be buffered. Distances can be provided as either a value representing a linear distance or a field from the input features that contains the distance t..."
                },
                "dissolve_option": {
                        "type": "string",
                        "description": "Specifies the type of dissolve operation that will be performed to remove buffer overlap.NONE\u2014An individual buffer for each feature will be maintained, regardless of overlap. This is the default. ALL\u2014...",
                        "default": None
                },
                "dissolve_field": {
                        "type": "string",
                        "description": "The list of fields from the input features on which the output buffers will be dissolved. Any buffers sharing attribute values in the listed fields (carried over from the input features) will be disso...",
                        "default": None
                },
                "method": {
                        "type": "string",
                        "description": "Specifies whether the planar or geodesic method will be used to create the buffers.PLANAR\u2014If the input features are in a projected coordinate system, Euclidean buffers will be created. If the input fe...",
                        "default": None
                },
                "max_deviation": {
                        "type": "string",
                        "description": "The maximum distance the output buffer boundary will deviate from the true buffer boundary. While the true boundary of the buffer is a curve, the output boundary will be densified. Use this parameter ...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "buffer_distance_or_field"
        ]
},
    "pairwise_clip": {
        "name": "pairwise_clip",
        "description": "Extracts input features that overlay the clip features. Use this tool to cut out a piece of one feature class using one or more of the features in another feature class. This is particularly useful for creating a new feature class\u2014also referred to as a study area or area of interest (AOI)\u2014that contains a geographic subset of the features in another, larger feature class. Clip operations can also be performed with  the Clip tool.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The features that will be clipped."
                },
                "clip_features": {
                        "type": "string",
                        "description": "The features that will be used to clip the input features."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class that will be created."
                },
                "cluster_tolerance": {
                        "type": "string",
                        "description": "The minimum distance separating all feature coordinates (nodes and vertices) as well as the distance a coordinate can move in x or y (or both). Caution:  Changing this parameter's value may cause fail...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "clip_features",
                "out_feature_class"
        ]
},
    "select": {
        "name": "select",
        "description": "Extracts features from an input feature class or input feature layer, typically using a select or SQL expression, and stores them in an output feature class.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature class or layer from which features will be selected."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will be created. If no expression is used, the output will contain all the input features."
                },
                "where_clause": {
                        "type": "string",
                        "description": "The SQL expression that will be used to select a subset of features.  For more information about SQL syntax,  see SQL reference for query expressions used in ArcGIS.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "buffer": {
        "name": "buffer",
        "description": "Creates buffer polygons around input features to a specified distance. Alternate tools are available for buffer operations. See the Pairwise Buffer and Graphic Buffer  tool documentation for details. Learn more about how Buffer works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point, line, or polygon features that will be buffered."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class containing the output buffers."
                },
                "buffer_distance_or_field": {
                        "type": "string",
                        "description": "The distance around the input features that will be buffered. Distances can be provided as either a value representing a linear distance or a field from the input features that contains the distance t..."
                },
                "line_side": {
                        "type": "string",
                        "description": "Specifies the sides of the input features that will be buffered. This parameter is only supported for polygon and line features.FULL\u2014For lines, buffers will be generated on both sides of the line. For...",
                        "default": None
                },
                "line_end_type": {
                        "type": "string",
                        "description": "Specifies the shape of the buffer at the end of line input features. This parameter is not valid for polygon input features.ROUND\u2014The ends of the buffer will be round, in the shape of a half circle. T...",
                        "default": None
                },
                "dissolve_option": {
                        "type": "string",
                        "description": "Specifies the type of dissolve that will be performed to remove buffer overlap.NONE\u2014An individual buffer for each feature will be maintained, regardless of overlap. This is the default. ALL\u2014All buffer...",
                        "default": None
                },
                "dissolve_field": {
                        "type": "string",
                        "description": "The list of fields from the input features on which the output buffers will be dissolved. Any buffers sharing attribute values in the listed fields (carried over from the input features) will be disso...",
                        "default": None
                },
                "method": {
                        "type": "string",
                        "description": "Specifies whether the planar or geodesic method will be used to create the buffers.PLANAR\u2014If the input features are in a projected coordinate system, Euclidean buffers will be created. If the input fe...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "buffer_distance_or_field"
        ]
},
    "near": {
        "name": "near",
        "description": "Calculates distance and additional proximity information between the input features and the closest feature in another layer or feature class. Learn more about how proximity is calculated by geoprocessing tools",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features, which can be point, polyline, polygon, or multipoint type."
                },
                "near_features": {
                        "type": "string",
                        "description": "One or more feature layers or feature classes containing near feature candidates. The near features can be point, polyline, polygon, or multipoint. If multiple layers or feature classes are specified,..."
                },
                "search_radius": {
                        "type": "string",
                        "description": "The radius that will be used to search for near features. If no value is specified, all near features will be considered. If a distance but no unit or unknown is specified, the units of the coordinate...",
                        "default": None
                },
                "location": {
                        "type": "string",
                        "description": "Specifies whether x- and y-coordinates of the closest location of the near feature will be written to the NEAR_X and NEAR_Y fields.NO_LOCATION\u2014 Location information will not be written. This is the de...",
                        "default": None
                },
                "angle": {
                        "type": "string",
                        "description": "Specifies whether the near angle will be calculated and written to the NEAR_ANGLE field in the output table. A near angle measures direction of the line connecting an input feature to its nearest feat...",
                        "default": None
                },
                "method": {
                        "type": "string",
                        "description": "Specifies whether a shortest path on a spheroid (geodesic) or a flat earth (planar) distance method will be used. It is recommended that you use the GEODESIC method for data stored in a coordinate sys...",
                        "default": None
                },
                "field_namesproperty_fieldname": {
                        "type": "string",
                        "description": "The names of the attribute fields that will be added during processing.If this parameter is not used or any fields that will be added are excluded from this parameter, the default field names will be ...",
                        "default": None
                },
                "distance_unit": {
                        "type": "string",
                        "description": "Specifies the unit of measurement for the NEAR_DIST field. When no unit of measurement is specified, the values in the NEAR_DIST field will be in the linear unit of the input feature's coordinate syst...",
                        "default": None
                },
                "match_fieldsinput_field_near_field": {
                        "type": "string",
                        "description": "The pairs of fields from the input features and near features that will be used for attribute matching. Only the near features that share match field values with the input features will be used in the...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "near_features"
        ]
},
    "create_thiessen_polygons": {
        "name": "create_thiessen_polygons",
        "description": "Creates Thiessen polygons from point features. Each Thiessen polygon contains only a single point input feature. Any location within a Thiessen polygon is closer to its associated point than to any other point input feature.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The point input features from which Thiessen polygons will be generated."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing the Thiessen polygons that are generated from the point input features."
                },
                "fields_to_copy": {
                        "type": "string",
                        "description": "Specifies which fields from the input features will be transferred to the output feature class.ONLY_FID\u2014Only the FID field from the input features will be transferred to the output feature class. This...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "generate_origin_destination_links": {
        "name": "generate_origin_destination_links",
        "description": "Generates connecting lines from origin features to destination features. This is often referred to as a spider diagram.",
        "parameters": {
                "origin_features": {
                        "type": "string",
                        "description": "The input features from which links will be generated."
                },
                "destination_features": {
                        "type": "string",
                        "description": "The destination features to which links will be generated."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output polyline feature class that will contain the output links."
                },
                "origin_group_field": {
                        "type": "string",
                        "description": "The attribute field from the input origin features that will be used for grouping. Features that have the same group field value between origins and destinations will be connected with a link.",
                        "default": None
                },
                "destination_group_field": {
                        "type": "string",
                        "description": "The attribute field from the input destination features that will be used for grouping. Features that have the same group field value between origins and destinations will be connected with a link.",
                        "default": None
                },
                "line_type": {
                        "type": "string",
                        "description": "Specifies whether a shortest path on a spheroid (geodesic) or a  Cartesian projected earth (planar) will be used when generating the output links. Geodesic lines will have a slight curve when their le...",
                        "default": None
                },
                "num_nearest": {
                        "type": "string",
                        "description": "The maximum number of links that will be generated per origin feature to the nearest destination features. If no number is specified, the tool will generate links between all origin and destination fe...",
                        "default": None
                },
                "search_distance": {
                        "type": "string",
                        "description": "The maximum distance between an origin and destination feature that will produce a link feature  in the output. The unit of the search distance is specified in the distance unit parameter. If no searc...",
                        "default": None
                },
                "distance_unit": {
                        "type": "string",
                        "description": "Specifies the units used to measure the length of the links. Distances for each link will appear in the LINK_DIST field. If a distance unit  is not specified, the distance unit of the origin features'..."
                },
                "aggregate_links": {
                        "type": "string",
                        "description": "Specifies whether overlapping links will be aggregated.AGGREGATE_OVERLAPPING\u2014Overlapping links will be aggregated if the starting point coordinates are the same.NO_AGGREGATE\u2014Overlapping links will not...",
                        "default": None
                },
                "sum_fields": {
                        "type": "string",
                        "description": "Specifies the field or fields containing the attribute values that will be used to calculate the specified statistic. Multiple statistic and field combinations can be specified. Null values are exclud...",
                        "default": None
                }
        },
        "required": [
                "origin_features",
                "destination_features",
                "out_feature_class",
                "distance_unit"
        ]
},
    "polygon_neighbors": {
        "name": "polygon_neighbors",
        "description": "Creates a table with statistics based on polygon contiguity (overlaps, coincident edges, or nodes). Learn more about how Polygon Neighbors works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input polygon features."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table."
                },
                "in_fields": {
                        "type": "string",
                        "description": "The input attribute field or fields that will be used to identify unique polygons or polygon groups and represent them in the output.",
                        "default": None
                },
                "area_overlap": {
                        "type": "string",
                        "description": "Specifies whether overlapping relationships will  be analyzed and included in the output.  \r\nNO_AREA_OVERLAP\u2014Overlapping relationships will not be analyzed or included in the output. This is the defau...",
                        "default": None
                },
                "both_sides": {
                        "type": "string",
                        "description": "Specifies whether both sides of neighbor relationships will be included in the output.BOTH_SIDES\u2014 For a pair of neighboring polygons, both neighboring information of one polygon being the source and t...",
                        "default": None
                },
                "cluster_tolerance": {
                        "type": "string",
                        "description": "The minimum distance between coordinates before they will be considered equal. By default, this is the x,y tolerance of the input  features.Caution:  Changing this parameter's value may cause failure ...",
                        "default": None
                },
                "out_linear_units": {
                        "type": "string",
                        "description": "Specifies the units that will be used to report the total  length of the coincident edge between neighboring polygons. The default is the input feature units.UNKNOWN\u2014The length unit will be unknown.KI...",
                        "default": None
                },
                "out_area_units": {
                        "type": "string",
                        "description": "Specifies the units that will be used to report the area overlap of neighboring polygons.  The default is the input feature units. \r\nThis parameter is only enabled when the area_overlap parameter is s...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_table"
        ]
},
    "multiple_ring_buffer": {
        "name": "multiple_ring_buffer",
        "description": "Creates multiple buffers at specified distances around the input features. These buffers can be merged and dissolved using the buffer distance values to create nonoverlapping buffers.",
        "parameters": {
                "input_features": {
                        "type": "string",
                        "description": "The input point, line, or polygon features to be buffered."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will contain multiple buffers."
                },
                "distancesdistance": {
                        "type": "string",
                        "description": "The list of buffer distances."
                },
                "buffer_unit": {
                        "type": "string",
                        "description": "Specifies the linear unit that will be used with the distance values.Default\u2014The linear unit of the input features' spatial reference will be used. If the Output Coordinate System geoprocessing enviro...",
                        "default": None
                },
                "dissolve_option": {
                        "type": "string",
                        "description": "Specifies whether buffers will be dissolved to resemble rings around the input features.ALL\u2014Buffers will be dissolved to resemble rings around the input features that do not overlap (think of these as...",
                        "default": None
                },
                "outside_polygons_only": {
                        "type": "string",
                        "description": "Specifies whether the buffers will cover the input features. This parameter is valid only for polygon input features.FULL\u2014Buffers will overlap or cover the input features. This is the default.OUTSIDE_...",
                        "default": None
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the method used to create the buffer.\r\nPLANAR\u2014Buffers will be created using a Euclidean buffer method. This is the default when the input has a projected coordinate system.GEODESIC\u2014Buffers w...",
                        "default": None
                }
        },
        "required": [
                "input_features",
                "output_feature_class",
                "distancesdistance"
        ]
},
    "graphic_buffer": {
        "name": "graphic_buffer",
        "description": "Creates buffer polygons around input features to a specified distance. A number of cartographic shapes are available for buffer ends (caps) and corners (joins) when the buffer is generated around the feature. Learn more about how Graphic Buffer works Alternate tools are available for buffer operations. See the Pairwise Buffer and Buffer  tool documentation for details.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point, line, or polygon features that will be buffered."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class containing the output buffers."
                },
                "buffer_distance_or_field": {
                        "type": "string",
                        "description": "The distance around the input features that will be buffered. Distances can be provided as either a value representing a linear distance or a field from the input features that contains the distance t..."
                },
                "line_caps": {
                        "type": "string",
                        "description": "Specifies the type of caps (ends) of the input features that will be buffered. This parameter is only supported for point and polygon features.SQUARE\u2014The output buffer will have a square cap around th...",
                        "default": None
                },
                "line_joins": {
                        "type": "string",
                        "description": "Specifies the shape of the buffer at corners where two segments join. This parameter is  only supported for line and polygon features.\r\nMITER\u2014The output buffer feature will be a square or sharp shape ...",
                        "default": None
                },
                "miter_limit": {
                        "type": "string",
                        "description": "Where line segments meet at a sharp angle and the line_joins parameter value has been specified as MITER, this parameter can be used to control how sharp corners in buffer output come to a point. In s...",
                        "default": None
                },
                "max_deviation": {
                        "type": "string",
                        "description": "The maximum distance the output buffer boundary will deviate from the true buffer boundary. While the true boundary of the buffer is a curve, the output boundary will be densified. Use this parameter ...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "buffer_distance_or_field"
        ]
},
    "generate_near_table": {
        "name": "generate_near_table",
        "description": "Calculates distances and other proximity information between features in one or more feature classes or layers. Unlike the Near tool, which modifies the input, Generate Near Table writes results to a new stand-alone table and supports finding more than one near feature. Learn more about how proximity is calculated by geoprocessing tools",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features, which can be point, polyline, polygon, or multipoint type."
                },
                "near_features": {
                        "type": "string",
                        "description": "One or more feature layers or feature classes containing near feature candidates. The near features can be point, polyline, polygon, or multipoint. If multiple layers or feature classes are specified,..."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table containing the result of the analysis."
                },
                "search_radius": {
                        "type": "string",
                        "description": "The radius that will be used to search for near features. If no value is specified, all near features will be considered. If a distance but no unit or unknown is specified, the units of the coordinate...",
                        "default": None
                },
                "location": {
                        "type": "string",
                        "description": "Specifies whether x- and y-coordinates of the input feature's location and closest location of the near feature will be written to the FROM_X, FROM_Y, NEAR_X, and NEAR_Y fields.NO_LOCATION\u2014 Locations ...",
                        "default": None
                },
                "angle": {
                        "type": "string",
                        "description": "Specifies whether the near angle will be calculated and written to the  NEAR_ANGLE field in the output table. A near angle measures direction of the line connecting an input feature to its nearest fea...",
                        "default": None
                },
                "closest": {
                        "type": "string",
                        "description": "Specifies whether only the closest near feature will be written to the output table.CLOSEST\u2014Only the closest near feature will be written to the output table. This is the default.ALL\u2014Multiple near fea...",
                        "default": None
                },
                "closest_count": {
                        "type": "string",
                        "description": "Limits the number of near features reported for each input feature. This parameter is ignored if the closest parameter  is set to CLOSEST.",
                        "default": None
                },
                "method": {
                        "type": "string",
                        "description": "Specifies whether a shortest path on a spheroid (geodesic) or a flat earth (planar) distance method will be used. It is recommended that you use the GEODESIC method for data stored in a coordinate sys...",
                        "default": None
                },
                "distance_unit": {
                        "type": "string",
                        "description": "Specifies the unit of measurement for the NEAR_DIST field. When no unit of measurement is specified, the values in the NEAR_DIST field will be in the linear unit of the input feature's coordinate syst...",
                        "default": None
                },
                "match_fieldsinput_field_near_field": {
                        "type": "string",
                        "description": "The pairs of fields from the input features and near features that will be used for attribute matching. Only the near features that share match field values with the input features will be used in the...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "near_features",
                "out_table"
        ]
},
    "select": {
        "name": "select",
        "description": "Extracts features from an input feature class or input feature layer, typically using a select or SQL expression, and stores them in an output feature class.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature class or layer from which features will be selected."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will be created. If no expression is used, the output will contain all the input features."
                },
                "where_clause": {
                        "type": "string",
                        "description": "The SQL expression that will be used to select a subset of features.  For more information about SQL syntax,  see SQL reference for query expressions used in ArcGIS.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "tabulate_intersection": {
        "name": "tabulate_intersection",
        "description": "Computes the intersection between two feature classes and cross tabulates the area, length, or count of the intersecting features.",
        "parameters": {
                "in_zone_features": {
                        "type": "string",
                        "description": "The features used to identify zones."
                },
                "zone_fields": {
                        "type": "string",
                        "description": "The attribute field or fields that will be used to define zones."
                },
                "in_class_features": {
                        "type": "string",
                        "description": "The features used to identify classes."
                },
                "out_table": {
                        "type": "string",
                        "description": "The table that will contain the cross tabulation of intersections between zones and classes."
                },
                "class_fields": {
                        "type": "string",
                        "description": "The attribute field or fields used to define classes.",
                        "default": None
                },
                "sum_fields": {
                        "type": "string",
                        "description": "The fields that will be summed from the in_class_features parameter.",
                        "default": None
                },
                "xy_tolerance": {
                        "type": "string",
                        "description": "The distance that determines the range in which features or their vertices are considered equal. By default, this is the x,y tolerance of the in_zone_features parameter value.\r\nCaution:  Changing this...",
                        "default": None
                },
                "out_units": {
                        "type": "string",
                        "description": "Specifies the units that will be used to calculate area or length measurements. Setting output units when the \r\ninput class features are points is not supported.UNKNOWN\u2014The units will be unknown.KILOM...",
                        "default": None
                }
        },
        "required": [
                "in_zone_features",
                "zone_fields",
                "in_class_features",
                "out_table"
        ]
},
    "summarize_within": {
        "name": "summarize_within",
        "description": "Overlays a polygon layer with another layer to summarize the number of points, length of the lines, or area of the polygons within each polygon, and calculate attribute field statistics about the features within the polygons. The following are example scenarios using Summarize Within:From a layer of watershed boundaries and a layer of land-use boundaries by land-use type, calculate total acreage of land-use type for each watershed.From a layer of parcels in a county and a layer of city boundaries, summarize the average value of vacant parcels within each city boundary.From a layer of counties and a layer of roads, summarize the total mileage of roads by road type in each county.",
        "parameters": {
                "in_polygons": {
                        "type": "string",
                        "description": "The polygons that will be used to summarize the features, or portions of features, in the input summary layer."
                },
                "in_sum_features": {
                        "type": "string",
                        "description": "The point, line, or polygon features that will be summarized for each polygon in the input polygons."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output polygon feature class containing the same geometries and attributes as the input polygons. The feature class will include additional attributes for the number of points, length of lines, an..."
                },
                "keep_all_polygons": {
                        "type": "string",
                        "description": "Specifies whether all input polygons or only those intersecting or containing at least one  input summary feature will be copied to the output feature class.KEEP_ALL\u2014All input polygons will be copied ...",
                        "default": None
                },
                "sum_fieldssummary_field_statistic_type": {
                        "type": "string",
                        "description": "A list of attribute  field names from the input summary features, as well as statistical summary types that will be calculated for those attribute fields for all points in each polygon. Summary fields...",
                        "default": None
                },
                "sum_shape": {
                        "type": "string",
                        "description": "Specifies whether attributes for the number of points, length of lines, and area of polygon features summarized in each input polygon will be added to the output feature class.ADD_SHAPE_SUM\u2014Shape summ...",
                        "default": None
                },
                "shape_unit": {
                        "type": "string",
                        "description": "Specifies the unit that will be used when calculating shape summary\r\nattributes. If the input summary features are points, no shape unit is necessary, since only the count of points in each input poly...",
                        "default": None
                },
                "group_field": {
                        "type": "string",
                        "description": "An attribute field from the input summary features that will be used for grouping. Features that have the same group field value will be combined and summarized with other features with the same group...",
                        "default": None
                },
                "add_min_maj": {
                        "type": "string",
                        "description": "Specifies whether minority and majority fields will be added to the output. This parameter allows you to determine which group field value is the minority (least dominant) and the majority (most domin...",
                        "default": None
                },
                "add_group_percent": {
                        "type": "string",
                        "description": "Specifies whether a percentage attribute field will be added to the output. This parameter allows you to determine the percentage of each attribute value in each group.This parameter is enabled if you...",
                        "default": None
                },
                "out_group_table": {
                        "type": "string",
                        "description": "An output table that includes summary fields for each group of summary features for each input polygon. The table will have the following attribute fields:Join_ID\u2014An ID corresponding to an ID field ad...",
                        "default": None
                }
        },
        "required": [
                "in_polygons",
                "in_sum_features",
                "out_feature_class"
        ]
},
    "summary_statistics": {
        "name": "summary_statistics",
        "description": "Calculates summary statistics for fields in a table.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input table containing the fields that will be used to calculate statistics."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table that will store the calculated statistics."
                },
                "statistics_fieldsfield_statistic_type": {
                        "type": "string",
                        "description": "Specifies the field or fields containing the attribute values that will be used to calculate the specified statistic. Multiple statistic and field combinations can be specified. Null values are exclud..."
                },
                "case_field": {
                        "type": "string",
                        "description": "The field or fields in the input that will be used to calculate statistics separately for each unique attribute value (or combination of attribute values when multiple fields are specified).",
                        "default": None
                },
                "concatenation_separator": {
                        "type": "string",
                        "description": "A character or characters that will be used to concatenate values when the CONCATENATION option is used for the statistics_fields parameter. By default, the tool will concatenate values without a sepa...",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "out_table",
                "statistics_fieldsfield_statistic_type"
        ]
},
    "enrich": {
        "name": "enrich",
        "description": "Enriches data by adding demographic and landscape facts about the people and places that surround or are inside data locations.  The output is a duplicate of your input with additional attribute fields.  This tool requires an ArcGIS Online organizational account or a locally installed Business Analyst dataset. The demographic and landscape information available with this tool can come from ArcGIS Online or locally installed Business Analyst data. The Enrich tool will consume credits if ArcGIS Online is set as the Business Analyst data source. The Enrich tool uses detailed aggregation and apportionment settings to summarize data. For more information, see Data apportionment.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The features to be enriched."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "A new layer containing both the input attributes and user-selected attributes. User-selected attributes are summarized from underlying demographic boundaries. Only the area inside the input boundary i..."
                },
                "variables": {
                        "type": "string",
                        "description": "The variables to be summarized and added to the output feature class."
                },
                "buffer_type": {
                        "type": "string",
                        "description": "Input point features must have an associated boundary polygon to enrich. When connected to ArcGIS Online, travel mode options are dynamically populated. Input line features can only use Straight Line ...",
                        "default": None
                },
                "distance": {
                        "type": "string",
                        "description": "Determines the distance or size of an area to enrich (for example, a 1-mile buffer or 5-minute walk time). Units correspond to the buffer type. The default value is 1.",
                        "default": None
                },
                "unit": {
                        "type": "string",
                        "description": "The units associated with the distance or time parameter.Miles\u2014MilesYards\u2014YardsFeet\u2014FeetKilometers\u2014KilometersMeters\u2014MetersHours\u2014HoursMinutes\u2014MinutesSeconds\u2014Seconds",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "variables"
        ]
},
    "summarize_nearby": {
        "name": "summarize_nearby",
        "description": "Finds features that are within a specified distance of features in the input layer and calculates statistics for the nearby features. Distance can be measured as a straight-line distance, a drive-time distance (for example, within 10 minutes), or a drive distance (for example, within 5 kilometers). For drive-time and drive-distance measurements, you  must be signed in to an  ArcGIS Online organizational account with Network Analysis privileges. Both measurement options consume credits. The following are example scenarios using Summarize Nearby:Calculate the total population within a 5minute drive time of a proposed new store location.Calculate the number of freeway access ramps within a 1-mile drive distance of a proposed new store location to use as a measure of store accessibility.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The point, line, or polygon features that will be buffered. Those buffers will be used to summarize the input summary features."
                },
                "in_sum_features": {
                        "type": "string",
                        "description": "The point, line, or polygon features that will be summarized."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output polygon feature class containing the buffered input features, attributes of the input features, and new attributes about the number points, length of lines, and area of polygons inside each..."
                },
                "distance_type": {
                        "type": "string",
                        "description": "Specifies the distance measurement type that will be used to generate buffer areas. Both driving distance and driving time will use the road network and honor restrictions such as one-way streets. Dri..."
                },
                "distancesdistance": {
                        "type": "string",
                        "description": "Distance values that will define a search distance (for straight-line, driving, trucking, or walking distance) or travel time (for driving, trucking, or walking time). Features that are within (or equ..."
                },
                "distance_units": {
                        "type": "string",
                        "description": "Specifies the unit that will be used for the distance values.\r\nMILES\u2014The units will be miles.KILOMETERS\u2014The units will be kilometers.FEET\u2014The units will be feet.YARDS\u2014The units will be yards.METERS\u2014Th...",
                        "default": None
                },
                "time_of_day": {
                        "type": "string",
                        "description": "The date or time when traffic conditions will be considered during travel time. Traffic conditions, especially in urbanized areas, can significantly impact the area covered within a specified travel t...",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "Specifies the time zone that will be used for the specified time of day. Time zones can be specified in local time or coordinated universal time (UTC).\r\n\r\nGEOLOCAL\u2014The time of day refers to the local ...",
                        "default": None
                },
                "keep_all_polygons": {
                        "type": "string",
                        "description": "Specifies whether all buffers of the input features or only those intersecting or containing at least one input summary feature will be copied to the output feature class.KEEP_ALL\u2014All buffers will be ...",
                        "default": None
                },
                "sum_fieldssummary_field_statistic_type": {
                        "type": "string",
                        "description": "A list of attribute  field names from the input summary features and statistical summary types that will be calculated for those attribute fields for all points within each input feature buffer. Summa...",
                        "default": None
                },
                "sum_shape": {
                        "type": "string",
                        "description": "Specifies whether attributes for the number of points, length of lines, and area of polygon features summarized in each input feature buffer (shape summary attributes) will be added to the output feat...",
                        "default": None
                },
                "shape_unit": {
                        "type": "string",
                        "description": "Specifies the unit that will be used when calculating shape summary\r\nattributes. If the input summary features are points, no shape unit is necessary, since only the count of points within each input ...",
                        "default": None
                },
                "group_field": {
                        "type": "string",
                        "description": "The attribute field from the input summary features that will be used for grouping. Features that have the same group field value will be combined and summarized with other features with the same grou...",
                        "default": None
                },
                "add_min_maj": {
                        "type": "string",
                        "description": "Specifies whether minority (least dominant) and majority (most dominant) group field values within each input feature buffer will be added to the output. This parameter is enabled if you specified a g...",
                        "default": None
                },
                "add_group_percent": {
                        "type": "string",
                        "description": "Specifies whether a percentage of each attribute value in each group will be added to the output. This parameter allows you to determine the percentage of each attribute value in each group. This para...",
                        "default": None
                },
                "output_grouped_table": {
                        "type": "string",
                        "description": "An output table that includes summary fields for each group of summary features for each input feature buffer. If a group field is specified, the output grouped table is required.The table will have t...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "in_sum_features",
                "out_feature_class",
                "distance_type",
                "distancesdistance"
        ]
},
    "frequency": {
        "name": "frequency",
        "description": "Reads a table and a set of fields and creates a new table containing unique field values and the number of occurrences of each unique field value.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table containing the field(s) that will be used to calculate frequency statistics."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table that will store the frequency statistics."
                },
                "frequency_fields": {
                        "type": "string",
                        "description": "The field(s) used to calculate frequency statistics. Each unique combination of field values will be included as a new row in the output table."
                },
                "summary_fields": {
                        "type": "string",
                        "description": "The attribute field(s) to sum and add to the output table. Values will be summed for each unique combination of frequency fields. Null values are excluded from this calculation.",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "out_table",
                "frequency_fields"
        ]
}
}
