# Generated ArcGIS Pro spatial-statistics Progent Functions
# Generated on 2025-10-01T15:21:07.919406
# Total tools: 69

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

    def incremental_spatial_autocorrelation(self, params):
        """Incremental Spatial Autocorrelation

Measures spatial autocorrelation for a series of distances and optionally creates a line graph of those distances and their corresponding z-scores.  Z-scores reflect the intensity of spatial clustering, and statistically significant peak z-scores indicate distances where spatial processes promoting clustering are most pronounced.  These peak distances are often appropriate values to use for tools with a Distance Band or Distance Radius parameter.

        params: {"input_features": <Feature Layer>, "input_field": <Field>, "number_of_distance_bands": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_features = params.get("input_features")
        if input_features is None:
            return {"success": False, "error": "input_features parameter is required"}
        input_field = params.get("input_field")
        if input_field is None:
            return {"success": False, "error": "input_field parameter is required"}
        number_of_distance_bands = params.get("number_of_distance_bands")
        if number_of_distance_bands is None:
            return {"success": False, "error": "number_of_distance_bands parameter is required"}
        beginning_distance = params.get("beginning_distance")
        distance_increment = params.get("distance_increment")
        distance_method = params.get("distance_method")
        row_standardization = params.get("row_standardization")
        output_table = params.get("output_table")
        output_report_file = params.get("output_report_file")

            # Generate output name and path
            output_name = f"{input_features.replace(' ', '_')}_Incremental_Spatial_Autocorrelation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Incremental Spatial Autocorrelation
            arcpy.IncrementalSpatialAutocorrelation(input_features, input_field, number_of_distance_bands, beginning_distance, distance_increment, distance_method, row_standardization, output_table, output_report_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def hot_spot_analysis(self, params):
        """Hot Spot Analysis

