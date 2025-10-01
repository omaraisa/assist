# Generated ArcGIS Pro image-analyst Progent Functions
# Generated on 2025-10-01T15:16:34.151770
# Total tools: 96

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

    def analyze_changes_using_ccdc(self, params):
        """Analyze Changes Using CCDC

Evaluates changes in pixel values over time using the Continuous Change Detection and Classification (CCDC) method and generates a change analysis raster containing the model results. Learn more about how Analyze Changes Using CCDC works

        params: {"in_multidimensional_raster": <Raster Dataset; Raster Layer; Mosaic Dataset; Mosaic Layer; Image Service>, "bands": <Long>, "tmask_bands": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_multidimensional_raster = params.get("in_multidimensional_raster")
        if in_multidimensional_raster is None:
            return {"success": False, "error": "in_multidimensional_raster parameter is required"}
        bands = params.get("bands")
        tmask_bands = params.get("tmask_bands")
        chi_squared_threshold = params.get("chi_squared_threshold")
        min_anomaly_observations = params.get("min_anomaly_observations")
        update_frequency = params.get("update_frequency")

            # Generate output name and path
            output_name = f"{in_multidimensional_raster.replace(' ', '_')}_Analyze_Changes_Using_CCDC"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Analyze Changes Using CCDC
            arcpy.AnalyzeChangesUsingCCDC(in_multidimensional_raster, bands, tmask_bands, chi_squared_threshold, min_anomaly_observations, update_frequency)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def analyze_changes_using_landtrendr(self, params):
        """Analyze Changes Using LandTrendr

