# Generated ArcGIS Pro image-analyst AI Function Declarations
# Generated on 2025-10-01T15:16:34.153773
# Total tools: 96

functions_declarations = {
    "analyze_changes_using_ccdc": {
        "name": "analyze_changes_using_ccdc",
        "description": "Evaluates changes in pixel values over time using the Continuous Change Detection and Classification (CCDC) method and generates a change analysis raster containing the model results. Learn more about how Analyze Changes Using CCDC works",
        "parameters": {
                "in_multidimensional_raster": {
                        "type": "string",
                        "description": "The input multidimensional raster dataset."
                },
                "bands": {
                        "type": "string",
                        "description": "The band IDs to use for change detection. If no band IDs are provided, all the bands from the input raster dataset will be used.",
                        "default": None
                },
                "tmask_bands": {
                        "type": "string",
                        "description": "The band IDs to be used in the temporal mask (Tmask). It is recommended that you use the green band and the SWIR band. If no band IDs are provided, no masking will occur.",
                        "default": None
                },
                "chi_squared_threshold": {
                        "type": "string",
                        "description": "The chi-square statistic change probability threshold. If an observation has a calculated change probability that is above this threshold, \r\nit is flagged as an anomaly, which is a potential change ev...",
                        "default": None
                },
                "min_anomaly_observations": {
                        "type": "string",
                        "description": "The minimum number of consecutive anomaly observations that must occur before an event is considered a change. A pixel must be flagged as an anomaly for the specified number of consecutive time slices...",
                        "default": None
                },
                "update_frequency": {
                        "type": "string",
                        "description": "The frequency, in years, at which to update the time series model with new observations. \r\nThe default value is 1.",
                        "default": None
                }
        },
        "required": [
                "in_multidimensional_raster"
        ]
},
    "analyze_changes_using_landtrendr": {
        "name": "analyze_changes_using_landtrendr",
        "description": "Evaluates changes in pixel values over time using the Landsat-based detection of trends in disturbance and recovery (LandTrendr) method and generates a change analysis raster containing the model results. Learn more about how LandTrendr works",
        "parameters": {
                "in_multidimensional_raster": {
                        "type": "string",
                        "description": "The input multidimensional raster dataset."
                },
                "processing_band": {
                        "type": "string",
                        "description": "The image band name to use for segmenting the pixel value trajectories over time. Choose the band name that will best capture the changes in the feature you want to observe.If no band value is specifi...",
                        "default": None
                },
                "snapping_date": {
                        "type": "string",
                        "description": "The date used to identify a slice for each year in the input multidimensional dataset. The slice with the date closest to the snapping date will be used. This parameter is required if the input datase...",
                        "default": None
                },
                "max_num_segments": {
                        "type": "string",
                        "description": "The maximum number of segments to be fitted to the time series for each pixel. The default is 5.",
                        "default": None
                },
                "vertex_count_overshoot": {
                        "type": "string",
                        "description": "The number of additional vertices beyond  max_num_segments + 1 that can be used to fit the model during the initial stage of identifying vertices. Later in the modeling process, the number of addition...",
                        "default": None
                },
                "spike_threshold": {
                        "type": "string",
                        "description": "The threshold to use for dampening spikes or anomalies in the pixel value trajectory. The value must  range between 0 and 1 in which 1 means no dampening. The default is 0.9.",
                        "default": None
                },
                "recovery_threshold": {
                        "type": "string",
                        "description": "The recovery threshold value in years. If a segment has a recovery rate that is faster than 1/recovery threshold, the segment is discarded and not included in the time series model. The value must ran...",
                        "default": None
                },
                "prevent_one_year_recovery": {
                        "type": "string",
                        "description": "Specifies whether segments that exhibit a one year recovery will be excluded.ALLOW_ONE_YEAR_RECOVERY\u2014Segments that exhibit a one year recovery will not be excluded.PREVENT_ONE_YEAR_RECOVERY\u2014Segments t...",
                        "default": None
                },
                "recovery_trend": {
                        "type": "string",
                        "description": "Specifies whether the recovery has an increasing (positive) trend.INCREASING_TREND\u2014The recovery has an increasing trend. This is the default.DECREASING_TREND\u2014The recovery has a decreasing trend.",
                        "default": None
                },
                "min_num_observations": {
                        "type": "string",
                        "description": "The   minimum number of valid observations required to perform fitting. The number of years in the input multidimensional dataset must be equal to or greater than this value. The default is 6.",
                        "default": None
                },
                "best_model_proportion": {
                        "type": "string",
                        "description": "The best model proportion value. During the model selection process, the tool will calculate the p-value for each model and identify a model that has the most vertices while maintaining the smallest (...",
                        "default": None
                },
                "pvalue_threshold": {
                        "type": "string",
                        "description": "The p-value threshold\r\nfor a model to be selected. After the vertices are detected in the initial stage of the model fitting, the tool will fit each segment and calculate the p-value to determine the ..."
                },
                "output_other_bands": {
                        "type": "string",
                        "description": "Specifies whether other bands will be included in the segmentation process.INCLUDE_OTHER_BANDS\u2014Other bands will be included. The segmentation and vertices information from the initial segmentation ban...",
                        "default": None
                }
        },
        "required": [
                "in_multidimensional_raster",
                "pvalue_threshold"
        ]
},
    "compute_change_raster": {
        "name": "compute_change_raster",
        "description": "Calculates the absolute, relative, categorical, or spectral difference between two raster datasets.",
        "parameters": {
                "from_raster": {
                        "type": "string",
                        "description": "The \r\ninitial or earlier raster to be analyzed."
                },
                "to_raster": {
                        "type": "string",
                        "description": "The \r\nfinal or later raster to be analyzed. This is the raster that will be compared to the initial raster."
                },
                "compute_change_method": {
                        "type": "string",
                        "description": "Specifies the type of calculation that will be performed between the two rasters. DIFFERENCE\u2014The mathematical difference, or subtraction, between the pixel values in the rasters will be calculated. Th...",
                        "default": None
                },
                "from_classes": {
                        "type": "string",
                        "description": "The list of class names from the from_raster parameter that will be included in the computation. If no classes are provided, all classes will be included. This parameter is enabled when the compute_ch...",
                        "default": None
                },
                "to_classes": {
                        "type": "string",
                        "description": "The list of class names from the to_raster parameter that will be included in the computation. If no classes are provided, all classes will be included. This parameter is enabled when the compute_chan...",
                        "default": None
                },
                "filter_method": {
                        "type": "string",
                        "description": "Specifies the pixels that will be categorized in the output raster. This parameter is enabled when the compute_change_method parameter is set to CATEGORICAL_DIFFERENCE.CHANGED_PIXELS_ONLY\u2014Only the pix...",
                        "default": None
                },
                "define_transition_colors": {
                        "type": "string",
                        "description": "Specifies the color that will be used to symbolize the output classes.  When a pixel changes from one class type to another, the output pixel color represents the initial class type, the final class t...",
                        "default": None
                }
        },
        "required": [
                "from_raster",
                "to_raster"
        ]
},
    "detect_change_using_change_analysis_raster": {
        "name": "detect_change_using_change_analysis_raster",
        "description": "Generates a raster containing pixel change information using the output change analysis raster from the Analyze Changes Using CCDC tool or the Analyze Changes Using LandTrendr tool.",
        "parameters": {
                "in_change_analysis_raster": {
                        "type": "string",
                        "description": "The change analysis raster generated from the Analyze Changes Using CCDCtool or the Analyze Changes Using LandTrendr tool."
                },
                "change_type": {
                        "type": "string",
                        "description": "Specifies the change information that will be calculated for each pixel.TIME_OF_LATEST_CHANGE\u2014Each pixel will contain the date of its most recent change in the time series. This is the default.TIME_OF...",
                        "default": None
                },
                "max_number_changes": {
                        "type": "string",
                        "description": "The maximum number of changes per pixel that will be calculated. This number corresponds to the number of bands in the output raster. The default is 1, meaning only one change date will be calculated,...",
                        "default": None
                },
                "segment_date": {
                        "type": "string",
                        "description": "Specifies whether the date at the beginning of a change segment will be extracted or at the end.This parameter is available only when the input change analysis raster is the output from the Analyze Ch...",
                        "default": None
                },
                "change_direction": {
                        "type": "string",
                        "description": "Specifies the direction of change that will be included in the analysis.This parameter is available only when the input change analysis raster is the output from the Analyze Changes Using LandTrendr t...",
                        "default": None
                },
                "filter_by_year": {
                        "type": "string",
                        "description": "Specifies whether the output will be filtered by a range of years. FILTER_BY_YEAR\u2014Results will be filtered so that only changes that occurred within a specific range of years will be included in the o...",
                        "default": None
                },
                "min_year": {
                        "type": "string",
                        "description": "The earliest year that will be used to filter results. This parameter is required if the filter_by_year parameter is set to FILTER_BY_YEAR.",
                        "default": None
                },
                "max_year": {
                        "type": "string",
                        "description": "The latest year that will be used to filter results. This parameter is required if the filter_by_year parameter is set to FILTER_BY_YEAR.",
                        "default": None
                },
                "filter_by_duration": {
                        "type": "string",
                        "description": "Specifies whether results will be filtered by the change duration. This parameter is enabled only when the input change analysis raster is the output from the Analyze Changes Using LandTrendr tool.FIL...",
                        "default": None
                },
                "min_duration": {
                        "type": "string",
                        "description": "The minimum number of consecutive years that will be included in the results. This parameter is required if the filter_by_duration parameter is set to FILTER_BY_DURATION.",
                        "default": None
                },
                "max_duration": {
                        "type": "string",
                        "description": "The maximum number of consecutive years that will be included in the results. This parameter is required if the filter_by_duration parameter is set to FILTER_BY_DURATION.",
                        "default": None
                },
                "filter_by_magnitude": {
                        "type": "string",
                        "description": "Specifies whether results will be filtered by change magnitude.Checked\u2014Results will be filtered by magnitude so that only the changes of a given magnitude will be included in the output.Unchecked\u2014Resu...",
                        "default": None
                },
                "min_magnitude": {
                        "type": "string",
                        "description": "The minimum magnitude that will be included in the results. This parameter is required if the filter_by_magnitude parameter is set to FILTER_BY_MAGNITUDE.",
                        "default": None
                },
                "max_magnitude": {
                        "type": "string",
                        "description": "The maximum magnitude that will be included in the results. This parameter is required if the filter_by_magnitude parameter is set to FILTER_BY_MAGNITUDE.",
                        "default": None
                },
                "filter_by_start_value": {
                        "type": "string",
                        "description": "Specifies whether results will be filtered by start value.This parameter is enabled only when the input change analysis raster is the output from the Analyze Changes Using LandTrendr tool.FILTER_BY_ST...",
                        "default": None
                },
                "min_start_value": {
                        "type": "string",
                        "description": "The minimum start value that will be included in the results.This parameter is required if the filter_by_start_value parameter is set to FILTER_BY_START_VALUE.",
                        "default": None
                },
                "max_start_value": {
                        "type": "string",
                        "description": "The maximum start value that will be included in the results.This parameter is required if the filter_by_start_value parameter is set to FILTER_BY_START_VALUE.",
                        "default": None
                },
                "filter_by_end_value": {
                        "type": "string",
                        "description": "Specifies whether results will be filtered by end value.This parameter is enabled only when the input change analysis raster is the output from the Analyze Changes Using LandTrendr tool.FILTER_BY_END_...",
                        "default": None
                },
                "min_end_value": {
                        "type": "string",
                        "description": "The minimum end value that will be included in the results.This parameter is required if the filter_by_end_value parameter is set to FILTER_BY_END_VALUE.",
                        "default": None
                },
                "max_end_value": {
                        "type": "string",
                        "description": "The maximum end value that will be included in the results.This parameter is required if the filter_by_end_value parameter is set to FILTER_BY_END_VALUE.",
                        "default": None
                }
        },
        "required": [
                "in_change_analysis_raster"
        ]
},
    "classify_raster": {
        "name": "classify_raster",
        "description": "Classifies a raster dataset based on an Esri classifier definition file (.ecd) and raster dataset inputs. The .ecd file contains all the information needed to perform a specific type of Esri-supported classification. The inputs to this tool must match the inputs used to generate the required .ecd file. The .ecd file can be generated from any of the classifier training tools, such as Train Random Trees Classifier or Train Support Vector Machine Classifier.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset to classify."
                },
                "in_classifier_definition": {
                        "type": "string",
                        "description": "The input Esri classifier definition file (.ecd) containing the statistics for the chosen attributes for the classifier."
                },
                "in_additional_raster": {
                        "type": "string",
                        "description": "Ancillary raster datasets, such as a multispectral image or a DEM, will be incorporated to generate attributes and other required information for the classifier. This raster is necessary when calculat...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_classifier_definition"
        ]
},
    "classify_raster_using_spectra": {
        "name": "classify_raster_using_spectra",
        "description": "Classifies a multiband raster dataset using spectral matching techniques. The input spectral data can be provided as a point feature class or a .json file.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input multiband raster."
                },
                "in_spectra_file": {
                        "type": "string",
                        "description": "The  spectral information for different pixel classes.\r\nThe spectral information can be provided as point features, a training sample point feature class generated from the Training Samples Manager pa..."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the spectral matching method that will be used.SAM\u2014The  vector angle between the input multiband raster and the reference spectra will be calculated in which the spectra of each pixel is tre..."
                },
                "thresholds": {
                        "type": "string",
                        "description": "The threshold for spectral matching. Pixel values that exceed this value will be classified as undefined. This can be a single value applied to all spectral classes or a space-delimited list of values...",
                        "default": None
                },
                "out_score_raster": {
                        "type": "string",
                        "description": "A multiband raster that stores the matching results for each end member. The band order follows the order of the classes in the in_spectra_file parameter value. If the input is a multidimensional rast...",
                        "default": None
                },
                "out_classifier_definition": {
                        "type": "string",
                        "description": "The output .ecd file.",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_spectra_file",
                "method"
        ]
},
    "compute_confusion_matrix": {
        "name": "compute_confusion_matrix",
        "description": "Computes a confusion matrix with errors of omission and commission and derives a kappa index of agreement, Intersection over Union (IoU), and overall accuracy between the classified map and the reference data. This tool uses the outputs from the Create Accuracy Assessment Points tool or the Update Accuracy Assessment Points tool.",
        "parameters": {
                "in_accuracy_assessment_points": {
                        "type": "string",
                        "description": "The accuracy assessment point feature class created from the Create Accuracy Assessment Points tool, containing the Classified and GrndTruth fields. These fields are both long integer field types."
                },
                "out_confusion_matrix": {
                        "type": "string",
                        "description": "The output file name of the confusion matrix in table format.The format of the table is determined by the output location and path. By default, the output will be a geodatabase table. If the path is n..."
                }
        },
        "required": [
                "in_accuracy_assessment_points",
                "out_confusion_matrix"
        ]
},
    "compute_segment_attributes": {
        "name": "compute_segment_attributes",
        "description": "Computes a set of attributes associated with the segmented image. The input raster can be a single-band or 3-band, 8-bit segmented image.",
        "parameters": {
                "in_segmented_raster": {
                        "type": "string",
                        "description": "The input segmented raster dataset, where all the pixels belonging to a segment have the same converged RGB color. Usually, it is an 8-bit, 3-band RGB raster, but it can also be a 1-band grayscale ras..."
                },
                "in_additional_raster": {
                        "type": "string",
                        "description": "Ancillary raster datasets, such as a multispectral image or a DEM, will be incorporated to generate attributes and other required information for the classifier. This raster is necessary when calculat...",
                        "default": None
                },
                "used_attributes": {
                        "type": "string",
                        "description": "Specifies the attributes that will be included in the attribute table associated with the output raster.COLOR\u2014The RGB color values will be derived from the input raster on a per-segment basis. This is...",
                        "default": None
                }
        },
        "required": [
                "in_segmented_raster"
        ]
},
    "create_accuracy_assessment_points": {
        "name": "create_accuracy_assessment_points",
        "description": "Creates randomly sampled points for postclassification accuracy assessment. A common practice is to randomly select hundreds of points and label their classification types by referencing reliable sources, such as field work or human interpretation of high-resolution imagery. The reference points are then compared with the classification results at the same locations.",
        "parameters": {
                "in_class_data": {
                        "type": "string",
                        "description": "The input classification image or other thematic GIS reference data. The input can be a raster or feature class.Typical data is a classification image of a single band of integer data type.If using po..."
                },
                "out_points": {
                        "type": "string",
                        "description": "The output point shapefile or feature class that contains the random points to be used for accuracy assessment."
                },
                "target_field": {
                        "type": "string",
                        "description": "Specifies whether the input data is a classified image or ground truth data.A classified image is the image that was just classified. Ground truth data, or reference data, consists of identified featu...",
                        "default": None
                },
                "num_random_points": {
                        "type": "string",
                        "description": "The total number of random points that will be generated.The actual number may exceed but never fall below this number, depending on sampling strategy and number of classes. The default number of rand...",
                        "default": None
                },
                "sampling": {
                        "type": "string",
                        "description": "Specifies the sampling scheme that will be used.STRATIFIED_RANDOM\u2014Randomly distributed points will be created in each class in which each class has a number of points proportional to its relative area...",
                        "default": None
                },
                "polygon_dimension_field": {
                        "type": "string",
                        "description": "A field that defines the dimension (time) of the features. This parameter is used only if the classification result is a multidimensional raster and you want to generate assessment points from a featu...",
                        "default": None
                },
                "min_point_distance": {
                        "type": "string",
                        "description": "The minimum distance between the reference points. The default is 0.",
                        "default": None
                }
        },
        "required": [
                "in_class_data",
                "out_points"
        ]
},
    "generate_training_samples_from_seed_points": {
        "name": "generate_training_samples_from_seed_points",
        "description": "Generates training samples from seed points, such as accuracy assessment points or training sample points. A typical use case is generating training samples from an existing source, such as a thematic raster or a feature class.",
        "parameters": {
                "in_class_data": {
                        "type": "string",
                        "description": "The data source that labels the training samples."
                },
                "in_seed_points": {
                        "type": "string",
                        "description": "A point shapefile or feature class to provide the centers of training sample polygons."
                },
                "out_training_feature_class": {
                        "type": "string",
                        "description": "The output training sample feature class in the format that can be used in training tools, including shapefiles. The output feature class can be either a polygon feature class or a point feature class..."
                },
                "min_sample_area": {
                        "type": "string",
                        "description": "The minimum area needed for each training sample, in square meters. The minimum value must be greater than or equal to 0.",
                        "default": None
                },
                "max_sample_radius": {
                        "type": "string",
                        "description": "The longest distance (in meters) from any point within the training sample to its center seed point. If set to 0, the output training sample will be points instead of polygons. The minimum value must ...",
                        "default": None
                }
        },
        "required": [
                "in_class_data",
                "in_seed_points",
                "out_training_feature_class"
        ]
},
    "inspect_training_samples": {
        "name": "inspect_training_samples",
        "description": "Estimates the accuracy of individual training samples. The cross validation accuracy is computed using the previously generated classification training result in an .ecd file and the training samples. Outputs include a raster dataset containing the misclassified class values and a training sample dataset with the accuracy score for each training sample.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster to be classified."
                },
                "in_training_features": {
                        "type": "string",
                        "description": "A training sample feature class created in the Training Samples Manager pane."
                },
                "in_classifier_definition": {
                        "type": "string",
                        "description": "The .ecd output classifier file from any of the train classifier tools. The .ecd file is a JSON file that contains attribute information, statistics, or other information needed for the classifier."
                },
                "out_training_feature_class": {
                        "type": "string",
                        "description": "The output individual training samples saved as a feature class. The associated attribute table contains an addition field listing the accuracy score."
                },
                "out_misclassified_raster": {
                        "type": "string",
                        "description": "The output misclassified raster having NoData outside training samples. In training samples, correctly classified pixels are represented as NoData, and misclassified pixels are represented by their cl..."
                },
                "in_additional_raster": {
                        "type": "string",
                        "description": "Ancillary raster datasets, such as a multispectral image or a DEM, will be incorporated to generate attributes and other required information for the classifier. This raster is necessary when calculat...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_training_features",
                "in_classifier_definition",
                "out_training_feature_class",
                "out_misclassified_raster"
        ]
},
    "linear_spectral_unmixing": {
        "name": "linear_spectral_unmixing",
        "description": "Performs subpixel classification and calculates the fractional abundance of different land-cover types for individual pixels.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The \r\ninput raster dataset."
                },
                "in_spectral_profile_file": {
                        "type": "string",
                        "description": "The  spectral information for the different land-cover classes.This can be provided as polygon features, a classifier definition file (.ecd) generated from the Train Maximum Likelihood Classifier tool..."
                },
                "value_option": {
                        "type": "string",
                        "description": "Specifies how the output pixel values will be defined.SUM_TO_ONE\u2014Class values for each pixel will be provided in decimal format with the sum of all classes equal to 1. For example, Class1 = 0.16; Clas...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_spectral_profile_file"
        ]
},
    "predict_using_regression_model": {
        "name": "predict_using_regression_model",
        "description": "Predicts data values using the output from the Train Random Trees Regression Model tool.",
        "parameters": {
                "in_rasters": {
                        "type": "string",
                        "description": "The single-band, multidimensional, or multiband raster datasets, or mosaic datasets containing \r\nexplanatory variables."
                },
                "in_regression_definition": {
                        "type": "string",
                        "description": "A JSON format file that contains attribute information, statistics, or other information from the regression model. The file has an .ecd extension. The file is the output of the Train Random Trees Reg..."
                },
                "out_raster_dataset": {
                        "type": "string",
                        "description": "A raster of the predicted values."
                }
        },
        "required": [
                "in_rasters",
                "in_regression_definition",
                "out_raster_dataset"
        ]
},
    "train_random_trees_regression_model": {
        "name": "train_random_trees_regression_model",
        "description": "Models the relationship between explanatory variables (independent variables) and a target dataset (dependent variable).",
        "parameters": {
                "in_rasters": {
                        "type": "string",
                        "description": "The single-band, multidimensional, or multiband raster datasets, or mosaic datasets containing \r\nexplanatory variables."
                },
                "in_target_data": {
                        "type": "string",
                        "description": "The raster or point feature class containing the target variable (dependant variable)  data."
                },
                "out_regression_definition": {
                        "type": "string",
                        "description": "A JSON format file with an .ecd extension that contains attribute information, statistics, or other information for the classifier."
                },
                "target_value_field": {
                        "type": "string",
                        "description": "The field name of the information to model in the target point feature class or raster dataset.",
                        "default": None
                },
                "target_dimension_field": {
                        "type": "string",
                        "description": "A date field or numeric field in the input point feature class that defines the dimension values.",
                        "default": None
                },
                "raster_dimension": {
                        "type": "string",
                        "description": "The dimension name of the input multidimensional raster (explanatory variables) that  links to the dimension in the target data.",
                        "default": None
                },
                "out_importance_table": {
                        "type": "string",
                        "description": "A table containing information describing the importance of each explanatory variable used in the model. A larger number indicates the corresponding variable is more correlated to the predicted variab...",
                        "default": None
                },
                "max_num_trees": {
                        "type": "string",
                        "description": "The maximum number of trees in the forest. Increasing the number of trees will lead to higher accuracy rates, although this improvement will level off. The number of trees increases the processing tim...",
                        "default": None
                },
                "max_tree_depth": {
                        "type": "string",
                        "description": "The maximum depth of each tree in the forest. Depth determines the number of rules each tree can create, resulting in a decision. Trees will not grow any deeper than this setting. The default is 30.",
                        "default": None
                },
                "max_samples": {
                        "type": "string",
                        "description": "The maximum number of samples that will be used for the regression analysis. A value that is less than or equal to 0 means that the system will use all the samples from the input target raster or poin...",
                        "default": None
                },
                "average_points_per_cell": {
                        "type": "string",
                        "description": "Specifies whether the average will be calculated when multiple training points fall into one cell. This parameter is applicable only when the input target is a point feature class.Unchecked\u2014All points...",
                        "default": None
                },
                "percent_testing": {
                        "type": "string",
                        "description": "The percentage of test points that will be used for error checking. The tool checks for three types of errors: errors on training points, errors on test points, and errors on test location points. The...",
                        "default": None
                },
                "out_scatterplots": {
                        "type": "string",
                        "description": "The output scatter plots in PDF or HTML format. The output will include scatter plots of training data, test data, and location test data.",
                        "default": None
                },
                "out_sample_features": {
                        "type": "string",
                        "description": "The output feature class that will contain target values and predicted values for training points, test points, and location test points.",
                        "default": None
                }
        },
        "required": [
                "in_rasters",
                "in_target_data",
                "out_regression_definition"
        ]
},
    "remove_raster_segment_tiling_artifacts": {
        "name": "remove_raster_segment_tiling_artifacts",
        "description": "Corrects segments or objects cut by tile boundaries during the segmentation process performed as a raster function. This tool is helpful for some regional processes, such as image segmentation, that have inconsistencies near image tile boundaries. This processing step is included in the Segment Mean Shift tool. It should only be used on a segmented image that was not created from that tool.",
        "parameters": {
                "in_segmented_raster": {
                        "type": "string",
                        "description": "Select the segmented raster with the tiling artifacts that you want to remove."
                },
                "tilesizex": {
                        "type": "string",
                        "description": "Specify the tile width from Segment Mean Shift. If left blank, the default is 512 pixels.",
                        "default": None
                },
                "tilesizey": {
                        "type": "string",
                        "description": "Specify the tile height from Segment Mean Shift. If left blank, the default is 512 pixels.",
                        "default": None
                }
        },
        "required": [
                "in_segmented_raster"
        ]
},
    "segment_mean_shift": {
        "name": "segment_mean_shift",
        "description": "Groups adjacent pixels that have similar spectral characteristics into segments.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset to segment. This can be a multispectral or grayscale image."
                },
                "spectral_detail": {
                        "type": "string",
                        "description": "The level of importance given to the spectral differences of features in the imagery.Valid values range from 1.0 to 20.0. A higher value is appropriate when there are features to classify separately t...",
                        "default": None
                },
                "spatial_detail": {
                        "type": "string",
                        "description": "The level of importance given to the proximity between features in the imagery.Valid values range from 1.0 to 20. A higher value is appropriate for a scene in which the features of interest are small ...",
                        "default": None
                },
                "min_segment_size": {
                        "type": "string",
                        "description": "The minimum size of a segment. Merge segments smaller than this size with their best fitting neighbor segment. This is related to the minimum mapping unit for your project.Units are in pixels.",
                        "default": None
                },
                "band_indexes": {
                        "type": "string",
                        "description": "The bands that will be used to segment the imagery, separated by a space. If no band indexes are specified, they are determined by the following criteria:\r\n If the raster has only 3 bands, those 3 ban...",
                        "default": None
                },
                "max_segment_size": {
                        "type": "string",
                        "description": "The maximum size of a segment. Segments that are larger than the specified size will be divided. Use this parameter to prevent artifacts in the output raster resulting from large segments.Units are in...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "train_iso_cluster_classifier": {
        "name": "train_iso_cluster_classifier",
        "description": "Generates an Esri classifier definition file (.ecd) using the Iso Cluster classification definition. This tool performs an unsupervised classification.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset to classify."
                },
                "max_classes": {
                        "type": "string",
                        "description": "Maximum number of desired classes to group pixels or segments. This should be set to be greater than the number of classes in your legend.It is possible that you will get fewer classes than what you s..."
                },
                "out_classifier_definition": {
                        "type": "string",
                        "description": "The output JSON format file that will contain attribute information, statistics, hyperplane vectors, and other information for the classifier. An .ecd file will be created."
                },
                "in_additional_raster": {
                        "type": "string",
                        "description": "Ancillary raster datasets, such as a multispectral image or a DEM, will be incorporated to generate attributes and other required information for classification. This parameter is optional.",
                        "default": None
                },
                "max_iterations": {
                        "type": "string",
                        "description": "The maximum number of iterations the clustering process will run.The recommended range is between 10 and 20 iterations. Increasing this value will linearly increase the processing time.",
                        "default": None
                },
                "min_samples_per_cluster": {
                        "type": "string",
                        "description": "The minimum number of pixels or segments in a valid cluster or class.The default value of 20 is effective in creating statistically significant classes. You can increase this number for more larger cl...",
                        "default": None
                },
                "skip_factor": {
                        "type": "string",
                        "description": "Number of pixels to skip for a pixel image input. If a segmented image is an input, specify the number of segments to skip.",
                        "default": None
                },
                "used_attributes_used_attributes": {
                        "type": "string",
                        "description": "Specifies the attributes that will be included in the attribute table associated with the output raster.COLOR\u2014The RGB color values will be derived from the input raster on a per-segment basis. This is...",
                        "default": None
                },
                "max_merge_per_iter": {
                        "type": "string",
                        "description": "The maximum number of cluster merges per iteration. Increasing the number of merges will reduce the number of classes that are created. A lower value will result in more classes.",
                        "default": None
                },
                "max_merge_distance": {
                        "type": "string",
                        "description": "The maximum distance between cluster centers in feature space. Increasing the distance will allow more clusters to merge, resulting in fewer classes. A lower value will result in more classes. Values ...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "max_classes",
                "out_classifier_definition"
        ]
},
    "train_maximum_likelihood_classifier": {
        "name": "train_maximum_likelihood_classifier",
        "description": "Generates an Esri classifier definition file (.ecd) using the Maximum Likelihood Classifier (MLC) classification definition.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset to classify."
                },
                "in_training_features": {
                        "type": "string",
                        "description": "The training sample file or layer that delineates the training sites.These can be either shapefiles or feature classes that contain the training samples. The following field names are required in the ..."
                },
                "out_classifier_definition": {
                        "type": "string",
                        "description": "The output JSON format file that will contain attribute information, statistics, hyperplane vectors, and other information for the classifier. An .ecd file will be created."
                },
                "in_additional_raster": {
                        "type": "string",
                        "description": "Incorporates ancillary raster datasets, such as a segmented image or DEM. This parameter is optional.",
                        "default": None
                },
                "used_attributes": {
                        "type": "string",
                        "description": "Specifies the attributes that will be included in the attribute table associated with the output raster.COLOR\u2014The RGB color values will be derived from the input raster on a per-segment basis. This is...",
                        "default": None
                },
                "dimension_value_field": {
                        "type": "string",
                        "description": "Contains dimension values in the input training sample feature class.\r\nThis parameter is required to classify a time series of raster data using the change analysis raster output from the Analyze Chan...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_training_features",
                "out_classifier_definition"
        ]
},
    "train_random_trees_classifier": {
        "name": "train_random_trees_classifier",
        "description": "Generates an Esri classifier definition file (.ecd) using the Random Trees classification method. The random trees classifier is an image classification technique that is resistant to overfitting and can work with segmented images and other ancillary raster datasets. For standard image inputs, the tool accepts multiband imagery with any bit depth, and it will perform the Random Trees classification on a pixel basis or segment, based on the input training feature file.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset to classify.You can use any Esri-supported raster dataset. One option is a 3-band, 8-bit segmented raster dataset in which all the pixels in the same segment have the same color. Th..."
                },
                "in_training_features": {
                        "type": "string",
                        "description": "The training sample file or layer that delineates the training sites.These can be either shapefiles or feature classes that contain the training samples. The following field names are required in the ..."
                },
                "out_classifier_definition": {
                        "type": "string",
                        "description": "A JSON file that contains attribute information, statistics, or other information for the classifier. An .ecd file is created."
                },
                "in_additional_raster": {
                        "type": "string",
                        "description": "Ancillary raster datasets, such as a multispectral image or a DEM, will be incorporated to generate attributes and other required information for classification. This parameter is optional.",
                        "default": None
                },
                "max_num_trees": {
                        "type": "string",
                        "description": "The maximum number of trees in the forest. Increasing the number of trees will lead to higher accuracy rates, although this improvement will level off eventually. The number of trees increases the pro...",
                        "default": None
                },
                "max_tree_depth": {
                        "type": "string",
                        "description": "The maximum depth of each tree in the forest. Depth is another way of saying the number of rules each tree is allowed to create to come to a decision. Trees will not grow any deeper than this setting.",
                        "default": None
                },
                "max_samples_per_class": {
                        "type": "string",
                        "description": "The maximum number of samples that will be used to define each class.The default value of 1000 is recommended when the inputs are nonsegmented rasters. A value that is less than or equal to 0 means th...",
                        "default": None
                },
                "used_attributes_used_attributes": {
                        "type": "string",
                        "description": "Specifies the attributes that will be included in the attribute table associated with the output raster.\r\nCOLOR\u2014The RGB color values will be derived from the input raster on a per-segment basis. This ...",
                        "default": None
                },
                "dimension_value_field": {
                        "type": "string",
                        "description": "Contains dimension values in the input training sample feature class.\r\nThis parameter is required to classify a time series of raster data using the change analysis raster output from the Analyze Chan...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_training_features",
                "out_classifier_definition"
        ]
},
    "train_support_vector_machine_classifier": {
        "name": "train_support_vector_machine_classifier",
        "description": "Generates an Esri classifier definition file (.ecd) using the Support Vector Machine (SVM) classification definition.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster dataset to classify.The preferred input is a 3-band, 8-bit segmented raster dataset in which all the pixels in the same segment have the same color. The input can also be a 1-band, 8-bit gr..."
                },
                "in_training_features": {
                        "type": "string",
                        "description": "The training sample file or layer that delineates the training sites.These can be either shapefiles or feature classes that contain the training samples. The following field names are required in the ..."
                },
                "out_classifier_definition": {
                        "type": "string",
                        "description": "The output JSON format file that will contain attribute information, statistics, hyperplane vectors, and other information for the classifier. An .ecd file will be created."
                },
                "in_additional_raster": {
                        "type": "string",
                        "description": "Ancillary raster datasets, such as a multispectral image or a DEM, will be incorporated to generate attributes and other required information for classification. This parameter is optional.",
                        "default": None
                },
                "max_samples_per_class": {
                        "type": "string",
                        "description": "The maximum number of samples that will be used to define each class.The default value of 500 is recommended when the inputs are nonsegmented rasters. A value that is less than or equal to 0 means tha...",
                        "default": None
                },
                "used_attributes_used_attributes": {
                        "type": "string",
                        "description": "Specifies the attributes that will be included in the attribute table associated with the output raster.\r\nCOLOR\u2014The RGB color values will be derived from the input raster on a per-segment basis. This ...",
                        "default": None
                },
                "dimension_value_field": {
                        "type": "string",
                        "description": "Contains dimension values in the input training sample feature class.\r\nThis parameter is required to classify a time series of raster data using the change analysis raster output from the Analyze Chan...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_training_features",
                "out_classifier_definition"
        ]
},
    "update_accuracy_assessment_points": {
        "name": "update_accuracy_assessment_points",
        "description": "Updates the Target field in the attribute table to compare reference points to the classified image. Accuracy assessment uses known points to assess the validity of the classification model.",
        "parameters": {
                "in_class_data": {
                        "type": "string",
                        "description": "The input classification image or other thematic GIS reference data. The input can be a raster or feature class.Typical data is a classification image of a single band of integer data type.If using po..."
                },
                "in_points": {
                        "type": "string",
                        "description": "The point feature class with the accuracy assessment points that will be updated.\r\nAll points from this input will be copied to the updated output feature class, and the target_field parameter value w..."
                },
                "out_points": {
                        "type": "string",
                        "description": "The output point shapefile or feature class that contains the random points to be used for accuracy assessment."
                },
                "target_field": {
                        "type": "string",
                        "description": "Specifies whether the input data is a classified image or ground truth data.A classified image is the image that was just classified. Ground truth data, or reference data, consists of identified featu...",
                        "default": None
                },
                "polygon_dimension_field": {
                        "type": "string",
                        "description": "The dimension field for the in_points parameter value. The assessment points will be updated based on the matching dimension values with this field.",
                        "default": None
                },
                "point_dimension_field": {
                        "type": "string",
                        "description": "The dimension field in the in_points parameter value. Input data with identical dimension values will be used to update corresponding points.\r\n\r\n\r\nWhen the in_class_data parameter value is a multidime...",
                        "default": None
                }
        },
        "required": [
                "in_class_data",
                "in_points",
                "out_points"
        ]
},
    "classify_objects_using_deep_learning": {
        "name": "classify_objects_using_deep_learning",
        "description": "Runs a trained deep learning model on an input raster and an optional feature class to produce a feature class or table in which each input object or feature has an assigned class or category label. This tool requires a model definition file containing trained model information. The model can be trained using the Train Deep Learning Model tool or by a third-party training software such as TensorFlow, PyTorch, or Keras. The model definition file can be an Esri model definition JSON file (.emd) or a deep learning model package, and it must contain the path to the Python raster function to be called to process each object and the path to the trained binary deep learning model file.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input image that will be used to classify objects.The input can be a single raster, multiple rasters in a mosaic dataset, an image service, a folder of images, or a feature class with image attach..."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will contain geometries surrounding the objects or feature from the input feature class, as well as a field to store the categorization label.If the feature class already..."
                },
                "in_model_definition": {
                        "type": "string",
                        "description": "The in_model_definition parameter value can be an Esri model definition JSON file (.emd), a JSON string, or a deep learning model package (.dlpk). A JSON string is useful when this tool is used on the..."
                },
                "in_features": {
                        "type": "string",
                        "description": "The point, line, or polygon input feature class that identifies the location of each object or feature to be classified and labelled. Each row in the input feature class represents a single object or ...",
                        "default": None
                },
                "class_label_field": {
                        "type": "string",
                        "description": "The name of the field that will contain the class or category label in the output feature class.If no field name is provided, a ClassLabel field will be generated in the output feature class.",
                        "default": None
                },
                "processing_mode": {
                        "type": "string",
                        "description": "Specifies how all raster items in a mosaic dataset or an image service will be processed. This parameter is applied when the input raster is a mosaic dataset or an image service.PROCESS_AS_MOSAICKED_I...",
                        "default": None
                },
                "model_arguments": {
                        "type": "string",
                        "description": "The information from the in_model_definition parameter will be used to set the default values for this parameter. These arguments vary, depending on the model architecture. The following are supported...",
                        "default": None
                },
                "caption_field": {
                        "type": "string",
                        "description": "The name of the field that will contain the text or caption in the output feature class. This parameter is only supported when an Image Captioner model is used.If no field name is specified, a Caption...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_feature_class",
                "in_model_definition"
        ]
},
    "classify_pixels_using_deep_learning": {
        "name": "classify_pixels_using_deep_learning",
        "description": "Runs a trained deep learning model on an input raster to produce a classified raster, with each valid pixel having an assigned class label. This tool requires a model definition file containing trained model information. The model can be trained using the Train Deep Learning Model tool or by a third-party training software such as TensorFlow, PyTorch, or Keras. The model definition file can be an Esri model definition JSON file (.emd) or a deep learning model package, and it must contain the path to the Python raster function to be called to process each object and the path to the trained binary deep learning model file.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster dataset that will be classified. The input can be a single raster, multiple rasters in a mosaic dataset, an image service, a folder of images, or a feature class with image attachment..."
                },
                "in_model_definition": {
                        "type": "string",
                        "description": "The in_model_definition parameter value can be an Esri model definition JSON file (.emd), a JSON string, or a deep learning model package (.dlpk). A JSON string is useful when this tool is used on the..."
                },
                "arguments": {
                        "type": "string",
                        "description": "The information from the in_model_definition parameter will be used to set the default values for this parameter. These arguments vary, depending on the model architecture. The following are supported...",
                        "default": None
                },
                "processing_mode": {
                        "type": "string",
                        "description": "Specifies how all raster items in a mosaic dataset or an image service will be processed. This parameter is applied when the input raster is a mosaic dataset or an image service.PROCESS_AS_MOSAICKED_I..."
                },
                "out_classified_folder": {
                        "type": "string",
                        "description": "The folder where the output classified rasters will be stored. A mosaic dataset will be generated using the classified rasters in this folder.This parameter is required when the input raster is a fold...",
                        "default": None
                },
                "out_featureclass": {
                        "type": "string",
                        "description": "The feature class where the output classified rasters will be stored.This parameter is required when the input raster is a feature class of images.If the feature class already exists, the results will...",
                        "default": None
                },
                "overwrite_attachments": {
                        "type": "string",
                        "description": "Specifies whether existing image attachments will be overwritten.NO_OVERWRITE\u2014Existing image attachments will not be overwritten and new image attachments will be stored in a new feature class. When t...",
                        "default": None
                },
                "use_pixelspace": {
                        "type": "string",
                        "description": "Specifies whether inferencing will be performed on images in pixel space.NO_PIXELSPACE\u2014Inferencing will be performed in map space. This is the default.PIXELSPACE\u2014Inferencing will be performed in image...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_model_definition",
                "processing_mode"
        ]
},
    "compute_accuracy_for_object_detection": {
        "name": "compute_accuracy_for_object_detection",
        "description": "Calculates the accuracy of a deep learning model by comparing the detected objects from the Detect Objects Using Deep Learning tool to ground truth data. Learn more about how Compute Accuracy For Object Detection works.",
        "parameters": {
                "detected_features": {
                        "type": "string",
                        "description": "The polygon feature class containing the objects detected from the Detect Objects Using Deep Learning tool."
                },
                "ground_truth_features": {
                        "type": "string",
                        "description": "The polygon feature class containing ground truth data."
                },
                "out_accuracy_table": {
                        "type": "string",
                        "description": "The output accuracy table."
                },
                "out_accuracy_report": {
                        "type": "string",
                        "description": "The name of the output accuracy report. The report is a PDF document containing accuracy metrics and charts.",
                        "default": None
                },
                "detected_class_value_field": {
                        "type": "string",
                        "description": "The field in the detected objects feature class that contains the class values or class names.If no field name is provided, a Classvalue or Value field will be used. If these fields do not exist, all ...",
                        "default": None
                },
                "ground_truth_class_value_field": {
                        "type": "string",
                        "description": "The field in the ground truth feature class that contains the class values.If no field name is provided, a Classvalue or Value field will be used. If these fields do not exist, all records will be ide...",
                        "default": None
                },
                "min_iou": {
                        "type": "string",
                        "description": "The IoU ratio that will be used as a threshold to evaluate the accuracy of the object detection model. The numerator is the area of overlap between the predicted bounding box and the ground reference ...",
                        "default": None
                },
                "mask_features": {
                        "type": "string",
                        "description": "A polygon feature class that delineates the area or areas where accuracy will be computed. Only the features that intersect the mask will be assessed for accuracy.",
                        "default": None
                }
        },
        "required": [
                "detected_features",
                "ground_truth_features",
                "out_accuracy_table"
        ]
},
    "compute_accuracy_for_pixel_classification": {
        "name": "compute_accuracy_for_pixel_classification",
        "description": "Computes a confusion matrix, based on errors of omission and commission, and the Intersection over Union (IoU) score. The accuracy is computed  between the output from the Classify Pixels Using Deep Learning tool  and the ground truth data. The tool is only valid for pixel classification models, not other models used with the Classify Pixels Using Deep Learning tool.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input classified raster."
                },
                "in_ground_truth_data": {
                        "type": "string",
                        "description": "The input classification image or other thematic GIS reference data. The input can be a raster or feature class.Typical data is a classification image of a single band of integer data type.If using po..."
                },
                "out_confusion_matrix": {
                        "type": "string",
                        "description": "The output file name of the confusion matrix in table format.The format of the table is determined by the output location and path. By default, the output will be a geodatabase table. If the path is n..."
                },
                "num_random_points": {
                        "type": "string",
                        "description": "The total number of random points that will be generated.The actual number may exceed but never fall below this number, depending on sampling strategy and number of classes. The default number of rand...",
                        "default": None
                },
                "sampling": {
                        "type": "string",
                        "description": "Specifies the sampling scheme that will be used.STRATIFIED_RANDOM\u2014Randomly distributed points will be created in each class in which each class has a number of points proportional to its relative area...",
                        "default": None
                },
                "min_point_distance": {
                        "type": "string",
                        "description": "The minimum distance between the reference points. The default is 0.",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_ground_truth_data",
                "out_confusion_matrix"
        ]
},
    "detect_change_using_deep_learning": {
        "name": "detect_change_using_deep_learning",
        "description": "Runs a trained deep learning model to detect change between two rasters. This tool requires a model definition file containing trained model information. The model definition file can be an Esri model definition JSON file (.emd) or a deep learning model package, and it must contain the path to the Python raster function to be called to process each object and the path to the trained binary deep learning model file.",
        "parameters": {
                "from_raster": {
                        "type": "string",
                        "description": "The input raster before the change."
                },
                "to_raster": {
                        "type": "string",
                        "description": "The input raster after the change."
                },
                "out_classified_raster": {
                        "type": "string",
                        "description": "The output classified raster that shows the change."
                },
                "in_model_definition": {
                        "type": "string",
                        "description": "The in_model_definition parameter value can be an Esri model definition JSON file (.emd), a JSON string, or a deep learning model package (.dlpk). A JSON string is useful when this tool is used on the..."
                },
                "arguments": {
                        "type": "string",
                        "description": "The information from the in_model_definition parameter will be used to set the default values for this parameter. These arguments vary, depending on the model architecture. The following are supported...",
                        "default": None
                }
        },
        "required": [
                "from_raster",
                "to_raster",
                "out_classified_raster",
                "in_model_definition"
        ]
},
    "detect_control_points": {
        "name": "detect_control_points",
        "description": "Detects ground control points in a mosaic dataset.",
        "parameters": {
                "in_mosaic_dataset": {
                        "type": "string",
                        "description": "The mosaic dataset that contains the source imagery from which the ground control points will be created."
                },
                "in_control_points": {
                        "type": "string",
                        "description": "The input control point set that contains a list of ground control point features."
                },
                "out_control_points": {
                        "type": "string",
                        "description": "The output ground control point features."
                },
                "out_folder_image_chips": {
                        "type": "string",
                        "description": "The output folder of image chips.",
                        "default": None
                },
                "tile_size": {
                        "type": "string",
                        "description": "The tile size of the output image chips.The default tile size is 1024.",
                        "default": None
                },
                "number_tie_points_per_gcp": {
                        "type": "string",
                        "description": "The number of tie points for each ground control point.The default is 5.",
                        "default": None
                }
        },
        "required": [
                "in_mosaic_dataset",
                "in_control_points",
                "out_control_points"
        ]
},
    "detect_objects_using_deep_learning": {
        "name": "detect_objects_using_deep_learning",
        "description": "Runs a trained deep learning model on an input raster to produce a feature class containing the objects it finds. The features can be bounding boxes or polygons around the objects found or points at the centers of the objects. This tool requires a model definition file containing trained model information. The model can be trained using the Train Deep Learning Model tool or by a third-party training software such as TensorFlow, PyTorch, or Keras. The model definition file can be an Esri model definition JSON file (.emd) or a deep learning model package, and it must contain the path to the Python raster function to be called to process each object and the path to the trained binary deep learning model file.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input image that will be used to detect objects. The input can be a single raster, multiple rasters in a mosaic dataset, an image service, a folder of images, a feature class with image attachment..."
                },
                "out_detected_objects": {
                        "type": "string",
                        "description": "The output feature class that will contain geometries circling the object or objects detected in the input image.If the feature class already exists, the results will be appended to the existing featu..."
                },
                "in_model_definition": {
                        "type": "string",
                        "description": "The in_model_definition parameter value can be an Esri model definition JSON file (.emd), a JSON string, or a deep learning model package (.dlpk). A JSON string is useful when this tool is used on the..."
                },
                "arguments": {
                        "type": "string",
                        "description": "The information from the in_model_definition parameter will be used to set the default values for this parameter. These arguments vary, depending on the model architecture. The following are supported...",
                        "default": None
                },
                "run_nms": {
                        "type": "string",
                        "description": "Specifies whether nonmaximum suppression will be performed in which duplicate objects are identified and the duplicate features with lower confidence value are removed.NO_NMS\u2014Nonmaximum suppression wi...",
                        "default": None
                },
                "confidence_score_field": {
                        "type": "string",
                        "description": "The name of the field in the feature class that will contain the confidence scores as output by the object detection method.This parameter is required when the run_nms parameter is set to NMS.",
                        "default": None
                },
                "class_value_field": {
                        "type": "string",
                        "description": "The name of the class value field in the input feature class. If no field name is provided, a Classvalue or Value field will be used. If these fields do not exist, all records will be identified as be...",
                        "default": None
                },
                "max_overlap_ratio": {
                        "type": "string",
                        "description": "The maximum overlap ratio for two overlapping features, which is defined as the ratio of intersection area over union area. The default is 0.",
                        "default": None
                },
                "processing_mode": {
                        "type": "string",
                        "description": "Specifies how all raster items in a mosaic dataset or an image service will be processed. This parameter is applied when the input raster is a mosaic dataset or an image service.PROCESS_AS_MOSAICKED_I...",
                        "default": None
                },
                "use_pixelspace": {
                        "type": "string",
                        "description": "Specifies whether inferencing will be performed on images in pixel space.NO_PIXELSPACE\u2014Inferencing will be performed in map space. This is the default.PIXELSPACE\u2014Inferencing will be performed in image...",
                        "default": None
                },
                "in_objects_of_interest": {
                        "type": "string",
                        "description": "Specifies the objects that will be detected by the tool. The available options will be based on the in_model_definition parameter value.This parameter is only active when the model detects more than o...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_detected_objects",
                "in_model_definition"
        ]
},
    "export_training_data_for_deep_learning": {
        "name": "export_training_data_for_deep_learning",
        "description": "Converts labeled vector or raster data to deep learning training datasets using a remote sensing image. The output is a folder of image chips and a folder of metadata files in the specified format.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input source imagery, typically multispectral imagery.Examples of the types of input source imagery include multispectral satellite, drone, aerial, and National Agriculture Imagery Program (NAIP)...."
                },
                "out_folder": {
                        "type": "string",
                        "description": "The folder where the output image chips and metadata will be stored.The folder can also be a folder URL that uses a cloud storage connection file (*.acs)."
                },
                "in_class_data": {
                        "type": "string",
                        "description": "The training sample data in either vector or raster form. Vector inputs should follow the training sample format generated using the Training Samples Manager pane. Raster inputs should follow a classi..."
                },
                "image_chip_format": {
                        "type": "string",
                        "description": "Specifies the raster format that will be used for the image chip outputs.The PNG and JPEG formats support up to three bands.TIFF\u2014TIFF format will be used.PNG\u2014PNG format will be used.JPEG\u2014JPEG format w..."
                },
                "tile_size_x": {
                        "type": "string",
                        "description": "The size of the image chips for the x dimension.",
                        "default": None
                },
                "tile_size_y": {
                        "type": "string",
                        "description": "The size of the image chips for the y dimension.",
                        "default": None
                },
                "stride_x": {
                        "type": "string",
                        "description": "The distance to move in the x direction when creating the next image chips.When stride is equal to tile size, there will be no overlap. When stride is equal to half the tile size, there will be 50 per...",
                        "default": None
                },
                "stride_y": {
                        "type": "string",
                        "description": "The distance to move in the y direction when creating the next image chips.When stride is equal to tile size, there will be no overlap. When stride is equal to half the tile size, there will be 50 per...",
                        "default": None
                },
                "output_nofeature_tiles": {
                        "type": "string",
                        "description": "Specifies whether image chips that do not capture training samples will be exported.ALL_TILES\u2014All image chips, including those that do not capture training samples, will be exported.ONLY_TILES_WITH_FE...",
                        "default": None
                },
                "metadata_format": {
                        "type": "string",
                        "description": "Specifies the format that will be used for the output metadata labels. If the input training sample data is a feature class layer, such as a building layer or a standard classification training sample...",
                        "default": None
                },
                "start_index": {
                        "type": "string",
                        "description": "Legacy:This parameter has been deprecated. Use a value of 0 or # in Python.",
                        "default": None
                },
                "class_value_field": {
                        "type": "string",
                        "description": "The field that contains the class values. If no field is specified, the system searches for a value or classvalue field. The field should be numeric, usually an integer. If the feature does not contai...",
                        "default": None
                },
                "buffer_radius": {
                        "type": "string",
                        "description": "The radius of a buffer around each training sample that will be used to delineate a training sample area. This allows you to create circular polygon training samples from points.\r\nThe linear unit of t...",
                        "default": None
                },
                "in_mask_polygons": {
                        "type": "string",
                        "description": "A polygon feature class that delineates the area where image chips will be created.Only image chips that fall completely within the polygons will be created.",
                        "default": None
                },
                "rotation_angle": {
                        "type": "string",
                        "description": "The rotation angle that will be used to generate image chips.\r\nAn image chip will first be generated with no rotation. It will then be rotated at the specified angle to create additional image chips. ...",
                        "default": None
                },
                "reference_system": {
                        "type": "string",
                        "description": "Specifies the type of reference system that will be used to interpret the input image. The reference system specified must match the reference system used to train the deep learning model.MAP_SPACE\u2014A ...",
                        "default": None
                },
                "processing_mode": {
                        "type": "string",
                        "description": "Specifies how all raster items in a mosaic dataset or an image service will be processed. This parameter is applied when the input raster is a mosaic dataset or an image service.PROCESS_AS_MOSAICKED_I...",
                        "default": None
                },
                "blacken_around_feature": {
                        "type": "string",
                        "description": "Specifies whether the pixels around each object or feature in each image tile will be masked out.This parameter only applies when the metadata_format parameter is set to Labeled_Tiles and an input fea...",
                        "default": None
                },
                "crop_mode": {
                        "type": "string",
                        "description": "Specifies whether the exported tiles will be cropped so that they are all the same size.This parameter only applies when the  metadata_format parameter is set to either Labeled_Tiles or Imagenet, and ...",
                        "default": None
                },
                "in_raster2": {
                        "type": "string",
                        "description": "An additional input  imagery source that will be used for image translation methods.This parameter is valid when the metadata_format parameter is set to Classified_Tiles, Export_Tiles, or CycleGAN.",
                        "default": None
                },
                "in_instance_data": {
                        "type": "string",
                        "description": "The training sample data collected that contains classes for instance segmentation. The input can also be a point feature class without a class value field or an integer raster without class informati...",
                        "default": None
                },
                "instance_class_value_field": {
                        "type": "string",
                        "description": "The field that contains the class values for instance segmentation. If no field is specified, the tool will use a value or class value field if one is present. If the feature does not contain a class ...",
                        "default": None
                },
                "min_polygon_overlap_ratio": {
                        "type": "string",
                        "description": "The minimum overlap percentage for a feature to be included in the training data. If the percentage overlap is less than the value specified, the feature will be excluded from the training chip and wi...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_folder",
                "in_class_data",
                "image_chip_format"
        ]
},
    "extract_features_using_ai_models": {
        "name": "extract_features_using_ai_models",
        "description": "Runs one or more pretrained deep learning models on an input raster to extract features and automate the postprocessing of the inferenced outputs. Learn more about how Extract Features Using AI Models works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster on which processing will be performed.If the mode parameter is specified as Only Postprocess, a raster with binary classification is required for this parameter."
                },
                "mode": {
                        "type": "string",
                        "description": "Specifies the mode that will be used for the processing of the input raster. Infer and Postprocess\u2014Features will be extracted from the imagery  and postprocessed. This is the default.Only Postprocess\u2014..."
                },
                "out_location": {
                        "type": "string",
                        "description": "The  geodatabase where the intermediate output from the models and the final postprocessed output will be stored."
                },
                "out_prefix": {
                        "type": "string",
                        "description": "A prefix that will be added to the name of the outputs that will be saved to the output location. The prefix will also be used as the name of a group layer that will be used to display all outputs."
                },
                "area_of_interest": {
                        "type": "string",
                        "description": "The geographical extent that will be used to extract features. Only features within the area of interest will be extracted.",
                        "default": None
                },
                "pretrained_models": {
                        "type": "string",
                        "description": "The ArcGIS pretrained models from ArcGIS Living Atlas of the World that can be used on the provided input raster.  This parameter requires an internet connection to download the pretrained models.",
                        "default": None
                },
                "additional_models": {
                        "type": "string",
                        "description": "The deep learning models that can be used on the provided input raster and the postprocessing workflow that will be used for additional model files (.dlpk and .emd). Available postprocessing workflows...",
                        "default": None
                },
                "confidence_threshold": {
                        "type": "string",
                        "description": "The minimum confidence of deep learning model that will be used when detecting objects. The value must be between 0 and 1.",
                        "default": None
                },
                "save_intermediate_output": {
                        "type": "string",
                        "description": "Specifies whether the intermediate outputs will be saved to the output location. The term intermediate outputs refers to the results generated after the model has been inferenced.\r\n\r\n\r\n\r\n\r\n\r\n\r\nTRUE\u2014Th...",
                        "default": None
                },
                "test_time_augmentation": {
                        "type": "string",
                        "description": "Specifies whether predictions of flipped and rotated variants of the input image will be merged into the final output.\r\n\r\n\r\n\r\n\r\n\r\n\r\nTRUE\u2014Predictions of flipped and rotated variants of the input image ...",
                        "default": None
                },
                "buffer_distance": {
                        "type": "string",
                        "description": "The  distance that will be used to buffer  polyline  features before they are used in postprocessing. The default is 15 meters.",
                        "default": None
                },
                "extend_length": {
                        "type": "string",
                        "description": "The maximum distance a  line segment will be extended to an intersecting feature. The default is 25 meters.",
                        "default": None
                },
                "smoothing_tolerance": {
                        "type": "string",
                        "description": "The tolerance used by the Polynomial Approximation with Exponential Kernel (PAEK) algorithm. The default is 30 meters.",
                        "default": None
                },
                "dangle_length": {
                        "type": "string",
                        "description": "The length at which line segments that do not touch another line at both endpoints (dangles) will be trimmed. The default is 5 meters.",
                        "default": None
                },
                "in_road_features": {
                        "type": "string",
                        "description": "A road feature class that will be used for refining the  parcels. The input can be a polygon or polyline feature class.",
                        "default": None
                },
                "road_buffer_width": {
                        "type": "string",
                        "description": "The buffer distance that will be used for the input road features.  The default value is 5 meters for polyline features and 0 meters for polygon features.",
                        "default": None
                },
                "regularize_parcels": {
                        "type": "string",
                        "description": "Specifies whether extracted parcels will be normalized by eliminating undesirable artifacts in their geometry.\r\n\r\n\r\n\r\n\r\n\r\n\r\nTRUE\u2014Extracted parcels will be normalized. This is the default.FALSE\u2014Extract...",
                        "default": None
                },
                "post_processing_workflow": {
                        "type": "string",
                        "description": "Specifies the postprocessing workflow that will be used. Line Regularization\u2014Line features will be extracted from a single band raster with binary classification and a polyline feature class will be g...",
                        "default": None
                },
                "out_features": {
                        "type": "string",
                        "description": "The feature class containing the postprocessed output.",
                        "default": None
                },
                "parcel_tolerance": {
                        "type": "string",
                        "description": "The minimum distance between\r\ncoordinates before they are considered equal. This parameter is used to reduce slivers between extracted parcels. The default is 3 meters.",
                        "default": None
                },
                "regularization_method": {
                        "type": "string",
                        "description": "Specifies the regularization method that will be used in postprocessing.Right Angles\u2014Shapes composed of 90\u00b0 angles between adjoining edges will be constructed. This is the default.Right Angles and Dia...",
                        "default": None
                },
                "poly_tolerance": {
                        "type": "string",
                        "description": "The maximum distance that the regularized footprint can deviate from the boundary of its originating feature. The default is 1 meter.",
                        "default": None
                },
                "prompt": {
                        "type": "string",
                        "description": "Specifies the segmentation method that will be used when the additional_models parameter is set to Polygon Segmentation.Centroid\u2014  The centroid of the detections will be used to indicate to the polygo...",
                        "default": None
                },
                "in_features": {
                        "type": "string",
                        "description": "The feature class on which postprocessing will be performed. This parameter is only supported when the post_processing_workflow parameter is set to Line Regularization or Polygon Regularization.",
                        "default": None
                },
                "out_summary": {
                        "type": "string",
                        "description": "The table that will contain a list of outputs that were generated along with their respective paths.",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "mode",
                "out_location",
                "out_prefix"
        ]
},
    "non_maximum_suppression": {
        "name": "non_maximum_suppression",
        "description": "Identifies duplicate features from the output of the Detect Objects Using Deep Learning tool as a postprocessing step and creates a new output with no duplicate features. The Detect Objects Using Deep Learning tool can return more than one bounding box or polygon for the same object, especially as a tiling side effect. If two features overlap more than a given maximum ratio, the feature with the lower confidence value will be removed.",
        "parameters": {
                "in_featureclass": {
                        "type": "string",
                        "description": "The input feature class or feature layer containing overlapping or duplicate features."
                },
                "confidence_score_field": {
                        "type": "string",
                        "description": "The field in the feature class that contains the confidence scores as output by the object detection method."
                },
                "out_featureclass": {
                        "type": "string",
                        "description": "The output feature class with the duplicate features removed."
                },
                "class_value_field": {
                        "type": "string",
                        "description": "The class value field in the input feature class. If not specified, the tool will use the standard class value fields  Classvalue and Value. If these fields do not exist, all features will be treated ...",
                        "default": None
                },
                "max_overlap_ratio": {
                        "type": "string",
                        "description": "The maximum overlap ratio for two overlapping features. This is defined as the ratio of intersection area over union area. The default is 0.",
                        "default": None
                }
        },
        "required": [
                "in_featureclass",
                "confidence_score_field",
                "out_featureclass"
        ]
},
    "train_deep_learning_model": {
        "name": "train_deep_learning_model",
        "description": "Trains a deep learning model using the output from the Export Training Data For Deep Learning tool.",
        "parameters": {
                "in_folder": {
                        "type": "string",
                        "description": "The folders containing the image chips, labels, and statistics required to train the model. This is the output from the Export Training Data For Deep Learning tool.Multiple input folders are supported..."
                },
                "out_folder": {
                        "type": "string",
                        "description": "The output folder location where the trained model will be stored."
                },
                "max_epochs": {
                        "type": "string",
                        "description": "The maximum number of epochs for which the model will be trained. A maximum epoch of 1 means the dataset will be passed forward and backward through the neural network one time. The default value is 2...",
                        "default": None
                },
                "model_type": {
                        "type": "string",
                        "description": "Specifies the model type that will be used to train the deep learning model.BDCN_EDGEDETECTOR\u2014 The Bi-Directional Cascade Network (BDCN) architecture will be used to train the model. BDCN Edge Detecto...",
                        "default": None
                },
                "batch_size": {
                        "type": "string",
                        "description": "The number of training samples that will be processed for training at one time.Increasing the batch size can improve tool performance; however, as the batch size increases, more memory is used. When n...",
                        "default": None
                },
                "arguments": {
                        "type": "string",
                        "description": "The information from the model_type parameter will be used to set the default values for this parameter. These arguments vary, depending on the model architecture. The supported model arguments for mo...",
                        "default": None
                },
                "learning_rate": {
                        "type": "string",
                        "description": "The rate at which existing information will be overwritten with newly acquired information throughout the training process. If no value is specified, the optimal learning rate will be extracted from t...",
                        "default": None
                },
                "backbone_model": {
                        "type": "string",
                        "description": "Specifies the preconfigured neural network that will be used as the architecture for training the new model. This method is known as Transfer Learning.1.40625deg\u2014This backbone was trained on imagery i...",
                        "default": None
                },
                "pretrained_model": {
                        "type": "string",
                        "description": "A pretrained model that will be used to fine-tune the new model. The input is an Esri model definition file (.emd) or a deep learning package file (.dlpk).A pretrained model with similar classes can b...",
                        "default": None
                },
                "validation_percentage": {
                        "type": "string",
                        "description": "The percentage of training samples that will be used for validating the model. The default value is 10.",
                        "default": None
                },
                "stop_training": {
                        "type": "string",
                        "description": "Specifies whether early stopping will be implemented.STOP_TRAINING\u2014Early stopping will be implemented, and the model training will stop when the model is no longer improving, regardless of the max_epo...",
                        "default": None
                },
                "freeze": {
                        "type": "string",
                        "description": "Specifies whether the backbone layers in the pretrained model will be frozen, so that the weights and biases remain as originally designed. FREEZE_MODEL\u2014The backbone layers will be frozen, and the pre...",
                        "default": None
                },
                "augmentation": {
                        "type": "string",
                        "description": "Specifies the type of data augmentation that will be used.Data augmentation is a technique of artificially increasing the training set by creating modified copies of a dataset using existing data.DEFA...",
                        "default": None
                },
                "augmentation_parameters": {
                        "type": "string",
                        "description": "Specifies the value for each transform in the augmentation parameter.\r\nrotate\u2014The image will be randomly rotated (in degrees) by a probability (p). If degrees is a range (a,b), a value will be uniform...",
                        "default": None
                },
                "chip_size": {
                        "type": "string",
                        "description": "The size of the image that will be used to train the model. Images will be cropped to the specified chip size.The default chip size will be the same as the tile size of the training data. If the x- an...",
                        "default": None
                },
                "resize_to": {
                        "type": "string",
                        "description": "Resizes the image chips. Once a chip is resized, pixel blocks of chip size will be cropped and used for training. This parameter applies to object detection (PASCAL VOC), object classification (labele...",
                        "default": None
                },
                "weight_init_scheme": {
                        "type": "string",
                        "description": "Specifies the scheme in which the weights will be initialized for the layer. To train a model with multispectral data, the model must accommodate the various types of bands available. This is done by ...",
                        "default": None
                },
                "monitor": {
                        "type": "string",
                        "description": "Specifies the metric that will be monitored while checkpointing and early stopping.VALID_LOSS\u2014The validation loss will be monitored. When the validation loss no longer changes significantly, the model...",
                        "default": None
                },
                "tensorboard": {
                        "type": "string",
                        "description": "Specifies whether Tensorboard metrics will be enabled while the tool is training. \r\nTensorboard can be accessed using the URL in the tool messages.This parameter is only supported for the following mo...",
                        "default": None
                }
        },
        "required": [
                "in_folder",
                "out_folder"
        ]
},
    "train_using_autodl": {
        "name": "train_using_autodl",
        "description": "Trains a deep learning model by building training pipelines and automating much of the training process.  This includes data augmentation, model selection, hyperparameter tuning, and batch size deduction. Its outputs include performance metrics of the best model on the training data, as well as the trained  deep learning model package (.dlpk file) that can be used as input for the Extract Features Using AI Models tool to predict on new imagery. Learn more about how AutoDL works",
        "parameters": {
                "in_data": {
                        "type": "string",
                        "description": "The folders containing the image chips, labels, and statistics required to train the model. This is the output from the Export Training Data For Deep Learning tool.   The metadata format of the export..."
                },
                "out_model": {
                        "type": "string",
                        "description": "The output trained model that will be saved as a deep learning package (.dlpk file)."
                },
                "pretrained_model": {
                        "type": "string",
                        "description": "A pretrained model that will be used to fine-tune the new model. The input is an Esri model definition file (.emd) or a deep learning package file (.dlpk).\r\nA pretrained model with similar classes can...",
                        "default": None
                },
                "total_time_limit": {
                        "type": "string",
                        "description": "The total time limit in hours it will take for AutoDL model training. The default is 2 hours.",
                        "default": None
                },
                "autodl_mode": {
                        "type": "string",
                        "description": "Specifies the AutoDL mode that will be used and how intensive the AutoDL\r\nsearch will be.\r\n\r\n\r\n\r\n\r\n\r\n\r\nBASIC\u2014The basic mode will be used. This mode is used to train all selected networks without hyper...",
                        "default": None
                },
                "networks": {
                        "type": "string",
                        "description": "Specifies the architectures that will be used to train the model. \r\nSingleShotDetector\u2014The SingleShotDetector architecture will be used to train the model. SingleShotDetector is used for object detect...",
                        "default": None
                },
                "save_evaluated_models": {
                        "type": "string",
                        "description": "Specifies whether all evaluated models will be saved.SAVE_ALL_MODELS\u2014 All evaluated models will be saved.SAVE_BEST_MODEL\u2014Only the best performing model will be saved. This is the default.",
                        "default": None
                }
        },
        "required": [
                "in_data",
                "out_model"
        ]
},
    "sample": {
        "name": "sample",
        "description": "Creates a table or a point feature class that shows the values of cells from a raster, or a set of rasters, for defined locations. The locations are defined by raster cells, points, polylines, or polygons. Learn more about how Sample works",
        "parameters": {
                "in_rastersin_raster": {
                        "type": "string",
                        "description": "The rasters with values that will be sampled based on the input location data.\r\nThe process_as_multidimensional parameter is only supported when the input is a single, multidimensional raster."
                },
                "in_location_data": {
                        "type": "string",
                        "description": "The data identifying positions where a sample will be taken.The input can be a raster or a feature class."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table or feature class containing the sampled cell values.The output format is determined by the output location and path. By default, the output will be a geodatabase table or a geodatabas..."
                },
                "resampling_type": {
                        "type": "string",
                        "description": "The resampling algorithm that will be used to sample a raster to determine how the values will be obtained from the raster.\r\nNEAREST\u2014Nearest neighbor assignment will be used. This is the default.BILIN...",
                        "default": None
                },
                "unique_id_field": {
                        "type": "string",
                        "description": "A field containing a different value for every location or feature in the input location raster or features.",
                        "default": None
                },
                "process_as_multidimensional": {
                        "type": "string",
                        "description": "Specifies how the input rasters will be processed.This parameter is only available when the input is a single, multidimensional raster.ALL_SLICES\u2014Samples will be processed for all dimensions (such as ...",
                        "default": None
                },
                "acquisition_definition": {
                        "type": "string",
                        "description": "Specifies the time, depth, or other acquisition data associated with the location features.Only the following combinations are supported:\r\nDimension + Start field or valueDimension + Start field or va...",
                        "default": None
                },
                "statistics_type": {
                        "type": "string",
                        "description": "Specifies the statistic type to be calculated.MINIMUM\u2014The minimum value within the specified range will be calculated.MAXIMUM\u2014The maximum value within the specified range will be calculated.MEDIAN\u2014The...",
                        "default": None
                },
                "percentile_value": {
                        "type": "string",
                        "description": "The percentile to calculate when the Statistics Type parameter is set to Percentile.\r\nThe percentile to calculate when the statistics_type parameter is set to PERCENTILE.This value can range from 0 to...",
                        "default": None
                },
                "buffer_distance": {
                        "type": "string",
                        "description": "The distance around the location data features. The buffer distance is specified in the linear unit of the location feature's spatial reference. If the feature uses a geographic reference, the unit wi...",
                        "default": None
                },
                "layout": {
                        "type": "string",
                        "description": "Specifies whether sampled values will appear in rows or columns in the output table.ROW_WISE\u2014Sampled values will appear in separate rows in the output table. This is the default.COLUMN_WISE\u2014Sampled va...",
                        "default": None
                },
                "generate_feature_class": {
                        "type": "string",
                        "description": "Specifies whether a point feature class with sampled values in its attribute table or a table with sampled values will be generated.TABLE\u2014A table with sampled values will be generated. This is the def...",
                        "default": None
                }
        },
        "required": [
                "in_rastersin_raster",
                "in_location_data",
                "out_table"
        ]
},
    "interpolate_from_spatiotemporal_points": {
        "name": "interpolate_from_spatiotemporal_points",
        "description": "Interpolates temporal point data into a multidimensional raster.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The input point layer, trajectory layer, or trajectory dataset."
                },
                "variable_field": {
                        "type": "string",
                        "description": "A field containing variable values."
                },
                "time_field": {
                        "type": "string",
                        "description": "A field containing time values."
                },
                "temporal_aggregation": {
                        "type": "string",
                        "description": "Specifies the temporal aggregation of the output multidimensional raster. The interpolation algorithm uses all available data within these time periods to calculate the output slice.DAILY\u2014The data val...",
                        "default": None
                },
                "cell_size": {
                        "type": "string",
                        "description": "The output cell size. By default, the cell size will be the shorter of the width or the height of the input point feature extent, divided by 250.",
                        "default": None
                },
                "interpolation_method": {
                        "type": "string",
                        "description": "Specifies the interpolation method that will be used.\r\nIDW\u2014Inverse distance weighted interpolation will be used.TRIANGULATION\u2014Triangulation interpolation will be used.MEAN\u2014Mean interpolation will be u..."
                }
        },
        "required": [
                "in_dataset",
                "variable_field",
                "time_field",
                "interpolation_method"
        ]
},
    "optimal_interpolation": {
        "name": "optimal_interpolation",
        "description": "Statistically assimilates data combined from multiple sources to produce an output raster. The tool can be used to merge background data, such as model outputs, with observation data, such as point measurements, to perform interpolation. Learn more about how Optimal Interpolation works.",
        "parameters": {
                "in_background_raster": {
                        "type": "string",
                        "description": "The input background raster also known as the background field."
                },
                "in_obs_data": {
                        "type": "string",
                        "description": "The input point features that will be used for interpolation."
                },
                "obs_field": {
                        "type": "string",
                        "description": "The field containing observation values that will be used for interpolation."
                },
                "background_error_var": {
                        "type": "string",
                        "description": "The error variance of the background measurements. The input can be a single value or an error variance raster. If a single value is provided, the value will be used as the error variance for all back..."
                },
                "obs_error_var": {
                        "type": "string",
                        "description": "The error variance of the observations. The input can be a single value or a field from the observation data. If a single value is provided, the value will be used as the error variance for all observ..."
                },
                "background_error_corr_length": {
                        "type": "string",
                        "description": "The correlation length between background measurements. The default is three times the cell size of the in_background_raster parameter value.",
                        "default": None
                }
        },
        "required": [
                "in_background_raster",
                "in_obs_data",
                "obs_field",
                "background_error_var",
                "obs_error_var"
        ]
},
    "raster_calculator": {
        "name": "raster_calculator",
        "description": "Build and run a single map algebra expression using Python syntax. Learn more about how Raster Calculator works",
        "parameters": {
                "expression": {
                        "type": "string",
                        "description": "Note:In Python, create and run map algebra expressions using the Image Analyst module, which is an extension of the ArcPy Python site package.See Map algebra to learn how to perform an analysis in Pyt..."
                },
                "output_raster": {
                        "type": "string",
                        "description": "Note:See Create output for information about producing output from map algebra expressions in Python."
                }
        },
        "required": [
                "expression",
                "output_raster"
        ]
},
    "abs": {
        "name": "abs",
        "description": "Calculates the absolute value of the cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input raster for which to calculate the absolute values.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "divide": {
        "name": "divide",
        "description": "Divides the values of two rasters on a cell-by-cell basis.",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input whose values will be divided by the second input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inp..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input whose values the first input are to be divided by.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both in..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "exp": {
        "name": "exp",
        "description": "Calculates the base e exponential of the cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input values for which to find the base e exponential.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "exp10": {
        "name": "exp10",
        "description": "Calculates the base 10 exponential of the cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input values for which to find the base 10 exponential.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "exp2": {
        "name": "exp2",
        "description": "Calculates the base 2 exponential of the cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input values for which to find the base 2 exponential.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "float": {
        "name": "float",
        "description": "Converts each cell value of a raster into a floating-point representation.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input raster to be converted to floating point.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "int": {
        "name": "int",
        "description": "Converts each cell value of a raster to an integer by truncation.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input raster to be converted to integer.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "ln": {
        "name": "ln",
        "description": "Calculates the natural logarithm (base e) of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "Input values for which to find the natural logarithm (Ln).To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "log10": {
        "name": "log10",
        "description": "Calculates the base 10 logarithm of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "Input values for which to find the base 10 logarithm.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "log2": {
        "name": "log2",
        "description": "Calculates the base 2 logarithm of cells in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "Input values for which to find the base 2 logarithm.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "minus": {
        "name": "minus",
        "description": "Subtracts the value of the second input raster from the value of the first input raster on a cell-by-cell basis.",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input from which to subtract the values in the second input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for bot..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input values to subtract from the values in the first input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for bot..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "mod": {
        "name": "mod",
        "description": "Finds the remainder (modulo) of the first raster when divided by the second raster on a cell-by-cell basis.",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The numerator input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the cell size and extent must firs..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The denominator input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the cell size and extent must fi..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "negate": {
        "name": "negate",
        "description": "Changes the sign (multiplies by -1) of the cell values of the input raster on a cell-by-cell basis.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input raster to be negated (multiplied by -1).To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "plus": {
        "name": "plus",
        "description": "Adds (sums) the values of two rasters on a cell-by-cell basis.",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input whose values will be added to.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the cell size ..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input whose values will be added to the first input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "power": {
        "name": "power",
        "description": "Raises the cell values in a raster to the power of the values found in another raster.",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input values to be raised to the power defined by the second input.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number ..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input that determines the power the values in the first input will be raised to.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To spec..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "round_down": {
        "name": "round_down",
        "description": "Returns the next lower integer value, just represented as a floating point, for each cell in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input values to be rounded down.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "round_up": {
        "name": "round_up",
        "description": "Returns the next higher integer value, just represented as a floating point, for each cell in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input values to be rounded up.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "square": {
        "name": "square",
        "description": "Calculates the square of the cell values in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input values to find the square of.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "square_root": {
        "name": "square_root",
        "description": "Calculates the square root of the cell values in a raster.",
        "parameters": {
                "in_raster_or_constant": {
                        "type": "string",
                        "description": "The input values to find the square root of.To use a number as an input for this parameter, the cell size and extent must first be set in the environment."
                }
        },
        "required": [
                "in_raster_or_constant"
        ]
},
    "times": {
        "name": "times",
        "description": "Multiplies the values of two rasters on a cell-by-cell basis.",
        "parameters": {
                "in_raster_or_constant1": {
                        "type": "string",
                        "description": "The input containing the values to be multiplied.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a number for both inputs, the c..."
                },
                "in_raster_or_constant2": {
                        "type": "string",
                        "description": "The input containing the values by which the first input will be multiplied.A number can be used as an input for this parameter, provided a raster is specified for the other parameter. To specify a nu..."
                }
        },
        "required": [
                "in_raster_or_constant1",
                "in_raster_or_constant2"
        ]
},
    "extract_video_frames_to_images": {
        "name": "extract_video_frames_to_images",
        "description": "Extracts video frame images and associated metadata from a full-motion video (FMV)-compliant video stream.  The extracted images can be added to a mosaic dataset or other tools and functions for further analysis.",
        "parameters": {
                "in_video": {
                        "type": "string",
                        "description": "The input video file in any of the supported video file formats, including  .av1, .avi, .csv, .gpx, .h264, .h265, .json, .mp2, .mp4, .m2ts, .mpeg, .mpeg2, .mpeg4, .mpg, .mpg2, .mpg4, .ps, .ts, .vob, a..."
                },
                "out_folder": {
                        "type": "string",
                        "description": "The \r\nfile directory where the output images and metadata will be saved."
                },
                "image_type": {
                        "type": "string",
                        "description": "Specifies the output image format.JPEG\u2014The output will be in JPEG image format.TIFF\u2014The output will be in TIFF image format. This is the default.NITF\u2014The output will be in NITF image format.PNG\u2014The ou...",
                        "default": None
                },
                "image_overlap": {
                        "type": "string",
                        "description": "The maximum overlap percentage between two images. If the overlap between a candidate image and the last image written to disk is greater than this value, the candidate image will be ignored. The defa...",
                        "default": None
                },
                "require_fresh_metadata": {
                        "type": "string",
                        "description": "Specifies whether  only video frames with associated metadata will be extracted and saved.   REQUIRE_FRESH_METADATA\u2014Only video frames with associated metadata will be saved.NO_REQUIRE_FRESH_METADATA\u2014A...",
                        "default": None
                },
                "min_time": {
                        "type": "string",
                        "description": "The minimum time interval between video frames that will be saved. If no value is provided, all video frames will be saved as images.",
                        "default": None
                }
        },
        "required": [
                "in_video",
                "out_folder"
        ]
},
    "video_metadata_to_feature_class": {
        "name": "video_metadata_to_feature_class",
        "description": "Extracts the platform, frame center, frame outline, and attributes metadata from a full-motion video (FMV)-compliant video. The output geometry and attributes are saved as feature classes.",
        "parameters": {
                "in_video": {
                        "type": "string",
                        "description": "The FMV-compliant input video file containing essential metadata for each frame of the video data. The supported video file types are .av1, .avi, .csv, .gpx, .h264, .h265, .json, .mp2, .mp4, .m2ts, .m..."
                },
                "csv_file": {
                        "type": "string",
                        "description": "An output .csv or .json file containing metadata about the video frames for specific times.The metadata file is in the same format used by the Video Multiplexer tool.",
                        "default": None
                },
                "flightpath": {
                        "type": "string",
                        "description": "The feature class containing the sensor's flight path information.",
                        "default": None
                },
                "flightpath_type": {
                        "type": "string",
                        "description": "Specifies the feature class type that will be used for the flight path.POINT\u2014A point feature class will be used.POLYLINE\u2014A polyline feature class will be used. This is the default.",
                        "default": None
                },
                "imagepath": {
                        "type": "string",
                        "description": "The output feature class containing the image path information.",
                        "default": None
                },
                "imagepath_type": {
                        "type": "string",
                        "description": "Specifies the feature class type that will be used for the image path.  If you're using a point output, the center of each video frame image will appear on the map.POINT\u2014A point feature class will be ...",
                        "default": None
                },
                "footprint": {
                        "type": "string",
                        "description": "The output feature class containing the video image footprint information.",
                        "default": None
                },
                "start_time": {
                        "type": "string",
                        "description": "The metadata recording start time from the beginning of the video. The input format is d.hh:mm:ss, and the default start time is 0.00:00:00. Metadata time stamps are not used in this field; the time o...",
                        "default": None
                },
                "stop_time": {
                        "type": "string",
                        "description": "The metadata recording end time. The input format is d.hh:mm:ss. If  no value is provided, the value will default to the end of the video. Metadata time stamps are not used in this field.",
                        "default": None
                },
                "min_distance": {
                        "type": "string",
                        "description": "The distance between the features in sequential video frames. If no value is provided, every metadata feature will be extracted and added to the feature class.",
                        "default": None
                },
                "min_time": {
                        "type": "string",
                        "description": "The time interval between the features in sequential video frames. If no value is provided, every metadata feature will be extracted and added to the feature class.",
                        "default": None
                },
                "vmti": {
                        "type": "string",
                        "description": "The output feature dataset containing the video VMTI information.",
                        "default": None
                }
        },
        "required": [
                "in_video"
        ]
},
    "video_multiplexer": {
        "name": "video_multiplexer",
        "description": "Creates a single full-motion video (FMV)-compliant video file that combines an archived video stream file and a separate associated metadata file synchronized by a time stamp. The process of combining the two files containing the video and metadata files is called multiplexing.",
        "parameters": {
                "in_video_file": {
                        "type": "string",
                        "description": "The input video file that will be converted to an FMV-compliant video file.The following file types are supported: .av1,.avi, .csv, .gpx, .h264, .h265, .json, .mp2, .mp4, .m2ts, .mpeg, .mpeg2, .mpeg4,..."
                },
                "metadata_file": {
                        "type": "string",
                        "description": "A .csv, .json, or .gpx file containing metadata about the video frames for specific times. Each column in the metadata file represents one metadata field, and one of the columns must be a time referen..."
                },
                "out_video_file": {
                        "type": "string",
                        "description": "The name of the output video file, including the file extension.The supported output video file is a .ts file."
                },
                "metadata_mapping_file": {
                        "type": "string",
                        "description": "A .csv file that contains 5 columns and 87 rows and is based on the FMV_Multiplexer_Field_Mapping_Template.csv template file obtained from C:\\Program Files\\ArcGIS\\Pro\\Resources\\MotionImagery.Each row ...",
                        "default": None
                },
                "timeshift_file": {
                        "type": "string",
                        "description": "A file containing defined time shift intervals.Ideally, the video images and the metadata are synchronized in time. In this case, the image footprint in FMV surrounds features that can be seen in the ...",
                        "default": None
                },
                "elevation_layer": {
                        "type": "string",
                        "description": "The source of the elevation needed for calculating the video frame corner coordinates. The source can be a layer, image service, or an average ground elevation or ocean depth. The average elevation va...",
                        "default": None
                },
                "input_coordinate_system": {
                        "type": "string",
                        "description": "The coordinate system that will be used for the metadata_file parameter value.",
                        "default": None
                }
        },
        "required": [
                "in_video_file",
                "metadata_file",
                "out_video_file"
        ]
},
    "aggregate_multidimensional_raster": {
        "name": "aggregate_multidimensional_raster",
        "description": "Generates a multidimensional raster dataset by combining existing multidimensional raster variables along a dimension.",
        "parameters": {
                "in_multidimensional_raster": {
                        "type": "string",
                        "description": "The input multidimensional raster dataset."
                },
                "dimension": {
                        "type": "string",
                        "description": "The aggregation dimension. This is the dimension along which the variables will be aggregated."
                },
                "aggregation_method": {
                        "type": "string",
                        "description": "Specifies the mathematical method that will be used to combine the aggregated slices in an interval.MEAN\u2014The mean of a pixel's values will be calculated across all slices in the interval. This is the ...",
                        "default": None
                },
                "variables": {
                        "type": "string",
                        "description": "The variable or variables that will be aggregated along the given dimension. If no variable is specified, all variables with the selected dimension will be aggregated.For example, to aggregate daily t...",
                        "default": None
                },
                "aggregation_def": {
                        "type": "string",
                        "description": "Specifies the dimension interval for which the data will be aggregated.ALL\u2014The data values will be aggregated across all slices. This is the default.INTERVAL_KEYWORD\u2014The variable data will be aggregat...",
                        "default": None
                },
                "interval_keyword": {
                        "type": "string",
                        "description": "Specifies the keyword interval that will be used when aggregating along the dimension. This parameter is required when the aggregation_def parameter is set to INTERVAL_KEYWORD and the aggregation must...",
                        "default": None
                },
                "interval_value": {
                        "type": "string",
                        "description": "The size of the interval that will be used for the aggregation. This parameter is required when the aggregation_def parameter is set to INTERVAL_VALUE.For example, to aggregate 30 years of monthly tem...",
                        "default": None
                },
                "interval_unit": {
                        "type": "string",
                        "description": "The unit that will be used for the interval_value parameter. This parameter is required when the dimension parameter is set to a time field and the aggregation_def parameter is set to INTERVAL_VALUE.I...",
                        "default": None
                },
                "interval_ranges": {
                        "type": "string",
                        "description": "Interval ranges specified in a value table will be used to aggregate groups of values. The value table consists of pairs of minimum and maximum range values, with data type Double or Date.\r\nThis param...",
                        "default": None
                },
                "aggregation_function": {
                        "type": "string",
                        "description": "A custom raster function that will be used to compute the pixel values of the aggregated rasters. The input is a raster function JSON object or an .rft.xml file created from a function chain or a cust...",
                        "default": None
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Specifies whether NoData values will be ignored in the analysis.DATA\u2014The analysis will include all valid pixels along a given dimension and ignore NoData pixels. This is the default.NODATA\u2014The analysi...",
                        "default": None
                },
                "dimensionless": {
                        "type": "string",
                        "description": "Specifies whether the layer will have dimension values. This parameter is only enabled if a single slice is selected to create a layer.NO_DIMENSIONS\u2014 The layer will not have dimension values.DIMENSION...",
                        "default": None
                },
                "percentile_value": {
                        "type": "string",
                        "description": "The percentile that will be calculated. The default is 90, indicating the 90th percentile.The values can range from 0 to 100. The 0th percentile is essentially equivalent to the minimum statistic, and...",
                        "default": None
                },
                "percentile_interpolation_type": {
                        "type": "string",
                        "description": "Specifies the method of percentile interpolation that will be used when there is an even number of values from the input raster to be calculated.NEAREST\u2014The nearest available value to the desired perc...",
                        "default": None
                }
        },
        "required": [
                "in_multidimensional_raster",
                "dimension"
        ]
},
    "find_argument_statistics": {
        "name": "find_argument_statistics",
        "description": "Extracts the dimension value or band index at which a given statistic is attained for each pixel in a multidimensional or multiband raster.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input multidimensional or multiband raster to be analyzed."
                },
                "dimension": {
                        "type": "string",
                        "description": "The dimension from which the statistic will be extracted. If the input raster is not a multidimensional raster, this parameter is not required.",
                        "default": None
                },
                "dimension_def": {
                        "type": "string",
                        "description": "Specifies how the statistic will be extracted from the dimension. ALL\u2014The statistic will be extracted across all dimensions. This is the default.INTERVAL_KEYWORD\u2014The statistic will be extracted from t...",
                        "default": None
                },
                "interval_keyword": {
                        "type": "string",
                        "description": "The unit of time for which the statistic will be extracted.For example, you have five years of daily sea surface temperature data and you want to know the year in which the maximum temperature was obs...",
                        "default": None
                },
                "variables": {
                        "type": "string",
                        "description": "The variable or variables to be analyzed. If the input raster is not multidimensional, the pixel values of the multiband raster are considered the variable. If the input raster is multidimensional and...",
                        "default": None
                },
                "statistics_type": {
                        "type": "string",
                        "description": "Specifies the statistic to extract from the variable or variables along the given dimension.ARGUMENT_MIN\u2014The dimension value at which the minimum variable value is reached will be extracted. This is t...",
                        "default": None
                },
                "min": {
                        "type": "string",
                        "description": "The minimum variable value to be used to extract the duration.This parameter is required when the statistics_type parameter is set to DURATION.",
                        "default": None
                },
                "max": {
                        "type": "string",
                        "description": "The maximum variable value to be used to extract the duration.This parameter is required when the statistics_type parameter is set to DURATION.",
                        "default": None
                },
                "multiple_occurrence": {
                        "type": "string",
                        "description": "The pixel value to use to indicate that a given argument statistic was reached more than once in the input raster dataset. If not specified, the pixel value will be the value of the dimension as speci...",
                        "default": None
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Specifies whether NoData values will be ignored in the analysis.DATA\u2014The analysis will include all valid pixels along a given dimension and ignore NoData pixels. This is the default.NODATA\u2014The analysi...",
                        "default": None
                },
                "value": {
                        "type": "string",
                        "description": "The value at which a comparison will be made to extract the dimension value.This parameter is required when the Statistics Type parameter is set to Argument of the value.",
                        "default": None
                },
                "comparison": {
                        "type": "string",
                        "description": "Specifies the comparison type that will be used to extract the dimension value.EQUAL_TO\u2014The extracted dimension is equal to the specified value. This is the default.GREATER_THAN\u2014The extracted dimensio...",
                        "default": None
                },
                "occurrence": {
                        "type": "string",
                        "description": "Specifies whether the value of the dimension will be returned the first time or last time the argument statistic is reached.FIRST_OCCURRENCE\u2014The value of the dimension will be returned the first time ...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "generate_multidimensional_anomaly": {
        "name": "generate_multidimensional_anomaly",
        "description": "Computes the anomaly for each slice in an existing multidimensional raster to generate a new multidimensional raster. An anomaly is the deviation of an observation from its standard or mean value.",
        "parameters": {
                "in_multidimensional_raster": {
                        "type": "string",
                        "description": "The input multidimensional raster dataset."
                },
                "variables": {
                        "type": "string",
                        "description": "The variable or variables for which anomalies will be calculated. If no variable is specified, all variables with a time dimension will be analyzed.",
                        "default": None
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to calculate the anomaly.\r\nDIFFERENCE_FROM_MEAN\u2014The difference between a pixel's value and the mean of that pixel's values across slices defined by the interval ...",
                        "default": None
                },
                "calculation_interval": {
                        "type": "string",
                        "description": "Specifies the temporal interval that will be used to calculate the mean.ALL\u2014The mean is calculated across all slices for each pixel.YEARLY\u2014The yearly mean is calculated for each pixel.RECURRING_MONTHL...",
                        "default": None
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Specifies whether NoData values will be ignored in the analysis.DATA\u2014The analysis will include all valid pixels along a given dimension and ignore NoData pixels. This is the default.NODATA\u2014The analysi...",
                        "default": None
                },
                "reference_mean_raster": {
                        "type": "string",
                        "description": "The reference raster dataset that contains a previously calculated mean for each pixel. The anomalies will be calculated in comparison to this mean.",
                        "default": None
                }
        },
        "required": [
                "in_multidimensional_raster"
        ]
},
    "generate_trend_raster": {
        "name": "generate_trend_raster",
        "description": "Estimates the trend for each pixel along a dimension for one or more variables in a multidimensional raster.",
        "parameters": {
                "in_multidimensional_raster": {
                        "type": "string",
                        "description": "The input multidimensional raster dataset."
                },
                "dimension": {
                        "type": "string",
                        "description": "The dimension along which a trend will be extracted for the variable or variables selected in the analysis."
                },
                "variables": {
                        "type": "string",
                        "description": "The variable or variables for which trends will be calculated. If no variable is specified, the first variable in the multidimensional raster will be analyzed.",
                        "default": None
                },
                "line_type": {
                        "type": "string",
                        "description": "Specifies the type of trend analysis to perform to pixel values along a dimension.LINEAR\u2014Variable pixel values will be fitted along a linear trend line. This is the default.POLYNOMIAL\u2014Variable pixel v...",
                        "default": None
                },
                "frequency": {
                        "type": "string",
                        "description": "The frequency or the polynomial order number to use in the trend fitting. If the trend type is polynomial, this parameter specifies the polynomial order. If the trend type is harmonic, this parameter ...",
                        "default": None
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Specifies whether NoData values will be ignored in the analysis.DATA\u2014The analysis will include all valid pixels along a given dimension and ignore NoData pixels. This is the default.NODATA\u2014The analysi...",
                        "default": None
                },
                "cycle_length": {
                        "type": "string",
                        "description": "The length of periodic variation to model.  This parameter is required when line_type is set to HARMONIC. For example, leaf greenness often has one strong cycle of variation in a single year, so the c...",
                        "default": None
                },
                "cycle_unit": {
                        "type": "string",
                        "description": "Specifies the time unit to be used for the length of a harmonic cycle.DAYS\u2014The unit for the length of the harmonic cycle is days.YEARS\u2014The unit for the length of the harmonic cycle is years. This is t...",
                        "default": None
                },
                "rmse": {
                        "type": "string",
                        "description": "Specifies whether the root mean square error (RMSE) of the trend fit line will be calculated.RMSE\u2014The RMSE will be calculated. This is the default.NO_RMSE\u2014The RMSE will not be calculated.",
                        "default": None
                },
                "r2": {
                        "type": "string",
                        "description": "Specifies whether the R-squared goodness-of-fit statistic  for the trend fit line will be calculated.R2\u2014The R-squared value will be calculated.NO_R2\u2014The R-squared value will not be calculated. This is...",
                        "default": None
                },
                "slope_p_value": {
                        "type": "string",
                        "description": "Specifies whether the p-value statistic  for the slope coefficient of the trend line will be calculated.SLOPEPVALUE\u2014The p-value will be calculated. NO_SLOPEPVALUE\u2014The p-value will not be calculated. T...",
                        "default": None
                },
                "seasonal_period": {
                        "type": "string",
                        "description": "Specifies the time unit to be used for the length of a seasonal period when performing the Seasonal-Kendall test.DAYS\u2014The unit for the length of the seasonal period is days. This is the default.MONTHS...",
                        "default": None
                }
        },
        "required": [
                "in_multidimensional_raster",
                "dimension"
        ]
},
    "interpolate_from_spatiotemporal_points": {
        "name": "interpolate_from_spatiotemporal_points",
        "description": "Interpolates temporal point data into a multidimensional raster.",
        "parameters": {
                "in_dataset": {
                        "type": "string",
                        "description": "The input point layer, trajectory layer, or trajectory dataset."
                },
                "variable_field": {
                        "type": "string",
                        "description": "A field containing variable values."
                },
                "time_field": {
                        "type": "string",
                        "description": "A field containing time values."
                },
                "temporal_aggregation": {
                        "type": "string",
                        "description": "Specifies the temporal aggregation of the output multidimensional raster. The interpolation algorithm uses all available data within these time periods to calculate the output slice.DAILY\u2014The data val...",
                        "default": None
                },
                "cell_size": {
                        "type": "string",
                        "description": "The output cell size. By default, the cell size will be the shorter of the width or the height of the input point feature extent, divided by 250.",
                        "default": None
                },
                "interpolation_method": {
                        "type": "string",
                        "description": "Specifies the interpolation method that will be used.\r\nIDW\u2014Inverse distance weighted interpolation will be used.TRIANGULATION\u2014Triangulation interpolation will be used.MEAN\u2014Mean interpolation will be u..."
                }
        },
        "required": [
                "in_dataset",
                "variable_field",
                "time_field",
                "interpolation_method"
        ]
},
    "multidimensional_principal_components": {
        "name": "multidimensional_principal_components",
        "description": "Transforms multidimensional rasters into  their principal components, loadings, and eigenvalues. The tool transforms the data into a reduced number of components that account for the variance of the data, so that spatial and temporal patterns can be readily identified.",
        "parameters": {
                "in_multidimensional_raster": {
                        "type": "string",
                        "description": "The input multidimensional raster.The tool processes data along one dimension, such as a time series raster or a data cube defined by a nontime dimension [X, Y, Z]. If an input variable includes multi..."
                },
                "mode": {
                        "type": "string",
                        "description": "Specifies the method that will be used to perform principal component analysis.DIMENSION_REDUCTION\u2014The input time series data will be treated as a set of images. Principal components that  extract pre..."
                },
                "dimension": {
                        "type": "string",
                        "description": "The dimension name used to process the principal components."
                },
                "out_pc": {
                        "type": "string",
                        "description": "The name of the output raster dataset. When the mode parameter is specified as DIMENSION_REDUCTION, the output will be a multiband raster with the components as bands. The first band is the first prin..."
                },
                "out_loadings": {
                        "type": "string",
                        "description": "The output loadings data contributing to the principal components.When the mode parameter is specified as DIMENSION_REDUCTION, the output will be a table containing the weights that each input raster ..."
                },
                "out_eigenvalues": {
                        "type": "string",
                        "description": "The output Eigenvalues table. Eigenvalues are values indicating the variance percentage of each component. Eigenvalues help you define the number of principal components that are needed to represent t...",
                        "default": None
                },
                "variable": {
                        "type": "string",
                        "description": "The variable of the input multidimensional raster used in computation. If the input raster is multidimensional and no variable is specified, only the first variable will be analyzed, by default.For ex...",
                        "default": None
                },
                "number_of_pc": {
                        "type": "string",
                        "description": "The number of principal components to compute, usually fewer than the number of input rasters.This parameter also takes the form of a percentage (%).  For example, a value of 90% means the number of c...",
                        "default": None
                }
        },
        "required": [
                "in_multidimensional_raster",
                "mode",
                "dimension",
                "out_pc",
                "out_loadings"
        ]
},
    "multidimensional_raster_correlation": {
        "name": "multidimensional_raster_correlation",
        "description": "Analyzes correlations between two variables in one or two multidimensional rasters. The tool takes two multidimensional rasters as input, compares two variables using the Pearson, Kendall, or Spearman correlation method, and outputs a correlation raster, with each pixel representing the correlation values of the corresponding pixel arrays. The output raster can map where the two variables are correlated and where they are not correlated. The tool can also calculate cross correlation when the lag is a nonzero value and calculate auto correlation when the two inputs are the same. You can analyze correlations between two variables in one or two multidimensional rasters.   The output is a correlation raster in which each pixel is the correlation of the two time series from the two variables.   The tool can be used to calculate correlation with a lag, a cross correlation, or an autocorrelation. For example, the correlation raster in the images below was calculated from a soil moisture variable over time and a precipitation variable over time.",
        "parameters": {
                "in_mdim_raster1": {
                        "type": "string",
                        "description": "The input multidimensional raster dataset.The first multidimensional raster in any supported format."
                },
                "in_mdim_raster2": {
                        "type": "string",
                        "description": "The second multidimensional raster that will be correlated with the first input. The length of the dimension used in the calculation must be greater than 2. Autocorrelation will be calculated if the i..."
                },
                "dimension1": {
                        "type": "string",
                        "description": "A  dimension name in the first dataset, along which the pixel array is defined. When the input has two nonspatial dimensions, a dimension must be specified. The length of the dimension used in the cal...",
                        "default": None
                },
                "variable1": {
                        "type": "string",
                        "description": "A variable name from the first input raster.",
                        "default": None
                },
                "dimension2": {
                        "type": "string",
                        "description": "A dimension name in the second dataset. The length of the dimension used in the calculation must be greater than 2.",
                        "default": None
                },
                "variable2": {
                        "type": "string",
                        "description": "A variable name from the second input raster.",
                        "default": None
                },
                "corr_method": {
                        "type": "string",
                        "description": "Specifies the correlation calculation method that will be used.PEARSON\u2014The correlation method will be Pearson. This is the default.SPEARMAN\u2014The correlation method will be Spearman.KENDALL\u2014The correlat...",
                        "default": None
                },
                "lag": {
                        "type": "string",
                        "description": "Calculate a correlation value by shifting the pixel array by the step specified, from 0 to dimension/2, depending on the time lag.  The default is 0.",
                        "default": None
                },
                "calculate_xcorr": {
                        "type": "string",
                        "description": "Specifies whether the cross correlation will be computed at lags.When ALL_CROSS_CORRELATION is specified, the correlations will be calculated at each lag within a range defined by the lag value. For e...",
                        "default": None
                },
                "calculate_pvalue": {
                        "type": "string",
                        "description": "Specifies whether the p-value will be computed at lags. P-value is a confidence value that describes how well the two variables are correlated.CALCULATE_P_VALUE\u2014 The p-value will be computed at lags. ...",
                        "default": None
                },
                "out_max_corr_raster": {
                        "type": "string",
                        "description": "A 2-band raster with maximum correlation values and the lags at which the maximum correlations occur. The raster will be created when the calculate_xcorr parameter is specified as ALL_CROSS_CORRELATIO...",
                        "default": None
                }
        },
        "required": [
                "in_mdim_raster1",
                "in_mdim_raster2"
        ]
},
    "predict_using_trend_raster": {
        "name": "predict_using_trend_raster",
        "description": "Computes a forecasted multidimensional raster using the output trend raster from the Generate Trend Raster tool.",
        "parameters": {
                "in_multidimensional_raster": {
                        "type": "string",
                        "description": "The input multidimensional trend raster from the Generate Trend Raster tool."
                },
                "variables": {
                        "type": "string",
                        "description": "The variable or variables that will be predicted in the analysis. If no variables are specified, all variables will be used.",
                        "default": None
                },
                "dimension_def": {
                        "type": "string",
                        "description": "Specifies the method used to provide prediction dimension values.BY_VALUE\u2014The prediction will be calculated for a single dimension value or a list of dimension values defined by the Values parameter (...",
                        "default": None
                },
                "dimension_values": {
                        "type": "string",
                        "description": "The dimension value or values to be used in the prediction. The format of the time, depth, and height values must match the format of the dimension values used to generate the trend raster. If the tre...",
                        "default": None
                },
                "start": {
                        "type": "string",
                        "description": "The start date, height, or depth of the dimension interval to be used in the prediction.",
                        "default": None
                },
                "end": {
                        "type": "string",
                        "description": "The end date, height, or depth of the dimension interval to be used in the prediction.",
                        "default": None
                },
                "interval_value": {
                        "type": "string",
                        "description": "The number of steps between two dimension values to be included in the prediction. \r\nThe default value is 1.For example, to predict temperature values every five years, use a value of 5.",
                        "default": None
                },
                "interval_unit": {
                        "type": "string",
                        "description": "Specifies the unit that will be used for the interval value. This parameter only applies when the dimension of analysis is a time dimension.\r\n\r\nHOURS\u2014The prediction will be calculated for each hour in...",
                        "default": None
                }
        },
        "required": [
                "in_multidimensional_raster"
        ]
},
    "summarize_categorical_raster": {
        "name": "summarize_categorical_raster",
        "description": "Generates a table containing the pixel count for each class, in each slice of an input categorical raster.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input multidimensional raster of integer type."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output summary table. Geodatabase, database, text, Microsoft Excel, and comma-separated value (CSV) tables are supported."
                },
                "dimension": {
                        "type": "string",
                        "description": "The input dimension to use for the summary. \r\nIf there is more than one dimension and no value is specified, all slices will be summarized using all combinations of dimension values.",
                        "default": None
                },
                "aoi": {
                        "type": "string",
                        "description": "The polygon feature layer containing the area or areas of interest to use when calculating the pixel count per category. If no area of interest is specified, the entire raster dataset will be included...",
                        "default": None
                },
                "aoi_id_field": {
                        "type": "string",
                        "description": "The field in the polygon feature layer that defines each area of interest. Text and integer fields are supported.",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_table"
        ]
},
    "weighted_sum": {
        "name": "weighted_sum",
        "description": "Overlays several rasters, multiplying each by their given weight and summing them together. Learn more about how Weighted Sum works",
        "parameters": {
                "in_rasters": {
                        "type": "string",
                        "description": "TheWeighted Sum tool overlays several rasters, multiplying each by their given weight and summing them together.An Overlay class is used to define the table. The WSTable object is used to specify a Py..."
                }
        },
        "required": [
                "in_rasters"
        ]
},
    "classify_raster_using_spectra": {
        "name": "classify_raster_using_spectra",
        "description": "Classifies a multiband raster dataset using spectral matching techniques. The input spectral data can be provided as a point feature class or a .json file.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input multiband raster."
                },
                "in_spectra_file": {
                        "type": "string",
                        "description": "The  spectral information for different pixel classes.\r\nThe spectral information can be provided as point features, a training sample point feature class generated from the Training Samples Manager pa..."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the spectral matching method that will be used.SAM\u2014The  vector angle between the input multiband raster and the reference spectra will be calculated in which the spectra of each pixel is tre..."
                },
                "thresholds": {
                        "type": "string",
                        "description": "The threshold for spectral matching. Pixel values that exceed this value will be classified as undefined. This can be a single value applied to all spectral classes or a space-delimited list of values...",
                        "default": None
                },
                "out_score_raster": {
                        "type": "string",
                        "description": "A multiband raster that stores the matching results for each end member. The band order follows the order of the classes in the in_spectra_file parameter value. If the input is a multidimensional rast...",
                        "default": None
                },
                "out_classifier_definition": {
                        "type": "string",
                        "description": "The output .ecd file.",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_spectra_file",
                "method"
        ]
},
    "detect_image_anomalies": {
        "name": "detect_image_anomalies",
        "description": "Processes a multiband or hyperspectral image and creates an anomaly score raster. An anomaly score raster is a single band raster, with values between 0 and 1.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "A multiband or hyperspectral image."
                },
                "out_raster": {
                        "type": "string",
                        "description": "A single band raster that stores the anomaly scores between 0-1 as a floating point number.  Zero (0) is the background value, and large values approaching 1 are potential anomaly pixels. Use the file..."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the anomaly calculation method that will be used. \r\nRXD\u2014The RXD method will be used to extract pixels that are significantly different from the background pixel values. This is the default.U...",
                        "default": None
                },
                "num_cluster": {
                        "type": "string",
                        "description": "The number of clusters that will be used when the method parameter is set to KMEANS.",
                        "default": None
                },
                "background_region": {
                        "type": "string",
                        "description": "A polygon feature class that will define the region to be used to calculate background statistics when the method parameter is set to RXD or UTD.",
                        "default": None
                },
                "recompute_stats": {
                        "type": "string",
                        "description": "Specifies whether statistics will be recomputed for the output score raster when the method parameter is set to RXD or UTD.  The RXD and UTD options require accurate statistics in which the skip facto...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_raster"
        ]
},
    "linear_spectral_unmixing": {
        "name": "linear_spectral_unmixing",
        "description": "Performs subpixel classification and calculates the fractional abundance of different land-cover types for individual pixels.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The \r\ninput raster dataset."
                },
                "in_spectral_profile_file": {
                        "type": "string",
                        "description": "The  spectral information for the different land-cover classes.This can be provided as polygon features, a classifier definition file (.ecd) generated from the Train Maximum Likelihood Classifier tool..."
                },
                "value_option": {
                        "type": "string",
                        "description": "Specifies how the output pixel values will be defined.SUM_TO_ONE\u2014Class values for each pixel will be provided in decimal format with the sum of all classes equal to 1. For example, Class1 = 0.16; Clas...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "in_spectral_profile_file"
        ]
},
    "cell_statistics": {
        "name": "cell_statistics",
        "description": "Calculates a per-cell statistic from multiple rasters. The available statistics are Majority, Maximum, Mean, Median, Minimum, Minority, Percentile, Range, Standard deviation, Sum, and Variety. Learn more about how Cell Statistics works",
        "parameters": {
                "in_rasters_or_constantsin_raster_or_constant": {
                        "type": "string",
                        "description": "A list of input rasters for which a statistical operation will be calculated for each cell in the analysis window.A number can be used as an input; however, the cell size and extent must first be set ..."
                },
                "statistics_type": {
                        "type": "string",
                        "description": "Specifies the statistic type to be calculated.MEAN\u2014The mean (average) of the inputs will be calculated. This is the default.MAJORITY\u2014The majority (value that occurs most often) of the inputs will be d...",
                        "default": None
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Specifies whether NoData values will be ignored by the statistic calculation.DATA\u2014At the processing cell location, if any of the input rasters has NoData, that NoData value will be ignored. The statis...",
                        "default": None
                },
                "process_as_multiband": {
                        "type": "string",
                        "description": "Specifies how the input multiband raster bands will be processed.\r\nSINGLE_BAND\u2014Each band from a multiband raster input will be processed separately as a single band raster. This is the default.MULTI_B...",
                        "default": None
                },
                "percentile_value": {
                        "type": "string",
                        "description": "The percentile value that will be calculated. The default is 90, indicating the 90th percentile.The value can range from 0 to 100. The 0th percentile is essentially equivalent to the minimum statistic...",
                        "default": None
                },
                "percentile_interpolation_type": {
                        "type": "string",
                        "description": "Specifies the method of interpolation that will be used when the specified percentile value is between two input cell values.AUTO_DETECT\u2014If the input rasters are of integer pixel type, the NEAREST met...",
                        "default": None
                }
        },
        "required": [
                "in_rasters_or_constantsin_raster_or_constant"
        ]
},
    "focal_statistics": {
        "name": "focal_statistics",
        "description": "Calculates for each input cell location a statistic of the values within a specified neighborhood around it. Learn more about how Focal Statistics works",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The raster for which the focal statistics for each input cell will be calculated."
                },
                "neighborhood": {
                        "type": "string",
                        "description": "The cells surrounding a processing cell that will be used in the statistic calculation. There are several predefined neighborhood types to choose from, or a custom kernel can be defined.Once the neigh...",
                        "default": None
                },
                "statistics_type": {
                        "type": "string",
                        "description": "Specifies the statistic type to be calculated.MEAN\u2014The mean (average value) of the cells in the neighborhood will be calculated.MAJORITY\u2014The majority (value that occurs most often) of the cells in the...",
                        "default": None
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Specifies whether NoData values will be ignored by the statistic calculation.DATA\u2014If a NoData value exists within a neighborhood, the NoData value will be ignored. Only cells within the neighborhood t...",
                        "default": None
                },
                "percentile_value": {
                        "type": "string",
                        "description": "The percentile value that will be calculated. The default is 90, for the 90th percentile.The value can range from 0 to 100. The 0th percentile is essentially equivalent to the minimum statistic, and t...",
                        "default": None
                }
        },
        "required": [
                "in_raster"
        ]
},
    "zonal_statistics": {
        "name": "zonal_statistics",
        "description": "Summarizes the values of a raster within the zones of another dataset. Learn more about how the zonal statistics tools work",
        "parameters": {
                "in_zone_data": {
                        "type": "string",
                        "description": "The dataset that defines the zones.The zones can be defined by an integer raster or a feature layer."
                },
                "zone_field": {
                        "type": "string",
                        "description": "The field that contains the values that define each zone.It can be an integer or a string field of the zone dataset."
                },
                "in_value_raster": {
                        "type": "string",
                        "description": "The raster that contains the values for which a statistic will be calculated."
                },
                "statistics_type": {
                        "type": "string",
                        "description": "Specifies the statistic type to be calculated.MEAN\u2014The average of all cells in the value raster that belong to the same zone as the output cell will be calculated.This is the default.MAJORITY\u2014The valu...",
                        "default": None
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Specifies whether NoData values in the value input will be ignored in the results of the zone that they fall within.DATA\u2014Within any particular zone, only cells that have a value in the input value ras...",
                        "default": None
                },
                "process_as_multidimensional": {
                        "type": "string",
                        "description": "Specifies how the input rasters will be calculated if they are multidimensional.CURRENT_SLICE\u2014Statistics will be calculated from the current slice of the input multidimensional dataset. This is the de...",
                        "default": None
                },
                "percentile_value": {
                        "type": "string",
                        "description": "The percentile that will be calculated. The default is 90, indicating the 90th percentile.The values can range from 0 to 100. The 0th percentile is essentially equivalent to the minimum statistic, and...",
                        "default": None
                },
                "percentile_interpolation_type": {
                        "type": "string",
                        "description": "Specifies the method of interpolation that will be used when the percentile value falls between two cell values from the input value raster.AUTO_DETECT\u2014If the input value raster is of integer pixel ty...",
                        "default": None
                },
                "circular_calculation": {
                        "type": "string",
                        "description": "Specifies how the input raster will be processed for circular data.ARITHMETIC\u2014Ordinary linear statistics will be calculated. This is the default. CIRCULAR\u2014The statistics for angles or other cyclic qua...",
                        "default": None
                },
                "circular_wrap_value": {
                        "type": "string",
                        "description": "The value that will be used to round a linear value to the range of a given circular statistic. Its value must be a positive integer or a floating-point value. The default value is 360 degrees.This pa...",
                        "default": None
                }
        },
        "required": [
                "in_zone_data",
                "zone_field",
                "in_value_raster"
        ]
},
    "zonal_statistics_as_table": {
        "name": "zonal_statistics_as_table",
        "description": "Summarizes the values of a raster within the zones of another dataset and reports the results as a table. Learn more about how the zonal statistics tools work",
        "parameters": {
                "in_zone_data": {
                        "type": "string",
                        "description": "The dataset that defines the zones.The zones can be defined by an integer raster or a feature layer."
                },
                "zone_field": {
                        "type": "string",
                        "description": "The field that contains the values that define each zone.It can be an integer or a string field of the zone dataset."
                },
                "in_value_raster": {
                        "type": "string",
                        "description": "The raster that contains the values for which a statistic will be calculated."
                },
                "out_table": {
                        "type": "string",
                        "description": "The output table that will contain the summary of the values in each zone.The format of the table is determined by the output location and path. By default, the output will be a geodatabase table if i..."
                },
                "ignore_nodata": {
                        "type": "string",
                        "description": "Specifies whether NoData values in the value input will be ignored in the results of the zone that they fall within.DATA\u2014Within any particular zone, only cells that have a value in the input value ras...",
                        "default": None
                },
                "statistics_type": {
                        "type": "string",
                        "description": "Specifies the statistic type to be calculated.ALL\u2014All of the statistics will be calculated. This is the default.MEAN\u2014The average of all cells in the value raster that belong to the same zone as the ou...",
                        "default": None
                },
                "process_as_multidimensional": {
                        "type": "string",
                        "description": "Specifies how the input rasters will be calculated if they are multidimensional.\r\nCURRENT_SLICE\u2014Statistics will be calculated from the current slice of the input multidimensional dataset. This is the ...",
                        "default": None
                },
                "percentile_values": {
                        "type": "string",
                        "description": "The percentile that will be calculated. The default is 90, indicating the 90th percentile.The values can range from 0 to 100. The 0th percentile is essentially equivalent to the minimum statistic, and...",
                        "default": None
                },
                "percentile_interpolation_type": {
                        "type": "string",
                        "description": "Specifies the method of interpolation that will be used when the percentile value falls between two cell values from the input value raster.AUTO_DETECT\u2014If the input value raster is of integer pixel ty...",
                        "default": None
                },
                "circular_calculation": {
                        "type": "string",
                        "description": "Specifies how the input raster will be processed for circular data.ARITHMETIC\u2014Ordinary linear statistics will be calculated. This is the default. CIRCULAR\u2014The statistics for angles or other cyclic qua...",
                        "default": None
                },
                "circular_wrap_value": {
                        "type": "string",
                        "description": "The value that will be used to round a linear value to the range of a given circular statistic. Its value must be a positive integer or a floating-point value. The default value is 360 degrees.This pa...",
                        "default": None
                },
                "out_join_layer": {
                        "type": "string",
                        "description": "The output layer that will be created by joining the output table to the input zone data.",
                        "default": None
                }
        },
        "required": [
                "in_zone_data",
                "zone_field",
                "in_value_raster",
                "out_table"
        ]
},
    "create_color_composite": {
        "name": "create_color_composite",
        "description": "Creates a three-band raster dataset from a multiband raster dataset.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input multiband raster data."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output three-band composite raster."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the\r\nmethod that will be used to extract bands.BAND_NAMES\u2014The band name representing the wavelength\r\ninterval on the electromagnetic spectrum (such as Red, Near Infrared,\r\nor Thermal Infrare..."
                },
                "red_expression": {
                        "type": "string",
                        "description": "The calculation \r\nthat will be assigned to the first band.A band name, band ID, or an algebraic expression using the bands.The supported operators are unary: plus (+), minus (-), times (*), and divide..."
                },
                "green_expression": {
                        "type": "string",
                        "description": "The calculation \r\nthat will be assigned to the second band.A band name, band ID, or an algebraic expression using the bands.The supported operators are unary: plus (+), minus (-), times (*), and divid..."
                },
                "blue_expression": {
                        "type": "string",
                        "description": "The calculation \r\nthat will be assigned to the third band.\r\nA band name, band ID, or an algebraic expression using the bands.The supported operators are unary: plus (+), minus (-), times (*), and divi..."
                }
        },
        "required": [
                "in_raster",
                "out_raster",
                "method",
                "red_expression",
                "green_expression",
                "blue_expression"
        ]
},
    "apply_coregistration": {
        "name": "apply_coregistration",
        "description": "Resamples  the secondary single look complex (SLC) data to the reference SLC grid using a digital elevation model (DEM) and orbit state vector metadata. For Terrain Observation by Progressive Scan (TOPS) mode radar data, the tool also deramps and demodulates the secondary SLC before resampling. Once resampling is performed, the secondary radar data is reramped and remodulated.",
        "parameters": {
                "in_reference_radar_data": {
                        "type": "string",
                        "description": "The input reference complex radar data."
                },
                "in_secondary_radar_data": {
                        "type": "string",
                        "description": "The input secondary complex radar data."
                },
                "out_secondary_radar_data": {
                        "type": "string",
                        "description": "The output secondary radar data coregistered to the reference radar data."
                },
                "in_dem_raster": {
                        "type": "string",
                        "description": "The DEM raster that will be used to estimate the local illuminated area."
                },
                "geoid": {
                        "type": "string",
                        "description": "Specifies whether the vertical reference system of the input DEM will be transformed to ellipsoidal height. Most elevation datasets are referenced to sea level orthometric height, so a correction is r...",
                        "default": None
                },
                "polarization_bands": {
                        "type": "string",
                        "description": "The polarization bands that will be corrected.  The first band is  selected by default.",
                        "default": None
                }
        },
        "required": [
                "in_reference_radar_data",
                "in_secondary_radar_data",
                "out_secondary_radar_data",
                "in_dem_raster"
        ]
},
    "apply_geometric_terrain_correction": {
        "name": "apply_geometric_terrain_correction",
        "description": "Orthorectifies the input synthetic aperture radar (SAR) data using a range-Doppler backgeocoding algorithm. The range-Doppler backgeocoding approach computes the radar range and azimuth indices for every digital elevation model (DEM) grid point using the orbit state vectors.  If no DEM is provided, the tool uses the tie points included in the metadata to perform the range-Doppler terrain correction.",
        "parameters": {
                "in_radar_data": {
                        "type": "string",
                        "description": "The input radar data."
                },
                "out_radar_data": {
                        "type": "string",
                        "description": "The corrected geometric terrain radar data."
                },
                "polarization_bands": {
                        "type": "string",
                        "description": "The polarization bands that will be corrected.  The first band is  selected by default.",
                        "default": None
                },
                "in_dem_raster": {
                        "type": "string",
                        "description": "The input DEM.If no DEM is specified or in areas that are not covered by a specified DEM, an approximated DEM, interpolated from metadata tie points, will be created. Use the tie-point approach for fu...",
                        "default": None
                },
                "geoid": {
                        "type": "string",
                        "description": "Specifies whether the vertical reference system of the input DEM will be transformed to ellipsoidal height. Most elevation datasets are referenced to sea level orthometric height, so a correction is r...",
                        "default": None
                }
        },
        "required": [
                "in_radar_data",
                "out_radar_data"
        ]
},
    "apply_orbit_correction": {
        "name": "apply_orbit_correction",
        "description": "Updates the orbital information in the Sentinel-1 synthetic aperture radar (SAR) data using a more accurate orbit state vector (OSV) file. Orbit files can be downloaded from external sources using the Download Orbit File  tool.",
        "parameters": {
                "in_radar_data": {
                        "type": "string",
                        "description": "The input radar data."
                },
                "in_orbit_file": {
                        "type": "string",
                        "description": "The input orbit file."
                },
                "folder": {
                        "type": "string",
                        "description": "The alternate folder location that will be searched for the downloaded orbit state vector files. The default folder is the input radar data .SAFE folder.",
                        "default": None
                }
        },
        "required": [
                "in_radar_data",
                "in_orbit_file"
        ]
},
    "apply_radiometric_calibration": {
        "name": "apply_radiometric_calibration",
        "description": "Converts the input synthetic aperture radar (SAR) reflectivity into physical units of normalized backscatter by normalizing the reflectivity using a reference plane. Calibrating SAR data is necessary to obtain meaningful backscatter that can be related to the physical properties of features in the image.",
        "parameters": {
                "in_radar_data": {
                        "type": "string",
                        "description": "The input radar data."
                },
                "out_radar_data": {
                        "type": "string",
                        "description": "The calibrated radar data."
                },
                "polarization_bands": {
                        "type": "string",
                        "description": "The polarization bands that will be corrected.  The first band is  selected by default.",
                        "default": None
                },
                "calibration_type": {
                        "type": "string",
                        "description": "Specifies the type of calibration that will be applied.BETA_NOUGHT\u2014The radar reflectivity will be calibrated to backscatter for a unit area on the slant range. This is the default.SIGMA_NOUGHT\u2014 The ba...",
                        "default": None
                }
        },
        "required": [
                "in_radar_data",
                "out_radar_data"
        ]
},
    "apply_radiometric_terrain_flattening": {
        "name": "apply_radiometric_terrain_flattening",
        "description": "Corrects the input synthetic aperture radar (SAR) data for radiometric distortions due to topography. Due to the side-looking nature of SAR sensors,\r\nfeatures facing the sensor appear artificially brighter and\r\nfeatures facing away from the sensor appear artificially\r\ndarker. Radiometric terrain flattening normalizes the backscatter\r\nvalues so that value variations will be due to surface scattering\r\nproperties. Radiometric terrain flattening is necessary to\r\nobtain meaningful backscatter that can be\r\nrelated directly to the surface scattering properties of features\r\nin a SAR image over any terrain.",
        "parameters": {
                "in_radar_data": {
                        "type": "string",
                        "description": "The input radar data.The data that will have radiometric terrain flattening applied. The data must be radiometrically calibrated to beta nought."
                },
                "out_radar_data": {
                        "type": "string",
                        "description": "The radiometrically terrain-flattened radar data."
                },
                "in_dem_raster": {
                        "type": "string",
                        "description": "The input DEM.The DEM that will be used  to estimate the local illuminated area and the local incidence angle."
                },
                "geoid": {
                        "type": "string",
                        "description": "Specifies whether the vertical reference system of the input DEM will be transformed to ellipsoidal height. Most elevation datasets are referenced to sea level orthometric height, so a correction is r...",
                        "default": None
                },
                "polarization_bands": {
                        "type": "string",
                        "description": "The polarization bands that will be radiometrically terrain flattened. The first band is  selected by default.",
                        "default": None
                },
                "calibration_type": {
                        "type": "string",
                        "description": "Specifies whether the output will be terrain flattened using sigma nought or gamma nought.GAMMA_NOUGHT\u2014  The beta nought backscatter will be corrected using an accurate computation of an area using a ...",
                        "default": None
                },
                "out_scattering_area": {
                        "type": "string",
                        "description": "The scattering area radar\r\ndataset.",
                        "default": None
                },
                "out_geometric_distortion": {
                        "type": "string",
                        "description": "The 4-band geometric distortion radar dataset. The first band is the terrain slope, the second band is look angle, the third band is the foreshortening ratio, and the fourth band is the local incidenc...",
                        "default": None
                },
                "out_geometric_distortion_mask": {
                        "type": "string",
                        "description": "The 1-band geometric distortion mask radar dataset. The pixels are classified using six unique values, one for each distortion type:Undetermined \u2014Value of 0Foreshortening \u2014Value of 1Lengthening \u2014Value...",
                        "default": None
                }
        },
        "required": [
                "in_radar_data",
                "out_radar_data",
                "in_dem_raster"
        ]
},
    "compute_coherence": {
        "name": "compute_coherence",
        "description": "Computes the similarity between the reference and secondary input complex radar data. The output is a coherence raster with a value range of 0 to 1 in which 0 indicates no coherence and 1 indicates perfect coherence. A value of 0.3 or above is considered a good coherence value.",
        "parameters": {
                "in_reference_radar_data": {
                        "type": "string",
                        "description": "The input reference complex radar data."
                },
                "in_secondary_radar_data": {
                        "type": "string",
                        "description": "The input secondary complex radar data."
                },
                "out_radar_data": {
                        "type": "string",
                        "description": "The output coherence radar data."
                },
                "polarization_bands": {
                        "type": "string",
                        "description": "The polarization bands that will be corrected.  The first band is  selected by default.",
                        "default": None
                },
                "range_window_size": {
                        "type": "string",
                        "description": "The range window size in pixels. The default value is 10.",
                        "default": None
                },
                "azimuth_window_size": {
                        "type": "string",
                        "description": "The azimuth window size in pixels. The default value is the minimum number of pixels required to create an approximate square window. For example, if the range_window_size parameter value is 10, the d...",
                        "default": None
                }
        },
        "required": [
                "in_reference_radar_data",
                "in_secondary_radar_data",
                "out_radar_data"
        ]
},
    "convert_sar_units": {
        "name": "convert_sar_units",
        "description": "Converts the scaling of the input synthetic aperture radar (SAR) data. Conversions can be performed  between amplitude and intensity, between linear and decibels (dB), and between complex and intensity.",
        "parameters": {
                "in_radar_data": {
                        "type": "string",
                        "description": "The input radar data."
                },
                "out_radar_data": {
                        "type": "string",
                        "description": "The converted radar dataset."
                },
                "conversion_type": {
                        "type": "string",
                        "description": "Specifies the type of backscatter conversion that will\r\nbe applied.LINEAR_TO_DB\u2014The unitless values will be converted to dB values. This is the default.DB_TO_LINEAR\u2014The dB values will be converted to ...",
                        "default": None
                }
        },
        "required": [
                "in_radar_data",
                "out_radar_data"
        ]
},
    "deburst": {
        "name": "deburst",
        "description": "Merges the multiple bursts from the input Sentinel-1 Single Look Complex (SLC) synthetic aperture radar (SAR) data and outputs a single, seamless subswath raster.",
        "parameters": {
                "in_radar_data": {
                        "type": "string",
                        "description": "The input radar data."
                },
                "out_radar_data": {
                        "type": "string",
                        "description": "The debursted radar data."
                },
                "polarization_bands": {
                        "type": "string",
                        "description": "The polarization bands that will be corrected.  The first band is  selected by default.",
                        "default": None
                }
        },
        "required": [
                "in_radar_data",
                "out_radar_data"
        ]
},
    "despeckle": {
        "name": "despeckle",
        "description": "Corrects the input synthetic aperture radar (SAR) data for speckle,  which is a result of coherent illumination that resembles a grainy or salt and pepper effect. This tool filters out noise while retaining edges and sharp features in the SAR image. The available filters are Lee, Enhanced Lee, Refined Lee, Frost, Kuan, and Gamma MAP.",
        "parameters": {
                "in_radar_data": {
                        "type": "string",
                        "description": "The input radar data."
                },
                "out_radar_data": {
                        "type": "string",
                        "description": "The despeckled radar data."
                },
                "polarization_bands": {
                        "type": "string",
                        "description": "The polarization bands that will be filtered. The first band is  selected by default.",
                        "default": None
                },
                "filter_type": {
                        "type": "string",
                        "description": "Specifies the type of smoothing algorithm or filter that will be applied.LEE\u2014A spatial filter will be applied to each pixel in an image to reduce the speckle noise. This option filters the data based ...",
                        "default": None
                },
                "filter_size": {
                        "type": "string",
                        "description": "Specifies the size of the pixel window\r\nthat will be used to filter noise.3x3\u2014A 3-by-3 filter  size will be used. This is the default.5x5\u2014A 5-by-5 filter  size will be used.7x7\u2014A 7-by-7 filter  size w...",
                        "default": None
                },
                "noise_model": {
                        "type": "string",
                        "description": "This parameter is only valid when the filter_type parameter is set to LEE.",
                        "default": None
                },
                "noise_variance": {
                        "type": "string",
                        "description": "The noise variance of the radar image. The default is 0.25.\r\nThis parameter is only valid when the filter_type parameter is set to LEE and the noise_model parameter is set to ADDITIVE_NOISE or ADDITIV...",
                        "default": None
                },
                "add_noise_mean": {
                        "type": "string",
                        "description": "The mean value of additive noise. A larger noise mean value will produce less smoothing, while a smaller value results in more smoothing.\r\nThe default value is 0.This parameter is only valid when the ...",
                        "default": None
                },
                "mult_noise_mean": {
                        "type": "string",
                        "description": "The mean value of multiplicative noise. A larger noise mean value will produce less smoothing, while a smaller value results in more smoothing.\r\nThe default value is 1.This parameter is only valid whe...",
                        "default": None
                },
                "number_of_looks": {
                        "type": "string",
                        "description": "The number of looks value of the image, which controls image smoothing and estimates noise variance. A smaller value results in more smoothing, while a larger value retains more image features. The de...",
                        "default": None
                },
                "damp_factor": {
                        "type": "string",
                        "description": "The exponential damping level of smoothing that will be applied. A damping value greater than 1 will result in better edge preservation but less smoothing. Values less than 1 will result in more smoot...",
                        "default": None
                }
        },
        "required": [
                "in_radar_data",
                "out_radar_data"
        ]
},
    "download_orbit_file": {
        "name": "download_orbit_file",
        "description": "Downloads the updated orbit  files for Sentinel-1 synthetic aperture radar (SAR) data. This tool uses the orbit type to make a call to the orbit website. Using the SAR metadata, it identifies the appropriate orbit state vector (OSV) file and downloads it to the input SAR data directory. Three types of OSVs are available for a Sentinel-1 product: predicted, restituted, and precise. Predicted OSVs are provided with the Sentinel-1 Level 1 ground range detected (GRD)\r\nand single look complex (SLC)\r\n auxiliary products. Restituted OSVs are available through the European Space Agency (ESA) within 3 hours of image acquisition. Precise OSVs are available through ESA within 3 weeks of image acquisition. Sentinel-1 OSV files are downloaded from the Copernicus Data Space Ecosystem.",
        "parameters": {
                "in_radar_data": {
                        "type": "string",
                        "description": "The input radar data."
                },
                "orbit_type": {
                        "type": "string",
                        "description": "Specifies the OSV type that will be downloaded. SENTINEL_RESTITUTED\u2014Approximate OSV data will be downloaded. This is available several hours\r\nafter data acquisition.SENTINEL_PRECISE\u2014Refined OSV\r\ndata ...",
                        "default": None
                },
                "username": {
                        "type": "string",
                        "description": "The Copernicus Data Space Ecosystem login credential username.  This parameter is only valid when the input data has Sentinel restituted or Sentinel precise orbit types.",
                        "default": None
                },
                "password": {
                        "type": "string",
                        "description": "The Copernicus Data Space Ecosystem login credential password.This parameter is only valid when the input data has Sentinel restituted or Sentinel precise orbit types.",
                        "default": None
                },
                "cloud_storage": {
                        "type": "string",
                        "description": "The Copernicus Data Space Ecosystem cloud storage connection file.",
                        "default": None
                },
                "folder": {
                        "type": "string",
                        "description": "An alternate folder location where the downloaded orbit state vector file will be stored.\r\nThe default folder is the input radar data .SAFE folder.",
                        "default": None
                }
        },
        "required": [
                "in_radar_data"
        ]
},
    "generate_radiometric_terrain_corrected_data": {
        "name": "generate_radiometric_terrain_corrected_data",
        "description": "Transforms Level 1 synthetic aperture radar (SAR) data to a radiometric terrain-corrected (RTC) dataset. Use the RTC data for analysis and visualization. This tool creates a SAR output that removes unwanted noise and distortions by applying the appropriate RTC workflow according to the input SAR sensor, mode, and product type.",
        "parameters": {
                "in_radar_data": {
                        "type": "string",
                        "description": "The input radar data.This data needs to be Level 1 radar data."
                },
                "out_radar_data": {
                        "type": "string",
                        "description": "The radiometric terrain-corrected radar dataset."
                },
                "in_dem_raster": {
                        "type": "string",
                        "description": "The input DEM.The DEM that will be used  to estimate the local illuminated area and the local incidence angle."
                },
                "geoid": {
                        "type": "string",
                        "description": "Specifies whether the vertical reference system of the input DEM will be transformed to ellipsoidal height. Most elevation datasets are referenced to sea level orthometric height, so a correction is r...",
                        "default": None
                },
                "polarization_bands": {
                        "type": "string",
                        "description": "The polarization bands that will be filtered. The first band is  selected by default.",
                        "default": None
                },
                "output_units": {
                        "type": "string",
                        "description": "Specifies the units that will be used for the RTC outputs.LINEAR\u2014The units of the output will be  in linear backscatter. This is the default.DECIBEL\u2014The units of the output will be  in decibels.",
                        "default": None
                },
                "processing_level": {
                        "type": "string",
                        "description": "Specifies the radar products that will be retained. The available processing levels depend on the input radar data and its corresponding processing workflow.By default, no option will be used, and no ...",
                        "default": None
                },
                "out_folder": {
                        "type": "string",
                        "description": "The output folder where the output radar products will be retained.",
                        "default": None
                }
        },
        "required": [
                "in_radar_data",
                "out_radar_data",
                "in_dem_raster"
        ]
},
    "multilook": {
        "name": "multilook",
        "description": "Averages the input synthetic aperture radar (SAR) data  by looks in range and azimuth to approximate square pixels, mitigates speckle, and reduces SAR tool processing time.",
        "parameters": {
                "in_radar_data": {
                        "type": "string",
                        "description": "The input radar data."
                },
                "out_radar_data": {
                        "type": "string",
                        "description": "The output multilook radar data."
                },
                "polarization_bands": {
                        "type": "string",
                        "description": "The polarization bands that will be corrected.  The first band is  selected by default.",
                        "default": None
                },
                "range_looks": {
                        "type": "string",
                        "description": "The integer number of looks in the range direction. If no value is provided, the minimum number of looks required to create an approximate square pixel will be used.",
                        "default": None
                },
                "azimuth_looks": {
                        "type": "string",
                        "description": "The integer number of looks in the azimuth direction. If no value is provided, the minimum number of looks required to create an approximate square pixel will be used.",
                        "default": None
                }
        },
        "required": [
                "in_radar_data",
                "out_radar_data"
        ]
},
    "remove_thermal_noise": {
        "name": "remove_thermal_noise",
        "description": "Corrects backscatter disturbances caused by thermal noise in the input synthetic aperture radar (SAR) data, resulting in a more seamless image.",
        "parameters": {
                "in_radar_data": {
                        "type": "string",
                        "description": "The input radar data."
                },
                "out_radar_data": {
                        "type": "string",
                        "description": "The thermal noise-corrected radar data."
                },
                "polarization_bands": {
                        "type": "string",
                        "description": "The polarization bands that will be corrected.  The first band is  selected by default.",
                        "default": None
                }
        },
        "required": [
                "in_radar_data",
                "out_radar_data"
        ]
},
    "compute_sar_indices": {
        "name": "compute_sar_indices",
        "description": "Computes various SAR indices for synthetic aperture radar (SAR) data, such as \r\nRadar Vegetation Index (RVI), Radar Forest Degradation Index (RFDI), and Canopy Structure Index (CSI). The formulas used for these indices depend on the polarizations available in the input radar dataset.",
        "parameters": {
                "in_radar_data": {
                        "type": "string",
                        "description": "The input radar data."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output SAR index raster."
                },
                "index": {
                        "type": "string",
                        "description": "Specifies the SAR index that will be computed.RVI\u2014The Radar Vegetation Index will be used. RVI is the ratio of cross-polarized backscatter to the total backscatter from all polarizations. The values r...",
                        "default": None
                },
                "polarization_bands": {
                        "type": "string",
                        "description": "Specifies the polarization bands that will be used in the index computation.This parameter is only supported when the in_radar_data parameter value is a quad-polarized SAR dataset and the index parame...",
                        "default": None
                }
        },
        "required": [
                "in_radar_data",
                "out_raster"
        ]
},
    "detect_bright_ocean_objects": {
        "name": "detect_bright_ocean_objects",
        "description": "Detects potential bright human-made objects\u2014such as ships, oil rigs, and windmills\u2014while masking out the synthetic aperture radar (SAR) data outside the region of interest. The tool clusters pixels and filters the clusters by the minimum and maximum width and length parameters, and outputs the results to a feature class. The output feature class can be specified as  a bounding box or a perimeter around the polygon for the detected objects.",
        "parameters": {
                "in_radar_data": {
                        "type": "string",
                        "description": "The input radar data."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class of detected bright ocean objects."
                },
                "out_type": {
                        "type": "string",
                        "description": "Specifies the type of boundary that will be used for the output feature class.BOUNDS\u2014 The minimum bounding box of the detected object will be used. This is the default.PERIMETER\u2014 An outline of the per...",
                        "default": None
                },
                "min_object_width": {
                        "type": "string",
                        "description": "The minimum width of an object to be detected. The width must be a positive value. The default value is 10 meters.",
                        "default": None
                },
                "max_object_width": {
                        "type": "string",
                        "description": "The maximum width of an object to be detected. The width must be a positive value. The default value is 100 meters.",
                        "default": None
                },
                "min_object_length": {
                        "type": "string",
                        "description": "The minimum length of an object to be detected. The length must be a positive value. The default value is 50 meters.",
                        "default": None
                },
                "max_object_length": {
                        "type": "string",
                        "description": "The maximum length of an object to be detected. The length must be a positive value. The default value is 500 meters.",
                        "default": None
                },
                "mask_features": {
                        "type": "string",
                        "description": "A land or water polygon feature. This polygon will be used to create a mask.",
                        "default": None
                },
                "feature_type": {
                        "type": "string",
                        "description": "Specifies the type of polygon the mask_features parameter value represents. This parameter is required if the mask_features  parameter is specified.LAND\u2014The mask input is a land polygon. An inverted m...",
                        "default": None
                },
                "in_dem_raster": {
                        "type": "string",
                        "description": "The input DEM.If the input radar data is not orthorectified, this DEM will be used to orthorectify it.If no value is provided for the mask_features parameter, this DEM will also be used to create a la...",
                        "default": None
                },
                "geoid": {
                        "type": "string",
                        "description": "Specifies whether the vertical reference system of the input DEM will be transformed to ellipsoidal height. Most elevation datasets are referenced to sea level orthometric height, so a correction is r...",
                        "default": None
                },
                "mask_tolerance": {
                        "type": "string",
                        "description": "The buffer distance surrounding the mask created from either the mask_features  parameter or the in_dem_raster parameter. The distance cannot be negative. The default value is 100 meters.",
                        "default": None
                }
        },
        "required": [
                "in_radar_data",
                "out_feature_class"
        ]
},
    "detect_dark_ocean_areas": {
        "name": "detect_dark_ocean_areas",
        "description": "Identifies potential dark pixels belonging to oil spills or algae, and clusters these pixels, while masking out the synthetic aperture radar (SAR) data outside the region of interest. The tool filters clusters using the Minimum Area parameter, and creates the result as a binary raster. A value of 1 corresponds to dark areas detected and is symbolized in a random color. A value of 0 indicates that no dark areas were detected and is symbolized with full transparency. Both orthorectified and nonorthorectified radar data are valid inputs. Nonorthorectified radar data results in improved azimuth artifact filtering, since the data is in radar coordinates.",
        "parameters": {
                "in_radar_data": {
                        "type": "string",
                        "description": "The input radar data."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output binary raster of the detected dark ocean areas. A value of 1 corresponds to a detected dark area."
                },
                "min_area": {
                        "type": "string",
                        "description": "The minimum area to be detected.The size cannot be negative. The default value is 10000 square meters.",
                        "default": None
                },
                "mask_features": {
                        "type": "string",
                        "description": "A land or water polygon feature. This polygon will be used to create a mask.",
                        "default": None
                },
                "feature_type": {
                        "type": "string",
                        "description": "Specifies the type of polygon the mask_features parameter value represents. This parameter is required if the mask_features  parameter is specified.LAND\u2014The mask input is a land polygon. An inverted m...",
                        "default": None
                },
                "in_dem_raster": {
                        "type": "string",
                        "description": "The input DEM.If the input radar data is not orthorectified, this DEM will be used to orthorectify it.If no value is provided for the mask_features parameter, this DEM will also be used to create a la...",
                        "default": None
                },
                "geoid": {
                        "type": "string",
                        "description": "Specifies whether the vertical reference system of the input DEM will be transformed to ellipsoidal height. Most elevation datasets are referenced to sea level orthometric height, so a correction is r...",
                        "default": None
                },
                "mask_tolerance": {
                        "type": "string",
                        "description": "The buffer distance surrounding the mask created from either the mask_features  parameter or the in_dem_raster parameter. The distance cannot be negative. The default value is 100 meters.",
                        "default": None
                }
        },
        "required": [
                "in_radar_data",
                "out_raster"
        ]
},
    "extract_water": {
        "name": "extract_water",
        "description": "Finds water bodies using input synthetic aperture radar (SAR) data and a digital elevation model (DEM). The tool uses the input radar backscatter to determine whether pixels should be classified as water; then creates polygons for water areas. The tool will also create polygons for areas that are not water, which will be considered land areas.",
        "parameters": {
                "in_radar_data": {
                        "type": "string",
                        "description": "The input radar data."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output polygon feature class that depicts water and land polygons."
                },
                "min_area": {
                        "type": "string",
                        "description": "The minimum area to extract as a water body. The default value is 50,000 square meters.",
                        "default": None
                },
                "in_dem_raster": {
                        "type": "string",
                        "description": "The input DEM.If the input radar data is not orthorectified, this DEM will be used to orthorectify it.This DEM will also be used to optimize the polygon construction.",
                        "default": None
                },
                "geoid": {
                        "type": "string",
                        "description": "Specifies whether the vertical reference system of the input DEM will be transformed to ellipsoidal height. Most elevation datasets are referenced to sea level orthometric height, so a correction is r...",
                        "default": None
                }
        },
        "required": [
                "in_radar_data",
                "out_feature_class"
        ]
},
    "create_binary_mask": {
        "name": "create_binary_mask",
        "description": "Converts an input raster dataset to a binary raster. Pixels are labeled as either mask or background based on user-defined values.",
        "parameters": {
                "in_raster": {
                        "type": "string",
                        "description": "The input raster dataset. \r\nIf the input is  multiband, the first band will be used by default."
                },
                "out_raster": {
                        "type": "string",
                        "description": "The output binary raster dataset. Supported formats are TIFF, \r\nCRF, and PNG."
                },
                "background_value": {
                        "type": "string",
                        "description": "The background value for the output raster. The default value is 0.",
                        "default": None
                },
                "flood_fill": {
                        "type": "string",
                        "description": "Specifies how \r\nbackground pixel values will be determined.FLOOD_FILL\u2014Background pixel values will be determined by the flood fill operation, which fills the connected pixels from the image boundary t...",
                        "default": None
                },
                "expand_background": {
                        "type": "string",
                        "description": "The number of pixels that will be used to expand or shrink the background. Negative values will shrink the background.",
                        "default": None
                },
                "expand_mask": {
                        "type": "string",
                        "description": "The number of pixels that will be used to expand or shrink the mask. Negative values will shrink the mask.",
                        "default": None
                },
                "min_region_size": {
                        "type": "string",
                        "description": "The number of connected pixels that will be used to define a mask region. Mask regions that are smaller than this size will be classified as background.",
                        "default": None
                },
                "background_nodata": {
                        "type": "string",
                        "description": "Specifies whether the background value will be set to NoData.\r\nBACKGROUND_NODATA\u2014The background value will be set to NoData.BACKGROUND_DATA\u2014The background value will not be set to NoData. This is the ...",
                        "default": None
                }
        },
        "required": [
                "in_raster",
                "out_raster"
        ]
}
}