Given a set of weighted features, identifies statistically significant hot spots and cold spots using the Getis-Ord Gi* statistic. Learn more about how Hot Spot Analysis (Getis-Ord Gi*) works

        params: {"input_feature_class": <Feature Layer>, "input_field": <Field>, "output_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        input_field = params.get("input_field")
        if input_field is None:
            return {"success": False, "error": "input_field parameter is required"}
        output_feature_class = params.get("output_feature_class")
        if output_feature_class is None:
            return {"success": False, "error": "output_feature_class parameter is required"}
        conceptualization_of_spatial_relationships = params.get("conceptualization_of_spatial_relationships")
        if conceptualization_of_spatial_relationships is None:
            return {"success": False, "error": "conceptualization_of_spatial_relationships parameter is required"}
        distance_method = params.get("distance_method")
        if distance_method is None:
            return {"success": False, "error": "distance_method parameter is required"}
        standardization = params.get("standardization")
        if standardization is None:
            return {"success": False, "error": "standardization parameter is required"}
        distance_band_or_threshold_distance = params.get("distance_band_or_threshold_distance")
        self_potential_field = params.get("self_potential_field")
        weights_matrix_file = params.get("weights_matrix_file")
        apply_false_discovery_rate_fdr_correction = params.get("apply_false_discovery_rate_fdr_correction")
        number_of_neighbors = params.get("number_of_neighbors")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Hot_Spot_Analysis"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Hot Spot Analysis
            arcpy.HotSpotAnalysis(input_feature_class, input_field, output_feature_class, conceptualization_of_spatial_relationships, distance_method, standardization, distance_band_or_threshold_distance, self_potential_field, weights_matrix_file, apply_false_discovery_rate_fdr_correction, number_of_neighbors)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def average_nearest_neighbor(self, params):
        """Average Nearest Neighbor

Calculates a nearest neighbor index based on the average distance from each feature to its nearest neighboring feature. Learn more about how Average Nearest Neighbor Distance works

        params: {"input_feature_class": <Feature Layer>, "distance_method": <String>, "generate_report": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        distance_method = params.get("distance_method")
        if distance_method is None:
            return {"success": False, "error": "distance_method parameter is required"}
        generate_report = params.get("generate_report")
        area = params.get("area")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Average_Nearest_Neighbor"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Average Nearest Neighbor
            arcpy.AverageNearestNeighbor(input_feature_class, distance_method, generate_report, area)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def high/low_clustering(self, params):
        """High/Low Clustering

Measures the degree of clustering for either high or low values using the Getis-Ord General G statistic. Learn more about how High/Low Clustering: Getis-Ord General G works

        params: {"input_feature_class": <Feature Layer>, "input_field": <Field>, "generate_report": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        input_field = params.get("input_field")
        if input_field is None:
            return {"success": False, "error": "input_field parameter is required"}
        generate_report = params.get("generate_report")
        conceptualization_of_spatial_relationships = params.get("conceptualization_of_spatial_relationships")
        if conceptualization_of_spatial_relationships is None:
            return {"success": False, "error": "conceptualization_of_spatial_relationships parameter is required"}
        distance_method = params.get("distance_method")
        if distance_method is None:
            return {"success": False, "error": "distance_method parameter is required"}
        standardization = params.get("standardization")
        if standardization is None:
            return {"success": False, "error": "standardization parameter is required"}
        distance_band_or_threshold_distance = params.get("distance_band_or_threshold_distance")
        weights_matrix_file = params.get("weights_matrix_file")
        number_of_neighbors = params.get("number_of_neighbors")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_High/Low_Clustering"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute High/Low Clustering
            arcpy.High/LowClustering(input_feature_class, input_field, generate_report, conceptualization_of_spatial_relationships, distance_method, standardization, distance_band_or_threshold_distance, weights_matrix_file, number_of_neighbors)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def multi_distance_spatial_cluster_analysis_(ripley's_k_function)(self, params):
        """Multi-Distance Spatial Cluster Analysis (Ripley's k-function)

Determines whether features, or the values associated with features, exhibit statistically significant clustering or dispersion over a range of distances. Learn more about how Multi-Distance Spatial Cluster Analysis works

        params: {"input_feature_class": <Feature Layer>, "output_table": <Table>, "number_of_distance_bands": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        output_table = params.get("output_table")
        if output_table is None:
            return {"success": False, "error": "output_table parameter is required"}
        number_of_distance_bands = params.get("number_of_distance_bands")
        if number_of_distance_bands is None:
            return {"success": False, "error": "number_of_distance_bands parameter is required"}
        compute_confidence_envelope = params.get("compute_confidence_envelope")
        display_results_graphically = params.get("display_results_graphically")
        weight_field = params.get("weight_field")
        beginning_distance = params.get("beginning_distance")
        distance_increment = params.get("distance_increment")
        boundary_correction_method = params.get("boundary_correction_method")
        study_area_method = params.get("study_area_method")
        study_area_feature_class = params.get("study_area_feature_class")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Multi-Distance_Spatial_Cluster_Analysis_(Ripley's_k-function)"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Multi-Distance Spatial Cluster Analysis (Ripley's k-function)
            arcpy.MultiDistanceSpatialClusterAnalysis(Ripley'skfunction)(input_feature_class, output_table, number_of_distance_bands, compute_confidence_envelope, display_results_graphically, weight_field, beginning_distance, distance_increment, boundary_correction_method, study_area_method, study_area_feature_class)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def spatial_autocorrelation(self, params):
        """Spatial Autocorrelation

Measures spatial autocorrelation based on feature locations and attribute values using the Global Moran's I statistic. Learn more about how Spatial Autocorrelation (Global Moran's I) works

        params: {"input_feature_class": <Feature Layer>, "input_field": <Field>, "generate_report": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        input_field = params.get("input_field")
        if input_field is None:
            return {"success": False, "error": "input_field parameter is required"}
        generate_report = params.get("generate_report")
        conceptualization_of_spatial_relationships = params.get("conceptualization_of_spatial_relationships")
        if conceptualization_of_spatial_relationships is None:
            return {"success": False, "error": "conceptualization_of_spatial_relationships parameter is required"}
        distance_method = params.get("distance_method")
        if distance_method is None:
            return {"success": False, "error": "distance_method parameter is required"}
        standardization = params.get("standardization")
        if standardization is None:
            return {"success": False, "error": "standardization parameter is required"}
        distance_band_or_threshold_distance = params.get("distance_band_or_threshold_distance")
        weights_matrix_file = params.get("weights_matrix_file")
        number_of_neighbors = params.get("number_of_neighbors")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Spatial_Autocorrelation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Spatial Autocorrelation
            arcpy.SpatialAutocorrelation(input_feature_class, input_field, generate_report, conceptualization_of_spatial_relationships, distance_method, standardization, distance_band_or_threshold_distance, weights_matrix_file, number_of_neighbors)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def hot_spot_analysis_(getis_ord_gi*)(self, params):
        """Hot Spot Analysis (Getis-Ord Gi*)

Given a set of weighted features, identifies statistically significant hot spots and cold spots using the Getis-Ord Gi* statistic. Learn more about how Hot Spot Analysis (Getis-Ord Gi*) works

        params: {"input_feature_class": <Feature Layer>, "input_field": <Field>, "output_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        input_field = params.get("input_field")
        if input_field is None:
            return {"success": False, "error": "input_field parameter is required"}
        output_feature_class = params.get("output_feature_class")
        if output_feature_class is None:
            return {"success": False, "error": "output_feature_class parameter is required"}
        conceptualization_of_spatial_relationships = params.get("conceptualization_of_spatial_relationships")
        if conceptualization_of_spatial_relationships is None:
            return {"success": False, "error": "conceptualization_of_spatial_relationships parameter is required"}
        distance_method = params.get("distance_method")
        if distance_method is None:
            return {"success": False, "error": "distance_method parameter is required"}
        standardization = params.get("standardization")
        if standardization is None:
            return {"success": False, "error": "standardization parameter is required"}
        distance_band_or_threshold_distance = params.get("distance_band_or_threshold_distance")
        self_potential_field = params.get("self_potential_field")
        weights_matrix_file = params.get("weights_matrix_file")
        apply_false_discovery_rate_fdr_correction = params.get("apply_false_discovery_rate_fdr_correction")
        number_of_neighbors = params.get("number_of_neighbors")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Hot_Spot_Analysis_(Getis-Ord_Gi*)"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Hot Spot Analysis (Getis-Ord Gi*)
            arcpy.HotSpotAnalysis(GetisOrdGi*)(input_feature_class, input_field, output_feature_class, conceptualization_of_spatial_relationships, distance_method, standardization, distance_band_or_threshold_distance, self_potential_field, weights_matrix_file, apply_false_discovery_rate_fdr_correction, number_of_neighbors)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def optimized_hot_spot_analysis(self, params):
        """Optimized Hot Spot Analysis

Creates a map of statistically significant hot and cold spots using the Getis-Ord Gi* statistic, given incident points or weighted features (points or polygons). The tool evaluates the characteristics of the input feature class to produce optimal results. Learn more about how Optimized Hot Spot Analysis works

        params: {"input_features": <Feature Layer>, "output_features": <Feature Class>, "analysis_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_features = params.get("input_features")
        if input_features is None:
            return {"success": False, "error": "input_features parameter is required"}
        output_features = params.get("output_features")
        if output_features is None:
            return {"success": False, "error": "output_features parameter is required"}
        analysis_field = params.get("analysis_field")
        incident_data_aggregation_method = params.get("incident_data_aggregation_method")
        bounding_polygons_defining_where_incidents_are_possible = params.get("bounding_polygons_defining_where_incidents_are_possible")
        polygons_for_aggregating_incidents_into_counts = params.get("polygons_for_aggregating_incidents_into_counts")
        density_surface = params.get("density_surface")
        cell_size = params.get("cell_size")
        distance_band = params.get("distance_band")

            # Generate output name and path
            output_name = f"{input_features.replace(' ', '_')}_Optimized_Hot_Spot_Analysis"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Optimized Hot Spot Analysis
            arcpy.OptimizedHotSpotAnalysis(input_features, output_features, analysis_field, incident_data_aggregation_method, bounding_polygons_defining_where_incidents_are_possible, polygons_for_aggregating_incidents_into_counts, density_surface, cell_size, distance_band)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def cluster_and_outlier_analysis_(anselin_local_moran's_i)(self, params):
        """Cluster and Outlier Analysis (Anselin Local Moran's I)

Identifies statistically significant hot spots, cold spots, and spatial outliers using the Anselin Local Moran's I statistic, given a set of weighted features. Learn more about how Cluster and Outlier Analysis (Anselin Local Moran's I) works

        params: {"input_feature_class": <Feature Layer>, "input_field": <Field>, "output_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        input_field = params.get("input_field")
        if input_field is None:
            return {"success": False, "error": "input_field parameter is required"}
        output_feature_class = params.get("output_feature_class")
        if output_feature_class is None:
            return {"success": False, "error": "output_feature_class parameter is required"}
        conceptualization_of_spatial_relationships = params.get("conceptualization_of_spatial_relationships")
        if conceptualization_of_spatial_relationships is None:
            return {"success": False, "error": "conceptualization_of_spatial_relationships parameter is required"}
        distance_method = params.get("distance_method")
        if distance_method is None:
            return {"success": False, "error": "distance_method parameter is required"}
        standardization = params.get("standardization")
        if standardization is None:
            return {"success": False, "error": "standardization parameter is required"}
        distance_band_or_threshold_distance = params.get("distance_band_or_threshold_distance")
        weights_matrix_file = params.get("weights_matrix_file")
        apply_false_discovery_rate_fdr_correction = params.get("apply_false_discovery_rate_fdr_correction")
        number_of_permutations = params.get("number_of_permutations")
        number_of_neighbors = params.get("number_of_neighbors")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Cluster_and_Outlier_Analysis_(Anselin_Local_Moran's_I)"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Cluster and Outlier Analysis (Anselin Local Moran's I)
            arcpy.ClusterandOutlierAnalysis(AnselinLocalMoran'sI)(input_feature_class, input_field, output_feature_class, conceptualization_of_spatial_relationships, distance_method, standardization, distance_band_or_threshold_distance, weights_matrix_file, apply_false_discovery_rate_fdr_correction, number_of_permutations, number_of_neighbors)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def optimized_outlier_analysis(self, params):
        """Optimized Outlier Analysis

Given incident points or weighted features (points or polygons), creates a map of statistically significant hot spots, cold spots, and spatial outliers using the Anselin Local Moran's I statistic. It evaluates the characteristics of the input feature class to produce optimal results. Learn more about how Optimized Outlier Analysis works

        params: {"input_features": <Feature Layer>, "output_features": <Feature Class>, "analysis_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_features = params.get("input_features")
        if input_features is None:
            return {"success": False, "error": "input_features parameter is required"}
        output_features = params.get("output_features")
        if output_features is None:
            return {"success": False, "error": "output_features parameter is required"}
        analysis_field = params.get("analysis_field")
        incident_data_aggregation_method = params.get("incident_data_aggregation_method")
        bounding_polygons_defining_where_incidents_are_possible = params.get("bounding_polygons_defining_where_incidents_are_possible")
        polygons_for_aggregating_incidents_into_counts = params.get("polygons_for_aggregating_incidents_into_counts")
        performance_adjustment = params.get("performance_adjustment")
        cell_size = params.get("cell_size")
        distance_band = params.get("distance_band")

            # Generate output name and path
            output_name = f"{input_features.replace(' ', '_')}_Optimized_Outlier_Analysis"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Optimized Outlier Analysis
            arcpy.OptimizedOutlierAnalysis(input_features, output_features, analysis_field, incident_data_aggregation_method, bounding_polygons_defining_where_incidents_are_possible, polygons_for_aggregating_incidents_into_counts, performance_adjustment, cell_size, distance_band)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generalized_linear_regression(self, params):
        """Generalized Linear Regression

Performs generalized linear regression (GLR) to generate predictions or to model a dependent variable in terms of its relationship to a set of explanatory variables.  This tool can be used to fit continuous (OLS), binary (logistic), and count (Poisson) models. Learn more about how Generalized Linear Regression works

        params: {"in_features": <Feature Layer>, "dependent_variable": <Field>, "model_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        dependent_variable = params.get("dependent_variable")
        if dependent_variable is None:
            return {"success": False, "error": "dependent_variable parameter is required"}
        model_type = params.get("model_type")
        if model_type is None:
            return {"success": False, "error": "model_type parameter is required"}
        output_features = params.get("output_features")
        if output_features is None:
            return {"success": False, "error": "output_features parameter is required"}
        explanatory_variables = params.get("explanatory_variables")
        if explanatory_variables is None:
            return {"success": False, "error": "explanatory_variables parameter is required"}
        distance_features = params.get("distance_features")
        prediction_locations = params.get("prediction_locations")
        explanatory_variables_to_matchfield_from_prediction_locations_field_from_input_features = params.get("explanatory_variables_to_matchfield_from_prediction_locations_field_from_input_features")
        explanatory_distance_matchingprediction_distance_features_input_explanatory_distance_features = params.get("explanatory_distance_matchingprediction_distance_features_input_explanatory_distance_features")
        output_predicted_features = params.get("output_predicted_features")
        output_trained_model = params.get("output_trained_model")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Generalized_Linear_Regression"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generalized Linear Regression
            arcpy.GeneralizedLinearRegression(in_features, dependent_variable, model_type, output_features, explanatory_variables, distance_features, prediction_locations, explanatory_variables_to_matchfield_from_prediction_locations_field_from_input_features, explanatory_distance_matchingprediction_distance_features_input_explanatory_distance_features, output_predicted_features, output_trained_model)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def spatial_autocorrelation_(global_moran's_i)(self, params):
        """Spatial Autocorrelation (Global Moran's I)

Measures spatial autocorrelation based on feature locations and attribute values using the Global Moran's I statistic. Learn more about how Spatial Autocorrelation (Global Moran's I) works

        params: {"input_feature_class": <Feature Layer>, "input_field": <Field>, "generate_report": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        input_field = params.get("input_field")
        if input_field is None:
            return {"success": False, "error": "input_field parameter is required"}
        generate_report = params.get("generate_report")
        conceptualization_of_spatial_relationships = params.get("conceptualization_of_spatial_relationships")
        if conceptualization_of_spatial_relationships is None:
            return {"success": False, "error": "conceptualization_of_spatial_relationships parameter is required"}
        distance_method = params.get("distance_method")
        if distance_method is None:
            return {"success": False, "error": "distance_method parameter is required"}
        standardization = params.get("standardization")
        if standardization is None:
            return {"success": False, "error": "standardization parameter is required"}
        distance_band_or_threshold_distance = params.get("distance_band_or_threshold_distance")
        weights_matrix_file = params.get("weights_matrix_file")
        number_of_neighbors = params.get("number_of_neighbors")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Spatial_Autocorrelation_(Global_Moran's_I)"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Spatial Autocorrelation (Global Moran's I)
            arcpy.SpatialAutocorrelation(GlobalMoran'sI)(input_feature_class, input_field, generate_report, conceptualization_of_spatial_relationships, distance_method, standardization, distance_band_or_threshold_distance, weights_matrix_file, number_of_neighbors)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_composite_index(self, params):
        """Calculate Composite Index

Combines multiple numeric variables to create a single index. Composite indices are used across social and environmental domains to represent complex information from multiple indicators as a single metric that can measure progress toward a goal and facilitate decisions. The tool supports the three main steps of the index creation process: standardize input variables to a common scale (preprocessing), combine variables to a single index variable (combination), and scale and classify the resulting index to meaningful values (postprocessing). Learn more about how Calculate Composite Index works

        params: {"in_table": <Table View>, "in_variablesvar1_reverse1_var2_reverse2": <Value Table>, "append_to_input": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        in_variablesvar1_reverse1_var2_reverse2 = params.get("in_variablesvar1_reverse1_var2_reverse2")
        if in_variablesvar1_reverse1_var2_reverse2 is None:
            return {"success": False, "error": "in_variablesvar1_reverse1_var2_reverse2 parameter is required"}
        append_to_input = params.get("append_to_input")
        out_table = params.get("out_table")
        index_preset = params.get("index_preset")
        preprocessing = params.get("preprocessing")
        pre_threshold_scaling = params.get("pre_threshold_scaling")
        pre_custom_zscorefield1_mean1_stdev1_field2_mean2_stdev2 = params.get("pre_custom_zscorefield1_mean1_stdev1_field2_mean2_stdev2")
        pre_min_maxfield1_min1_max1_field2_min2_max2 = params.get("pre_min_maxfield1_min1_max1_field2_min2_max2")
        pre_thresholdsfield1_method1_threshold1_field2_method2_threshold2 = params.get("pre_thresholdsfield1_method1_threshold1_field2_method2_threshold2")
        index_method = params.get("index_method")
        index_weightsfield1_weight1_field2_weight2 = params.get("index_weightsfield1_weight1_field2_weight2")
        out_index_name = params.get("out_index_name")
        out_index_reverse = params.get("out_index_reverse")
        post_min_max = params.get("post_min_max")
        post_reclass = params.get("post_reclass")
        post_num_classes = params.get("post_num_classes")
        post_custom_classesmin1_max1_min2_max2 = params.get("post_custom_classesmin1_max1_min2_max2")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Calculate_Composite_Index"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Composite Index
            arcpy.CalculateCompositeIndex(in_table, in_variablesvar1_reverse1_var2_reverse2, append_to_input, out_table, index_preset, preprocessing, pre_threshold_scaling, pre_custom_zscorefield1_mean1_stdev1_field2_mean2_stdev2, pre_min_maxfield1_min1_max1_field2_min2_max2, pre_thresholdsfield1_method1_threshold1_field2_method2_threshold2, index_method, index_weightsfield1_weight1_field2_weight2, out_index_name, out_index_reverse, post_min_max, post_reclass, post_num_classes, post_custom_classesmin1_max1_min2_max2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def assess_sensitivity_to_attribute_uncertainty(self, params):
        """Assess Sensitivity to Attribute Uncertainty

Measures the stability of an analysis result by comparing the original analysis output to the results from multiple tool runs using simulated data. The simulated data accounts for uncertainty in one or more analysis variables. Three types of attribute uncertainty are supported: margin of error, confidence bounds, and a percentage of the original attribute value. Learn more about how Assess Sensitivity to Attribute Uncertainty Works

        params: {"in_features": <Feature Layer>, "out_features": <Feature Class>, "out_simulation_table": <Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_features = params.get("out_features")
        if out_features is None:
            return {"success": False, "error": "out_features parameter is required"}
        out_simulation_table = params.get("out_simulation_table")
        if out_simulation_table is None:
            return {"success": False, "error": "out_simulation_table parameter is required"}
        analysis_input_features = params.get("analysis_input_features")
        uncertainty_measure = params.get("uncertainty_measure")
        moe_field = params.get("moe_field")
        confidence_bound_field = params.get("confidence_bound_field")
        randomize_pct = params.get("randomize_pct")
        num_simulations = params.get("num_simulations")
        simulation_method = params.get("simulation_method")
        output_workspace = params.get("output_workspace")
        sim_data_limits = params.get("sim_data_limits")
        moe_conf_level = params.get("moe_conf_level")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Assess_Sensitivity_to_Attribute_Uncertainty"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Assess Sensitivity to Attribute Uncertainty
            arcpy.AssessSensitivitytoAttributeUncertainty(in_features, out_features, out_simulation_table, analysis_input_features, uncertainty_measure, moe_field, confidence_bound_field, randomize_pct, num_simulations, simulation_method, output_workspace, sim_data_limits, moe_conf_level)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def build_balanced_zones(self, params):
        """Build Balanced Zones

Creates spatially contiguous zones in a study area using a genetic growth algorithm based on specified criteria. You can create zones that contain an equal number of features, zones that are similar based on a set of attribute values, or both. You can also select zones with approximately equal areas, that are as compact as possible, and that maintain consistent summary statistics of other variables. Learn more about how Build Balanced Zones works

        params: {"in_features": <Feature Layer>, "output_features": <Feature Class>, "zone_creation_method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        output_features = params.get("output_features")
        if output_features is None:
            return {"success": False, "error": "output_features parameter is required"}
        zone_creation_method = params.get("zone_creation_method")
        if zone_creation_method is None:
            return {"success": False, "error": "zone_creation_method parameter is required"}
        number_of_zones = params.get("number_of_zones")
        zone_building_criteria_targetvariable_sum_weight = params.get("zone_building_criteria_targetvariable_sum_weight")
        zone_building_criteriavariable_weight = params.get("zone_building_criteriavariable_weight")
        spatial_constraints = params.get("spatial_constraints")
        weights_matrix_file = params.get("weights_matrix_file")
        zone_characteristics = params.get("zone_characteristics")
        attribute_to_considervariable_function = params.get("attribute_to_considervariable_function")
        distance_to_consider = params.get("distance_to_consider")
        categorial_variable = params.get("categorial_variable")
        proportion_method = params.get("proportion_method")
        population_size = params.get("population_size")
        number_generations = params.get("number_generations")
        mutation_factor = params.get("mutation_factor")
        output_convergence_table = params.get("output_convergence_table")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Build_Balanced_Zones"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Build Balanced Zones
            arcpy.BuildBalancedZones(in_features, output_features, zone_creation_method, number_of_zones, zone_building_criteria_targetvariable_sum_weight, zone_building_criteriavariable_weight, spatial_constraints, weights_matrix_file, zone_characteristics, attribute_to_considervariable_function, distance_to_consider, categorial_variable, proportion_method, population_size, number_generations, mutation_factor, output_convergence_table)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_composite_index(self, params):
        """Calculate Composite Index

Combines multiple numeric variables to create a single index. Composite indices are used across social and environmental domains to represent complex information from multiple indicators as a single metric that can measure progress toward a goal and facilitate decisions. The tool supports the three main steps of the index creation process: standardize input variables to a common scale (preprocessing), combine variables to a single index variable (combination), and scale and classify the resulting index to meaningful values (postprocessing). Learn more about how Calculate Composite Index works

        params: {"in_table": <Table View>, "in_variablesvar1_reverse1_var2_reverse2": <Value Table>, "append_to_input": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        in_variablesvar1_reverse1_var2_reverse2 = params.get("in_variablesvar1_reverse1_var2_reverse2")
        if in_variablesvar1_reverse1_var2_reverse2 is None:
            return {"success": False, "error": "in_variablesvar1_reverse1_var2_reverse2 parameter is required"}
        append_to_input = params.get("append_to_input")
        out_table = params.get("out_table")
        index_preset = params.get("index_preset")
        preprocessing = params.get("preprocessing")
        pre_threshold_scaling = params.get("pre_threshold_scaling")
        pre_custom_zscorefield1_mean1_stdev1_field2_mean2_stdev2 = params.get("pre_custom_zscorefield1_mean1_stdev1_field2_mean2_stdev2")
        pre_min_maxfield1_min1_max1_field2_min2_max2 = params.get("pre_min_maxfield1_min1_max1_field2_min2_max2")
        pre_thresholdsfield1_method1_threshold1_field2_method2_threshold2 = params.get("pre_thresholdsfield1_method1_threshold1_field2_method2_threshold2")
        index_method = params.get("index_method")
        index_weightsfield1_weight1_field2_weight2 = params.get("index_weightsfield1_weight1_field2_weight2")
        out_index_name = params.get("out_index_name")
        out_index_reverse = params.get("out_index_reverse")
        post_min_max = params.get("post_min_max")
        post_reclass = params.get("post_reclass")
        post_num_classes = params.get("post_num_classes")
        post_custom_classesmin1_max1_min2_max2 = params.get("post_custom_classesmin1_max1_min2_max2")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Calculate_Composite_Index"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Composite Index
            arcpy.CalculateCompositeIndex(in_table, in_variablesvar1_reverse1_var2_reverse2, append_to_input, out_table, index_preset, preprocessing, pre_threshold_scaling, pre_custom_zscorefield1_mean1_stdev1_field2_mean2_stdev2, pre_min_maxfield1_min1_max1_field2_min2_max2, pre_thresholdsfield1_method1_threshold1_field2_method2_threshold2, index_method, index_weightsfield1_weight1_field2_weight2, out_index_name, out_index_reverse, post_min_max, post_reclass, post_num_classes, post_custom_classesmin1_max1_min2_max2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def cluster_and_outlier_analysis_(anselin_local_moran's_i)(self, params):
        """Cluster and Outlier Analysis (Anselin Local Moran's I)

Identifies statistically significant hot spots, cold spots, and spatial outliers using the Anselin Local Moran's I statistic, given a set of weighted features. Learn more about how Cluster and Outlier Analysis (Anselin Local Moran's I) works

        params: {"input_feature_class": <Feature Layer>, "input_field": <Field>, "output_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        input_field = params.get("input_field")
        if input_field is None:
            return {"success": False, "error": "input_field parameter is required"}
        output_feature_class = params.get("output_feature_class")
        if output_feature_class is None:
            return {"success": False, "error": "output_feature_class parameter is required"}
        conceptualization_of_spatial_relationships = params.get("conceptualization_of_spatial_relationships")
        if conceptualization_of_spatial_relationships is None:
            return {"success": False, "error": "conceptualization_of_spatial_relationships parameter is required"}
        distance_method = params.get("distance_method")
        if distance_method is None:
            return {"success": False, "error": "distance_method parameter is required"}
        standardization = params.get("standardization")
        if standardization is None:
            return {"success": False, "error": "standardization parameter is required"}
        distance_band_or_threshold_distance = params.get("distance_band_or_threshold_distance")
        weights_matrix_file = params.get("weights_matrix_file")
        apply_false_discovery_rate_fdr_correction = params.get("apply_false_discovery_rate_fdr_correction")
        number_of_permutations = params.get("number_of_permutations")
        number_of_neighbors = params.get("number_of_neighbors")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Cluster_and_Outlier_Analysis_(Anselin_Local_Moran's_I)"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Cluster and Outlier Analysis (Anselin Local Moran's I)
            arcpy.ClusterandOutlierAnalysis(AnselinLocalMoran'sI)(input_feature_class, input_field, output_feature_class, conceptualization_of_spatial_relationships, distance_method, standardization, distance_band_or_threshold_distance, weights_matrix_file, apply_false_discovery_rate_fdr_correction, number_of_permutations, number_of_neighbors)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def density_based_clustering(self, params):
        """Density-based Clustering

Finds clusters of point features within surrounding noise based on their spatial distribution. Time can also be incorporated to find space-time clusters. Learn more about how Density-based Clustering works

        params: {"in_features": <Feature Layer>, "output_features": <Feature Class>, "cluster_method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        output_features = params.get("output_features")
        if output_features is None:
            return {"success": False, "error": "output_features parameter is required"}
        cluster_method = params.get("cluster_method")
        if cluster_method is None:
            return {"success": False, "error": "cluster_method parameter is required"}
        min_features_cluster = params.get("min_features_cluster")
        if min_features_cluster is None:
            return {"success": False, "error": "min_features_cluster parameter is required"}
        search_distance = params.get("search_distance")
        cluster_sensitivity = params.get("cluster_sensitivity")
        if cluster_sensitivity is None:
            return {"success": False, "error": "cluster_sensitivity parameter is required"}
        time_field = params.get("time_field")
        if time_field is None:
            return {"success": False, "error": "time_field parameter is required"}
        search_time_interval = params.get("search_time_interval")
        if search_time_interval is None:
            return {"success": False, "error": "search_time_interval parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Density-based_Clustering"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Density-based Clustering
            arcpy.DensitybasedClustering(in_features, output_features, cluster_method, min_features_cluster, search_distance, cluster_sensitivity, time_field, search_time_interval)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def hot_spot_analysis_(getis_ord_gi*)(self, params):
        """Hot Spot Analysis (Getis-Ord Gi*)

Given a set of weighted features, identifies statistically significant hot spots and cold spots using the Getis-Ord Gi* statistic. Learn more about how Hot Spot Analysis (Getis-Ord Gi*) works

        params: {"input_feature_class": <Feature Layer>, "input_field": <Field>, "output_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        input_field = params.get("input_field")
        if input_field is None:
            return {"success": False, "error": "input_field parameter is required"}
        output_feature_class = params.get("output_feature_class")
        if output_feature_class is None:
            return {"success": False, "error": "output_feature_class parameter is required"}
        conceptualization_of_spatial_relationships = params.get("conceptualization_of_spatial_relationships")
        if conceptualization_of_spatial_relationships is None:
            return {"success": False, "error": "conceptualization_of_spatial_relationships parameter is required"}
        distance_method = params.get("distance_method")
        if distance_method is None:
            return {"success": False, "error": "distance_method parameter is required"}
        standardization = params.get("standardization")
        if standardization is None:
            return {"success": False, "error": "standardization parameter is required"}
        distance_band_or_threshold_distance = params.get("distance_band_or_threshold_distance")
        self_potential_field = params.get("self_potential_field")
        weights_matrix_file = params.get("weights_matrix_file")
        apply_false_discovery_rate_fdr_correction = params.get("apply_false_discovery_rate_fdr_correction")
        number_of_neighbors = params.get("number_of_neighbors")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Hot_Spot_Analysis_(Getis-Ord_Gi*)"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Hot Spot Analysis (Getis-Ord Gi*)
            arcpy.HotSpotAnalysis(GetisOrdGi*)(input_feature_class, input_field, output_feature_class, conceptualization_of_spatial_relationships, distance_method, standardization, distance_band_or_threshold_distance, self_potential_field, weights_matrix_file, apply_false_discovery_rate_fdr_correction, number_of_neighbors)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def hot_spot_analysis_comparison(self, params):
        """Hot Spot Analysis Comparison

Compares two hot spot analysis result layers and measures their similarity and association. The  similarity and association between the hot spot result layers is determined by comparing the significance level categories between corresponding features in both input layers. The similarity measures how closely the hot spots, cold spots, and nonsignificant areas of both hot spot results spatially align. The association (or dependence) measures the strength of the underlying statistical relationship between the hot spot variables (similar to correlation for continuous variables). Learn more about how Hot Spot Analysis Comparison works

        params: {"in_hot_spot_1": <Feature Layer>, "in_hot_spot_2": <Feature Layer>, "out_features": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_hot_spot_1 = params.get("in_hot_spot_1")
        if in_hot_spot_1 is None:
            return {"success": False, "error": "in_hot_spot_1 parameter is required"}
        in_hot_spot_2 = params.get("in_hot_spot_2")
        if in_hot_spot_2 is None:
            return {"success": False, "error": "in_hot_spot_2 parameter is required"}
        out_features = params.get("out_features")
        if out_features is None:
            return {"success": False, "error": "out_features parameter is required"}
        num_neighbors = params.get("num_neighbors")
        num_perms = params.get("num_perms")
        weighting_method = params.get("weighting_method")
        similarity_weights = params.get("similarity_weights")
        in_weights_table = params.get("in_weights_table")
        exclude_nonsig_features = params.get("exclude_nonsig_features")

            # Generate output name and path
            output_name = f"{in_hot_spot_1.replace(' ', '_')}_Hot_Spot_Analysis_Comparison"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Hot Spot Analysis Comparison
            arcpy.HotSpotAnalysisComparison(in_hot_spot_1, in_hot_spot_2, out_features, num_neighbors, num_perms, weighting_method, similarity_weights, in_weights_table, exclude_nonsig_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def multivariate_clustering(self, params):
        """Multivariate Clustering

Finds natural clusters of features based solely on feature attribute values. Learn more about how Multivariate Clustering works

        params: {"in_features": <Feature Layer>, "output_features": <Feature Class>, "analysis_fieldsanalysis_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        output_features = params.get("output_features")
        if output_features is None:
            return {"success": False, "error": "output_features parameter is required"}
        analysis_fieldsanalysis_field = params.get("analysis_fieldsanalysis_field")
        if analysis_fieldsanalysis_field is None:
            return {"success": False, "error": "analysis_fieldsanalysis_field parameter is required"}
        clustering_method = params.get("clustering_method")
        initialization_method = params.get("initialization_method")
        initialization_field = params.get("initialization_field")
        number_of_clusters = params.get("number_of_clusters")
        output_table = params.get("output_table")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Multivariate_Clustering"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Multivariate Clustering
            arcpy.MultivariateClustering(in_features, output_features, analysis_fieldsanalysis_field, clustering_method, initialization_method, initialization_field, number_of_clusters, output_table)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def optimized_hot_spot_analysis(self, params):
        """Optimized Hot Spot Analysis

Creates a map of statistically significant hot and cold spots using the Getis-Ord Gi* statistic, given incident points or weighted features (points or polygons). The tool evaluates the characteristics of the input feature class to produce optimal results. Learn more about how Optimized Hot Spot Analysis works

        params: {"input_features": <Feature Layer>, "output_features": <Feature Class>, "analysis_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_features = params.get("input_features")
        if input_features is None:
            return {"success": False, "error": "input_features parameter is required"}
        output_features = params.get("output_features")
        if output_features is None:
            return {"success": False, "error": "output_features parameter is required"}
        analysis_field = params.get("analysis_field")
        incident_data_aggregation_method = params.get("incident_data_aggregation_method")
        bounding_polygons_defining_where_incidents_are_possible = params.get("bounding_polygons_defining_where_incidents_are_possible")
        polygons_for_aggregating_incidents_into_counts = params.get("polygons_for_aggregating_incidents_into_counts")
        density_surface = params.get("density_surface")
        cell_size = params.get("cell_size")
        distance_band = params.get("distance_band")

            # Generate output name and path
            output_name = f"{input_features.replace(' ', '_')}_Optimized_Hot_Spot_Analysis"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Optimized Hot Spot Analysis
            arcpy.OptimizedHotSpotAnalysis(input_features, output_features, analysis_field, incident_data_aggregation_method, bounding_polygons_defining_where_incidents_are_possible, polygons_for_aggregating_incidents_into_counts, density_surface, cell_size, distance_band)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def optimized_outlier_analysis(self, params):
        """Optimized Outlier Analysis

Given incident points or weighted features (points or polygons), creates a map of statistically significant hot spots, cold spots, and spatial outliers using the Anselin Local Moran's I statistic. It evaluates the characteristics of the input feature class to produce optimal results. Learn more about how Optimized Outlier Analysis works

        params: {"input_features": <Feature Layer>, "output_features": <Feature Class>, "analysis_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_features = params.get("input_features")
        if input_features is None:
            return {"success": False, "error": "input_features parameter is required"}
        output_features = params.get("output_features")
        if output_features is None:
            return {"success": False, "error": "output_features parameter is required"}
        analysis_field = params.get("analysis_field")
        incident_data_aggregation_method = params.get("incident_data_aggregation_method")
        bounding_polygons_defining_where_incidents_are_possible = params.get("bounding_polygons_defining_where_incidents_are_possible")
        polygons_for_aggregating_incidents_into_counts = params.get("polygons_for_aggregating_incidents_into_counts")
        performance_adjustment = params.get("performance_adjustment")
        cell_size = params.get("cell_size")
        distance_band = params.get("distance_band")

            # Generate output name and path
            output_name = f"{input_features.replace(' ', '_')}_Optimized_Outlier_Analysis"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Optimized Outlier Analysis
            arcpy.OptimizedOutlierAnalysis(input_features, output_features, analysis_field, incident_data_aggregation_method, bounding_polygons_defining_where_incidents_are_possible, polygons_for_aggregating_incidents_into_counts, performance_adjustment, cell_size, distance_band)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def similarity_search(self, params):
        """Similarity Search

Identifies which candidate features are most similar or most dissimilar to one or more input features based on feature attributes. Learn more about how Similarity Search works

        params: {"input_features_to_match": <Feature Layer>, "candidate_features": <Feature Layer>, "output_features": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_features_to_match = params.get("input_features_to_match")
        if input_features_to_match is None:
            return {"success": False, "error": "input_features_to_match parameter is required"}
        candidate_features = params.get("candidate_features")
        if candidate_features is None:
            return {"success": False, "error": "candidate_features parameter is required"}
        output_features = params.get("output_features")
        if output_features is None:
            return {"success": False, "error": "output_features parameter is required"}
        collapse_output_to_points = params.get("collapse_output_to_points")
        if collapse_output_to_points is None:
            return {"success": False, "error": "collapse_output_to_points parameter is required"}
        most_or_least_similar = params.get("most_or_least_similar")
        if most_or_least_similar is None:
            return {"success": False, "error": "most_or_least_similar parameter is required"}
        match_method = params.get("match_method")
        if match_method is None:
            return {"success": False, "error": "match_method parameter is required"}
        number_of_results = params.get("number_of_results")
        if number_of_results is None:
            return {"success": False, "error": "number_of_results parameter is required"}
        attributes_of_interest = params.get("attributes_of_interest")
        if attributes_of_interest is None:
            return {"success": False, "error": "attributes_of_interest parameter is required"}
        fields_to_append_to_output = params.get("fields_to_append_to_output")

            # Generate output name and path
            output_name = f"{input_features_to_match.replace(' ', '_')}_Similarity_Search"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Similarity Search
            arcpy.SimilaritySearch(input_features_to_match, candidate_features, output_features, collapse_output_to_points, most_or_least_similar, match_method, number_of_results, attributes_of_interest, fields_to_append_to_output)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def spatial_outlier_detection(self, params):
        """Spatial Outlier Detection

Identifies global or local spatial outliers in point features. A global outlier is a point that is far away from all other points in a feature class.   Global outliers are detected by examining distances between each point and one of its closest neighbors (by default, the closest neighbor) and detecting points where the distance is large. A local outlier is a point that is farther away from its neighbors than would be expected by the density of points in the surrounding area.  Local outliers are detected by calculating the local outlier factor (LOF) of each feature.  The LOF is a measure that describes how isolated a location is compared to its local neighbors. A higher LOF value indicates greater isolation. The tool can also be used to produce a raster prediction surface that can be used to estimate whether new features will be classified as outliers based on the spatial distribution of the data. Learn more about how Spatial Outlier Detection works

        params: {"in_features": <Feature Layer>, "output_features": <Feature Class>, "n_neighbors": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        output_features = params.get("output_features")
        if output_features is None:
            return {"success": False, "error": "output_features parameter is required"}
        n_neighbors = params.get("n_neighbors")
        percent_outlier = params.get("percent_outlier")
        output_raster = params.get("output_raster")
        outlier_type = params.get("outlier_type")
        sensitivity = params.get("sensitivity")
        keep_type = params.get("keep_type")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Spatial_Outlier_Detection"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Spatial Outlier Detection
            arcpy.SpatialOutlierDetection(in_features, output_features, n_neighbors, percent_outlier, output_raster, outlier_type, sensitivity, keep_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def spatially_constrained_multivariate_clustering(self, params):
        """Spatially Constrained Multivariate Clustering

Finds spatially contiguous clusters of features based on a set of feature attribute values and optional cluster size limits. Learn more about how Spatially Constrained Multivariate Clustering works

        params: {"in_features": <Feature Layer>, "output_features": <Feature Class>, "analysis_fields": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        output_features = params.get("output_features")
        if output_features is None:
            return {"success": False, "error": "output_features parameter is required"}
        analysis_fields = params.get("analysis_fields")
        if analysis_fields is None:
            return {"success": False, "error": "analysis_fields parameter is required"}
        size_constraints = params.get("size_constraints")
        constraint_field = params.get("constraint_field")
        min_constraint = params.get("min_constraint")
        max_constraint = params.get("max_constraint")
        number_of_clusters = params.get("number_of_clusters")
        spatial_constraints = params.get("spatial_constraints")
        weights_matrix_file = params.get("weights_matrix_file")
        number_of_permutations = params.get("number_of_permutations")
        output_table = params.get("output_table")
        if output_table is None:
            return {"success": False, "error": "output_table parameter is required"}

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Spatially_Constrained_Multivariate_Clustering"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Spatially Constrained Multivariate Clustering
            arcpy.SpatiallyConstrainedMultivariateClustering(in_features, output_features, analysis_fields, size_constraints, constraint_field, min_constraint, max_constraint, number_of_clusters, spatial_constraints, weights_matrix_file, number_of_permutations, output_table)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def central_feature(self, params):
        """Central Feature

Identifies the most centrally located feature in a point, line, or polygon feature class. Learn more about how Central Feature works

        params: {"input_feature_class": <Feature Layer>, "output_feature_class": <Feature Class>, "distance_method": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        output_feature_class = params.get("output_feature_class")
        if output_feature_class is None:
            return {"success": False, "error": "output_feature_class parameter is required"}
        distance_method = params.get("distance_method")
        if distance_method is None:
            return {"success": False, "error": "distance_method parameter is required"}
        weight_field = params.get("weight_field")
        self_potential_weight_field = params.get("self_potential_weight_field")
        case_field = params.get("case_field")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Central_Feature"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Central Feature
            arcpy.CentralFeature(input_feature_class, output_feature_class, distance_method, weight_field, self_potential_weight_field, case_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def decompose_spatial_structure(self, params):
        """Decompose Spatial Structure

Decomposes a feature class and neighborhood into a set of spatial components. The components represent potential spatial patterns among the features, such as clusters or trends. The components are returned as fields of the output feature class and represent variables of the input features and neighborhood that have the strongest possible spatial clustering (spatial autocorrelation).  The components are called Moran eigenvectors, and each component represents a different spatial pattern that are each independent of each other. Learn more about Moran eigenvectors

        params: {"in_features": <Feature Layer>, "out_features": <Feature Class>, "append_all_fields": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_features = params.get("out_features")
        if out_features is None:
            return {"success": False, "error": "out_features parameter is required"}
        append_all_fields = params.get("append_all_fields")
        min_autocorrelation = params.get("min_autocorrelation")
        max_components = params.get("max_components")
        neighborhood_type = params.get("neighborhood_type")
        distance_band = params.get("distance_band")
        number_of_neighbors = params.get("number_of_neighbors")
        weights_matrix_file = params.get("weights_matrix_file")
        local_weighting_scheme = params.get("local_weighting_scheme")
        kernel_bandwidth = params.get("kernel_bandwidth")
        out_swm = params.get("out_swm")
        id_field = params.get("id_field")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Decompose_Spatial_Structure"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Decompose Spatial Structure
            arcpy.DecomposeSpatialStructure(in_features, out_features, append_all_fields, min_autocorrelation, max_components, neighborhood_type, distance_band, number_of_neighbors, weights_matrix_file, local_weighting_scheme, kernel_bandwidth, out_swm, id_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def directional_distribution(self, params):
        """Directional Distribution

Creates standard deviational ellipses or ellipsoids to summarize the spatial characteristics of geographic features: central tendency, dispersion, and directional trends. Learn how Directional Distribution (Standard Deviational Ellipse) works

        params: {"input_feature_class": <Feature Layer>, "output_ellipse_feature_class": <Feature Class>, "ellipse_size": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        output_ellipse_feature_class = params.get("output_ellipse_feature_class")
        if output_ellipse_feature_class is None:
            return {"success": False, "error": "output_ellipse_feature_class parameter is required"}
        ellipse_size = params.get("ellipse_size")
        if ellipse_size is None:
            return {"success": False, "error": "ellipse_size parameter is required"}
        weight_field = params.get("weight_field")
        case_field = params.get("case_field")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Directional_Distribution"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Directional Distribution
            arcpy.DirectionalDistribution(input_feature_class, output_ellipse_feature_class, ellipse_size, weight_field, case_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def directional_trend(self, params):
        """Directional Trend

Creates a scatter plot chart on a feature layer displaying the trend of data values in a particular direction.

        params: {"in_features": <Feature Layer>, "analysis_field": <Field>, "direction": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        analysis_field = params.get("analysis_field")
        if analysis_field is None:
            return {"success": False, "error": "analysis_field parameter is required"}
        direction = params.get("direction")
        determine_direction = params.get("determine_direction")
        order = params.get("order")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Directional_Trend"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Directional Trend
            arcpy.DirectionalTrend(in_features, analysis_field, direction, determine_direction, order)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def linear_directional_mean(self, params):
        """Linear Directional Mean

Identifies the mean direction, length, and geographic center for a set of lines. Learn more about how Linear Directional Mean works

        params: {"input_feature_class": <Feature Layer>, "output_feature_class": <Feature Class>, "orientation_only": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        output_feature_class = params.get("output_feature_class")
        if output_feature_class is None:
            return {"success": False, "error": "output_feature_class parameter is required"}
        orientation_only = params.get("orientation_only")
        if orientation_only is None:
            return {"success": False, "error": "orientation_only parameter is required"}
        case_field = params.get("case_field")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Linear_Directional_Mean"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Linear Directional Mean
            arcpy.LinearDirectionalMean(input_feature_class, output_feature_class, orientation_only, case_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def mean_center(self, params):
        """Mean Center

Identifies the geographic center (or the center of concentration) for a set of features. Learn more about how Mean Center works

        params: {"input_feature_class": <Feature Layer>, "output_feature_class": <Feature Class>, "weight_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        output_feature_class = params.get("output_feature_class")
        if output_feature_class is None:
            return {"success": False, "error": "output_feature_class parameter is required"}
        weight_field = params.get("weight_field")
        case_field = params.get("case_field")
        dimension_field = params.get("dimension_field")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Mean_Center"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Mean Center
            arcpy.MeanCenter(input_feature_class, output_feature_class, weight_field, case_field, dimension_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def median_center(self, params):
        """Median Center

Identifies the location that minimizes overall Euclidean distance to the features in a dataset. Learn more about how Median Center works

        params: {"input_feature_class": <Feature Layer>, "output_feature_class": <Feature Class>, "weight_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        output_feature_class = params.get("output_feature_class")
        if output_feature_class is None:
            return {"success": False, "error": "output_feature_class parameter is required"}
        weight_field = params.get("weight_field")
        case_field = params.get("case_field")
        attribute_field = params.get("attribute_field")
        if attribute_field is None:
            return {"success": False, "error": "attribute_field parameter is required"}

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Median_Center"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Median Center
            arcpy.MedianCenter(input_feature_class, output_feature_class, weight_field, case_field, attribute_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def neighborhood_summary_statistics(self, params):
        """Neighborhood Summary Statistics

Calculates summary  statistics of one or more numeric fields using local neighborhoods around each feature.  The local statistics include mean (average), median, standard deviation, interquartile range, skewness, and quantile imbalance. All statistics can be geographically weighted using kernels to give more influence to neighbors closer to the focal feature.  Various neighborhood types can be used, including distance band, number of neighbors, polygon contiguity, Delaunay triangulation, and spatial weights matrix files (.swm). Summary statistics are also calculated for the distances to the neighbors of each feature. Learn more about how Neighborhood Summary Statistics works

        params: {"in_features": <Feature Layer>, "output_features": <Feature Class>, "analysis_fields": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        output_features = params.get("output_features")
        if output_features is None:
            return {"success": False, "error": "output_features parameter is required"}
        analysis_fields = params.get("analysis_fields")
        local_summary_statistic = params.get("local_summary_statistic")
        include_focal_feature = params.get("include_focal_feature")
        ignore_nulls = params.get("ignore_nulls")
        neighborhood_type = params.get("neighborhood_type")
        distance_band = params.get("distance_band")
        number_of_neighbors = params.get("number_of_neighbors")
        weights_matrix_file = params.get("weights_matrix_file")
        local_weighting_scheme = params.get("local_weighting_scheme")
        kernel_bandwidth = params.get("kernel_bandwidth")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Neighborhood_Summary_Statistics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Neighborhood Summary Statistics
            arcpy.NeighborhoodSummaryStatistics(in_features, output_features, analysis_fields, local_summary_statistic, include_focal_feature, ignore_nulls, neighborhood_type, distance_band, number_of_neighbors, weights_matrix_file, local_weighting_scheme, kernel_bandwidth)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def standard_distance(self, params):
        """Standard Distance

Measures the degree to which features are concentrated or dispersed around the geometric mean center. Learn more about how Standard Distance works

        params: {"input_feature_class": <Feature Layer>, "output_standard_distance_feature_class": <Feature Class>, "circle_size": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        output_standard_distance_feature_class = params.get("output_standard_distance_feature_class")
        if output_standard_distance_feature_class is None:
            return {"success": False, "error": "output_standard_distance_feature_class parameter is required"}
        circle_size = params.get("circle_size")
        if circle_size is None:
            return {"success": False, "error": "circle_size parameter is required"}
        weight_field = params.get("weight_field")
        case_field = params.get("case_field")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Standard_Distance"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Standard Distance
            arcpy.StandardDistance(input_feature_class, output_standard_distance_feature_class, circle_size, weight_field, case_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def bivariate_spatial_association_(lee's_l)(self, params):
        """Bivariate Spatial Association (Lee's L)

Calculates the spatial association between two continuous variables using the Lee's L statistic. The Lee's L statistic characterizes both the degree of correlation and the degree of copatterning (similarity of spatial clustering) between the variables.  The value will be between -1 and 1 and is conceptually similar to a correlation coefficient but is adjusted to account for spatial autocorrelation of the two variables. Lee's L values close to 1 indicate that the variables are highly positively correlated and that each variable has high spatial autocorrelation (high and low values of the variables each tend to cluster together).  Values close to -1 indicate that the variables are highly negatively correlated and that each variable has highly positive spatial autocorrelation.  Values close to 0 indicate that the variables are uncorrelated, not spatially autocorrelated, or both. The Lee's L statistic can be partitioned to each input feature, called local Lee's L statistics, that show the local spatial association of the feature and its neighbors.  This can be used to determine areas that have higher or lower spatial association than the global Lee's L statistic. The local statistics can also be classified into one of several categories based on the values of the neighbors of each feature.  Both the global and local statistics are tested for statistical significance using permutations. Learn more about how Bivariate Spatial Association (Lee's L) works

        params: {"in_features": <Feature Layer>, "analysis_field1": <Field>, "analysis_field2": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        analysis_field1 = params.get("analysis_field1")
        if analysis_field1 is None:
            return {"success": False, "error": "analysis_field1 parameter is required"}
        analysis_field2 = params.get("analysis_field2")
        if analysis_field2 is None:
            return {"success": False, "error": "analysis_field2 parameter is required"}
        out_features = params.get("out_features")
        if out_features is None:
            return {"success": False, "error": "out_features parameter is required"}
        neighborhood_type = params.get("neighborhood_type")
        distance_band = params.get("distance_band")
        num_neighbors = params.get("num_neighbors")
        weights_matrix_file = params.get("weights_matrix_file")
        local_weighting_scheme = params.get("local_weighting_scheme")
        kernel_bandwidth = params.get("kernel_bandwidth")
        num_permutations = params.get("num_permutations")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Bivariate_Spatial_Association_(Lee's_L)"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Bivariate Spatial Association (Lee's L)
            arcpy.BivariateSpatialAssociation(Lee'sL)(in_features, analysis_field1, analysis_field2, out_features, neighborhood_type, distance_band, num_neighbors, weights_matrix_file, local_weighting_scheme, kernel_bandwidth, num_permutations)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def causal_inference_analysis(self, params):
        """Causal Inference Analysis

Estimates the causal effect of a continuous exposure variable on a continuous outcome variable by approximating a randomized experiment and controlling for confounding variables. In statistical experiments, the cause-and-effect relationship between an exposure variable (such as the dose of a drug) and an outcome variable (such as a health outcome) is determined by randomly assigning each participant a particular exposure level so that any differences in the outcomes must be due only to the differences in the exposures and not any other attributes of the participants, such as age, preexisting conditions, and healthcare access. However, it is frequently impossible or unethical to perform controlled experiments, so relationships are often established through observational studies. For example, to study the effect of pollution on depression rates, you cannot intentionally expose individuals to high pollution to see the effect on depression. Instead, you can only observe the exposure to pollution and the depression rates of the individuals in your sample. However, because there are many variables (called confounding variables) that impact both pollution and depression, the causal effect cannot be directly estimated without controlling for these variables. To emulate the process of a randomized, controlled experiment, the tool calculates propensity scores for each observation, and the propensity scores are used to weight the observations in such a way that the causal relationship between the exposure and outcome variables is maintained, but correlations between the confounding variables and the exposure variable are removed. This weighted dataset is often called a pseudopopulation, and it has analogous properties to a controlled experiment in which each participant is randomly assigned an exposure. Using the weighted observations, the tool creates an exposure-response function (ERF) that estimates what the average outcome would be if all members of the population received a given exposure value but did not change their confounding variables. Learn more about how Causal Inference Analysis works

        params: {"in_features": <Feature Layer; Table View>, "outcome_field": <Field>, "exposure_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        outcome_field = params.get("outcome_field")
        if outcome_field is None:
            return {"success": False, "error": "outcome_field parameter is required"}
        exposure_field = params.get("exposure_field")
        if exposure_field is None:
            return {"success": False, "error": "exposure_field parameter is required"}
        confounding_variablesvar1_cat1_var2_cat2 = params.get("confounding_variablesvar1_cat1_var2_cat2")
        if confounding_variablesvar1_cat1_var2_cat2 is None:
            return {"success": False, "error": "confounding_variablesvar1_cat1_var2_cat2 parameter is required"}
        out_features = params.get("out_features")
        if out_features is None:
            return {"success": False, "error": "out_features parameter is required"}
        ps_method = params.get("ps_method")
        balancing_method = params.get("balancing_method")
        enable_erf_popups = params.get("enable_erf_popups")
        out_erf_table = params.get("out_erf_table")
        target_outcomes = params.get("target_outcomes")
        target_exposures = params.get("target_exposures")
        lower_exp_trim = params.get("lower_exp_trim")
        upper_exp_trim = params.get("upper_exp_trim")
        lower_ps_trim = params.get("lower_ps_trim")
        upper_ps_trim = params.get("upper_ps_trim")
        num_bins = params.get("num_bins")
        scale = params.get("scale")
        balance_type = params.get("balance_type")
        balance_threshold = params.get("balance_threshold")
        bw_method = params.get("bw_method")
        bandwidth = params.get("bandwidth")
        create_bootstrap_ci = params.get("create_bootstrap_ci")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Causal_Inference_Analysis"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Causal Inference Analysis
            arcpy.CausalInferenceAnalysis(in_features, outcome_field, exposure_field, confounding_variablesvar1_cat1_var2_cat2, out_features, ps_method, balancing_method, enable_erf_popups, out_erf_table, target_outcomes, target_exposures, lower_exp_trim, upper_exp_trim, lower_ps_trim, upper_ps_trim, num_bins, scale, balance_type, balance_threshold, bw_method, bandwidth, create_bootstrap_ci)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def colocation_analysis(self, params):
        """Colocation Analysis

Measures local patterns of spatial association, or colocation, between two categories of point features using the colocation quotient statistic. Learn more about how Colocation Analysis works

        params: {"input_type": <String>, "in_features_of_interest": <Feature Layer>, "output_features": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_type = params.get("input_type")
        if input_type is None:
            return {"success": False, "error": "input_type parameter is required"}
        in_features_of_interest = params.get("in_features_of_interest")
        if in_features_of_interest is None:
            return {"success": False, "error": "in_features_of_interest parameter is required"}
        output_features = params.get("output_features")
        if output_features is None:
            return {"success": False, "error": "output_features parameter is required"}
        field_of_interest = params.get("field_of_interest")
        time_field_of_interest = params.get("time_field_of_interest")
        category_of_interest = params.get("category_of_interest")
        input_feature_for_comparison = params.get("input_feature_for_comparison")
        field_for_comparison = params.get("field_for_comparison")
        time_field_for_comparison = params.get("time_field_for_comparison")
        category_for_comparison = params.get("category_for_comparison")
        neighborhood_type = params.get("neighborhood_type")
        if neighborhood_type is None:
            return {"success": False, "error": "neighborhood_type parameter is required"}
        number_of_neighbors = params.get("number_of_neighbors")
        distance_band = params.get("distance_band")
        weights_matrix_file = params.get("weights_matrix_file")
        temporal_relationship_type = params.get("temporal_relationship_type")
        time_step_interval = params.get("time_step_interval")
        number_of_permutations = params.get("number_of_permutations")
        local_weighting_scheme = params.get("local_weighting_scheme")
        output_table = params.get("output_table")

            # Generate output name and path
            output_name = f"{input_type.replace(' ', '_')}_Colocation_Analysis"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Colocation Analysis
            arcpy.ColocationAnalysis(input_type, in_features_of_interest, output_features, field_of_interest, time_field_of_interest, category_of_interest, input_feature_for_comparison, field_for_comparison, time_field_for_comparison, category_for_comparison, neighborhood_type, number_of_neighbors, distance_band, weights_matrix_file, temporal_relationship_type, time_step_interval, number_of_permutations, local_weighting_scheme, output_table)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def estimate_time_to_event(self, params):
        """Estimate Time to Event

Predicts the time until an event occurs based on the prior times to the event. Explanatory variables can be used to improve the predictions, and the tool can determine which variables increase or decrease the time until the event. Learn more about how Estimate Time to Event works

        params: {"in_features": <Table View>, "age_field": <Field>, "event_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        age_field = params.get("age_field")
        if age_field is None:
            return {"success": False, "error": "age_field parameter is required"}
        event_field = params.get("event_field")
        if event_field is None:
            return {"success": False, "error": "event_field parameter is required"}
        out_features = params.get("out_features")
        if out_features is None:
            return {"success": False, "error": "out_features parameter is required"}
        explanatory_variablesvariable_categorical = params.get("explanatory_variablesvariable_categorical")
        enable_survival_curve_popups = params.get("enable_survival_curve_popups")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Estimate_Time_to_Event"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Estimate Time to Event
            arcpy.EstimateTimetoEvent(in_features, age_field, event_field, out_features, explanatory_variablesvariable_categorical, enable_survival_curve_popups)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def exploratory_regression(self, params):
        """Exploratory Regression

Evaluates all possible combinations of the input candidate explanatory variables, looking for OLS models that best explain the dependent variable within the context of user-specified criteria. Learn more about how Exploratory Regression works

        params: {"input_features": <Feature Layer>, "dependent_variable": <Field>, "candidate_explanatory_variables": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_features = params.get("input_features")
        if input_features is None:
            return {"success": False, "error": "input_features parameter is required"}
        dependent_variable = params.get("dependent_variable")
        if dependent_variable is None:
            return {"success": False, "error": "dependent_variable parameter is required"}
        candidate_explanatory_variables = params.get("candidate_explanatory_variables")
        if candidate_explanatory_variables is None:
            return {"success": False, "error": "candidate_explanatory_variables parameter is required"}
        weights_matrix_file = params.get("weights_matrix_file")
        output_report_file = params.get("output_report_file")
        output_results_table = params.get("output_results_table")
        maximum_number_of_explanatory_variables = params.get("maximum_number_of_explanatory_variables")
        minimum_number_of_explanatory_variables = params.get("minimum_number_of_explanatory_variables")
        minimum_acceptable_adj_r_squared = params.get("minimum_acceptable_adj_r_squared")
        maximum_coefficient_p_value_cutoff = params.get("maximum_coefficient_p_value_cutoff")
        maximum_vif_value_cutoff = params.get("maximum_vif_value_cutoff")
        minimum_acceptable_jarque_bera_p_value = params.get("minimum_acceptable_jarque_bera_p_value")
        minimum_acceptable_spatial_autocorrelation_p_value = params.get("minimum_acceptable_spatial_autocorrelation_p_value")

            # Generate output name and path
            output_name = f"{input_features.replace(' ', '_')}_Exploratory_Regression"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Exploratory Regression
            arcpy.ExploratoryRegression(input_features, dependent_variable, candidate_explanatory_variables, weights_matrix_file, output_report_file, output_results_table, maximum_number_of_explanatory_variables, minimum_number_of_explanatory_variables, minimum_acceptable_adj_r_squared, maximum_coefficient_p_value_cutoff, maximum_vif_value_cutoff, minimum_acceptable_jarque_bera_p_value, minimum_acceptable_spatial_autocorrelation_p_value)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def ols(self, params):
        """OLS

Performs global Ordinary Least Squares (OLS) linear regression to generate predictions or to model a dependent variable in terms of its relationships to a set of explanatory variables. The functionality of this tool is included in the Generalized Linear Regression tool added at ArcGIS Pro 2.3.  The Generalized Linear Regression tool supports additional models.

        params: {"input_feature_class": <Feature Layer>, "unique_id_field": <Field>, "output_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        unique_id_field = params.get("unique_id_field")
        if unique_id_field is None:
            return {"success": False, "error": "unique_id_field parameter is required"}
        output_feature_class = params.get("output_feature_class")
        if output_feature_class is None:
            return {"success": False, "error": "output_feature_class parameter is required"}
        dependent_variable = params.get("dependent_variable")
        if dependent_variable is None:
            return {"success": False, "error": "dependent_variable parameter is required"}
        explanatory_variables = params.get("explanatory_variables")
        if explanatory_variables is None:
            return {"success": False, "error": "explanatory_variables parameter is required"}
        coefficient_output_table = params.get("coefficient_output_table")
        diagnostic_output_table = params.get("diagnostic_output_table")
        output_report_file = params.get("output_report_file")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_OLS"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute OLS
            arcpy.OLS(input_feature_class, unique_id_field, output_feature_class, dependent_variable, explanatory_variables, coefficient_output_table, diagnostic_output_table, output_report_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def forest_based_and_boosted_classification_and_regression(self, params):
        """Forest-based and Boosted Classification and Regression

Creates models and generates predictions using one of two supervised machine learning methods: an adaptation of the random forest algorithm developed by Leo Breiman and Adele Cutler or the Extreme Gradient Boosting (XGBoost) algorithm developed by Tianqi Chen and Carlos Guestrin. Predictions can be performed for both categorical variables (classification) and continuous variables (regression). Explanatory variables can take the form of fields in the attribute table of the training features, raster datasets, and distance features used to calculate proximity values for use as additional variables. In addition to validation of model performance based on the training data, predictions can be made to either features or a prediction raster. Learn more about how Forest-based and Boosted Classification and Regression works

        params: {"prediction_type": <String>, "in_features": <Feature Layer>, "variable_predict": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        prediction_type = params.get("prediction_type")
        if prediction_type is None:
            return {"success": False, "error": "prediction_type parameter is required"}
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        variable_predict = params.get("variable_predict")
        treat_variable_as_categorical = params.get("treat_variable_as_categorical")
        explanatory_variablesvariable_categorical = params.get("explanatory_variablesvariable_categorical")
        distance_features = params.get("distance_features")
        explanatory_rastersvariable_categorical = params.get("explanatory_rastersvariable_categorical")
        features_to_predict = params.get("features_to_predict")
        output_features = params.get("output_features")
        output_raster = params.get("output_raster")
        explanatory_variable_matchingprediction_training = params.get("explanatory_variable_matchingprediction_training")
        explanatory_distance_matchingprediction_training = params.get("explanatory_distance_matchingprediction_training")
        explanatory_rasters_matchingprediction_training = params.get("explanatory_rasters_matchingprediction_training")
        output_trained_features = params.get("output_trained_features")
        output_importance_table = params.get("output_importance_table")
        use_raster_values = params.get("use_raster_values")
        number_of_trees = params.get("number_of_trees")
        minimum_leaf_size = params.get("minimum_leaf_size")
        maximum_depth = params.get("maximum_depth")
        sample_size = params.get("sample_size")
        random_variables = params.get("random_variables")
        percentage_for_training = params.get("percentage_for_training")
        output_classification_table = params.get("output_classification_table")
        output_validation_table = params.get("output_validation_table")
        compensate_sparse_categories = params.get("compensate_sparse_categories")
        number_validation_runs = params.get("number_validation_runs")
        calculate_uncertainty = params.get("calculate_uncertainty")
        output_trained_model = params.get("output_trained_model")
        model_type = params.get("model_type")
        reg_lambda = params.get("reg_lambda")
        gamma = params.get("gamma")
        eta = params.get("eta")
        max_bins = params.get("max_bins")
        optimize = params.get("optimize")
        optimize_algorithm = params.get("optimize_algorithm")
        optimize_target = params.get("optimize_target")
        num_search = params.get("num_search")
        model_param_setting = params.get("model_param_setting")
        output_param_tuning_table = params.get("output_param_tuning_table")
        include_probabilities = params.get("include_probabilities")

            # Generate output name and path
            output_name = f"{prediction_type.replace(' ', '_')}_Forest-based_and_Boosted_Classification_and_Regression"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Forest-based and Boosted Classification and Regression
            arcpy.ForestbasedandBoostedClassificationandRegression(prediction_type, in_features, variable_predict, treat_variable_as_categorical, explanatory_variablesvariable_categorical, distance_features, explanatory_rastersvariable_categorical, features_to_predict, output_features, output_raster, explanatory_variable_matchingprediction_training, explanatory_distance_matchingprediction_training, explanatory_rasters_matchingprediction_training, output_trained_features, output_importance_table, use_raster_values, number_of_trees, minimum_leaf_size, maximum_depth, sample_size, random_variables, percentage_for_training, output_classification_table, output_validation_table, compensate_sparse_categories, number_validation_runs, calculate_uncertainty, output_trained_model, model_type, reg_lambda, gamma, eta, max_bins, optimize, optimize_algorithm, optimize_target, num_search, model_param_setting, output_param_tuning_table, include_probabilities)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generalized_linear_regression_(glr)(self, params):
        """Generalized Linear Regression (GLR)

Performs generalized linear regression (GLR) to generate predictions or to model a dependent variable in terms of its relationship to a set of explanatory variables.  This tool can be used to fit continuous (OLS), binary (logistic), and count (Poisson) models. Learn more about how Generalized Linear Regression works

        params: {"in_features": <Feature Layer>, "dependent_variable": <Field>, "model_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        dependent_variable = params.get("dependent_variable")
        if dependent_variable is None:
            return {"success": False, "error": "dependent_variable parameter is required"}
        model_type = params.get("model_type")
        if model_type is None:
            return {"success": False, "error": "model_type parameter is required"}
        output_features = params.get("output_features")
        if output_features is None:
            return {"success": False, "error": "output_features parameter is required"}
        explanatory_variables = params.get("explanatory_variables")
        if explanatory_variables is None:
            return {"success": False, "error": "explanatory_variables parameter is required"}
        distance_features = params.get("distance_features")
        prediction_locations = params.get("prediction_locations")
        explanatory_variables_to_matchfield_from_prediction_locations_field_from_input_features = params.get("explanatory_variables_to_matchfield_from_prediction_locations_field_from_input_features")
        explanatory_distance_matchingprediction_distance_features_input_explanatory_distance_features = params.get("explanatory_distance_matchingprediction_distance_features_input_explanatory_distance_features")
        output_predicted_features = params.get("output_predicted_features")
        output_trained_model = params.get("output_trained_model")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Generalized_Linear_Regression_(GLR)"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generalized Linear Regression (GLR)
            arcpy.GeneralizedLinearRegression(GLR)(in_features, dependent_variable, model_type, output_features, explanatory_variables, distance_features, prediction_locations, explanatory_variables_to_matchfield_from_prediction_locations_field_from_input_features, explanatory_distance_matchingprediction_distance_features_input_explanatory_distance_features, output_predicted_features, output_trained_model)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_network_spatial_weights(self, params):
        """Generate Network Spatial Weights

Constructs a spatial weights matrix file (.swm) using a network dataset, defining spatial relationships in terms of the underlying network structure. Learn more about how Generate Network Spatial Weights works

        params: {"input_feature_class": <Feature Class>, "unique_id_field": <Field>, "output_spatial_weights_matrix_file": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        unique_id_field = params.get("unique_id_field")
        if unique_id_field is None:
            return {"success": False, "error": "unique_id_field parameter is required"}
        output_spatial_weights_matrix_file = params.get("output_spatial_weights_matrix_file")
        if output_spatial_weights_matrix_file is None:
            return {"success": False, "error": "output_spatial_weights_matrix_file parameter is required"}
        input_network_data_source = params.get("input_network_data_source")
        if input_network_data_source is None:
            return {"success": False, "error": "input_network_data_source parameter is required"}
        travel_mode = params.get("travel_mode")
        if travel_mode is None:
            return {"success": False, "error": "travel_mode parameter is required"}
        impedance_distance_cutoff = params.get("impedance_distance_cutoff")
        if impedance_distance_cutoff is None:
            return {"success": False, "error": "impedance_distance_cutoff parameter is required"}
        impedance_temporal_cutoff = params.get("impedance_temporal_cutoff")
        impedance_cost_cutoff = params.get("impedance_cost_cutoff")
        maximum_number_of_neighbors = params.get("maximum_number_of_neighbors")
        time_of_day = params.get("time_of_day")
        time_zone = params.get("time_zone")
        barriers = params.get("barriers")
        search_tolerance = params.get("search_tolerance")
        conceptualization_of_spatial_relationships = params.get("conceptualization_of_spatial_relationships")
        exponent = params.get("exponent")
        row_standardization = params.get("row_standardization")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Generate_Network_Spatial_Weights"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Network Spatial Weights
            arcpy.GenerateNetworkSpatialWeights(input_feature_class, unique_id_field, output_spatial_weights_matrix_file, input_network_data_source, travel_mode, impedance_distance_cutoff, impedance_temporal_cutoff, impedance_cost_cutoff, maximum_number_of_neighbors, time_of_day, time_zone, barriers, search_tolerance, conceptualization_of_spatial_relationships, exponent, row_standardization)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_spatial_weights_matrix(self, params):
        """Generate Spatial Weights Matrix

Generates a spatial weights matrix file (.swm) to represent the spatial relationships among features in a dataset. Learn more about how Generate Spatial Weights Matrix works

        params: {"input_feature_class": <Feature Class>, "unique_id_field": <Field>, "output_spatial_weights_matrix_file": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        unique_id_field = params.get("unique_id_field")
        if unique_id_field is None:
            return {"success": False, "error": "unique_id_field parameter is required"}
        output_spatial_weights_matrix_file = params.get("output_spatial_weights_matrix_file")
        if output_spatial_weights_matrix_file is None:
            return {"success": False, "error": "output_spatial_weights_matrix_file parameter is required"}
        conceptualization_of_spatial_relationships = params.get("conceptualization_of_spatial_relationships")
        if conceptualization_of_spatial_relationships is None:
            return {"success": False, "error": "conceptualization_of_spatial_relationships parameter is required"}
        distance_method = params.get("distance_method")
        exponent = params.get("exponent")
        threshold_distance = params.get("threshold_distance")
        number_of_neighbors = params.get("number_of_neighbors")
        row_standardization = params.get("row_standardization")
        input_table = params.get("input_table")
        date_time_field = params.get("date_time_field")
        date_time_interval_type = params.get("date_time_interval_type")
        date_time_interval_value = params.get("date_time_interval_value")
        use_z_values = params.get("use_z_values")
        if use_z_values is None:
            return {"success": False, "error": "use_z_values parameter is required"}

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Generate_Spatial_Weights_Matrix"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Spatial Weights Matrix
            arcpy.GenerateSpatialWeightsMatrix(input_feature_class, unique_id_field, output_spatial_weights_matrix_file, conceptualization_of_spatial_relationships, distance_method, exponent, threshold_distance, number_of_neighbors, row_standardization, input_table, date_time_field, date_time_interval_type, date_time_interval_value, use_z_values)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def geographically_weighted_regression_(gwr)(self, params):
        """Geographically Weighted Regression (GWR)

Performs Geographically Weighted Regression, which is a local form of linear regression that is used to model spatially varying relationships. Learn more about how Geographically Weighted Regression (GWR) works

        params: {"in_features": <Feature Layer>, "dependent_variable": <Field>, "model_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        dependent_variable = params.get("dependent_variable")
        if dependent_variable is None:
            return {"success": False, "error": "dependent_variable parameter is required"}
        model_type = params.get("model_type")
        if model_type is None:
            return {"success": False, "error": "model_type parameter is required"}
        explanatory_variables = params.get("explanatory_variables")
        if explanatory_variables is None:
            return {"success": False, "error": "explanatory_variables parameter is required"}
        output_features = params.get("output_features")
        if output_features is None:
            return {"success": False, "error": "output_features parameter is required"}
        neighborhood_type = params.get("neighborhood_type")
        if neighborhood_type is None:
            return {"success": False, "error": "neighborhood_type parameter is required"}
        neighborhood_selection_method = params.get("neighborhood_selection_method")
        if neighborhood_selection_method is None:
            return {"success": False, "error": "neighborhood_selection_method parameter is required"}
        minimum_number_of_neighbors = params.get("minimum_number_of_neighbors")
        maximum_number_of_neighbors = params.get("maximum_number_of_neighbors")
        minimum_search_distance = params.get("minimum_search_distance")
        maximum_search_distance = params.get("maximum_search_distance")
        number_of_neighbors_increment = params.get("number_of_neighbors_increment")
        search_distance_increment = params.get("search_distance_increment")
        number_of_increments = params.get("number_of_increments")
        number_of_neighbors = params.get("number_of_neighbors")
        distance_band = params.get("distance_band")
        prediction_locations = params.get("prediction_locations")
        explanatory_variables_to_match = params.get("explanatory_variables_to_match")
        output_predicted_features = params.get("output_predicted_features")
        robust_prediction = params.get("robust_prediction")
        local_weighting_scheme = params.get("local_weighting_scheme")
        coefficient_raster_workspace = params.get("coefficient_raster_workspace")
        scale = params.get("scale")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Geographically_Weighted_Regression_(GWR)"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Geographically Weighted Regression (GWR)
            arcpy.GeographicallyWeightedRegression(GWR)(in_features, dependent_variable, model_type, explanatory_variables, output_features, neighborhood_type, neighborhood_selection_method, minimum_number_of_neighbors, maximum_number_of_neighbors, minimum_search_distance, maximum_search_distance, number_of_neighbors_increment, search_distance_increment, number_of_increments, number_of_neighbors, distance_band, prediction_locations, explanatory_variables_to_match, output_predicted_features, robust_prediction, local_weighting_scheme, coefficient_raster_workspace, scale)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def local_bivariate_relationships(self, params):
        """Local Bivariate Relationships

Analyzes two variables for statistically significant relationships using local entropy. Each feature is classified into one of six categories based on the type of relationship. The output can be used to visualize areas where the variables are related and explore how their relationship changes across the study area. Learn more about how Local Bivariate Relationships works

        params: {"in_features": <Feature Layer>, "dependent_variable": <Field>, "explanatory_variable": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        dependent_variable = params.get("dependent_variable")
        if dependent_variable is None:
            return {"success": False, "error": "dependent_variable parameter is required"}
        explanatory_variable = params.get("explanatory_variable")
        if explanatory_variable is None:
            return {"success": False, "error": "explanatory_variable parameter is required"}
        output_features = params.get("output_features")
        if output_features is None:
            return {"success": False, "error": "output_features parameter is required"}
        number_of_neighbors = params.get("number_of_neighbors")
        number_of_permutations = params.get("number_of_permutations")
        enable_local_scatterplot_popups = params.get("enable_local_scatterplot_popups")
        level_of_confidence = params.get("level_of_confidence")
        apply_false_discovery_rate_fdr_correction = params.get("apply_false_discovery_rate_fdr_correction")
        scaling_factor = params.get("scaling_factor")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Local_Bivariate_Relationships"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Local Bivariate Relationships
            arcpy.LocalBivariateRelationships(in_features, dependent_variable, explanatory_variable, output_features, number_of_neighbors, number_of_permutations, enable_local_scatterplot_popups, level_of_confidence, apply_false_discovery_rate_fdr_correction, scaling_factor)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def multiscale_geographically_weighted_regression_(mgwr)(self, params):
        """Multiscale Geographically Weighted Regression (MGWR)

Performs Multiscale Geographically Weighted Regression (MGWR), which is a local form of linear regression that models spatially varying relationships. MGWR builds upon geographically weighted regression (GWR). It is a local regression model that allows the coefficients of the explanatory variables to vary across space. Each explanatory variable may operate at a different spatial scale. GWR does not account for this, but MGWR does by allowing a different neighborhood (bandwidth) for each explanatory variable. The neighborhood (bandwidth) of an explanatory variable determines the features that are used to estimate the coefficient of that explanatory variable in the linear regression model that is fit at a target feature. Learn more about how Multiscale Geographically Weighted Regression (MGWR)
works

        params: {"in_features": <Feature Layer>, "dependent_variable": <Field>, "model_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        dependent_variable = params.get("dependent_variable")
        if dependent_variable is None:
            return {"success": False, "error": "dependent_variable parameter is required"}
        model_type = params.get("model_type")
        if model_type is None:
            return {"success": False, "error": "model_type parameter is required"}
        explanatory_variables = params.get("explanatory_variables")
        if explanatory_variables is None:
            return {"success": False, "error": "explanatory_variables parameter is required"}
        output_features = params.get("output_features")
        if output_features is None:
            return {"success": False, "error": "output_features parameter is required"}
        neighborhood_type = params.get("neighborhood_type")
        if neighborhood_type is None:
            return {"success": False, "error": "neighborhood_type parameter is required"}
        neighborhood_selection_method = params.get("neighborhood_selection_method")
        if neighborhood_selection_method is None:
            return {"success": False, "error": "neighborhood_selection_method parameter is required"}
        minimum_number_of_neighbors = params.get("minimum_number_of_neighbors")
        maximum_number_of_neighbors = params.get("maximum_number_of_neighbors")
        distance_unit = params.get("distance_unit")
        minimum_search_distance = params.get("minimum_search_distance")
        maximum_search_distance = params.get("maximum_search_distance")
        number_of_neighbors_increment = params.get("number_of_neighbors_increment")
        search_distance_increment = params.get("search_distance_increment")
        number_of_increments = params.get("number_of_increments")
        number_of_neighbors = params.get("number_of_neighbors")
        distance_band = params.get("distance_band")
        number_of_neighbors_golden = params.get("number_of_neighbors_golden")
        number_of_neighbors_manual = params.get("number_of_neighbors_manual")
        number_of_neighbors_defined = params.get("number_of_neighbors_defined")
        distance_golden = params.get("distance_golden")
        distance_manual = params.get("distance_manual")
        distance_defined = params.get("distance_defined")
        prediction_locations = params.get("prediction_locations")
        explanatory_variables_to_match = params.get("explanatory_variables_to_match")
        output_predicted_features = params.get("output_predicted_features")
        robust_prediction = params.get("robust_prediction")
        local_weighting_scheme = params.get("local_weighting_scheme")
        output_table = params.get("output_table")
        coefficient_raster_workspace = params.get("coefficient_raster_workspace")
        scale = params.get("scale")
        number_of_neighbors_gradient = params.get("number_of_neighbors_gradient")
        distance_gradient = params.get("distance_gradient")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Multiscale_Geographically_Weighted_Regression_(MGWR)"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Multiscale Geographically Weighted Regression (MGWR)
            arcpy.MultiscaleGeographicallyWeightedRegression(MGWR)(in_features, dependent_variable, model_type, explanatory_variables, output_features, neighborhood_type, neighborhood_selection_method, minimum_number_of_neighbors, maximum_number_of_neighbors, distance_unit, minimum_search_distance, maximum_search_distance, number_of_neighbors_increment, search_distance_increment, number_of_increments, number_of_neighbors, distance_band, number_of_neighbors_golden, number_of_neighbors_manual, number_of_neighbors_defined, distance_golden, distance_manual, distance_defined, prediction_locations, explanatory_variables_to_match, output_predicted_features, robust_prediction, local_weighting_scheme, output_table, coefficient_raster_workspace, scale, number_of_neighbors_gradient, distance_gradient)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def ordinary_least_squares_(ols)(self, params):
        """Ordinary Least Squares (OLS)

Performs global Ordinary Least Squares (OLS) linear regression to generate predictions or to model a dependent variable in terms of its relationships to a set of explanatory variables. The functionality of this tool is included in the Generalized Linear Regression tool added at ArcGIS Pro 2.3.  The Generalized Linear Regression tool supports additional models.

        params: {"input_feature_class": <Feature Layer>, "unique_id_field": <Field>, "output_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        unique_id_field = params.get("unique_id_field")
        if unique_id_field is None:
            return {"success": False, "error": "unique_id_field parameter is required"}
        output_feature_class = params.get("output_feature_class")
        if output_feature_class is None:
            return {"success": False, "error": "output_feature_class parameter is required"}
        dependent_variable = params.get("dependent_variable")
        if dependent_variable is None:
            return {"success": False, "error": "dependent_variable parameter is required"}
        explanatory_variables = params.get("explanatory_variables")
        if explanatory_variables is None:
            return {"success": False, "error": "explanatory_variables parameter is required"}
        coefficient_output_table = params.get("coefficient_output_table")
        diagnostic_output_table = params.get("diagnostic_output_table")
        output_report_file = params.get("output_report_file")

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Ordinary_Least_Squares_(OLS)"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Ordinary Least Squares (OLS)
            arcpy.OrdinaryLeastSquares(OLS)(input_feature_class, unique_id_field, output_feature_class, dependent_variable, explanatory_variables, coefficient_output_table, diagnostic_output_table, output_report_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def predict_using_spatial_statistics_model_file(self, params):
        """Predict Using Spatial Statistics Model File

Predicts continuous or categorical values using a trained spatial statistics model (.ssm file). Learn more about spatial statistics model files

        params: {"input_model": <File>, "prediction_type": <String>, "features_to_predict": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_model = params.get("input_model")
        if input_model is None:
            return {"success": False, "error": "input_model parameter is required"}
        prediction_type = params.get("prediction_type")
        if prediction_type is None:
            return {"success": False, "error": "prediction_type parameter is required"}
        features_to_predict = params.get("features_to_predict")
        output_features = params.get("output_features")
        output_raster = params.get("output_raster")
        explanatory_variable_matchingpred1_train1_cat1_pred2_train2_cat2 = params.get("explanatory_variable_matchingpred1_train1_cat1_pred2_train2_cat2")
        explanatory_distance_matchingpred1_cat1_pred2_cat2 = params.get("explanatory_distance_matchingpred1_cat1_pred2_cat2")
        explanatory_rasters_matchingpred1_train1_cat1_pred2_train2_cat2 = params.get("explanatory_rasters_matchingpred1_train1_cat1_pred2_train2_cat2")

            # Generate output name and path
            output_name = f"{input_model.replace(' ', '_')}_Predict_Using_Spatial_Statistics_Model_File"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Predict Using Spatial Statistics Model File
            arcpy.PredictUsingSpatialStatisticsModelFile(input_model, prediction_type, features_to_predict, output_features, output_raster, explanatory_variable_matchingpred1_train1_cat1_pred2_train2_cat2, explanatory_distance_matchingpred1_cat1_pred2_cat2, explanatory_rasters_matchingpred1_train1_cat1_pred2_train2_cat2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def presence_only_prediction(self, params):
        """Presence-only Prediction

Models the presence of a phenomenon given known presence locations and explanatory variables using a maximum entropy approach (MaxEnt). The tool provides output features and rasters that include the probability of presence and can be applied to problems in which only presence is known and absence is not known. Learn more about how Presence-only Prediction (MaxEnt) works

        params: {"input_point_features": <Feature Layer>, "contains_background": <Boolean>, "presence_indicator_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_point_features = params.get("input_point_features")
        if input_point_features is None:
            return {"success": False, "error": "input_point_features parameter is required"}
        contains_background = params.get("contains_background")
        presence_indicator_field = params.get("presence_indicator_field")
        explanatory_variablesvariable_categorical = params.get("explanatory_variablesvariable_categorical")
        distance_features = params.get("distance_features")
        explanatory_rastersvariable_categorical = params.get("explanatory_rastersvariable_categorical")
        basis_expansion_functions = params.get("basis_expansion_functions")
        number_knots = params.get("number_knots")
        study_area_type = params.get("study_area_type")
        study_area_polygon = params.get("study_area_polygon")
        spatial_thinning = params.get("spatial_thinning")
        thinning_distance_band = params.get("thinning_distance_band")
        number_of_iterations = params.get("number_of_iterations")
        relative_weight = params.get("relative_weight")
        link_function = params.get("link_function")
        presence_probability_cutoff = params.get("presence_probability_cutoff")
        output_trained_features = params.get("output_trained_features")
        output_trained_raster = params.get("output_trained_raster")
        output_response_curve_table = params.get("output_response_curve_table")
        output_sensitivity_table = params.get("output_sensitivity_table")
        features_to_predict = params.get("features_to_predict")
        output_pred_features = params.get("output_pred_features")
        output_pred_raster = params.get("output_pred_raster")
        explanatory_variable_matchingprediction_training = params.get("explanatory_variable_matchingprediction_training")
        explanatory_distance_matchingprediction_training = params.get("explanatory_distance_matchingprediction_training")
        explanatory_rasters_matchingprediction_training = params.get("explanatory_rasters_matchingprediction_training")
        allow_predictions_outside_of_data_ranges = params.get("allow_predictions_outside_of_data_ranges")
        resampling_scheme = params.get("resampling_scheme")
        number_of_groups = params.get("number_of_groups")
        output_trained_model = params.get("output_trained_model")

            # Generate output name and path
            output_name = f"{input_point_features.replace(' ', '_')}_Presence-only_Prediction"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Presence-only Prediction
            arcpy.PresenceonlyPrediction(input_point_features, contains_background, presence_indicator_field, explanatory_variablesvariable_categorical, distance_features, explanatory_rastersvariable_categorical, basis_expansion_functions, number_knots, study_area_type, study_area_polygon, spatial_thinning, thinning_distance_band, number_of_iterations, relative_weight, link_function, presence_probability_cutoff, output_trained_features, output_trained_raster, output_response_curve_table, output_sensitivity_table, features_to_predict, output_pred_features, output_pred_raster, explanatory_variable_matchingprediction_training, explanatory_distance_matchingprediction_training, explanatory_rasters_matchingprediction_training, allow_predictions_outside_of_data_ranges, resampling_scheme, number_of_groups, output_trained_model)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def spatial_association_between_zones(self, params):
        """Spatial Association Between Zones

Measures the degree of spatial association between two regionalizations of the same study area in which each regionalization is composed of a set of categories, called zones.  The association between the regionalizations is determined by the area overlap between zones of each regionalization. The association is highest when each zone of one regionalization closely corresponds to a zone of the other regionalization.  Similarly, spatial association is lowest when the zones of one regionalization have large overlap with many different zones of the other regionalization.   The primary output of the tool is a global measure of spatial association between the categorical variables: a single number ranging from 0 (no correspondence) to 1 (perfect spatial alignment of zones). Optionally, this global association can be calculated and visualized for specific zones of either regionalization or for specific combinations of zones between regionalizations. For example, you can use this tool to compare two sets of categorical zones, such as the crop type and soil drainage class of an agricultural area to measure how closely particular crops correspond to a specific class of soil drainage. However, you can also use this tool to measure the degree of change of the same categorical zones over time.  For example, climate zones from 1990 can be compared to climate zones from 2020 to measure how much the climate zones changed over three decades. Using optional outputs, you can determine how each individual climate zone changed, such as whether arid climate zones expanded into areas that were
previously semiarid. Learn more about how Spatial Association Between Zones works

        params: {"input_feature_or_raster": <Feature Layer; Raster Layer; Image Service>, "categorical_zone_field": <Field>, "overlay_feature_or_raster": <Feature Layer; Raster Layer; Image Service>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_or_raster = params.get("input_feature_or_raster")
        if input_feature_or_raster is None:
            return {"success": False, "error": "input_feature_or_raster parameter is required"}
        categorical_zone_field = params.get("categorical_zone_field")
        if categorical_zone_field is None:
            return {"success": False, "error": "categorical_zone_field parameter is required"}
        overlay_feature_or_raster = params.get("overlay_feature_or_raster")
        if overlay_feature_or_raster is None:
            return {"success": False, "error": "overlay_feature_or_raster parameter is required"}
        categorical_overlay_zone_field = params.get("categorical_overlay_zone_field")
        if categorical_overlay_zone_field is None:
            return {"success": False, "error": "categorical_overlay_zone_field parameter is required"}
        output_features = params.get("output_features")
        output_raster = params.get("output_raster")
        correspondence_overlay_to_input = params.get("correspondence_overlay_to_input")
        correspondence_input_to_overlay = params.get("correspondence_input_to_overlay")

            # Generate output name and path
            output_name = f"{input_feature_or_raster.replace(' ', '_')}_Spatial_Association_Between_Zones"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Spatial Association Between Zones
            arcpy.SpatialAssociationBetweenZones(input_feature_or_raster, categorical_zone_field, overlay_feature_or_raster, categorical_overlay_zone_field, output_features, output_raster, correspondence_overlay_to_input, correspondence_input_to_overlay)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def spatial_autoregression(self, params):
        """Spatial Autoregression

Estimates a global spatial regression model for a point or polygon feature class. The assumptions of traditional linear regression models are often violated when using spatial data. When spatial autocorrelation is present in a dataset, coefficient estimates may be biased and lead to overconfident inference. This tool can be used to estimate a regression model that is robust in the presence of spatial dependence and heteroskedasticity, as well as measure spatial spillovers. The tool uses Lagrange Multiplier (LM), also known as a Rao Score, diagnostic tests to determine the model that is most appropriate. Based on the LM diagnostics, either an ordinary least square (OLS), spatial lag model (SLM), spatial error model (SEM), or spatial autoregressive combined model (SAC) may be estimated. Learn more about how Spatial Autoregression works

        params: {"in_features": <Feature Layer>, "dependent_variable": <Field>, "explanatory_variables": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        dependent_variable = params.get("dependent_variable")
        if dependent_variable is None:
            return {"success": False, "error": "dependent_variable parameter is required"}
        explanatory_variables = params.get("explanatory_variables")
        if explanatory_variables is None:
            return {"success": False, "error": "explanatory_variables parameter is required"}
        out_features = params.get("out_features")
        if out_features is None:
            return {"success": False, "error": "out_features parameter is required"}
        model_type = params.get("model_type")
        if model_type is None:
            return {"success": False, "error": "model_type parameter is required"}
        neighborhood_type = params.get("neighborhood_type")
        distance_band = params.get("distance_band")
        number_of_neighbors = params.get("number_of_neighbors")
        weights_matrix_file = params.get("weights_matrix_file")
        local_weighting_scheme = params.get("local_weighting_scheme")
        kernel_bandwidth = params.get("kernel_bandwidth")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Spatial_Autoregression"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Spatial Autoregression
            arcpy.SpatialAutoregression(in_features, dependent_variable, explanatory_variables, out_features, model_type, neighborhood_type, distance_band, number_of_neighbors, weights_matrix_file, local_weighting_scheme, kernel_bandwidth)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compare_neighborhood_conceptualizations(self, params):
        """Compare Neighborhood Conceptualizations

Selects the spatial weights matrix (SWM) from a set of candidate SWMs that best represents the spatial patterns (such as trends or clusters) of one or more numeric fields. The output spatial weights matrix  file can then be used in tools that allow .swm files for their Neighborhood Type or Conceptualization of Spatial Relationships parameter values, such as the Bivariate Spatial Association (Lee's L), Hot Spot Analysis (Getis-Ord Gi*), and Cluster and Outlier Analysis (Anselin Local Moran's I) tools. The tool selects the SWM by creating spatial components (called Moran eigenvectors) from each candidate SWM and testing how effectively the components represent the spatial patterns of the input fields. Learn more about Moran eigenvectors

        params: {"in_features": <Feature Layer>, "input_fields": <Field>, "out_swm": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        input_fields = params.get("input_fields")
        if input_fields is None:
            return {"success": False, "error": "input_fields parameter is required"}
        out_swm = params.get("out_swm")
        if out_swm is None:
            return {"success": False, "error": "out_swm parameter is required"}
        id_field = params.get("id_field")
        if id_field is None:
            return {"success": False, "error": "id_field parameter is required"}
        in_swm = params.get("in_swm")
        compare_only_inputs = params.get("compare_only_inputs")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Compare_Neighborhood_Conceptualizations"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compare Neighborhood Conceptualizations
            arcpy.CompareNeighborhoodConceptualizations(in_features, input_fields, out_swm, id_field, in_swm, compare_only_inputs)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_spatial_component_explanatory_variables(self, params):
        """Create Spatial Component Explanatory Variables

Creates a set of spatial component fields that best describe the spatial patterns of one or more numeric fields and serve as useful explanatory variables in a prediction or regression model. The input fields should be the explanatory and dependent variables that will be used in a prediction model. The resulting spatial component fields (called Moran eigenvectors) can be used as explanatory variables (in addition to the original explanatory variables) that will often improve the predictive power of the model by accounting for spatial patterns of the other variables. Learn more about Moran eigenvectors

        params: {"in_features": <Feature Layer>, "input_fields": <Field>, "out_features": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        input_fields = params.get("input_fields")
        if input_fields is None:
            return {"success": False, "error": "input_fields parameter is required"}
        out_features = params.get("out_features")
        if out_features is None:
            return {"success": False, "error": "out_features parameter is required"}
        append_all_fields = params.get("append_all_fields")
        in_swm = params.get("in_swm")
        out_swm = params.get("out_swm")
        id_field = params.get("id_field")
        compare_only_inputs = params.get("compare_only_inputs")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Create_Spatial_Component_Explanatory_Variables"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Spatial Component Explanatory Variables
            arcpy.CreateSpatialComponentExplanatoryVariables(in_features, input_fields, out_features, append_all_fields, in_swm, out_swm, id_field, compare_only_inputs)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def decompose_spatial_structure_(moran_eigenvectors)(self, params):
        """Decompose Spatial Structure (Moran Eigenvectors)

Decomposes a feature class and neighborhood into a set of spatial components. The components represent potential spatial patterns among the features, such as clusters or trends. The components are returned as fields of the output feature class and represent variables of the input features and neighborhood that have the strongest possible spatial clustering (spatial autocorrelation).  The components are called Moran eigenvectors, and each component represents a different spatial pattern that are each independent of each other. Learn more about Moran eigenvectors

        params: {"in_features": <Feature Layer>, "out_features": <Feature Class>, "append_all_fields": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_features = params.get("out_features")
        if out_features is None:
            return {"success": False, "error": "out_features parameter is required"}
        append_all_fields = params.get("append_all_fields")
        min_autocorrelation = params.get("min_autocorrelation")
        max_components = params.get("max_components")
        neighborhood_type = params.get("neighborhood_type")
        distance_band = params.get("distance_band")
        number_of_neighbors = params.get("number_of_neighbors")
        weights_matrix_file = params.get("weights_matrix_file")
        local_weighting_scheme = params.get("local_weighting_scheme")
        kernel_bandwidth = params.get("kernel_bandwidth")
        out_swm = params.get("out_swm")
        id_field = params.get("id_field")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Decompose_Spatial_Structure_(Moran_Eigenvectors)"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Decompose Spatial Structure (Moran Eigenvectors)
            arcpy.DecomposeSpatialStructure(MoranEigenvectors)(in_features, out_features, append_all_fields, min_autocorrelation, max_components, neighborhood_type, distance_band, number_of_neighbors, weights_matrix_file, local_weighting_scheme, kernel_bandwidth, out_swm, id_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def filter_spatial_autocorrelation_from_field(self, params):
        """Filter Spatial Autocorrelation From Field

Creates a spatially filtered version of an input field.  The filtered variable will have no statistically significant spatial clustering but will maintain the core statistical properties of the field. The spatially filtered version of the field can then be used in analytical workflows (such as correlation or regression analysis) that assume the values at each location are spatially independent (not spatially clustered). The tool filters spatial autocorrelation by splitting the field in a nonspatial component (the filtered field) and a set of spatial components (called Moran eigenvectors). When the input field is a field of residuals or standardized residuals from a prediction or regression model, including the spatial components as explanatory variables in the model (in addition to the original explanatory variables) will reduce or eliminate spatial autocorrelation of the residual term, which is an assumption of various prediction models. Learn more about Moran eigenvectors

        params: {"in_features": <Feature Layer>, "input_field": <Field>, "out_features": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        input_field = params.get("input_field")
        if input_field is None:
            return {"success": False, "error": "input_field parameter is required"}
        out_features = params.get("out_features")
        if out_features is None:
            return {"success": False, "error": "out_features parameter is required"}
        append_all_fields = params.get("append_all_fields")
        in_swm = params.get("in_swm")
        out_swm = params.get("out_swm")
        id_field = params.get("id_field")
        compare_only_inputs = params.get("compare_only_inputs")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Filter_Spatial_Autocorrelation_From_Field"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Filter Spatial Autocorrelation From Field
            arcpy.FilterSpatialAutocorrelationFromField(in_features, input_field, out_features, append_all_fields, in_swm, out_swm, id_field, compare_only_inputs)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_distance_band_from_neighbor_count(self, params):
        """Calculate Distance Band from Neighbor Count

Returns the minimum, the maximum, and the average distance to the specified Nth nearest neighbor (N is an input parameter) for a set of features.  Results are written as tool execution messages.

        params: {"input_features": <Feature Layer>, "neighbors": <Long>, "distance_method": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_features = params.get("input_features")
        if input_features is None:
            return {"success": False, "error": "input_features parameter is required"}
        neighbors = params.get("neighbors")
        if neighbors is None:
            return {"success": False, "error": "neighbors parameter is required"}
        distance_method = params.get("distance_method")
        if distance_method is None:
            return {"success": False, "error": "distance_method parameter is required"}

            # Generate output name and path
            output_name = f"{input_features.replace(' ', '_')}_Calculate_Distance_Band_from_Neighbor_Count"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Distance Band from Neighbor Count
            arcpy.CalculateDistanceBandfromNeighborCount(input_features, neighbors, distance_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_rates(self, params):
        """Calculate Rates

Calculates crude or smoothed rates. The global empirical Bayes rate method smooths the rates toward a global reference rate. The local empirical Bayes, locally weighted average, and locally weighted median rate methods use local neighbors to spatially smooth rates. Learn more about how Calculate Rates works

        params: {"in_table": <Table View>, "rate_fieldscount_field_population_field": <Value Table>, "append_to_input": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        rate_fieldscount_field_population_field = params.get("rate_fieldscount_field_population_field")
        if rate_fieldscount_field_population_field is None:
            return {"success": False, "error": "rate_fieldscount_field_population_field parameter is required"}
        append_to_input = params.get("append_to_input")
        out_table = params.get("out_table")
        rate_method = params.get("rate_method")
        probability_distribution = params.get("probability_distribution")
        if probability_distribution is None:
            return {"success": False, "error": "probability_distribution parameter is required"}
        neighborhood_type = params.get("neighborhood_type")
        distance_band = params.get("distance_band")
        number_of_neighbors = params.get("number_of_neighbors")
        weights_matrix_file = params.get("weights_matrix_file")
        local_weighting_scheme = params.get("local_weighting_scheme")
        kernel_bandwidth = params.get("kernel_bandwidth")
        rate_multiplier = params.get("rate_multiplier")
        if rate_multiplier is None:
            return {"success": False, "error": "rate_multiplier parameter is required"}

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Calculate_Rates"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Rates
            arcpy.CalculateRates(in_table, rate_fieldscount_field_population_field, append_to_input, out_table, rate_method, probability_distribution, neighborhood_type, distance_band, number_of_neighbors, weights_matrix_file, local_weighting_scheme, kernel_bandwidth, rate_multiplier)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def collect_events(self, params):
        """Collect Events

Converts event data, such as crime or disease incidents, to weighted point data.

        params: {"input_incident_features": <Feature Layer>, "output_weighted_point_feature_class": <Feature Class>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_incident_features = params.get("input_incident_features")
        if input_incident_features is None:
            return {"success": False, "error": "input_incident_features parameter is required"}
        output_weighted_point_feature_class = params.get("output_weighted_point_feature_class")
        if output_weighted_point_feature_class is None:
            return {"success": False, "error": "output_weighted_point_feature_class parameter is required"}

            # Generate output name and path
            output_name = f"{input_incident_features.replace(' ', '_')}_Collect_Events"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Collect Events
            arcpy.CollectEvents(input_incident_features, output_weighted_point_feature_class)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def convert_spatial_statistics_popup_charts_for_web_display(self, params):
        """Convert Spatial Statistics Popup Charts for Web Display

Prepares interactive pop-up charts for web display by saving them as image attachments to a feature class. Several tools in the Spatial Statistics and Space Time Pattern Mining toolboxes create output feature classes that include an HTML_CHART  field. If you click a feature that contains this field, an interactive chart will appear in the pop-up pane. However, if you share this feature class as a web layer to ArcGIS Online and click a feature in Map Viewer, the chart will not appear in the pop-ups. This tool creates a feature class that contains the pop-up charts as image attachments. If the feature class with image attachments is shared as a web service to ArcGIS Online, the charts will appear in the pop-ups of the web feature layer.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "img_width": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        img_width = params.get("img_width")
        img_height = params.get("img_height")
        rotate_x_axis_labels = params.get("rotate_x_axis_labels")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Convert_Spatial_Statistics_Popup_Charts_for_Web_Display"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Convert Spatial Statistics Popup Charts for Web Display
            arcpy.ConvertSpatialStatisticsPopupChartsforWebDisplay(in_features, out_feature_class, img_width, img_height, rotate_x_axis_labels)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def convert_spatial_weights_matrix_to_table(self, params):
        """Convert Spatial Weights Matrix To Table

Converts a binary spatial weights matrix file (.swm) to a table.

        params: {"input_spatial_weights_matrix_file": <File>, "output_table": <Table>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_spatial_weights_matrix_file = params.get("input_spatial_weights_matrix_file")
        if input_spatial_weights_matrix_file is None:
            return {"success": False, "error": "input_spatial_weights_matrix_file parameter is required"}
        output_table = params.get("output_table")
        if output_table is None:
            return {"success": False, "error": "output_table parameter is required"}

            # Generate output name and path
            output_name = f"{input_spatial_weights_matrix_file.replace(' ', '_')}_Convert_Spatial_Weights_Matrix_To_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Convert Spatial Weights Matrix To Table
            arcpy.ConvertSpatialWeightsMatrixToTable(input_spatial_weights_matrix_file, output_table)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def describe_spatial_statistics_model_file(self, params):
        """Describe Spatial Statistics Model File

Describes the contents and diagnostics of a spatial statistics model file. Learn more about spatial statistics model files

        params: {"input_model": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_model = params.get("input_model")
        if input_model is None:
            return {"success": False, "error": "input_model parameter is required"}

            # Generate output name and path
            output_name = f"{input_model.replace(' ', '_')}_Describe_Spatial_Statistics_Model_File"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Describe Spatial Statistics Model File
            arcpy.DescribeSpatialStatisticsModelFile(input_model)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def dimension_reduction(self, params):
        """Dimension Reduction

Reduces the number of dimensions of a set of continuous variables by aggregating the highest possible amount of variance into fewer components using Principal Component Analysis (PCA) or Reduced-Rank Linear Discriminant Analysis (LDA). The variables are specified as fields in an input table or feature layer, and new fields representing the new variables are saved  in the output table or feature class. The number of new fields will be fewer than the number of original variables while maintaining the highest possible amount of variance from all the original variables. Dimension reduction is commonly used to explore multivariate relationships between variables and to reduce the computational cost of machine learning algorithms in which the required memory and processing time depend on the number of dimensions of the data. Using the components in place of the original data in analysis or machine learning algorithms can often provide comparable (or better) results while consuming fewer computational resources. Learn more about how Dimension Reduction works

        params: {"in_table": <Table View>, "output_data": <Table>, "fields": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        output_data = params.get("output_data")
        fields = params.get("fields")
        if fields is None:
            return {"success": False, "error": "fields parameter is required"}
        method = params.get("method")
        scale = params.get("scale")
        categorical_field = params.get("categorical_field")
        min_variance = params.get("min_variance")
        min_components = params.get("min_components")
        append_fields = params.get("append_fields")
        output_eigenvalues_table = params.get("output_eigenvalues_table")
        output_eigenvectors_table = params.get("output_eigenvectors_table")
        number_of_permutations = params.get("number_of_permutations")
        append_to_input = params.get("append_to_input")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Dimension_Reduction"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Dimension Reduction
            arcpy.DimensionReduction(in_table, output_data, fields, method, scale, categorical_field, min_variance, min_components, append_fields, output_eigenvalues_table, output_eigenvectors_table, number_of_permutations, append_to_input)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def export_feature_attributes_to_ascii(self, params):
        """Export Feature Attributes To ASCII

Exports feature class coordinates and attribute values to a space-, comma-, tab-, or semicolon-delimited ASCII text file.

        params: {"input_feature_class": <Feature Layer>, "value_field": <Field>, "delimiter": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_feature_class = params.get("input_feature_class")
        if input_feature_class is None:
            return {"success": False, "error": "input_feature_class parameter is required"}
        value_field = params.get("value_field")
        if value_field is None:
            return {"success": False, "error": "value_field parameter is required"}
        delimiter = params.get("delimiter")
        if delimiter is None:
            return {"success": False, "error": "delimiter parameter is required"}
        output_ascii_file = params.get("output_ascii_file")
        if output_ascii_file is None:
            return {"success": False, "error": "output_ascii_file parameter is required"}

            # Generate output name and path
            output_name = f"{input_feature_class.replace(' ', '_')}_Export_Feature_Attributes_To_ASCII"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Export Feature Attributes To ASCII
            arcpy.ExportFeatureAttributesToASCII(input_feature_class, value_field, delimiter, output_ascii_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_spatial_statistics_model_file_properties(self, params):
        """Set Spatial Statistics Model File Properties

Adds descriptions and units to the variables stored in a spatial statistics model file. Learn more about spatial statistics model files

        params: {"input_model": <File>, "variable_predictvar1_desc1_unit1_var2_desc2_unit2": <Value Table>, "explanatory_variablesvar1_desc1_unit1_var2_desc2_unit2": <Value Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_model = params.get("input_model")
        if input_model is None:
            return {"success": False, "error": "input_model parameter is required"}
        variable_predictvar1_desc1_unit1_var2_desc2_unit2 = params.get("variable_predictvar1_desc1_unit1_var2_desc2_unit2")
        explanatory_variablesvar1_desc1_unit1_var2_desc2_unit2 = params.get("explanatory_variablesvar1_desc1_unit1_var2_desc2_unit2")
        distance_featuresvar1_desc1_unit1_var2_desc2_unit2 = params.get("distance_featuresvar1_desc1_unit1_var2_desc2_unit2")
        explanatory_rastersvar1_desc1_unit1_var2_desc2_unit2 = params.get("explanatory_rastersvar1_desc1_unit1_var2_desc2_unit2")

            # Generate output name and path
            output_name = f"{input_model.replace(' ', '_')}_Set_Spatial_Statistics_Model_File_Properties"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Set Spatial Statistics Model File Properties
            arcpy.SetSpatialStatisticsModelFileProperties(input_model, variable_predictvar1_desc1_unit1_var2_desc2_unit2, explanatory_variablesvar1_desc1_unit1_var2_desc2_unit2, distance_featuresvar1_desc1_unit1_var2_desc2_unit2, explanatory_rastersvar1_desc1_unit1_var2_desc2_unit2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def time_series_smoothing(self, params):
        """Time Series Smoothing

Smooths a numeric variable of one or more time series using centered, forward, and backward moving averages, as well as an adaptive method based on local linear regression. After smoothing short-term fluctuations, longer-term trends or cycles often become apparent. Learn more about how Time Series Smoothing works

        params: {"in_features": <Table View>, "time_field": <Field>, "analysis_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        time_field = params.get("time_field")
        if time_field is None:
            return {"success": False, "error": "time_field parameter is required"}
        analysis_field = params.get("analysis_field")
        if analysis_field is None:
            return {"success": False, "error": "analysis_field parameter is required"}
        group_method = params.get("group_method")
        method = params.get("method")
        time_window = params.get("time_window")
        append_to_input = params.get("append_to_input")
        output_features = params.get("output_features")
        id_field = params.get("id_field")
        apply_shorter_window = params.get("apply_shorter_window")
        enable_time_series_popups = params.get("enable_time_series_popups")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Time_Series_Smoothing"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Time Series Smoothing
            arcpy.TimeSeriesSmoothing(in_features, time_field, analysis_field, group_method, method, time_window, append_to_input, output_features, id_field, apply_shorter_window, enable_time_series_popups)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_field(self, params):
        """Calculate Field

Calculates the values of a field for a feature class, feature layer, or raster.

        params: {"in_table": <Mosaic Layer; Raster Layer; Table View>, "field": <Field>, "expression": <SQL Expression>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        field = params.get("field")
        if field is None:
            return {"success": False, "error": "field parameter is required"}
        expression = params.get("expression")
        if expression is None:
            return {"success": False, "error": "expression parameter is required"}
        expression_type = params.get("expression_type")
        code_block = params.get("code_block")
        field_type = params.get("field_type")
        enforce_domains = params.get("enforce_domains")

            # Generate output name and path
            output_name = f"{in_table.replace(' ', '_')}_Calculate_Field"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Field
            arcpy.CalculateField(in_table, field, expression, expression_type, code_block, field_type, enforce_domains)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_geometry_attributes(self, params):
        """Calculate Geometry Attributes

Adds information to a feature's attribute fields representing the spatial or geometric characteristics and location of each feature, such as length or area and x-, y-, z-coordinates, and m-values.

        params: {"in_features": <Feature Layer>, "geometry_propertyfield_property": <Value Table>, "length_unit": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        geometry_propertyfield_property = params.get("geometry_propertyfield_property")
        if geometry_propertyfield_property is None:
            return {"success": False, "error": "geometry_propertyfield_property parameter is required"}
        length_unit = params.get("length_unit")
        area_unit = params.get("area_unit")
        coordinate_system = params.get("coordinate_system")
        coordinate_format = params.get("coordinate_format")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Calculate_Geometry_Attributes"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Geometry Attributes
            arcpy.CalculateGeometryAttributes(in_features, geometry_propertyfield_property, length_unit, area_unit, coordinate_system, coordinate_format)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}
