# Generated ArcGIS Pro geostatistical-analyst Progent Functions
# Generated on 2025-10-01T15:05:41.306074
# Total tools: 36

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

    def diffusion_interpolation_with_barriers(self, params):
        """Diffusion Interpolation With Barriers

Interpolates a surface using a kernel that is based upon the heat equation and allows one to use raster and feature  barriers to redefine distances between input points. Learn more about how Diffusion Interpolation With Barriers works

        params: {"in_features": <Feature Layer>, "z_field": <Field>, "out_ga_layer": <Geostatistical Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        z_field = params.get("z_field")
        if z_field is None:
            return {"success": False, "error": "z_field parameter is required"}
        out_ga_layer = params.get("out_ga_layer")
        out_raster = params.get("out_raster")
        cell_size = params.get("cell_size")
        in_barrier_features = params.get("in_barrier_features")
        bandwidth = params.get("bandwidth")
        number_iterations = params.get("number_iterations")
        weight_field = params.get("weight_field")
        in_additive_barrier_raster = params.get("in_additive_barrier_raster")
        in_cumulative_barrier_raster = params.get("in_cumulative_barrier_raster")
        in_flow_barrier_raster = params.get("in_flow_barrier_raster")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Diffusion_Interpolation_With_Barriers"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Diffusion Interpolation With Barriers
            arcpy.DiffusionInterpolationWithBarriers(in_features, z_field, out_ga_layer, out_raster, cell_size, in_barrier_features, bandwidth, number_iterations, weight_field, in_additive_barrier_raster, in_cumulative_barrier_raster, in_flow_barrier_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def ebk_regression_prediction(self, params):
        """EBK Regression Prediction