Evaluates changes in pixel values over time using the Landsat-based detection of trends in disturbance and recovery (LandTrendr) method and generates a change analysis raster containing the model results. Learn more about how LandTrendr works

        params: {"in_multidimensional_raster": <Raster Dataset; Raster Layer; Mosaic Dataset; Mosaic Layer; Image Service; File>, "processing_band": <String>, "snapping_date": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_multidimensional_raster = params.get("in_multidimensional_raster")
        if in_multidimensional_raster is None:
            return {"success": False, "error": "in_multidimensional_raster parameter is required"}
        processing_band = params.get("processing_band")
        snapping_date = params.get("snapping_date")
        max_num_segments = params.get("max_num_segments")
        vertex_count_overshoot = params.get("vertex_count_overshoot")
        spike_threshold = params.get("spike_threshold")
        recovery_threshold = params.get("recovery_threshold")
        prevent_one_year_recovery = params.get("prevent_one_year_recovery")
        recovery_trend = params.get("recovery_trend")
        min_num_observations = params.get("min_num_observations")
        best_model_proportion = params.get("best_model_proportion")
        pvalue_threshold = params.get("pvalue_threshold")
        if pvalue_threshold is None:
            return {"success": False, "error": "pvalue_threshold parameter is required"}
        output_other_bands = params.get("output_other_bands")

            # Generate output name and path
            output_name = f"{in_multidimensional_raster.replace(' ', '_')}_Analyze_Changes_Using_LandTrendr"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Analyze Changes Using LandTrendr
            arcpy.AnalyzeChangesUsingLandTrendr(in_multidimensional_raster, processing_band, snapping_date, max_num_segments, vertex_count_overshoot, spike_threshold, recovery_threshold, prevent_one_year_recovery, recovery_trend, min_num_observations, best_model_proportion, pvalue_threshold, output_other_bands)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compute_change_raster(self, params):
        """Compute Change Raster

Calculates the absolute, relative, categorical, or spectral difference between two raster datasets.

        params: {"from_raster": <Raster Dataset; Raster Layer; Mosaic Dataset; Mosaic Layer; Image Service; String>, "to_raster": <Raster Dataset; Raster Layer; Mosaic Dataset; Mosaic Layer; Image Service; String>, "compute_change_method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        from_raster = params.get("from_raster")
        if from_raster is None:
            return {"success": False, "error": "from_raster parameter is required"}
        to_raster = params.get("to_raster")
        if to_raster is None:
            return {"success": False, "error": "to_raster parameter is required"}
        compute_change_method = params.get("compute_change_method")
        from_classes = params.get("from_classes")
        to_classes = params.get("to_classes")
        filter_method = params.get("filter_method")
        define_transition_colors = params.get("define_transition_colors")

            # Generate output name and path
            output_name = f"{from_raster.replace(' ', '_')}_Compute_Change_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compute Change Raster
            arcpy.ComputeChangeRaster(from_raster, to_raster, compute_change_method, from_classes, to_classes, filter_method, define_transition_colors)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def detect_change_using_change_analysis_raster(self, params):
        """Detect Change Using Change Analysis Raster

Generates a raster containing pixel change information using the output change analysis raster from the Analyze Changes Using CCDC tool or the Analyze Changes Using LandTrendr tool.

        params: {"in_change_analysis_raster": <Raster Dataset; Raster Layer; Image Service>, "change_type": <String>, "max_number_changes": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_change_analysis_raster = params.get("in_change_analysis_raster")
        if in_change_analysis_raster is None:
            return {"success": False, "error": "in_change_analysis_raster parameter is required"}
        change_type = params.get("change_type")
        max_number_changes = params.get("max_number_changes")
        segment_date = params.get("segment_date")
        change_direction = params.get("change_direction")
        filter_by_year = params.get("filter_by_year")
        min_year = params.get("min_year")
        max_year = params.get("max_year")
        filter_by_duration = params.get("filter_by_duration")
        min_duration = params.get("min_duration")
        max_duration = params.get("max_duration")
        filter_by_magnitude = params.get("filter_by_magnitude")
        min_magnitude = params.get("min_magnitude")
        max_magnitude = params.get("max_magnitude")
        filter_by_start_value = params.get("filter_by_start_value")
        min_start_value = params.get("min_start_value")
        max_start_value = params.get("max_start_value")
        filter_by_end_value = params.get("filter_by_end_value")
        min_end_value = params.get("min_end_value")
        max_end_value = params.get("max_end_value")

            # Generate output name and path
            output_name = f"{in_change_analysis_raster.replace(' ', '_')}_Detect_Change_Using_Change_Analysis_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Detect Change Using Change Analysis Raster
            arcpy.DetectChangeUsingChangeAnalysisRaster(in_change_analysis_raster, change_type, max_number_changes, segment_date, change_direction, filter_by_year, min_year, max_year, filter_by_duration, min_duration, max_duration, filter_by_magnitude, min_magnitude, max_magnitude, filter_by_start_value, min_start_value, max_start_value, filter_by_end_value, min_end_value, max_end_value)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def classify_raster(self, params):
        """Classify Raster

Classifies a raster dataset based on an Esri classifier definition file (.ecd) and raster dataset inputs. The .ecd file contains all the information needed to perform a specific type of Esri-supported classification. The inputs to this tool must match the inputs used to generate the required .ecd file. The .ecd file can be generated from any of the classifier training tools, such as Train Random Trees Classifier or Train Support Vector Machine Classifier.

        params: {"in_raster": <Mosaic Layer; Raster Layer; Image Service; String; Raster Dataset; Mosaic Dataset>, "in_classifier_definition": <File>, "in_additional_raster": <Mosaic Layer; Raster Layer; Image Service; String; Raster Dataset; Mosaic Dataset>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_classifier_definition = params.get("in_classifier_definition")
        if in_classifier_definition is None:
            return {"success": False, "error": "in_classifier_definition parameter is required"}
        in_additional_raster = params.get("in_additional_raster")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Classify_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Classify Raster
            arcpy.ClassifyRaster(in_raster, in_classifier_definition, in_additional_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def classify_raster_using_spectra(self, params):
        """Classify Raster Using Spectra

Classifies a multiband raster dataset using spectral matching techniques. The input spectral data can be provided as a point feature class or a .json file.

        params: {"in_raster": <Mosaic Layer; Raster Layer; Image Service; String; Raster Dataset; Mosaic Dataset>, "in_spectra_file": <Feature Layer; File; String>, "method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_spectra_file = params.get("in_spectra_file")
        if in_spectra_file is None:
            return {"success": False, "error": "in_spectra_file parameter is required"}
        method = params.get("method")
        if method is None:
            return {"success": False, "error": "method parameter is required"}
        thresholds = params.get("thresholds")
        out_score_raster = params.get("out_score_raster")
        out_classifier_definition = params.get("out_classifier_definition")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Classify_Raster_Using_Spectra"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Classify Raster Using Spectra
            arcpy.ClassifyRasterUsingSpectra(in_raster, in_spectra_file, method, thresholds, out_score_raster, out_classifier_definition)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compute_confusion_matrix(self, params):
        """Compute Confusion Matrix

Computes a confusion matrix with errors of omission and commission and derives a kappa index of agreement, Intersection over Union (IoU), and overall accuracy between the classified map and the reference data. This tool uses the outputs from the Create Accuracy Assessment Points tool or the Update Accuracy Assessment Points tool.

        params: {"in_accuracy_assessment_points": <Feature Layer>, "out_confusion_matrix": <Table>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_accuracy_assessment_points = params.get("in_accuracy_assessment_points")
        if in_accuracy_assessment_points is None:
            return {"success": False, "error": "in_accuracy_assessment_points parameter is required"}
        out_confusion_matrix = params.get("out_confusion_matrix")
        if out_confusion_matrix is None:
            return {"success": False, "error": "out_confusion_matrix parameter is required"}

            # Generate output name and path
            output_name = f"{in_accuracy_assessment_points.replace(' ', '_')}_Compute_Confusion_Matrix"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compute Confusion Matrix
            arcpy.ComputeConfusionMatrix(in_accuracy_assessment_points, out_confusion_matrix)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compute_segment_attributes(self, params):
        """Compute Segment Attributes

Computes a set of attributes associated with the segmented image. The input raster can be a single-band or 3-band, 8-bit segmented image.

        params: {"in_segmented_raster": <Raster Layer; Mosaic Layer>, "in_additional_raster": <Raster Layer; Mosaic Layer>, "used_attributes": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_segmented_raster = params.get("in_segmented_raster")
        if in_segmented_raster is None:
            return {"success": False, "error": "in_segmented_raster parameter is required"}
        in_additional_raster = params.get("in_additional_raster")
        used_attributes = params.get("used_attributes")

            # Generate output name and path
            output_name = f"{in_segmented_raster.replace(' ', '_')}_Compute_Segment_Attributes"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compute Segment Attributes
            arcpy.ComputeSegmentAttributes(in_segmented_raster, in_additional_raster, used_attributes)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_accuracy_assessment_points(self, params):
        """Create Accuracy Assessment Points

Creates randomly sampled points for postclassification accuracy assessment. A common practice is to randomly select hundreds of points and label their classification types by referencing reliable sources, such as field work or human interpretation of high-resolution imagery. The reference points are then compared with the classification results at the same locations.

        params: {"in_class_data": <Raster Layer; Mosaic Layer; Feature Layer>, "out_points": <Feature Class>, "target_field": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_class_data = params.get("in_class_data")
        if in_class_data is None:
            return {"success": False, "error": "in_class_data parameter is required"}
        out_points = params.get("out_points")
        if out_points is None:
            return {"success": False, "error": "out_points parameter is required"}
        target_field = params.get("target_field")
        num_random_points = params.get("num_random_points")
        sampling = params.get("sampling")
        polygon_dimension_field = params.get("polygon_dimension_field")
        min_point_distance = params.get("min_point_distance")

            # Generate output name and path
            output_name = f"{in_class_data.replace(' ', '_')}_Create_Accuracy_Assessment_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Accuracy Assessment Points
            arcpy.CreateAccuracyAssessmentPoints(in_class_data, out_points, target_field, num_random_points, sampling, polygon_dimension_field, min_point_distance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_training_samples_from_seed_points(self, params):
        """Generate Training Samples From Seed Points

Generates training samples from seed points, such as accuracy assessment points or training sample points. A typical use case is generating training samples from an existing source, such as a thematic raster or a feature class.

        params: {"in_class_data": <Mosaic Layer; Raster Layer; Feature Layer; Image Service; String>, "in_seed_points": <Feature Layer>, "out_training_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_class_data = params.get("in_class_data")
        if in_class_data is None:
            return {"success": False, "error": "in_class_data parameter is required"}
        in_seed_points = params.get("in_seed_points")
        if in_seed_points is None:
            return {"success": False, "error": "in_seed_points parameter is required"}
        out_training_feature_class = params.get("out_training_feature_class")
        if out_training_feature_class is None:
            return {"success": False, "error": "out_training_feature_class parameter is required"}
        min_sample_area = params.get("min_sample_area")
        max_sample_radius = params.get("max_sample_radius")

            # Generate output name and path
            output_name = f"{in_class_data.replace(' ', '_')}_Generate_Training_Samples_From_Seed_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Training Samples From Seed Points
            arcpy.GenerateTrainingSamplesFromSeedPoints(in_class_data, in_seed_points, out_training_feature_class, min_sample_area, max_sample_radius)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def inspect_training_samples(self, params):
        """Inspect Training Samples

Estimates the accuracy of individual training samples. The cross validation accuracy is computed using the previously generated classification training result in an .ecd file and the training samples. Outputs include a raster dataset containing the misclassified class values and a training sample dataset with the accuracy score for each training sample.

        params: {"in_raster": <Mosaic Layer; Raster Layer; Image Service; String>, "in_training_features": <Feature Layer>, "in_classifier_definition": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_training_features = params.get("in_training_features")
        if in_training_features is None:
            return {"success": False, "error": "in_training_features parameter is required"}
        in_classifier_definition = params.get("in_classifier_definition")
        if in_classifier_definition is None:
            return {"success": False, "error": "in_classifier_definition parameter is required"}
        out_training_feature_class = params.get("out_training_feature_class")
        if out_training_feature_class is None:
            return {"success": False, "error": "out_training_feature_class parameter is required"}
        out_misclassified_raster = params.get("out_misclassified_raster")
        if out_misclassified_raster is None:
            return {"success": False, "error": "out_misclassified_raster parameter is required"}
        in_additional_raster = params.get("in_additional_raster")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Inspect_Training_Samples"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Inspect Training Samples
            arcpy.InspectTrainingSamples(in_raster, in_training_features, in_classifier_definition, out_training_feature_class, out_misclassified_raster, in_additional_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def linear_spectral_unmixing(self, params):
        """Linear Spectral Unmixing

Performs subpixel classification and calculates the fractional abundance of different land-cover types for individual pixels.

        params: {"in_raster": <Raster Dataset; Mosaic Dataset; Mosaic Layer; Raster Layer; File; Image Service>, "in_spectral_profile_file": <File; Feature Layer; String>, "value_option": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_spectral_profile_file = params.get("in_spectral_profile_file")
        if in_spectral_profile_file is None:
            return {"success": False, "error": "in_spectral_profile_file parameter is required"}
        value_option = params.get("value_option")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Linear_Spectral_Unmixing"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Linear Spectral Unmixing
            arcpy.LinearSpectralUnmixing(in_raster, in_spectral_profile_file, value_option)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def predict_using_regression_model(self, params):
        """Predict Using Regression Model

Predicts data values using the output from the Train Random Trees Regression Model tool.

        params: {"in_rasters": <Raster Dataset; Raster Layer; Mosaic Dataset; Mosaic Layer; Image Service; String>, "in_regression_definition": <File>, "out_raster_dataset": <Raster Dataset>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rasters = params.get("in_rasters")
        if in_rasters is None:
            return {"success": False, "error": "in_rasters parameter is required"}
        in_regression_definition = params.get("in_regression_definition")
        if in_regression_definition is None:
            return {"success": False, "error": "in_regression_definition parameter is required"}
        out_raster_dataset = params.get("out_raster_dataset")
        if out_raster_dataset is None:
            return {"success": False, "error": "out_raster_dataset parameter is required"}

            # Generate output name and path
            output_name = f"{in_rasters.replace(' ', '_')}_Predict_Using_Regression_Model"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Predict Using Regression Model
            arcpy.PredictUsingRegressionModel(in_rasters, in_regression_definition, out_raster_dataset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def train_random_trees_regression_model(self, params):
        """Train Random Trees Regression Model

Models the relationship between explanatory variables (independent variables) and a target dataset (dependent variable).

        params: {"in_rasters": <Mosaic Dataset; Mosaic Layer; Raster Dataset; Raster Layer; Image Service; String>, "in_target_data": <Feature Class; Feature Layer; Raster Dataset; Raster Layer; Mosaic Layer; Image Service>, "out_regression_definition": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rasters = params.get("in_rasters")
        if in_rasters is None:
            return {"success": False, "error": "in_rasters parameter is required"}
        in_target_data = params.get("in_target_data")
        if in_target_data is None:
            return {"success": False, "error": "in_target_data parameter is required"}
        out_regression_definition = params.get("out_regression_definition")
        if out_regression_definition is None:
            return {"success": False, "error": "out_regression_definition parameter is required"}
        target_value_field = params.get("target_value_field")
        target_dimension_field = params.get("target_dimension_field")
        raster_dimension = params.get("raster_dimension")
        out_importance_table = params.get("out_importance_table")
        max_num_trees = params.get("max_num_trees")
        max_tree_depth = params.get("max_tree_depth")
        max_samples = params.get("max_samples")
        average_points_per_cell = params.get("average_points_per_cell")
        percent_testing = params.get("percent_testing")
        out_scatterplots = params.get("out_scatterplots")
        out_sample_features = params.get("out_sample_features")

            # Generate output name and path
            output_name = f"{in_rasters.replace(' ', '_')}_Train_Random_Trees_Regression_Model"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Train Random Trees Regression Model
            arcpy.TrainRandomTreesRegressionModel(in_rasters, in_target_data, out_regression_definition, target_value_field, target_dimension_field, raster_dimension, out_importance_table, max_num_trees, max_tree_depth, max_samples, average_points_per_cell, percent_testing, out_scatterplots, out_sample_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_raster_segment_tiling_artifacts(self, params):
        """Remove Raster Segment Tiling Artifacts

Corrects segments or objects cut by tile boundaries during the segmentation process performed as a raster function. This tool is helpful for some regional processes, such as image segmentation, that have inconsistencies near image tile boundaries. This processing step is included in the Segment Mean Shift tool. It should only be used on a segmented image that was not created from that tool.

        params: {"in_segmented_raster": <Raster Dataset; Mosaic Dataset; Raster Layer; Mosaic Layer; Image Service; String>, "tilesizex": <Long>, "tilesizey": <Long>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_segmented_raster = params.get("in_segmented_raster")
        if in_segmented_raster is None:
            return {"success": False, "error": "in_segmented_raster parameter is required"}
        tilesizex = params.get("tilesizex")
        tilesizey = params.get("tilesizey")

            # Generate output name and path
            output_name = f"{in_segmented_raster.replace(' ', '_')}_Remove_Raster_Segment_Tiling_Artifacts"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Remove Raster Segment Tiling Artifacts
            arcpy.RemoveRasterSegmentTilingArtifacts(in_segmented_raster, tilesizex, tilesizey)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def segment_mean_shift(self, params):
        """Segment Mean Shift

Groups adjacent pixels that have similar spectral characteristics into segments.

        params: {"in_raster": <Mosaic Layer; Raster Layer>, "spectral_detail": <Double>, "spatial_detail": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        spectral_detail = params.get("spectral_detail")
        spatial_detail = params.get("spatial_detail")
        min_segment_size = params.get("min_segment_size")
        band_indexes = params.get("band_indexes")
        max_segment_size = params.get("max_segment_size")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Segment_Mean_Shift"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Segment Mean Shift
            arcpy.SegmentMeanShift(in_raster, spectral_detail, spatial_detail, min_segment_size, band_indexes, max_segment_size)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def train_iso_cluster_classifier(self, params):
        """Train Iso Cluster Classifier

Generates an Esri classifier definition file (.ecd) using the Iso Cluster classification definition. This tool performs an unsupervised classification.

        params: {"in_raster": <Raster Layer; Mosaic Layer; Image Service; String>, "max_classes": <Long>, "out_classifier_definition": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        max_classes = params.get("max_classes")
        if max_classes is None:
            return {"success": False, "error": "max_classes parameter is required"}
        out_classifier_definition = params.get("out_classifier_definition")
        if out_classifier_definition is None:
            return {"success": False, "error": "out_classifier_definition parameter is required"}
        in_additional_raster = params.get("in_additional_raster")
        max_iterations = params.get("max_iterations")
        min_samples_per_cluster = params.get("min_samples_per_cluster")
        skip_factor = params.get("skip_factor")
        used_attributes_used_attributes = params.get("used_attributes_used_attributes")
        max_merge_per_iter = params.get("max_merge_per_iter")
        max_merge_distance = params.get("max_merge_distance")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Train_Iso_Cluster_Classifier"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Train Iso Cluster Classifier
            arcpy.TrainIsoClusterClassifier(in_raster, max_classes, out_classifier_definition, in_additional_raster, max_iterations, min_samples_per_cluster, skip_factor, used_attributes_used_attributes, max_merge_per_iter, max_merge_distance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def train_maximum_likelihood_classifier(self, params):
        """Train Maximum Likelihood Classifier

Generates an Esri classifier definition file (.ecd) using the Maximum Likelihood Classifier (MLC) classification definition.

        params: {"in_raster": <Raster Layer; Mosaic Layer; Image Service; String>, "in_training_features": <Feature Layer>, "out_classifier_definition": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_training_features = params.get("in_training_features")
        if in_training_features is None:
            return {"success": False, "error": "in_training_features parameter is required"}
        out_classifier_definition = params.get("out_classifier_definition")
        if out_classifier_definition is None:
            return {"success": False, "error": "out_classifier_definition parameter is required"}
        in_additional_raster = params.get("in_additional_raster")
        used_attributes = params.get("used_attributes")
        dimension_value_field = params.get("dimension_value_field")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Train_Maximum_Likelihood_Classifier"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Train Maximum Likelihood Classifier
            arcpy.TrainMaximumLikelihoodClassifier(in_raster, in_training_features, out_classifier_definition, in_additional_raster, used_attributes, dimension_value_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def train_random_trees_classifier(self, params):
        """Train Random Trees Classifier

Generates an Esri classifier definition file (.ecd) using the Random Trees classification method. The random trees classifier is an image classification technique that is resistant to overfitting and can work with segmented images and other ancillary raster datasets. For standard image inputs, the tool accepts multiband imagery with any bit depth, and it will perform the Random Trees classification on a pixel basis or segment, based on the input training feature file.

        params: {"in_raster": <Raster Layer; Mosaic Layer; Image Service; String>, "in_training_features": <Feature Layer>, "out_classifier_definition": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_training_features = params.get("in_training_features")
        if in_training_features is None:
            return {"success": False, "error": "in_training_features parameter is required"}
        out_classifier_definition = params.get("out_classifier_definition")
        if out_classifier_definition is None:
            return {"success": False, "error": "out_classifier_definition parameter is required"}
        in_additional_raster = params.get("in_additional_raster")
        max_num_trees = params.get("max_num_trees")
        max_tree_depth = params.get("max_tree_depth")
        max_samples_per_class = params.get("max_samples_per_class")
        used_attributes_used_attributes = params.get("used_attributes_used_attributes")
        dimension_value_field = params.get("dimension_value_field")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Train_Random_Trees_Classifier"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Train Random Trees Classifier
            arcpy.TrainRandomTreesClassifier(in_raster, in_training_features, out_classifier_definition, in_additional_raster, max_num_trees, max_tree_depth, max_samples_per_class, used_attributes_used_attributes, dimension_value_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def train_support_vector_machine_classifier(self, params):
        """Train Support Vector Machine Classifier

Generates an Esri classifier definition file (.ecd) using the Support Vector Machine (SVM) classification definition.

        params: {"in_raster": <Raster Layer; Mosaic Layer; Image Service; String>, "in_training_features": <Feature Layer>, "out_classifier_definition": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_training_features = params.get("in_training_features")
        if in_training_features is None:
            return {"success": False, "error": "in_training_features parameter is required"}
        out_classifier_definition = params.get("out_classifier_definition")
        if out_classifier_definition is None:
            return {"success": False, "error": "out_classifier_definition parameter is required"}
        in_additional_raster = params.get("in_additional_raster")
        max_samples_per_class = params.get("max_samples_per_class")
        used_attributes_used_attributes = params.get("used_attributes_used_attributes")
        dimension_value_field = params.get("dimension_value_field")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Train_Support_Vector_Machine_Classifier"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Train Support Vector Machine Classifier
            arcpy.TrainSupportVectorMachineClassifier(in_raster, in_training_features, out_classifier_definition, in_additional_raster, max_samples_per_class, used_attributes_used_attributes, dimension_value_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def update_accuracy_assessment_points(self, params):
        """Update Accuracy Assessment Points

Updates the Target field in the attribute table to compare reference points to the classified image. Accuracy assessment uses known points to assess the validity of the classification model.

        params: {"in_class_data": <Raster Layer; Mosaic Layer; Feature Layer>, "in_points": <Feature Layer>, "out_points": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_class_data = params.get("in_class_data")
        if in_class_data is None:
            return {"success": False, "error": "in_class_data parameter is required"}
        in_points = params.get("in_points")
        if in_points is None:
            return {"success": False, "error": "in_points parameter is required"}
        out_points = params.get("out_points")
        if out_points is None:
            return {"success": False, "error": "out_points parameter is required"}
        target_field = params.get("target_field")
        polygon_dimension_field = params.get("polygon_dimension_field")
        point_dimension_field = params.get("point_dimension_field")

            # Generate output name and path
            output_name = f"{in_class_data.replace(' ', '_')}_Update_Accuracy_Assessment_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Update Accuracy Assessment Points
            arcpy.UpdateAccuracyAssessmentPoints(in_class_data, in_points, out_points, target_field, polygon_dimension_field, point_dimension_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def classify_objects_using_deep_learning(self, params):
        """Classify Objects Using Deep Learning

Runs a trained deep learning model on an input raster and an optional feature class to produce a feature class or table in which each input object or feature has an assigned class or category label. This tool requires a model definition file containing trained model information. The model can be trained using the Train Deep Learning Model tool or by a third-party training software such as TensorFlow, PyTorch, or Keras. The model definition file can be an Esri model definition JSON file (.emd) or a deep learning model package, and it must contain the path to the Python raster function to be called to process each object and the path to the trained binary deep learning model file.

        params: {"in_raster": <Raster Dataset; Raster Layer; Mosaic Layer; Image Service; Map Server; Map Server Layer; Internet Tiled Layer; Folder; Feature Layer; Feature Class>, "out_feature_class": <Feature Class>, "in_model_definition": <File; String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        in_model_definition = params.get("in_model_definition")
        if in_model_definition is None:
            return {"success": False, "error": "in_model_definition parameter is required"}
        in_features = params.get("in_features")
        class_label_field = params.get("class_label_field")
        processing_mode = params.get("processing_mode")
        model_arguments = params.get("model_arguments")
        caption_field = params.get("caption_field")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Classify_Objects_Using_Deep_Learning"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Classify Objects Using Deep Learning
            arcpy.ClassifyObjectsUsingDeepLearning(in_raster, out_feature_class, in_model_definition, in_features, class_label_field, processing_mode, model_arguments, caption_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def classify_pixels_using_deep_learning(self, params):
        """Classify Pixels Using Deep Learning

Runs a trained deep learning model on an input raster to produce a classified raster, with each valid pixel having an assigned class label. This tool requires a model definition file containing trained model information. The model can be trained using the Train Deep Learning Model tool or by a third-party training software such as TensorFlow, PyTorch, or Keras. The model definition file can be an Esri model definition JSON file (.emd) or a deep learning model package, and it must contain the path to the Python raster function to be called to process each object and the path to the trained binary deep learning model file.

        params: {"in_raster": <Raster Dataset; Raster Layer; Mosaic Layer; Image Service; Map Server; Map Server Layer; Internet Tiled Layer; Folder; Feature Layer; Feature Class>, "in_model_definition": <File; String>, "arguments": <Value Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_model_definition = params.get("in_model_definition")
        if in_model_definition is None:
            return {"success": False, "error": "in_model_definition parameter is required"}
        arguments = params.get("arguments")
        processing_mode = params.get("processing_mode")
        if processing_mode is None:
            return {"success": False, "error": "processing_mode parameter is required"}
        out_classified_folder = params.get("out_classified_folder")
        out_featureclass = params.get("out_featureclass")
        overwrite_attachments = params.get("overwrite_attachments")
        use_pixelspace = params.get("use_pixelspace")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Classify_Pixels_Using_Deep_Learning"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Classify Pixels Using Deep Learning
            arcpy.ClassifyPixelsUsingDeepLearning(in_raster, in_model_definition, arguments, processing_mode, out_classified_folder, out_featureclass, overwrite_attachments, use_pixelspace)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compute_accuracy_for_object_detection(self, params):
        """Compute Accuracy For Object Detection

Calculates the accuracy of a deep learning model by comparing the detected objects from the Detect Objects Using Deep Learning tool to ground truth data. Learn more about how Compute Accuracy For Object Detection works.

        params: {"detected_features": <Feature Class; Feature Layer>, "ground_truth_features": <Feature Class; Feature Layer>, "out_accuracy_table": <Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        detected_features = params.get("detected_features")
        if detected_features is None:
            return {"success": False, "error": "detected_features parameter is required"}
        ground_truth_features = params.get("ground_truth_features")
        if ground_truth_features is None:
            return {"success": False, "error": "ground_truth_features parameter is required"}
        out_accuracy_table = params.get("out_accuracy_table")
        if out_accuracy_table is None:
            return {"success": False, "error": "out_accuracy_table parameter is required"}
        out_accuracy_report = params.get("out_accuracy_report")
        detected_class_value_field = params.get("detected_class_value_field")
        ground_truth_class_value_field = params.get("ground_truth_class_value_field")
        min_iou = params.get("min_iou")
        mask_features = params.get("mask_features")

            # Generate output name and path
            output_name = f"{detected_features.replace(' ', '_')}_Compute_Accuracy_For_Object_Detection"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compute Accuracy For Object Detection
            arcpy.ComputeAccuracyForObjectDetection(detected_features, ground_truth_features, out_accuracy_table, out_accuracy_report, detected_class_value_field, ground_truth_class_value_field, min_iou, mask_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compute_accuracy_for_pixel_classification(self, params):
        """Compute Accuracy For Pixel Classification

Computes a confusion matrix, based on errors of omission and commission, and the Intersection over Union (IoU) score. The accuracy is computed  between the output from the Classify Pixels Using Deep Learning tool  and the ground truth data. The tool is only valid for pixel classification models, not other models used with the Classify Pixels Using Deep Learning tool.

        params: {"in_raster": <Mosaic Layer; Raster Layer; Image Service; String; Raster Dataset; Mosaic Dataset>, "in_ground_truth_data": <Mosaic Layer; Raster Layer; Feature Layer>, "out_confusion_matrix": <Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_ground_truth_data = params.get("in_ground_truth_data")
        if in_ground_truth_data is None:
            return {"success": False, "error": "in_ground_truth_data parameter is required"}
        out_confusion_matrix = params.get("out_confusion_matrix")
        if out_confusion_matrix is None:
            return {"success": False, "error": "out_confusion_matrix parameter is required"}
        num_random_points = params.get("num_random_points")
        sampling = params.get("sampling")
        min_point_distance = params.get("min_point_distance")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Compute_Accuracy_For_Pixel_Classification"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compute Accuracy For Pixel Classification
            arcpy.ComputeAccuracyForPixelClassification(in_raster, in_ground_truth_data, out_confusion_matrix, num_random_points, sampling, min_point_distance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def detect_change_using_deep_learning(self, params):
        """Detect Change Using Deep Learning

Runs a trained deep learning model to detect change between two rasters. This tool requires a model definition file containing trained model information. The model definition file can be an Esri model definition JSON file (.emd) or a deep learning model package, and it must contain the path to the Python raster function to be called to process each object and the path to the trained binary deep learning model file.

        params: {"from_raster": <Raster Dataset; Raster Layer; Mosaic Layer; Image Service; Map Server; Map Server Layer; Internet Tiled Layer>, "to_raster": <Raster Dataset; Raster Layer; Mosaic Layer; Image Service; Map Server; Map Server Layer; Internet Tiled Layer>, "out_classified_raster": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        from_raster = params.get("from_raster")
        if from_raster is None:
            return {"success": False, "error": "from_raster parameter is required"}
        to_raster = params.get("to_raster")
        if to_raster is None:
            return {"success": False, "error": "to_raster parameter is required"}
        out_classified_raster = params.get("out_classified_raster")
        if out_classified_raster is None:
            return {"success": False, "error": "out_classified_raster parameter is required"}
        in_model_definition = params.get("in_model_definition")
        if in_model_definition is None:
            return {"success": False, "error": "in_model_definition parameter is required"}
        arguments = params.get("arguments")

            # Generate output name and path
            output_name = f"{from_raster.replace(' ', '_')}_Detect_Change_Using_Deep_Learning"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Detect Change Using Deep Learning
            arcpy.DetectChangeUsingDeepLearning(from_raster, to_raster, out_classified_raster, in_model_definition, arguments)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def detect_control_points(self, params):
        """Detect Control Points

Detects ground control points in a mosaic dataset.

        params: {"in_mosaic_dataset": <Mosaic Dataset; Mosaic Layer>, "in_control_points": <File; Feature Class; Feature Layer; String>, "out_control_points": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mosaic_dataset = params.get("in_mosaic_dataset")
        if in_mosaic_dataset is None:
            return {"success": False, "error": "in_mosaic_dataset parameter is required"}
        in_control_points = params.get("in_control_points")
        if in_control_points is None:
            return {"success": False, "error": "in_control_points parameter is required"}
        out_control_points = params.get("out_control_points")
        if out_control_points is None:
            return {"success": False, "error": "out_control_points parameter is required"}
        out_folder_image_chips = params.get("out_folder_image_chips")
        tile_size = params.get("tile_size")
        number_tie_points_per_gcp = params.get("number_tie_points_per_gcp")

            # Generate output name and path
            output_name = f"{in_mosaic_dataset.replace(' ', '_')}_Detect_Control_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Detect Control Points
            arcpy.DetectControlPoints(in_mosaic_dataset, in_control_points, out_control_points, out_folder_image_chips, tile_size, number_tie_points_per_gcp)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def detect_objects_using_deep_learning(self, params):
        """Detect Objects Using Deep Learning

Runs a trained deep learning model on an input raster to produce a feature class containing the objects it finds. The features can be bounding boxes or polygons around the objects found or points at the centers of the objects. This tool requires a model definition file containing trained model information. The model can be trained using the Train Deep Learning Model tool or by a third-party training software such as TensorFlow, PyTorch, or Keras. The model definition file can be an Esri model definition JSON file (.emd) or a deep learning model package, and it must contain the path to the Python raster function to be called to process each object and the path to the trained binary deep learning model file.

        params: {"in_raster": <Raster Dataset; Raster Layer; Mosaic Layer; Image Service; Map Server; Map Server Layer; Internet Tiled Layer; Folder; Feature Layer; Feature Class; Oriented Imagery Layer>, "out_detected_objects": <Feature Class>, "in_model_definition": <File; String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_detected_objects = params.get("out_detected_objects")
        if out_detected_objects is None:
            return {"success": False, "error": "out_detected_objects parameter is required"}
        in_model_definition = params.get("in_model_definition")
        if in_model_definition is None:
            return {"success": False, "error": "in_model_definition parameter is required"}
        arguments = params.get("arguments")
        run_nms = params.get("run_nms")
        confidence_score_field = params.get("confidence_score_field")
        class_value_field = params.get("class_value_field")
        max_overlap_ratio = params.get("max_overlap_ratio")
        processing_mode = params.get("processing_mode")
        use_pixelspace = params.get("use_pixelspace")
        in_objects_of_interest = params.get("in_objects_of_interest")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Detect_Objects_Using_Deep_Learning"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Detect Objects Using Deep Learning
            arcpy.DetectObjectsUsingDeepLearning(in_raster, out_detected_objects, in_model_definition, arguments, run_nms, confidence_score_field, class_value_field, max_overlap_ratio, processing_mode, use_pixelspace, in_objects_of_interest)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_training_data_for_deep_learning(self, params):
        """Export Training Data For Deep Learning

Converts labeled vector or raster data to deep learning training datasets using a remote sensing image. The output is a folder of image chips and a folder of metadata files in the specified format.

        params: {"in_raster": <Raster Dataset; Raster Layer; Mosaic Layer; Image Service; Map Server; Map Server Layer; Internet Tiled Layer; Folder>, "out_folder": <Folder>, "in_class_data": <Feature Class; Feature Layer; Raster Dataset; Raster Layer; Mosaic Layer; Image Service; Table; Folder>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_folder = params.get("out_folder")
        if out_folder is None:
            return {"success": False, "error": "out_folder parameter is required"}
        in_class_data = params.get("in_class_data")
        if in_class_data is None:
            return {"success": False, "error": "in_class_data parameter is required"}
        image_chip_format = params.get("image_chip_format")
        if image_chip_format is None:
            return {"success": False, "error": "image_chip_format parameter is required"}
        tile_size_x = params.get("tile_size_x")
        tile_size_y = params.get("tile_size_y")
        stride_x = params.get("stride_x")
        stride_y = params.get("stride_y")
        output_nofeature_tiles = params.get("output_nofeature_tiles")
        metadata_format = params.get("metadata_format")
        start_index = params.get("start_index")
        class_value_field = params.get("class_value_field")
        buffer_radius = params.get("buffer_radius")
        in_mask_polygons = params.get("in_mask_polygons")
        rotation_angle = params.get("rotation_angle")
        reference_system = params.get("reference_system")
        processing_mode = params.get("processing_mode")
        blacken_around_feature = params.get("blacken_around_feature")
        crop_mode = params.get("crop_mode")
        in_raster2 = params.get("in_raster2")
        in_instance_data = params.get("in_instance_data")
        instance_class_value_field = params.get("instance_class_value_field")
        min_polygon_overlap_ratio = params.get("min_polygon_overlap_ratio")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Export_Training_Data_For_Deep_Learning"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Training Data For Deep Learning
            arcpy.ExportTrainingDataForDeepLearning(in_raster, out_folder, in_class_data, image_chip_format, tile_size_x, tile_size_y, stride_x, stride_y, output_nofeature_tiles, metadata_format, start_index, class_value_field, buffer_radius, in_mask_polygons, rotation_angle, reference_system, processing_mode, blacken_around_feature, crop_mode, in_raster2, in_instance_data, instance_class_value_field, min_polygon_overlap_ratio)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_features_using_ai_models(self, params):
        """Extract Features Using AI Models

Runs one or more pretrained deep learning models on an input raster to extract features and automate the postprocessing of the inferenced outputs. Learn more about how Extract Features Using AI Models works

        params: {"in_raster": <Raster Layer; Raster Dataset; Mosaic Layer>, "mode": <String>, "out_location": <Workspace>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        mode = params.get("mode")
        if mode is None:
            return {"success": False, "error": "mode parameter is required"}
        out_location = params.get("out_location")
        if out_location is None:
            return {"success": False, "error": "out_location parameter is required"}
        out_prefix = params.get("out_prefix")
        if out_prefix is None:
            return {"success": False, "error": "out_prefix parameter is required"}
        area_of_interest = params.get("area_of_interest")
        pretrained_models = params.get("pretrained_models")
        additional_models = params.get("additional_models")
        confidence_threshold = params.get("confidence_threshold")
        save_intermediate_output = params.get("save_intermediate_output")
        test_time_augmentation = params.get("test_time_augmentation")
        buffer_distance = params.get("buffer_distance")
        extend_length = params.get("extend_length")
        smoothing_tolerance = params.get("smoothing_tolerance")
        dangle_length = params.get("dangle_length")
        in_road_features = params.get("in_road_features")
        road_buffer_width = params.get("road_buffer_width")
        regularize_parcels = params.get("regularize_parcels")
        post_processing_workflow = params.get("post_processing_workflow")
        out_features = params.get("out_features")
        parcel_tolerance = params.get("parcel_tolerance")
        regularization_method = params.get("regularization_method")
        poly_tolerance = params.get("poly_tolerance")
        prompt = params.get("prompt")
        in_features = params.get("in_features")
        out_summary = params.get("out_summary")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Extract_Features_Using_AI_Models"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract Features Using AI Models
            arcpy.ExtractFeaturesUsingAIModels(in_raster, mode, out_location, out_prefix, area_of_interest, pretrained_models, additional_models, confidence_threshold, save_intermediate_output, test_time_augmentation, buffer_distance, extend_length, smoothing_tolerance, dangle_length, in_road_features, road_buffer_width, regularize_parcels, post_processing_workflow, out_features, parcel_tolerance, regularization_method, poly_tolerance, prompt, in_features, out_summary)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def non_maximum_suppression(self, params):
        """Non Maximum Suppression

Identifies duplicate features from the output of the Detect Objects Using Deep Learning tool as a postprocessing step and creates a new output with no duplicate features. The Detect Objects Using Deep Learning tool can return more than one bounding box or polygon for the same object, especially as a tiling side effect. If two features overlap more than a given maximum ratio, the feature with the lower confidence value will be removed.

        params: {"in_featureclass": <Feature Class; Feature Layer>, "confidence_score_field": <Field>, "out_featureclass": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_featureclass = params.get("in_featureclass")
        if in_featureclass is None:
            return {"success": False, "error": "in_featureclass parameter is required"}
        confidence_score_field = params.get("confidence_score_field")
        if confidence_score_field is None:
            return {"success": False, "error": "confidence_score_field parameter is required"}
        out_featureclass = params.get("out_featureclass")
        if out_featureclass is None:
            return {"success": False, "error": "out_featureclass parameter is required"}
        class_value_field = params.get("class_value_field")
        max_overlap_ratio = params.get("max_overlap_ratio")

            # Generate output name and path
            output_name = f"{in_featureclass.replace(' ', '_')}_Non_Maximum_Suppression"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Non Maximum Suppression
            arcpy.NonMaximumSuppression(in_featureclass, confidence_score_field, out_featureclass, class_value_field, max_overlap_ratio)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def train_deep_learning_model(self, params):
        """Train Deep Learning Model

Trains a deep learning model using the output from the Export Training Data For Deep Learning tool.

        params: {"in_folder": <Folder>, "out_folder": <Folder>, "max_epochs": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_folder = params.get("in_folder")
        if in_folder is None:
            return {"success": False, "error": "in_folder parameter is required"}
        out_folder = params.get("out_folder")
        if out_folder is None:
            return {"success": False, "error": "out_folder parameter is required"}
        max_epochs = params.get("max_epochs")
        model_type = params.get("model_type")
        batch_size = params.get("batch_size")
        arguments = params.get("arguments")
        learning_rate = params.get("learning_rate")
        backbone_model = params.get("backbone_model")
        pretrained_model = params.get("pretrained_model")
        validation_percentage = params.get("validation_percentage")
        stop_training = params.get("stop_training")
        freeze = params.get("freeze")
        augmentation = params.get("augmentation")
        augmentation_parameters = params.get("augmentation_parameters")
        chip_size = params.get("chip_size")
        resize_to = params.get("resize_to")
        weight_init_scheme = params.get("weight_init_scheme")
        monitor = params.get("monitor")
        tensorboard = params.get("tensorboard")

            # Generate output name and path
            output_name = f"{in_folder.replace(' ', '_')}_Train_Deep_Learning_Model"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Train Deep Learning Model
            arcpy.TrainDeepLearningModel(in_folder, out_folder, max_epochs, model_type, batch_size, arguments, learning_rate, backbone_model, pretrained_model, validation_percentage, stop_training, freeze, augmentation, augmentation_parameters, chip_size, resize_to, weight_init_scheme, monitor, tensorboard)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def train_using_autodl(self, params):
        """Train Using AutoDL

Trains a deep learning model by building training pipelines and automating much of the training process.  This includes data augmentation, model selection, hyperparameter tuning, and batch size deduction. Its outputs include performance metrics of the best model on the training data, as well as the trained  deep learning model package (.dlpk file) that can be used as input for the Extract Features Using AI Models tool to predict on new imagery. Learn more about how AutoDL works

        params: {"in_data": <Folder>, "out_model": <File>, "pretrained_model": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_data = params.get("in_data")
        if in_data is None:
            return {"success": False, "error": "in_data parameter is required"}
        out_model = params.get("out_model")
        if out_model is None:
            return {"success": False, "error": "out_model parameter is required"}
        pretrained_model = params.get("pretrained_model")
        total_time_limit = params.get("total_time_limit")
        autodl_mode = params.get("autodl_mode")
        networks = params.get("networks")
        save_evaluated_models = params.get("save_evaluated_models")

            # Generate output name and path
            output_name = f"{in_data.replace(' ', '_')}_Train_Using_AutoDL"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Train Using AutoDL
            arcpy.TrainUsingAutoDL(in_data, out_model, pretrained_model, total_time_limit, autodl_mode, networks, save_evaluated_models)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def sample(self, params):
        """Sample

Creates a table or a point feature class that shows the values of cells from a raster, or a set of rasters, for defined locations. The locations are defined by raster cells, points, polylines, or polygons. Learn more about how Sample works

        params: {"in_rastersin_raster": <Raster Layer>, "in_location_data": <Raster Layer; Feature Layer>, "out_table": <Table; Point feature class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rastersin_raster = params.get("in_rastersin_raster")
        if in_rastersin_raster is None:
            return {"success": False, "error": "in_rastersin_raster parameter is required"}
        in_location_data = params.get("in_location_data")
        if in_location_data is None:
            return {"success": False, "error": "in_location_data parameter is required"}
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}
        resampling_type = params.get("resampling_type")
        unique_id_field = params.get("unique_id_field")
        process_as_multidimensional = params.get("process_as_multidimensional")
        acquisition_definition = params.get("acquisition_definition")
        statistics_type = params.get("statistics_type")
        percentile_value = params.get("percentile_value")
        buffer_distance = params.get("buffer_distance")
        layout = params.get("layout")
        generate_feature_class = params.get("generate_feature_class")

            # Generate output name and path
            output_name = f"{in_rastersin_raster.replace(' ', '_')}_Sample"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Sample
            arcpy.Sample(in_rastersin_raster, in_location_data, out_table, resampling_type, unique_id_field, process_as_multidimensional, acquisition_definition, statistics_type, percentile_value, buffer_distance, layout, generate_feature_class)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def interpolate_from_spatiotemporal_points(self, params):
        """Interpolate From Spatiotemporal Points

Interpolates temporal point data into a multidimensional raster.

        params: {"in_dataset": <Trajectory Layer; Feature Layer; Mosaic Dataset; Mosaic Layer>, "variable_field": <String>, "time_field": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        variable_field = params.get("variable_field")
        if variable_field is None:
            return {"success": False, "error": "variable_field parameter is required"}
        time_field = params.get("time_field")
        if time_field is None:
            return {"success": False, "error": "time_field parameter is required"}
        temporal_aggregation = params.get("temporal_aggregation")
        cell_size = params.get("cell_size")
        interpolation_method = params.get("interpolation_method")
        if interpolation_method is None:
            return {"success": False, "error": "interpolation_method parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Interpolate_From_Spatiotemporal_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Interpolate From Spatiotemporal Points
            arcpy.InterpolateFromSpatiotemporalPoints(in_dataset, variable_field, time_field, temporal_aggregation, cell_size, interpolation_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def optimal_interpolation(self, params):
        """Optimal Interpolation

Statistically assimilates data combined from multiple sources to produce an output raster. The tool can be used to merge background data, such as model outputs, with observation data, such as point measurements, to perform interpolation. Learn more about how Optimal Interpolation works.

        params: {"in_background_raster": <Raster Dataset; Raster Layer; Image Service>, "in_obs_data": <Feature Layer; Trajectory Layer>, "obs_field": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_background_raster = params.get("in_background_raster")
        if in_background_raster is None:
            return {"success": False, "error": "in_background_raster parameter is required"}
        in_obs_data = params.get("in_obs_data")
        if in_obs_data is None:
            return {"success": False, "error": "in_obs_data parameter is required"}
        obs_field = params.get("obs_field")
        if obs_field is None:
            return {"success": False, "error": "obs_field parameter is required"}
        background_error_var = params.get("background_error_var")
        if background_error_var is None:
            return {"success": False, "error": "background_error_var parameter is required"}
        obs_error_var = params.get("obs_error_var")
        if obs_error_var is None:
            return {"success": False, "error": "obs_error_var parameter is required"}
        background_error_corr_length = params.get("background_error_corr_length")

            # Generate output name and path
            output_name = f"{in_background_raster.replace(' ', '_')}_Optimal_Interpolation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Optimal Interpolation
            arcpy.OptimalInterpolation(in_background_raster, in_obs_data, obs_field, background_error_var, obs_error_var, background_error_corr_length)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def raster_calculator(self, params):
        """Raster Calculator

Build and run a single map algebra expression using Python syntax. Learn more about how Raster Calculator works

        params: {"expression": <Raster Calculator Expression>, "output_raster": <Raster Dataset>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        expression = params.get("expression")
        if expression is None:
            return {"success": False, "error": "expression parameter is required"}
        output_raster = params.get("output_raster")
        if output_raster is None:
            return {"success": False, "error": "output_raster parameter is required"}

            # Generate output name and path
            output_name = f"{expression.replace(' ', '_')}_Raster_Calculator"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Raster Calculator
            arcpy.RasterCalculator(expression, output_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def abs(self, params):
        """Abs

Calculates the absolute value of the cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Abs"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Abs
            arcpy.Abs(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def divide(self, params):
        """Divide

Divides the values of two rasters on a cell-by-cell basis.

        params: {"in_raster_or_constant1": <Raster Layer; Constant>, "in_raster_or_constant2": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant1 = params.get("in_raster_or_constant1")
        if in_raster_or_constant1 is None:
            return {"success": False, "error": "in_raster_or_constant1 parameter is required"}
        in_raster_or_constant2 = params.get("in_raster_or_constant2")
        if in_raster_or_constant2 is None:
            return {"success": False, "error": "in_raster_or_constant2 parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Divide"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Divide
            arcpy.Divide(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def exp(self, params):
        """Exp

Calculates the base e exponential of the cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Exp"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Exp
            arcpy.Exp(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def exp10(self, params):
        """Exp10

Calculates the base 10 exponential of the cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Exp10"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Exp10
            arcpy.Exp10(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def exp2(self, params):
        """Exp2

Calculates the base 2 exponential of the cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Exp2"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Exp2
            arcpy.Exp2(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def float(self, params):
        """Float

Converts each cell value of a raster into a floating-point representation.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Float"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Float
            arcpy.Float(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def int(self, params):
        """Int

Converts each cell value of a raster to an integer by truncation.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Int"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Int
            arcpy.Int(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def ln(self, params):
        """Ln

Calculates the natural logarithm (base e) of cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Ln"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Ln
            arcpy.Ln(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def log10(self, params):
        """Log10

Calculates the base 10 logarithm of cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Log10"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Log10
            arcpy.Log10(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def log2(self, params):
        """Log2

Calculates the base 2 logarithm of cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Log2"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Log2
            arcpy.Log2(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def minus(self, params):
        """Minus

Subtracts the value of the second input raster from the value of the first input raster on a cell-by-cell basis.

        params: {"in_raster_or_constant1": <Raster Layer; Constant>, "in_raster_or_constant2": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant1 = params.get("in_raster_or_constant1")
        if in_raster_or_constant1 is None:
            return {"success": False, "error": "in_raster_or_constant1 parameter is required"}
        in_raster_or_constant2 = params.get("in_raster_or_constant2")
        if in_raster_or_constant2 is None:
            return {"success": False, "error": "in_raster_or_constant2 parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Minus"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Minus
            arcpy.Minus(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def mod(self, params):
        """Mod

Finds the remainder (modulo) of the first raster when divided by the second raster on a cell-by-cell basis.

        params: {"in_raster_or_constant1": <Raster Layer; Constant>, "in_raster_or_constant2": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant1 = params.get("in_raster_or_constant1")
        if in_raster_or_constant1 is None:
            return {"success": False, "error": "in_raster_or_constant1 parameter is required"}
        in_raster_or_constant2 = params.get("in_raster_or_constant2")
        if in_raster_or_constant2 is None:
            return {"success": False, "error": "in_raster_or_constant2 parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Mod"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Mod
            arcpy.Mod(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def negate(self, params):
        """Negate

Changes the sign (multiplies by -1) of the cell values of the input raster on a cell-by-cell basis.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Negate"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Negate
            arcpy.Negate(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def plus(self, params):
        """Plus

Adds (sums) the values of two rasters on a cell-by-cell basis.

        params: {"in_raster_or_constant1": <Raster Layer; Constant>, "in_raster_or_constant2": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant1 = params.get("in_raster_or_constant1")
        if in_raster_or_constant1 is None:
            return {"success": False, "error": "in_raster_or_constant1 parameter is required"}
        in_raster_or_constant2 = params.get("in_raster_or_constant2")
        if in_raster_or_constant2 is None:
            return {"success": False, "error": "in_raster_or_constant2 parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Plus"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Plus
            arcpy.Plus(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def power(self, params):
        """Power

Raises the cell values in a raster to the power of the values found in another raster.

        params: {"in_raster_or_constant1": <Raster Layer; Constant>, "in_raster_or_constant2": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant1 = params.get("in_raster_or_constant1")
        if in_raster_or_constant1 is None:
            return {"success": False, "error": "in_raster_or_constant1 parameter is required"}
        in_raster_or_constant2 = params.get("in_raster_or_constant2")
        if in_raster_or_constant2 is None:
            return {"success": False, "error": "in_raster_or_constant2 parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Power"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Power
            arcpy.Power(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def round_down(self, params):
        """Round Down

Returns the next lower integer value, just represented as a floating point, for each cell in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Round_Down"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Round Down
            arcpy.RoundDown(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def round_up(self, params):
        """Round Up

Returns the next higher integer value, just represented as a floating point, for each cell in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Round_Up"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Round Up
            arcpy.RoundUp(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def square(self, params):
        """Square

Calculates the square of the cell values in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Square"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Square
            arcpy.Square(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def square_root(self, params):
        """Square Root

Calculates the square root of the cell values in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Square_Root"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Square Root
            arcpy.SquareRoot(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def times(self, params):
        """Times

Multiplies the values of two rasters on a cell-by-cell basis.

        params: {"in_raster_or_constant1": <Raster Layer; Constant>, "in_raster_or_constant2": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant1 = params.get("in_raster_or_constant1")
        if in_raster_or_constant1 is None:
            return {"success": False, "error": "in_raster_or_constant1 parameter is required"}
        in_raster_or_constant2 = params.get("in_raster_or_constant2")
        if in_raster_or_constant2 is None:
            return {"success": False, "error": "in_raster_or_constant2 parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Times"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Times
            arcpy.Times(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_video_frames_to_images(self, params):
        """Extract Video Frames To Images

Extracts video frame images and associated metadata from a full-motion video (FMV)-compliant video stream.  The extracted images can be added to a mosaic dataset or other tools and functions for further analysis.

        params: {"in_video": <File>, "out_folder": <Folder>, "image_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_video = params.get("in_video")
        if in_video is None:
            return {"success": False, "error": "in_video parameter is required"}
        out_folder = params.get("out_folder")
        if out_folder is None:
            return {"success": False, "error": "out_folder parameter is required"}
        image_type = params.get("image_type")
        image_overlap = params.get("image_overlap")
        require_fresh_metadata = params.get("require_fresh_metadata")
        min_time = params.get("min_time")

            # Generate output name and path
            output_name = f"{in_video.replace(' ', '_')}_Extract_Video_Frames_To_Images"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract Video Frames To Images
            arcpy.ExtractVideoFramesToImages(in_video, out_folder, image_type, image_overlap, require_fresh_metadata, min_time)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def video_metadata_to_feature_class(self, params):
        """Video Metadata To Feature Class

Extracts the platform, frame center, frame outline, and attributes metadata from a full-motion video (FMV)-compliant video. The output geometry and attributes are saved as feature classes.

        params: {"in_video": <File>, "csv_file": <File>, "flightpath": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_video = params.get("in_video")
        if in_video is None:
            return {"success": False, "error": "in_video parameter is required"}
        csv_file = params.get("csv_file")
        flightpath = params.get("flightpath")
        flightpath_type = params.get("flightpath_type")
        imagepath = params.get("imagepath")
        imagepath_type = params.get("imagepath_type")
        footprint = params.get("footprint")
        start_time = params.get("start_time")
        stop_time = params.get("stop_time")
        min_distance = params.get("min_distance")
        min_time = params.get("min_time")
        vmti = params.get("vmti")

            # Generate output name and path
            output_name = f"{in_video.replace(' ', '_')}_Video_Metadata_To_Feature_Class"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Video Metadata To Feature Class
            arcpy.VideoMetadataToFeatureClass(in_video, csv_file, flightpath, flightpath_type, imagepath, imagepath_type, footprint, start_time, stop_time, min_distance, min_time, vmti)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def video_multiplexer(self, params):
        """Video Multiplexer

Creates a single full-motion video (FMV)-compliant video file that combines an archived video stream file and a separate associated metadata file synchronized by a time stamp. The process of combining the two files containing the video and metadata files is called multiplexing.

        params: {"in_video_file": <File>, "metadata_file": <File>, "out_video_file": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_video_file = params.get("in_video_file")
        if in_video_file is None:
            return {"success": False, "error": "in_video_file parameter is required"}
        metadata_file = params.get("metadata_file")
        if metadata_file is None:
            return {"success": False, "error": "metadata_file parameter is required"}
        out_video_file = params.get("out_video_file")
        if out_video_file is None:
            return {"success": False, "error": "out_video_file parameter is required"}
        metadata_mapping_file = params.get("metadata_mapping_file")
        timeshift_file = params.get("timeshift_file")
        elevation_layer = params.get("elevation_layer")
        input_coordinate_system = params.get("input_coordinate_system")

            # Generate output name and path
            output_name = f"{in_video_file.replace(' ', '_')}_Video_Multiplexer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Video Multiplexer
            arcpy.VideoMultiplexer(in_video_file, metadata_file, out_video_file, metadata_mapping_file, timeshift_file, elevation_layer, input_coordinate_system)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def aggregate_multidimensional_raster(self, params):
        """Aggregate Multidimensional Raster

Generates a multidimensional raster dataset by combining existing multidimensional raster variables along a dimension.

        params: {"in_multidimensional_raster": <Raster Dataset; Raster Layer; Mosaic Dataset; Mosaic Layer; Image Service; File>, "dimension": <String>, "aggregation_method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_multidimensional_raster = params.get("in_multidimensional_raster")
        if in_multidimensional_raster is None:
            return {"success": False, "error": "in_multidimensional_raster parameter is required"}
        dimension = params.get("dimension")
        if dimension is None:
            return {"success": False, "error": "dimension parameter is required"}
        aggregation_method = params.get("aggregation_method")
        variables = params.get("variables")
        aggregation_def = params.get("aggregation_def")
        interval_keyword = params.get("interval_keyword")
        interval_value = params.get("interval_value")
        interval_unit = params.get("interval_unit")
        interval_ranges = params.get("interval_ranges")
        aggregation_function = params.get("aggregation_function")
        ignore_nodata = params.get("ignore_nodata")
        dimensionless = params.get("dimensionless")
        percentile_value = params.get("percentile_value")
        percentile_interpolation_type = params.get("percentile_interpolation_type")

            # Generate output name and path
            output_name = f"{in_multidimensional_raster.replace(' ', '_')}_Aggregate_Multidimensional_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Aggregate Multidimensional Raster
            arcpy.AggregateMultidimensionalRaster(in_multidimensional_raster, dimension, aggregation_method, variables, aggregation_def, interval_keyword, interval_value, interval_unit, interval_ranges, aggregation_function, ignore_nodata, dimensionless, percentile_value, percentile_interpolation_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def find_argument_statistics(self, params):
        """Find Argument Statistics

Extracts the dimension value or band index at which a given statistic is attained for each pixel in a multidimensional or multiband raster.

        params: {"in_raster": <Raster Dataset; Raster Layer; Mosaic Dataset; Mosaic Layer; Image Service; File>, "dimension": <String>, "dimension_def": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        dimension = params.get("dimension")
        dimension_def = params.get("dimension_def")
        interval_keyword = params.get("interval_keyword")
        variables = params.get("variables")
        statistics_type = params.get("statistics_type")
        min = params.get("min")
        max = params.get("max")
        multiple_occurrence = params.get("multiple_occurrence")
        ignore_nodata = params.get("ignore_nodata")
        value = params.get("value")
        comparison = params.get("comparison")
        occurrence = params.get("occurrence")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Find_Argument_Statistics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Find Argument Statistics
            arcpy.FindArgumentStatistics(in_raster, dimension, dimension_def, interval_keyword, variables, statistics_type, min, max, multiple_occurrence, ignore_nodata, value, comparison, occurrence)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_multidimensional_anomaly(self, params):
        """Generate Multidimensional Anomaly

Computes the anomaly for each slice in an existing multidimensional raster to generate a new multidimensional raster. An anomaly is the deviation of an observation from its standard or mean value.

        params: {"in_multidimensional_raster": <Raster Dataset; Raster Layer; Mosaic Dataset; Mosaic Layer; Image Service; File>, "variables": <String>, "method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_multidimensional_raster = params.get("in_multidimensional_raster")
        if in_multidimensional_raster is None:
            return {"success": False, "error": "in_multidimensional_raster parameter is required"}
        variables = params.get("variables")
        method = params.get("method")
        calculation_interval = params.get("calculation_interval")
        ignore_nodata = params.get("ignore_nodata")
        reference_mean_raster = params.get("reference_mean_raster")

            # Generate output name and path
            output_name = f"{in_multidimensional_raster.replace(' ', '_')}_Generate_Multidimensional_Anomaly"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Multidimensional Anomaly
            arcpy.GenerateMultidimensionalAnomaly(in_multidimensional_raster, variables, method, calculation_interval, ignore_nodata, reference_mean_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_trend_raster(self, params):
        """Generate Trend Raster

Estimates the trend for each pixel along a dimension for one or more variables in a multidimensional raster.

        params: {"in_multidimensional_raster": <Raster Dataset; Raster Layer; Mosaic Dataset; Mosaic Layer; Image Service; File>, "dimension": <String>, "variables": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_multidimensional_raster = params.get("in_multidimensional_raster")
        if in_multidimensional_raster is None:
            return {"success": False, "error": "in_multidimensional_raster parameter is required"}
        dimension = params.get("dimension")
        if dimension is None:
            return {"success": False, "error": "dimension parameter is required"}
        variables = params.get("variables")
        line_type = params.get("line_type")
        frequency = params.get("frequency")
        ignore_nodata = params.get("ignore_nodata")
        cycle_length = params.get("cycle_length")
        cycle_unit = params.get("cycle_unit")
        rmse = params.get("rmse")
        r2 = params.get("r2")
        slope_p_value = params.get("slope_p_value")
        seasonal_period = params.get("seasonal_period")

            # Generate output name and path
            output_name = f"{in_multidimensional_raster.replace(' ', '_')}_Generate_Trend_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Trend Raster
            arcpy.GenerateTrendRaster(in_multidimensional_raster, dimension, variables, line_type, frequency, ignore_nodata, cycle_length, cycle_unit, rmse, r2, slope_p_value, seasonal_period)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def interpolate_from_spatiotemporal_points(self, params):
        """Interpolate From Spatiotemporal Points

Interpolates temporal point data into a multidimensional raster.

        params: {"in_dataset": <Trajectory Layer; Feature Layer; Mosaic Dataset; Mosaic Layer>, "variable_field": <String>, "time_field": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        variable_field = params.get("variable_field")
        if variable_field is None:
            return {"success": False, "error": "variable_field parameter is required"}
        time_field = params.get("time_field")
        if time_field is None:
            return {"success": False, "error": "time_field parameter is required"}
        temporal_aggregation = params.get("temporal_aggregation")
        cell_size = params.get("cell_size")
        interpolation_method = params.get("interpolation_method")
        if interpolation_method is None:
            return {"success": False, "error": "interpolation_method parameter is required"}

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Interpolate_From_Spatiotemporal_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Interpolate From Spatiotemporal Points
            arcpy.InterpolateFromSpatiotemporalPoints(in_dataset, variable_field, time_field, temporal_aggregation, cell_size, interpolation_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def multidimensional_principal_components(self, params):
        """Multidimensional Principal Components

Transforms multidimensional rasters into  their principal components, loadings, and eigenvalues. The tool transforms the data into a reduced number of components that account for the variance of the data, so that spatial and temporal patterns can be readily identified.

        params: {"in_multidimensional_raster": <Raster Dataset; Mosaic Dataset; Raster Layer; Mosaic Layer; Image Service; File>, "mode": <String>, "dimension": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_multidimensional_raster = params.get("in_multidimensional_raster")
        if in_multidimensional_raster is None:
            return {"success": False, "error": "in_multidimensional_raster parameter is required"}
        mode = params.get("mode")
        if mode is None:
            return {"success": False, "error": "mode parameter is required"}
        dimension = params.get("dimension")
        if dimension is None:
            return {"success": False, "error": "dimension parameter is required"}
        out_pc = params.get("out_pc")
        if out_pc is None:
            return {"success": False, "error": "out_pc parameter is required"}
        out_loadings = params.get("out_loadings")
        if out_loadings is None:
            return {"success": False, "error": "out_loadings parameter is required"}
        out_eigenvalues = params.get("out_eigenvalues")
        variable = params.get("variable")
        number_of_pc = params.get("number_of_pc")

            # Generate output name and path
            output_name = f"{in_multidimensional_raster.replace(' ', '_')}_Multidimensional_Principal_Components"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Multidimensional Principal Components
            arcpy.MultidimensionalPrincipalComponents(in_multidimensional_raster, mode, dimension, out_pc, out_loadings, out_eigenvalues, variable, number_of_pc)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def multidimensional_raster_correlation(self, params):
        """Multidimensional Raster Correlation

Analyzes correlations between two variables in one or two multidimensional rasters. The tool takes two multidimensional rasters as input, compares two variables using the Pearson, Kendall, or Spearman correlation method, and outputs a correlation raster, with each pixel representing the correlation values of the corresponding pixel arrays. The output raster can map where the two variables are correlated and where they are not correlated. The tool can also calculate cross correlation when the lag is a nonzero value and calculate auto correlation when the two inputs are the same. You can analyze correlations between two variables in one or two multidimensional rasters.   The output is a correlation raster in which each pixel is the correlation of the two time series from the two variables.   The tool can be used to calculate correlation with a lag, a cross correlation, or an autocorrelation. For example, the correlation raster in the images below was calculated from a soil moisture variable over time and a precipitation variable over time.

        params: {"in_mdim_raster1": <Raster Dataset; Raster Layer; Mosaic Dataset; Mosaic Layer; Image Service>, "in_mdim_raster2": <Raster Dataset; Raster Layer; Mosaic Dataset; Mosaic Layer; Image Service>, "dimension1": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_mdim_raster1 = params.get("in_mdim_raster1")
        if in_mdim_raster1 is None:
            return {"success": False, "error": "in_mdim_raster1 parameter is required"}
        in_mdim_raster2 = params.get("in_mdim_raster2")
        if in_mdim_raster2 is None:
            return {"success": False, "error": "in_mdim_raster2 parameter is required"}
        dimension1 = params.get("dimension1")
        variable1 = params.get("variable1")
        dimension2 = params.get("dimension2")
        variable2 = params.get("variable2")
        corr_method = params.get("corr_method")
        lag = params.get("lag")
        calculate_xcorr = params.get("calculate_xcorr")
        calculate_pvalue = params.get("calculate_pvalue")
        out_max_corr_raster = params.get("out_max_corr_raster")

            # Generate output name and path
            output_name = f"{in_mdim_raster1.replace(' ', '_')}_Multidimensional_Raster_Correlation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Multidimensional Raster Correlation
            arcpy.MultidimensionalRasterCorrelation(in_mdim_raster1, in_mdim_raster2, dimension1, variable1, dimension2, variable2, corr_method, lag, calculate_xcorr, calculate_pvalue, out_max_corr_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def predict_using_trend_raster(self, params):
        """Predict Using Trend Raster

Computes a forecasted multidimensional raster using the output trend raster from the Generate Trend Raster tool.

        params: {"in_multidimensional_raster": <Raster Dataset; Raster Layer; Mosaic Dataset; Mosaic Layer; Image Service; File>, "variables": <String>, "dimension_def": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_multidimensional_raster = params.get("in_multidimensional_raster")
        if in_multidimensional_raster is None:
            return {"success": False, "error": "in_multidimensional_raster parameter is required"}
        variables = params.get("variables")
        dimension_def = params.get("dimension_def")
        dimension_values = params.get("dimension_values")
        start = params.get("start")
        end = params.get("end")
        interval_value = params.get("interval_value")
        interval_unit = params.get("interval_unit")

            # Generate output name and path
            output_name = f"{in_multidimensional_raster.replace(' ', '_')}_Predict_Using_Trend_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Predict Using Trend Raster
            arcpy.PredictUsingTrendRaster(in_multidimensional_raster, variables, dimension_def, dimension_values, start, end, interval_value, interval_unit)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def summarize_categorical_raster(self, params):
        """Summarize Categorical Raster

Generates a table containing the pixel count for each class, in each slice of an input categorical raster.

        params: {"in_raster": <Raster Dataset; Raster Layer; Mosaic Dataset; Mosaic Layer; Image Service; String>, "out_table": <Table>, "dimension": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}
        dimension = params.get("dimension")
        aoi = params.get("aoi")
        aoi_id_field = params.get("aoi_id_field")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Summarize_Categorical_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Summarize Categorical Raster
            arcpy.SummarizeCategoricalRaster(in_raster, out_table, dimension, aoi, aoi_id_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def weighted_sum(self, params):
        """Weighted Sum

Overlays several rasters, multiplying each by their given weight and summing them together. Learn more about how Weighted Sum works

        params: {"in_rasters": <WSTable>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rasters = params.get("in_rasters")
        if in_rasters is None:
            return {"success": False, "error": "in_rasters parameter is required"}

            # Generate output name and path
            output_name = f"{in_rasters.replace(' ', '_')}_Weighted_Sum"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Weighted Sum
            arcpy.WeightedSum(in_rasters)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def classify_raster_using_spectra(self, params):
        """Classify Raster Using Spectra

Classifies a multiband raster dataset using spectral matching techniques. The input spectral data can be provided as a point feature class or a .json file.

        params: {"in_raster": <Mosaic Layer; Raster Layer; Image Service; String; Raster Dataset; Mosaic Dataset>, "in_spectra_file": <Feature Layer; File; String>, "method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_spectra_file = params.get("in_spectra_file")
        if in_spectra_file is None:
            return {"success": False, "error": "in_spectra_file parameter is required"}
        method = params.get("method")
        if method is None:
            return {"success": False, "error": "method parameter is required"}
        thresholds = params.get("thresholds")
        out_score_raster = params.get("out_score_raster")
        out_classifier_definition = params.get("out_classifier_definition")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Classify_Raster_Using_Spectra"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Classify Raster Using Spectra
            arcpy.ClassifyRasterUsingSpectra(in_raster, in_spectra_file, method, thresholds, out_score_raster, out_classifier_definition)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def detect_image_anomalies(self, params):
        """Detect Image Anomalies

Processes a multiband or hyperspectral image and creates an anomaly score raster. An anomaly score raster is a single band raster, with values between 0 and 1.

        params: {"in_raster": <Raster Dataset; Raster Layer; Mosaic Dataset; Mosaic Layer; Image Service>, "out_raster": <Raster Dataset>, "method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        method = params.get("method")
        num_cluster = params.get("num_cluster")
        background_region = params.get("background_region")
        recompute_stats = params.get("recompute_stats")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Detect_Image_Anomalies"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Detect Image Anomalies
            arcpy.DetectImageAnomalies(in_raster, out_raster, method, num_cluster, background_region, recompute_stats)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def linear_spectral_unmixing(self, params):
        """Linear Spectral Unmixing

Performs subpixel classification and calculates the fractional abundance of different land-cover types for individual pixels.

        params: {"in_raster": <Raster Dataset; Mosaic Dataset; Mosaic Layer; Raster Layer; File; Image Service>, "in_spectral_profile_file": <File; Feature Layer; String>, "value_option": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_spectral_profile_file = params.get("in_spectral_profile_file")
        if in_spectral_profile_file is None:
            return {"success": False, "error": "in_spectral_profile_file parameter is required"}
        value_option = params.get("value_option")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Linear_Spectral_Unmixing"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Linear Spectral Unmixing
            arcpy.LinearSpectralUnmixing(in_raster, in_spectral_profile_file, value_option)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def cell_statistics(self, params):
        """Cell Statistics

Calculates a per-cell statistic from multiple rasters. The available statistics are Majority, Maximum, Mean, Median, Minimum, Minority, Percentile, Range, Standard deviation, Sum, and Variety. Learn more about how Cell Statistics works

        params: {"in_rasters_or_constantsin_raster_or_constant": <Raster Layer; Constant>, "statistics_type": <String>, "ignore_nodata": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rasters_or_constantsin_raster_or_constant = params.get("in_rasters_or_constantsin_raster_or_constant")
        if in_rasters_or_constantsin_raster_or_constant is None:
            return {"success": False, "error": "in_rasters_or_constantsin_raster_or_constant parameter is required"}
        statistics_type = params.get("statistics_type")
        ignore_nodata = params.get("ignore_nodata")
        process_as_multiband = params.get("process_as_multiband")
        percentile_value = params.get("percentile_value")
        percentile_interpolation_type = params.get("percentile_interpolation_type")

            # Generate output name and path
            output_name = f"{in_rasters_or_constantsin_raster_or_constant.replace(' ', '_')}_Cell_Statistics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Cell Statistics
            arcpy.CellStatistics(in_rasters_or_constantsin_raster_or_constant, statistics_type, ignore_nodata, process_as_multiband, percentile_value, percentile_interpolation_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def focal_statistics(self, params):
        """Focal Statistics

Calculates for each input cell location a statistic of the values within a specified neighborhood around it. Learn more about how Focal Statistics works

        params: {"in_raster": <Raster Layer>, "neighborhood": <Neighborhood>, "statistics_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        neighborhood = params.get("neighborhood")
        statistics_type = params.get("statistics_type")
        ignore_nodata = params.get("ignore_nodata")
        percentile_value = params.get("percentile_value")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Focal_Statistics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Focal Statistics
            arcpy.FocalStatistics(in_raster, neighborhood, statistics_type, ignore_nodata, percentile_value)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def zonal_statistics(self, params):
        """Zonal Statistics

Summarizes the values of a raster within the zones of another dataset. Learn more about how the zonal statistics tools work

        params: {"in_zone_data": <Raster Layer; Feature Layer>, "zone_field": <Field>, "in_value_raster": <Raster Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_zone_data = params.get("in_zone_data")
        if in_zone_data is None:
            return {"success": False, "error": "in_zone_data parameter is required"}
        zone_field = params.get("zone_field")
        if zone_field is None:
            return {"success": False, "error": "zone_field parameter is required"}
        in_value_raster = params.get("in_value_raster")
        if in_value_raster is None:
            return {"success": False, "error": "in_value_raster parameter is required"}
        statistics_type = params.get("statistics_type")
        ignore_nodata = params.get("ignore_nodata")
        process_as_multidimensional = params.get("process_as_multidimensional")
        percentile_value = params.get("percentile_value")
        percentile_interpolation_type = params.get("percentile_interpolation_type")
        circular_calculation = params.get("circular_calculation")
        circular_wrap_value = params.get("circular_wrap_value")

            # Generate output name and path
            output_name = f"{in_zone_data.replace(' ', '_')}_Zonal_Statistics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Zonal Statistics
            arcpy.ZonalStatistics(in_zone_data, zone_field, in_value_raster, statistics_type, ignore_nodata, process_as_multidimensional, percentile_value, percentile_interpolation_type, circular_calculation, circular_wrap_value)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def zonal_statistics_as_table(self, params):
        """Zonal Statistics as Table

Summarizes the values of a raster within the zones of another dataset and reports the results as a table. Learn more about how the zonal statistics tools work

        params: {"in_zone_data": <Raster Layer; Feature Layer>, "zone_field": <Field>, "in_value_raster": <Raster Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_zone_data = params.get("in_zone_data")
        if in_zone_data is None:
            return {"success": False, "error": "in_zone_data parameter is required"}
        zone_field = params.get("zone_field")
        if zone_field is None:
            return {"success": False, "error": "zone_field parameter is required"}
        in_value_raster = params.get("in_value_raster")
        if in_value_raster is None:
            return {"success": False, "error": "in_value_raster parameter is required"}
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}
        ignore_nodata = params.get("ignore_nodata")
        statistics_type = params.get("statistics_type")
        process_as_multidimensional = params.get("process_as_multidimensional")
        percentile_values = params.get("percentile_values")
        percentile_interpolation_type = params.get("percentile_interpolation_type")
        circular_calculation = params.get("circular_calculation")
        circular_wrap_value = params.get("circular_wrap_value")
        out_join_layer = params.get("out_join_layer")

            # Generate output name and path
            output_name = f"{in_zone_data.replace(' ', '_')}_Zonal_Statistics_as_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Zonal Statistics as Table
            arcpy.ZonalStatisticsasTable(in_zone_data, zone_field, in_value_raster, out_table, ignore_nodata, statistics_type, process_as_multidimensional, percentile_values, percentile_interpolation_type, circular_calculation, circular_wrap_value, out_join_layer)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_color_composite(self, params):
        """Create Color Composite

Creates a three-band raster dataset from a multiband raster dataset.

        params: {"in_raster": <Raster Dataset; Raster Layer>, "out_raster": <Raster Dataset>, "method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        method = params.get("method")
        if method is None:
            return {"success": False, "error": "method parameter is required"}
        red_expression = params.get("red_expression")
        if red_expression is None:
            return {"success": False, "error": "red_expression parameter is required"}
        green_expression = params.get("green_expression")
        if green_expression is None:
            return {"success": False, "error": "green_expression parameter is required"}
        blue_expression = params.get("blue_expression")
        if blue_expression is None:
            return {"success": False, "error": "blue_expression parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Create_Color_Composite"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Color Composite
            arcpy.CreateColorComposite(in_raster, out_raster, method, red_expression, green_expression, blue_expression)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def apply_coregistration(self, params):
        """Apply Coregistration

Resamples  the secondary single look complex (SLC) data to the reference SLC grid using a digital elevation model (DEM) and orbit state vector metadata. For Terrain Observation by Progressive Scan (TOPS) mode radar data, the tool also deramps and demodulates the secondary SLC before resampling. Once resampling is performed, the secondary radar data is reramped and remodulated.

        params: {"in_reference_radar_data": <Raster Dataset; Raster Layer>, "in_secondary_radar_data": <Raster Dataset; Raster Layer>, "out_secondary_radar_data": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_reference_radar_data = params.get("in_reference_radar_data")
        if in_reference_radar_data is None:
            return {"success": False, "error": "in_reference_radar_data parameter is required"}
        in_secondary_radar_data = params.get("in_secondary_radar_data")
        if in_secondary_radar_data is None:
            return {"success": False, "error": "in_secondary_radar_data parameter is required"}
        out_secondary_radar_data = params.get("out_secondary_radar_data")
        if out_secondary_radar_data is None:
            return {"success": False, "error": "out_secondary_radar_data parameter is required"}
        in_dem_raster = params.get("in_dem_raster")
        if in_dem_raster is None:
            return {"success": False, "error": "in_dem_raster parameter is required"}
        geoid = params.get("geoid")
        polarization_bands = params.get("polarization_bands")

            # Generate output name and path
            output_name = f"{in_reference_radar_data.replace(' ', '_')}_Apply_Coregistration"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Apply Coregistration
            arcpy.ApplyCoregistration(in_reference_radar_data, in_secondary_radar_data, out_secondary_radar_data, in_dem_raster, geoid, polarization_bands)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def apply_geometric_terrain_correction(self, params):
        """Apply Geometric Terrain Correction

Orthorectifies the input synthetic aperture radar (SAR) data using a range-Doppler backgeocoding algorithm. The range-Doppler backgeocoding approach computes the radar range and azimuth indices for every digital elevation model (DEM) grid point using the orbit state vectors.  If no DEM is provided, the tool uses the tie points included in the metadata to perform the range-Doppler terrain correction.

        params: {"in_radar_data": <Raster Dataset; Raster Layer>, "out_radar_data": <Raster Dataset>, "polarization_bands": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_radar_data = params.get("in_radar_data")
        if in_radar_data is None:
            return {"success": False, "error": "in_radar_data parameter is required"}
        out_radar_data = params.get("out_radar_data")
        if out_radar_data is None:
            return {"success": False, "error": "out_radar_data parameter is required"}
        polarization_bands = params.get("polarization_bands")
        in_dem_raster = params.get("in_dem_raster")
        geoid = params.get("geoid")

            # Generate output name and path
            output_name = f"{in_radar_data.replace(' ', '_')}_Apply_Geometric_Terrain_Correction"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Apply Geometric Terrain Correction
            arcpy.ApplyGeometricTerrainCorrection(in_radar_data, out_radar_data, polarization_bands, in_dem_raster, geoid)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def apply_orbit_correction(self, params):
        """Apply Orbit Correction

Updates the orbital information in the Sentinel-1 synthetic aperture radar (SAR) data using a more accurate orbit state vector (OSV) file. Orbit files can be downloaded from external sources using the Download Orbit File  tool.

        params: {"in_radar_data": <Raster Dataset; Raster Layer>, "in_orbit_file": <File>, "folder": <Folder>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_radar_data = params.get("in_radar_data")
        if in_radar_data is None:
            return {"success": False, "error": "in_radar_data parameter is required"}
        in_orbit_file = params.get("in_orbit_file")
        if in_orbit_file is None:
            return {"success": False, "error": "in_orbit_file parameter is required"}
        folder = params.get("folder")

            # Generate output name and path
            output_name = f"{in_radar_data.replace(' ', '_')}_Apply_Orbit_Correction"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Apply Orbit Correction
            arcpy.ApplyOrbitCorrection(in_radar_data, in_orbit_file, folder)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def apply_radiometric_calibration(self, params):
        """Apply Radiometric Calibration

Converts the input synthetic aperture radar (SAR) reflectivity into physical units of normalized backscatter by normalizing the reflectivity using a reference plane. Calibrating SAR data is necessary to obtain meaningful backscatter that can be related to the physical properties of features in the image.

        params: {"in_radar_data": <Raster Dataset; Raster Layer>, "out_radar_data": <Raster Dataset>, "polarization_bands": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_radar_data = params.get("in_radar_data")
        if in_radar_data is None:
            return {"success": False, "error": "in_radar_data parameter is required"}
        out_radar_data = params.get("out_radar_data")
        if out_radar_data is None:
            return {"success": False, "error": "out_radar_data parameter is required"}
        polarization_bands = params.get("polarization_bands")
        calibration_type = params.get("calibration_type")

            # Generate output name and path
            output_name = f"{in_radar_data.replace(' ', '_')}_Apply_Radiometric_Calibration"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Apply Radiometric Calibration
            arcpy.ApplyRadiometricCalibration(in_radar_data, out_radar_data, polarization_bands, calibration_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def apply_radiometric_terrain_flattening(self, params):
        """Apply Radiometric Terrain Flattening

Corrects the input synthetic aperture radar (SAR) data for radiometric distortions due to topography. Due to the side-looking nature of SAR sensors,

features facing the sensor appear artificially brighter and

features facing away from the sensor appear artificially

darker. Radiometric terrain flattening normalizes the backscatter

values so that value variations will be due to surface scattering

properties. Radiometric terrain flattening is necessary to

obtain meaningful backscatter that can be

related directly to the surface scattering properties of features

in a SAR image over any terrain.

        params: {"in_radar_data": <Raster Dataset; Raster Layer>, "out_radar_data": <Raster Dataset>, "in_dem_raster": <Mosaic Layer; Raster Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_radar_data = params.get("in_radar_data")
        if in_radar_data is None:
            return {"success": False, "error": "in_radar_data parameter is required"}
        out_radar_data = params.get("out_radar_data")
        if out_radar_data is None:
            return {"success": False, "error": "out_radar_data parameter is required"}
        in_dem_raster = params.get("in_dem_raster")
        if in_dem_raster is None:
            return {"success": False, "error": "in_dem_raster parameter is required"}
        geoid = params.get("geoid")
        polarization_bands = params.get("polarization_bands")
        calibration_type = params.get("calibration_type")
        out_scattering_area = params.get("out_scattering_area")
        out_geometric_distortion = params.get("out_geometric_distortion")
        out_geometric_distortion_mask = params.get("out_geometric_distortion_mask")

            # Generate output name and path
            output_name = f"{in_radar_data.replace(' ', '_')}_Apply_Radiometric_Terrain_Flattening"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Apply Radiometric Terrain Flattening
            arcpy.ApplyRadiometricTerrainFlattening(in_radar_data, out_radar_data, in_dem_raster, geoid, polarization_bands, calibration_type, out_scattering_area, out_geometric_distortion, out_geometric_distortion_mask)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compute_coherence(self, params):
        """Compute Coherence

Computes the similarity between the reference and secondary input complex radar data. The output is a coherence raster with a value range of 0 to 1 in which 0 indicates no coherence and 1 indicates perfect coherence. A value of 0.3 or above is considered a good coherence value.

        params: {"in_reference_radar_data": <Raster Dataset; Raster Layer>, "in_secondary_radar_data": <Raster Dataset; Raster Layer>, "out_radar_data": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_reference_radar_data = params.get("in_reference_radar_data")
        if in_reference_radar_data is None:
            return {"success": False, "error": "in_reference_radar_data parameter is required"}
        in_secondary_radar_data = params.get("in_secondary_radar_data")
        if in_secondary_radar_data is None:
            return {"success": False, "error": "in_secondary_radar_data parameter is required"}
        out_radar_data = params.get("out_radar_data")
        if out_radar_data is None:
            return {"success": False, "error": "out_radar_data parameter is required"}
        polarization_bands = params.get("polarization_bands")
        range_window_size = params.get("range_window_size")
        azimuth_window_size = params.get("azimuth_window_size")

            # Generate output name and path
            output_name = f"{in_reference_radar_data.replace(' ', '_')}_Compute_Coherence"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compute Coherence
            arcpy.ComputeCoherence(in_reference_radar_data, in_secondary_radar_data, out_radar_data, polarization_bands, range_window_size, azimuth_window_size)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def convert_sar_units(self, params):
        """Convert SAR Units

Converts the scaling of the input synthetic aperture radar (SAR) data. Conversions can be performed  between amplitude and intensity, between linear and decibels (dB), and between complex and intensity.

        params: {"in_radar_data": <Raster Dataset; Raster Layer>, "out_radar_data": <Raster Dataset>, "conversion_type": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_radar_data = params.get("in_radar_data")
        if in_radar_data is None:
            return {"success": False, "error": "in_radar_data parameter is required"}
        out_radar_data = params.get("out_radar_data")
        if out_radar_data is None:
            return {"success": False, "error": "out_radar_data parameter is required"}
        conversion_type = params.get("conversion_type")

            # Generate output name and path
            output_name = f"{in_radar_data.replace(' ', '_')}_Convert_SAR_Units"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Convert SAR Units
            arcpy.ConvertSARUnits(in_radar_data, out_radar_data, conversion_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def deburst(self, params):
        """Deburst

Merges the multiple bursts from the input Sentinel-1 Single Look Complex (SLC) synthetic aperture radar (SAR) data and outputs a single, seamless subswath raster.

        params: {"in_radar_data": <Raster Dataset; Raster Layer>, "out_radar_data": <Raster Dataset>, "polarization_bands": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_radar_data = params.get("in_radar_data")
        if in_radar_data is None:
            return {"success": False, "error": "in_radar_data parameter is required"}
        out_radar_data = params.get("out_radar_data")
        if out_radar_data is None:
            return {"success": False, "error": "out_radar_data parameter is required"}
        polarization_bands = params.get("polarization_bands")

            # Generate output name and path
            output_name = f"{in_radar_data.replace(' ', '_')}_Deburst"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Deburst
            arcpy.Deburst(in_radar_data, out_radar_data, polarization_bands)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def despeckle(self, params):
        """Despeckle

Corrects the input synthetic aperture radar (SAR) data for speckle,  which is a result of coherent illumination that resembles a grainy or salt and pepper effect. This tool filters out noise while retaining edges and sharp features in the SAR image. The available filters are Lee, Enhanced Lee, Refined Lee, Frost, Kuan, and Gamma MAP.

        params: {"in_radar_data": <Raster Dataset; Raster Layer>, "out_radar_data": <Raster Dataset>, "polarization_bands": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_radar_data = params.get("in_radar_data")
        if in_radar_data is None:
            return {"success": False, "error": "in_radar_data parameter is required"}
        out_radar_data = params.get("out_radar_data")
        if out_radar_data is None:
            return {"success": False, "error": "out_radar_data parameter is required"}
        polarization_bands = params.get("polarization_bands")
        filter_type = params.get("filter_type")
        filter_size = params.get("filter_size")
        noise_model = params.get("noise_model")
        noise_variance = params.get("noise_variance")
        add_noise_mean = params.get("add_noise_mean")
        mult_noise_mean = params.get("mult_noise_mean")
        number_of_looks = params.get("number_of_looks")
        damp_factor = params.get("damp_factor")

            # Generate output name and path
            output_name = f"{in_radar_data.replace(' ', '_')}_Despeckle"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Despeckle
            arcpy.Despeckle(in_radar_data, out_radar_data, polarization_bands, filter_type, filter_size, noise_model, noise_variance, add_noise_mean, mult_noise_mean, number_of_looks, damp_factor)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def download_orbit_file(self, params):
        """Download Orbit File

Downloads the updated orbit  files for Sentinel-1 synthetic aperture radar (SAR) data. This tool uses the orbit type to make a call to the orbit website. Using the SAR metadata, it identifies the appropriate orbit state vector (OSV) file and downloads it to the input SAR data directory. Three types of OSVs are available for a Sentinel-1 product: predicted, restituted, and precise. Predicted OSVs are provided with the Sentinel-1 Level 1 ground range detected (GRD)

and single look complex (SLC)

 auxiliary products. Restituted OSVs are available through the European Space Agency (ESA) within 3 hours of image acquisition. Precise OSVs are available through ESA within 3 weeks of image acquisition. Sentinel-1 OSV files are downloaded from the Copernicus Data Space Ecosystem.

        params: {"in_radar_data": <Raster Dataset; Raster Layer>, "orbit_type": <String>, "username": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_radar_data = params.get("in_radar_data")
        if in_radar_data is None:
            return {"success": False, "error": "in_radar_data parameter is required"}
        orbit_type = params.get("orbit_type")
        username = params.get("username")
        password = params.get("password")
        cloud_storage = params.get("cloud_storage")
        folder = params.get("folder")

            # Generate output name and path
            output_name = f"{in_radar_data.replace(' ', '_')}_Download_Orbit_File"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Download Orbit File
            arcpy.DownloadOrbitFile(in_radar_data, orbit_type, username, password, cloud_storage, folder)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_radiometric_terrain_corrected_data(self, params):
        """Generate Radiometric Terrain Corrected Data

Transforms Level 1 synthetic aperture radar (SAR) data to a radiometric terrain-corrected (RTC) dataset. Use the RTC data for analysis and visualization. This tool creates a SAR output that removes unwanted noise and distortions by applying the appropriate RTC workflow according to the input SAR sensor, mode, and product type.

        params: {"in_radar_data": <Raster Dataset; Raster Layer>, "out_radar_data": <Raster Dataset>, "in_dem_raster": <Raster Dataset; Raster Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_radar_data = params.get("in_radar_data")
        if in_radar_data is None:
            return {"success": False, "error": "in_radar_data parameter is required"}
        out_radar_data = params.get("out_radar_data")
        if out_radar_data is None:
            return {"success": False, "error": "out_radar_data parameter is required"}
        in_dem_raster = params.get("in_dem_raster")
        if in_dem_raster is None:
            return {"success": False, "error": "in_dem_raster parameter is required"}
        geoid = params.get("geoid")
        polarization_bands = params.get("polarization_bands")
        output_units = params.get("output_units")
        processing_level = params.get("processing_level")
        out_folder = params.get("out_folder")

            # Generate output name and path
            output_name = f"{in_radar_data.replace(' ', '_')}_Generate_Radiometric_Terrain_Corrected_Data"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Radiometric Terrain Corrected Data
            arcpy.GenerateRadiometricTerrainCorrectedData(in_radar_data, out_radar_data, in_dem_raster, geoid, polarization_bands, output_units, processing_level, out_folder)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def multilook(self, params):
        """Multilook

Averages the input synthetic aperture radar (SAR) data  by looks in range and azimuth to approximate square pixels, mitigates speckle, and reduces SAR tool processing time.

        params: {"in_radar_data": <Raster Dataset; Raster Layer>, "out_radar_data": <Raster Dataset>, "polarization_bands": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_radar_data = params.get("in_radar_data")
        if in_radar_data is None:
            return {"success": False, "error": "in_radar_data parameter is required"}
        out_radar_data = params.get("out_radar_data")
        if out_radar_data is None:
            return {"success": False, "error": "out_radar_data parameter is required"}
        polarization_bands = params.get("polarization_bands")
        range_looks = params.get("range_looks")
        azimuth_looks = params.get("azimuth_looks")

            # Generate output name and path
            output_name = f"{in_radar_data.replace(' ', '_')}_Multilook"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Multilook
            arcpy.Multilook(in_radar_data, out_radar_data, polarization_bands, range_looks, azimuth_looks)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def remove_thermal_noise(self, params):
        """Remove Thermal Noise

Corrects backscatter disturbances caused by thermal noise in the input synthetic aperture radar (SAR) data, resulting in a more seamless image.

        params: {"in_radar_data": <Raster Dataset; Raster Layer>, "out_radar_data": <Raster Dataset>, "polarization_bands": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_radar_data = params.get("in_radar_data")
        if in_radar_data is None:
            return {"success": False, "error": "in_radar_data parameter is required"}
        out_radar_data = params.get("out_radar_data")
        if out_radar_data is None:
            return {"success": False, "error": "out_radar_data parameter is required"}
        polarization_bands = params.get("polarization_bands")

            # Generate output name and path
            output_name = f"{in_radar_data.replace(' ', '_')}_Remove_Thermal_Noise"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Remove Thermal Noise
            arcpy.RemoveThermalNoise(in_radar_data, out_radar_data, polarization_bands)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compute_sar_indices(self, params):
        """Compute SAR Indices

Computes various SAR indices for synthetic aperture radar (SAR) data, such as 

Radar Vegetation Index (RVI), Radar Forest Degradation Index (RFDI), and Canopy Structure Index (CSI). The formulas used for these indices depend on the polarizations available in the input radar dataset.

        params: {"in_radar_data": <Raster Dataset; Raster Layer>, "out_raster": <Raster Dataset>, "index": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_radar_data = params.get("in_radar_data")
        if in_radar_data is None:
            return {"success": False, "error": "in_radar_data parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        index = params.get("index")
        polarization_bands = params.get("polarization_bands")

            # Generate output name and path
            output_name = f"{in_radar_data.replace(' ', '_')}_Compute_SAR_Indices"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compute SAR Indices
            arcpy.ComputeSARIndices(in_radar_data, out_raster, index, polarization_bands)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def detect_bright_ocean_objects(self, params):
        """Detect Bright Ocean Objects

Detects potential bright human-made objects—such as ships, oil rigs, and windmills—while masking out the synthetic aperture radar (SAR) data outside the region of interest. The tool clusters pixels and filters the clusters by the minimum and maximum width and length parameters, and outputs the results to a feature class. The output feature class can be specified as  a bounding box or a perimeter around the polygon for the detected objects.

        params: {"in_radar_data": <Raster Dataset; Raster Layer>, "out_feature_class": <Feature Class>, "out_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_radar_data = params.get("in_radar_data")
        if in_radar_data is None:
            return {"success": False, "error": "in_radar_data parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        out_type = params.get("out_type")
        min_object_width = params.get("min_object_width")
        max_object_width = params.get("max_object_width")
        min_object_length = params.get("min_object_length")
        max_object_length = params.get("max_object_length")
        mask_features = params.get("mask_features")
        feature_type = params.get("feature_type")
        in_dem_raster = params.get("in_dem_raster")
        geoid = params.get("geoid")
        mask_tolerance = params.get("mask_tolerance")

            # Generate output name and path
            output_name = f"{in_radar_data.replace(' ', '_')}_Detect_Bright_Ocean_Objects"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Detect Bright Ocean Objects
            arcpy.DetectBrightOceanObjects(in_radar_data, out_feature_class, out_type, min_object_width, max_object_width, min_object_length, max_object_length, mask_features, feature_type, in_dem_raster, geoid, mask_tolerance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def detect_dark_ocean_areas(self, params):
        """Detect Dark Ocean Areas

Identifies potential dark pixels belonging to oil spills or algae, and clusters these pixels, while masking out the synthetic aperture radar (SAR) data outside the region of interest. The tool filters clusters using the Minimum Area parameter, and creates the result as a binary raster. A value of 1 corresponds to dark areas detected and is symbolized in a random color. A value of 0 indicates that no dark areas were detected and is symbolized with full transparency. Both orthorectified and nonorthorectified radar data are valid inputs. Nonorthorectified radar data results in improved azimuth artifact filtering, since the data is in radar coordinates.

        params: {"in_radar_data": <Raster Dataset; Raster Layer>, "out_raster": <Raster Dataset>, "min_area": <Areal Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_radar_data = params.get("in_radar_data")
        if in_radar_data is None:
            return {"success": False, "error": "in_radar_data parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        min_area = params.get("min_area")
        mask_features = params.get("mask_features")
        feature_type = params.get("feature_type")
        in_dem_raster = params.get("in_dem_raster")
        geoid = params.get("geoid")
        mask_tolerance = params.get("mask_tolerance")

            # Generate output name and path
            output_name = f"{in_radar_data.replace(' ', '_')}_Detect_Dark_Ocean_Areas"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Detect Dark Ocean Areas
            arcpy.DetectDarkOceanAreas(in_radar_data, out_raster, min_area, mask_features, feature_type, in_dem_raster, geoid, mask_tolerance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_water(self, params):
        """Extract Water

Finds water bodies using input synthetic aperture radar (SAR) data and a digital elevation model (DEM). The tool uses the input radar backscatter to determine whether pixels should be classified as water; then creates polygons for water areas. The tool will also create polygons for areas that are not water, which will be considered land areas.

        params: {"in_radar_data": <Raster Dataset; Raster Layer>, "out_feature_class": <Feature Class>, "min_area": <Areal Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_radar_data = params.get("in_radar_data")
        if in_radar_data is None:
            return {"success": False, "error": "in_radar_data parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        min_area = params.get("min_area")
        in_dem_raster = params.get("in_dem_raster")
        geoid = params.get("geoid")

            # Generate output name and path
            output_name = f"{in_radar_data.replace(' ', '_')}_Extract_Water"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract Water
            arcpy.ExtractWater(in_radar_data, out_feature_class, min_area, in_dem_raster, geoid)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_binary_mask(self, params):
        """Create Binary Mask

Converts an input raster dataset to a binary raster. Pixels are labeled as either mask or background based on user-defined values.

        params: {"in_raster": <Mosaic Layer; Raster Layer; Image Service; String; Raster Dataset; Mosaic Dataset>, "out_raster": <Raster Dataset>, "background_value": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        background_value = params.get("background_value")
        flood_fill = params.get("flood_fill")
        expand_background = params.get("expand_background")
        expand_mask = params.get("expand_mask")
        min_region_size = params.get("min_region_size")
        background_nodata = params.get("background_nodata")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Create_Binary_Mask"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Binary Mask
            arcpy.CreateBinaryMask(in_raster, out_raster, background_value, flood_fill, expand_background, expand_mask, min_region_size, background_nodata)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}
