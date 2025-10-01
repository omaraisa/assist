# Generated ArcGIS Pro geostatistical-analyst AI Function Declarations
# Generated on 2025-10-01T15:05:41.308075
# Total tools: 36

functions_declarations = {
    "diffusion_interpolation_with_barriers": {
        "name": "diffusion_interpolation_with_barriers",
        "description": "Interpolates a surface using a kernel that is based upon the heat equation and allows one to use raster and feature  barriers to redefine distances between input points. Learn more about how Diffusion Interpolation With Barriers works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point features containing the z-values to be interpolated."
                },
                "z_field": {
                        "type": "string",
                        "description": "Field that holds a height or magnitude value for each point. This can be a numeric field or the Shape field if the input features contain z-values or m-values."
                },
                "out_ga_layer": {
                        "type": "string",
                        "description": "The geostatistical layer produced. This layer is required output only if no output raster is requested.",
                        "default": null
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster. This raster is required output only if no output geostatistical layer is requested.",
                        "default": null
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size at which the output raster will be created.\r\nThis value can be explicitly set in the Environments by the  Cell Size parameter.If not set, it is the shorter of the width or the height of ...",
                        "default": null
                },
                "in_barrier_features": {
                        "type": "string",
                        "description": "Absolute barrier features using non-Euclidean distances rather than line-of-sight distances.",
                        "default": null
                },
                "bandwidth": {
                        "type": "string",
                        "description": "Used to specify the maximum distance at which data points are used for prediction. With increasing bandwidth, prediction bias increases and prediction variance decreases.",
                        "default": null
                },
                "number_iterations": {
                        "type": "string",
                        "description": "The iteration count controls the accuracy of the numerical solution because the model solves the diffusion equation numerically. The larger this number, the more accurate the predictions, yet the long...",
                        "default": null
                },
                "weight_field": {
                        "type": "string",
                        "description": "Used to emphasize an observation. The larger the weight, the more impact it has on the prediction. For coincident observations, assign the largest weight to the most reliable measurement.",
                        "default": null
                },
                "in_additive_barrier_raster": {
                        "type": "string",
                        "description": "The travel distance from one raster cell to the next based on this formula:(average cost value in the neighboring cells) x (distance between cell centers)",
                        "default": null
                },
                "in_cumulative_barrier_raster": {
                        "type": "string",
                        "description": "The travel distance from one raster cell to the next based on this formula:(difference between cost values in the neighboring cells) + (distance between cell centers)",
                        "default": null
                },
                "in_flow_barrier_raster": {
                        "type": "string",
                        "description": "A flow barrier is used when interpolating data with preferential direction of data variation, based on this formula:Indicator (cost values in the to neighboring cell &gt; cost values in the from neigh...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "z_field"
        ]
},
    "ebk_regression_prediction": {
        "name": "ebk_regression_prediction",
        "description": "EBK Regression Prediction is a geostatistical interpolation method that uses Empirical Bayesian Kriging with explanatory variable rasters that are known to affect the value of the data that you are interpolating. This approach combines kriging with regression analysis to make predictions that are more accurate than either regression or kriging can achieve on their own. Learn more about EBK Regression Prediction",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point features containing the field that will be interpolated."
                },
                "dependent_field": {
                        "type": "string",
                        "description": "The field of the Input dependent variable features containing the values of the dependent variable. This is the field that will be interpolated."
                },
                "in_explanatory_rastersin_explanatory_raster": {
                        "type": "string",
                        "description": "Input rasters representing the explanatory variables that will be used to build the regression model. These rasters should represent variables that are known to influence the values of the dependent v..."
                },
                "out_ga_layer": {
                        "type": "string",
                        "description": "The output geostatistical layer displaying the result of the interpolation."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster displaying the result of the interpolation. The default cell size will be the maximum of the cell sizes of the Input explanatory variable rasters. To use a different cell size, use t...",
                        "default": null
                },
                "out_diagnostic_feature_class": {
                        "type": "string",
                        "description": "Output polygon feature class that shows the regions of each local model and contains fields with diagnostic information for the local models. For each subset, a polygon will be created that surrounds ...",
                        "default": null
                },
                "measurement_error_field": {
                        "type": "string",
                        "description": "A field that specifies the measurement error for each point in the dependent variable features. For each point, the value of this field should correspond to one standard deviation of the measured valu...",
                        "default": null
                },
                "min_cumulative_variance": {
                        "type": "string",
                        "description": "Defines the minimum cumulative percent of variance from the principal components of the explanatory variable rasters. Before building the regression model, the principal components of the explanatory ...",
                        "default": null
                },
                "in_subset_features": {
                        "type": "string",
                        "description": "Polygon features defining where the local models will be calculated. The points inside each polygon will be used for the local models. This parameter is useful when you know that the values of the dep...",
                        "default": null
                },
                "transformation_type": {
                        "type": "string",
                        "description": "Type of transformation to be applied to the input data.NONE\u2014Do not apply any transformation. This is the default.EMPIRICAL\u2014Multiplicative Skewing transformation with Empirical base function.LOGEMPIRIC...",
                        "default": null
                },
                "semivariogram_model_type": {
                        "type": "string",
                        "description": "The semivariogram model that will be used for the interpolation.\r\nLearn more about the semivariogram models in EBK Regression Prediction\r\nEXPONENTIAL\u2014Exponential semivariogramNUGGET\u2014Nugget semivariogr...",
                        "default": null
                },
                "max_local_points": {
                        "type": "string",
                        "description": "The input data will automatically be divided into subsets that do not have more than this number of points. If Subset polygon features are supplied, the value of this parameter will be ignored.",
                        "default": null
                },
                "overlap_factor": {
                        "type": "string",
                        "description": "A factor representing the degree of overlap between local models (also called subsets). Each input point can fall into several subsets, and the overlap factor specifies the average number of subsets t...",
                        "default": null
                },
                "number_simulations": {
                        "type": "string",
                        "description": "The number of simulated semivariograms of each local model. Using more simulations will make the model calculations more stable, but the model will take longer to calculate.",
                        "default": null
                },
                "search_neighborhood": {
                        "type": "string",
                        "description": "Defines which surrounding points will be used to control the output. Standard is the default.The following are Search Neighborhood classes: SearchNeighborhoodStandardCircular and SearchNeighborhoodSmo...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "dependent_field",
                "in_explanatory_rastersin_explanatory_raster",
                "out_ga_layer"
        ]
},
    "empirical_bayesian_kriging": {
        "name": "empirical_bayesian_kriging",
        "description": "Empirical Bayesian kriging is an interpolation method that accounts for the error in estimating the underlying semivariogram through repeated simulations. What is Empirical Bayesian Kriging?",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point features containing the z-values to be interpolated."
                },
                "z_field": {
                        "type": "string",
                        "description": "Field that holds a height or magnitude value for each point. This can be a numeric field or the Shape field if the input features contain z-values or m-values."
                },
                "out_ga_layer": {
                        "type": "string",
                        "description": "The geostatistical layer produced. This layer is required output only if no output raster is requested.",
                        "default": null
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster. This raster is required output only if no output geostatistical layer is requested.",
                        "default": null
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size at which the output raster will be created.This value can be explicitly set in the Environments by the  Cell Size parameter.If not set, it is the shorter of the width or the height of th...",
                        "default": null
                },
                "transformation_type": {
                        "type": "string",
                        "description": "Type of transformation to be applied to the input data.NONE\u2014Do not apply any transformation. This is the default.EMPIRICAL\u2014Multiplicative Skewing transformation with Empirical base function.LOGEMPIRIC...",
                        "default": null
                },
                "max_local_points": {
                        "type": "string",
                        "description": "The input data will automatically be divided into groups that do not have more than this number of points.",
                        "default": null
                },
                "overlap_factor": {
                        "type": "string",
                        "description": "A factor representing the degree of overlap between local models (also called subsets). Each input point can fall into several subsets, and the overlap factor specifies the average number of subsets t...",
                        "default": null
                },
                "number_semivariograms": {
                        "type": "string",
                        "description": "The number of simulated semivariograms of each local model.",
                        "default": null
                },
                "search_neighborhood": {
                        "type": "string",
                        "description": "Defines which surrounding points will be used to control the output. Standard Circular is the default.The following are Search Neighborhood classes: SearchNeighborhoodStandardCircular and SearchNeighb...",
                        "default": null
                },
                "output_type": {
                        "type": "string",
                        "description": "Surface type to store the interpolation results.For more information about the output surface types, see What output surface types can the interpolation models generate?\r\nPREDICTION\u2014Prediction surface...",
                        "default": null
                },
                "quantile_value": {
                        "type": "string",
                        "description": "The quantile value for which the output raster will be generated.",
                        "default": null
                },
                "threshold_type": {
                        "type": "string",
                        "description": "Specifies whether to calculate the probability of exceeding or not exceeding the specified threshold.EXCEED\u2014Probability values exceed the threshold. This is the default.NOT_EXCEED\u2014Probability values w...",
                        "default": null
                },
                "probability_threshold": {
                        "type": "string",
                        "description": "The probability threshold value. If left empty, the median (50th quantile) of the input data will be used.",
                        "default": null
                },
                "semivariogram_model_type": {
                        "type": "string",
                        "description": "The semivariogram model that will be used for the interpolation.POWER\u2014Power semivariogramLINEAR\u2014Linear semivariogramTHIN_PLATE_SPLINE\u2014Thin Plate Spline semivariogramEXPONENTIAL\u2014Exponential semivariogr...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "z_field"
        ]
},
    "empirical_bayesian_kriging_3d": {
        "name": "empirical_bayesian_kriging_3d",
        "description": "Interpolates 3D points using Empirical Bayesian Kriging methodology. All points must have x-, y-, and z-coordinates and a measured value to be interpolated. The output is a 3D geostatistical layer that calculates and renders itself as a 2D transect at a given elevation. The elevation of the layer can be changed using the range slider, and the layer will update to show the interpolated predictions for the new elevation. 3D interpolation has the following potential applications:\r\nOceanographers can create maps of dissolved oxygen and salinity at various depths in the ocean.Atmospheric scientists can create models for pollution and greenhouse gasses throughout the atmosphere.Geologists can predict subsurface geologic properties such as mineral concentrations and porosity. Learn more about Empirical Bayesian Kriging 3D",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point features containing the field that will be interpolated."
                },
                "elevation_field": {
                        "type": "string",
                        "description": "The field of the input features containing the elevation value of each input point.If the elevation values are stored as geometry attributes in Shape.Z, it is recommended that you use that field. If t..."
                },
                "value_field": {
                        "type": "string",
                        "description": "The field of the input features containing the measured values that will be interpolated."
                },
                "out_ga_layer": {
                        "type": "string",
                        "description": "The output geostatistical layer that will display the interpolation result."
                },
                "elevation_units": {
                        "type": "string",
                        "description": "The units of the elevation field.If Shape.Z is provided as the elevation field, the units will automatically match the z-units of the vertical coordinate system.INCH\u2014Elevations are in U.S. survey inch...",
                        "default": null
                },
                "measurement_error_field": {
                        "type": "string",
                        "description": "The field of the input features containing measurement error values for each point. The value should correspond to one standard deviation of the measured value of each point. Use this field if the mea...",
                        "default": null
                },
                "semivariogram_model_type": {
                        "type": "string",
                        "description": "The semivariogram model that will be used for the interpolation.\r\nPOWER\u2014The Power semivariogram model will be used.LINEAR\u2014The Linear semivariogram model will be used.THIN_PLATE_SPLINE\u2014The Thin Plate S...",
                        "default": null
                },
                "transformation_type": {
                        "type": "string",
                        "description": "The type of transformation that will be applied to the input features.NONE\u2014No transformation will be applied. This is the default.EMPIRICAL\u2014Multiplicative Skewing transformation with Empirical base fu...",
                        "default": null
                },
                "subset_size": {
                        "type": "string",
                        "description": "The size of the subset. The input data will automatically be divided into subsets before processing. This parameter controls the number of points that will be in each subset.",
                        "default": null
                },
                "overlap_factor": {
                        "type": "string",
                        "description": "A factor representing the degree of overlap between local models (also called subsets).Each input point can fall into several subsets, and the overlap factor specifies the average number of subsets in...",
                        "default": null
                },
                "number_simulations": {
                        "type": "string",
                        "description": "The number of simulated semivariograms that will be used for each local model.Using more simulations will make the model calculations more stable, but the model will take longer to calculate.",
                        "default": null
                },
                "trend_removal": {
                        "type": "string",
                        "description": "Specifies the order of trend removal in the vertical direction.For most 3D data, the values of the points change faster vertically than horizontally. Removing trend in the vertical direction will help...",
                        "default": null
                },
                "elev_inflation_factor": {
                        "type": "string",
                        "description": "A constant value that is multiplied by the Elevation field value prior to subsetting and model estimation. For most 3D data, the values of the points change faster vertically than horizontally, and th...",
                        "default": null
                },
                "search_neighborhood": {
                        "type": "string",
                        "description": "Specifies the number and orientation of the neighbors using the SearchNeighborhoodStandard3D class.\r\nStandard3D\r\n radius\u2014The length of the radius of the search neighborhood. nbrMax\u2014The maximum number ...",
                        "default": null
                },
                "output_elevation": {
                        "type": "string",
                        "description": "The default elevation of the out_ga_layer parameter value.\r\nThe geostatistical layer will draw as a horizontal surface at a given elevation, and this parameter specifies this elevation. After it's cre...",
                        "default": null
                },
                "output_type": {
                        "type": "string",
                        "description": "Surface type to store the interpolation results.For more information about output surface types, see What output surface types can the interpolation models generate.\r\nPREDICTION\u2014Prediction surfaces ar...",
                        "default": null
                },
                "quantile_value": {
                        "type": "string",
                        "description": "The quantile value for which the output layer will be generated.",
                        "default": null
                },
                "threshold_type": {
                        "type": "string",
                        "description": "Specifies whether to calculate the probability that a value exceeds or does not exceed the specified threshold.EXCEED\u2014The probability that the value exceeds the threshold will be calculated. This is t...",
                        "default": null
                },
                "probability_threshold": {
                        "type": "string",
                        "description": "The probability threshold value. If no value is provided, the median (50th quantile) of the input data will be used.",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "elevation_field",
                "value_field",
                "out_ga_layer"
        ]
},
    "global_polynomial_interpolation": {
        "name": "global_polynomial_interpolation",
        "description": "Fits a smooth surface that is defined by a mathematical function (a polynomial) to the input sample points. Learn more about how Global Polynomial Interpolation works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point features containing the z-values to be interpolated."
                },
                "z_field": {
                        "type": "string",
                        "description": "Field that holds a height or magnitude value for each point. This can be a numeric field or the Shape field if the input features contain z-values or m-values."
                },
                "out_ga_layer": {
                        "type": "string",
                        "description": "The geostatistical layer produced. This layer is required output only if no output raster is requested.",
                        "default": null
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster. This raster is required output only if no output geostatistical layer is requested.",
                        "default": null
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size at which the output raster will be created.\r\nThis value can be explicitly set in the Environments by the  Cell Size parameter.If not set, it is the shorter of the width or the height of ...",
                        "default": null
                },
                "power": {
                        "type": "string",
                        "description": "The order of the polynomial.",
                        "default": null
                },
                "weight_field": {
                        "type": "string",
                        "description": "Used to emphasize an observation. The larger the weight, the more impact it has on the prediction. For coincident observations, assign the largest weight to the most reliable measurement.",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "z_field"
        ]
},
    "idw": {
        "name": "idw",
        "description": "Uses the measured values surrounding the prediction location to predict a value for any unsampled location, based on the assumption that things that are close to one another are more alike than those that are farther apart. How IDW works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point features containing the z-values to be interpolated."
                },
                "z_field": {
                        "type": "string",
                        "description": "Field that holds a height or magnitude value for each point. This can be a numeric field or the Shape field if the input features contain z-values or m-values."
                },
                "out_ga_layer": {
                        "type": "string",
                        "description": "The geostatistical layer produced. This layer is required output only if no output raster is requested.",
                        "default": null
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster. This raster is required output only if no output geostatistical layer is requested.",
                        "default": null
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size at which the output raster will be created.This value can be explicitly set in the Environments by the  Cell Size parameter.If not set, it is the shorter of the width or the height of th...",
                        "default": null
                },
                "power": {
                        "type": "string",
                        "description": "The exponent of distance that controls the significance of surrounding points on the interpolated value. A higher power results in less influence from distant points.",
                        "default": null
                },
                "search_neighborhood": {
                        "type": "string",
                        "description": "Defines which surrounding points will be used to control the output. Standard is the default.The following are Search Neighborhood classes: SearchNeighborhoodStandard, SearchNeighborhoodSmooth, Search...",
                        "default": null
                },
                "weight_field": {
                        "type": "string",
                        "description": "Used to emphasize an observation. The larger the weight, the more impact it has on the prediction. For coincident observations, assign the largest weight to the most reliable measurement.",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "z_field"
        ]
},
    "idw_3d": {
        "name": "idw_3d",
        "description": "Interpolates the values of 3D points using inverse distance weighting (IDW) and creates a voxel layer and source file (.nc) of the predicted values.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The 3D point features that contain the field that will be interpolated. The points must be in a projected coordinate system."
                },
                "value_field": {
                        "type": "string",
                        "description": "The field from the input features containing the measured values that will be interpolated."
                },
                "out_netcdf_file": {
                        "type": "string",
                        "description": "The output netCDF file that will contain the predicted values in a 3D grid. This file can be used as the data source of a voxel layer."
                },
                "power": {
                        "type": "string",
                        "description": "The power value that will be used to weight the values of neighboring features when calculating predictions. A higher power results in higher influence to closer points. The value must be between 1 an...",
                        "default": null
                },
                "elev_inflation_factor": {
                        "type": "string",
                        "description": "A constant value that is multiplied to the z-coordinates of the input features prior to finding neighbors and calculating distances. For most 3D data, the values of the points change faster vertically...",
                        "default": null
                },
                "out_cv_features": {
                        "type": "string",
                        "description": "A feature class of the cross validation statistics for each input point. The feature class will contain two scatter plots.",
                        "default": null
                },
                "x_spacing": {
                        "type": "string",
                        "description": "The spacing between each gridded point in the x-dimension.\r\nThe default value creates 40 points along the output x-extent.",
                        "default": null
                },
                "y_spacing": {
                        "type": "string",
                        "description": "The spacing between each gridded point in the y-dimension.\r\nThe default value creates 40 points along the output y-extent.",
                        "default": null
                },
                "elevation_spacing": {
                        "type": "string",
                        "description": "The spacing between each gridded point in the elevation (z) dimension.\r\nThe default value creates 40 points along the output z-extent.",
                        "default": null
                },
                "in_study_area": {
                        "type": "string",
                        "description": "The polygon features that represent the study area. Only points that are within the study area are saved in the output netCDF file.\r\nWhen visualized as a voxel layer, only voxels within the study area...",
                        "default": null
                },
                "min_elev_raster": {
                        "type": "string",
                        "description": "The  elevation raster that will be used to clip the bottom of the voxel layer. Only voxels above this elevation raster will be assigned predictions. For example, if you use a ground elevation raster, ...",
                        "default": null
                },
                "max_elev_raster": {
                        "type": "string",
                        "description": "The  elevation raster that will be used to clip the top of the voxel layer. Only voxels below this elevation raster will be assigned predictions. For example, if you use a ground elevation raster, the...",
                        "default": null
                },
                "search_neighborhood": {
                        "type": "string",
                        "description": "Specifies the number and orientation of the neighbors using the SearchNeighborhoodStandard3D class.\r\nStandard3D\r\n radius\u2014The length of the radius of the search neighborhood. If no value is provided, a...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "value_field",
                "out_netcdf_file"
        ]
},
    "kernel_interpolation_with_barriers": {
        "name": "kernel_interpolation_with_barriers",
        "description": "A moving window predictor that uses the shortest distance between points so that points on either side of the line barriers are connected. How Kernel Interpolation With Barriers works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point features containing the z-values to be interpolated."
                },
                "z_field": {
                        "type": "string",
                        "description": "Field that holds a height or magnitude value for each point. This can be a numeric field or the Shape field if the input features contain z-values or m-values."
                },
                "out_ga_layer": {
                        "type": "string",
                        "description": "The geostatistical layer produced. This layer is required output only if no output raster is requested.",
                        "default": null
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster. This raster is required output only if no output geostatistical layer is requested.",
                        "default": null
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size at which the output raster will be created.This value can be explicitly set in the Environments by the  Cell Size parameter.If not set, it is the shorter of the width or the height of th...",
                        "default": null
                },
                "in_barrier_features": {
                        "type": "string",
                        "description": "Absolute barrier features using non-Euclidean distances rather than line-of-sight distances.",
                        "default": null
                },
                "kernel_function": {
                        "type": "string",
                        "description": "The kernel function used in the simulation.EXPONENTIAL\u2014 The function grows or decays proportionally.GAUSSIAN\u2014 Bell-shaped function that falls off quickly toward plus/minus infinity.QUARTIC\u2014 Fourth-ord...",
                        "default": null
                },
                "bandwidth": {
                        "type": "string",
                        "description": "Used to specify the maximum distance at which data points are used for prediction. With increasing bandwidth, prediction bias increases and prediction variance decreases.",
                        "default": null
                },
                "power": {
                        "type": "string",
                        "description": "Sets the order of the polynomial.",
                        "default": null
                },
                "ridge": {
                        "type": "string",
                        "description": "Used for the numerical stabilization of the solution of the system of linear equations. It does not influence predictions in the case of regularly distributed data without barriers. Predictions for ar...",
                        "default": null
                },
                "output_type": {
                        "type": "string",
                        "description": "Surface type to store the interpolation results.For more information about the output surface types, see What output surface types can the interpolation models generate?\r\n\r\nPREDICTION\u2014Prediction surfa...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "z_field"
        ]
},
    "local_polynomial_interpolation": {
        "name": "local_polynomial_interpolation",
        "description": "Fits the specified order (zero, first, second, third, and so on) polynomial, each within specified overlapping neighborhoods, to produce an output surface. How Local Polynomial Interpolation works",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point features containing the z-values to be interpolated."
                },
                "z_field": {
                        "type": "string",
                        "description": "Field that holds a height or magnitude value for each point. This can be a numeric field or the Shape field if the input features contain z-values or m-values."
                },
                "out_ga_layer": {
                        "type": "string",
                        "description": "The geostatistical layer produced. This layer is required output only if no output raster is requested.",
                        "default": null
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster. This raster is required output only if no output geostatistical layer is requested.",
                        "default": null
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size at which the output raster will be created.This value can be explicitly set in the Environments by the  Cell Size parameter.If not set, it is the shorter of the width or the height of th...",
                        "default": null
                },
                "power": {
                        "type": "string",
                        "description": "The order of the polynomial.",
                        "default": null
                },
                "search_neighborhood": {
                        "type": "string",
                        "description": "Defines which surrounding points will be used to control the output. Standard is the default.The following are Search Neighborhood classes: SearchNeighborhoodStandard, SearchNeighborhoodSmooth, Search...",
                        "default": null
                },
                "kernel_function": {
                        "type": "string",
                        "description": "The kernel function used in the simulation.\r\n\r\nEXPONENTIAL\u2014The function grows or decays proportionally.GAUSSIAN\u2014Bell-shaped function that falls off quickly toward plus or minus infinity.QUARTIC\u2014Fourth...",
                        "default": null
                },
                "bandwidth": {
                        "type": "string",
                        "description": "Used to specify the maximum distance at which data points are used for prediction. With increasing bandwidth, prediction bias increases and prediction variance decreases.",
                        "default": null
                },
                "use_condition_number": {
                        "type": "string",
                        "description": "Option to control the creation of prediction and prediction standard errors where the predictions are unstable. This option is only available for polynomials of order 1, 2, and 3.NO_USE_CONDITION_NUMB...",
                        "default": null
                },
                "condition_number": {
                        "type": "string",
                        "description": "Every invertible square matrix has a condition number that indicates how inaccurate the solution to the linear equations can be with a small change in the matrix coefficients (it can be due to impreci...",
                        "default": null
                },
                "weight_field": {
                        "type": "string",
                        "description": "Used to emphasize an observation. The larger the weight, the more impact it has on the prediction. For coincident observations, assign the largest weight to the most reliable measurement.",
                        "default": null
                },
                "output_type": {
                        "type": "string",
                        "description": "Surface type to store the interpolation results.For more information about the output surface types, see What output surface types can the interpolation models generate?\r\nPREDICTION\u2014Prediction surface...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "z_field"
        ]
},
    "moving_window_kriging": {
        "name": "moving_window_kriging",
        "description": "Recalculates the Range, Nugget, and Partial Sill semivariogram parameters based on a smaller neighborhood, moving through all location points. Learn more about how Moving Window Kriging works",
        "parameters": {
                "in_ga_model_source": {
                        "type": "string",
                        "description": "The geostatistical model source to be analyzed."
                },
                "in_datasets": {
                        "type": "string",
                        "description": "A GeostatisticalDatasets object.Alternatively, it can be a semicolon-delimited string of elements.  Each element is comprised of the following components:The catalog path and name to a dataset or the ..."
                },
                "in_locations": {
                        "type": "string",
                        "description": "Point locations where predictions will be performed."
                },
                "neighbors_max": {
                        "type": "string",
                        "description": "Number of neighbors to use in the moving window."
                },
                "out_featureclass": {
                        "type": "string",
                        "description": "Feature class storing the results."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size at which the output raster will be created.This value can be explicitly set in the Environments by the  Cell Size parameter.If not set, it is the shorter of the width or the height of th...",
                        "default": null
                },
                "out_surface_grid": {
                        "type": "string",
                        "description": "The prediction values in the output feature class are interpolated onto a raster using the Local polynomial interpolation method.",
                        "default": null
                }
        },
        "required": [
                "in_ga_model_source",
                "in_datasets",
                "in_locations",
                "neighbors_max",
                "out_featureclass"
        ]
},
    "nearest_neighbor_3d": {
        "name": "nearest_neighbor_3d",
        "description": "Creates a voxel layer source file (netCDF) from categorical 3D points by assigning each voxel the categories of the nearest neighbor in 3D. Learn more about voxel layers",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input points representing locations with known categories in 3D. The points must be in a projected coordinate system, and there must be at least three points."
                },
                "category_field": {
                        "type": "string",
                        "description": "The fields of the input features containing the categories of each point. For each field, the unique values of the field represent the categories of the field. Each field must be Text, Short, or Long ..."
                },
                "out_netcdf_file": {
                        "type": "string",
                        "description": "The output netCDF file containing categories in a 3D grid. Each point in the 3D grid is assigned the category of the closest input point. This file can be used as the data source of a voxel layer."
                },
                "x_spacing": {
                        "type": "string",
                        "description": "The spacing between each gridded point in the x-dimension.\r\nThe default value creates 40 points along the output x-extent.",
                        "default": null
                },
                "y_spacing": {
                        "type": "string",
                        "description": "The spacing between each gridded point in the y-dimension.\r\nThe default value creates 40 points along the output y-extent.",
                        "default": null
                },
                "elevation_spacing": {
                        "type": "string",
                        "description": "The spacing between each gridded point in the elevation (z) dimension.\r\nThe default value creates 40 points along the output z-extent.",
                        "default": null
                },
                "elev_inflation_factor": {
                        "type": "string",
                        "description": "A constant value that is multiplied to the elevation (z-coordinates) of the input points prior to finding the nearest neighbor. Values larger than 1  will search farther horizontally than vertically t...",
                        "default": null
                },
                "in_study_area": {
                        "type": "string",
                        "description": "The polygon features that represent the study area. Only points that are within the study area are saved in the output netCDF file.\r\nWhen visualized as a voxel layer, only voxels within the study area...",
                        "default": null
                },
                "min_elev_raster": {
                        "type": "string",
                        "description": "The  elevation raster that will be used to clip the bottom of the voxel layer. Only voxels above this elevation raster will be assigned predictions. For example, if you use a ground elevation raster, ...",
                        "default": null
                },
                "max_elev_raster": {
                        "type": "string",
                        "description": "The  elevation raster that will be used to clip the top of the voxel layer. Only voxels below this elevation raster will be assigned predictions. For example, if you use a ground elevation raster, the...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "category_field",
                "out_netcdf_file"
        ]
},
    "radial_basis_functions": {
        "name": "radial_basis_functions",
        "description": "Uses one of five basis functions to interpolate a surfaces that passes through the input points exactly. Learn more about how radial basis functions work",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point features containing the z-values to be interpolated."
                },
                "z_field": {
                        "type": "string",
                        "description": "Field that holds a height or magnitude value for each point. This can be a numeric field or the Shape field if the input features contain z-values or m-values."
                },
                "out_ga_layer": {
                        "type": "string",
                        "description": "The geostatistical layer produced. This layer is required output only if no output raster is requested.",
                        "default": null
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output raster. This raster is required output only if no output geostatistical layer is requested.",
                        "default": null
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size at which the output raster will be created.\r\nThis value can be explicitly set in the Environments by the  Cell Size parameter.If not set, it is the shorter of the width or the height of ...",
                        "default": null
                },
                "search_neighborhood": {
                        "type": "string",
                        "description": "Defines which surrounding points will be used to control the output. Standard is the default.The following are Search Neighborhood classes: SearchNeighborhoodStandard and SearchNeighborhoodStandardCir...",
                        "default": null
                },
                "radial_basis_functions": {
                        "type": "string",
                        "description": "There are five radial basis functions available.THIN_PLATE_SPLINE\u2014Thin-plate spline functionSPLINE_WITH_TENSION\u2014 Spline with tension functionCOMPLETELY_REGULARIZED_SPLINE\u2014 Completely regularized splin...",
                        "default": null
                },
                "small_scale_parameter": {
                        "type": "string",
                        "description": "Used to calculate the weights assigned to the points located in the moving window. Each of the radial basis functions has a parameter that controls the degree of small-scale variation of the surface. ...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "z_field"
        ]
},
    "create_spatially_balanced_points": {
        "name": "create_spatially_balanced_points",
        "description": "Creates a set of sample points based on inclusion probabilities, resulting in a spatially balanced sample design. This tool is typically used for designing a monitoring network by suggesting locations to take samples, and a preference for particular locations can be defined using an inclusion probability raster. Learn more about how Create Spatially Balanced Points works",
        "parameters": {
                "in_probability_raster": {
                        "type": "string",
                        "description": "Defines the inclusion probabilities for each location in the area of interest. The location values must range from 0 (low inclusion probability) to 1 (high inclusion probability)."
                },
                "number_output_points": {
                        "type": "string",
                        "description": "The number of sample locations that will be created."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing the selected sample locations and their inclusion probabilities."
                }
        },
        "required": [
                "in_probability_raster",
                "number_output_points",
                "out_feature_class"
        ]
},
    "densify_sampling_network": {
        "name": "densify_sampling_network",
        "description": "Uses a predefined geostatistical kriging layer to determine where new monitoring stations should be built.  It can also be used to determine which monitoring stations should be removed from an existing network.",
        "parameters": {
                "in_geostat_layer": {
                        "type": "string",
                        "description": "Input a geostatistical layer resulting from a Kriging model."
                },
                "number_output_points": {
                        "type": "string",
                        "description": "Specify how many sample locations to generate."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The name of the output feature class."
                },
                "selection_criteria": {
                        "type": "string",
                        "description": "Methods to densify a sampling network.STDERR\u2014Standard error of prediction criteriaSTDERR_THRESHOLD\u2014Standard error threshold criteriaQUARTILE_THRESHOLD\u2014 Lower quartile threshold criteriaQUARTILE_THRESH...",
                        "default": null
                },
                "threshold": {
                        "type": "string",
                        "description": "The threshold value used to densify the sampling network.\r\nThis parameter is only applicable when Standard error threshold, Lower quartile threshold, or Upper quartile threshold selection criteria is ...",
                        "default": null
                },
                "in_weight_raster": {
                        "type": "string",
                        "description": "A raster used to determine which locations to weight for  preference.",
                        "default": null
                },
                "in_candidate_point_features": {
                        "type": "string",
                        "description": "Sample locations to pick from.",
                        "default": null
                },
                "inhibition_distance": {
                        "type": "string",
                        "description": "Used to prevent any samples being placed within this distance from each other.",
                        "default": null
                }
        },
        "required": [
                "in_geostat_layer",
                "number_output_points",
                "out_feature_class"
        ]
},
    "extract_values_to_table": {
        "name": "extract_values_to_table",
        "description": "Extracts cell values from a set of rasters to a table, based on a point or polygon feature class.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The points or polygon features to be created."
                },
                "in_rastersin_raster": {
                        "type": "string",
                        "description": "The  rasters must all have the same extent, coordinate system, and cell size."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table contains a record for each point and each raster that has data. If polygon features are input, they are converted to points that coincide with the raster cell centers."
                },
                "out_raster_names_table": {
                        "type": "string",
                        "description": "Saves the names of the Input rasters to disc.",
                        "default": null
                },
                "add_warning_field": {
                        "type": "string",
                        "description": "Records if input features are partially or completely covered by the Input rasters.ADD_WARNING_FIELD\u2014Warning field is added to the output table and populated with a P when a feature is partially cover...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "in_rastersin_raster",
                "out_table"
        ]
},
    "gaussian_geostatistical_simulations": {
        "name": "gaussian_geostatistical_simulations",
        "description": "Performs a conditional or unconditional geostatistical simulation based on a Simple Kriging model. The simulated rasters can be considered equally probable realizations of the kriging model. Learn more about how Gaussian Geostatistical Simulations works",
        "parameters": {
                "in_geostat_layer": {
                        "type": "string",
                        "description": "Input a geostatistical layer resulting from a Simple Kriging model."
                },
                "number_of_realizations": {
                        "type": "string",
                        "description": "The number of simulations to perform."
                },
                "output_workspace": {
                        "type": "string",
                        "description": "Stores all the simulation results. The workspace can be either a folder or a geodatabase."
                },
                "output_simulation_prefix": {
                        "type": "string",
                        "description": "A one- to three-character alphanumeric prefix that is automatically added to the output dataset names."
                },
                "in_conditioning_features": {
                        "type": "string",
                        "description": "The features used to condition the realizations. If left blank, unconditional realizations are produced.",
                        "default": null
                },
                "conditioning_field": {
                        "type": "string",
                        "description": "The field used to condition the realizations. If left blank, unconditional realizations are produced.",
                        "default": null
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size at which the output raster will be created.This value can be explicitly set in the Environments by the  Cell Size parameter.If not set, it is the shorter of the width or the height of th...",
                        "default": null
                },
                "in_bounding_dataset": {
                        "type": "string",
                        "description": "Limits the analysis to these features' bounding polygon. If point features are entered, then a convex hull polygon is automatically created. Realizations are then performed within that polygon. If bou...",
                        "default": null
                },
                "save_simulated_rasters": {
                        "type": "string",
                        "description": "Specifies whether or not the simulated rasters are saved to disk.\r\nSAVE_SIMULATIONS\u2014Indicates that the simulated rasters will be saved to disk.DO_NOT_SAVE_SIMULATIONS\u2014Indicates that the simulated rast...",
                        "default": null
                },
                "quantile": {
                        "type": "string",
                        "description": "The quantile value for which the output raster will be generated.",
                        "default": null
                },
                "threshold": {
                        "type": "string",
                        "description": "The threshold value for which the output raster will be generated, as the percentage of the number of times the set threshold was exceeded, on a cell-by-cell basis.",
                        "default": null
                },
                "in_stats_polygons": {
                        "type": "string",
                        "description": "These polygons represent areas of interest for which summary statistics are calculated.\r\nIf in_stats_polygons are provided, the output polygon feature class will be saved in the location defined by ou...",
                        "default": null
                },
                "raster_stat_type": {
                        "type": "string",
                        "description": "The simulated rasters are postprocessed on a cell-by-cell basis, and each selected statistics type is calculated and reported in an output raster.MIN\u2014Calculates the minimum (smallest value).MAX\u2014Calcul...",
                        "default": null
                },
                "conditioning_measurement_error_field": {
                        "type": "string",
                        "description": "A field that specifies the measurement error for each input point in the conditioning features. For each conditioning feature, the value of this field should correspond to one standard deviation of th...",
                        "default": null
                }
        },
        "required": [
                "in_geostat_layer",
                "number_of_realizations",
                "output_workspace",
                "output_simulation_prefix"
        ]
},
    "compare_geostatistical_layers": {
        "name": "compare_geostatistical_layers",
        "description": "Compares and ranks geostatistical layers using customizable criteria based on cross validation statistics. Interpolation results can be ranked based on a single criterion (such as highest prediction accuracy or lowest bias), weighted average ranks of multiple criteria, or hierarchical sorting of multiple criteria (in which ties by each of the criteria are broken by subsequent criteria in the hierarchy).  Exclusion criteria can also be used to exclude interpolation results from the comparison that do not meet minimal quality standards. The output is a table summarizing the cross validation statistics and ranks for each interpolation result.  Optionally, you can output a geostatistical layer of the interpolation result with highest rank to be used in further workflows.",
        "parameters": {
                "in_geostat_layersin_geostat_layer1_in_geostat_layer2": {
                        "type": "string",
                        "description": "The geostatistical layers representing interpolation results. Each layer will be compared and ranked."
                },
                "out_cv_table": {
                        "type": "string",
                        "description": "The output table containing cross validation statistics and ranks for each interpolation result. The final ranks of the interpolation results are stored in the RANK field."
                },
                "out_geostat_layer": {
                        "type": "string",
                        "description": "The output geostatistical layer of the interpolation result with highest rank. This interpolation result will have the value 1 in the RANK field of the output cross validation table.\r\nIf there are tie...",
                        "default": null
                },
                "comparison_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to compare and rank the interpolation results.SINGLE\u2014A single cross validation statistic will be used to compare and rank results, such as highest prediction acc...",
                        "default": null
                },
                "criterion": {
                        "type": "string",
                        "description": "Specifies the criterion that will be used to rank the interpolation results.\r\nACCURACY\u2014Results will be ranked by lowest root mean square error. This option measures how closely the cross validation pr...",
                        "default": null
                },
                "criteria_hierarchycriteria1_tol_type1_tol_val1_criteria2_tol_type2_tol_val2": {
                        "type": "string",
                        "description": "The hierarchy of criteria that will be used for hierarchical sorting with tolerances. Provide multiple criteria in priority order with the first being most important.  The interpolation results are ra...",
                        "default": null
                },
                "weighted_criteria1_weight1_criteria2_weight2": {
                        "type": "string",
                        "description": "The multiple criteria with weights that will be used to rank interpolation results.  For each row, provide a criterion and a weight.  The interpolation results will be ranked independently by each of ...",
                        "default": null
                },
                "exclusion_criteria1_value1_criteria2_value2": {
                        "type": "string",
                        "description": "The criteria and associated values that will be used to exclude interpolation results from the comparison.  Excluded results will not receive ranks and will have the value No in the Included field of ...",
                        "default": null
                }
        },
        "required": [
                "in_geostat_layersin_geostat_layer1_in_geostat_layer2",
                "out_cv_table"
        ]
},
    "cross_validation": {
        "name": "cross_validation",
        "description": "Removes one data location and predicts the associated data using the data at the rest of the locations. The primary use for this tool is to compare the predicted value to the observed value in order to obtain useful information about some of your model parameters. Learn more about performing cross validation and validation",
        "parameters": {
                "in_geostat_layer": {
                        "type": "string",
                        "description": "The geostatistical layer to be analyzed."
                },
                "out_point_feature_class": {
                        "type": "string",
                        "description": "Stores the cross-validation statistics at each location in the geostatistical layer.",
                        "default": null
                }
        },
        "required": [
                "in_geostat_layer"
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
                        "default": null
                },
                "determine_direction": {
                        "type": "string",
                        "description": "Specifies whether the direction of the strongest trend will be determined by the tool. The direction of strongest trend is determined by finding the direction that maximizes the R-squared value for th...",
                        "default": null
                },
                "order": {
                        "type": "string",
                        "description": "Specifies the order of the polynomial that will be fitted to the data values.1\u2014First order (linear) polynomial will be used.2\u2014Second order (quadratic) polynomial will be used.3\u2014Third order (cubic) pol...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "analysis_field"
        ]
},
    "exploratory_interpolation": {
        "name": "exploratory_interpolation",
        "description": "Generates various interpolation results from input point features and a field. The interpolation results are then compared and ranked using customizable criteria based on cross validation statistics. Interpolation results can be ranked based on a single criterion (such as highest prediction accuracy or lowest bias), weighted average ranks of multiple criteria, or hierarchical sorting of multiple criteria (in which ties by each of the criteria are broken by subsequent criteria in the hierarchy).  Exclusion criteria can also be used to exclude interpolation results from the comparison that do not meet minimal quality standards. The output is a table summarizing the cross validation statistics and ranks for each interpolation result.  Optionally, you can output a geostatistical layer of the interpolation result with highest rank to be used in further workflows.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input points representing locations of points to be interpolated."
                },
                "value_field": {
                        "type": "string",
                        "description": "The field containing the values to be interpolated."
                },
                "out_cv_table": {
                        "type": "string",
                        "description": "The output table containing cross validation statistics and ranks for each interpolation result. The final ranks of the interpolation results are stored in the RANK field."
                },
                "out_geostat_layer": {
                        "type": "string",
                        "description": "The output geostatistical layer of the interpolation result with highest rank. This interpolation result will have the value 1 in the RANK field of the output cross validation table.\r\nIf there are tie...",
                        "default": null
                },
                "interp_methods": {
                        "type": "string",
                        "description": "Specifies the interpolation methods that will be performed on the input features and value field.\r\nFor each method specified, 1 to 5 interpolation results will be generated. By default, all methods wi...",
                        "default": null
                },
                "comparison_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to compare and rank the interpolation results.SINGLE\u2014A single cross validation statistic will be used to compare and rank results, such as highest prediction acc...",
                        "default": null
                },
                "criterion": {
                        "type": "string",
                        "description": "Specifies the criterion that will be used to rank the interpolation results.\r\nACCURACY\u2014Results will be ranked by lowest root mean square error. This option measures how closely the cross validation pr...",
                        "default": null
                },
                "criteria_hierarchycriteria1_tol_type1_tol_val1_criteria2_tol_type2_tol_val2": {
                        "type": "string",
                        "description": "The hierarchy of criteria that will be used for hierarchical sorting with tolerances. Provide multiple criteria in priority order with the first being most important.  The interpolation results are ra...",
                        "default": null
                },
                "weighted_criteria1_weight1_criteria2_weight2": {
                        "type": "string",
                        "description": "The multiple criteria with weights that will be used to rank interpolation results.  For each row, provide a criterion and a weight.  The interpolation results will be ranked independently by each of ...",
                        "default": null
                },
                "exclusion_criteria1_value1_criteria2_value2": {
                        "type": "string",
                        "description": "The criteria and associated values that will be used to exclude interpolation results from the comparison.  Excluded results will not receive ranks and will have the value No in the Included field of ...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "value_field",
                "out_cv_table"
        ]
},
    "generate_subset_polygons": {
        "name": "generate_subset_polygons",
        "description": "Generates nonoverlapping subset polygon features from a set of input points. The goal is to divide the points into compact, nonoverlapping subsets, and create polygon regions around each subset of points. The minimum and maximum number of points in each subset can be controlled. The process of generating subset polygon features begins by connecting all points with a linear curve and cutting this curve into segments. These segments are chosen in order to minimize the total squared distance from the center of the segment to each point in the segment given the minimum and maximum number of points that are allowed to be in each subset. Any overlaps between the segments are then removed, and new segments are created. After several iterations of segmentation and overlap removal, no overlaps will remain, and all points within each segment will be declared part of the same subset. Thiessen polygons are then generated for the input points, and all Thiessen polygons belonging to the same subset are dissolved into a single polygon feature.",
        "parameters": {
                "in_point_features": {
                        "type": "string",
                        "description": "The points that will be grouped into subsets."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The polygons defining the region of each subset. All points within a single polygon feature are considered part of the same subset. The polygon feature class will contain a field named PointCount that..."
                },
                "min_points_per_subset": {
                        "type": "string",
                        "description": "The minimum number of points that can be grouped into a subset. All subset polygons will contain at least this many points.",
                        "default": null
                },
                "max_points_per_subset": {
                        "type": "string",
                        "description": "The maximum number of points that can be grouped into a subset.\r\nEach subset will always contain fewer than two times the min_points_per_subset regardless of the maximum number provided. This is becau...",
                        "default": null
                },
                "coincident_points": {
                        "type": "string",
                        "description": "Specifies whether coincident points (points that are at the same location) are treated like a single point or as multiple individual points.If you intend to use the subset polygons as Subset polygon f...",
                        "default": null
                }
        },
        "required": [
                "in_point_features",
                "out_feature_class"
        ]
},
    "neighborhood_selection": {
        "name": "neighborhood_selection",
        "description": "Creates a layer of points based on a user-defined neighborhood. For example, you can create a selection of points in a circular neighborhood around a location defined by the input point.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The points that will be used to create a neighborhood selection."
                },
                "out_layer": {
                        "type": "string",
                        "description": "An output layer with the neighborhood selection."
                },
                "point_coord": {
                        "type": "string",
                        "description": "The neighborhood center's x,y-coordinate."
                },
                "neighbors_max": {
                        "type": "string",
                        "description": "The number of points that will be used in each sector. If a sector has the required number of points, all points in that sector will be used."
                },
                "neighbors_min": {
                        "type": "string",
                        "description": "The minimum number of points that will be used in each sector. If the minimum number of required points are not available in any given sector, the nearest available point outside the sector will be se..."
                },
                "minor_semiaxis": {
                        "type": "string",
                        "description": "The size of the minor semiaxis of the search neighborhood."
                },
                "major_semiaxis": {
                        "type": "string",
                        "description": "The size of the major semiaxis of the search neighborhood."
                },
                "angle": {
                        "type": "string",
                        "description": "The angle of rotation of the neighborhood axis."
                },
                "shape_type": {
                        "type": "string",
                        "description": "Species the geometry of the neighborhood.ONE_SECTOR\u2014The neighborhood will be a single ellipse.FOUR_SECTORS\u2014 The neighborhood will be an ellipse divided into four sectors.FOUR_SECTORS_SHIFTED\u2014 The neig...",
                        "default": null
                }
        },
        "required": [
                "in_dataset",
                "out_layer",
                "point_coord",
                "neighbors_max",
                "neighbors_min",
                "minor_semiaxis",
                "major_semiaxis",
                "angle"
        ]
},
    "semivariogram_sensitivity": {
        "name": "semivariogram_sensitivity",
        "description": "This tool performs a sensitivity analysis on the predicted values and associated standard errors by changing the model's semivariogram parameters (the nugget, partial sill, and major/minor ranges) within a percentage of the original values. The tool takes a geostatistical model source in order to populate these initial values of the nugget, partial sill, and major/minor ranges. The tool's output is a table indicating which parameter values were used and what the resulting predicted and standard error values were. If there are large fluctuations in the output with small changes in the model's parameter values, then you cannot have much confidence in the output. On the other hand, if changes in the output are small, then you can be confident in the model's predictions and make decisions based on its output.",
        "parameters": {
                "in_ga_model_source": {
                        "type": "string",
                        "description": "The geostatistical model source to be analyzed."
                },
                "in_datasets": {
                        "type": "string",
                        "description": "A GeostatisticalDatasets object.Alternatively, it can be a semicolon-delimited string of elements.  Each element is comprised of the following components:The catalog path and name to a dataset or the ..."
                },
                "in_locations": {
                        "type": "string",
                        "description": "Point locations where the sensitivity analysis is performed."
                },
                "nugget_span_percents": {
                        "type": "string",
                        "description": "The percentage subtracted and added to the Nugget parameter to create a range for a subsequent random Nugget parameter selection.",
                        "default": null
                },
                "nugget_calc_times": {
                        "type": "string",
                        "description": "Number of random Nugget values randomly sampled from the Nugget span.",
                        "default": null
                },
                "partialsill_span_percents": {
                        "type": "string",
                        "description": "Percentage subtracted from and added to the Partial Sill parameter to create a range for a random Partial Sill selection.",
                        "default": null
                },
                "partialsill_calc_times": {
                        "type": "string",
                        "description": "Number of Partial Sill values randomly sampled from the Partial Sill span.",
                        "default": null
                },
                "range_span_percents": {
                        "type": "string",
                        "description": "Percentage subtracted and added to the Major Range parameter to create a range for a random Major Range selection.",
                        "default": null
                },
                "range_calc_times": {
                        "type": "string",
                        "description": "Number of Major Range values randomly sampled from the Major Range span.",
                        "default": null
                },
                "minrange_span_percents": {
                        "type": "string",
                        "description": "Percentage subtracted and added to the Minor Range parameter to create a range for a random Minor Range selection.",
                        "default": null
                },
                "minrange_calc_times": {
                        "type": "string",
                        "description": "Number of Minor Range values randomly sampled from the Minor Range span.If Anisotropy has been set in the input geostatistical model source, a value is required.",
                        "default": null
                },
                "out_table": {
                        "type": "string",
                        "description": "Table storing the sensitivity results."
                }
        },
        "required": [
                "in_ga_model_source",
                "in_datasets",
                "in_locations",
                "out_table"
        ]
},
    "subset_features": {
        "name": "subset_features",
        "description": "Divides the records of a feature class or table into two subsets: one subset to be used as training data, and one subset to be used as test features to compare and validate the output surface.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The features or table from which subsets will be created."
                },
                "out_training_feature_class": {
                        "type": "string",
                        "description": "The subset of training features that will be created."
                },
                "out_test_feature_class": {
                        "type": "string",
                        "description": "The subset of test features that will be created.",
                        "default": null
                },
                "size_of_training_dataset": {
                        "type": "string",
                        "description": "The size of the output training feature class, entered either as a percentage of the input features or as an absolute number of features.",
                        "default": null
                },
                "subset_size_units": {
                        "type": "string",
                        "description": "Specifies whether the subset size value will be used as a percentage of the input features or as an absolute number of features.PERCENTAGE_OF_INPUT\u2014 The subset size will be used as a percentage of the...",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "out_training_feature_class"
        ]
},
    "areal_interpolation_layer_to_polygons": {
        "name": "areal_interpolation_layer_to_polygons",
        "description": "Reaggregates the predictions of an Areal Interpolation layer to a new set of polygons. Learn more about Areal Interpolation",
        "parameters": {
                "in_areal_interpolation_layer": {
                        "type": "string",
                        "description": "Input geostatistical layer resulting from an Areal Interpolation model."
                },
                "in_polygon_features": {
                        "type": "string",
                        "description": "The polygons where predictions and standard errors will be aggregated."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing the aggregated predictions and standard errors for the new polygons."
                },
                "append_all_fields": {
                        "type": "string",
                        "description": "Determines whether all fields will be copied from the input features to the output feature class.ALL\u2014 All fields from the input features will be copied to the output feature class. This is the default...",
                        "default": null
                }
        },
        "required": [
                "in_areal_interpolation_layer",
                "in_polygon_features",
                "out_feature_class"
        ]
},
    "calculate_z_value": {
        "name": "calculate_z_value",
        "description": "Uses the interpolation model in a geostatistical layer to predict a value at a single location.",
        "parameters": {
                "in_geostat_layer": {
                        "type": "string",
                        "description": "The geostatistical layer to be analyzed."
                },
                "point_coord": {
                        "type": "string",
                        "description": "The x,y coordinate of the point for which the Z-value will be calculated."
                }
        },
        "required": [
                "in_geostat_layer",
                "point_coord"
        ]
},
    "create_geostatistical_layer": {
        "name": "create_geostatistical_layer",
        "description": "Creates a new geostatistical layer. An  existing geostatistical layer  is required to populate the initial values for the new layer.",
        "parameters": {
                "in_ga_model_source": {
                        "type": "string",
                        "description": "The geostatistical model source to be analyzed."
                },
                "in_datasets": {
                        "type": "string",
                        "description": "A GeostatisticalDatasets object.Alternatively, it can be a semicolon-delimited string of elements.  Each element is comprised of the following components:The catalog path and name to a dataset or the ..."
                },
                "out_layer": {
                        "type": "string",
                        "description": "The geostatistical layer produced by the tool."
                }
        },
        "required": [
                "in_ga_model_source",
                "in_datasets",
                "out_layer"
        ]
},
    "ga_layer_3d_to_multidimensional_raster": {
        "name": "ga_layer_3d_to_multidimensional_raster",
        "description": "Exports a 3D geostatistical layer created using the Empirical Bayesian Kriging 3D tool to a multidimensional Cloud Raster Format (*.crf file) \r\nraster dataset. Tools in the Multidimensional Analysis toolset of the Image Analyst toolbox are designed to work directly on multidimensional rasters and can identify the 3D nature of the data. 3D geostatistical layers store continuous 3D interpolation results and appear as 2D horizontal slices at a given elevation.  The current elevation can be changed with the range slider, and the layer will calculate and render the predicted values of the new elevation.  Rasters of interpolated predictions can be extracted at any elevation using the GA Layer To Rasters tool.  The GA Layer 3D To Multidimensional Raster tool automates the process of extracting rasters at multiple elevations and stores them as a multidimensional raster dataset.",
        "parameters": {
                "in_3d_geostat_layer": {
                        "type": "string",
                        "description": "The 3D geostatistical layer representing the model to be exported to a multivariate raster dataset."
                },
                "out_multidimensional_raster": {
                        "type": "string",
                        "description": "The output raster dataset containing the results of exporting the geostatistical model.  The output must be saved as a Cloud Raster Format file (*.crf)."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output multidimensional raster.",
                        "default": null
                },
                "explicit_only": {
                        "type": "string",
                        "description": "Specifies whether elevations will be provided as an explicit list or an iterator will be used.EXPLICIT_VALUES\u2014Elevation values will be provided as a list.NO_EXPLICIT_VALUES\u2014Elevation values will be pr...",
                        "default": null
                },
                "min_elev": {
                        "type": "string",
                        "description": "The minimum elevation that will be used to start the iteration.",
                        "default": null
                },
                "max_elev": {
                        "type": "string",
                        "description": "The maximum elevation that will be used to stop the iteration.",
                        "default": null
                },
                "elev_interval": {
                        "type": "string",
                        "description": "The increment that the elevation will increase with each iteration.",
                        "default": null
                },
                "elev_values": {
                        "type": "string",
                        "description": "The elevation values to export.",
                        "default": null
                },
                "elev_units": {
                        "type": "string",
                        "description": "Specifies the measurement unit of the elevation values.INCH\u2014Elevations are in U.S. survey inches.FOOT\u2014Elevations are in U.S. survey feet.YARD\u2014Elevations are in U.S. survey yards.MILE_US\u2014Elevations are...",
                        "default": null
                },
                "output_type": {
                        "type": "string",
                        "description": "Specifies the primary output type of the output multidimensional raster.  The Additional output types parameter can be used to specify additional variables in the output multidimensional raster.For mo...",
                        "default": null
                },
                "quantile_probability_value": {
                        "type": "string",
                        "description": "If Output type is set to Quantile, use this parameter to enter the requested quantile. If Output type is set to Probability, use this parameter to enter the requested threshold value, and the probabil...",
                        "default": null
                },
                "additional_outputsoutput_type_quantile_probability_value": {
                        "type": "string",
                        "description": "Specifies the output type and quantile or probability value for each additional output type. If multiple output types are provided, the output raster will be a multivariate raster dataset with a diffe...",
                        "default": null
                },
                "build_transpose": {
                        "type": "string",
                        "description": "Specifies whether multidimensional transposes will be built on the output multidimensional raster.BUILD_TRANSPOSE\u2014Multidimensional transposes will be built on the output multidimensional raster.DO_NOT...",
                        "default": null
                }
        },
        "required": [
                "in_3d_geostat_layer",
                "out_multidimensional_raster"
        ]
},
    "empirical_bayesian_kriging_3d": {
        "name": "empirical_bayesian_kriging_3d",
        "description": "Interpolates 3D points using Empirical Bayesian Kriging methodology. All points must have x-, y-, and z-coordinates and a measured value to be interpolated. The output is a 3D geostatistical layer that calculates and renders itself as a 2D transect at a given elevation. The elevation of the layer can be changed using the range slider, and the layer will update to show the interpolated predictions for the new elevation. 3D interpolation has the following potential applications:\r\nOceanographers can create maps of dissolved oxygen and salinity at various depths in the ocean.Atmospheric scientists can create models for pollution and greenhouse gasses throughout the atmosphere.Geologists can predict subsurface geologic properties such as mineral concentrations and porosity. Learn more about Empirical Bayesian Kriging 3D",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point features containing the field that will be interpolated."
                },
                "elevation_field": {
                        "type": "string",
                        "description": "The field of the input features containing the elevation value of each input point.If the elevation values are stored as geometry attributes in Shape.Z, it is recommended that you use that field. If t..."
                },
                "value_field": {
                        "type": "string",
                        "description": "The field of the input features containing the measured values that will be interpolated."
                },
                "out_ga_layer": {
                        "type": "string",
                        "description": "The output geostatistical layer that will display the interpolation result."
                },
                "elevation_units": {
                        "type": "string",
                        "description": "The units of the elevation field.If Shape.Z is provided as the elevation field, the units will automatically match the z-units of the vertical coordinate system.INCH\u2014Elevations are in U.S. survey inch...",
                        "default": null
                },
                "measurement_error_field": {
                        "type": "string",
                        "description": "The field of the input features containing measurement error values for each point. The value should correspond to one standard deviation of the measured value of each point. Use this field if the mea...",
                        "default": null
                },
                "semivariogram_model_type": {
                        "type": "string",
                        "description": "The semivariogram model that will be used for the interpolation.\r\nPOWER\u2014The Power semivariogram model will be used.LINEAR\u2014The Linear semivariogram model will be used.THIN_PLATE_SPLINE\u2014The Thin Plate S...",
                        "default": null
                },
                "transformation_type": {
                        "type": "string",
                        "description": "The type of transformation that will be applied to the input features.NONE\u2014No transformation will be applied. This is the default.EMPIRICAL\u2014Multiplicative Skewing transformation with Empirical base fu...",
                        "default": null
                },
                "subset_size": {
                        "type": "string",
                        "description": "The size of the subset. The input data will automatically be divided into subsets before processing. This parameter controls the number of points that will be in each subset.",
                        "default": null
                },
                "overlap_factor": {
                        "type": "string",
                        "description": "A factor representing the degree of overlap between local models (also called subsets).Each input point can fall into several subsets, and the overlap factor specifies the average number of subsets in...",
                        "default": null
                },
                "number_simulations": {
                        "type": "string",
                        "description": "The number of simulated semivariograms that will be used for each local model.Using more simulations will make the model calculations more stable, but the model will take longer to calculate.",
                        "default": null
                },
                "trend_removal": {
                        "type": "string",
                        "description": "Specifies the order of trend removal in the vertical direction.For most 3D data, the values of the points change faster vertically than horizontally. Removing trend in the vertical direction will help...",
                        "default": null
                },
                "elev_inflation_factor": {
                        "type": "string",
                        "description": "A constant value that is multiplied by the Elevation field value prior to subsetting and model estimation. For most 3D data, the values of the points change faster vertically than horizontally, and th...",
                        "default": null
                },
                "search_neighborhood": {
                        "type": "string",
                        "description": "Specifies the number and orientation of the neighbors using the SearchNeighborhoodStandard3D class.\r\nStandard3D\r\n radius\u2014The length of the radius of the search neighborhood. nbrMax\u2014The maximum number ...",
                        "default": null
                },
                "output_elevation": {
                        "type": "string",
                        "description": "The default elevation of the out_ga_layer parameter value.\r\nThe geostatistical layer will draw as a horizontal surface at a given elevation, and this parameter specifies this elevation. After it's cre...",
                        "default": null
                },
                "output_type": {
                        "type": "string",
                        "description": "Surface type to store the interpolation results.For more information about output surface types, see What output surface types can the interpolation models generate.\r\nPREDICTION\u2014Prediction surfaces ar...",
                        "default": null
                },
                "quantile_value": {
                        "type": "string",
                        "description": "The quantile value for which the output layer will be generated.",
                        "default": null
                },
                "threshold_type": {
                        "type": "string",
                        "description": "Specifies whether to calculate the probability that a value exceeds or does not exceed the specified threshold.EXCEED\u2014The probability that the value exceeds the threshold will be calculated. This is t...",
                        "default": null
                },
                "probability_threshold": {
                        "type": "string",
                        "description": "The probability threshold value. If no value is provided, the median (50th quantile) of the input data will be used.",
                        "default": null
                }
        },
        "required": [
                "in_features",
                "elevation_field",
                "value_field",
                "out_ga_layer"
        ]
},
    "ga_layer_3d_to_netcdf": {
        "name": "ga_layer_3d_to_netcdf",
        "description": "Exports one or more 3D geostatistical layers created using the Empirical Bayesian Kriging 3D tool to netCDF format (*.nc file). The output file is displayed as a voxel layer in a local scene. Learn more about voxel layers",
        "parameters": {
                "in_3d_geostat_layers": {
                        "type": "string",
                        "description": "The 3D geostatistical layers that will be exported to an output netCDF file."
                },
                "out_netcdf_file": {
                        "type": "string",
                        "description": "The output netCDF file containing the exported values from the input geostatistical layers.  The results of each geostatistical layer are saved as different variables in the netCDF file."
                },
                "export_locations": {
                        "type": "string",
                        "description": "Specifies the locations to export from the in_3d_geostat_layers parameter value. If you choose the 3D_GRIDDED_POINTS option, you must provide values for the x_spacing, u_spacing, and elevation_spacing...",
                        "default": null
                },
                "x_spacing": {
                        "type": "string",
                        "description": "The spacing between each gridded point in the x-dimension.\r\nThe default value creates 40 points along the output x-extent.",
                        "default": null
                },
                "y_spacing": {
                        "type": "string",
                        "description": "The spacing between each gridded point in the y-dimension.\r\nThe default value creates 40 points along the output y-extent.",
                        "default": null
                },
                "elevation_spacing": {
                        "type": "string",
                        "description": "The spacing between each gridded point in the elevation (z) dimension.\r\nThe default value creates 40 points along the output z-extent.",
                        "default": null
                },
                "in_points_3d": {
                        "type": "string",
                        "description": "The 3D point features representing locations to export.\r\nThe point features must have their elevations stored in the Shape.Z geometry attribute.",
                        "default": null
                },
                "output_variableslayer_name_output_type_quantile_probability_value": {
                        "type": "string",
                        "description": "Specifies the output types for the Input 3D geostatistical layers values. You can specify one or more output types for each of the layers or you can apply an output type to all input geostatistical la...",
                        "default": null
                },
                "in_study_area": {
                        "type": "string",
                        "description": "The polygon features that represent the study area. Only points that are within the study area are saved in the output netCDF file.\r\nWhen visualized as a voxel layer, only voxels within the study area...",
                        "default": null
                },
                "min_elev_raster": {
                        "type": "string",
                        "description": "The  elevation raster that will be used to clip the bottom of the voxel layer. Only voxels above this elevation raster will be assigned predictions. For example, if you use a ground elevation raster, ...",
                        "default": null
                },
                "max_elev_raster": {
                        "type": "string",
                        "description": "The  elevation raster that will be used to clip the top of the voxel layer. Only voxels below this elevation raster will be assigned predictions. For example, if you use a ground elevation raster, the...",
                        "default": null
                }
        },
        "required": [
                "in_3d_geostat_layers",
                "out_netcdf_file"
        ]
},
    "ga_layer_to_contour": {
        "name": "ga_layer_to_contour",
        "description": "Creates a feature class of contours from a geostatistical layer. The output feature class can be either a line feature class of contour lines or a polygon feature class of filled contours.",
        "parameters": {
                "in_geostat_layer": {
                        "type": "string",
                        "description": "The geostatistical layer to be analyzed."
                },
                "contour_type": {
                        "type": "string",
                        "description": "Type of contour to represent the geostatistical layer.CONTOUR\u2014 The contour or isoline representation of the geostatistical layer. Displays the lines in either draft or presentation quality.FILLED_CONT..."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class will either be a polyline or a polygon, depending on the selected contour type."
                },
                "contour_quality": {
                        "type": "string",
                        "description": "Determines the smoothness of contour line representation.DRAFT\u2014 The default Draft quality presents a generalized version of isolines for faster display.PRESENTATION\u2014The Presentation option ensures mor...",
                        "default": null
                },
                "classification_type": {
                        "type": "string",
                        "description": "Specifies how the contour breaks will be calculated.GEOMETRIC_INTERVAL\u2014Contour breaks are calculated based on geometric intervals.EQUAL_INTERVAL\u2014Contour breaks are calculated based on equal intervals....",
                        "default": null
                },
                "classes_count": {
                        "type": "string",
                        "description": "Specify the number of classes in the output feature class.If contour_type is set to output filled contour polygons, the number of polygons created will equal the value specified in this parameter. If ...",
                        "default": null
                },
                "classes_breaks": {
                        "type": "string",
                        "description": "The list of break values if the classification_type is set to Manual. The values should be passed as a list, and the values can be in any order.For contour output, these are the values of the contour ...",
                        "default": null
                },
                "out_elevation": {
                        "type": "string",
                        "description": "For 3D interpolation models, you can export contours at any elevation. Use this parameter to specify the elevation that you want to export. If left empty, the elevation will be inherited from the inpu...",
                        "default": null
                }
        },
        "required": [
                "in_geostat_layer",
                "contour_type",
                "out_feature_class"
        ]
},
    "ga_layer_to_grid": {
        "name": "ga_layer_to_grid",
        "description": "Exports a Geostatistical layer to a raster. Learn more about the fundamentals of creating a raster from a geostatistical layer",
        "parameters": {
                "in_geostat_layer": {
                        "type": "string",
                        "description": "The geostatistical layer to be analyzed."
                },
                "out_surface_grid": {
                        "type": "string",
                        "description": "The raster to be created."
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size at which the output raster will be created.This value can be explicitly set in the Environments by the  Cell Size parameter.If not set, it is the shorter of the width or the height of th...",
                        "default": null
                },
                "points_per_block_horz": {
                        "type": "string",
                        "description": "The number of predictions for each cell in the horizontal direction for block interpolation. The default is 1.",
                        "default": null
                },
                "points_per_block_vert": {
                        "type": "string",
                        "description": "The number of predictions for each cell in the vertical direction for block interpolation. The default is 1.",
                        "default": null
                }
        },
        "required": [
                "in_geostat_layer",
                "out_surface_grid"
        ]
},
    "ga_layer_to_points": {
        "name": "ga_layer_to_points",
        "description": "Exports a geostatistical layer to points. The tool can also be used to predict values at unmeasured locations or to validate predictions made at measured locations.",
        "parameters": {
                "in_geostat_layer": {
                        "type": "string",
                        "description": "The geostatistical layer to be analyzed."
                },
                "in_locations": {
                        "type": "string",
                        "description": "Point locations where predictions or validations will be performed."
                },
                "z_field": {
                        "type": "string",
                        "description": "If this field is left blank, predictions are made at the location points. If a field is selected, predictions are made at the location points, compared to their Z_value_field values, and a validation ...",
                        "default": null
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing either the predictions or the predictions and the validation results.The fields in this feature class can include the following fields (where applicable):\r\n\r\n\r\nSour..."
                },
                "append_all_fields": {
                        "type": "string",
                        "description": "Determines whether all fields will be copied from the input features to the output feature class.ALL\u2014 All fields from the input features will be copied to the output feature class. This is the default...",
                        "default": null
                },
                "elevation_field": {
                        "type": "string",
                        "description": "The field containing the elevation of each input point. The parameter only applies to 3D geostatistical models. If the elevation values are stored as geometry attributes in Shape.Z, it is recommended ...",
                        "default": null
                },
                "elevation_units": {
                        "type": "string",
                        "description": "The units of the elevation field. This parameter only applies to 3D geostatistical models. If Shape.Z is provided as the elevation field, the units will automatically match the Z-units of the vertical...",
                        "default": null
                }
        },
        "required": [
                "in_geostat_layer",
                "in_locations",
                "out_feature_class"
        ]
},
    "ga_layer_to_rasters": {
        "name": "ga_layer_to_rasters",
        "description": "Exports a geostatistical layer to one or multiple rasters. Learn more about creating a raster from a geostatistical layer",
        "parameters": {
                "in_geostat_layer": {
                        "type": "string",
                        "description": "The geostatistical layer to be analyzed."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The primary output raster to be created. Additional rasters can be created with the Additional output rasters parameter."
                },
                "output_type": {
                        "type": "string",
                        "description": "The surface type of the output raster.For more information, see What output surface types can the interpolation models generate?PREDICTION\u2014A raster of predicted values.PREDICTION_STANDARD_ERROR\u2014A rast...",
                        "default": null
                },
                "quantile_probability_value": {
                        "type": "string",
                        "description": "If the Output surface type is set to Quantile, use this parameter to enter the requested quantile. If the Output surface type is set to Probability, use this parameter to enter the requested threshold...",
                        "default": null
                },
                "cell_size": {
                        "type": "string",
                        "description": "The cell size of the output rasters. This value will be shared by the Output raster and the Additional output rasters parameters.",
                        "default": null
                },
                "points_per_block_horz": {
                        "type": "string",
                        "description": "The number of predictions for each cell in the horizontal direction for block interpolation. The default is 1.",
                        "default": null
                },
                "points_per_block_vert": {
                        "type": "string",
                        "description": "The number of predictions for each cell in the vertical direction for block interpolation. The default is 1.",
                        "default": null
                },
                "additional_rastersout_raster_output_type_quantile_probability_value": {
                        "type": "string",
                        "description": "Provide the name, output type, and quantile or probability value for each additional output raster. See the descriptions of parameters above for more information. These additional rasters will be save...",
                        "default": null
                },
                "out_elevation": {
                        "type": "string",
                        "description": "For 3D interpolation models, you can export rasters at any elevation. Use this parameter to specify the elevation you want to export. If left empty, the elevation will be inherited from the input laye...",
                        "default": null
                }
        },
        "required": [
                "in_geostat_layer",
                "out_raster"
        ]
},
    "get_model_parameter": {
        "name": "get_model_parameter",
        "description": "Gets model parameter value from an existing geostatistical model source.",
        "parameters": {
                "in_ga_model_source": {
                        "type": "string",
                        "description": "The geostatistical model source to be analyzed."
                },
                "model_param_xpath": {
                        "type": "string",
                        "description": "XML path to the required model parameter."
                }
        },
        "required": [
                "in_ga_model_source",
                "model_param_xpath"
        ]
},
    "set_model_parameter": {
        "name": "set_model_parameter",
        "description": "Sets parameter values in an existing geostatistical model source.",
        "parameters": {
                "in_ga_model_source": {
                        "type": "string",
                        "description": "The geostatistical model source to be analyzed."
                },
                "model_param_xpath": {
                        "type": "string",
                        "description": "XML path to the required model parameter."
                },
                "in_param_value": {
                        "type": "string",
                        "description": "Value for the parameter defined by the XML path."
                },
                "out_ga_model": {
                        "type": "string",
                        "description": "Geostatistical model created with the parameter value defined in the XML path."
                }
        },
        "required": [
                "in_ga_model_source",
                "model_param_xpath",
                "in_param_value",
                "out_ga_model"
        ]
}
}
