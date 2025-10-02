import arcpy
import os

class GeostatisticalAnalystTools:
    """A collection of Geostatistical Analyst tools."""

    def _add_to_map(self, path):
        try:
            aprx = arcpy.mp.ArcGISProject('CURRENT')
            map_obj = aprx.activeMap
            if map_obj:
                map_obj.addDataFromPath(path)
        except Exception as e:
            print(f'Could not add {path} to map: {e}')

    def diffusion_interpolation_with_barriers(self, params):
        """
        Diffusion Interpolation With Barriers
        Interpolates a surface using a kernel that is based upon the heat equation and allows one to use raster and feature barriers to redefine distances between input points.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            z_field = params.get("z_field")
            if z_field is None:
                return {"success": False, "error": "z_field parameter is required"}
            out_ga_layer = params.get("out_ga_layer")
            out_raster = params.get("out_raster")

            if not out_ga_layer and not out_raster:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_raster = arcpy.CreateUniqueName("DiffusionInterpolation_Output", aprx.defaultGeodatabase)

            cell_size = params.get("cell_size")
            in_barrier_features = params.get("in_barrier_features")
            bandwidth = params.get("bandwidth")
            number_iterations = params.get("number_iterations")
            weight_field = params.get("weight_field")
            in_additive_barrier_raster = params.get("in_additive_barrier_raster")
            in_cumulative_barrier_raster = params.get("in_cumulative_barrier_raster")
            in_flow_barrier_raster = params.get("in_flow_barrier_raster")

            arcpy.ga.DiffusionInterpolationWithBarriers(in_features, z_field, out_ga_layer, out_raster, cell_size, in_barrier_features, bandwidth, number_iterations, weight_field, in_additive_barrier_raster, in_cumulative_barrier_raster, in_flow_barrier_raster)

            output_path = out_raster if out_raster else out_ga_layer
            if output_path:
                output_name = os.path.basename(output_path)
                self._add_to_map(output_path)
                return {"success": True, "output_layer": output_name, "output_path": output_path}
            return {"success": True, "message": "Diffusion Interpolation With Barriers completed successfully."}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def ebk_regression_prediction(self, params):
        """
        EBK Regression Prediction
        A geostatistical interpolation method that uses Empirical Bayesian Kriging with explanatory variable rasters that are known to affect the value of the data that you are interpolating.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            dependent_field = params.get("dependent_field")
            if dependent_field is None: return {"success": False, "error": "dependent_field is required"}
            in_explanatory_rasters = params.get("in_explanatory_rasters")
            if in_explanatory_rasters is None: return {"success": False, "error": "in_explanatory_rasters is required"}
            out_ga_layer = params.get("out_ga_layer")
            out_raster = params.get("out_raster")

            if not out_ga_layer and not out_raster:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_raster = arcpy.CreateUniqueName("EBKRegression_Output", aprx.defaultGeodatabase)

            out_diagnostic_feature_class = params.get("out_diagnostic_feature_class")
            measurement_error_field = params.get("measurement_error_field")
            min_cumulative_variance = params.get("min_cumulative_variance")
            in_subset_features = params.get("in_subset_features")
            transformation_type = params.get("transformation_type", "NONE")
            semivariogram_model_type = params.get("semivariogram_model_type", "POWER")
            max_local_points = params.get("max_local_points", 50)
            overlap_factor = params.get("overlap_factor", 1)
            number_simulations = params.get("number_simulations", 100)
            search_neighborhood = params.get("search_neighborhood")

            arcpy.ga.EBKRegressionPrediction(in_features, dependent_field, in_explanatory_rasters, out_ga_layer, out_raster, out_diagnostic_feature_class, measurement_error_field, min_cumulative_variance, in_subset_features, transformation_type, semivariogram_model_type, max_local_points, overlap_factor, number_simulations, search_neighborhood)

            output_path = out_raster if out_raster else out_ga_layer
            if output_path:
                output_name = os.path.basename(output_path)
                self._add_to_map(output_path)
                return {"success": True, "output_layer": output_name, "output_path": output_path}
            return {"success": True, "message": "EBK Regression Prediction completed successfully."}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def empirical_bayesian_kriging(self, params):
        """
        Empirical Bayesian Kriging
        An interpolation method that accounts for the error in estimating the underlying semivariogram through repeated simulations.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            z_field = params.get("z_field")
            if z_field is None: return {"success": False, "error": "z_field is required"}
            out_ga_layer = params.get("out_ga_layer")
            out_raster = params.get("out_raster")

            if not out_ga_layer and not out_raster:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_raster = arcpy.CreateUniqueName("EBK_Output", aprx.defaultGeodatabase)

            cell_size = params.get("cell_size")
            transformation_type = params.get("transformation_type", "NONE")
            max_local_points = params.get("max_local_points", 100)
            overlap_factor = params.get("overlap_factor", 1)
            number_semivariograms = params.get("number_semivariograms", 100)
            search_neighborhood = params.get("search_neighborhood")
            output_type = params.get("output_type", "PREDICTION")
            quantile_value = params.get("quantile_value", 0.5)
            threshold_type = params.get("threshold_type", "EXCEED")
            probability_threshold = params.get("probability_threshold")
            semivariogram_model_type = params.get("semivariogram_model_type", "POWER")

            arcpy.ga.EmpiricalBayesianKriging(in_features, z_field, out_ga_layer, out_raster, cell_size, transformation_type, max_local_points, overlap_factor, number_semivariograms, search_neighborhood, output_type, quantile_value, threshold_type, probability_threshold, semivariogram_model_type)

            output_path = out_raster if out_raster else out_ga_layer
            if output_path:
                output_name = os.path.basename(output_path)
                self._add_to_map(output_path)
                return {"success": True, "output_layer": output_name, "output_path": output_path}
            return {"success": True, "message": "Empirical Bayesian Kriging completed successfully."}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def empirical_bayesian_kriging_3d(self, params):
        """
        Empirical Bayesian Kriging 3D
        Interpolates 3D points using Empirical Bayesian Kriging methodology.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            elevation_field = params.get("elevation_field")
            if elevation_field is None: return {"success": False, "error": "elevation_field is required"}
            value_field = params.get("value_field")
            if value_field is None: return {"success": False, "error": "value_field is required"}
            out_ga_layer = params.get("out_ga_layer")
            if out_ga_layer is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_ga_layer = arcpy.CreateUniqueName("EBK3D_Output_Layer", aprx.defaultGeodatabase)

            elevation_units = params.get("elevation_units")
            measurement_error_field = params.get("measurement_error_field")
            semivariogram_model_type = params.get("semivariogram_model_type", "EXPONENTIAL_DETRENDED")
            transformation_type = params.get("transformation_type", "NONE")
            subset_size = params.get("subset_size", 100)
            overlap_factor = params.get("overlap_factor", 1)
            number_simulations = params.get("number_simulations", 100)
            trend_removal = params.get("trend_removal", "FIRST")
            elev_inflation_factor = params.get("elev_inflation_factor")
            search_neighborhood = params.get("search_neighborhood")
            output_elevation = params.get("output_elevation")
            output_type = params.get("output_type", "PREDICTION")
            quantile_value = params.get("quantile_value", 0.5)
            threshold_type = params.get("threshold_type", "EXCEED")
            probability_threshold = params.get("probability_threshold")

            arcpy.ga.EmpiricalBayesianKriging3D(in_features, elevation_field, value_field, out_ga_layer, elevation_units, measurement_error_field, semivariogram_model_type, transformation_type, subset_size, overlap_factor, number_simulations, trend_removal, elev_inflation_factor, search_neighborhood, output_elevation, output_type, quantile_value, threshold_type, probability_threshold)

            output_name = os.path.basename(out_ga_layer)
            self._add_to_map(out_ga_layer)
            return {"success": True, "output_layer": output_name, "output_path": out_ga_layer}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def global_polynomial_interpolation(self, params):
        """
        Global Polynomial Interpolation
        Fits a smooth surface that is defined by a mathematical function (a polynomial) to the input sample points.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            z_field = params.get("z_field")
            if z_field is None: return {"success": False, "error": "z_field is required"}
            out_ga_layer = params.get("out_ga_layer")
            out_raster = params.get("out_raster")

            if not out_ga_layer and not out_raster:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_raster = arcpy.CreateUniqueName("GlobalPoly_Output", aprx.defaultGeodatabase)

            cell_size = params.get("cell_size")
            power = params.get("power", 2)
            weight_field = params.get("weight_field")

            arcpy.ga.GlobalPolynomialInterpolation(in_features, z_field, out_ga_layer, out_raster, cell_size, power, weight_field)

            output_path = out_raster if out_raster else out_ga_layer
            if output_path:
                output_name = os.path.basename(output_path)
                self._add_to_map(output_path)
                return {"success": True, "output_layer": output_name, "output_path": output_path}
            return {"success": True, "message": "Global Polynomial Interpolation completed successfully."}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def idw(self, params):
        """
        IDW
        Uses the measured values surrounding the prediction location to predict a value for any unsampled location.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            z_field = params.get("z_field")
            if z_field is None: return {"success": False, "error": "z_field is required"}
            out_ga_layer = params.get("out_ga_layer")
            out_raster = params.get("out_raster")

            if not out_ga_layer and not out_raster:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_raster = arcpy.CreateUniqueName("IDW_Output", aprx.defaultGeodatabase)

            cell_size = params.get("cell_size")
            power = params.get("power", 2)
            search_neighborhood = params.get("search_neighborhood")
            weight_field = params.get("weight_field")

            arcpy.ga.IDW(in_features, z_field, out_ga_layer, out_raster, cell_size, power, search_neighborhood, weight_field)

            output_path = out_raster if out_raster else out_ga_layer
            if output_path:
                output_name = os.path.basename(output_path)
                self._add_to_map(output_path)
                return {"success": True, "output_layer": output_name, "output_path": output_path}
            return {"success": True, "message": "IDW completed successfully."}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def idw_3d(self, params):
        """
        IDW 3D
        Interpolates the values of 3D points using inverse distance weighting (IDW) and creates a voxel layer.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            value_field = params.get("value_field")
            if value_field is None: return {"success": False, "error": "value_field is required"}
            out_netcdf_file = params.get("out_netcdf_file")
            if out_netcdf_file is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_netcdf_file = arcpy.CreateUniqueName("IDW3D_Output", aprx.scratchFolder, "nc")

            power = params.get("power", 2)
            elev_inflation_factor = params.get("elev_inflation_factor")
            out_cv_features = params.get("out_cv_features")
            x_spacing = params.get("x_spacing")
            y_spacing = params.get("y_spacing")
            elevation_spacing = params.get("elevation_spacing")
            in_study_area = params.get("in_study_area")
            min_elev_raster = params.get("min_elev_raster")
            max_elev_raster = params.get("max_elev_raster")
            search_neighborhood = params.get("search_neighborhood")

            arcpy.ga.IDW3D(in_features, value_field, out_netcdf_file, power, elev_inflation_factor, out_cv_features, x_spacing, y_spacing, elevation_spacing, in_study_area, min_elev_raster, max_elev_raster, search_neighborhood)

            output_name = os.path.basename(out_netcdf_file)
            # Voxel layers are added to scenes, not maps, special handling may be needed.
            # self._add_to_map(out_netcdf_file)
            return {"success": True, "output_file": output_name, "output_path": out_netcdf_file}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def kernel_interpolation_with_barriers(self, params):
        """
        Kernel Interpolation With Barriers
        A moving window predictor that uses the shortest distance between points so that points on either side of the line barriers are connected.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            z_field = params.get("z_field")
            if z_field is None: return {"success": False, "error": "z_field is required"}
            out_ga_layer = params.get("out_ga_layer")
            out_raster = params.get("out_raster")

            if not out_ga_layer and not out_raster:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_raster = arcpy.CreateUniqueName("KernelInterpolation_Output", aprx.defaultGeodatabase)

            cell_size = params.get("cell_size")
            in_barrier_features = params.get("in_barrier_features")
            kernel_function = params.get("kernel_function", "EXPONENTIAL")
            bandwidth = params.get("bandwidth")
            power = params.get("power", 2)
            ridge = params.get("ridge")
            output_type = params.get("output_type", "PREDICTION")

            arcpy.ga.KernelInterpolationWithBarriers(in_features, z_field, out_ga_layer, out_raster, cell_size, in_barrier_features, kernel_function, bandwidth, power, ridge, output_type)

            output_path = out_raster if out_raster else out_ga_layer
            if output_path:
                output_name = os.path.basename(output_path)
                self._add_to_map(output_path)
                return {"success": True, "output_layer": output_name, "output_path": output_path}
            return {"success": True, "message": "Kernel Interpolation With Barriers completed successfully."}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def local_polynomial_interpolation(self, params):
        """
        Local Polynomial Interpolation
        Fits the specified order polynomial, each within specified overlapping neighborhoods, to produce an output surface.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            z_field = params.get("z_field")
            if z_field is None: return {"success": False, "error": "z_field is required"}
            out_ga_layer = params.get("out_ga_layer")
            out_raster = params.get("out_raster")

            if not out_ga_layer and not out_raster:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_raster = arcpy.CreateUniqueName("LocalPoly_Output", aprx.defaultGeodatabase)

            cell_size = params.get("cell_size")
            power = params.get("power", 2)
            search_neighborhood = params.get("search_neighborhood")
            kernel_function = params.get("kernel_function", "EPANECHNIKOV")
            bandwidth = params.get("bandwidth")
            use_condition_number = params.get("use_condition_number", "USE_CONDITION_NUMBER")
            condition_number = params.get("condition_number")
            weight_field = params.get("weight_field")
            output_type = params.get("output_type", "PREDICTION")

            arcpy.ga.LocalPolynomialInterpolation(in_features, z_field, out_ga_layer, out_raster, cell_size, power, search_neighborhood, kernel_function, bandwidth, use_condition_number, condition_number, weight_field, output_type)

            output_path = out_raster if out_raster else out_ga_layer
            if output_path:
                output_name = os.path.basename(output_path)
                self._add_to_map(output_path)
                return {"success": True, "output_layer": output_name, "output_path": output_path}
            return {"success": True, "message": "Local Polynomial Interpolation completed successfully."}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def moving_window_kriging(self, params):
        """
        Moving Window Kriging
        Recalculates the Range, Nugget, and Partial Sill semivariogram parameters based on a smaller neighborhood.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_ga_model_source = params.get("in_ga_model_source")
            if in_ga_model_source is None: return {"success": False, "error": "in_ga_model_source is required"}
            in_datasets = params.get("in_datasets")
            if in_datasets is None: return {"success": False, "error": "in_datasets is required"}
            in_locations = params.get("in_locations")
            if in_locations is None: return {"success": False, "error": "in_locations is required"}
            neighbors_max = params.get("neighbors_max")
            if neighbors_max is None: return {"success": False, "error": "neighbors_max is required"}
            out_featureclass = params.get("out_featureclass")
            if out_featureclass is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_featureclass = arcpy.CreateUniqueName("MovingWindowKriging_Output", aprx.defaultGeodatabase)

            cell_size = params.get("cell_size")
            out_surface_grid = params.get("out_surface_grid")

            arcpy.ga.MovingWindowKriging(in_ga_model_source, in_datasets, in_locations, neighbors_max, out_featureclass, cell_size, out_surface_grid)

            output_name = os.path.basename(out_featureclass)
            self._add_to_map(out_featureclass)
            return {"success": True, "output_layer": output_name, "output_path": out_featureclass}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def nearest_neighbor_3d(self, params):
        """
        Nearest Neighbor 3D
        Creates a voxel layer source file (netCDF) from categorical 3D points by assigning each voxel the categories of the nearest neighbor in 3D.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            category_field = params.get("category_field")
            if category_field is None: return {"success": False, "error": "category_field is required"}
            out_netcdf_file = params.get("out_netcdf_file")
            if out_netcdf_file is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_netcdf_file = arcpy.CreateUniqueName("NearestNeighbor3D_Output", aprx.scratchFolder, "nc")

            x_spacing = params.get("x_spacing")
            y_spacing = params.get("y_spacing")
            elevation_spacing = params.get("elevation_spacing")
            elev_inflation_factor = params.get("elev_inflation_factor")
            in_study_area = params.get("in_study_area")
            min_elev_raster = params.get("min_elev_raster")
            max_elev_raster = params.get("max_elev_raster")

            arcpy.ga.NearestNeighbor3D(in_features, category_field, out_netcdf_file, x_spacing, y_spacing, elevation_spacing, elev_inflation_factor, in_study_area, min_elev_raster, max_elev_raster)

            output_name = os.path.basename(out_netcdf_file)
            # Voxel layers are added to scenes
            return {"success": True, "output_file": output_name, "output_path": out_netcdf_file}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def radial_basis_functions(self, params):
        """
        Radial Basis Functions
        Uses one of five basis functions to interpolate a surfaces that passes through the input points exactly.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            z_field = params.get("z_field")
            if z_field is None: return {"success": False, "error": "z_field is required"}
            out_ga_layer = params.get("out_ga_layer")
            out_raster = params.get("out_raster")

            if not out_ga_layer and not out_raster:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_raster = arcpy.CreateUniqueName("RadialBasis_Output", aprx.defaultGeodatabase)

            cell_size = params.get("cell_size")
            search_neighborhood = params.get("search_neighborhood")
            radial_basis_functions = params.get("radial_basis_functions", "THIN_PLATE_SPLINE")
            small_scale_parameter = params.get("small_scale_parameter")

            arcpy.ga.RadialBasisFunctions(in_features, z_field, out_ga_layer, out_raster, cell_size, search_neighborhood, radial_basis_functions, small_scale_parameter)

            output_path = out_raster if out_raster else out_ga_layer
            if output_path:
                output_name = os.path.basename(output_path)
                self._add_to_map(output_path)
                return {"success": True, "output_layer": output_name, "output_path": output_path}
            return {"success": True, "message": "Radial Basis Functions completed successfully."}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def create_spatially_balanced_points(self, params):
        """
        Create Spatially Balanced Points
        Creates a set of sample points based on inclusion probabilities, resulting in a spatially balanced sample design.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_probability_raster = params.get("in_probability_raster")
            if in_probability_raster is None: return {"success": False, "error": "in_probability_raster is required"}
            number_output_points = params.get("number_output_points")
            if number_output_points is None: return {"success": False, "error": "number_output_points is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("SpatiallyBalancedPoints", aprx.defaultGeodatabase)

            arcpy.ga.CreateSpatiallyBalancedPoints(in_probability_raster, number_output_points, out_feature_class)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def densify_sampling_network(self, params):
        """
        Densify Sampling Network
        Uses a predefined geostatistical kriging layer to determine where new monitoring stations should be built.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_geostat_layer = params.get("in_geostat_layer")
            if in_geostat_layer is None: return {"success": False, "error": "in_geostat_layer is required"}
            number_output_points = params.get("number_output_points")
            if number_output_points is None: return {"success": False, "error": "number_output_points is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("DensifyNetwork_Output", aprx.defaultGeodatabase)

            selection_criteria = params.get("selection_criteria", "LARGEST_STANDARD_ERROR_OF_PREDICTION")
            threshold = params.get("threshold")
            in_weight_raster = params.get("in_weight_raster")
            in_candidate_point_features = params.get("in_candidate_point_features")
            inhibition_distance = params.get("inhibition_distance")

            arcpy.ga.DensifySamplingNetwork(in_geostat_layer, number_output_points, out_feature_class, selection_criteria, threshold, in_weight_raster, in_candidate_point_features, inhibition_distance)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def extract_values_to_table(self, params):
        """
        Extract Values To Table
        Extracts cell values from a set of rasters to a table, based on a point or polygon feature class.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            in_rasters = params.get("in_rasters")
            if in_rasters is None: return {"success": False, "error": "in_rasters is required"}
            out_table = params.get("out_table")
            if out_table is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_table = arcpy.CreateUniqueName("ExtractValues_Output", aprx.defaultGeodatabase)

            out_raster_names_table = params.get("out_raster_names_table")
            add_warning_field = params.get("add_warning_field", "ADD_WARNING_FIELD")

            arcpy.ga.ExtractValuesToTable(in_features, in_rasters, out_table, out_raster_names_table, add_warning_field)

            output_name = os.path.basename(out_table)
            # Tables are not added to map
            return {"success": True, "output_table": output_name, "output_path": out_table}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def gaussian_geostatistical_simulations(self, params):
        """
        Gaussian Geostatistical Simulations
        Performs a conditional or unconditional geostatistical simulation based on a Simple Kriging model.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_geostat_layer = params.get("in_geostat_layer")
            if in_geostat_layer is None: return {"success": False, "error": "in_geostat_layer is required"}
            number_of_realizations = params.get("number_of_realizations")
            if number_of_realizations is None: return {"success": False, "error": "number_of_realizations is required"}
            output_workspace = params.get("output_workspace")
            if output_workspace is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                output_workspace = aprx.defaultGeodatabase

            output_simulation_prefix = params.get("output_simulation_prefix")
            if output_simulation_prefix is None:
                output_simulation_prefix = "GCSim"

            in_conditioning_features = params.get("in_conditioning_features")
            conditioning_field = params.get("conditioning_field")
            cell_size = params.get("cell_size")
            in_bounding_dataset = params.get("in_bounding_dataset")
            save_simulated_rasters = params.get("save_simulated_rasters", "SAVE_RASTERS")
            quantile = params.get("quantile")
            threshold = params.get("threshold")
            in_stats_polygons = params.get("in_stats_polygons")
            raster_stat_type = params.get("raster_stat_type")
            conditioning_measurement_error_field = params.get("conditioning_measurement_error_field")

            arcpy.ga.GaussianGeostatisticalSimulations(in_geostat_layer, number_of_realizations, output_workspace, output_simulation_prefix, in_conditioning_features, conditioning_field, cell_size, in_bounding_dataset, save_simulated_rasters, quantile, threshold, in_stats_polygons, raster_stat_type, conditioning_measurement_error_field)

            return {"success": True, "message": f"Gaussian Geostatistical Simulations completed in {output_workspace}."}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def compare_geostatistical_layers(self, params):
        """
        Compare Geostatistical Layers
        Compares and ranks geostatistical layers using customizable criteria based on cross validation statistics.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_geostat_layers = params.get("in_geostat_layers")
            if in_geostat_layers is None: return {"success": False, "error": "in_geostat_layers is required"}
            out_cv_table = params.get("out_cv_table")
            if out_cv_table is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_cv_table = arcpy.CreateUniqueName("CompareLayers_Output", aprx.defaultGeodatabase)

            out_geostat_layer = params.get("out_geostat_layer")
            comparison_method = params.get("comparison_method", "SINGLE")
            criterion = params.get("criterion", "ROOT_MEAN_SQUARE")
            criteria_hierarchy = params.get("criteria_hierarchy")
            weighted_criteria = params.get("weighted_criteria")
            exclusion_criteria = params.get("exclusion_criteria")

            arcpy.ga.CompareGeostatisticalLayers(in_geostat_layers, out_cv_table, out_geostat_layer, comparison_method, criterion, criteria_hierarchy, weighted_criteria, exclusion_criteria)

            output_name = os.path.basename(out_cv_table)
            return {"success": True, "output_table": output_name, "output_path": out_cv_table}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def cross_validation(self, params):
        """
        Cross Validation
        Removes one data location and predicts the associated data using the data at the rest of the locations.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_geostat_layer = params.get("in_geostat_layer")
            if in_geostat_layer is None: return {"success": False, "error": "in_geostat_layer is required"}
            out_point_feature_class = params.get("out_point_feature_class")
            if out_point_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_point_feature_class = arcpy.CreateUniqueName("CrossValidation_Output", aprx.defaultGeodatabase)

            arcpy.ga.CrossValidation(in_geostat_layer, out_point_feature_class)

            output_name = os.path.basename(out_point_feature_class)
            self._add_to_map(out_point_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_point_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def directional_trend(self, params):
        """
        Directional Trend
        Creates a scatter plot chart on a feature layer displaying the trend of data values in a particular direction.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            analysis_field = params.get("analysis_field")
            if analysis_field is None: return {"success": False, "error": "analysis_field is required"}
            direction = params.get("direction", 0)
            determine_direction = params.get("determine_direction", "DETERMINE_DIRECTION")
            order = params.get("order", 1)

            result = arcpy.ga.DirectionalTrend(in_features, analysis_field, direction, determine_direction, order)

            # This tool returns a Chart object, not a layer.
            # We will return the chart object in the result.
            return {"success": True, "output_chart": result}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def exploratory_interpolation(self, params):
        """
        Exploratory Interpolation
        Generates various interpolation results from input point features and a field.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            value_field = params.get("value_field")
            if value_field is None: return {"success": False, "error": "value_field is required"}
            out_cv_table = params.get("out_cv_table")
            if out_cv_table is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_cv_table = arcpy.CreateUniqueName("ExploratoryInterp_Output", aprx.defaultGeodatabase)

            out_geostat_layer = params.get("out_geostat_layer")
            interp_methods = params.get("interp_methods", ["IDW", "LPI", "RBF"])
            comparison_method = params.get("comparison_method", "SINGLE")
            criterion = params.get("criterion", "ROOT_MEAN_SQUARE")
            criteria_hierarchy = params.get("criteria_hierarchy")
            weighted_criteria = params.get("weighted_criteria")
            exclusion_criteria = params.get("exclusion_criteria")

            arcpy.ga.ExploratoryInterpolation(in_features, value_field, out_cv_table, out_geostat_layer, interp_methods, comparison_method, criterion, criteria_hierarchy, weighted_criteria, exclusion_criteria)

            output_name = os.path.basename(out_cv_table)
            return {"success": True, "output_table": output_name, "output_path": out_cv_table}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def generate_subset_polygons(self, params):
        """
        Generate Subset Polygons
        Generates nonoverlapping subset polygon features from a set of input points.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_point_features = params.get("in_point_features")
            if in_point_features is None: return {"success": False, "error": "in_point_features is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("SubsetPolygons_Output", aprx.defaultGeodatabase)

            min_points_per_subset = params.get("min_points_per_subset", 20)
            max_points_per_subset = params.get("max_points_per_subset")
            coincident_points = params.get("coincident_points", "MEAN_CENTER")

            arcpy.ga.GenerateSubsetPolygons(in_point_features, out_feature_class, min_points_per_subset, max_points_per_subset, coincident_points)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def neighborhood_selection(self, params):
        """
        Neighborhood Selection
        Creates a layer of points based on a user-defined neighborhood.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_dataset = params.get("in_dataset")
            if in_dataset is None: return {"success": False, "error": "in_dataset is required"}
            out_layer = params.get("out_layer")
            if out_layer is None:
                out_layer = "NeighborhoodSelection"
            point_coord = params.get("point_coord")
            if point_coord is None: return {"success": False, "error": "point_coord is required"}
            neighbors_max = params.get("neighbors_max")
            if neighbors_max is None: return {"success": False, "error": "neighbors_max is required"}
            neighbors_min = params.get("neighbors_min")
            if neighbors_min is None: return {"success": False, "error": "neighbors_min is required"}
            minor_semiaxis = params.get("minor_semiaxis")
            if minor_semiaxis is None: return {"success": False, "error": "minor_semiaxis is required"}
            major_semiaxis = params.get("major_semiaxis")
            if major_semiaxis is None: return {"success": False, "error": "major_semiaxis is required"}
            angle = params.get("angle")
            if angle is None: return {"success": False, "error": "angle is required"}
            shape_type = params.get("shape_type", "SECTORS")

            arcpy.ga.NeighborhoodSelection(in_dataset, out_layer, point_coord, neighbors_max, neighbors_min, minor_semiaxis, major_semiaxis, angle, shape_type)

            self._add_to_map(out_layer)
            return {"success": True, "output_layer": out_layer}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def semivariogram_sensitivity(self, params):
        """
        Semivariogram Sensitivity
        Performs a sensitivity analysis on the predicted values and associated standard errors.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_ga_model_source = params.get("in_ga_model_source")
            if in_ga_model_source is None: return {"success": False, "error": "in_ga_model_source is required"}
            in_datasets = params.get("in_datasets")
            if in_datasets is None: return {"success": False, "error": "in_datasets is required"}
            in_locations = params.get("in_locations")
            if in_locations is None: return {"success": False, "error": "in_locations is required"}
            out_table = params.get("out_table")
            if out_table is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_table = arcpy.CreateUniqueName("SemivariogramSensitivity_Output", aprx.defaultGeodatabase)

            nugget_span_percents = params.get("nugget_span_percents")
            nugget_calc_times = params.get("nugget_calc_times")
            partialsill_span_percents = params.get("partialsill_span_percents")
            partialsill_calc_times = params.get("partialsill_calc_times")
            range_span_percents = params.get("range_span_percents")
            range_calc_times = params.get("range_calc_times")
            minrange_span_percents = params.get("minrange_span_percents")
            minrange_calc_times = params.get("minrange_calc_times")

            arcpy.ga.SemivariogramSensitivity(in_ga_model_source, in_datasets, in_locations, out_table, nugget_span_percents, nugget_calc_times, partialsill_span_percents, partialsill_calc_times, range_span_percents, range_calc_times, minrange_span_percents, minrange_calc_times)

            output_name = os.path.basename(out_table)
            return {"success": True, "output_table": output_name, "output_path": out_table}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def subset_features(self, params):
        """
        Subset Features
        Divides the records of a feature class or table into two subsets for training and testing.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_features = params.get("in_features")
            if in_features is None: return {"success": False, "error": "in_features is required"}
            out_training_feature_class = params.get("out_training_feature_class")
            if out_training_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_training_feature_class = arcpy.CreateUniqueName("TrainingData", aprx.defaultGeodatabase)

            out_test_feature_class = params.get("out_test_feature_class")
            if out_test_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_test_feature_class = arcpy.CreateUniqueName("TestData", aprx.defaultGeodatabase)

            size_of_training_dataset = params.get("size_of_training_dataset", 50)
            subset_size_units = params.get("subset_size_units", "PERCENTAGE_OF_FEATURES")

            arcpy.ga.SubsetFeatures(in_features, out_training_feature_class, out_test_feature_class, size_of_training_dataset, subset_size_units)

            self._add_to_map(out_training_feature_class)
            self._add_to_map(out_test_feature_class)
            return {"success": True, "training_data": out_training_feature_class, "test_data": out_test_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def areal_interpolation_layer_to_polygons(self, params):
        """
        Areal Interpolation Layer To Polygons
        Reaggregates the predictions of an Areal Interpolation layer to a new set of polygons.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_areal_interpolation_layer = params.get("in_areal_interpolation_layer")
            if in_areal_interpolation_layer is None: return {"success": False, "error": "in_areal_interpolation_layer is required"}
            in_polygon_features = params.get("in_polygon_features")
            if in_polygon_features is None: return {"success": False, "error": "in_polygon_features is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("ArealInterp_Output", aprx.defaultGeodatabase)

            append_all_fields = params.get("append_all_fields", "ALL")

            arcpy.ga.ArealInterpolationLayerToPolygons(in_areal_interpolation_layer, in_polygon_features, out_feature_class, append_all_fields)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def calculate_z_value(self, params):
        """
        Calculate Z Value
        Uses the interpolation model in a geostatistical layer to predict a value at a single location.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_geostat_layer = params.get("in_geostat_layer")
            if in_geostat_layer is None: return {"success": False, "error": "in_geostat_layer is required"}
            point_coord = params.get("point_coord")
            if point_coord is None: return {"success": False, "error": "point_coord is required"}

            result = arcpy.ga.CalculateZValue(in_geostat_layer, point_coord)

            # This tool returns a numeric value.
            return {"success": True, "z_value": float(result.getOutput(0))}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def create_geostatistical_layer(self, params):
        """
        Create Geostatistical Layer
        Creates a new geostatistical layer from an existing geostatistical model source.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_ga_model_source = params.get("in_ga_model_source")
            if in_ga_model_source is None: return {"success": False, "error": "in_ga_model_source is required"}
            in_datasets = params.get("in_datasets")
            if in_datasets is None: return {"success": False, "error": "in_datasets is required"}
            out_layer = params.get("out_layer")
            if out_layer is None:
                out_layer = "NewGeostatLayer"

            arcpy.ga.CreateGeostatisticalLayer(in_ga_model_source, in_datasets, out_layer)

            self._add_to_map(out_layer)
            return {"success": True, "output_layer": out_layer}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def ga_layer_3d_to_multidimensional_raster(self, params):
        """
        GA Layer 3D To Multidimensional Raster
        Exports a 3D geostatistical layer to a multidimensional raster dataset.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_3d_geostat_layer = params.get("in_3d_geostat_layer")
            if in_3d_geostat_layer is None: return {"success": False, "error": "in_3d_geostat_layer is required"}
            out_multidimensional_raster = params.get("out_multidimensional_raster")
            if out_multidimensional_raster is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_multidimensional_raster = arcpy.CreateUniqueName("GALayer3DToMD", aprx.defaultGeodatabase)

            cell_size = params.get("cell_size")
            explicit_only = params.get("explicit_only", "EXPLICIT_ONLY")
            min_elev = params.get("min_elev")
            max_elev = params.get("max_elev")
            elev_interval = params.get("elev_interval")
            elev_values = params.get("elev_values")
            elev_units = params.get("elev_units")
            output_type = params.get("output_type", "PREDICTION")
            quantile_probability_value = params.get("quantile_probability_value")
            additional_outputs = params.get("additional_outputs")
            build_transpose = params.get("build_transpose", "NO_TRANSPOSE")

            arcpy.ga.GALayer3DToMultidimensionalRaster(in_3d_geostat_layer, out_multidimensional_raster, cell_size, explicit_only, min_elev, max_elev, elev_interval, elev_values, elev_units, output_type, quantile_probability_value, additional_outputs, build_transpose)

            output_name = os.path.basename(out_multidimensional_raster)
            self._add_to_map(out_multidimensional_raster)
            return {"success": True, "output_raster": output_name, "output_path": out_multidimensional_raster}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def ga_layer_3d_to_netcdf(self, params):
        """
        GA Layer 3D To NetCDF
        Exports one or more 3D geostatistical layers to netCDF format.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_3d_geostat_layers = params.get("in_3d_geostat_layers")
            if in_3d_geostat_layers is None: return {"success": False, "error": "in_3d_geostat_layers is required"}
            out_netcdf_file = params.get("out_netcdf_file")
            if out_netcdf_file is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_netcdf_file = arcpy.CreateUniqueName("GALayer3DToNetCDF", aprx.scratchFolder, "nc")

            export_locations = params.get("export_locations", "REGULAR_GRID")
            x_spacing = params.get("x_spacing")
            y_spacing = params.get("y_spacing")
            elevation_spacing = params.get("elevation_spacing")
            in_points_3d = params.get("in_points_3d")
            output_variables = params.get("output_variables")
            in_study_area = params.get("in_study_area")
            min_elev_raster = params.get("min_elev_raster")
            max_elev_raster = params.get("max_elev_raster")

            arcpy.ga.GALayer3DToNetCDF(in_3d_geostat_layers, out_netcdf_file, export_locations, x_spacing, y_spacing, elevation_spacing, in_points_3d, output_variables, in_study_area, min_elev_raster, max_elev_raster)

            output_name = os.path.basename(out_netcdf_file)
            return {"success": True, "output_file": output_name, "output_path": out_netcdf_file}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def ga_layer_to_contour(self, params):
        """
        GA Layer To Contour
        Creates a feature class of contours from a geostatistical layer.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_geostat_layer = params.get("in_geostat_layer")
            if in_geostat_layer is None: return {"success": False, "error": "in_geostat_layer is required"}
            contour_type = params.get("contour_type")
            if contour_type is None: return {"success": False, "error": "contour_type is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("Contour_Output", aprx.defaultGeodatabase)

            contour_quality = params.get("contour_quality", "DRAFT")
            classification_type = params.get("classification_type", "MANUAL")
            classes_count = params.get("classes_count", 10)
            classes_breaks = params.get("classes_breaks")
            out_elevation = params.get("out_elevation")

            arcpy.ga.GALayerToContour(in_geostat_layer, out_feature_class, contour_type, contour_quality, classification_type, classes_count, classes_breaks, out_elevation)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def ga_layer_to_grid(self, params):
        """
        GA Layer To Grid
        Exports a Geostatistical layer to a raster.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_geostat_layer = params.get("in_geostat_layer")
            if in_geostat_layer is None: return {"success": False, "error": "in_geostat_layer is required"}
            out_surface_grid = params.get("out_surface_grid")
            if out_surface_grid is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_surface_grid = arcpy.CreateUniqueName("Grid_Output", aprx.defaultGeodatabase)

            cell_size = params.get("cell_size")
            points_per_block_horz = params.get("points_per_block_horz", 1)
            points_per_block_vert = params.get("points_per_block_vert", 1)

            arcpy.ga.GALayerToGrid(in_geostat_layer, out_surface_grid, cell_size, points_per_block_horz, points_per_block_vert)

            output_name = os.path.basename(out_surface_grid)
            self._add_to_map(out_surface_grid)
            return {"success": True, "output_raster": output_name, "output_path": out_surface_grid}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def ga_layer_to_points(self, params):
        """
        GA Layer To Points
        Exports a geostatistical layer to points.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_geostat_layer = params.get("in_geostat_layer")
            if in_geostat_layer is None: return {"success": False, "error": "in_geostat_layer is required"}
            in_locations = params.get("in_locations")
            if in_locations is None: return {"success": False, "error": "in_locations is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("Points_Output", aprx.defaultGeodatabase)

            z_field = params.get("z_field")
            append_all_fields = params.get("append_all_fields", "ALL")
            elevation_field = params.get("elevation_field")
            elevation_units = params.get("elevation_units")

            arcpy.ga.GALayerToPoints(in_geostat_layer, in_locations, out_feature_class, z_field, append_all_fields, elevation_field, elevation_units)

            output_name = os.path.basename(out_feature_class)
            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": output_name, "output_path": out_feature_class}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def ga_layer_to_rasters(self, params):
        """
        GA Layer To Rasters
        Exports a geostatistical layer to one or multiple rasters.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_geostat_layer = params.get("in_geostat_layer")
            if in_geostat_layer is None: return {"success": False, "error": "in_geostat_layer is required"}
            out_raster = params.get("out_raster")
            if out_raster is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_raster = arcpy.CreateUniqueName("Raster_Output", aprx.defaultGeodatabase)

            output_type = params.get("output_type", "PREDICTION")
            quantile_probability_value = params.get("quantile_probability_value")
            cell_size = params.get("cell_size")
            points_per_block_horz = params.get("points_per_block_horz", 1)
            points_per_block_vert = params.get("points_per_block_vert", 1)
            additional_rasters = params.get("additional_rasters")
            out_elevation = params.get("out_elevation")

            arcpy.ga.GALayerToRasters(in_geostat_layer, out_raster, output_type, quantile_probability_value, cell_size, points_per_block_horz, points_per_block_vert, additional_rasters, out_elevation)

            output_name = os.path.basename(out_raster)
            self._add_to_map(out_raster)
            return {"success": True, "output_raster": output_name, "output_path": out_raster}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def get_model_parameter(self, params):
        """
        Get Model Parameter
        Gets model parameter value from an existing geostatistical model source.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_ga_model_source = params.get("in_ga_model_source")
            if in_ga_model_source is None: return {"success": False, "error": "in_ga_model_source is required"}
            model_param_xpath = params.get("model_param_xpath")
            if model_param_xpath is None: return {"success": False, "error": "model_param_xpath is required"}

            result = arcpy.ga.GetModelParameter(in_ga_model_source, model_param_xpath)

            # This tool returns a string value.
            return {"success": True, "parameter_value": result.getOutput(0)}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")

    def set_model_parameter(self, params):
        """
        Set Model Parameter
        Sets parameter values in an existing geostatistical model source.
        """
        try:
            arcpy.CheckOutExtension("GeoStats")
            in_ga_model_source = params.get("in_ga_model_source")
            if in_ga_model_source is None: return {"success": False, "error": "in_ga_model_source is required"}
            model_param_xpath = params.get("model_param_xpath")
            if model_param_xpath is None: return {"success": False, "error": "model_param_xpath is required"}
            in_param_value = params.get("in_param_value")
            if in_param_value is None: return {"success": False, "error": "in_param_value is required"}
            out_ga_model = params.get("out_ga_model")
            if out_ga_model is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_ga_model = arcpy.CreateUniqueName("UpdatedModel", aprx.scratchFolder, "xml")

            arcpy.ga.SetModelParameter(in_ga_model_source, model_param_xpath, in_param_value, out_ga_model)

            return {"success": True, "output_model": out_ga_model}
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            arcpy.CheckInExtension("GeoStats")