EBK Regression Prediction is a geostatistical interpolation method that uses Empirical Bayesian Kriging with explanatory variable rasters that are known to affect the value of the data that you are interpolating. This approach combines kriging with regression analysis to make predictions that are more accurate than either regression or kriging can achieve on their own. Learn more about EBK Regression Prediction

        params: {"in_features": <Feature Layer>, "dependent_field": <Field>, "in_explanatory_rastersin_explanatory_raster": <Raster Layer; Mosaic Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        dependent_field = params.get("dependent_field")
        if dependent_field is None:
            return {"success": False, "error": "dependent_field parameter is required"}
        in_explanatory_rastersin_explanatory_raster = params.get("in_explanatory_rastersin_explanatory_raster")
        if in_explanatory_rastersin_explanatory_raster is None:
            return {"success": False, "error": "in_explanatory_rastersin_explanatory_raster parameter is required"}
        out_ga_layer = params.get("out_ga_layer")
        if out_ga_layer is None:
            return {"success": False, "error": "out_ga_layer parameter is required"}
        out_raster = params.get("out_raster")
        out_diagnostic_feature_class = params.get("out_diagnostic_feature_class")
        measurement_error_field = params.get("measurement_error_field")
        min_cumulative_variance = params.get("min_cumulative_variance")
        in_subset_features = params.get("in_subset_features")
        transformation_type = params.get("transformation_type")
        semivariogram_model_type = params.get("semivariogram_model_type")
        max_local_points = params.get("max_local_points")
        overlap_factor = params.get("overlap_factor")
        number_simulations = params.get("number_simulations")
        search_neighborhood = params.get("search_neighborhood")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_EBK_Regression_Prediction"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute EBK Regression Prediction
            arcpy.EBKRegressionPrediction(in_features, dependent_field, in_explanatory_rastersin_explanatory_raster, out_ga_layer, out_raster, out_diagnostic_feature_class, measurement_error_field, min_cumulative_variance, in_subset_features, transformation_type, semivariogram_model_type, max_local_points, overlap_factor, number_simulations, search_neighborhood)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def empirical_bayesian_kriging(self, params):
        """Empirical Bayesian Kriging

Empirical Bayesian kriging is an interpolation method that accounts for the error in estimating the underlying semivariogram through repeated simulations. What is Empirical Bayesian Kriging?

        params: {"in_features": <Feature Layer>, "z_field": <Field>, "out_ga_layer": <Geostatistical Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        z_field = params.get("z_field")
        if z_field is None:
            return {"success": False, "error": "z_field parameter is required"}
        out_ga_layer = params.get("out_ga_layer")
        out_raster = params.get("out_raster")
        cell_size = params.get("cell_size")
        transformation_type = params.get("transformation_type")
        max_local_points = params.get("max_local_points")
        overlap_factor = params.get("overlap_factor")
        number_semivariograms = params.get("number_semivariograms")
        search_neighborhood = params.get("search_neighborhood")
        output_type = params.get("output_type")
        quantile_value = params.get("quantile_value")
        threshold_type = params.get("threshold_type")
        probability_threshold = params.get("probability_threshold")
        semivariogram_model_type = params.get("semivariogram_model_type")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Empirical_Bayesian_Kriging"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Empirical Bayesian Kriging
            arcpy.EmpiricalBayesianKriging(in_features, z_field, out_ga_layer, out_raster, cell_size, transformation_type, max_local_points, overlap_factor, number_semivariograms, search_neighborhood, output_type, quantile_value, threshold_type, probability_threshold, semivariogram_model_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def empirical_bayesian_kriging_3d(self, params):
        """Empirical Bayesian Kriging 3D

Interpolates 3D points using Empirical Bayesian Kriging methodology. All points must have x-, y-, and z-coordinates and a measured value to be interpolated. The output is a 3D geostatistical layer that calculates and renders itself as a 2D transect at a given elevation. The elevation of the layer can be changed using the range slider, and the layer will update to show the interpolated predictions for the new elevation. 3D interpolation has the following potential applications:

Oceanographers can create maps of dissolved oxygen and salinity at various depths in the ocean.Atmospheric scientists can create models for pollution and greenhouse gasses throughout the atmosphere.Geologists can predict subsurface geologic properties such as mineral concentrations and porosity. Learn more about Empirical Bayesian Kriging 3D

        params: {"in_features": <Feature Layer>, "elevation_field": <Field>, "value_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        elevation_field = params.get("elevation_field")
        if elevation_field is None:
            return {"success": False, "error": "elevation_field parameter is required"}
        value_field = params.get("value_field")
        if value_field is None:
            return {"success": False, "error": "value_field parameter is required"}
        out_ga_layer = params.get("out_ga_layer")
        if out_ga_layer is None:
            return {"success": False, "error": "out_ga_layer parameter is required"}
        elevation_units = params.get("elevation_units")
        measurement_error_field = params.get("measurement_error_field")
        semivariogram_model_type = params.get("semivariogram_model_type")
        transformation_type = params.get("transformation_type")
        subset_size = params.get("subset_size")
        overlap_factor = params.get("overlap_factor")
        number_simulations = params.get("number_simulations")
        trend_removal = params.get("trend_removal")
        elev_inflation_factor = params.get("elev_inflation_factor")
        search_neighborhood = params.get("search_neighborhood")
        output_elevation = params.get("output_elevation")
        output_type = params.get("output_type")
        quantile_value = params.get("quantile_value")
        threshold_type = params.get("threshold_type")
        probability_threshold = params.get("probability_threshold")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Empirical_Bayesian_Kriging_3D"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Empirical Bayesian Kriging 3D
            arcpy.EmpiricalBayesianKriging3D(in_features, elevation_field, value_field, out_ga_layer, elevation_units, measurement_error_field, semivariogram_model_type, transformation_type, subset_size, overlap_factor, number_simulations, trend_removal, elev_inflation_factor, search_neighborhood, output_elevation, output_type, quantile_value, threshold_type, probability_threshold)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def global_polynomial_interpolation(self, params):
        """Global Polynomial Interpolation

Fits a smooth surface that is defined by a mathematical function (a polynomial) to the input sample points. Learn more about how Global Polynomial Interpolation works

        params: {"in_features": <Feature Layer>, "z_field": <Field>, "out_ga_layer": <Geostatistical Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        z_field = params.get("z_field")
        if z_field is None:
            return {"success": False, "error": "z_field parameter is required"}
        out_ga_layer = params.get("out_ga_layer")
        out_raster = params.get("out_raster")
        cell_size = params.get("cell_size")
        power = params.get("power")
        weight_field = params.get("weight_field")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Global_Polynomial_Interpolation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Global Polynomial Interpolation
            arcpy.GlobalPolynomialInterpolation(in_features, z_field, out_ga_layer, out_raster, cell_size, power, weight_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def idw(self, params):
        """IDW

Uses the measured values surrounding the prediction location to predict a value for any unsampled location, based on the assumption that things that are close to one another are more alike than those that are farther apart. How IDW works

        params: {"in_features": <Feature Layer>, "z_field": <Field>, "out_ga_layer": <Geostatistical Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        z_field = params.get("z_field")
        if z_field is None:
            return {"success": False, "error": "z_field parameter is required"}
        out_ga_layer = params.get("out_ga_layer")
        out_raster = params.get("out_raster")
        cell_size = params.get("cell_size")
        power = params.get("power")
        search_neighborhood = params.get("search_neighborhood")
        weight_field = params.get("weight_field")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_IDW"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute IDW
            arcpy.IDW(in_features, z_field, out_ga_layer, out_raster, cell_size, power, search_neighborhood, weight_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def idw_3d(self, params):
        """IDW 3D

Interpolates the values of 3D points using inverse distance weighting (IDW) and creates a voxel layer and source file (.nc) of the predicted values.

        params: {"in_features": <Feature Layer>, "value_field": <Field>, "out_netcdf_file": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        value_field = params.get("value_field")
        if value_field is None:
            return {"success": False, "error": "value_field parameter is required"}
        out_netcdf_file = params.get("out_netcdf_file")
        if out_netcdf_file is None:
            return {"success": False, "error": "out_netcdf_file parameter is required"}
        power = params.get("power")
        elev_inflation_factor = params.get("elev_inflation_factor")
        out_cv_features = params.get("out_cv_features")
        x_spacing = params.get("x_spacing")
        y_spacing = params.get("y_spacing")
        elevation_spacing = params.get("elevation_spacing")
        in_study_area = params.get("in_study_area")
        min_elev_raster = params.get("min_elev_raster")
        max_elev_raster = params.get("max_elev_raster")
        search_neighborhood = params.get("search_neighborhood")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_IDW_3D"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute IDW 3D
            arcpy.IDW3D(in_features, value_field, out_netcdf_file, power, elev_inflation_factor, out_cv_features, x_spacing, y_spacing, elevation_spacing, in_study_area, min_elev_raster, max_elev_raster, search_neighborhood)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def kernel_interpolation_with_barriers(self, params):
        """Kernel Interpolation With Barriers

A moving window predictor that uses the shortest distance between points so that points on either side of the line barriers are connected. How Kernel Interpolation With Barriers works

        params: {"in_features": <Feature Layer>, "z_field": <Field>, "out_ga_layer": <Geostatistical Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        z_field = params.get("z_field")
        if z_field is None:
            return {"success": False, "error": "z_field parameter is required"}
        out_ga_layer = params.get("out_ga_layer")
        out_raster = params.get("out_raster")
        cell_size = params.get("cell_size")
        in_barrier_features = params.get("in_barrier_features")
        kernel_function = params.get("kernel_function")
        bandwidth = params.get("bandwidth")
        power = params.get("power")
        ridge = params.get("ridge")
        output_type = params.get("output_type")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Kernel_Interpolation_With_Barriers"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Kernel Interpolation With Barriers
            arcpy.KernelInterpolationWithBarriers(in_features, z_field, out_ga_layer, out_raster, cell_size, in_barrier_features, kernel_function, bandwidth, power, ridge, output_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def local_polynomial_interpolation(self, params):
        """Local Polynomial Interpolation

Fits the specified order (zero, first, second, third, and so on) polynomial, each within specified overlapping neighborhoods, to produce an output surface. How Local Polynomial Interpolation works

        params: {"in_features": <Feature Layer>, "z_field": <Field>, "out_ga_layer": <Geostatistical Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        z_field = params.get("z_field")
        if z_field is None:
            return {"success": False, "error": "z_field parameter is required"}
        out_ga_layer = params.get("out_ga_layer")
        out_raster = params.get("out_raster")
        cell_size = params.get("cell_size")
        power = params.get("power")
        search_neighborhood = params.get("search_neighborhood")
        kernel_function = params.get("kernel_function")
        bandwidth = params.get("bandwidth")
        use_condition_number = params.get("use_condition_number")
        condition_number = params.get("condition_number")
        weight_field = params.get("weight_field")
        output_type = params.get("output_type")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Local_Polynomial_Interpolation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Local Polynomial Interpolation
            arcpy.LocalPolynomialInterpolation(in_features, z_field, out_ga_layer, out_raster, cell_size, power, search_neighborhood, kernel_function, bandwidth, use_condition_number, condition_number, weight_field, output_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def moving_window_kriging(self, params):
        """Moving Window Kriging

Recalculates the Range, Nugget, and Partial Sill semivariogram parameters based on a smaller neighborhood, moving through all location points. Learn more about how Moving Window Kriging works

        params: {"in_ga_model_source": <File; Geostatistical Layer>, "in_datasets": <Geostatistical Value Table>, "in_locations": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_ga_model_source = params.get("in_ga_model_source")
        if in_ga_model_source is None:
            return {"success": False, "error": "in_ga_model_source parameter is required"}
        in_datasets = params.get("in_datasets")
        if in_datasets is None:
            return {"success": False, "error": "in_datasets parameter is required"}
        in_locations = params.get("in_locations")
        if in_locations is None:
            return {"success": False, "error": "in_locations parameter is required"}
        neighbors_max = params.get("neighbors_max")
        if neighbors_max is None:
            return {"success": False, "error": "neighbors_max parameter is required"}
        out_featureclass = params.get("out_featureclass")
        if out_featureclass is None:
            return {"success": False, "error": "out_featureclass parameter is required"}
        cell_size = params.get("cell_size")
        out_surface_grid = params.get("out_surface_grid")

            # Generate output name and path
            output_name = f"{in_ga_model_source.replace(' ', '_')}_Moving_Window_Kriging"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Moving Window Kriging
            arcpy.MovingWindowKriging(in_ga_model_source, in_datasets, in_locations, neighbors_max, out_featureclass, cell_size, out_surface_grid)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def nearest_neighbor_3d(self, params):
        """Nearest Neighbor 3D

Creates a voxel layer source file (netCDF) from categorical 3D points by assigning each voxel the categories of the nearest neighbor in 3D. Learn more about voxel layers

        params: {"in_features": <Feature Layer>, "category_field": <Field>, "out_netcdf_file": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        category_field = params.get("category_field")
        if category_field is None:
            return {"success": False, "error": "category_field parameter is required"}
        out_netcdf_file = params.get("out_netcdf_file")
        if out_netcdf_file is None:
            return {"success": False, "error": "out_netcdf_file parameter is required"}
        x_spacing = params.get("x_spacing")
        y_spacing = params.get("y_spacing")
        elevation_spacing = params.get("elevation_spacing")
        elev_inflation_factor = params.get("elev_inflation_factor")
        in_study_area = params.get("in_study_area")
        min_elev_raster = params.get("min_elev_raster")
        max_elev_raster = params.get("max_elev_raster")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Nearest_Neighbor_3D"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Nearest Neighbor 3D
            arcpy.NearestNeighbor3D(in_features, category_field, out_netcdf_file, x_spacing, y_spacing, elevation_spacing, elev_inflation_factor, in_study_area, min_elev_raster, max_elev_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def radial_basis_functions(self, params):
        """Radial Basis Functions

Uses one of five basis functions to interpolate a surfaces that passes through the input points exactly. Learn more about how radial basis functions work

        params: {"in_features": <Feature Layer>, "z_field": <Field>, "out_ga_layer": <Geostatistical Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        z_field = params.get("z_field")
        if z_field is None:
            return {"success": False, "error": "z_field parameter is required"}
        out_ga_layer = params.get("out_ga_layer")
        out_raster = params.get("out_raster")
        cell_size = params.get("cell_size")
        search_neighborhood = params.get("search_neighborhood")
        radial_basis_functions = params.get("radial_basis_functions")
        small_scale_parameter = params.get("small_scale_parameter")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Radial_Basis_Functions"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Radial Basis Functions
            arcpy.RadialBasisFunctions(in_features, z_field, out_ga_layer, out_raster, cell_size, search_neighborhood, radial_basis_functions, small_scale_parameter)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_spatially_balanced_points(self, params):
        """Create Spatially Balanced Points

Creates a set of sample points based on inclusion probabilities, resulting in a spatially balanced sample design. This tool is typically used for designing a monitoring network by suggesting locations to take samples, and a preference for particular locations can be defined using an inclusion probability raster. Learn more about how Create Spatially Balanced Points works

        params: {"in_probability_raster": <Raster Layer; Mosaic Layer>, "number_output_points": <Long>, "out_feature_class": <Feature Class>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_probability_raster = params.get("in_probability_raster")
        if in_probability_raster is None:
            return {"success": False, "error": "in_probability_raster parameter is required"}
        number_output_points = params.get("number_output_points")
        if number_output_points is None:
            return {"success": False, "error": "number_output_points parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}

            # Generate output name and path
            output_name = f"{in_probability_raster.replace(' ', '_')}_Create_Spatially_Balanced_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Spatially Balanced Points
            arcpy.CreateSpatiallyBalancedPoints(in_probability_raster, number_output_points, out_feature_class)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def densify_sampling_network(self, params):
        """Densify Sampling Network

Uses a predefined geostatistical kriging layer to determine where new monitoring stations should be built.  It can also be used to determine which monitoring stations should be removed from an existing network.

        params: {"in_geostat_layer": <Geostatistical Layer>, "number_output_points": <Long>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geostat_layer = params.get("in_geostat_layer")
        if in_geostat_layer is None:
            return {"success": False, "error": "in_geostat_layer parameter is required"}
        number_output_points = params.get("number_output_points")
        if number_output_points is None:
            return {"success": False, "error": "number_output_points parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        selection_criteria = params.get("selection_criteria")
        threshold = params.get("threshold")
        in_weight_raster = params.get("in_weight_raster")
        in_candidate_point_features = params.get("in_candidate_point_features")
        inhibition_distance = params.get("inhibition_distance")

            # Generate output name and path
            output_name = f"{in_geostat_layer.replace(' ', '_')}_Densify_Sampling_Network"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Densify Sampling Network
            arcpy.DensifySamplingNetwork(in_geostat_layer, number_output_points, out_feature_class, selection_criteria, threshold, in_weight_raster, in_candidate_point_features, inhibition_distance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_values_to_table(self, params):
        """Extract Values To Table

Extracts cell values from a set of rasters to a table, based on a point or polygon feature class.

        params: {"in_features": <Feature Layer>, "in_rastersin_raster": <Raster Layer; Mosaic Layer>, "out_table": <Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        in_rastersin_raster = params.get("in_rastersin_raster")
        if in_rastersin_raster is None:
            return {"success": False, "error": "in_rastersin_raster parameter is required"}
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}
        out_raster_names_table = params.get("out_raster_names_table")
        add_warning_field = params.get("add_warning_field")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Extract_Values_To_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract Values To Table
            arcpy.ExtractValuesToTable(in_features, in_rastersin_raster, out_table, out_raster_names_table, add_warning_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def gaussian_geostatistical_simulations(self, params):
        """Gaussian Geostatistical Simulations

Performs a conditional or unconditional geostatistical simulation based on a Simple Kriging model. The simulated rasters can be considered equally probable realizations of the kriging model. Learn more about how Gaussian Geostatistical Simulations works

        params: {"in_geostat_layer": <Geostatistical Layer>, "number_of_realizations": <Long>, "output_workspace": <Workspace>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geostat_layer = params.get("in_geostat_layer")
        if in_geostat_layer is None:
            return {"success": False, "error": "in_geostat_layer parameter is required"}
        number_of_realizations = params.get("number_of_realizations")
        if number_of_realizations is None:
            return {"success": False, "error": "number_of_realizations parameter is required"}
        output_workspace = params.get("output_workspace")
        if output_workspace is None:
            return {"success": False, "error": "output_workspace parameter is required"}
        output_simulation_prefix = params.get("output_simulation_prefix")
        if output_simulation_prefix is None:
            return {"success": False, "error": "output_simulation_prefix parameter is required"}
        in_conditioning_features = params.get("in_conditioning_features")
        conditioning_field = params.get("conditioning_field")
        cell_size = params.get("cell_size")
        in_bounding_dataset = params.get("in_bounding_dataset")
        save_simulated_rasters = params.get("save_simulated_rasters")
        quantile = params.get("quantile")
        threshold = params.get("threshold")
        in_stats_polygons = params.get("in_stats_polygons")
        raster_stat_type = params.get("raster_stat_type")
        conditioning_measurement_error_field = params.get("conditioning_measurement_error_field")

            # Generate output name and path
            output_name = f"{in_geostat_layer.replace(' ', '_')}_Gaussian_Geostatistical_Simulations"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Gaussian Geostatistical Simulations
            arcpy.GaussianGeostatisticalSimulations(in_geostat_layer, number_of_realizations, output_workspace, output_simulation_prefix, in_conditioning_features, conditioning_field, cell_size, in_bounding_dataset, save_simulated_rasters, quantile, threshold, in_stats_polygons, raster_stat_type, conditioning_measurement_error_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def compare_geostatistical_layers(self, params):
        """Compare Geostatistical Layers

Compares and ranks geostatistical layers using customizable criteria based on cross validation statistics. Interpolation results can be ranked based on a single criterion (such as highest prediction accuracy or lowest bias), weighted average ranks of multiple criteria, or hierarchical sorting of multiple criteria (in which ties by each of the criteria are broken by subsequent criteria in the hierarchy).  Exclusion criteria can also be used to exclude interpolation results from the comparison that do not meet minimal quality standards. The output is a table summarizing the cross validation statistics and ranks for each interpolation result.  Optionally, you can output a geostatistical layer of the interpolation result with highest rank to be used in further workflows.

        params: {"in_geostat_layersin_geostat_layer1_in_geostat_layer2": <Geostatistical Layer>, "out_cv_table": <Table>, "out_geostat_layer": <Geostatistical Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geostat_layersin_geostat_layer1_in_geostat_layer2 = params.get("in_geostat_layersin_geostat_layer1_in_geostat_layer2")
        if in_geostat_layersin_geostat_layer1_in_geostat_layer2 is None:
            return {"success": False, "error": "in_geostat_layersin_geostat_layer1_in_geostat_layer2 parameter is required"}
        out_cv_table = params.get("out_cv_table")
        if out_cv_table is None:
            return {"success": False, "error": "out_cv_table parameter is required"}
        out_geostat_layer = params.get("out_geostat_layer")
        comparison_method = params.get("comparison_method")
        criterion = params.get("criterion")
        criteria_hierarchycriteria1_tol_type1_tol_val1_criteria2_tol_type2_tol_val2 = params.get("criteria_hierarchycriteria1_tol_type1_tol_val1_criteria2_tol_type2_tol_val2")
        weighted_criteria1_weight1_criteria2_weight2 = params.get("weighted_criteria1_weight1_criteria2_weight2")
        exclusion_criteria1_value1_criteria2_value2 = params.get("exclusion_criteria1_value1_criteria2_value2")

            # Generate output name and path
            output_name = f"{in_geostat_layersin_geostat_layer1_in_geostat_layer2.replace(' ', '_')}_Compare_Geostatistical_Layers"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Compare Geostatistical Layers
            arcpy.CompareGeostatisticalLayers(in_geostat_layersin_geostat_layer1_in_geostat_layer2, out_cv_table, out_geostat_layer, comparison_method, criterion, criteria_hierarchycriteria1_tol_type1_tol_val1_criteria2_tol_type2_tol_val2, weighted_criteria1_weight1_criteria2_weight2, exclusion_criteria1_value1_criteria2_value2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def cross_validation(self, params):
        """Cross Validation

Removes one data location and predicts the associated data using the data at the rest of the locations. The primary use for this tool is to compare the predicted value to the observed value in order to obtain useful information about some of your model parameters. Learn more about performing cross validation and validation

        params: {"in_geostat_layer": <Geostatistical Layer>, "out_point_feature_class": <Feature Class>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geostat_layer = params.get("in_geostat_layer")
        if in_geostat_layer is None:
            return {"success": False, "error": "in_geostat_layer parameter is required"}
        out_point_feature_class = params.get("out_point_feature_class")

            # Generate output name and path
            output_name = f"{in_geostat_layer.replace(' ', '_')}_Cross_Validation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Cross Validation
            arcpy.CrossValidation(in_geostat_layer, out_point_feature_class)

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


    def exploratory_interpolation(self, params):
        """Exploratory Interpolation

Generates various interpolation results from input point features and a field. The interpolation results are then compared and ranked using customizable criteria based on cross validation statistics. Interpolation results can be ranked based on a single criterion (such as highest prediction accuracy or lowest bias), weighted average ranks of multiple criteria, or hierarchical sorting of multiple criteria (in which ties by each of the criteria are broken by subsequent criteria in the hierarchy).  Exclusion criteria can also be used to exclude interpolation results from the comparison that do not meet minimal quality standards. The output is a table summarizing the cross validation statistics and ranks for each interpolation result.  Optionally, you can output a geostatistical layer of the interpolation result with highest rank to be used in further workflows.

        params: {"in_features": <Feature Layer>, "value_field": <Field>, "out_cv_table": <Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        value_field = params.get("value_field")
        if value_field is None:
            return {"success": False, "error": "value_field parameter is required"}
        out_cv_table = params.get("out_cv_table")
        if out_cv_table is None:
            return {"success": False, "error": "out_cv_table parameter is required"}
        out_geostat_layer = params.get("out_geostat_layer")
        interp_methods = params.get("interp_methods")
        comparison_method = params.get("comparison_method")
        criterion = params.get("criterion")
        criteria_hierarchycriteria1_tol_type1_tol_val1_criteria2_tol_type2_tol_val2 = params.get("criteria_hierarchycriteria1_tol_type1_tol_val1_criteria2_tol_type2_tol_val2")
        weighted_criteria1_weight1_criteria2_weight2 = params.get("weighted_criteria1_weight1_criteria2_weight2")
        exclusion_criteria1_value1_criteria2_value2 = params.get("exclusion_criteria1_value1_criteria2_value2")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Exploratory_Interpolation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Exploratory Interpolation
            arcpy.ExploratoryInterpolation(in_features, value_field, out_cv_table, out_geostat_layer, interp_methods, comparison_method, criterion, criteria_hierarchycriteria1_tol_type1_tol_val1_criteria2_tol_type2_tol_val2, weighted_criteria1_weight1_criteria2_weight2, exclusion_criteria1_value1_criteria2_value2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def generate_subset_polygons(self, params):
        """Generate Subset Polygons

Generates nonoverlapping subset polygon features from a set of input points. The goal is to divide the points into compact, nonoverlapping subsets, and create polygon regions around each subset of points. The minimum and maximum number of points in each subset can be controlled. The process of generating subset polygon features begins by connecting all points with a linear curve and cutting this curve into segments. These segments are chosen in order to minimize the total squared distance from the center of the segment to each point in the segment given the minimum and maximum number of points that are allowed to be in each subset. Any overlaps between the segments are then removed, and new segments are created. After several iterations of segmentation and overlap removal, no overlaps will remain, and all points within each segment will be declared part of the same subset. Thiessen polygons are then generated for the input points, and all Thiessen polygons belonging to the same subset are dissolved into a single polygon feature.

        params: {"in_point_features": <Feature Layer>, "out_feature_class": <Feature Class>, "min_points_per_subset": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_point_features = params.get("in_point_features")
        if in_point_features is None:
            return {"success": False, "error": "in_point_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        min_points_per_subset = params.get("min_points_per_subset")
        max_points_per_subset = params.get("max_points_per_subset")
        coincident_points = params.get("coincident_points")

            # Generate output name and path
            output_name = f"{in_point_features.replace(' ', '_')}_Generate_Subset_Polygons"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Generate Subset Polygons
            arcpy.GenerateSubsetPolygons(in_point_features, out_feature_class, min_points_per_subset, max_points_per_subset, coincident_points)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def neighborhood_selection(self, params):
        """Neighborhood Selection

Creates a layer of points based on a user-defined neighborhood. For example, you can create a selection of points in a circular neighborhood around a location defined by the input point.

        params: {"in_dataset": <Feature Layer>, "out_layer": <Feature Layer>, "point_coord": <Point>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_dataset = params.get("in_dataset")
        if in_dataset is None:
            return {"success": False, "error": "in_dataset parameter is required"}
        out_layer = params.get("out_layer")
        if out_layer is None:
            return {"success": False, "error": "out_layer parameter is required"}
        point_coord = params.get("point_coord")
        if point_coord is None:
            return {"success": False, "error": "point_coord parameter is required"}
        neighbors_max = params.get("neighbors_max")
        if neighbors_max is None:
            return {"success": False, "error": "neighbors_max parameter is required"}
        neighbors_min = params.get("neighbors_min")
        if neighbors_min is None:
            return {"success": False, "error": "neighbors_min parameter is required"}
        minor_semiaxis = params.get("minor_semiaxis")
        if minor_semiaxis is None:
            return {"success": False, "error": "minor_semiaxis parameter is required"}
        major_semiaxis = params.get("major_semiaxis")
        if major_semiaxis is None:
            return {"success": False, "error": "major_semiaxis parameter is required"}
        angle = params.get("angle")
        if angle is None:
            return {"success": False, "error": "angle parameter is required"}
        shape_type = params.get("shape_type")

            # Generate output name and path
            output_name = f"{in_dataset.replace(' ', '_')}_Neighborhood_Selection"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Neighborhood Selection
            arcpy.NeighborhoodSelection(in_dataset, out_layer, point_coord, neighbors_max, neighbors_min, minor_semiaxis, major_semiaxis, angle, shape_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def semivariogram_sensitivity(self, params):
        """Semivariogram Sensitivity

This tool performs a sensitivity analysis on the predicted values and associated standard errors by changing the model's semivariogram parameters (the nugget, partial sill, and major/minor ranges) within a percentage of the original values. The tool takes a geostatistical model source in order to populate these initial values of the nugget, partial sill, and major/minor ranges. The tool's output is a table indicating which parameter values were used and what the resulting predicted and standard error values were. If there are large fluctuations in the output with small changes in the model's parameter values, then you cannot have much confidence in the output. On the other hand, if changes in the output are small, then you can be confident in the model's predictions and make decisions based on its output.

        params: {"in_ga_model_source": <File; Geostatistical Layer>, "in_datasets": <Geostatistical Value Table>, "in_locations": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_ga_model_source = params.get("in_ga_model_source")
        if in_ga_model_source is None:
            return {"success": False, "error": "in_ga_model_source parameter is required"}
        in_datasets = params.get("in_datasets")
        if in_datasets is None:
            return {"success": False, "error": "in_datasets parameter is required"}
        in_locations = params.get("in_locations")
        if in_locations is None:
            return {"success": False, "error": "in_locations parameter is required"}
        nugget_span_percents = params.get("nugget_span_percents")
        nugget_calc_times = params.get("nugget_calc_times")
        partialsill_span_percents = params.get("partialsill_span_percents")
        partialsill_calc_times = params.get("partialsill_calc_times")
        range_span_percents = params.get("range_span_percents")
        range_calc_times = params.get("range_calc_times")
        minrange_span_percents = params.get("minrange_span_percents")
        minrange_calc_times = params.get("minrange_calc_times")
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}

            # Generate output name and path
            output_name = f"{in_ga_model_source.replace(' ', '_')}_Semivariogram_Sensitivity"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Semivariogram Sensitivity
            arcpy.SemivariogramSensitivity(in_ga_model_source, in_datasets, in_locations, nugget_span_percents, nugget_calc_times, partialsill_span_percents, partialsill_calc_times, range_span_percents, range_calc_times, minrange_span_percents, minrange_calc_times, out_table)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def subset_features(self, params):
        """Subset Features

Divides the records of a feature class or table into two subsets: one subset to be used as training data, and one subset to be used as test features to compare and validate the output surface.

        params: {"in_features": <Table View>, "out_training_feature_class": <Feature Class; Table>, "out_test_feature_class": <Feature Class; Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_training_feature_class = params.get("out_training_feature_class")
        if out_training_feature_class is None:
            return {"success": False, "error": "out_training_feature_class parameter is required"}
        out_test_feature_class = params.get("out_test_feature_class")
        size_of_training_dataset = params.get("size_of_training_dataset")
        subset_size_units = params.get("subset_size_units")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Subset_Features"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Subset Features
            arcpy.SubsetFeatures(in_features, out_training_feature_class, out_test_feature_class, size_of_training_dataset, subset_size_units)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def areal_interpolation_layer_to_polygons(self, params):
        """Areal Interpolation Layer To Polygons

Reaggregates the predictions of an Areal Interpolation layer to a new set of polygons. Learn more about Areal Interpolation

        params: {"in_areal_interpolation_layer": <Geostatistical Layer>, "in_polygon_features": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_areal_interpolation_layer = params.get("in_areal_interpolation_layer")
        if in_areal_interpolation_layer is None:
            return {"success": False, "error": "in_areal_interpolation_layer parameter is required"}
        in_polygon_features = params.get("in_polygon_features")
        if in_polygon_features is None:
            return {"success": False, "error": "in_polygon_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        append_all_fields = params.get("append_all_fields")

            # Generate output name and path
            output_name = f"{in_areal_interpolation_layer.replace(' ', '_')}_Areal_Interpolation_Layer_To_Polygons"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Areal Interpolation Layer To Polygons
            arcpy.ArealInterpolationLayerToPolygons(in_areal_interpolation_layer, in_polygon_features, out_feature_class, append_all_fields)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_z_value(self, params):
        """Calculate Z Value

Uses the interpolation model in a geostatistical layer to predict a value at a single location.

        params: {"in_geostat_layer": <Geostatistical Layer>, "point_coord": <Point>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geostat_layer = params.get("in_geostat_layer")
        if in_geostat_layer is None:
            return {"success": False, "error": "in_geostat_layer parameter is required"}
        point_coord = params.get("point_coord")
        if point_coord is None:
            return {"success": False, "error": "point_coord parameter is required"}

            # Generate output name and path
            output_name = f"{in_geostat_layer.replace(' ', '_')}_Calculate_Z_Value"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Z Value
            arcpy.CalculateZValue(in_geostat_layer, point_coord)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_geostatistical_layer(self, params):
        """Create Geostatistical Layer

Creates a new geostatistical layer. An  existing geostatistical layer  is required to populate the initial values for the new layer.

        params: {"in_ga_model_source": <File; Geostatistical Layer>, "in_datasets": <Geostatistical Value Table>, "out_layer": <Geostatistical Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_ga_model_source = params.get("in_ga_model_source")
        if in_ga_model_source is None:
            return {"success": False, "error": "in_ga_model_source parameter is required"}
        in_datasets = params.get("in_datasets")
        if in_datasets is None:
            return {"success": False, "error": "in_datasets parameter is required"}
        out_layer = params.get("out_layer")
        if out_layer is None:
            return {"success": False, "error": "out_layer parameter is required"}

            # Generate output name and path
            output_name = f"{in_ga_model_source.replace(' ', '_')}_Create_Geostatistical_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Geostatistical Layer
            arcpy.CreateGeostatisticalLayer(in_ga_model_source, in_datasets, out_layer)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def ga_layer_3d_to_multidimensional_raster(self, params):
        """GA Layer 3D To Multidimensional Raster

Exports a 3D geostatistical layer created using the Empirical Bayesian Kriging 3D tool to a multidimensional Cloud Raster Format (*.crf file) 

raster dataset. Tools in the Multidimensional Analysis toolset of the Image Analyst toolbox are designed to work directly on multidimensional rasters and can identify the 3D nature of the data. 3D geostatistical layers store continuous 3D interpolation results and appear as 2D horizontal slices at a given elevation.  The current elevation can be changed with the range slider, and the layer will calculate and render the predicted values of the new elevation.  Rasters of interpolated predictions can be extracted at any elevation using the GA Layer To Rasters tool.  The GA Layer 3D To Multidimensional Raster tool automates the process of extracting rasters at multiple elevations and stores them as a multidimensional raster dataset.

        params: {"in_3d_geostat_layer": <Geostatistical Layer>, "out_multidimensional_raster": <Raster Dataset>, "cell_size": <Analysis Cell Size>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_3d_geostat_layer = params.get("in_3d_geostat_layer")
        if in_3d_geostat_layer is None:
            return {"success": False, "error": "in_3d_geostat_layer parameter is required"}
        out_multidimensional_raster = params.get("out_multidimensional_raster")
        if out_multidimensional_raster is None:
            return {"success": False, "error": "out_multidimensional_raster parameter is required"}
        cell_size = params.get("cell_size")
        explicit_only = params.get("explicit_only")
        min_elev = params.get("min_elev")
        max_elev = params.get("max_elev")
        elev_interval = params.get("elev_interval")
        elev_values = params.get("elev_values")
        elev_units = params.get("elev_units")
        output_type = params.get("output_type")
        quantile_probability_value = params.get("quantile_probability_value")
        additional_outputsoutput_type_quantile_probability_value = params.get("additional_outputsoutput_type_quantile_probability_value")
        build_transpose = params.get("build_transpose")

            # Generate output name and path
            output_name = f"{in_3d_geostat_layer.replace(' ', '_')}_GA_Layer_3D_To_Multidimensional_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute GA Layer 3D To Multidimensional Raster
            arcpy.GALayer3DToMultidimensionalRaster(in_3d_geostat_layer, out_multidimensional_raster, cell_size, explicit_only, min_elev, max_elev, elev_interval, elev_values, elev_units, output_type, quantile_probability_value, additional_outputsoutput_type_quantile_probability_value, build_transpose)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def empirical_bayesian_kriging_3d(self, params):
        """Empirical Bayesian Kriging 3D

Interpolates 3D points using Empirical Bayesian Kriging methodology. All points must have x-, y-, and z-coordinates and a measured value to be interpolated. The output is a 3D geostatistical layer that calculates and renders itself as a 2D transect at a given elevation. The elevation of the layer can be changed using the range slider, and the layer will update to show the interpolated predictions for the new elevation. 3D interpolation has the following potential applications:

Oceanographers can create maps of dissolved oxygen and salinity at various depths in the ocean.Atmospheric scientists can create models for pollution and greenhouse gasses throughout the atmosphere.Geologists can predict subsurface geologic properties such as mineral concentrations and porosity. Learn more about Empirical Bayesian Kriging 3D

        params: {"in_features": <Feature Layer>, "elevation_field": <Field>, "value_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        elevation_field = params.get("elevation_field")
        if elevation_field is None:
            return {"success": False, "error": "elevation_field parameter is required"}
        value_field = params.get("value_field")
        if value_field is None:
            return {"success": False, "error": "value_field parameter is required"}
        out_ga_layer = params.get("out_ga_layer")
        if out_ga_layer is None:
            return {"success": False, "error": "out_ga_layer parameter is required"}
        elevation_units = params.get("elevation_units")
        measurement_error_field = params.get("measurement_error_field")
        semivariogram_model_type = params.get("semivariogram_model_type")
        transformation_type = params.get("transformation_type")
        subset_size = params.get("subset_size")
        overlap_factor = params.get("overlap_factor")
        number_simulations = params.get("number_simulations")
        trend_removal = params.get("trend_removal")
        elev_inflation_factor = params.get("elev_inflation_factor")
        search_neighborhood = params.get("search_neighborhood")
        output_elevation = params.get("output_elevation")
        output_type = params.get("output_type")
        quantile_value = params.get("quantile_value")
        threshold_type = params.get("threshold_type")
        probability_threshold = params.get("probability_threshold")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Empirical_Bayesian_Kriging_3D"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Empirical Bayesian Kriging 3D
            arcpy.EmpiricalBayesianKriging3D(in_features, elevation_field, value_field, out_ga_layer, elevation_units, measurement_error_field, semivariogram_model_type, transformation_type, subset_size, overlap_factor, number_simulations, trend_removal, elev_inflation_factor, search_neighborhood, output_elevation, output_type, quantile_value, threshold_type, probability_threshold)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def ga_layer_3d_to_netcdf(self, params):
        """GA Layer 3D To NetCDF

Exports one or more 3D geostatistical layers created using the Empirical Bayesian Kriging 3D tool to netCDF format (*.nc file). The output file is displayed as a voxel layer in a local scene. Learn more about voxel layers

        params: {"in_3d_geostat_layers": <Geostatistical Layer>, "out_netcdf_file": <File>, "export_locations": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_3d_geostat_layers = params.get("in_3d_geostat_layers")
        if in_3d_geostat_layers is None:
            return {"success": False, "error": "in_3d_geostat_layers parameter is required"}
        out_netcdf_file = params.get("out_netcdf_file")
        if out_netcdf_file is None:
            return {"success": False, "error": "out_netcdf_file parameter is required"}
        export_locations = params.get("export_locations")
        x_spacing = params.get("x_spacing")
        y_spacing = params.get("y_spacing")
        elevation_spacing = params.get("elevation_spacing")
        in_points_3d = params.get("in_points_3d")
        output_variableslayer_name_output_type_quantile_probability_value = params.get("output_variableslayer_name_output_type_quantile_probability_value")
        in_study_area = params.get("in_study_area")
        min_elev_raster = params.get("min_elev_raster")
        max_elev_raster = params.get("max_elev_raster")

            # Generate output name and path
            output_name = f"{in_3d_geostat_layers.replace(' ', '_')}_GA_Layer_3D_To_NetCDF"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute GA Layer 3D To NetCDF
            arcpy.GALayer3DToNetCDF(in_3d_geostat_layers, out_netcdf_file, export_locations, x_spacing, y_spacing, elevation_spacing, in_points_3d, output_variableslayer_name_output_type_quantile_probability_value, in_study_area, min_elev_raster, max_elev_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def ga_layer_to_contour(self, params):
        """GA Layer To Contour

Creates a feature class of contours from a geostatistical layer. The output feature class can be either a line feature class of contour lines or a polygon feature class of filled contours.

        params: {"in_geostat_layer": <Geostatistical Layer>, "contour_type": <String>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geostat_layer = params.get("in_geostat_layer")
        if in_geostat_layer is None:
            return {"success": False, "error": "in_geostat_layer parameter is required"}
        contour_type = params.get("contour_type")
        if contour_type is None:
            return {"success": False, "error": "contour_type parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        contour_quality = params.get("contour_quality")
        classification_type = params.get("classification_type")
        classes_count = params.get("classes_count")
        classes_breaks = params.get("classes_breaks")
        out_elevation = params.get("out_elevation")

            # Generate output name and path
            output_name = f"{in_geostat_layer.replace(' ', '_')}_GA_Layer_To_Contour"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute GA Layer To Contour
            arcpy.GALayerToContour(in_geostat_layer, contour_type, out_feature_class, contour_quality, classification_type, classes_count, classes_breaks, out_elevation)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def ga_layer_to_grid(self, params):
        """GA Layer To Grid

Exports a Geostatistical layer to a raster. Learn more about the fundamentals of creating a raster from a geostatistical layer

        params: {"in_geostat_layer": <Geostatistical Layer>, "out_surface_grid": <Raster Dataset>, "cell_size": <Analysis Cell Size>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geostat_layer = params.get("in_geostat_layer")
        if in_geostat_layer is None:
            return {"success": False, "error": "in_geostat_layer parameter is required"}
        out_surface_grid = params.get("out_surface_grid")
        if out_surface_grid is None:
            return {"success": False, "error": "out_surface_grid parameter is required"}
        cell_size = params.get("cell_size")
        points_per_block_horz = params.get("points_per_block_horz")
        points_per_block_vert = params.get("points_per_block_vert")

            # Generate output name and path
            output_name = f"{in_geostat_layer.replace(' ', '_')}_GA_Layer_To_Grid"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute GA Layer To Grid
            arcpy.GALayerToGrid(in_geostat_layer, out_surface_grid, cell_size, points_per_block_horz, points_per_block_vert)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def ga_layer_to_points(self, params):
        """GA Layer To Points

Exports a geostatistical layer to points. The tool can also be used to predict values at unmeasured locations or to validate predictions made at measured locations.

        params: {"in_geostat_layer": <Geostatistical Layer>, "in_locations": <Feature Layer>, "z_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geostat_layer = params.get("in_geostat_layer")
        if in_geostat_layer is None:
            return {"success": False, "error": "in_geostat_layer parameter is required"}
        in_locations = params.get("in_locations")
        if in_locations is None:
            return {"success": False, "error": "in_locations parameter is required"}
        z_field = params.get("z_field")
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        append_all_fields = params.get("append_all_fields")
        elevation_field = params.get("elevation_field")
        elevation_units = params.get("elevation_units")

            # Generate output name and path
            output_name = f"{in_geostat_layer.replace(' ', '_')}_GA_Layer_To_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute GA Layer To Points
            arcpy.GALayerToPoints(in_geostat_layer, in_locations, z_field, out_feature_class, append_all_fields, elevation_field, elevation_units)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def ga_layer_to_rasters(self, params):
        """GA Layer To Rasters

Exports a geostatistical layer to one or multiple rasters. Learn more about creating a raster from a geostatistical layer

        params: {"in_geostat_layer": <Geostatistical Layer>, "out_raster": <Raster Dataset>, "output_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_geostat_layer = params.get("in_geostat_layer")
        if in_geostat_layer is None:
            return {"success": False, "error": "in_geostat_layer parameter is required"}
        out_raster = params.get("out_raster")
        if out_raster is None:
            return {"success": False, "error": "out_raster parameter is required"}
        output_type = params.get("output_type")
        quantile_probability_value = params.get("quantile_probability_value")
        cell_size = params.get("cell_size")
        points_per_block_horz = params.get("points_per_block_horz")
        points_per_block_vert = params.get("points_per_block_vert")
        additional_rastersout_raster_output_type_quantile_probability_value = params.get("additional_rastersout_raster_output_type_quantile_probability_value")
        out_elevation = params.get("out_elevation")

            # Generate output name and path
            output_name = f"{in_geostat_layer.replace(' ', '_')}_GA_Layer_To_Rasters"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute GA Layer To Rasters
            arcpy.GALayerToRasters(in_geostat_layer, out_raster, output_type, quantile_probability_value, cell_size, points_per_block_horz, points_per_block_vert, additional_rastersout_raster_output_type_quantile_probability_value, out_elevation)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def get_model_parameter(self, params):
        """Get Model Parameter

Gets model parameter value from an existing geostatistical model source.

        params: {"in_ga_model_source": <File; Geostatistical Layer>, "model_param_xpath": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_ga_model_source = params.get("in_ga_model_source")
        if in_ga_model_source is None:
            return {"success": False, "error": "in_ga_model_source parameter is required"}
        model_param_xpath = params.get("model_param_xpath")
        if model_param_xpath is None:
            return {"success": False, "error": "model_param_xpath parameter is required"}

            # Generate output name and path
            output_name = f"{in_ga_model_source.replace(' ', '_')}_Get_Model_Parameter"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Get Model Parameter
            arcpy.GetModelParameter(in_ga_model_source, model_param_xpath)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_model_parameter(self, params):
        """Set Model Parameter

Sets parameter values in an existing geostatistical model source.

        params: {"in_ga_model_source": <File; Geostatistical Layer>, "model_param_xpath": <String>, "in_param_value": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_ga_model_source = params.get("in_ga_model_source")
        if in_ga_model_source is None:
            return {"success": False, "error": "in_ga_model_source parameter is required"}
        model_param_xpath = params.get("model_param_xpath")
        if model_param_xpath is None:
            return {"success": False, "error": "model_param_xpath parameter is required"}
        in_param_value = params.get("in_param_value")
        if in_param_value is None:
            return {"success": False, "error": "in_param_value parameter is required"}
        out_ga_model = params.get("out_ga_model")
        if out_ga_model is None:
            return {"success": False, "error": "out_ga_model parameter is required"}

            # Generate output name and path
            output_name = f"{in_ga_model_source.replace(' ', '_')}_Set_Model_Parameter"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Set Model Parameter
            arcpy.SetModelParameter(in_ga_model_source, model_param_xpath, in_param_value, out_ga_model)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}
