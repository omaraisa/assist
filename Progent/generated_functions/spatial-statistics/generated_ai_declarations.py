# Generated ArcGIS Pro spatial-statistics AI Function Declarations
# Generated on 2025-10-01T15:21:07.919406
# Total tools: 69

functions_declarations = {
    "incremental_spatial_autocorrelation": {
        "name": "incremental_spatial_autocorrelation",
        "description": "Measures spatial autocorrelation for a series of distances and optionally creates a line graph of those distances and their corresponding z-scores.  Z-scores reflect the intensity of spatial clustering, and statistically significant peak z-scores indicate distances where spatial processes promoting clustering are most pronounced.  These peak distances are often appropriate values to use for tools with a Distance Band or Distance Radius parameter.",
        "parameters": {
                "input_features": {
                        "type": "string",
                        "description": "The feature class for which spatial autocorrelation will be measured over a series of distances."
                },
                "input_field": {
                        "type": "string",
                        "description": "The numeric field that will be used in assessing spatial autocorrelation."
                },
                "number_of_distance_bands": {
                        "type": "string",
                        "description": "The number of times the neighborhood size will be incremented and the dataset will be analyzed for spatial autocorrelation. The starting point and size of the increment are specified by the Beginning_..."
                },
                "beginning_distance": {
                        "type": "string",
                        "description": "The distance at which the analysis of spatial autocorrelation and the distance from which to increment will start. The value provided for this parameter should be in the units of the Output Coordinate...",
                        "default": None
                },
                "distance_increment": {
                        "type": "string",
                        "description": "The distance that will be increased after each iteration. The distance used in the analysis starts at the Beginning_Distance parameter value and increases by the amount specified in the Distance_Incre...",
                        "default": None
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies how distances will be calculated from each feature to neighboring features.            EUCLIDEAN\u2014The distances will be calculated using the straight-line distance between two points (as the ...",
                        "default": None
                },
                "row_standardization": {
                        "type": "string",
                        "description": "Specifies whether spatial weights will be standardized. Row standardization is recommended whenever feature distribution is potentially biased due to sampling design or an imposed aggregation scheme.R...",
                        "default": None
                },
                "output_table": {
                        "type": "string",
                        "description": "The table that will be created with each distance band and associated z-score result.",
                        "default": None
                },
                "output_report_file": {
                        "type": "string",
                        "description": "The .pdf file that will be created containing a line graph summarizing results.",
                        "default": None
                }
        },
        "required": [
                "input_features",
                "input_field",
                "number_of_distance_bands"
        ]
},
    "hot_spot_analysis": {
        "name": "hot_spot_analysis",
        "description": "Given a set of weighted features, identifies statistically significant hot spots and cold spots using the Getis-Ord Gi* statistic. Learn more about how Hot Spot Analysis (Getis-Ord Gi*) works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "The feature class for which hot spot analysis will be performed."
                },
                "input_field": {
                        "type": "string",
                        "description": "The numeric field (for example, number of victims, crime rate, test scores, and so on) to be evaluated."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will receive the z-score and p-value results."
                },
                "conceptualization_of_spatial_relationships": {
                        "type": "string",
                        "description": "Specifies how spatial relationships among features will be defined.INVERSE_DISTANCE\u2014Nearby neighboring features will have a larger influence  on the  computations for a target feature than features th..."
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies how distances will be calculated from each feature to neighboring features.EUCLIDEAN_DISTANCE\u2014The straight-line distance between two points (as the crow flies) will be used.MANHATTAN_DISTANC..."
                },
                "standardization": {
                        "type": "string",
                        "description": "Row standardization has no impact on this tool: Results from this tool would be identical with or without row standardization.  This parameter is disabled; it remains only to support backward compatib..."
                },
                "distance_band_or_threshold_distance": {
                        "type": "string",
                        "description": "The cutoff distance for the inverse distance and fixed distance options. Features outside the specified cutoff for a target feature will be ignored in analyses for that feature. However, for ZONE_OF_I...",
                        "default": None
                },
                "self_potential_field": {
                        "type": "string",
                        "description": "The field representing self potential, which is the distance or weight between a feature and itself.",
                        "default": None
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "The path to a file containing weights that define spatial, and potentially temporal, relationships among features.",
                        "default": None
                },
                "apply_false_discovery_rate_fdr_correction": {
                        "type": "string",
                        "description": "Specifies whether statistical significance will be assessed based on the FDR correction.APPLY_FDR\u2014Statistical significance will be based on the FDR correction.NO_FDR\u2014Statistical significance will not ...",
                        "default": None
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "An integer specifying the number of neighbors that will be included in the analysis.",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "input_field",
                "output_feature_class",
                "conceptualization_of_spatial_relationships",
                "distance_method",
                "standardization"
        ]
},
    "average_nearest_neighbor": {
        "name": "average_nearest_neighbor",
        "description": "Calculates a nearest neighbor index based on the average distance from each feature to its nearest neighboring feature. Learn more about how Average Nearest Neighbor Distance works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "The feature class, typically a point feature class, for which the average nearest neighbor distance will be calculated."
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies how distances are calculated from each feature to neighboring features.EUCLIDEAN_DISTANCE\u2014The straight-line distance between two points (as the crow flies) MANHATTAN_DISTANCE\u2014The distance be..."
                },
                "generate_report": {
                        "type": "string",
                        "description": "Specifies whether the tool will create a graphical summary of results.            \r\n            NO_REPORT\u2014No graphical summary will be created. This is the default.GENERATE_REPORT\u2014A graphical summary ...",
                        "default": None
                },
                "area": {
                        "type": "string",
                        "description": "A numeric value representing the study area size. The default value is the area of the minimum enclosing rectangle that would encompass all features (or all selected features). Units should match thos...",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "distance_method"
        ]
},
    "high/low_clustering": {
        "name": "high/low_clustering",
        "description": "Measures the degree of clustering for either high or low values using the Getis-Ord General G statistic. Learn more about how High/Low Clustering: Getis-Ord General G works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "The feature class for which the General G statistic will be calculated."
                },
                "input_field": {
                        "type": "string",
                        "description": "The numeric field to be evaluated."
                },
                "generate_report": {
                        "type": "string",
                        "description": "Specifies whether a graphical summary of result will be created as an .html file.\r\nNO_REPORT\u2014No graphical summary will be created. This is the default.GENERATE_REPORT\u2014A graphical summary will be creat...",
                        "default": None
                },
                "conceptualization_of_spatial_relationships": {
                        "type": "string",
                        "description": "Specifies how spatial relationships among features are defined.INVERSE_DISTANCE\u2014Nearby neighboring features have a larger influence  on the  computations for a target feature than features that are fa..."
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies how distances are calculated from each feature to neighboring features.EUCLIDEAN_DISTANCE\u2014The straight-line distance between two points (as the crow flies) MANHATTAN_DISTANCE\u2014The distance be..."
                },
                "standardization": {
                        "type": "string",
                        "description": "Specifies whether standardization of spatial weights will be applied. Row standardization is recommended whenever the distribution of your features is potentially biased due to sampling design or an i..."
                },
                "distance_band_or_threshold_distance": {
                        "type": "string",
                        "description": "Specifies a cutoff distance for the inverse distance and fixed distance options. Features outside the specified cutoff for a target feature are ignored in analyses for that feature. However, for ZONE_...",
                        "default": None
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "The path to a file containing weights that define spatial, and potentially temporal, relationships among features.",
                        "default": None
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "An integer specifying the number of neighbors that will be included in the analysis.",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "input_field",
                "conceptualization_of_spatial_relationships",
                "distance_method",
                "standardization"
        ]
},
    "multi_distance_spatial_cluster_analysis_(ripley's_k_function)": {
        "name": "multi_distance_spatial_cluster_analysis_(ripley's_k_function)",
        "description": "Determines whether features, or the values associated with features, exhibit statistically significant clustering or dispersion over a range of distances. Learn more about how Multi-Distance Spatial Cluster Analysis works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "The feature class upon which the analysis will be performed."
                },
                "output_table": {
                        "type": "string",
                        "description": "The table to which the results of the analysis will be written."
                },
                "number_of_distance_bands": {
                        "type": "string",
                        "description": "The number of times to increment the neighborhood size and analyze the dataset for clustering. The starting point and size of the increment are specified in the Beginning_Distance and Distance_Increme..."
                },
                "compute_confidence_envelope": {
                        "type": "string",
                        "description": "The confidence envelope is calculated by randomly placing feature points (or feature values) in the study area. The number of points/values randomly placed is equal to the number of points in the feat...",
                        "default": None
                },
                "display_results_graphically": {
                        "type": "string",
                        "description": "This parameter has no effect; it remains to support backward compatibility.NO_DISPLAY\u2014No graphical summary will be created (default).DISPLAY_IT\u2014A graphical summary will be created as a graph layer.",
                        "default": None
                },
                "weight_field": {
                        "type": "string",
                        "description": "A numeric field with weights representing the number of features/events at each location.",
                        "default": None
                },
                "beginning_distance": {
                        "type": "string",
                        "description": "The distance at which to start the cluster analysis and the distance from which to increment. The value entered for this parameter should be in the units of the Output Coordinate System.",
                        "default": None
                },
                "distance_increment": {
                        "type": "string",
                        "description": "The distance to increment during each iteration. The distance used in the analysis starts at the Beginning_Distance and increments by the amount specified in the Distance_Increment. The value entered ...",
                        "default": None
                },
                "boundary_correction_method": {
                        "type": "string",
                        "description": "Method to use to correct for underestimates in the number of neighbors for features near the edges of the study area.NONE\u2014No edge correction is applied. However, if the input feature class already has...",
                        "default": None
                },
                "study_area_method": {
                        "type": "string",
                        "description": "Specifies the region to use for the study area. The K Function is sensitive to changes in study area size so careful selection of this value is important.MINIMUM_ENCLOSING_RECTANGLE\u2014Indicates that the...",
                        "default": None
                },
                "study_area_feature_class": {
                        "type": "string",
                        "description": "Feature class that delineates the area over which the input feature class should be analyzed. Only specified if Study_Area_Method = \"USER_PROVIDED_STUDY_AREA_FEATURE_CLASS\".",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "output_table",
                "number_of_distance_bands"
        ]
},
    "spatial_autocorrelation": {
        "name": "spatial_autocorrelation",
        "description": "Measures spatial autocorrelation based on feature locations and attribute values using the Global Moran's I statistic. Learn more about how Spatial Autocorrelation (Global Moran's I) works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "The feature class for which spatial autocorrelation will be calculated."
                },
                "input_field": {
                        "type": "string",
                        "description": "The numeric field that will be used in assessing spatial autocorrelation."
                },
                "generate_report": {
                        "type": "string",
                        "description": "Specifies whether a graphical summary of result will be created as an .html file.\r\nNO_REPORT\u2014No graphical summary will be created. This is the default.GENERATE_REPORT\u2014A graphical summary will be creat...",
                        "default": None
                },
                "conceptualization_of_spatial_relationships": {
                        "type": "string",
                        "description": "Specifies how spatial relationships among features will be defined.INVERSE_DISTANCE\u2014Nearby neighboring features have a larger influence  on the  computations for a target feature than features that ar..."
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies how distances will be calculated from each feature to neighboring features.EUCLIDEAN_DISTANCE\u2014The straight-line distance between two points (as the crow flies) will be used. This is the defa..."
                },
                "standardization": {
                        "type": "string",
                        "description": "Specifies whether standardization of spatial weights will be applied. Row standardization is recommended whenever the distribution of features is potentially biased due to sampling design or an impose..."
                },
                "distance_band_or_threshold_distance": {
                        "type": "string",
                        "description": "The cutoff distance for the various inverse distance and fixed distance options. Features outside the specified cutoff for a target feature are ignored in analyses for that feature. However, for ZONE_...",
                        "default": None
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "The path to a file containing weights that define spatial, and potentially temporal, relationships among features.",
                        "default": None
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "An integer specifying the number of neighbors that will be included in the analysis.",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "input_field",
                "conceptualization_of_spatial_relationships",
                "distance_method",
                "standardization"
        ]
},
    "hot_spot_analysis_(getis_ord_gi*)": {
        "name": "hot_spot_analysis_(getis_ord_gi*)",
        "description": "Given a set of weighted features, identifies statistically significant hot spots and cold spots using the Getis-Ord Gi* statistic. Learn more about how Hot Spot Analysis (Getis-Ord Gi*) works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "The feature class for which hot spot analysis will be performed."
                },
                "input_field": {
                        "type": "string",
                        "description": "The numeric field (for example, number of victims, crime rate, test scores, and so on) to be evaluated."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will receive the z-score and p-value results."
                },
                "conceptualization_of_spatial_relationships": {
                        "type": "string",
                        "description": "Specifies how spatial relationships among features will be defined.INVERSE_DISTANCE\u2014Nearby neighboring features will have a larger influence  on the  computations for a target feature than features th..."
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies how distances will be calculated from each feature to neighboring features.EUCLIDEAN_DISTANCE\u2014The straight-line distance between two points (as the crow flies) will be used.MANHATTAN_DISTANC..."
                },
                "standardization": {
                        "type": "string",
                        "description": "Row standardization has no impact on this tool: Results from this tool would be identical with or without row standardization.  This parameter is disabled; it remains only to support backward compatib..."
                },
                "distance_band_or_threshold_distance": {
                        "type": "string",
                        "description": "The cutoff distance for the inverse distance and fixed distance options. Features outside the specified cutoff for a target feature will be ignored in analyses for that feature. However, for ZONE_OF_I...",
                        "default": None
                },
                "self_potential_field": {
                        "type": "string",
                        "description": "The field representing self potential, which is the distance or weight between a feature and itself.",
                        "default": None
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "The path to a file containing weights that define spatial, and potentially temporal, relationships among features.",
                        "default": None
                },
                "apply_false_discovery_rate_fdr_correction": {
                        "type": "string",
                        "description": "Specifies whether statistical significance will be assessed based on the FDR correction.APPLY_FDR\u2014Statistical significance will be based on the FDR correction.NO_FDR\u2014Statistical significance will not ...",
                        "default": None
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "An integer specifying the number of neighbors that will be included in the analysis.",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "input_field",
                "output_feature_class",
                "conceptualization_of_spatial_relationships",
                "distance_method",
                "standardization"
        ]
},
    "optimized_hot_spot_analysis": {
        "name": "optimized_hot_spot_analysis",
        "description": "Creates a map of statistically significant hot and cold spots using the Getis-Ord Gi* statistic, given incident points or weighted features (points or polygons). The tool evaluates the characteristics of the input feature class to produce optimal results. Learn more about how Optimized Hot Spot Analysis works",
        "parameters": {
                "input_features": {
                        "type": "string",
                        "description": "The point or polygon feature class for which hot spot analysis will be performed."
                },
                "output_features": {
                        "type": "string",
                        "description": "The output feature class to receive the z-score, p-value, and Gi_Bin results."
                },
                "analysis_field": {
                        "type": "string",
                        "description": "The numeric field (number of incidents, crime rates, test scores, and so on) to be evaluated.",
                        "default": None
                },
                "incident_data_aggregation_method": {
                        "type": "string",
                        "description": "The aggregation method to use to create weighted features for analysis from incident point data.\r\nCOUNT_INCIDENTS_WITHIN_FISHNET_POLYGONS\u2014A fishnet polygon mesh will overlay the incident point data  a...",
                        "default": None
                },
                "bounding_polygons_defining_where_incidents_are_possible": {
                        "type": "string",
                        "description": "A polygon feature class defining where the incident Input_Features could possibly occur.",
                        "default": None
                },
                "polygons_for_aggregating_incidents_into_counts": {
                        "type": "string",
                        "description": "The polygons to use to aggregate the incident Input_Features in order to get an incident count for each polygon feature.",
                        "default": None
                },
                "density_surface": {
                        "type": "string",
                        "description": "The Density_Surface parameter is disabled; it\r\nremains as a tool parameter only to support backwards\r\ncompatibility.\r\nThe Kernel Density tool can be used if you would like a density surface visualizat...",
                        "default": None
                },
                "cell_size": {
                        "type": "string",
                        "description": "The size of the grid cells used to aggregate the Input_Features.  When aggregating into a hexagon grid, this distance is used as the height to construct the hexagon polygons.",
                        "default": None
                },
                "distance_band": {
                        "type": "string",
                        "description": "The spatial extent of the analysis neighborhood.  This value determines which features are analyzed together in order to assess local clustering.",
                        "default": None
                }
        },
        "required": [
                "input_features",
                "output_features"
        ]
},
    "cluster_and_outlier_analysis_(anselin_local_moran's_i)": {
        "name": "cluster_and_outlier_analysis_(anselin_local_moran's_i)",
        "description": "Identifies statistically significant hot spots, cold spots, and spatial outliers using the Anselin Local Moran's I statistic, given a set of weighted features. Learn more about how Cluster and Outlier Analysis (Anselin Local Moran's I) works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "The feature class for which cluster and outlier analysis will be performed."
                },
                "input_field": {
                        "type": "string",
                        "description": "The numeric field to be evaluated."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "The output feature class to receive the results fields."
                },
                "conceptualization_of_spatial_relationships": {
                        "type": "string",
                        "description": "Specifies how spatial relationships among features are defined.INVERSE_DISTANCE\u2014Nearby neighboring features have a larger influence  on the  computations for a target feature than features that are fa..."
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies how distances are calculated from each feature to neighboring features.EUCLIDEAN_DISTANCE\u2014The straight-line distance between two points (as the crow flies) MANHATTAN_DISTANCE\u2014The distance be..."
                },
                "standardization": {
                        "type": "string",
                        "description": "Row standardization is recommended whenever the distribution of your features is potentially biased due to sampling design or an imposed aggregation scheme.NONE\u2014No standardization of spatial weights i..."
                },
                "distance_band_or_threshold_distance": {
                        "type": "string",
                        "description": "Specifies a cutoff distance for Inverse Distance and Fixed Distance options. Features outside the specified cutoff for a target feature are ignored in analyses for that feature. However, for Zone of I...",
                        "default": None
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "The path to a file containing weights that define spatial, and potentially temporal, relationships among features.",
                        "default": None
                },
                "apply_false_discovery_rate_fdr_correction": {
                        "type": "string",
                        "description": "APPLY_FDR\u2014Statistical significance will be based on the False Discovery Rate correction for a 95 percent confidence level.NO_FDR\u2014Features with p-values less than 0.05 will appear in the COType field r...",
                        "default": None
                },
                "number_of_permutations": {
                        "type": "string",
                        "description": "The number of random permutations for the calculation of pseudo p-values. The default number of permutations is 499. \r\nIf you choose 0 permutations, the standard p-value is calculated.0\u2014Permutations a...",
                        "default": None
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "The number of neighbors to include in the analysis.",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "input_field",
                "output_feature_class",
                "conceptualization_of_spatial_relationships",
                "distance_method",
                "standardization"
        ]
},
    "optimized_outlier_analysis": {
        "name": "optimized_outlier_analysis",
        "description": "Given incident points or weighted features (points or polygons), creates a map of statistically significant hot spots, cold spots, and spatial outliers using the Anselin Local Moran's I statistic. It evaluates the characteristics of the input feature class to produce optimal results. Learn more about how Optimized Outlier Analysis works",
        "parameters": {
                "input_features": {
                        "type": "string",
                        "description": "The point or polygon feature class for which the cluster and outlier analysis will be performed."
                },
                "output_features": {
                        "type": "string",
                        "description": "The output feature class to receive the result fields."
                },
                "analysis_field": {
                        "type": "string",
                        "description": "The numeric field (number of incidents, crime rates, test scores, and so on) to be evaluated.",
                        "default": None
                },
                "incident_data_aggregation_method": {
                        "type": "string",
                        "description": "The aggregation method to use to create weighted features for analysis from incident point data.\r\nCOUNT_INCIDENTS_WITHIN_FISHNET_POLYGONS\u2014A fishnet polygon mesh will overlay the incident point data  a...",
                        "default": None
                },
                "bounding_polygons_defining_where_incidents_are_possible": {
                        "type": "string",
                        "description": "A polygon feature class defining where the incident Input_Features could possibly occur.",
                        "default": None
                },
                "polygons_for_aggregating_incidents_into_counts": {
                        "type": "string",
                        "description": "The polygons to use to aggregate the incident Input_Features in order to get an incident count for each polygon feature.",
                        "default": None
                },
                "performance_adjustment": {
                        "type": "string",
                        "description": "This analysis utilizes permutations to create a reference distribution.  Choosing the number of permutations is a balance between precision and increased processing time. \r\nChoose your preference for ...",
                        "default": None
                },
                "cell_size": {
                        "type": "string",
                        "description": "The size of the grid cells used to aggregate the Input_Features.  When aggregating into a hexagon grid, this distance is used as the height to construct the hexagon polygons.",
                        "default": None
                },
                "distance_band": {
                        "type": "string",
                        "description": "The spatial extent of the analysis neighborhood.  This value determines which features are analyzed together in order to assess local clustering.",
                        "default": None
                }
        },
        "required": [
                "input_features",
                "output_features"
        ]
},
    "generalized_linear_regression": {
        "name": "generalized_linear_regression",
        "description": "Performs generalized linear regression (GLR) to generate predictions or to model a dependent variable in terms of its relationship to a set of explanatory variables.  This tool can be used to fit continuous (OLS), binary (logistic), and count (Poisson) models. Learn more about how Generalized Linear Regression works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The feature class containing the dependent and independent variables."
                },
                "dependent_variable": {
                        "type": "string",
                        "description": "The numeric field containing the observed values to be modeled."
                },
                "model_type": {
                        "type": "string",
                        "description": "Specifies the  type of data that will be modeled.CONTINUOUS\u2014 The dependent_variable value is continuous.  The model used is Gaussian, and the tool performs  ordinary least squares regression.BINARY\u2014 T..."
                },
                "output_features": {
                        "type": "string",
                        "description": "The new feature class that will contain the dependent variable estimates and residuals."
                },
                "explanatory_variables": {
                        "type": "string",
                        "description": "A list of fields representing independent explanatory variables in the regression model."
                },
                "distance_features": {
                        "type": "string",
                        "description": "Automatically creates explanatory variables by calculating a distance from the provided features to the in_features values. Distances will be calculated from each of the input distance_features values...",
                        "default": None
                },
                "prediction_locations": {
                        "type": "string",
                        "description": "A feature class containing features representing locations where estimates will be computed. Each feature in this dataset should contain values for all  the explanatory variables specified. The depend...",
                        "default": None
                },
                "explanatory_variables_to_matchfield_from_prediction_locations_field_from_input_features": {
                        "type": "string",
                        "description": "Matches the explanatory variables in the prediction_locations parameter to corresponding explanatory variables from the in_features parameter.",
                        "default": None
                },
                "explanatory_distance_matchingprediction_distance_features_input_explanatory_distance_features": {
                        "type": "string",
                        "description": "Matches the distance features specified for the features_to_predict parameter on the left to the corresponding distance features for the in_features parameter on the right.",
                        "default": None
                },
                "output_predicted_features": {
                        "type": "string",
                        "description": "The output feature class that will receive dependent variable estimates for each prediction_location value.\r\n The output feature class that will receive dependent variable estimates for each Predictio...",
                        "default": None
                },
                "output_trained_model": {
                        "type": "string",
                        "description": "An output model file that will save the trained model, which can be used later for prediction.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "dependent_variable",
                "model_type",
                "output_features",
                "explanatory_variables"
        ]
},
    "spatial_autocorrelation_(global_moran's_i)": {
        "name": "spatial_autocorrelation_(global_moran's_i)",
        "description": "Measures spatial autocorrelation based on feature locations and attribute values using the Global Moran's I statistic. Learn more about how Spatial Autocorrelation (Global Moran's I) works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "The feature class for which spatial autocorrelation will be calculated."
                },
                "input_field": {
                        "type": "string",
                        "description": "The numeric field that will be used in assessing spatial autocorrelation."
                },
                "generate_report": {
                        "type": "string",
                        "description": "Specifies whether a graphical summary of result will be created as an .html file.\r\nNO_REPORT\u2014No graphical summary will be created. This is the default.GENERATE_REPORT\u2014A graphical summary will be creat...",
                        "default": None
                },
                "conceptualization_of_spatial_relationships": {
                        "type": "string",
                        "description": "Specifies how spatial relationships among features will be defined.INVERSE_DISTANCE\u2014Nearby neighboring features have a larger influence  on the  computations for a target feature than features that ar..."
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies how distances will be calculated from each feature to neighboring features.EUCLIDEAN_DISTANCE\u2014The straight-line distance between two points (as the crow flies) will be used. This is the defa..."
                },
                "standardization": {
                        "type": "string",
                        "description": "Specifies whether standardization of spatial weights will be applied. Row standardization is recommended whenever the distribution of features is potentially biased due to sampling design or an impose..."
                },
                "distance_band_or_threshold_distance": {
                        "type": "string",
                        "description": "The cutoff distance for the various inverse distance and fixed distance options. Features outside the specified cutoff for a target feature are ignored in analyses for that feature. However, for ZONE_...",
                        "default": None
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "The path to a file containing weights that define spatial, and potentially temporal, relationships among features.",
                        "default": None
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "An integer specifying the number of neighbors that will be included in the analysis.",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "input_field",
                "conceptualization_of_spatial_relationships",
                "distance_method",
                "standardization"
        ]
},
    "calculate_composite_index": {
        "name": "calculate_composite_index",
        "description": "Combines multiple numeric variables to create a single index. Composite indices are used across social and environmental domains to represent complex information from multiple indicators as a single metric that can measure progress toward a goal and facilitate decisions. The tool supports the three main steps of the index creation process: standardize input variables to a common scale (preprocessing), combine variables to a single index variable (combination), and scale and classify the resulting index to meaningful values (postprocessing). Learn more about how Calculate Composite Index works",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table or features containing the variables that will be combined into the index."
                },
                "in_variablesvar1_reverse1_var2_reverse2": {
                        "type": "string",
                        "description": "A list of numeric fields representing the variables that will be combined as an index. The Reverse Direction column reverses the values of the variables. This means that the feature or record that ori..."
                },
                "append_to_input": {
                        "type": "string",
                        "description": "Specifies whether the results will be appended to the input data or provided as an output feature class or table.APPEND_TO_INPUT\u2014 The results will be appended to the input data. This option modifies t...",
                        "default": None
                },
                "out_table": {
                        "type": "string",
                        "description": "The output features or table that will include the results.",
                        "default": None
                },
                "index_preset": {
                        "type": "string",
                        "description": "Specifies the workflow that will be used when creating the index. The options represent common index creation workflows; each option sets default values for the preprocessing and index_method paramete...",
                        "default": None
                },
                "preprocessing": {
                        "type": "string",
                        "description": "Specifies the method that will be used to convert \r\nthe input variables to a common scale.MINMAX\u2014 Variables will be scaled between 0 and 1 using the minimum and maximum values of each variable. This i...",
                        "default": None
                },
                "pre_threshold_scaling": {
                        "type": "string",
                        "description": "Specifies the method that will be used to convert the input variables to a common scale prior to setting thresholds.\r\nTHRESHOLD_MINMAX\u2014Variables between 0 and 1 will be scaled using the minimum and ma...",
                        "default": None
                },
                "pre_custom_zscorefield1_mean1_stdev1_field2_mean2_stdev2": {
                        "type": "string",
                        "description": "The custom mean value and custom standard deviation that will be used when standardizing each input variable. For each variable, provide the custom mean in the Mean column and the custom standard devi...",
                        "default": None
                },
                "pre_min_maxfield1_min1_max1_field2_min2_max2": {
                        "type": "string",
                        "description": "The possible minimum and maximum values that will be used in the units of the variables. Each variable will be scaled between 0 and 1 based on the possible minimum and maximum values.",
                        "default": None
                },
                "pre_thresholdsfield1_method1_threshold1_field2_method2_threshold2": {
                        "type": "string",
                        "description": "The threshold that determines whether a feature will be flagged. Specify the value in the units of the scaled variables and specify whether values above or below the threshold value will be flagged.",
                        "default": None
                },
                "index_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to combine the scaled variables into a single value.\r\nSUM\u2014The values will be added.MEAN\u2014The arithmetic (additive) mean of the values will be calculated. This is ...",
                        "default": None
                },
                "index_weightsfield1_weight1_field2_weight2": {
                        "type": "string",
                        "description": "The weights that will set the relative influence of each input variable on the index.\r\n Each weight has a default value of 1, meaning that each variable has equal contribution. Increase or decrease th...",
                        "default": None
                },
                "out_index_name": {
                        "type": "string",
                        "description": "The name of the index. The value is used in the visualization of the outputs, such as field aliases and chart labels. The value is not used when the output (or appended input) is a shapefile.",
                        "default": None
                },
                "out_index_reverse": {
                        "type": "string",
                        "description": "Specifies whether the output index values will be reversed in direction (for example, to treat high index values as low values).REVERSE\u2014 The index values will be reversed in direction.NO_REVERSE\u2014 The ...",
                        "default": None
                },
                "post_min_max": {
                        "type": "string",
                        "description": "The minimum and maximum of the output index values. This scaling is applied after combining the scaled variables. If no values are provided, the output index is not scaled.",
                        "default": None
                },
                "post_reclass": {
                        "type": "string",
                        "description": "Specifies the method that will be used to classify the output index. An additional output field will be provided for each selected option.EQINTERVAL\u2014Classes will be created by dividing the range of va...",
                        "default": None
                },
                "post_num_classes": {
                        "type": "string",
                        "description": "The number of classes that will be used for the equal interval and quantile classification methods.",
                        "default": None
                },
                "post_custom_classesmin1_max1_min2_max2": {
                        "type": "string",
                        "description": "The upper bounds and class values\r\nfor the custom classification method. For example, you can use this variable to classify an index containing values between 0 and 100 into classes representing low, ...",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "in_variablesvar1_reverse1_var2_reverse2"
        ]
},
    "assess_sensitivity_to_attribute_uncertainty": {
        "name": "assess_sensitivity_to_attribute_uncertainty",
        "description": "Measures the stability of an analysis result by comparing the original analysis output to the results from multiple tool runs using simulated data. The simulated data accounts for uncertainty in one or more analysis variables. Three types of attribute uncertainty are supported: margin of error, confidence bounds, and a percentage of the original attribute value. Learn more about how Assess Sensitivity to Attribute Uncertainty Works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "A feature class containing the output analysis result from a spatial statistics tool. Only certain tools are supported. This is the analysis result that will be evaluated for stability."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output features that will contain a copy of the original analysis results and fields summarizing the stability of the analysis for each feature."
                },
                "out_simulation_table": {
                        "type": "string",
                        "description": "The output table that will contain fields summarizing the stability of the analysis."
                },
                "analysis_input_features": {
                        "type": "string",
                        "description": "The input features that were used in the analysis that produced the analysis result features.",
                        "default": None
                },
                "uncertainty_measure": {
                        "type": "string",
                        "description": "Specifies how attribute uncertainty will be measured.MOE\u2014The input feature class of the original analysis contains a field with the symmetrical margin of error for each feature and that will be used.C...",
                        "default": None
                },
                "moe_field": {
                        "type": "string",
                        "description": "The field containing the margin of error (MOE) of the analysis variable. The MOE is used to construct a symmetric distribution from which the simulated values will be generated.",
                        "default": None
                },
                "confidence_bound_field": {
                        "type": "string",
                        "description": "The fields containing the lower and upper bounds for the analysis variable. Values will be generated between the lower and upper confidence bounds.",
                        "default": None
                },
                "randomize_pct": {
                        "type": "string",
                        "description": "The percentage of the original attribute value that will be subtracted and added to the original value of the analysis variable to create a range of values for the simulations.",
                        "default": None
                },
                "num_simulations": {
                        "type": "string",
                        "description": "The number of simulations that will be performed.",
                        "default": None
                },
                "simulation_method": {
                        "type": "string",
                        "description": "Specifies the probability distribution that will be used to simulate data.\r\nNORMAL\u2014A normal distribution will be used. This is the default.UNIFORM\u2014A uniform distribution will be used.TRIANGULAR\u2014A tria...",
                        "default": None
                },
                "output_workspace": {
                        "type": "string",
                        "description": "An existing workspace where the analysis results from each simulation will be stored. The workspace can be a folder or a geodatabase.",
                        "default": None
                },
                "sim_data_limits": {
                        "type": "string",
                        "description": "The lower and upper limits for the simulated values. All simulated values will be within these limits. For example, for counts or percentages, use a lower limit of zero to ensure that there are no neg...",
                        "default": None
                },
                "moe_conf_level": {
                        "type": "string",
                        "description": "The confidence level of the margins of error. For example, if the margins of error were created from 95 percent confidence intervals, provide a value of 95.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_features",
                "out_simulation_table"
        ]
},
    "build_balanced_zones": {
        "name": "build_balanced_zones",
        "description": "Creates spatially contiguous zones in a study area using a genetic growth algorithm based on specified criteria. You can create zones that contain an equal number of features, zones that are similar based on a set of attribute values, or both. You can also select zones with approximately equal areas, that are as compact as possible, and that maintain consistent summary statistics of other variables. Learn more about how Build Balanced Zones works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The feature class or feature layer that will be aggregated into zones."
                },
                "output_features": {
                        "type": "string",
                        "description": "The output feature class indicating which features are aggregated into each zone. The feature class will be symbolized by the ZONE_ID field and will contain fields displaying the values of each criter..."
                },
                "zone_creation_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to create each zone. Zones grow until all specified criteria are satisfied.ATTRIBUTE_TARGET\u2014Zones will be created based on target values of one or multiple varia..."
                },
                "number_of_zones": {
                        "type": "string",
                        "description": "The number of zones that will be created.",
                        "default": None
                },
                "zone_building_criteria_targetvariable_sum_weight": {
                        "type": "string",
                        "description": "Specifies the variables that will be considered, as well as their target values and optional weights. The default weight is 1, and each variable contributes equally unless they are changed.",
                        "default": None
                },
                "zone_building_criteriavariable_weight": {
                        "type": "string",
                        "description": "Specifies the variables that will be considered and, optionally, their weights. The default weight is 1, and each variable contributes equally unless changed.",
                        "default": None
                },
                "spatial_constraints": {
                        "type": "string",
                        "description": "Specifies how neighbors will be defined while the zones grow. Zones can only grow into new features that are neighbors of at least one of the features already in the zone. If the input features are po...",
                        "default": None
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "The path to a file containing spatial weights that define spatial and, optionally, temporal relationships among features.",
                        "default": None
                },
                "zone_characteristics": {
                        "type": "string",
                        "description": "Specifies the characteristics of the zones that will be created.EQUAL_AREA\u2014 Zones with total area as similar as possible will be created.COMPACTNESS\u2014Zones with more closely-packed (compact) features w...",
                        "default": None
                },
                "attribute_to_considervariable_function": {
                        "type": "string",
                        "description": "Specifies attributes and statistics to consider in the selection of final zones. You can homogenize attributes based on their sum, average, median, or variance. For example, if you are creating zones ...",
                        "default": None
                },
                "distance_to_consider": {
                        "type": "string",
                        "description": "The feature class that will be used to homogenize the total distance per zone. The distance is calculated from each of the input features to the closest feature provided in this parameter. This distan...",
                        "default": None
                },
                "categorial_variable": {
                        "type": "string",
                        "description": "The categorical variable to be considered for zone proportions.",
                        "default": None
                },
                "proportion_method": {
                        "type": "string",
                        "description": "Specifies the type of proportion that will be maintained based on the chosen categorical variable.MAINTAIN_WITHIN_PROPORTION\u2014Each zone will maintain the same proportions as the overall study area for ...",
                        "default": None
                },
                "population_size": {
                        "type": "string",
                        "description": "The number of randomly generated initial seeds. For larger datasets, increasing this number will increase the search space and the probability of finding a better solution. The default is 100.",
                        "default": None
                },
                "number_generations": {
                        "type": "string",
                        "description": "The number of times the zone search process will be repeated. For larger datasets, increasing the number is recommended to find an optimal solution. The default is 50 generations.",
                        "default": None
                },
                "mutation_factor": {
                        "type": "string",
                        "description": "The probability that an individual's seed values will be mutated to a new set of seeds. Mutation increases the search space by introducing variability of the possible solutions in every generation and...",
                        "default": None
                },
                "output_convergence_table": {
                        "type": "string",
                        "description": "The table containing the total fitness score for the best solution found in every generation as well as the fitness score for the individual zone constraints.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "output_features",
                "zone_creation_method"
        ]
},
    "calculate_composite_index": {
        "name": "calculate_composite_index",
        "description": "Combines multiple numeric variables to create a single index. Composite indices are used across social and environmental domains to represent complex information from multiple indicators as a single metric that can measure progress toward a goal and facilitate decisions. The tool supports the three main steps of the index creation process: standardize input variables to a common scale (preprocessing), combine variables to a single index variable (combination), and scale and classify the resulting index to meaningful values (postprocessing). Learn more about how Calculate Composite Index works",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table or features containing the variables that will be combined into the index."
                },
                "in_variablesvar1_reverse1_var2_reverse2": {
                        "type": "string",
                        "description": "A list of numeric fields representing the variables that will be combined as an index. The Reverse Direction column reverses the values of the variables. This means that the feature or record that ori..."
                },
                "append_to_input": {
                        "type": "string",
                        "description": "Specifies whether the results will be appended to the input data or provided as an output feature class or table.APPEND_TO_INPUT\u2014 The results will be appended to the input data. This option modifies t...",
                        "default": None
                },
                "out_table": {
                        "type": "string",
                        "description": "The output features or table that will include the results.",
                        "default": None
                },
                "index_preset": {
                        "type": "string",
                        "description": "Specifies the workflow that will be used when creating the index. The options represent common index creation workflows; each option sets default values for the preprocessing and index_method paramete...",
                        "default": None
                },
                "preprocessing": {
                        "type": "string",
                        "description": "Specifies the method that will be used to convert \r\nthe input variables to a common scale.MINMAX\u2014 Variables will be scaled between 0 and 1 using the minimum and maximum values of each variable. This i...",
                        "default": None
                },
                "pre_threshold_scaling": {
                        "type": "string",
                        "description": "Specifies the method that will be used to convert the input variables to a common scale prior to setting thresholds.\r\nTHRESHOLD_MINMAX\u2014Variables between 0 and 1 will be scaled using the minimum and ma...",
                        "default": None
                },
                "pre_custom_zscorefield1_mean1_stdev1_field2_mean2_stdev2": {
                        "type": "string",
                        "description": "The custom mean value and custom standard deviation that will be used when standardizing each input variable. For each variable, provide the custom mean in the Mean column and the custom standard devi...",
                        "default": None
                },
                "pre_min_maxfield1_min1_max1_field2_min2_max2": {
                        "type": "string",
                        "description": "The possible minimum and maximum values that will be used in the units of the variables. Each variable will be scaled between 0 and 1 based on the possible minimum and maximum values.",
                        "default": None
                },
                "pre_thresholdsfield1_method1_threshold1_field2_method2_threshold2": {
                        "type": "string",
                        "description": "The threshold that determines whether a feature will be flagged. Specify the value in the units of the scaled variables and specify whether values above or below the threshold value will be flagged.",
                        "default": None
                },
                "index_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to combine the scaled variables into a single value.\r\nSUM\u2014The values will be added.MEAN\u2014The arithmetic (additive) mean of the values will be calculated. This is ...",
                        "default": None
                },
                "index_weightsfield1_weight1_field2_weight2": {
                        "type": "string",
                        "description": "The weights that will set the relative influence of each input variable on the index.\r\n Each weight has a default value of 1, meaning that each variable has equal contribution. Increase or decrease th...",
                        "default": None
                },
                "out_index_name": {
                        "type": "string",
                        "description": "The name of the index. The value is used in the visualization of the outputs, such as field aliases and chart labels. The value is not used when the output (or appended input) is a shapefile.",
                        "default": None
                },
                "out_index_reverse": {
                        "type": "string",
                        "description": "Specifies whether the output index values will be reversed in direction (for example, to treat high index values as low values).REVERSE\u2014 The index values will be reversed in direction.NO_REVERSE\u2014 The ...",
                        "default": None
                },
                "post_min_max": {
                        "type": "string",
                        "description": "The minimum and maximum of the output index values. This scaling is applied after combining the scaled variables. If no values are provided, the output index is not scaled.",
                        "default": None
                },
                "post_reclass": {
                        "type": "string",
                        "description": "Specifies the method that will be used to classify the output index. An additional output field will be provided for each selected option.EQINTERVAL\u2014Classes will be created by dividing the range of va...",
                        "default": None
                },
                "post_num_classes": {
                        "type": "string",
                        "description": "The number of classes that will be used for the equal interval and quantile classification methods.",
                        "default": None
                },
                "post_custom_classesmin1_max1_min2_max2": {
                        "type": "string",
                        "description": "The upper bounds and class values\r\nfor the custom classification method. For example, you can use this variable to classify an index containing values between 0 and 100 into classes representing low, ...",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "in_variablesvar1_reverse1_var2_reverse2"
        ]
},
    "cluster_and_outlier_analysis_(anselin_local_moran's_i)": {
        "name": "cluster_and_outlier_analysis_(anselin_local_moran's_i)",
        "description": "Identifies statistically significant hot spots, cold spots, and spatial outliers using the Anselin Local Moran's I statistic, given a set of weighted features. Learn more about how Cluster and Outlier Analysis (Anselin Local Moran's I) works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "The feature class for which cluster and outlier analysis will be performed."
                },
                "input_field": {
                        "type": "string",
                        "description": "The numeric field to be evaluated."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "The output feature class to receive the results fields."
                },
                "conceptualization_of_spatial_relationships": {
                        "type": "string",
                        "description": "Specifies how spatial relationships among features are defined.INVERSE_DISTANCE\u2014Nearby neighboring features have a larger influence  on the  computations for a target feature than features that are fa..."
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies how distances are calculated from each feature to neighboring features.EUCLIDEAN_DISTANCE\u2014The straight-line distance between two points (as the crow flies) MANHATTAN_DISTANCE\u2014The distance be..."
                },
                "standardization": {
                        "type": "string",
                        "description": "Row standardization is recommended whenever the distribution of your features is potentially biased due to sampling design or an imposed aggregation scheme.NONE\u2014No standardization of spatial weights i..."
                },
                "distance_band_or_threshold_distance": {
                        "type": "string",
                        "description": "Specifies a cutoff distance for Inverse Distance and Fixed Distance options. Features outside the specified cutoff for a target feature are ignored in analyses for that feature. However, for Zone of I...",
                        "default": None
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "The path to a file containing weights that define spatial, and potentially temporal, relationships among features.",
                        "default": None
                },
                "apply_false_discovery_rate_fdr_correction": {
                        "type": "string",
                        "description": "APPLY_FDR\u2014Statistical significance will be based on the False Discovery Rate correction for a 95 percent confidence level.NO_FDR\u2014Features with p-values less than 0.05 will appear in the COType field r...",
                        "default": None
                },
                "number_of_permutations": {
                        "type": "string",
                        "description": "The number of random permutations for the calculation of pseudo p-values. The default number of permutations is 499. \r\nIf you choose 0 permutations, the standard p-value is calculated.0\u2014Permutations a...",
                        "default": None
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "The number of neighbors to include in the analysis.",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "input_field",
                "output_feature_class",
                "conceptualization_of_spatial_relationships",
                "distance_method",
                "standardization"
        ]
},
    "density_based_clustering": {
        "name": "density_based_clustering",
        "description": "Finds clusters of point features within surrounding noise based on their spatial distribution. Time can also be incorporated to find space-time clusters. Learn more about how Density-based Clustering works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The point features for which density-based clustering will be performed."
                },
                "output_features": {
                        "type": "string",
                        "description": "The output feature class that will receive the cluster results."
                },
                "cluster_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to define clusters.\r\nDBSCAN\u2014 A specified distance will be used to separate dense clusters from sparser noise. DBSCAN is the fastest of the clustering methods but..."
                },
                "min_features_cluster": {
                        "type": "string",
                        "description": "The minimum number of points that will be considered a cluster.\r\nAny cluster with fewer points than the number provided will be considered noise."
                },
                "search_distance": {
                        "type": "string",
                        "description": "The maximum distance that will be considered.For the cluster_method parameter's DBSCAN option, the min_features_cluster parameter value must be found within this distance for cluster membership. Indiv...",
                        "default": None
                },
                "cluster_sensitivity": {
                        "type": "string",
                        "description": "An integer between 0 and 100 that determines the compactness of clusters. A number close to 100 will result in a higher number of dense clusters. A number close to 0 will result in fewer, less compact..."
                },
                "time_field": {
                        "type": "string",
                        "description": "The field containing the time stamp for each record in the dataset. This field must be of type Date. If provided,  the tool will find clusters of points that are close to each other in space and time...."
                },
                "search_time_interval": {
                        "type": "string",
                        "description": "The time interval that will be used to determine whether points form a space-time cluster.  The search time interval spans before and after the time of each point; for example, an interval of 3 days a..."
                }
        },
        "required": [
                "in_features",
                "output_features",
                "cluster_method",
                "min_features_cluster",
                "cluster_sensitivity",
                "time_field",
                "search_time_interval"
        ]
},
    "hot_spot_analysis_(getis_ord_gi*)": {
        "name": "hot_spot_analysis_(getis_ord_gi*)",
        "description": "Given a set of weighted features, identifies statistically significant hot spots and cold spots using the Getis-Ord Gi* statistic. Learn more about how Hot Spot Analysis (Getis-Ord Gi*) works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "The feature class for which hot spot analysis will be performed."
                },
                "input_field": {
                        "type": "string",
                        "description": "The numeric field (for example, number of victims, crime rate, test scores, and so on) to be evaluated."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will receive the z-score and p-value results."
                },
                "conceptualization_of_spatial_relationships": {
                        "type": "string",
                        "description": "Specifies how spatial relationships among features will be defined.INVERSE_DISTANCE\u2014Nearby neighboring features will have a larger influence  on the  computations for a target feature than features th..."
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies how distances will be calculated from each feature to neighboring features.EUCLIDEAN_DISTANCE\u2014The straight-line distance between two points (as the crow flies) will be used.MANHATTAN_DISTANC..."
                },
                "standardization": {
                        "type": "string",
                        "description": "Row standardization has no impact on this tool: Results from this tool would be identical with or without row standardization.  This parameter is disabled; it remains only to support backward compatib..."
                },
                "distance_band_or_threshold_distance": {
                        "type": "string",
                        "description": "The cutoff distance for the inverse distance and fixed distance options. Features outside the specified cutoff for a target feature will be ignored in analyses for that feature. However, for ZONE_OF_I...",
                        "default": None
                },
                "self_potential_field": {
                        "type": "string",
                        "description": "The field representing self potential, which is the distance or weight between a feature and itself.",
                        "default": None
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "The path to a file containing weights that define spatial, and potentially temporal, relationships among features.",
                        "default": None
                },
                "apply_false_discovery_rate_fdr_correction": {
                        "type": "string",
                        "description": "Specifies whether statistical significance will be assessed based on the FDR correction.APPLY_FDR\u2014Statistical significance will be based on the FDR correction.NO_FDR\u2014Statistical significance will not ...",
                        "default": None
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "An integer specifying the number of neighbors that will be included in the analysis.",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "input_field",
                "output_feature_class",
                "conceptualization_of_spatial_relationships",
                "distance_method",
                "standardization"
        ]
},
    "hot_spot_analysis_comparison": {
        "name": "hot_spot_analysis_comparison",
        "description": "Compares two hot spot analysis result layers and measures their similarity and association. The  similarity and association between the hot spot result layers is determined by comparing the significance level categories between corresponding features in both input layers. The similarity measures how closely the hot spots, cold spots, and nonsignificant areas of both hot spot results spatially align. The association (or dependence) measures the strength of the underlying statistical relationship between the hot spot variables (similar to correlation for continuous variables). Learn more about how Hot Spot Analysis Comparison works",
        "parameters": {
                "in_hot_spot_1": {
                        "type": "string",
                        "description": "The first hot spot analysis result layer."
                },
                "in_hot_spot_2": {
                        "type": "string",
                        "description": "The second hot spot analysis result layer."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output feature class that will contain the local measures of similarity and association."
                },
                "num_neighbors": {
                        "type": "string",
                        "description": "The number of neighbors around each feature that will be used for distance weighting. Distance weighting is one component of the overall similarity, and any features with matching significance levels ...",
                        "default": None
                },
                "num_perms": {
                        "type": "string",
                        "description": "The number of permutations that will be used to estimate the expected similarity and kappa values. A larger number of simulations will increase the precision of the estimates but will also increase ca...",
                        "default": None
                },
                "weighting_method": {
                        "type": "string",
                        "description": "Specifies how similarity weights between significance level categories will be defined.  Similarity weights are numbers between 0 and 1 that define the categories of one result that are expected to ma...",
                        "default": None
                },
                "similarity_weights": {
                        "type": "string",
                        "description": "The custom similarity weights between significance level categories.  \r\nThe weights are values between 0 and 1 and indicate how similar to consider the two categories. A value of 0 indicates the categ...",
                        "default": None
                },
                "in_weights_table": {
                        "type": "string",
                        "description": "The table containing custom similarity weights for each combination of hot spot significance level categories. The table must contain CATEGORY1, CATEGORY2, and WEIGHT fields. Provide the significance ...",
                        "default": None
                },
                "exclude_nonsig_features": {
                        "type": "string",
                        "description": "Specifies whether pairs of features will be excluded from the comparisons if both hot spot results are nonsignificant. If excluded, conditional similarity and kappa values will be calculated that comp...",
                        "default": None
                }
        },
        "required": [
                "in_hot_spot_1",
                "in_hot_spot_2",
                "out_features"
        ]
},
    "multivariate_clustering": {
        "name": "multivariate_clustering",
        "description": "Finds natural clusters of features based solely on feature attribute values. Learn more about how Multivariate Clustering works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The feature class or feature layer for which clusters will be created."
                },
                "output_features": {
                        "type": "string",
                        "description": "The output feature class that will be created containing all features, the analysis fields specified, and a field indicating to which cluster each feature belongs."
                },
                "analysis_fieldsanalysis_field": {
                        "type": "string",
                        "description": "A list of fields that will be used to distinguish one cluster from another."
                },
                "clustering_method": {
                        "type": "string",
                        "description": "Specifies the clustering algorithm that will be used.The K_MEANS and K_MEDOIDS options generally produce similar results. However, K_MEDOIDS is more robust to noise and outliers in the in_features par...",
                        "default": None
                },
                "initialization_method": {
                        "type": "string",
                        "description": "Specifies how initial seeds to grow clusters are obtained.   If you indicate you want three clusters, for example, the analysis will begin with three seeds.            OPTIMIZED_SEED_LOCATIONS\u2014Seed  f...",
                        "default": None
                },
                "initialization_field": {
                        "type": "string",
                        "description": "The numeric field identifying seed features.  Features with a value of 1 for this field will be used to grow clusters.  Each seed results in a cluster, so at least two seed features must be provided.",
                        "default": None
                },
                "number_of_clusters": {
                        "type": "string",
                        "description": "The number of clusters that will be created.  If you leave this parameter empty,  the tool will evaluate the optimal number of clusters by computing a pseudo F-statistic for clustering solutions with ...",
                        "default": None
                },
                "output_table": {
                        "type": "string",
                        "description": "The table containing the pseudo  F-statistic for clustering solutions 2 through 30,  calculated to evaluate the optimal number of clusters. The chart created from this table can be accessed in the sta...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "output_features",
                "analysis_fieldsanalysis_field"
        ]
},
    "optimized_hot_spot_analysis": {
        "name": "optimized_hot_spot_analysis",
        "description": "Creates a map of statistically significant hot and cold spots using the Getis-Ord Gi* statistic, given incident points or weighted features (points or polygons). The tool evaluates the characteristics of the input feature class to produce optimal results. Learn more about how Optimized Hot Spot Analysis works",
        "parameters": {
                "input_features": {
                        "type": "string",
                        "description": "The point or polygon feature class for which hot spot analysis will be performed."
                },
                "output_features": {
                        "type": "string",
                        "description": "The output feature class to receive the z-score, p-value, and Gi_Bin results."
                },
                "analysis_field": {
                        "type": "string",
                        "description": "The numeric field (number of incidents, crime rates, test scores, and so on) to be evaluated.",
                        "default": None
                },
                "incident_data_aggregation_method": {
                        "type": "string",
                        "description": "The aggregation method to use to create weighted features for analysis from incident point data.\r\nCOUNT_INCIDENTS_WITHIN_FISHNET_POLYGONS\u2014A fishnet polygon mesh will overlay the incident point data  a...",
                        "default": None
                },
                "bounding_polygons_defining_where_incidents_are_possible": {
                        "type": "string",
                        "description": "A polygon feature class defining where the incident Input_Features could possibly occur.",
                        "default": None
                },
                "polygons_for_aggregating_incidents_into_counts": {
                        "type": "string",
                        "description": "The polygons to use to aggregate the incident Input_Features in order to get an incident count for each polygon feature.",
                        "default": None
                },
                "density_surface": {
                        "type": "string",
                        "description": "The Density_Surface parameter is disabled; it\r\nremains as a tool parameter only to support backwards\r\ncompatibility.\r\nThe Kernel Density tool can be used if you would like a density surface visualizat...",
                        "default": None
                },
                "cell_size": {
                        "type": "string",
                        "description": "The size of the grid cells used to aggregate the Input_Features.  When aggregating into a hexagon grid, this distance is used as the height to construct the hexagon polygons.",
                        "default": None
                },
                "distance_band": {
                        "type": "string",
                        "description": "The spatial extent of the analysis neighborhood.  This value determines which features are analyzed together in order to assess local clustering.",
                        "default": None
                }
        },
        "required": [
                "input_features",
                "output_features"
        ]
},
    "optimized_outlier_analysis": {
        "name": "optimized_outlier_analysis",
        "description": "Given incident points or weighted features (points or polygons), creates a map of statistically significant hot spots, cold spots, and spatial outliers using the Anselin Local Moran's I statistic. It evaluates the characteristics of the input feature class to produce optimal results. Learn more about how Optimized Outlier Analysis works",
        "parameters": {
                "input_features": {
                        "type": "string",
                        "description": "The point or polygon feature class for which the cluster and outlier analysis will be performed."
                },
                "output_features": {
                        "type": "string",
                        "description": "The output feature class to receive the result fields."
                },
                "analysis_field": {
                        "type": "string",
                        "description": "The numeric field (number of incidents, crime rates, test scores, and so on) to be evaluated.",
                        "default": None
                },
                "incident_data_aggregation_method": {
                        "type": "string",
                        "description": "The aggregation method to use to create weighted features for analysis from incident point data.\r\nCOUNT_INCIDENTS_WITHIN_FISHNET_POLYGONS\u2014A fishnet polygon mesh will overlay the incident point data  a...",
                        "default": None
                },
                "bounding_polygons_defining_where_incidents_are_possible": {
                        "type": "string",
                        "description": "A polygon feature class defining where the incident Input_Features could possibly occur.",
                        "default": None
                },
                "polygons_for_aggregating_incidents_into_counts": {
                        "type": "string",
                        "description": "The polygons to use to aggregate the incident Input_Features in order to get an incident count for each polygon feature.",
                        "default": None
                },
                "performance_adjustment": {
                        "type": "string",
                        "description": "This analysis utilizes permutations to create a reference distribution.  Choosing the number of permutations is a balance between precision and increased processing time. \r\nChoose your preference for ...",
                        "default": None
                },
                "cell_size": {
                        "type": "string",
                        "description": "The size of the grid cells used to aggregate the Input_Features.  When aggregating into a hexagon grid, this distance is used as the height to construct the hexagon polygons.",
                        "default": None
                },
                "distance_band": {
                        "type": "string",
                        "description": "The spatial extent of the analysis neighborhood.  This value determines which features are analyzed together in order to assess local clustering.",
                        "default": None
                }
        },
        "required": [
                "input_features",
                "output_features"
        ]
},
    "similarity_search": {
        "name": "similarity_search",
        "description": "Identifies which candidate features are most similar or most dissimilar to one or more input features based on feature attributes. Learn more about how Similarity Search works",
        "parameters": {
                "input_features_to_match": {
                        "type": "string",
                        "description": "The layer, or a selection on a layer, containing the features you want to match; you are searching for other features that look like these features.  When more than one feature is provided, matching i..."
                },
                "candidate_features": {
                        "type": "string",
                        "description": "The layer, or a selection on a layer, containing candidate matching features.  The tool will check for features most similar (or most dissimilar) to the Input_Features_To_Match values among these cand..."
                },
                "output_features": {
                        "type": "string",
                        "description": "The output feature class containing a record for each of the  Input_Features_To_Match values and for all the solution-matching features found."
                },
                "collapse_output_to_points": {
                        "type": "string",
                        "description": "Specifies whether the geometry for the Output_Features parameter will be collapsed to points or will match the original geometry (lines or polygons) of the input features if the Input_Features_To_Matc..."
                },
                "most_or_least_similar": {
                        "type": "string",
                        "description": "Specifies whether features that are most similar or most dissimilar to the Input_Features_To_Match values will be identified.MOST_SIMILAR\u2014Features that are most similar will be identified. This is the..."
                },
                "match_method": {
                        "type": "string",
                        "description": "Specifies whether matching will be based on values, ranks, or cosine relationships.ATTRIBUTE_VALUES\u2014Matching will be based on the sum of squared standardized attribute value differences for all of the..."
                },
                "number_of_results": {
                        "type": "string",
                        "description": "The number of solution matches to find.  Entering zero or a number larger than the total number of   Candidate_Features values will return rankings for all the candidate features. The default is 10."
                },
                "attributes_of_interest": {
                        "type": "string",
                        "description": "The numeric attributes representing the matching criteria."
                },
                "fields_to_append_to_output": {
                        "type": "string",
                        "description": "The fields to include with the Output_Features parameter. These fields are not used to determine similarity; they are only included in the  Output_Features parameter for reference.",
                        "default": None
                }
        },
        "required": [
                "input_features_to_match",
                "candidate_features",
                "output_features",
                "collapse_output_to_points",
                "most_or_least_similar",
                "match_method",
                "number_of_results",
                "attributes_of_interest"
        ]
},
    "spatial_outlier_detection": {
        "name": "spatial_outlier_detection",
        "description": "Identifies global or local spatial outliers in point features. A global outlier is a point that is far away from all other points in a feature class.   Global outliers are detected by examining distances between each point and one of its closest neighbors (by default, the closest neighbor) and detecting points where the distance is large. A local outlier is a point that is farther away from its neighbors than would be expected by the density of points in the surrounding area.  Local outliers are detected by calculating the local outlier factor (LOF) of each feature.  The LOF is a measure that describes how isolated a location is compared to its local neighbors. A higher LOF value indicates greater isolation. The tool can also be used to produce a raster prediction surface that can be used to estimate whether new features will be classified as outliers based on the spatial distribution of the data. Learn more about how Spatial Outlier Detection works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The point features that will be used to build the spatial outlier\r\ndetection model. Each point will be classified as an outlier or inlier based on its local outlier factor."
                },
                "output_features": {
                        "type": "string",
                        "description": "The output feature class containing the local outlier factor for each input feature as well as an indicator of whether the point is a spatial outlier."
                },
                "n_neighbors": {
                        "type": "string",
                        "description": "The number of neighbors that will be used to detect spatial outliers for each input point. For local outlier detection, the value must be at least 2, and all features within the neighborhood will be u...",
                        "default": None
                },
                "percent_outlier": {
                        "type": "string",
                        "description": "The percent of locations that will be identified as spatial outliers by defining the threshold of the local outlier factor.  If no value is specified, a value is estimated at run time and is displayed...",
                        "default": None
                },
                "output_raster": {
                        "type": "string",
                        "description": "The output raster containing the local\r\noutlier factors at each cell, which is calculated based on the spatial distribution of the input features. This parameter is only available with a Desktop Advan...",
                        "default": None
                },
                "outlier_type": {
                        "type": "string",
                        "description": "Specifies the type of outlier that will be detected. A global outlier is a point that is far away from all other points in the feature class.  A local outlier is a point that is farther away from its ...",
                        "default": None
                },
                "sensitivity": {
                        "type": "string",
                        "description": "Specifies the sensitivity level that will be used to detect global outliers. The higher the sensitivity, the more points that will be detected as outliers.The sensitivity value will determine the thre...",
                        "default": None
                },
                "keep_type": {
                        "type": "string",
                        "description": "Specifies whether the output features will contain all input features or only features identified as spatial outliers.KEEP_OUTLIER\u2014The output features will only contain features identified as spatial ...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "output_features"
        ]
},
    "spatially_constrained_multivariate_clustering": {
        "name": "spatially_constrained_multivariate_clustering",
        "description": "Finds spatially contiguous clusters of features based on a set of feature attribute values and optional cluster size limits. Learn more about how Spatially Constrained Multivariate Clustering works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The feature class or feature layer for which you want to create clusters."
                },
                "output_features": {
                        "type": "string",
                        "description": "The new output feature class created containing all features, the analysis fields specified, and a field indicating to which cluster each feature belongs."
                },
                "analysis_fields": {
                        "type": "string",
                        "description": "A list of fields that will be used to distinguish one cluster from another."
                },
                "size_constraints": {
                        "type": "string",
                        "description": "Specifies cluster size based on number of features per group or a target attribute value per group.NONE\u2014No cluster size constraints will be used.  This is the default.NUM_FEATURES\u2014A minimum and maximu...",
                        "default": None
                },
                "constraint_field": {
                        "type": "string",
                        "description": "The attribute value to be summed per cluster.",
                        "default": None
                },
                "min_constraint": {
                        "type": "string",
                        "description": "The minimum number of features per cluster or the minimum attribute value per cluster.\r\nThis must be a positive value.",
                        "default": None
                },
                "max_constraint": {
                        "type": "string",
                        "description": "The maximum number of features per cluster or the maximum attribute value per cluster.  If a maximum constraint is set, the number_of_clusters parameter is disabled.\r\nThis must be a positive value.",
                        "default": None
                },
                "number_of_clusters": {
                        "type": "string",
                        "description": "The number of clusters to create.  If this parameter is empty,  the tool will evaluate the optimal number of clusters by computing a pseudo F-statistic value for clustering solutions with 2 through 30...",
                        "default": None
                },
                "spatial_constraints": {
                        "type": "string",
                        "description": "Specifies how spatial relationships among features will be defined.CONTIGUITY_EDGES_ONLY\u2014Clusters will contain contiguous polygon features. Only polygons that share an edge can be part of the same clu...",
                        "default": None
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "The path to a file containing spatial weights that define spatial, and potentially temporal, relationships among features.",
                        "default": None
                },
                "number_of_permutations": {
                        "type": "string",
                        "description": "The number of random permutations \r\nfor the calculation of membership stability scores.  If 0 (zero) is chosen, probabilities will not be calculated. Calculating these probabilities uses permutations ...",
                        "default": None
                },
                "output_table": {
                        "type": "string",
                        "description": "The table created containing the results of the F-statistic values calculated to evaluate the optimal number of clusters.  The chart created from this table can be accessed in the  Contents pane under..."
                }
        },
        "required": [
                "in_features",
                "output_features",
                "analysis_fields",
                "output_table"
        ]
},
    "central_feature": {
        "name": "central_feature",
        "description": "Identifies the most centrally located feature in a point, line, or polygon feature class. Learn more about how Central Feature works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "The feature class containing a distribution of features from which to identify the most centrally located feature."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "The feature class that will contain the most centrally located feature in the Input Feature Class."
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies how distances are calculated from each feature to neighboring features.EUCLIDEAN_DISTANCE\u2014The straight-line distance between two points (as the crow flies) MANHATTAN_DISTANCE\u2014The distance be..."
                },
                "weight_field": {
                        "type": "string",
                        "description": "The numeric field used to weight distances in the origin-destination distance matrix.",
                        "default": None
                },
                "self_potential_weight_field": {
                        "type": "string",
                        "description": "The field representing self-potential\u2014the distance or weight between a feature and itself.",
                        "default": None
                },
                "case_field": {
                        "type": "string",
                        "description": "Field used to group features for separate central feature computations. The case field can be of integer, date, or string type.",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "output_feature_class",
                "distance_method"
        ]
},
    "decompose_spatial_structure": {
        "name": "decompose_spatial_structure",
        "description": "Decomposes a feature class and neighborhood into a set of spatial components. The components represent potential spatial patterns among the features, such as clusters or trends. The components are returned as fields of the output feature class and represent variables of the input features and neighborhood that have the strongest possible spatial clustering (spatial autocorrelation).  The components are called Moran eigenvectors, and each component represents a different spatial pattern that are each independent of each other. Learn more about Moran eigenvectors",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The point or polygon features that will be used to create the spatial components."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output feature class that will contain the spatial components as fields. The number of fields created depends on the min_autocorrelation and max_components parameter values."
                },
                "append_all_fields": {
                        "type": "string",
                        "description": "Specifies whether all fields will be copied from the input features to the output feature class.ALL\u2014 All fields from the input features will be copied to the output feature class. This is the default....",
                        "default": None
                },
                "min_autocorrelation": {
                        "type": "string",
                        "description": "The threshold value for including a spatial component.  The value is a proportion of the largest possible Moran's I value for the spatial weights, and a component must have a larger Moran's I value th...",
                        "default": None
                },
                "max_components": {
                        "type": "string",
                        "description": "The maximum number of spatial components that will be created. The default is 15.",
                        "default": None
                },
                "neighborhood_type": {
                        "type": "string",
                        "description": "Specifies how neighbors will be chosen for each input feature.  Neighboring features must be identified in order to decompose the spatial structure of the input features. \r\nDISTANCE_BAND\u2014Features with...",
                        "default": None
                },
                "distance_band": {
                        "type": "string",
                        "description": "The distance within which features will be included as neighbors. If no value is provided, one will be estimated during processing and included as a geoprocessing message. If the specified distance re...",
                        "default": None
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "The number of neighbors that will be included for each feature. The number does not include the focal feature. The default is 8.",
                        "default": None
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "The path and file name of the spatial weights matrix file (.swm) that defines the neighbors and weights between the input features.",
                        "default": None
                },
                "local_weighting_scheme": {
                        "type": "string",
                        "description": "Specifies the weighting scheme that will be applied to neighboring features.  \r\nUNWEIGHTED\u2014Neighbors will not be weighted.  This is the default.BISQUARE\u2014Neighbors will be weighted using a bisquare ker...",
                        "default": None
                },
                "kernel_bandwidth": {
                        "type": "string",
                        "description": "The bandwidth of the bisquare or Gaussian local weighting schemes. If no value is provided, one will be estimated during processing and included as a geoprocessing message.",
                        "default": None
                },
                "out_swm": {
                        "type": "string",
                        "description": "The output spatial weights matrix file (.swm) of the neighbors and weights of all pairs of features.  If created, this file can be reused in tools that allow defining neighbors and weights with spatia...",
                        "default": None
                },
                "id_field": {
                        "type": "string",
                        "description": "The unique ID field of the output spatial weights matrix file. The field must be an integer and must have a unique value for each input feature.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_features"
        ]
},
    "directional_distribution": {
        "name": "directional_distribution",
        "description": "Creates standard deviational ellipses or ellipsoids to summarize the spatial characteristics of geographic features: central tendency, dispersion, and directional trends. Learn how Directional Distribution (Standard Deviational Ellipse) works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "A feature class containing a distribution of features for which the standard deviational ellipse or ellipsoid will be calculated."
                },
                "output_ellipse_feature_class": {
                        "type": "string",
                        "description": "A polygon feature class that will contain the output ellipse feature."
                },
                "ellipse_size": {
                        "type": "string",
                        "description": "Specifies the size of the output ellipses in standard deviations.1_STANDARD_DEVIATION\u2014The size of the output ellipses will be one standard deviation. This is the default.2_STANDARD_DEVIATIONS\u2014The size..."
                },
                "weight_field": {
                        "type": "string",
                        "description": "The numeric field that will be used to weight locations according to their relative importance.",
                        "default": None
                },
                "case_field": {
                        "type": "string",
                        "description": "The field that will be used to group features for separate directional distribution calculations. The case field can be of integer, date, or string type.",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "output_ellipse_feature_class",
                "ellipse_size"
        ]
},
    "directional_trend": {
        "name": "directional_trend",
        "description": "Creates a scatter plot chart on a feature layer displaying the trend of data values in a particular direction.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature layer that will be used to calculate the directional trend. \r\nThe input must be point or polygon features. For polygons, the centroids of the polygons will be used to create the char..."
                },
                "analysis_field": {
                        "type": "string",
                        "description": "The numeric field from the input feature layer that will be used to calculate the directional trend."
                },
                "direction": {
                        "type": "string",
                        "description": "The direction of the trend.  Provide the value as degrees clockwise from north. For example, 0 corresponds to north, 90 to east, 180 to south, and 270 to west.  The value must be between 0 and 360.  T...",
                        "default": None
                },
                "determine_direction": {
                        "type": "string",
                        "description": "Specifies whether the direction of the strongest trend will be determined by the tool. The direction of strongest trend is determined by finding the direction that maximizes the R-squared value for th...",
                        "default": None
                },
                "order": {
                        "type": "string",
                        "description": "Specifies the order of the polynomial that will be fitted to the data values.1\u2014First order (linear) polynomial will be used.2\u2014Second order (quadratic) polynomial will be used.3\u2014Third order (cubic) pol...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "analysis_field"
        ]
},
    "linear_directional_mean": {
        "name": "linear_directional_mean",
        "description": "Identifies the mean direction, length, and geographic center for a set of lines. Learn more about how Linear Directional Mean works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "The feature class containing vectors for which the mean direction will be calculated."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "A line feature class that will contain the features representing the mean directions of the input feature class."
                },
                "orientation_only": {
                        "type": "string",
                        "description": "Specifies whether to include direction (From and To nodes) information in the analysis.\r\nDIRECTION\u2014The From and To nodes are utilized in calculating the mean. This is the default.ORIENTATION_ONLY\u2014The ..."
                },
                "case_field": {
                        "type": "string",
                        "description": "Field used to group features for separate directional mean calculations. The case field can be of integer, date, or string type.",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "output_feature_class",
                "orientation_only"
        ]
},
    "mean_center": {
        "name": "mean_center",
        "description": "Identifies the geographic center (or the center of concentration) for a set of features. Learn more about how Mean Center works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "A feature class for which the mean center will be calculated."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "A point feature class that will contain the features representing the mean centers of the input feature class."
                },
                "weight_field": {
                        "type": "string",
                        "description": "The numeric field used to create a weighted mean center.",
                        "default": None
                },
                "case_field": {
                        "type": "string",
                        "description": "Field used to group features for separate mean center calculations. The case field can be of integer, date, or string type.",
                        "default": None
                },
                "dimension_field": {
                        "type": "string",
                        "description": "A numeric field containing attribute values from which an average value will be calculated.",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "output_feature_class"
        ]
},
    "median_center": {
        "name": "median_center",
        "description": "Identifies the location that minimizes overall Euclidean distance to the features in a dataset. Learn more about how Median Center works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "A feature class for which the median center will be calculated."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "A point feature class that will contain the features representing the median centers of the input feature class."
                },
                "weight_field": {
                        "type": "string",
                        "description": "The numeric field used to create a weighted median center.",
                        "default": None
                },
                "case_field": {
                        "type": "string",
                        "description": "Field used to group features for separate median center calculations. The case field can be of integer, date, or string type.",
                        "default": None
                },
                "attribute_field": {
                        "type": "string",
                        "description": "Numeric field(s) for which the data median value will be computed."
                }
        },
        "required": [
                "input_feature_class",
                "output_feature_class",
                "attribute_field"
        ]
},
    "neighborhood_summary_statistics": {
        "name": "neighborhood_summary_statistics",
        "description": "Calculates summary  statistics of one or more numeric fields using local neighborhoods around each feature.  The local statistics include mean (average), median, standard deviation, interquartile range, skewness, and quantile imbalance. All statistics can be geographically weighted using kernels to give more influence to neighbors closer to the focal feature.  Various neighborhood types can be used, including distance band, number of neighbors, polygon contiguity, Delaunay triangulation, and spatial weights matrix files (.swm). Summary statistics are also calculated for the distances to the neighbors of each feature. Learn more about how Neighborhood Summary Statistics works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The point or polygon features that will be used to calculate the local statistics."
                },
                "output_features": {
                        "type": "string",
                        "description": "The output feature class containing the local statistics as fields. Each statistic of each analysis field will be stored as an individual field."
                },
                "analysis_fields": {
                        "type": "string",
                        "description": "One or more fields that will be used to calculate local statistics. If no analysis fields are provided, only local statistics based on distances to neighbors will be calculated.",
                        "default": None
                },
                "local_summary_statistic": {
                        "type": "string",
                        "description": "Specifies the local summary statistic that will be calculated for each analysis field.\r\nALL\u2014All local statistics will be calculated.  This is the default.MEAN\u2014The local mean (average) will be calculat...",
                        "default": None
                },
                "include_focal_feature": {
                        "type": "string",
                        "description": "Specifies whether the focal feature will be included when calculating local statistics for each feature.INCLUDE_FOCAL\u2014The focal feature and all of its neighbors will be included when calculating local...",
                        "default": None
                },
                "ignore_Nones": {
                        "type": "string",
                        "description": "Specifies whether None values in the analysis fields will be included or ignored in the calculations.IGNORE_NULLS\u2014Null values will be ignored in the local calculations.INCLUDE_NULLS\u2014Null values will b...",
                        "default": None
                },
                "neighborhood_type": {
                        "type": "string",
                        "description": "Specifies which features will be included as neighbors.  To calculate local statistics, neighboring features must be identified for each input feature, and these neighbors are used to calculate the lo...",
                        "default": None
                },
                "distance_band": {
                        "type": "string",
                        "description": "All features within this distance will be included as neighbors. If no value is provided, one will be estimated during processing and included as a geoprocessing message.\r\nIf the specified distance re...",
                        "default": None
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "The number of neighbors that will be included for each local calculation. The number does not include the focal feature. If the focal feature is included in calculations, one additional neighbor will ...",
                        "default": None
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "The path and file name of the spatial weights matrix file that defines spatial, and potentially temporal, relationships among\r\nfeatures.",
                        "default": None
                },
                "local_weighting_scheme": {
                        "type": "string",
                        "description": "Specifies the weighting scheme that will be applied to neighbors when calculating local statistics.  \r\nUNWEIGHTED\u2014Neighbors will not be weighted.  This is the default.BISQUARE\u2014Neighbors will be weight...",
                        "default": None
                },
                "kernel_bandwidth": {
                        "type": "string",
                        "description": "The bandwidth of the bisquare or Gaussian local weighting schemes. If no value is provided, one will be estimated during processing and included as a geoprocessing message.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "output_features"
        ]
},
    "standard_distance": {
        "name": "standard_distance",
        "description": "Measures the degree to which features are concentrated or dispersed around the geometric mean center. Learn more about how Standard Distance works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "A feature class containing a distribution of features for which the standard distance will be calculated."
                },
                "output_standard_distance_feature_class": {
                        "type": "string",
                        "description": "A polygon feature class that will contain a circle polygon for each input center. These circle polygons graphically portray the standard distance at each center point."
                },
                "circle_size": {
                        "type": "string",
                        "description": "Specifies the size of output circles in standard deviations.1_STANDARD_DEVIATION\u2014The output circles will be 1 standard deviation. This is the default.2_STANDARD_DEVIATIONS\u2014The output circles will be 2..."
                },
                "weight_field": {
                        "type": "string",
                        "description": "The numeric field used to weight locations according to their relative importance.",
                        "default": None
                },
                "case_field": {
                        "type": "string",
                        "description": "The field used to group features for separate standard distance calculations. The case field can be of integer, date, or string type.",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "output_standard_distance_feature_class",
                "circle_size"
        ]
},
    "bivariate_spatial_association_(lee's_l)": {
        "name": "bivariate_spatial_association_(lee's_l)",
        "description": "Calculates the spatial association between two continuous variables using the Lee's L statistic. The Lee's L statistic characterizes both the degree of correlation and the degree of copatterning (similarity of spatial clustering) between the variables.  The value will be between -1 and 1 and is conceptually similar to a correlation coefficient but is adjusted to account for spatial autocorrelation of the two variables. Lee's L values close to 1 indicate that the variables are highly positively correlated and that each variable has high spatial autocorrelation (high and low values of the variables each tend to cluster together).  Values close to -1 indicate that the variables are highly negatively correlated and that each variable has highly positive spatial autocorrelation.  Values close to 0 indicate that the variables are uncorrelated, not spatially autocorrelated, or both. The Lee's L statistic can be partitioned to each input feature, called local Lee's L statistics, that show the local spatial association of the feature and its neighbors.  This can be used to determine areas that have higher or lower spatial association than the global Lee's L statistic. The local statistics can also be classified into one of several categories based on the values of the neighbors of each feature.  Both the global and local statistics are tested for statistical significance using permutations. Learn more about how Bivariate Spatial Association (Lee's L) works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features containing the fields of the two analysis variables."
                },
                "analysis_field1": {
                        "type": "string",
                        "description": "The field of the first analysis variable.\r\nThe field must be numeric."
                },
                "analysis_field2": {
                        "type": "string",
                        "description": "The field of the second analysis variable.  The field must be numeric."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output features\r\ncontaining the local Lee's L statistics, spatial association categories, p-values, and the weighted averages of the neighbors of each feature."
                },
                "neighborhood_type": {
                        "type": "string",
                        "description": "Specifies how neighbors of each feature will be determined. The feature is always included in the neighborhood, and all neighborhood weights are normalized to sum to 1.DISTANCE_BAND\u2014Features within a ...",
                        "default": None
                },
                "distance_band": {
                        "type": "string",
                        "description": "The distance band that will be used to determine neighbors around the focal feature. If no value is provided, the distance will be the shortest distance such that each feature has at least one other n...",
                        "default": None
                },
                "num_neighbors": {
                        "type": "string",
                        "description": "The number of neighbors around each feature that will be included as neighbors.  The value does not include the feature.  For example, specifying 6 will use the feature and its six closest neighbors (...",
                        "default": None
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "The path and file name of the spatial weights matrix file that defines the neighbors and weights between\r\nfeatures.",
                        "default": None
                },
                "local_weighting_scheme": {
                        "type": "string",
                        "description": "Specifies the weighting scheme that will be applied to neighbors when calculating spatial associations.  \r\nUNWEIGHTED\u2014Neighbors will not be weighted.  This is the default.BISQUARE\u2014Neighbors will be we...",
                        "default": None
                },
                "kernel_bandwidth": {
                        "type": "string",
                        "description": "The bandwidth for the bisquare kernel.  The bandwidth defines how quickly the weights decrease with distance.  Larger bandwidths will provide comparatively larger weights to neighbors that are farther...",
                        "default": None
                },
                "num_permutations": {
                        "type": "string",
                        "description": "Specifies the number of permutations that will be used to create reference distributions when calculating global and local p-values. All p-values are calculated using two-sided hypothesis tests.99\u2014The...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "analysis_field1",
                "analysis_field2",
                "out_features"
        ]
},
    "causal_inference_analysis": {
        "name": "causal_inference_analysis",
        "description": "Estimates the causal effect of a continuous exposure variable on a continuous outcome variable by approximating a randomized experiment and controlling for confounding variables. In statistical experiments, the cause-and-effect relationship between an exposure variable (such as the dose of a drug) and an outcome variable (such as a health outcome) is determined by randomly assigning each participant a particular exposure level so that any differences in the outcomes must be due only to the differences in the exposures and not any other attributes of the participants, such as age, preexisting conditions, and healthcare access. However, it is frequently impossible or unethical to perform controlled experiments, so relationships are often established through observational studies. For example, to study the effect of pollution on depression rates, you cannot intentionally expose individuals to high pollution to see the effect on depression. Instead, you can only observe the exposure to pollution and the depression rates of the individuals in your sample. However, because there are many variables (called confounding variables) that impact both pollution and depression, the causal effect cannot be directly estimated without controlling for these variables. To emulate the process of a randomized, controlled experiment, the tool calculates propensity scores for each observation, and the propensity scores are used to weight the observations in such a way that the causal relationship between the exposure and outcome variables is maintained, but correlations between the confounding variables and the exposure variable are removed. This weighted dataset is often called a pseudopopulation, and it has analogous properties to a controlled experiment in which each participant is randomly assigned an exposure. Using the weighted observations, the tool creates an exposure-response function (ERF) that estimates what the average outcome would be if all members of the population received a given exposure value but did not change their confounding variables. Learn more about how Causal Inference Analysis works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features or table containing fields of the exposure, outcome, and confounding variables."
                },
                "outcome_field": {
                        "type": "string",
                        "description": "The numeric field of the outcome variable.\r\nThis is the variable that responds to changes in the exposure variable. The outcome variable must be continuous or binary (not categorical)."
                },
                "exposure_field": {
                        "type": "string",
                        "description": "The numeric field of the exposure variable (sometimes called the treatment variable).\r\nThis is the variable that causes changes in the outcome variable. The exposure variable must be continuous (not b..."
                },
                "confounding_variablesvar1_cat1_var2_cat2": {
                        "type": "string",
                        "description": "The fields of the confounding variables. These are the variables that are related to both the exposure and outcome variables, and they must be balanced in order to estimate the causal effect between t..."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output features or table containing the propensity scores, balancing weights, and a field indicating whether the feature was trimmed (excluded from the analysis). The exposure, outcome, and confou..."
                },
                "ps_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used for calculating the propensity scores of each observation. The propensity score of an observation is the likelihood (or probability) of receiving the observed ex...",
                        "default": None
                },
                "balancing_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used for balancing the confounding variables. Each method estimates a set of balancing weights that removes the correlation between the confounding variables and the ...",
                        "default": None
                },
                "enable_erf_popups": {
                        "type": "string",
                        "description": "Specifies whether pop-up charts that display the local ERF for the observation will be created for each observation.CREATE_POPUP\u2014Local ERF pop-up charts will be created on the output features or table...",
                        "default": None
                },
                "out_erf_table": {
                        "type": "string",
                        "description": "A table containing values of the exposure-response function.\r\nThe table will contain 200 evenly spaced exposure values between the minimum and maximum exposure (after trimming) along with the estimate...",
                        "default": None
                },
                "target_outcomes": {
                        "type": "string",
                        "description": "A list of target outcome values from which required changes in exposure to achieve the outcomes will be calculated for each observation. \r\nFor example, if the exposure variable is an air quality index...",
                        "default": None
                },
                "target_exposures": {
                        "type": "string",
                        "description": "A list of target exposure values that will be used to calculate new outcomes for each observation. For each target exposure value, the tool estimates the new outcome value that the observation would r...",
                        "default": None
                },
                "lower_exp_trim": {
                        "type": "string",
                        "description": "The lower quantile that will be used to trim the exposure variable. Any observations with exposure values below this quantile will be excluded from the analysis before estimating propensity scores. Th...",
                        "default": None
                },
                "upper_exp_trim": {
                        "type": "string",
                        "description": "The upper quantile that will be used to trim the exposure variable. Any observations with exposure values above this quantile will be excluded from the analysis before estimating propensity scores. Th...",
                        "default": None
                },
                "lower_ps_trim": {
                        "type": "string",
                        "description": "The lower quantile that will be used to trim the propensity scores. Any observations with propensity scores below this quantile will be excluded from the analysis before performing propensity score ma...",
                        "default": None
                },
                "upper_ps_trim": {
                        "type": "string",
                        "description": "The upper quantile that will be used to trim the propensity scores. Any observations with propensity scores above this quantile will be excluded from the analysis before performing propensity score ma...",
                        "default": None
                },
                "num_bins": {
                        "type": "string",
                        "description": "The number of exposure bins that will be used for propensity score matching. In matching, the exposure variable is divided into evenly spaced bins (equal intervals), and matching is performed within e...",
                        "default": None
                },
                "scale": {
                        "type": "string",
                        "description": "The relative weight (sometimes called the scale) of the propensity score to the exposure variable that will be used when performing propensity score matching. Within each exposure bin, matches are det...",
                        "default": None
                },
                "balance_type": {
                        "type": "string",
                        "description": "Specifies the method that will be used to determine whether the confounding variables are balanced. After estimating weights with propensity score matching or inverse propensity score weighting, weigh...",
                        "default": None
                },
                "balance_threshold": {
                        "type": "string",
                        "description": "The threshold value that will be compared to the weighted correlations of the confounding variables to determine if they are balanced. The value must be between 0 and 1. A larger balance threshold ind...",
                        "default": None
                },
                "bw_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to estimate the bandwidth of the exposure-response function.\r\nPLUG_IN\u2014A plug-in method will be used to estimate the bandwidth. This is the default.CV\u2014The bandwid...",
                        "default": None
                },
                "bandwidth": {
                        "type": "string",
                        "description": "The bandwidth value of the exposure-response function when using a manual bandwidth.",
                        "default": None
                },
                "create_bootstrap_ci": {
                        "type": "string",
                        "description": "Specifies whether 95 percent confidence intervals for the exposure-response function will be created using M-out-of-N bootstrapping.CREATE_CI\u2014Confidence intervals for the exposure-response function wi...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "outcome_field",
                "exposure_field",
                "confounding_variablesvar1_cat1_var2_cat2",
                "out_features"
        ]
},
    "colocation_analysis": {
        "name": "colocation_analysis",
        "description": "Measures local patterns of spatial association, or colocation, between two categories of point features using the colocation quotient statistic. Learn more about how Colocation Analysis works",
        "parameters": {
                "input_type": {
                        "type": "string",
                        "description": "Specifies whether the in_features_of_interest  parameter values will come from the same dataset with specified categories, different datasets with specified categories, or different datasets that will..."
                },
                "in_features_of_interest": {
                        "type": "string",
                        "description": "The feature class containing points with representative categories."
                },
                "output_features": {
                        "type": "string",
                        "description": "The output feature class containing all the in_features parameter values with fields representing the local colocation quotient scores and p-values."
                },
                "field_of_interest": {
                        "type": "string",
                        "description": "The field containing the category or categories  to be analyzed.",
                        "default": None
                },
                "time_field_of_interest": {
                        "type": "string",
                        "description": "A date field with an optional  time stamp for each feature to analyze points using a space-time window.  Features near each other in space and time will be considered neighbors and will be  analyzed t...",
                        "default": None
                },
                "category_of_interest": {
                        "type": "string",
                        "description": "The base category for the analysis.  The tool will identify, for each category_of_interest value, the degree to which the base category is attracted to or colocated with the neighboring_category param...",
                        "default": None
                },
                "input_feature_for_comparison": {
                        "type": "string",
                        "description": "The input feature class containing the points with the categories that will be compared.",
                        "default": None
                },
                "field_for_comparison": {
                        "type": "string",
                        "description": "The field from the input_feature_for_comparison parameter containing the category to be compared.",
                        "default": None
                },
                "time_field_for_comparison": {
                        "type": "string",
                        "description": "A date field with a time stamp for each feature to analyze your points using a space-time window.  Features near each other in space and time will be considered neighbors and will be  analyzed togethe...",
                        "default": None
                },
                "category_for_comparison": {
                        "type": "string",
                        "description": "The neighboring category for the analysis.  The tool will identify the degree to which the category_of_interest parameter value is attracted to or isolated from the  category_for_comparison value.",
                        "default": None
                },
                "neighborhood_type": {
                        "type": "string",
                        "description": "Specifies how the spatial relationships among features will be defined.DISTANCE_BAND\u2014Each feature will be analyzed within the context of neighboring features. Neighboring features inside the specified..."
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "The number of neighbors around each feature that will be used to test for local relationships between categories.  If no value is provided, the default of 8 is used.  The provided value must be large ...",
                        "default": None
                },
                "distance_band": {
                        "type": "string",
                        "description": "The neighborhood size is a constant or fixed distance for each feature.  All features within this distance will be used to test for local relationships between categories.  If no value is provided, th...",
                        "default": None
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "The path to a file containing weights that define spatial, and potentially temporal, relationships among features.",
                        "default": None
                },
                "temporal_relationship_type": {
                        "type": "string",
                        "description": "Specifies how temporal relationships among features will be defined.\r\nBEFORE\u2014The time window will extend back in time for each of the in_features_of_interest values.  Neighboring features must have a ...",
                        "default": None
                },
                "time_step_interval": {
                        "type": "string",
                        "description": "An integer and unit of measurement representing the number of time units composing the time window.",
                        "default": None
                },
                "number_of_permutations": {
                        "type": "string",
                        "description": "The number of permutations that will be used to create a reference distribution. Choosing the number of permutations is a balance between precision and increased processing time. Choose your preferenc...",
                        "default": None
                },
                "local_weighting_scheme": {
                        "type": "string",
                        "description": "Specifies the kernel type that will be used to provide the spatial weighting. The kernel defines how each feature is related to other features within its neighborhood.BISQUARE\u2014Features will be weighte...",
                        "default": None
                },
                "output_table": {
                        "type": "string",
                        "description": "A table that includes the global colocation quotients between all the categories in the \r\nField of Interest parameter and all the categories in the Field Containing Neighboring Category parameter.  Th...",
                        "default": None
                }
        },
        "required": [
                "input_type",
                "in_features_of_interest",
                "output_features",
                "neighborhood_type"
        ]
},
    "estimate_time_to_event": {
        "name": "estimate_time_to_event",
        "description": "Predicts the time until an event occurs based on the prior times to the event. Explanatory variables can be used to improve the predictions, and the tool can determine which variables increase or decrease the time until the event. Learn more about how Estimate Time to Event works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features or table containing fields of the age, explanatory variables, and event indicator for each observation."
                },
                "age_field": {
                        "type": "string",
                        "description": "The numeric field of the age of the observation. This is often the age of the observation, but in general, it is the amount of time starting from the first moment the event could have occurred and end..."
                },
                "event_field": {
                        "type": "string",
                        "description": "The field containing an indicator or whether the event has occurred for the observation. The field must only contain the values 0 or 1. A value of 0 indicates that the event has not occurred (a censor..."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output features or table containing the predicted times to the event for observations in which the event has not occurred."
                },
                "explanatory_variablesvariable_categorical": {
                        "type": "string",
                        "description": "A list of fields representing the explanatory variables that help predict the time to the event. Specify the variable as CATEGORICAL if it represents classes or categories such as material type or inc...",
                        "default": None
                },
                "enable_survival_curve_popups": {
                        "type": "string",
                        "description": "Specifies whether pop-up charts will be generated for each output record. The pop-up charts show the baseline survival curve for each record and an additional time-to-event curve for censored observat...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "age_field",
                "event_field",
                "out_features"
        ]
},
    "exploratory_regression": {
        "name": "exploratory_regression",
        "description": "Evaluates all possible combinations of the input candidate explanatory variables, looking for OLS models that best explain the dependent variable within the context of user-specified criteria. Learn more about how Exploratory Regression works",
        "parameters": {
                "input_features": {
                        "type": "string",
                        "description": "The feature class or feature layer containing the dependent and candidate explanatory variables to analyze."
                },
                "dependent_variable": {
                        "type": "string",
                        "description": "The numeric field containing the observed values you want to model using OLS."
                },
                "candidate_explanatory_variables": {
                        "type": "string",
                        "description": "A list of fields to try as OLS model explanatory variables."
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "A file containing spatial weights that define the spatial relationships among your input features.  This file is used to assess spatial autocorrelation among regression residuals.  You can use the Gen...",
                        "default": None
                },
                "output_report_file": {
                        "type": "string",
                        "description": "The report file contains tool results, including details about any models found that passed all the search criteria you entered.  This output file also contains diagnostics to help you fix common regr...",
                        "default": None
                },
                "output_results_table": {
                        "type": "string",
                        "description": "The optional output table created containing the explanatory variables and diagnostics for all of the models within the Coefficient p-value \r\nand VIF value cutoffs.",
                        "default": None
                },
                "maximum_number_of_explanatory_variables": {
                        "type": "string",
                        "description": "All models with explanatory variables up to the value entered here will be assessed.  If, for example, the Minimum_Number_of_Explanatory_Variables is 2 and the Maximum_Number_of_Explanatory_Variables ...",
                        "default": None
                },
                "minimum_number_of_explanatory_variables": {
                        "type": "string",
                        "description": "This value represents the minimum number of explanatory variables for models evaluated.  If, for example, the Minimum_Number_of_Explanatory_Variables is 2 and the Maximum_Number_of_Explanatory_Variabl...",
                        "default": None
                },
                "minimum_acceptable_adj_r_squared": {
                        "type": "string",
                        "description": "This is the lowest Adjusted R-Squared value you consider a passing model.  If a model passes all of your other search criteria, but has an Adjusted R-Squared value smaller than the value entered here,...",
                        "default": None
                },
                "maximum_coefficient_p_value_cutoff": {
                        "type": "string",
                        "description": "For each model evaluated, OLS computes explanatory variable coefficient p-values.  The cutoff p-value you enter here represents the confidence level you require for all coefficients in the model in or...",
                        "default": None
                },
                "maximum_vif_value_cutoff": {
                        "type": "string",
                        "description": "This value reflects how much redundancy (multicollinearity) among model explanatory variables you will tolerate.  \r\n When the VIF (Variance Inflation Factor) value is higher than about 7.5, multicolli...",
                        "default": None
                },
                "minimum_acceptable_jarque_bera_p_value": {
                        "type": "string",
                        "description": "The p-value returned by the Jarque-Bera diagnostic test indicates whether the model residuals are normally distributed.  If the p-value is statistically significant (small),   \r\nthe model residuals ar...",
                        "default": None
                },
                "minimum_acceptable_spatial_autocorrelation_p_value": {
                        "type": "string",
                        "description": "For models that pass all of the other search criteria, the Exploratory Regression tool will check model residuals for spatial clustering using Global Moran's I.\r\n When the p-value for this diagnostic ...",
                        "default": None
                }
        },
        "required": [
                "input_features",
                "dependent_variable",
                "candidate_explanatory_variables"
        ]
},
    "ols": {
        "name": "ols",
        "description": "Performs global Ordinary Least Squares (OLS) linear regression to generate predictions or to model a dependent variable in terms of its relationships to a set of explanatory variables. The functionality of this tool is included in the Generalized Linear Regression tool added at ArcGIS Pro 2.3.  The Generalized Linear Regression tool supports additional models.",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "The feature class containing the dependent and independent variables for analysis."
                },
                "unique_id_field": {
                        "type": "string",
                        "description": "An integer field containing a different value for every feature in the Input Feature Class."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will receive dependent variable estimates and residuals."
                },
                "dependent_variable": {
                        "type": "string",
                        "description": "The numeric field containing values for what you are trying to model."
                },
                "explanatory_variables": {
                        "type": "string",
                        "description": "A list of fields representing explanatory variables in your regression model."
                },
                "coefficient_output_table": {
                        "type": "string",
                        "description": "The full path to an optional table that will receive model coefficients, standardized coefficients, standard errors, and probabilities for each explanatory variable.",
                        "default": None
                },
                "diagnostic_output_table": {
                        "type": "string",
                        "description": "The full path to an optional table that will receive model summary diagnostics.",
                        "default": None
                },
                "output_report_file": {
                        "type": "string",
                        "description": "The path to the optional PDF file \r\nthe tool will create.  This report file includes model diagnostics, graphs, and notes to help you interpret the OLS results.",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "unique_id_field",
                "output_feature_class",
                "dependent_variable",
                "explanatory_variables"
        ]
},
    "forest_based_and_boosted_classification_and_regression": {
        "name": "forest_based_and_boosted_classification_and_regression",
        "description": "Creates models and generates predictions using one of two supervised machine learning methods: an adaptation of the random forest algorithm developed by Leo Breiman and Adele Cutler or the Extreme Gradient Boosting (XGBoost) algorithm developed by Tianqi Chen and Carlos Guestrin. Predictions can be performed for both categorical variables (classification) and continuous variables (regression). Explanatory variables can take the form of fields in the attribute table of the training features, raster datasets, and distance features used to calculate proximity values for use as additional variables. In addition to validation of model performance based on the training data, predictions can be made to either features or a prediction raster. Learn more about how Forest-based and Boosted Classification and Regression works",
        "parameters": {
                "prediction_type": {
                        "type": "string",
                        "description": "Specifies the \r\noperation mode that will be used. The tool can be run to train a model to only assess performance, predict features, or create a prediction surface.TRAIN\u2014A model will be trained, but n..."
                },
                "in_features": {
                        "type": "string",
                        "description": "The feature class containing the variable_predict parameter value and, optionally, the explanatory training variables from fields."
                },
                "variable_predict": {
                        "type": "string",
                        "description": "The variable from the in_features parameter value containing the values to be used to train the model. This field contains known (training) values of the variable that will be used to predict at unkno...",
                        "default": None
                },
                "treat_variable_as_categorical": {
                        "type": "string",
                        "description": "CATEGORICAL\u2014The variable_predict value is a categorical variable and classification will be performed.NUMERIC\u2014The variable_predict value is continuous and regression will be performed. This is the def...",
                        "default": None
                },
                "explanatory_variablesvariable_categorical": {
                        "type": "string",
                        "description": "A list of fields representing the explanatory variables that help predict the value or category of the variable_predict value. Use the treat_variable_as_categorical parameter for any variables that re...",
                        "default": None
                },
                "distance_features": {
                        "type": "string",
                        "description": "The explanatory training distance features. Explanatory variables will be automatically created by calculating a distance from the provided features to the in_features values. Distances will be calcul...",
                        "default": None
                },
                "explanatory_rastersvariable_categorical": {
                        "type": "string",
                        "description": "The explanatory training variables extracted from rasters. Explanatory training variables will be automatically created by extracting raster cell values. For each feature in the in_features parameter,...",
                        "default": None
                },
                "features_to_predict": {
                        "type": "string",
                        "description": "A feature class representing the locations where predictions will be made. This feature class must also contain any explanatory variables provided as fields that correspond to those used from the trai...",
                        "default": None
                },
                "output_features": {
                        "type": "string",
                        "description": "The output feature class containing the prediction results.",
                        "default": None
                },
                "output_raster": {
                        "type": "string",
                        "description": "The output raster containing the prediction results. The default cell size will be the maximum cell size of the raster inputs. To set a different cell size, use the Cell Size environment setting.",
                        "default": None
                },
                "explanatory_variable_matchingprediction_training": {
                        "type": "string",
                        "description": "A list of the explanatory_variables values specified from the in_features parameter on the right and corresponding fields from the features_to_predict parameter on the left,\r\nfor example, [[\"LandCover...",
                        "default": None
                },
                "explanatory_distance_matchingprediction_training": {
                        "type": "string",
                        "description": "A list of the distance_features values specified for the in_features parameter on the right and  corresponding feature sets from the features_to_predict parameter on the left. explanatory_distance_fea...",
                        "default": None
                },
                "explanatory_rasters_matchingprediction_training": {
                        "type": "string",
                        "description": "A list of the explanatory_rasters values specified for the in_features on the right and corresponding rasters from the features_to_predict parameter or output_raster parameter to be created on the lef...",
                        "default": None
                },
                "output_trained_features": {
                        "type": "string",
                        "description": "The explanatory variables used for training (including sampled raster values and distance calculations), as well as the observed variable_predict field and accompanying predictions that will be used t...",
                        "default": None
                },
                "output_importance_table": {
                        "type": "string",
                        "description": "The table that will contain information describing the importance of each explanatory variable (fields, distance features, and rasters) used to create the model.",
                        "default": None
                },
                "use_raster_values": {
                        "type": "string",
                        "description": "Specifies how polygons will be treated when training the model\r\nif the in_features values are polygons with a categorical variable_predict value and only explanatory_rasters values have been provided....",
                        "default": None
                },
                "number_of_trees": {
                        "type": "string",
                        "description": "The number of trees that will be created in the Forest-based and Gradient Boosted models. The default is 100. If the model_type parameter value is FOREST-BASED, more trees will generally result in mor...",
                        "default": None
                },
                "minimum_leaf_size": {
                        "type": "string",
                        "description": "The minimum number of observations required to keep a leaf (that is, the terminal node on a tree without further splits). \r\nThe default minimum for regression is 5 and the default for classification i...",
                        "default": None
                },
                "maximum_depth": {
                        "type": "string",
                        "description": "The maximum number of splits that will be made down a tree. Using a large maximum depth, more splits will be created, which may increase the chances of overfitting the model. If the model_type paramet...",
                        "default": None
                },
                "sample_size": {
                        "type": "string",
                        "description": "The percentage of the in_features values that will be used for each decision tree. The default is 100 percent of the data. Samples for each tree are taken randomly from two-thirds of the data specifie...",
                        "default": None
                },
                "random_variables": {
                        "type": "string",
                        "description": "The number of explanatory variables that will be used to create each decision tree.Each decision tree in the forest is created using a random subset of the specified explanatory variables. Increasing ...",
                        "default": None
                },
                "percentage_for_training": {
                        "type": "string",
                        "description": "The percentage (between 10 percent and 50 percent) of \r\nthe in_features values that will be reserved as the test dataset for validation. The model will be trained without this random subset of data, a...",
                        "default": None
                },
                "output_classification_table": {
                        "type": "string",
                        "description": "A confusion matrix that  summarizes the performance of the model created on the validation data. The matrix compares the model predicted categories for the validation data to the actual categories. Th...",
                        "default": None
                },
                "output_validation_table": {
                        "type": "string",
                        "description": "A table that contains the \r\nR2 for each model if the variable_predict value is not categorical, or the accuracy of each model if the value is categorical. This table includes a bar chart of the distri...",
                        "default": None
                },
                "compensate_sparse_categories": {
                        "type": "string",
                        "description": "Specifies whether each category in the training dataset, regardless of its frequency, will be represented in each tree.\r\nThis parameter is available when the model_type parameter value is FOREST-BASED...",
                        "default": None
                },
                "number_validation_runs": {
                        "type": "string",
                        "description": "The number of iterations of the tool. The distribution of R-squared values or accuracies of all the models  can be displayed using the output_validation_table parameter. If  the prediction_type parame...",
                        "default": None
                },
                "calculate_uncertainty": {
                        "type": "string",
                        "description": "Specifies whether prediction uncertainty will be calculated when training, predicting to features, or predicting to raster.\r\nThis parameter is available when the model_type parameter value  is FOREST-...",
                        "default": None
                },
                "output_trained_model": {
                        "type": "string",
                        "description": "An output model file that will save the trained model, which can be used later for prediction.",
                        "default": None
                },
                "model_type": {
                        "type": "string",
                        "description": "Specifies the method that will be used to create the model. \r\nFOREST-BASED\u2014A model will be created using an adaptation of the random forest algorithm. The model will use the votes from hundreds of dec...",
                        "default": None
                },
                "reg_lambda": {
                        "type": "string",
                        "description": "A regularization term that reduces the model's sensitivity to individual features. Increasing this value will make the model more conservative and prevent overfitting the training data.  If the value ...",
                        "default": None
                },
                "gamma": {
                        "type": "string",
                        "description": "A threshold for the minimum loss reduction needed to split trees.Potential splits are evaluated for their loss reduction. If the candidate split has a higher loss reduction than this threshold value, ...",
                        "default": None
                },
                "eta": {
                        "type": "string",
                        "description": "A value that reduces the contribution of each tree to the final prediction. The value should be greater than 0 and less than or equal to 1. A lower learning rate prevents overfitting the model; howeve...",
                        "default": None
                },
                "max_bins": {
                        "type": "string",
                        "description": "The number of bins that the training data will be divided into \r\nto search for the best splitting point. The value cannot be 1. The default is 0, which corresponds to the use of a greedy algorithm.  A...",
                        "default": None
                },
                "optimize": {
                        "type": "string",
                        "description": "Specifies whether an optimization method will be used to find the set of hyperparameters that achieve optimal model performance.\r\nTRUE\u2014An optimization method will be used to find the set of hyperparam...",
                        "default": None
                },
                "optimize_algorithm": {
                        "type": "string",
                        "description": "Specifies the optimization method that will be used to select and test search points to find the optimal set of hyperparameters. Search points are combinations of hyperparameters within the search spa...",
                        "default": None
                },
                "optimize_target": {
                        "type": "string",
                        "description": "Specifies the objective function or value that will be minimized or maximized to find the optimal \r\nset of hyperparameters.R2\u2014The optimization method will maximize R2 to find the optimal set of hyperp...",
                        "default": None
                },
                "num_search": {
                        "type": "string",
                        "description": "The number of search points within the search space specified by the model_param_setting parameter \r\nthat will be tested. This parameter is available when the optimize_algorithm parameter value is RAN...",
                        "default": None
                },
                "model_param_setting": {
                        "type": "string",
                        "description": "A list of hyperparameters and their search spaces. Customize the search space of each hyperparameter by providing a lower bound, upper bound, and interval.\r\nThe lower bound and upper bound specify the...",
                        "default": None
                },
                "output_param_tuning_table": {
                        "type": "string",
                        "description": "A table that contains the parameter settings and objective values for each optimization trial. The output includes a chart of all the trials and their objective values. This option is available when o...",
                        "default": None
                },
                "include_probabilities": {
                        "type": "string",
                        "description": "For categorical variables to predict, specifies whether the probability of every category of the categorical variable or only the probability of the record's category will be predicted.\r\nFor example, ...",
                        "default": None
                }
        },
        "required": [
                "prediction_type",
                "in_features"
        ]
},
    "generalized_linear_regression_(glr)": {
        "name": "generalized_linear_regression_(glr)",
        "description": "Performs generalized linear regression (GLR) to generate predictions or to model a dependent variable in terms of its relationship to a set of explanatory variables.  This tool can be used to fit continuous (OLS), binary (logistic), and count (Poisson) models. Learn more about how Generalized Linear Regression works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The feature class containing the dependent and independent variables."
                },
                "dependent_variable": {
                        "type": "string",
                        "description": "The numeric field containing the observed values to be modeled."
                },
                "model_type": {
                        "type": "string",
                        "description": "Specifies the  type of data that will be modeled.CONTINUOUS\u2014 The dependent_variable value is continuous.  The model used is Gaussian, and the tool performs  ordinary least squares regression.BINARY\u2014 T..."
                },
                "output_features": {
                        "type": "string",
                        "description": "The new feature class that will contain the dependent variable estimates and residuals."
                },
                "explanatory_variables": {
                        "type": "string",
                        "description": "A list of fields representing independent explanatory variables in the regression model."
                },
                "distance_features": {
                        "type": "string",
                        "description": "Automatically creates explanatory variables by calculating a distance from the provided features to the in_features values. Distances will be calculated from each of the input distance_features values...",
                        "default": None
                },
                "prediction_locations": {
                        "type": "string",
                        "description": "A feature class containing features representing locations where estimates will be computed. Each feature in this dataset should contain values for all  the explanatory variables specified. The depend...",
                        "default": None
                },
                "explanatory_variables_to_matchfield_from_prediction_locations_field_from_input_features": {
                        "type": "string",
                        "description": "Matches the explanatory variables in the prediction_locations parameter to corresponding explanatory variables from the in_features parameter.",
                        "default": None
                },
                "explanatory_distance_matchingprediction_distance_features_input_explanatory_distance_features": {
                        "type": "string",
                        "description": "Matches the distance features specified for the features_to_predict parameter on the left to the corresponding distance features for the in_features parameter on the right.",
                        "default": None
                },
                "output_predicted_features": {
                        "type": "string",
                        "description": "The output feature class that will receive dependent variable estimates for each prediction_location value.\r\n The output feature class that will receive dependent variable estimates for each Predictio...",
                        "default": None
                },
                "output_trained_model": {
                        "type": "string",
                        "description": "An output model file that will save the trained model, which can be used later for prediction.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "dependent_variable",
                "model_type",
                "output_features",
                "explanatory_variables"
        ]
},
    "generate_network_spatial_weights": {
        "name": "generate_network_spatial_weights",
        "description": "Constructs a spatial weights matrix file (.swm) using a network dataset, defining spatial relationships in terms of the underlying network structure. Learn more about how Generate Network Spatial Weights works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "The point feature class representing locations on the network.  For each feature, neighbors and weights are calculated and stored in the output spatial weights matrix file."
                },
                "unique_id_field": {
                        "type": "string",
                        "description": "An integer field containing a unique value for each feature in the input feature class.  If you don't have a field with unique ID values, you can  create one by adding an integer field to   your featu..."
                },
                "output_spatial_weights_matrix_file": {
                        "type": "string",
                        "description": "The output network spatial weights matrix file (.swm) that will store the neighbors and weights for each input feature."
                },
                "input_network_data_source": {
                        "type": "string",
                        "description": "The network dataset used to find neighbors of each input feature.   Network datasets usually represent street networks but can also represent other kinds of transportation networks such as railroads o..."
                },
                "travel_mode": {
                        "type": "string",
                        "description": "The mode of transportation for the analysis.  A travel mode defines how a pedestrian, car, truck, or other medium of transportation moves through the network and represents a collection\r\nof network se..."
                },
                "impedance_distance_cutoff": {
                        "type": "string",
                        "description": "The maximum impedance distance allowed for neighbors of a feature. Any feature whose distance is farther than this value will not be used as a neighbor.  By default, no distance cutoff is used."
                },
                "impedance_temporal_cutoff": {
                        "type": "string",
                        "description": "The maximum impedance travel time allowed for neighbors of a feature. Any feature whose travel time  is longer than this value will not be used as a neighbor.  By default, no temporal cutoff is used.",
                        "default": None
                },
                "impedance_cost_cutoff": {
                        "type": "string",
                        "description": "The maximum impedance cost allowed for neighbors of a feature. Any feature whose cost of travel is larger than this value will not be used as a neighbor.  By default, no cost cutoff is used.",
                        "default": None
                },
                "maximum_number_of_neighbors": {
                        "type": "string",
                        "description": "An integer reflecting the maximum number of neighbors  for each feature. The actual number of neighbors used for each feature may be smaller due to impedance cutoffs.",
                        "default": None
                },
                "time_of_day": {
                        "type": "string",
                        "description": "The time of day traffic conditions will be considered in the analysis.  Traffic conditions can impact the distance that can be traveled over a given time.  If no date or time is provided, the analysis...",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "Specifies the time\r\nzone for the Time_of_Day parameter.\r\nLOCAL_TIME_AT_LOCATIONS\u2014The time zone in which the Input_Feature_Class is located will be used. This is\r\nthe default.UTC\u2014Coordinated universal ...",
                        "default": None
                },
                "barriers": {
                        "type": "string",
                        "description": "The features that represent blocked intersections, road closures, accident sites, or other locations where travel is blocked along the network.",
                        "default": None
                },
                "search_tolerance": {
                        "type": "string",
                        "description": "The maximum distance used to assign each input feature to a location on the network.  If any of the input points do not fall exactly on a line of the network, they will be assigned to the closest loca...",
                        "default": None
                },
                "conceptualization_of_spatial_relationships": {
                        "type": "string",
                        "description": "Specifies how weights will be defined for each neighbor.            INVERSE\u2014Features farther in distance, time, or cost will have a smaller weight than features nearby. The weights decrease by their i...",
                        "default": None
                },
                "exponent": {
                        "type": "string",
                        "description": "The exponent used when INVERSE option is specified for the Conceptualization_of_Spatial_Relationships parameter.  The weights assigned to each neighbor are calculated by taking the inverse distance, t...",
                        "default": None
                },
                "row_standardization": {
                        "type": "string",
                        "description": "Specifies whether row standardization will be applied. Row standardization is recommended when the locations of the input points are potentially biased due to sampling design or an imposed aggregation...",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "unique_id_field",
                "output_spatial_weights_matrix_file",
                "input_network_data_source",
                "travel_mode",
                "impedance_distance_cutoff"
        ]
},
    "generate_spatial_weights_matrix": {
        "name": "generate_spatial_weights_matrix",
        "description": "Generates a spatial weights matrix file (.swm) to represent the spatial relationships among features in a dataset. Learn more about how Generate Spatial Weights Matrix works",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "The feature class for which spatial relationships of features will be assessed."
                },
                "unique_id_field": {
                        "type": "string",
                        "description": "An integer field containing a different value for every feature in the input feature class.  If you don't have a Unique ID field, you can  create one by adding an integer field to   your feature class..."
                },
                "output_spatial_weights_matrix_file": {
                        "type": "string",
                        "description": "The full path for the output spatial weights matrix file (.swm)."
                },
                "conceptualization_of_spatial_relationships": {
                        "type": "string",
                        "description": "Specifies how spatial relationships among features will be conceptualized.INVERSE_DISTANCE\u2014The impact of one feature on another feature will decrease with distance. FIXED_DISTANCE\u2014Everything within a ..."
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies how distances will be calculated from each feature to neighboring features.EUCLIDEAN\u2014The straight-line distance between two points (as the crow flies) will be calculated. This is the default...",
                        "default": None
                },
                "exponent": {
                        "type": "string",
                        "description": "The value for inverse distance calculation. A typical value is 1 or 2.",
                        "default": None
                },
                "threshold_distance": {
                        "type": "string",
                        "description": "The cutoff distance for the Conceptualization_of_Spatial_Relationships parameter's INVERSE_DISTANCE and FIXED_DISTANCE options. Enter this value using the units specified in the environment output coo...",
                        "default": None
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "An integer reflecting either the minimum or the exact number of neighbors. When the Conceptualization_of_Spatial_Relationships parameter is set to K_NEAREST_NEIGHBORS, each feature will have exactly t...",
                        "default": None
                },
                "row_standardization": {
                        "type": "string",
                        "description": "Specifies whether spatial weights will be standardized by row. Row standardization is recommended whenever feature distribution is potentially biased due to sampling design or to an imposed aggregatio...",
                        "default": None
                },
                "input_table": {
                        "type": "string",
                        "description": "A table containing numeric weights relating every feature to every other feature in the input feature class. Required fields for the table are the Unique ID Field parameter value, NID (neighbor ID), a...",
                        "default": None
                },
                "date_time_field": {
                        "type": "string",
                        "description": "A date field with a time stamp for each feature.",
                        "default": None
                },
                "date_time_interval_type": {
                        "type": "string",
                        "description": "Specifies the units that will be used for measuring time.SECONDS\u2014The unit will be seconds.MINUTES\u2014The unit will be minutes.HOURS\u2014The unit will be hours.DAYS\u2014The unit will be days.WEEKS\u2014The unit will b...",
                        "default": None
                },
                "date_time_interval_value": {
                        "type": "string",
                        "description": "An integer reflecting the number of time units comprising the time window.For example, if you choose HOURS for the Date_Time_Interval_Type parameter and specify 3 for the Date_Time_Interval_Value para...",
                        "default": None
                },
                "use_z_values": {
                        "type": "string",
                        "description": "Specifies whether z-coordinates will be used in the construction of the spatial weights matrix if the input features are z-enabled.  USE_Z_VALUES\u2014Z-values will be used in the construction of the spati..."
                }
        },
        "required": [
                "input_feature_class",
                "unique_id_field",
                "output_spatial_weights_matrix_file",
                "conceptualization_of_spatial_relationships",
                "use_z_values"
        ]
},
    "geographically_weighted_regression_(gwr)": {
        "name": "geographically_weighted_regression_(gwr)",
        "description": "Performs Geographically Weighted Regression, which is a local form of linear regression that is used to model spatially varying relationships. Learn more about how Geographically Weighted Regression (GWR) works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The feature class containing the dependent and explanatory variables."
                },
                "dependent_variable": {
                        "type": "string",
                        "description": "The numeric field containing the observed values that will be modeled."
                },
                "model_type": {
                        "type": "string",
                        "description": "Specifies the  type of data that will be modeled.\r\nCONTINUOUS\u2014 The dependent_variable value is continuous.  The Gaussian model will be used, and the tool will perform  ordinary least squares regressio..."
                },
                "explanatory_variables": {
                        "type": "string",
                        "description": "A list of fields representing independent explanatory variables in the regression model."
                },
                "output_features": {
                        "type": "string",
                        "description": "The new feature class containing the dependent variable estimates and residuals."
                },
                "neighborhood_type": {
                        "type": "string",
                        "description": "Specifies whether the neighborhood used is constructed as a fixed distance or allowed to vary in spatial extent depending on the density of the features.NUMBER_OF_NEIGHBORS\u2014 The neighborhood size is a..."
                },
                "neighborhood_selection_method": {
                        "type": "string",
                        "description": "Specifies how the neighborhood size will be determined. The neighborhood selected with the GOLDEN_SEARCH and MANUAL_INTERVALS options is based on minimizing the AICc value.GOLDEN_SEARCH\u2014The tool will ..."
                },
                "minimum_number_of_neighbors": {
                        "type": "string",
                        "description": "The minimum number of neighbors each feature will include in its calculations. It is recommended that you use at least 30 neighbors.",
                        "default": None
                },
                "maximum_number_of_neighbors": {
                        "type": "string",
                        "description": "The maximum number of neighbors (up to 1000) each feature will include in its calculations.",
                        "default": None
                },
                "minimum_search_distance": {
                        "type": "string",
                        "description": "The minimum neighborhood search distance.\r\nIt is recommended that you use a distance at which each feature has at least 30 neighbors.",
                        "default": None
                },
                "maximum_search_distance": {
                        "type": "string",
                        "description": "The maximum neighborhood search distance.\r\nIf a distance results in features with more than 1000 neighbors, the tool will use the first 1000 in calculations for the target feature.",
                        "default": None
                },
                "number_of_neighbors_increment": {
                        "type": "string",
                        "description": "The number of neighbors by which manual intervals will increase for each neighborhood test.",
                        "default": None
                },
                "search_distance_increment": {
                        "type": "string",
                        "description": "The distance by which manual intervals will increase for each neighborhood test.",
                        "default": None
                },
                "number_of_increments": {
                        "type": "string",
                        "description": "The number of neighborhood sizes that will be tested starting with the minimum_number_of_neighbors or minimum_search_distance  parameter value.",
                        "default": None
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "The closest number of neighbors (up to 1000) that will be considered for each feature. The number must be an integer between 2 and 1000.",
                        "default": None
                },
                "distance_band": {
                        "type": "string",
                        "description": "The spatial extent of the neighborhood.",
                        "default": None
                },
                "prediction_locations": {
                        "type": "string",
                        "description": "A feature class containing features representing locations where estimates will be computed. Each feature in this dataset should contain values for all the explanatory variables specified. The depende...",
                        "default": None
                },
                "explanatory_variables_to_match": {
                        "type": "string",
                        "description": "The explanatory variables from the prediction_locations parameter that match corresponding explanatory variables from the in_features parameter.\r\n[[\"LandCover2000\", \"LandCover2010\"], [\"Income\", \"PerCa...",
                        "default": None
                },
                "output_predicted_features": {
                        "type": "string",
                        "description": "The output feature class that will receive dependent variable estimates for each prediction_location value.",
                        "default": None
                },
                "robust_prediction": {
                        "type": "string",
                        "description": "Specifies the features that will be used in prediction calculations.ROBUST\u2014Features with values more than three standard\r\ndeviations from the mean (value outliers) and features with\r\nweights of 0 (spa...",
                        "default": None
                },
                "local_weighting_scheme": {
                        "type": "string",
                        "description": "Specifies the kernel type that will be used to provide the spatial weighting in the model. The kernel defines how each feature is related to other features within its neighborhood.BISQUARE\u2014A weight of...",
                        "default": None
                },
                "coefficient_raster_workspace": {
                        "type": "string",
                        "description": "The workspace where the coefficient rasters will be created. When this workspace is provided, rasters are created for the intercept and every explanatory variable. This parameter is only available wit...",
                        "default": None
                },
                "scale": {
                        "type": "string",
                        "description": "Specifies whether the values of the explanatory and dependent variables will be scaled to  have mean zero and standard deviation one before fitting the model.SCALE_DATA\u2014The values of the variables wil...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "dependent_variable",
                "model_type",
                "explanatory_variables",
                "output_features",
                "neighborhood_type",
                "neighborhood_selection_method"
        ]
},
    "local_bivariate_relationships": {
        "name": "local_bivariate_relationships",
        "description": "Analyzes two variables for statistically significant relationships using local entropy. Each feature is classified into one of six categories based on the type of relationship. The output can be used to visualize areas where the variables are related and explore how their relationship changes across the study area. Learn more about how Local Bivariate Relationships works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The feature class containing fields representing the dependent_variable and explanatory_variable values."
                },
                "dependent_variable": {
                        "type": "string",
                        "description": "The numeric field representing the values of the dependent variable. When categorizing the relationships, the explanatory_variable value  is used to predict the dependent_variable value."
                },
                "explanatory_variable": {
                        "type": "string",
                        "description": "The numeric field representing the values of the explanatory variable. When categorizing the relationships, the explanatory_variable value is used to predict the dependent_variable value."
                },
                "output_features": {
                        "type": "string",
                        "description": "The output feature class containing all input features with fields representing the dependent_variable value, explanatory_variable value, entropy score, pseudo p-value, level of significance, type of ..."
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "The number of neighbors around each feature (including the feature) that will be used to test for a local relationship between the variables. The number of neighbors must be between 30 and 1,000, and ...",
                        "default": None
                },
                "number_of_permutations": {
                        "type": "string",
                        "description": "Specifies the number of permutations that will be used to calculate the pseudo p-value for each feature. Choosing a number of permutations is a balance between precision in the pseudo p-value and incr...",
                        "default": None
                },
                "enable_local_scatterplot_popups": {
                        "type": "string",
                        "description": "Specifies whether scatterplot pop-ups will be generated for each output feature. Each scatterplot displays the values of the explanatory (horizontal axis) and dependent (vertical axis) variables in th...",
                        "default": None
                },
                "level_of_confidence": {
                        "type": "string",
                        "description": "Specifies a confidence level of the hypothesis test for significant relationships.90%\u2014The confidence level is 90 percent. This is the default.95%\u2014The confidence level is 95 percent. 99%\u2014The confidence...",
                        "default": None
                },
                "apply_false_discovery_rate_fdr_correction": {
                        "type": "string",
                        "description": "Specifies whether False Discover Rate (FDR) correction will be applied to the pseudo p-values.APPLY_FDR\u2014Statistical significance will be based on the FDR correction. This is the default.NO_FDR\u2014Statist...",
                        "default": None
                },
                "scaling_factor": {
                        "type": "string",
                        "description": "The level of sensitivity to subtle relationships between the variables. Larger values (closer to one) can detect relatively weak relationships, while smaller values (closer to zero) will only detect s...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "dependent_variable",
                "explanatory_variable",
                "output_features"
        ]
},
    "multiscale_geographically_weighted_regression_(mgwr)": {
        "name": "multiscale_geographically_weighted_regression_(mgwr)",
        "description": "Performs Multiscale Geographically Weighted Regression (MGWR), which is a local form of linear regression that models spatially varying relationships. MGWR builds upon geographically weighted regression (GWR). It is a local regression model that allows the coefficients of the explanatory variables to vary across space. Each explanatory variable may operate at a different spatial scale. GWR does not account for this, but MGWR does by allowing a different neighborhood (bandwidth) for each explanatory variable. The neighborhood (bandwidth) of an explanatory variable determines the features that are used to estimate the coefficient of that explanatory variable in the linear regression model that is fit at a target feature. Learn more about how Multiscale Geographically Weighted Regression (MGWR)\r\nworks",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The feature class containing the dependent and explanatory variables."
                },
                "dependent_variable": {
                        "type": "string",
                        "description": "The numeric field containing the observed values that will be modeled."
                },
                "model_type": {
                        "type": "string",
                        "description": "Specifies the regression model based on the values of the dependent variable.  Currently, only continuous data is supported, and the parameter is hidden in the Geoprocessing pane.  Do not use categori..."
                },
                "explanatory_variables": {
                        "type": "string",
                        "description": "A list of fields that will be used as independent explanatory variables in the regression model."
                },
                "output_features": {
                        "type": "string",
                        "description": "The new feature class containing the coefficients, residuals, and significance levels of the MGWR model."
                },
                "neighborhood_type": {
                        "type": "string",
                        "description": "Specifies whether the neighborhood  will be a fixed distance or allowed to vary spatially depending on the density of the features.\t\t\t\t\t\tNUMBER_OF_NEIGHBORS\u2014 The neighborhood size will be a specified ..."
                },
                "neighborhood_selection_method": {
                        "type": "string",
                        "description": "Specifies how the neighborhood size will be determined. \t\t\t\t\t\tGOLDEN_SEARCH\u2014An optimal distance or number of neighbors will be identified by minimizing the AICc value using the Golden Search algorithm..."
                },
                "minimum_number_of_neighbors": {
                        "type": "string",
                        "description": "The minimum number of neighbors that each feature will include in its calculation. \r\nIt is recommended that you use at least 30 neighbors.",
                        "default": None
                },
                "maximum_number_of_neighbors": {
                        "type": "string",
                        "description": "The maximum number of neighbors that each feature will include in its calculations.",
                        "default": None
                },
                "distance_unit": {
                        "type": "string",
                        "description": "Specifies the unit of distance that will be used to measure the distances between features. FEETINT\u2014Distances will be measured in international feet.MILESINT\u2014Distances will be measured in statute mile...",
                        "default": None
                },
                "minimum_search_distance": {
                        "type": "string",
                        "description": "The minimum search distance that will be applied to every explanatory variable. It is recommended that you provide a minimum distance that includes at least 30 neighbors for each feature.",
                        "default": None
                },
                "maximum_search_distance": {
                        "type": "string",
                        "description": "The maximum neighborhood search distance that will be applied to all variables.",
                        "default": None
                },
                "number_of_neighbors_increment": {
                        "type": "string",
                        "description": "The number of neighbors by which manual intervals will increase for each neighborhood test.",
                        "default": None
                },
                "search_distance_increment": {
                        "type": "string",
                        "description": "The distance by which manual intervals will increase for each neighborhood test.",
                        "default": None
                },
                "number_of_increments": {
                        "type": "string",
                        "description": "The number of neighborhood sizes to test when using manual intervals. The  first neighborhood size is the value of the minimum_number_of_neighbors or minimum_search_distance parameter.",
                        "default": None
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "The number of neighbors that will be used for the user-defined neighborhood type.",
                        "default": None
                },
                "distance_band": {
                        "type": "string",
                        "description": "The size of the distance band that will be used for the user-defined neighborhood type. All features within this distance will be included as neighbors in the local models.",
                        "default": None
                },
                "number_of_neighbors_golden": {
                        "type": "string",
                        "description": "The customized Golden Search options for individual explanatory variables. For each explanatory variable to be customized, provide the variable, the minimum number of neighbors, and the maximum number...",
                        "default": None
                },
                "number_of_neighbors_manual": {
                        "type": "string",
                        "description": "The customized  manual intervals options for individual explanatory variables. For each explanatory variable to be customized, provide the minimum number of neighbors, number of neighbors increment, a...",
                        "default": None
                },
                "number_of_neighbors_defined": {
                        "type": "string",
                        "description": "The customized user-defined options for individual explanatory variables. For each explanatory variable to be customized, provide the number of neighbors.",
                        "default": None
                },
                "distance_golden": {
                        "type": "string",
                        "description": "The customized Golden Search options for individual explanatory variables. For each explanatory variable to be customized, provide the variable, the minimum search distance, and the maximum search dis...",
                        "default": None
                },
                "distance_manual": {
                        "type": "string",
                        "description": "The customized manual intervals options for individual explanatory variables. For each variable to be customized, provide the variable, the minimum search distance, search distance increments, and num...",
                        "default": None
                },
                "distance_defined": {
                        "type": "string",
                        "description": "The customized user-defined options  for individual explanatory variables. For each variable to be customized, provide the variable and the distance band in the columns.",
                        "default": None
                },
                "prediction_locations": {
                        "type": "string",
                        "description": "A feature class with the locations where estimates will be computed. Each feature in this dataset should contain a value for every explanatory variables specified. The dependent variable for these fea...",
                        "default": None
                },
                "explanatory_variables_to_match": {
                        "type": "string",
                        "description": "The explanatory variables from the prediction locations that match corresponding explanatory variables from the input features.",
                        "default": None
                },
                "output_predicted_features": {
                        "type": "string",
                        "description": "The output feature class that will receive dependent variable estimates for every prediction location.",
                        "default": None
                },
                "robust_prediction": {
                        "type": "string",
                        "description": "Specifies the features that will be used in the prediction calculations.ROBUST\u2014Features with values greater than three standard deviations from the mean (value outliers) and features with weights of 0...",
                        "default": None
                },
                "local_weighting_scheme": {
                        "type": "string",
                        "description": "Specifies the kernel type that will be used to provide the spatial weighting in the model. The kernel defines how each feature is related to other features within its neighborhood.\r\nBISQUARE\u2014A weight ...",
                        "default": None
                },
                "output_table": {
                        "type": "string",
                        "description": "A table containing the output statistics of the MGWR model. A bar chart of estimated bandwidths or numbers of neighbors will be included with the output.",
                        "default": None
                },
                "coefficient_raster_workspace": {
                        "type": "string",
                        "description": "The workspace where the coefficient rasters will be created. When this workspace is provided, rasters are created for the intercept and every explanatory variable.\r\nThis parameter is only available wi...",
                        "default": None
                },
                "scale": {
                        "type": "string",
                        "description": "Specifies whether the values of the explanatory and dependent variables will be scaled to  have mean zero and standard deviation one prior to fitting the model.SCALE_DATA\u2014The values of the variables w...",
                        "default": None
                },
                "number_of_neighbors_gradient": {
                        "type": "string",
                        "description": "The customized Gradient Search options for individual explanatory variables. For each explanatory variable to be customized, provide the variable, the minimum number of neighbors, and the maximum numb...",
                        "default": None
                },
                "distance_gradient": {
                        "type": "string",
                        "description": "The customized Gradient Search options for individual explanatory variables. For each explanatory variable to be customized, provide the variable, the minimum search distance, and the maximum search d...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "dependent_variable",
                "model_type",
                "explanatory_variables",
                "output_features",
                "neighborhood_type",
                "neighborhood_selection_method"
        ]
},
    "ordinary_least_squares_(ols)": {
        "name": "ordinary_least_squares_(ols)",
        "description": "Performs global Ordinary Least Squares (OLS) linear regression to generate predictions or to model a dependent variable in terms of its relationships to a set of explanatory variables. The functionality of this tool is included in the Generalized Linear Regression tool added at ArcGIS Pro 2.3.  The Generalized Linear Regression tool supports additional models.",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "The feature class containing the dependent and independent variables for analysis."
                },
                "unique_id_field": {
                        "type": "string",
                        "description": "An integer field containing a different value for every feature in the Input Feature Class."
                },
                "output_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will receive dependent variable estimates and residuals."
                },
                "dependent_variable": {
                        "type": "string",
                        "description": "The numeric field containing values for what you are trying to model."
                },
                "explanatory_variables": {
                        "type": "string",
                        "description": "A list of fields representing explanatory variables in your regression model."
                },
                "coefficient_output_table": {
                        "type": "string",
                        "description": "The full path to an optional table that will receive model coefficients, standardized coefficients, standard errors, and probabilities for each explanatory variable.",
                        "default": None
                },
                "diagnostic_output_table": {
                        "type": "string",
                        "description": "The full path to an optional table that will receive model summary diagnostics.",
                        "default": None
                },
                "output_report_file": {
                        "type": "string",
                        "description": "The path to the optional PDF file \r\nthe tool will create.  This report file includes model diagnostics, graphs, and notes to help you interpret the OLS results.",
                        "default": None
                }
        },
        "required": [
                "input_feature_class",
                "unique_id_field",
                "output_feature_class",
                "dependent_variable",
                "explanatory_variables"
        ]
},
    "predict_using_spatial_statistics_model_file": {
        "name": "predict_using_spatial_statistics_model_file",
        "description": "Predicts continuous or categorical values using a trained spatial statistics model (.ssm file). Learn more about spatial statistics model files",
        "parameters": {
                "input_model": {
                        "type": "string",
                        "description": "The spatial statistics model file that will be used to make new predictions."
                },
                "prediction_type": {
                        "type": "string",
                        "description": "Specifies the operation mode that will be used. The tool can predict new features or create a prediction raster surface.\r\nPREDICT_FEATURES\u2014Predictions or classifications will be generated for features..."
                },
                "features_to_predict": {
                        "type": "string",
                        "description": "The feature class representing locations where predictions will be made. This feature class must also contain any explanatory variables provided as fields that correspond to those used to train the in...",
                        "default": None
                },
                "output_features": {
                        "type": "string",
                        "description": "The \r\n output feature class containing the prediction results.",
                        "default": None
                },
                "output_raster": {
                        "type": "string",
                        "description": "The output raster containing the prediction results. The default cell size will be the maximum cell size of the input rasters.",
                        "default": None
                },
                "explanatory_variable_matchingpred1_train1_cat1_pred2_train2_cat2": {
                        "type": "string",
                        "description": "A list of the explanatory variables of the input model and corresponding fields of the input prediction features. For each explanatory variable in the Training column, provide the corresponding predic...",
                        "default": None
                },
                "explanatory_distance_matchingpred1_cat1_pred2_cat2": {
                        "type": "string",
                        "description": "A list of the explanatory distance features of the input model and corresponding prediction distance features. For each explanatory distance feature in the Training column, provide the corresponding p...",
                        "default": None
                },
                "explanatory_rasters_matchingpred1_train1_cat1_pred2_train2_cat2": {
                        "type": "string",
                        "description": "A list of the explanatory rasters of the input model and corresponding prediction rasters. For each explanatory raster in the Training column, provide the corresponding prediction raster in the Predic...",
                        "default": None
                }
        },
        "required": [
                "input_model",
                "prediction_type"
        ]
},
    "presence_only_prediction": {
        "name": "presence_only_prediction",
        "description": "Models the presence of a phenomenon given known presence locations and explanatory variables using a maximum entropy approach (MaxEnt). The tool provides output features and rasters that include the probability of presence and can be applied to problems in which only presence is known and absence is not known. Learn more about how Presence-only Prediction (MaxEnt) works",
        "parameters": {
                "input_point_features": {
                        "type": "string",
                        "description": "The point features representing locations where presence of a phenomenon of interest is known to occur."
                },
                "contains_background": {
                        "type": "string",
                        "description": "Specifies whether the input point features contain background points.\r\nIf the input points do not contain background points, the tool will generate background points\r\nusing cells in the explanatory tr...",
                        "default": None
                },
                "presence_indicator_field": {
                        "type": "string",
                        "description": "The field from the input point features containing binary values that indicate each point as presence (1) or background (0). The field must be numeric.",
                        "default": None
                },
                "explanatory_variablesvariable_categorical": {
                        "type": "string",
                        "description": "A list of fields representing the explanatory variables that will help predict the probability of presence. You can specify whether each variable is categorical or numeric. Specify the CATEGORICAL opt...",
                        "default": None
                },
                "distance_features": {
                        "type": "string",
                        "description": "A list of feature layers or feature classes that will be used to automatically create explanatory variables that represent the distance from the input point features to the nearest provided distance f...",
                        "default": None
                },
                "explanatory_rastersvariable_categorical": {
                        "type": "string",
                        "description": "A list of rasters that will be used to automatically create\r\nexplanatory training variables in the model whose values are\r\nextracted from rasters. For each feature (presence and background\r\npoints) in...",
                        "default": None
                },
                "basis_expansion_functions": {
                        "type": "string",
                        "description": "Specifies the basis function that will be used to transform the provided explanatory variables for use in the model. If multiple basis functions are selected, the tool will produce multiple transforme...",
                        "default": None
                },
                "number_knots": {
                        "type": "string",
                        "description": "The number of knots that will be used by the hinge and\r\nthreshold explanatory variable expansions.\r\nThe value controls how many thresholds are created, which are\r\nused to create multiple explanatory v...",
                        "default": None
                },
                "study_area_type": {
                        "type": "string",
                        "description": "Specifies the type of study area that will be used to define where presence is possible when the input point features do not contain background points.CONVEX_HULL\u2014 The smallest convex polygon that enc...",
                        "default": None
                },
                "study_area_polygon": {
                        "type": "string",
                        "description": "A feature class containing the polygons that define a custom study area. The input point features must be located within the custom study area covered by the polygon features. A study area can be comp...",
                        "default": None
                },
                "spatial_thinning": {
                        "type": "string",
                        "description": "Specifies whether spatial thinning will be applied to presence and background points before training the model.Spatial thinning helps to reduce sampling bias by removing\r\npoints and ensuring that rema...",
                        "default": None
                },
                "thinning_distance_band": {
                        "type": "string",
                        "description": "The minimum distance between any two presence points or any two background points when spatial thinning is applied.",
                        "default": None
                },
                "number_of_iterations": {
                        "type": "string",
                        "description": "The number of runs that will be used to find the optimal spatial thinning solution, seeking to maintain as many presence and background points as possible while ensuring that no two presence or two ba...",
                        "default": None
                },
                "relative_weight": {
                        "type": "string",
                        "description": "A value between 1 and 100 that specifies the relative\r\ninformation weight of presence points to background points. The\r\ndefault is 100.A higher value indicates that presence points are the primary\r\nso...",
                        "default": None
                },
                "link_function": {
                        "type": "string",
                        "description": "Specifies the function that will convert the unbounded outputs of the model to a number between 0 and 1. This value can be interpreted as the probability of presence at the location. Each option conve...",
                        "default": None
                },
                "presence_probability_cutoff": {
                        "type": "string",
                        "description": "A cutoff value between 0.01 and 0.99 that establishes which probabilities correspond with presence in the resulting classification. The cutoff value is used to help evaluate the model's performance us...",
                        "default": None
                },
                "output_trained_features": {
                        "type": "string",
                        "description": "An output feature class that will contain all features and explanatory variables used in the training of the model.",
                        "default": None
                },
                "output_trained_raster": {
                        "type": "string",
                        "description": "The output raster with cell values indicating the probability of presence using the selected link function.\r\nThe default cell size is the maximum of the cell sizes of the explanatory training rasters....",
                        "default": None
                },
                "output_response_curve_table": {
                        "type": "string",
                        "description": "The output table that will contain diagnostics from the\r\ntraining model that indicate the effect of each explanatory\r\nvariable on the probability of presence after accounting for the\r\naverage effects ...",
                        "default": None
                },
                "output_sensitivity_table": {
                        "type": "string",
                        "description": "The output table that will contain diagnostics of training model accuracy as the probability presence cutoff changes from 0 to 1.",
                        "default": None
                },
                "features_to_predict": {
                        "type": "string",
                        "description": "The feature class representing locations where predictions will be\r\nmade. The feature class must contain any provided explanatory\r\nvariable fields that were used from the input point features. When us...",
                        "default": None
                },
                "output_pred_features": {
                        "type": "string",
                        "description": "The output feature class that will contain the results of the prediction model applied to the input prediction features.",
                        "default": None
                },
                "output_pred_raster": {
                        "type": "string",
                        "description": "The output raster containing the prediction results at each cell of the matched explanatory rasters.\r\nThe default cell size is the maximum of the cell sizes of the explanatory training rasters.",
                        "default": None
                },
                "explanatory_variable_matchingprediction_training": {
                        "type": "string",
                        "description": "The matching explanatory variable fields for the input point features and input prediction features.",
                        "default": None
                },
                "explanatory_distance_matchingprediction_training": {
                        "type": "string",
                        "description": "The matching distance features for the training and prediction.",
                        "default": None
                },
                "explanatory_rasters_matchingprediction_training": {
                        "type": "string",
                        "description": "The matching rasters for the training and prediction.",
                        "default": None
                },
                "allow_predictions_outside_of_data_ranges": {
                        "type": "string",
                        "description": "ALLOWED\u2014The prediction will allow extrapolation beyond the range of values used in training. This is the default.NOT_ALLOWED\u2014The prediction will not allow extrapolation beyond the range of values used...",
                        "default": None
                },
                "resampling_scheme": {
                        "type": "string",
                        "description": "Specifies the method that will be used to perform cross validation of the prediction model. Cross validation excludes a portion of the data during training of the model and uses it to test the model's...",
                        "default": None
                },
                "number_of_groups": {
                        "type": "string",
                        "description": "The number of groups that will be used in cross validation\r\nfor the random resampling scheme. A field in the\r\noutput trained features indicates the group that each point\r\nwas assigned to. The default ...",
                        "default": None
                },
                "output_trained_model": {
                        "type": "string",
                        "description": "An output model file that will save the trained model, which can be used later for prediction.",
                        "default": None
                }
        },
        "required": [
                "input_point_features"
        ]
},
    "spatial_association_between_zones": {
        "name": "spatial_association_between_zones",
        "description": "Measures the degree of spatial association between two regionalizations of the same study area in which each regionalization is composed of a set of categories, called zones.  The association between the regionalizations is determined by the area overlap between zones of each regionalization. The association is highest when each zone of one regionalization closely corresponds to a zone of the other regionalization.  Similarly, spatial association is lowest when the zones of one regionalization have large overlap with many different zones of the other regionalization.   The primary output of the tool is a global measure of spatial association between the categorical variables: a single number ranging from 0 (no correspondence) to 1 (perfect spatial alignment of zones). Optionally, this global association can be calculated and visualized for specific zones of either regionalization or for specific combinations of zones between regionalizations. For example, you can use this tool to compare two sets of categorical zones, such as the crop type and soil drainage class of an agricultural area to measure how closely particular crops correspond to a specific class of soil drainage. However, you can also use this tool to measure the degree of change of the same categorical zones over time.  For example, climate zones from 1990 can be compared to climate zones from 2020 to measure how much the climate zones changed over three decades. Using optional outputs, you can determine how each individual climate zone changed, such as whether arid climate zones expanded into areas that were\r\npreviously semiarid. Learn more about how Spatial Association Between Zones works",
        "parameters": {
                "input_feature_or_raster": {
                        "type": "string",
                        "description": "The dataset representing the  zones of the first regionalization.  The zones can be defined using polygon features or a raster."
                },
                "categorical_zone_field": {
                        "type": "string",
                        "description": "The field representing the zone category of the input zones. Each unique value of this field defines an individual zone. For features, the field must be integer or text.  For rasters, the VALUE field ..."
                },
                "overlay_feature_or_raster": {
                        "type": "string",
                        "description": "The dataset representing the zones of the second regionalization.  The zones can be polygon features or a raster."
                },
                "categorical_overlay_zone_field": {
                        "type": "string",
                        "description": "The field representing the zone category of the overlay zones.\r\nEach unique value of this field defines an individual zone. For features, the field must be integer or text.  For rasters, the VALUE fie..."
                },
                "output_features": {
                        "type": "string",
                        "description": "The output polygon features containing spatial association measures at all intersections of the input and overlay zones.\r\nThe output features can be used to measure the association between specific co...",
                        "default": None
                },
                "output_raster": {
                        "type": "string",
                        "description": "The output raster containing spatial association measures\r\nbetween the input and overlay zones. The output raster will have three fields to indicate the spatial association measures for  intersections...",
                        "default": None
                },
                "correspondence_overlay_to_input": {
                        "type": "string",
                        "description": "The output polygon features containing the correspondence measures of the overlay zones  within the input zones.\r\nThis output will have the same geometry as the input zones and can be used to identify...",
                        "default": None
                },
                "correspondence_input_to_overlay": {
                        "type": "string",
                        "description": "The output polygon features containing the correspondence measures of the input zones  within the overlay zones.\r\nThis output will have the same geometry as the overlay zones and can be used to identi...",
                        "default": None
                }
        },
        "required": [
                "input_feature_or_raster",
                "categorical_zone_field",
                "overlay_feature_or_raster",
                "categorical_overlay_zone_field"
        ]
},
    "spatial_autoregression": {
        "name": "spatial_autoregression",
        "description": "Estimates a global spatial regression model for a point or polygon feature class. The assumptions of traditional linear regression models are often violated when using spatial data. When spatial autocorrelation is present in a dataset, coefficient estimates may be biased and lead to overconfident inference. This tool can be used to estimate a regression model that is robust in the presence of spatial dependence and heteroskedasticity, as well as measure spatial spillovers. The tool uses Lagrange Multiplier (LM), also known as a Rao Score, diagnostic tests to determine the model that is most appropriate. Based on the LM diagnostics, either an ordinary least square (OLS), spatial lag model (SLM), spatial error model (SEM), or spatial autoregressive combined model (SAC) may be estimated. Learn more about how Spatial Autoregression works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features containing the dependent and explanatory variables."
                },
                "dependent_variable": {
                        "type": "string",
                        "description": "The numeric field that will be predicted in the regression model."
                },
                "explanatory_variables": {
                        "type": "string",
                        "description": "A list of fields that will be used to predict the dependent variable in the regression model."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output feature class containing the predicted values of the dependent variable and the residuals."
                },
                "model_type": {
                        "type": "string",
                        "description": "The model type that will be used for the estimation. By default, LM diagnostic tests will be used to determine the model that is the most appropriate for the input data.AUTO\u2014LM diagnostic tests will b..."
                },
                "neighborhood_type": {
                        "type": "string",
                        "description": "Specifies how neighbors will be chosen for each input feature. To identify local spatial patterns, neighboring features must be identified for each input feature.DISTANCE_BAND\u2014Features within a specif...",
                        "default": None
                },
                "distance_band": {
                        "type": "string",
                        "description": "The distance within which features will be included as neighbors. If no value is provided, one will be estimated during processing and included as a geoprocessing message.",
                        "default": None
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "The number of neighbors that will be included as neighbors. The number does not include the focal feature. The default is 8.",
                        "default": None
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "The path and file name of the spatial weights matrix file that defines spatial relationships among features.",
                        "default": None
                },
                "local_weighting_scheme": {
                        "type": "string",
                        "description": "Specifies the weighting scheme that will be applied to neighbors. Weights will always be row-standardized unless a spatial weights matrix file is provided.UNWEIGHTED\u2014Neighbors will be assigned a weigh...",
                        "default": None
                },
                "kernel_bandwidth": {
                        "type": "string",
                        "description": "The bandwidth of the weighting kernel. If no value is provided, an adaptive kernel will be used. An adaptive kernel uses the maximum distance from a neighbor to a focal feature as the bandwidth.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "dependent_variable",
                "explanatory_variables",
                "out_features",
                "model_type"
        ]
},
    "compare_neighborhood_conceptualizations": {
        "name": "compare_neighborhood_conceptualizations",
        "description": "Selects the spatial weights matrix (SWM) from a set of candidate SWMs that best represents the spatial patterns (such as trends or clusters) of one or more numeric fields. The output spatial weights matrix  file can then be used in tools that allow .swm files for their Neighborhood Type or Conceptualization of Spatial Relationships parameter values, such as the Bivariate Spatial Association (Lee's L), Hot Spot Analysis (Getis-Ord Gi*), and Cluster and Outlier Analysis (Anselin Local Moran's I) tools. The tool selects the SWM by creating spatial components (called Moran eigenvectors) from each candidate SWM and testing how effectively the components represent the spatial patterns of the input fields. Learn more about Moran eigenvectors",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features containing the fields that will be used to select the SWM."
                },
                "input_fields": {
                        "type": "string",
                        "description": "The input fields that will be used to select the SWM."
                },
                "out_swm": {
                        "type": "string",
                        "description": "The output .swm file of the neighbors and weights selected by the tool."
                },
                "id_field": {
                        "type": "string",
                        "description": "The unique ID field of the output .swm file. The field must be an integer and must have a unique value for each input feature."
                },
                "in_swm": {
                        "type": "string",
                        "description": "The input .swm files that will be used as candidates for the SWM that best represents the spatial patterns (such as trends or clusters) of one or more numeric fields. If no files are provided, the too...",
                        "default": None
                },
                "compare_only_inputs": {
                        "type": "string",
                        "description": "Specifies whether only the .swm files provided in the in_swm parameter will be tested or whether 28 additional neighborhoods will also be tested. The tool will use the SWM that creates spatial compone...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "input_fields",
                "out_swm",
                "id_field"
        ]
},
    "create_spatial_component_explanatory_variables": {
        "name": "create_spatial_component_explanatory_variables",
        "description": "Creates a set of spatial component fields that best describe the spatial patterns of one or more numeric fields and serve as useful explanatory variables in a prediction or regression model. The input fields should be the explanatory and dependent variables that will be used in a prediction model. The resulting spatial component fields (called Moran eigenvectors) can be used as explanatory variables (in addition to the original explanatory variables) that will often improve the predictive power of the model by accounting for spatial patterns of the other variables. Learn more about Moran eigenvectors",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features containing fields of the explanatory and dependent variables that will be used in a prediction model."
                },
                "input_fields": {
                        "type": "string",
                        "description": "The input fields of the explanatory and dependent variables that will be used in a prediction model."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output features that will contain fields of the spatial components that can be used as additional explanatory variables in a prediction model."
                },
                "append_all_fields": {
                        "type": "string",
                        "description": "Specifies whether all fields will be copied from the input features to the output feature class.ALL\u2014 All fields from the input features will be copied to the output feature class. This is the default....",
                        "default": None
                },
                "in_swm": {
                        "type": "string",
                        "description": "A list of input SWM files (.swm) that will be used as candidates for the SWM that will be used to create the spatial component explanatory variables. If no files are provided, the tool will test 28 di...",
                        "default": None
                },
                "out_swm": {
                        "type": "string",
                        "description": "The output SWM file (.swm) of the neighbors and weights selected by the tool.  This parameter does not apply if you provide an input .swm file.",
                        "default": None
                },
                "id_field": {
                        "type": "string",
                        "description": "The unique ID field of the output .swm file. The field must be an integer and must have a unique value for each input feature.",
                        "default": None
                },
                "compare_only_inputs": {
                        "type": "string",
                        "description": "Specifies whether only the .swm files provided in the in_swm parameter will be tested or whether 28 additional neighborhoods will also be tested. The tool will use the SWM that creates spatial compone...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "input_fields",
                "out_features"
        ]
},
    "decompose_spatial_structure_(moran_eigenvectors)": {
        "name": "decompose_spatial_structure_(moran_eigenvectors)",
        "description": "Decomposes a feature class and neighborhood into a set of spatial components. The components represent potential spatial patterns among the features, such as clusters or trends. The components are returned as fields of the output feature class and represent variables of the input features and neighborhood that have the strongest possible spatial clustering (spatial autocorrelation).  The components are called Moran eigenvectors, and each component represents a different spatial pattern that are each independent of each other. Learn more about Moran eigenvectors",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The point or polygon features that will be used to create the spatial components."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output feature class that will contain the spatial components as fields. The number of fields created depends on the min_autocorrelation and max_components parameter values."
                },
                "append_all_fields": {
                        "type": "string",
                        "description": "Specifies whether all fields will be copied from the input features to the output feature class.ALL\u2014 All fields from the input features will be copied to the output feature class. This is the default....",
                        "default": None
                },
                "min_autocorrelation": {
                        "type": "string",
                        "description": "The threshold value for including a spatial component.  The value is a proportion of the largest possible Moran's I value for the spatial weights, and a component must have a larger Moran's I value th...",
                        "default": None
                },
                "max_components": {
                        "type": "string",
                        "description": "The maximum number of spatial components that will be created. The default is 15.",
                        "default": None
                },
                "neighborhood_type": {
                        "type": "string",
                        "description": "Specifies how neighbors will be chosen for each input feature.  Neighboring features must be identified in order to decompose the spatial structure of the input features. \r\nDISTANCE_BAND\u2014Features with...",
                        "default": None
                },
                "distance_band": {
                        "type": "string",
                        "description": "The distance within which features will be included as neighbors. If no value is provided, one will be estimated during processing and included as a geoprocessing message. If the specified distance re...",
                        "default": None
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "The number of neighbors that will be included for each feature. The number does not include the focal feature. The default is 8.",
                        "default": None
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "The path and file name of the spatial weights matrix file (.swm) that defines the neighbors and weights between the input features.",
                        "default": None
                },
                "local_weighting_scheme": {
                        "type": "string",
                        "description": "Specifies the weighting scheme that will be applied to neighboring features.  \r\nUNWEIGHTED\u2014Neighbors will not be weighted.  This is the default.BISQUARE\u2014Neighbors will be weighted using a bisquare ker...",
                        "default": None
                },
                "kernel_bandwidth": {
                        "type": "string",
                        "description": "The bandwidth of the bisquare or Gaussian local weighting schemes. If no value is provided, one will be estimated during processing and included as a geoprocessing message.",
                        "default": None
                },
                "out_swm": {
                        "type": "string",
                        "description": "The output spatial weights matrix file (.swm) of the neighbors and weights of all pairs of features.  If created, this file can be reused in tools that allow defining neighbors and weights with spatia...",
                        "default": None
                },
                "id_field": {
                        "type": "string",
                        "description": "The unique ID field of the output spatial weights matrix file. The field must be an integer and must have a unique value for each input feature.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_features"
        ]
},
    "filter_spatial_autocorrelation_from_field": {
        "name": "filter_spatial_autocorrelation_from_field",
        "description": "Creates a spatially filtered version of an input field.  The filtered variable will have no statistically significant spatial clustering but will maintain the core statistical properties of the field. The spatially filtered version of the field can then be used in analytical workflows (such as correlation or regression analysis) that assume the values at each location are spatially independent (not spatially clustered). The tool filters spatial autocorrelation by splitting the field in a nonspatial component (the filtered field) and a set of spatial components (called Moran eigenvectors). When the input field is a field of residuals or standardized residuals from a prediction or regression model, including the spatial components as explanatory variables in the model (in addition to the original explanatory variables) will reduce or eliminate spatial autocorrelation of the residual term, which is an assumption of various prediction models. Learn more about Moran eigenvectors",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features containing the field that will be spatially filtered."
                },
                "input_field": {
                        "type": "string",
                        "description": "The input field that will be spatially filtered."
                },
                "out_features": {
                        "type": "string",
                        "description": "The output features containing a field of the spatially filtered input field and fields of the spatial components used to filter it."
                },
                "append_all_fields": {
                        "type": "string",
                        "description": "Specifies whether all fields will be copied from the input features to the output feature class.ALL\u2014 All fields from the input features will be copied to the output feature class. This is the default....",
                        "default": None
                },
                "in_swm": {
                        "type": "string",
                        "description": "A list of input SWM files (.swm) that will be used as candidates for the SWM that will be used to filter the spatial autocorrelation from the input field. The SWM that most effectively filters spatial...",
                        "default": None
                },
                "out_swm": {
                        "type": "string",
                        "description": "The output SWM file (.swm) of the neighbors and weights selected by the tool.",
                        "default": None
                },
                "id_field": {
                        "type": "string",
                        "description": "The unique ID field of the output .swm file. The field must be an integer and must have a unique value for each input feature.",
                        "default": None
                },
                "compare_only_inputs": {
                        "type": "string",
                        "description": "Specifies whether only the .swm files provided in the in_swm parameter will be tested or whether 28 additional neighborhoods will also be tested. The tool will use the SWM that creates spatial compone...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "input_field",
                "out_features"
        ]
},
    "calculate_distance_band_from_neighbor_count": {
        "name": "calculate_distance_band_from_neighbor_count",
        "description": "Returns the minimum, the maximum, and the average distance to the specified Nth nearest neighbor (N is an input parameter) for a set of features.  Results are written as tool execution messages.",
        "parameters": {
                "input_features": {
                        "type": "string",
                        "description": "The feature class or layer used to calculate distance statistics."
                },
                "neighbors": {
                        "type": "string",
                        "description": "The number of neighbors (N) to consider for each feature. This number should be any integer between one and the total number of features in the feature class. A list of distances between each feature ..."
                },
                "distance_method": {
                        "type": "string",
                        "description": "Specifies how distances are calculated from each feature to neighboring features.EUCLIDEAN_DISTANCE\u2014The straight-line distance between two points (as the crow flies) MANHATTAN_DISTANCE\u2014The distance be..."
                }
        },
        "required": [
                "input_features",
                "neighbors",
                "distance_method"
        ]
},
    "calculate_rates": {
        "name": "calculate_rates",
        "description": "Calculates crude or smoothed rates. The global empirical Bayes rate method smooths the rates toward a global reference rate. The local empirical Bayes, locally weighted average, and locally weighted median rate methods use local neighbors to spatially smooth rates. Learn more about how Calculate Rates works",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table or features containing count fields and population fields to calculate rates."
                },
                "rate_fieldscount_field_population_field": {
                        "type": "string",
                        "description": "The count and population fields that will be used to calculate rates."
                },
                "append_to_input": {
                        "type": "string",
                        "description": "Specifies whether fields will be appended to the input dataset or saved to an output table or feature class.\r\nAPPEND\u2014  Fields will be appended to the input features. This modifies the input data.NO_AP...",
                        "default": None
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table or feature class containing the rates and additional fields to help evaluate the rates.",
                        "default": None
                },
                "rate_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to calculate rates.\r\nCRUDE_RATE\u2014The rates will be calculated by dividing the count field values by the population field values. This is the default.GLOBAL_EMPIRI...",
                        "default": None
                },
                "probability_distribution": {
                        "type": "string",
                        "description": "Specifies the probability distribution of the count field.\r\nPOISSON\u2014The count field is assumed to follow a Poisson distribution. This is the default.BINOMIAL\u2014The count field is assumed to follow a bin..."
                },
                "neighborhood_type": {
                        "type": "string",
                        "description": "Specifies the method that will be used to identify the neighbors of each feature.\r\nDISTANCE_BAND\u2014A threshold distance is applied to identify neighbors. Every feature that is within the threshold dista...",
                        "default": None
                },
                "distance_band": {
                        "type": "string",
                        "description": "The distance from each feature that will be used to search for neighbors. All features within this distance will be included as neighbors.",
                        "default": None
                },
                "number_of_neighbors": {
                        "type": "string",
                        "description": "The number of neighbors that will be included in a feature's neighborhood.",
                        "default": None
                },
                "weights_matrix_file": {
                        "type": "string",
                        "description": "The path and file name of the spatial weights matrix file that defines the spatial relationships among features.",
                        "default": None
                },
                "local_weighting_scheme": {
                        "type": "string",
                        "description": "Specifies the weighting scheme that will be applied to neighbors when calculating local statistics.UNWEIGHTED\u2014 Neighbors will not be weighted. This is the default.BISQUARE\u2014Neighbors will be weighted u...",
                        "default": None
                },
                "kernel_bandwidth": {
                        "type": "string",
                        "description": "The bandwidth of the bisquare or Gaussian local weighting schemes.\r\nIf no value is provided, one will be estimated during processing and included as a geoprocessing message.",
                        "default": None
                },
                "rate_multiplier": {
                        "type": "string",
                        "description": "A constant value that will be multiplied by the rates. This parameter can be used to scale the rates or to report the rates per specific unit of population. For example, when the value is set to 10,00..."
                }
        },
        "required": [
                "in_table",
                "rate_fieldscount_field_population_field",
                "probability_distribution",
                "rate_multiplier"
        ]
},
    "collect_events": {
        "name": "collect_events",
        "description": "Converts event data, such as crime or disease incidents, to weighted point data.",
        "parameters": {
                "input_incident_features": {
                        "type": "string",
                        "description": "The features representing event or incident data."
                },
                "output_weighted_point_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will contain the weighted point data."
                }
        },
        "required": [
                "input_incident_features",
                "output_weighted_point_feature_class"
        ]
},
    "convert_spatial_statistics_popup_charts_for_web_display": {
        "name": "convert_spatial_statistics_popup_charts_for_web_display",
        "description": "Prepares interactive pop-up charts for web display by saving them as image attachments to a feature class. Several tools in the Spatial Statistics and Space Time Pattern Mining toolboxes create output feature classes that include an HTML_CHART  field. If you click a feature that contains this field, an interactive chart will appear in the pop-up pane. However, if you share this feature class as a web layer to ArcGIS Online and click a feature in Map Viewer, the chart will not appear in the pop-ups. This tool creates a feature class that contains the pop-up charts as image attachments. If the feature class with image attachments is shared as a web service to ArcGIS Online, the charts will appear in the pop-ups of the web feature layer.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The feature class that contains the HTML_CHART field with the HTML code to create a pop-up chart. The feature class must have a 32 bit ObjectID - 64 bit Object IDs are not supported."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will contain the pop-up chart of each feature saved as an image attachment."
                },
                "img_width": {
                        "type": "string",
                        "description": "The width, in pixels, of each image attachment.",
                        "default": None
                },
                "img_height": {
                        "type": "string",
                        "description": "The height, in pixels, of each image attachment.",
                        "default": None
                },
                "rotate_x_axis_labels": {
                        "type": "string",
                        "description": "Specifies whether the x-axis labels will be rotated.ROTATE\u2014The x-axis labels will be rotated 20 degrees.NO_ROTATE\u2014The x-axis labels will not be rotated. This is the default.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "convert_spatial_weights_matrix_to_table": {
        "name": "convert_spatial_weights_matrix_to_table",
        "description": "Converts a binary spatial weights matrix file (.swm) to a table.",
        "parameters": {
                "input_spatial_weights_matrix_file": {
                        "type": "string",
                        "description": "The full pathname for the spatial weights matrix file (.swm) you want to convert."
                },
                "output_table": {
                        "type": "string",
                        "description": "A full pathname to the table you want to create."
                }
        },
        "required": [
                "input_spatial_weights_matrix_file",
                "output_table"
        ]
},
    "describe_spatial_statistics_model_file": {
        "name": "describe_spatial_statistics_model_file",
        "description": "Describes the contents and diagnostics of a spatial statistics model file. Learn more about spatial statistics model files",
        "parameters": {
                "input_model": {
                        "type": "string",
                        "description": "The spatial statistics model file that will be described."
                }
        },
        "required": [
                "input_model"
        ]
},
    "dimension_reduction": {
        "name": "dimension_reduction",
        "description": "Reduces the number of dimensions of a set of continuous variables by aggregating the highest possible amount of variance into fewer components using Principal Component Analysis (PCA) or Reduced-Rank Linear Discriminant Analysis (LDA). The variables are specified as fields in an input table or feature layer, and new fields representing the new variables are saved  in the output table or feature class. The number of new fields will be fewer than the number of original variables while maintaining the highest possible amount of variance from all the original variables. Dimension reduction is commonly used to explore multivariate relationships between variables and to reduce the computational cost of machine learning algorithms in which the required memory and processing time depend on the number of dimensions of the data. Using the components in place of the original data in analysis or machine learning algorithms can often provide comparable (or better) results while consuming fewer computational resources. Learn more about how Dimension Reduction works",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table or features containing the fields with the dimension that will be reduced."
                },
                "output_data": {
                        "type": "string",
                        "description": "The output table or feature class containing the resulting components of the dimension reduction.",
                        "default": None
                },
                "fields": {
                        "type": "string",
                        "description": "The fields representing the data with the dimension that will be reduced."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to reduce the dimensions of the analysis fields.PCA\u2014The analysis fields will be partitioned into components that each maintain the maximum proportion of the tota...",
                        "default": None
                },
                "scale": {
                        "type": "string",
                        "description": "Specifies whether the values of each analysis will be scaled to have a variance equal to one. This scaling ensures that each analysis field is given equal priority in the components. Scaling also remo...",
                        "default": None
                },
                "categorical_field": {
                        "type": "string",
                        "description": "The field representing the categorical variable for LDA.  The components will maintain the maximum amount of information needed to classify each input record into these categories.",
                        "default": None
                },
                "min_variance": {
                        "type": "string",
                        "description": "The minimum percent of total variance  of the analysis fields that must be maintained in the components.\r\nThe total variance depends on whether the analysis fields were scaled using the scale paramete...",
                        "default": None
                },
                "min_components": {
                        "type": "string",
                        "description": "The minimum number of components.",
                        "default": None
                },
                "append_fields": {
                        "type": "string",
                        "description": "Specifies whether all fields from the input table or features will be copied and appended to the output table or feature class. The fields provided in the fields parameter will be copied to the output...",
                        "default": None
                },
                "output_eigenvalues_table": {
                        "type": "string",
                        "description": "The output table containing the eigenvalues of each component.\r\nThe values of the eigenvectors are rescaled to have unit norm (the sum of squared values equals one).",
                        "default": None
                },
                "output_eigenvectors_table": {
                        "type": "string",
                        "description": "The output table containing the eigenvectors of each component.",
                        "default": None
                },
                "number_of_permutations": {
                        "type": "string",
                        "description": "The number of permutations that will be used when determining the optimal number of components.  The default value is 0, which indicates that no permutation test will be performed.\r\nThe provided value...",
                        "default": None
                },
                "append_to_input": {
                        "type": "string",
                        "description": "Specifies whether the component fields will be appended to the input dataset or saved to an output table or feature class. If you append the fields to the input, the output coordinate system environme...",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "fields"
        ]
},
    "export_feature_attributes_to_ascii": {
        "name": "export_feature_attributes_to_ascii",
        "description": "Exports feature class coordinates and attribute values to a space-, comma-, tab-, or semicolon-delimited ASCII text file.",
        "parameters": {
                "input_feature_class": {
                        "type": "string",
                        "description": "The feature class from which the feature coordinates and attribute values will be exported."
                },
                "value_field": {
                        "type": "string",
                        "description": "The field or fields in the input feature class containing the values to export to an ASCII text file."
                },
                "delimiter": {
                        "type": "string",
                        "description": "Specifies how feature coordinates and attribute values will be separated in the output ASCII file.SPACE\u2014Feature coordinates and attribute values will be separated by a space in the output. This is the..."
                },
                "output_ascii_file": {
                        "type": "string",
                        "description": "The ASCII text file that will contain the feature coordinates and attribute values."
                }
        },
        "required": [
                "input_feature_class",
                "value_field",
                "delimiter",
                "output_ascii_file"
        ]
},
    "set_spatial_statistics_model_file_properties": {
        "name": "set_spatial_statistics_model_file_properties",
        "description": "Adds descriptions and units to the variables stored in a spatial statistics model file. Learn more about spatial statistics model files",
        "parameters": {
                "input_model": {
                        "type": "string",
                        "description": "The spatial statistics model file."
                },
                "variable_predictvar1_desc1_unit1_var2_desc2_unit2": {
                        "type": "string",
                        "description": "The name, description, and unit of the variable that will be predicted at new locations.",
                        "default": None
                },
                "explanatory_variablesvar1_desc1_unit1_var2_desc2_unit2": {
                        "type": "string",
                        "description": "The name, description, and unit\r\nof the explanatory variables that will be used to train the input model.",
                        "default": None
                },
                "distance_featuresvar1_desc1_unit1_var2_desc2_unit2": {
                        "type": "string",
                        "description": "The name, description, and unit\r\nof the explanatory training distance features that will be used to train the input model.",
                        "default": None
                },
                "explanatory_rastersvar1_desc1_unit1_var2_desc2_unit2": {
                        "type": "string",
                        "description": "The name, description, and unit\r\nof the explanatory training rasters that will be used to train the input model.",
                        "default": None
                }
        },
        "required": [
                "input_model"
        ]
},
    "time_series_smoothing": {
        "name": "time_series_smoothing",
        "description": "Smooths a numeric variable of one or more time series using centered, forward, and backward moving averages, as well as an adaptive method based on local linear regression. After smoothing short-term fluctuations, longer-term trends or cycles often become apparent. Learn more about how Time Series Smoothing works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The features or table containing the time series data and the field to smooth."
                },
                "time_field": {
                        "type": "string",
                        "description": "The field containing the time of each record."
                },
                "analysis_field": {
                        "type": "string",
                        "description": "The field containing the values that will be smoothed."
                },
                "group_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to group records into different time series. \r\nSmoothing is performed independently for each time series.LOCATION\u2014Features at the same location will be grouped i...",
                        "default": None
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the smoothing method that will be used.\r\nBACKWARD\u2014The smoothed value is the average of the record and the values within the time window before it. This is the default.CENTERED\u2014The smoothed v...",
                        "default": None
                },
                "time_window": {
                        "type": "string",
                        "description": "The length of the time window. The value can be provided in seconds, minutes, hours, days, weeks, months, or years. For backward, forward, and centered moving averages, the value and unit must be prov...",
                        "default": None
                },
                "append_to_input": {
                        "type": "string",
                        "description": "Specifies whether the output fields will be appended to the input dataset or saved as a new output table or feature class. If you append the fields to the input, the output coordinate system environme...",
                        "default": None
                },
                "output_features": {
                        "type": "string",
                        "description": "The output features containing the smoothed values as well as fields for the time window and number of neighbors.",
                        "default": None
                },
                "id_field": {
                        "type": "string",
                        "description": "The integer or text field containing a unique ID for each time series. All records with the same value of this field are part of the same time series.",
                        "default": None
                },
                "apply_shorter_window": {
                        "type": "string",
                        "description": "Specifies whether the time window will be shortened at the beginning and end of each time series.APPLY_SHORTER_WINDOW\u2014The time window will be shortened at the start and end of the time series so that ...",
                        "default": None
                },
                "enable_time_series_popups": {
                        "type": "string",
                        "description": "Specifies whether the output features or table will include pop-up charts showing the original and smoothed values of the time series.CREATE_POPUP\u2014The output will include pop-up charts. This is the de...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "time_field",
                "analysis_field"
        ]
},
    "calculate_field": {
        "name": "calculate_field",
        "description": "Calculates the values of a field for a feature class, feature layer, or raster.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The table containing the field that will be updated with the new calculation."
                },
                "field": {
                        "type": "string",
                        "description": "The field that will be updated with the new calculation.If a field with the specified name does not exist in the input table, it will be added."
                },
                "expression": {
                        "type": "string",
                        "description": "The simple calculation expression used to create a value that will populate the selected rows."
                },
                "expression_type": {
                        "type": "string",
                        "description": "Specifies the type of expression that will be used.PYTHON3\u2014The Python expression type will be used.ARCADE\u2014The Arcade expression type will be used.SQL\u2014The SQL expression type will be used.VB\u2014The VBScri...",
                        "default": None
                },
                "code_block": {
                        "type": "string",
                        "description": "A block of code that will be used for complex Python or VBScript expressions.",
                        "default": None
                },
                "field_type": {
                        "type": "string",
                        "description": "Specifies the field type of the new field. This parameter is only used when the field name does not exist in the input table.If\r\nthe field is of type text, the field will have a length of 512,\r\nunless...",
                        "default": None
                },
                "enforce_domains": {
                        "type": "string",
                        "description": "Specifies whether field domain rules will be enforced.ENFORCE_DOMAINS\u2014Field domain rules will be enforced.NO_ENFORCE_DOMAINS\u2014Field domain rules will not be enforced. This is the default.",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "field",
                "expression"
        ]
},
    "calculate_geometry_attributes": {
        "name": "calculate_geometry_attributes",
        "description": "Adds information to a feature's attribute fields representing the spatial or geometric characteristics and location of each feature, such as length or area and x-, y-, z-coordinates, and m-values.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The features with a field that will be updated with geometry calculations."
                },
                "geometry_propertyfield_property": {
                        "type": "string",
                        "description": "The fields in which the specified geometry properties will be calculated. You can select an existing field or provide a new field name. If a new field name is provided, the field type is determined by..."
                },
                "length_unit": {
                        "type": "string",
                        "description": "Specifies the unit that will be used to calculate length.\r\nKILOMETERS\u2014The length unit will be kilometers.METERS\u2014The length unit will be meters.MILES_INT\u2014The length unit will be statute miles.NAUTICAL_...",
                        "default": None
                },
                "area_unit": {
                        "type": "string",
                        "description": "Specifies the unit that will be used to calculate area.\r\nSQUARE_KILOMETERS\u2014The area unit will be square kilometers.HECTARES\u2014The area unit will be hectares.SQUARE_METERS\u2014The area unit will be square me...",
                        "default": None
                },
                "coordinate_system": {
                        "type": "string",
                        "description": "The coordinate system in which the coordinates, length, and area will be calculated. The coordinate system of the input features is used by default.",
                        "default": None
                },
                "coordinate_format": {
                        "type": "string",
                        "description": "Specifies the coordinate format in which the x- and y-coordinates will be calculated. The coordinate format matching the input features' spatial reference units is used by default. \r\nSeveral coordinat...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "geometry_propertyfield_property"
        ]
}
}
