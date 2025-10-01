# Generated ArcGIS Pro spatial-analyst Progent Functions
# Generated on 2025-10-01T14:46:02.619661
# Total tools: 208

import arcpy
import os

class SpatialAnalystTools:
    """Generated spatial analysis functions in progent.pyt format"""

    def __init__(self):
        try:
            if arcpy.CheckExtension("Spatial") == "Available":
                arcpy.CheckOutExtension("Spatial")
            else:
                raise arcpy.ExecuteError("Spatial Analyst license is not available.")
        except Exception as e:
            print(f"Error checking out Spatial Analyst license: {e}")

    def _add_to_map(self, path):
        try:
            aprx = arcpy.mp.ArcGISProject('CURRENT')
            map_obj = aprx.activeMap
            if map_obj:
                map_obj.addDataFromPath(path)
        except Exception as e:
            print(f'Could not add {path} to map: {e}')

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
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                output_name = arcpy.CreateUniqueName("RasterCalculator_Output", aprx.defaultGeodatabase)
                output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            else:
                output_path = output_raster
                output_name = os.path.basename(output_path)

            # Execute Raster Calculator
            result = arcpy.sa.RasterCalculator(expression)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def con(self, params):
        """Con

Performs a conditional if/else evaluation on each of the input cells of an input raster. Learn more about performing conditional evaluation with Con

        params: {"in_conditional_raster": <Raster Layer>, "in_true_raster_or_constant": <Raster Layer; Constant>, "in_false_raster_or_constant": <Raster Layer; Constant>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_conditional_raster = params.get("in_conditional_raster")
            if in_conditional_raster is None:
                return {"success": False, "error": "in_conditional_raster parameter is required"}
            in_true_raster_or_constant = params.get("in_true_raster_or_constant")
            if in_true_raster_or_constant is None:
                return {"success": False, "error": "in_true_raster_or_constant parameter is required"}
            in_false_raster_or_constant = params.get("in_false_raster_or_constant")
            where_clause = params.get("where_clause")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_conditional_raster)).replace(' ', '_')}_Con"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Con
            result = arcpy.sa.Con(in_conditional_raster, in_true_raster_or_constant, in_false_raster_or_constant, where_clause)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def pick(self, params):
        """Pick

The value from a position raster is used to determine from which raster in a list of input rasters the output cell value will be obtained.

        params: {"in_position_raster": <Raster Layer>, "in_rasters_or_constants": <Raster Layer; Constant>, "process_as_multiband": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_position_raster = params.get("in_position_raster")
            if in_position_raster is None:
                return {"success": False, "error": "in_position_raster parameter is required"}
            in_rasters_or_constants = params.get("in_rasters_or_constants")
            if in_rasters_or_constants is None:
                return {"success": False, "error": "in_rasters_or_constants parameter is required"}
            process_as_multiband = params.get("process_as_multiband")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_position_raster)).replace(' ', '_')}_Pick"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Pick
            result = arcpy.sa.Pick(in_position_raster, in_rasters_or_constants, process_as_multiband)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_null(self, params):
        """Set Null

Set Null sets identified cell locations to NoData based on a specified criteria. It returns NoData if a conditional evaluation is true, and returns the value specified by another raster if it is false. Learn more about setting cell values to NoData with Set Null

        params: {"in_conditional_raster": <Raster Layer>, "in_false_raster_or_constant": <Raster Layer; Constant>, "where_clause": <SQL Expression>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_conditional_raster = params.get("in_conditional_raster")
            if in_conditional_raster is None:
                return {"success": False, "error": "in_conditional_raster parameter is required"}
            in_false_raster_or_constant = params.get("in_false_raster_or_constant")
            if in_false_raster_or_constant is None:
                return {"success": False, "error": "in_false_raster_or_constant parameter is required"}
            where_clause = params.get("where_clause")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_conditional_raster)).replace(' ', '_')}_Set_Null"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Set Null
            result = arcpy.sa.SetNull(in_conditional_raster, in_false_raster_or_constant, where_clause)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_kernel_density_ratio(self, params):
        """Calculate Kernel Density Ratio

Calculates a spatial relative risk surface using two input feature datasets. The numerator in the ratio represents cases, such as number of crimes or number of patients, and the denominator represents the control, such as the total population.

        params: {"in_features_numerator": <Feature Layer>, "in_features_denominator": <Feature Layer>, "population_field_numerator": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features_numerator = params.get("in_features_numerator")
            if in_features_numerator is None:
                return {"success": False, "error": "in_features_numerator parameter is required"}
            in_features_denominator = params.get("in_features_denominator")
            if in_features_denominator is None:
                return {"success": False, "error": "in_features_denominator parameter is required"}
            population_field_numerator = params.get("population_field_numerator")
            if population_field_numerator is None:
                return {"success": False, "error": "population_field_numerator parameter is required"}
            population_field_denominator = params.get("population_field_denominator")
            if population_field_denominator is None:
                return {"success": False, "error": "population_field_denominator parameter is required"}
            cell_size = params.get("cell_size")
            search_radius_numerator = params.get("search_radius_numerator")
            search_radius_denominator = params.get("search_radius_denominator")
            out_cell_values = params.get("out_cell_values")
            method = params.get("method")
            in_barriers_numerator = params.get("in_barriers_numerator")
            in_barriers_denominator = params.get("in_barriers_denominator")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_features_numerator)).replace(' ', '_')}_Calculate_Kernel_Density_Ratio"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Kernel Density Ratio
            result = arcpy.sa.CalculateKernelDensityRatio(in_features_numerator, in_features_denominator, population_field_numerator, population_field_denominator, cell_size, search_radius_numerator, search_radius_denominator, out_cell_values, method, in_barriers_numerator, in_barriers_denominator)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def kernel_density(self, params):
        """Kernel Density

Calculates a magnitude-per-unit area from point or polyline features using a kernel function to fit a smoothly tapered surface to each point or polyline. A barrier can be used to alter the influence of a feature while calculating kernel density. Learn more about how Kernel Density works

        params: {"in_features": <Feature Layer>, "population_field": <Field>, "cell_size": <Analysis Cell Size>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            population_field = params.get("population_field")
            if population_field is None:
                return {"success": False, "error": "population_field parameter is required"}
            cell_size = params.get("cell_size")
            search_radius = params.get("search_radius")
            area_unit_scale_factor = params.get("area_unit_scale_factor")
            out_cell_values = params.get("out_cell_values")
            method = params.get("method")
            in_barriers = params.get("in_barriers")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_features)).replace(' ', '_')}_Kernel_Density"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Kernel Density
            result = arcpy.sa.KernelDensity(in_features, population_field, cell_size, search_radius, area_unit_scale_factor, out_cell_values, method, in_barriers)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def line_density(self, params):
        """Line Density

Calculates a magnitude-per-unit area from polyline features that fall within a radius around each cell. Learn more about how Line Density works

        params: {"in_polyline_features": <Feature Layer>, "population_field": <Field>, "cell_size": <Analysis Cell Size>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_polyline_features = params.get("in_polyline_features")
            if in_polyline_features is None:
                return {"success": False, "error": "in_polyline_features parameter is required"}
            population_field = params.get("population_field")
            if population_field is None:
                return {"success": False, "error": "population_field parameter is required"}
            cell_size = params.get("cell_size")
            search_radius = params.get("search_radius")
            area_unit_scale_factor = params.get("area_unit_scale_factor")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_polyline_features)).replace(' ', '_')}_Line_Density"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Line Density
            result = arcpy.sa.LineDensity(in_polyline_features, population_field, cell_size, search_radius, area_unit_scale_factor)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def point_density(self, params):
        """Point Density

Calculates a magnitude-per-unit area from point features that fall within a neighborhood around each cell. Learn more about how Point Density works

        params: {"in_point_features": <Feature Layer>, "population_field": <Field>, "cell_size": <Analysis Cell Size>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_point_features = params.get("in_point_features")
            if in_point_features is None:
                return {"success": False, "error": "in_point_features parameter is required"}
            population_field = params.get("population_field")
            if population_field is None:
                return {"success": False, "error": "population_field parameter is required"}
            cell_size = params.get("cell_size")
            neighborhood = params.get("neighborhood")
            area_unit_scale_factor = params.get("area_unit_scale_factor")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_point_features)).replace(' ', '_')}_Point_Density"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Point Density
            result = arcpy.sa.PointDensity(in_point_features, population_field, cell_size, neighborhood, area_unit_scale_factor)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def space_time_kernel_density(self, params):
        """Space Time Kernel Density

Expands kernel density calculations from analyzing the relative position and magnitude of the input features to include other dimensions such as time and depth (elevation). The resulting output identifies the magnitude-per-unit area using the multiple kernel functions to fit a smoothly tapered surface to each input point. Learn more about how Space Time Kernel Density works

        params: {"in_features": <Feature Layer>, "population_field": <Field>, "elevation_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            population_field = params.get("population_field")
            if population_field is None:
                return {"success": False, "error": "population_field parameter is required"}
            elevation_field = params.get("elevation_field")
            elevation_field_unit = params.get("elevation_field_unit")
            time_field = params.get("time_field")
            cell_size = params.get("cell_size")
            kernel_search_radius_xy = params.get("kernel_search_radius_xy")
            kernel_search_radius_z = params.get("kernel_search_radius_z")
            kernel_search_time_window = params.get("kernel_search_time_window")
            resultant_values = params.get("resultant_values")
            method = params.get("method")
            min_elevation = params.get("min_elevation")
            max_elevation = params.get("max_elevation")
            elevation_interval = params.get("elevation_interval")
            elevation_unit = params.get("elevation_unit")
            start_time = params.get("start_time")
            end_time = params.get("end_time")
            time_interval = params.get("time_interval")
            time_interval_unit = params.get("time_interval_unit")
            out_voxel_layer = params.get("out_voxel_layer")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_features)).replace(' ', '_')}_Space_Time_Kernel_Density"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Space Time Kernel Density
            result = arcpy.sa.SpaceTimeKernelDensity(in_features, population_field, elevation_field, elevation_field_unit, time_field, cell_size, kernel_search_radius_xy, kernel_search_radius_z, kernel_search_time_window, resultant_values, method, min_elevation, max_elevation, elevation_interval, elevation_unit, start_time, end_time, time_interval, time_interval_unit, out_voxel_layer)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def distance_accumulation(self, params):
        """Distance Accumulation

Calculates accumulated distance for each cell to sources, allowing for straight-line distance, cost distance, and true surface distance, as well as vertical and horizontal cost factors. Learn more about how the distance accumulation tools work

        params: {"in_source_data": <Raster Layer; Feature Layer>, "in_barrier_data": <Raster Layer; Feature Layer>, "in_surface_raster": <Raster Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_source_data = params.get("in_source_data")
            if in_source_data is None:
                return {"success": False, "error": "in_source_data parameter is required"}
            in_barrier_data = params.get("in_barrier_data")
            in_surface_raster = params.get("in_surface_raster")
            in_cost_raster = params.get("in_cost_raster")
            in_vertical_raster = params.get("in_vertical_raster")
            vertical_factor = params.get("vertical_factor")
            in_horizontal_raster = params.get("in_horizontal_raster")
            horizontal_factor = params.get("horizontal_factor")
            out_back_direction_raster = params.get("out_back_direction_raster")
            out_source_direction_raster = params.get("out_source_direction_raster")
            out_source_location_raster = params.get("out_source_location_raster")
            source_initial_accumulation = params.get("source_initial_accumulation")
            source_maximum_accumulation = params.get("source_maximum_accumulation")
            source_cost_multiplier = params.get("source_cost_multiplier")
            source_direction = params.get("source_direction")
            distance_method = params.get("distance_method")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_source_data)).replace(' ', '_')}_Distance_Accumulation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Distance Accumulation
            result = arcpy.sa.DistanceAccumulation(in_source_data, in_barrier_data, in_surface_raster, in_cost_raster, in_vertical_raster, vertical_factor, in_horizontal_raster, horizontal_factor, out_back_direction_raster, out_source_direction_raster, out_source_location_raster, source_initial_accumulation, source_maximum_accumulation, source_cost_multiplier, source_direction, distance_method)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def distance_allocation(self, params):
        """Distance Allocation

Calculates distance allocation for each cell to the provided sources based on straight-line distance, cost distance, and true surface distance, as well as vertical and horizontal cost factors. Learn more about how the distance accumulation tools work

        params: {"in_source_data": <Raster Layer; Feature Layer>, "in_barrier_data": <Raster Layer; Feature Layer>, "in_surface_raster": <Raster Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_source_data = params.get("in_source_data")
            if in_source_data is None:
                return {"success": False, "error": "in_source_data parameter is required"}
            in_barrier_data = params.get("in_barrier_data")
            in_surface_raster = params.get("in_surface_raster")
            in_cost_raster = params.get("in_cost_raster")
            in_vertical_raster = params.get("in_vertical_raster")
            vertical_factor = params.get("vertical_factor")
            in_horizontal_raster = params.get("in_horizontal_raster")
            horizontal_factor = params.get("horizontal_factor")
            out_distance_accumulation_raster = params.get("out_distance_accumulation_raster")
            out_back_direction_raster = params.get("out_back_direction_raster")
            out_source_direction_raster = params.get("out_source_direction_raster")
            out_source_location_raster = params.get("out_source_location_raster")
            source_field = params.get("source_field")
            source_initial_accumulation = params.get("source_initial_accumulation")
            source_maximum_accumulation = params.get("source_maximum_accumulation")
            source_cost_multiplier = params.get("source_cost_multiplier")
            source_direction = params.get("source_direction")
            distance_method = params.get("distance_method")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_source_data)).replace(' ', '_')}_Distance_Allocation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Distance Allocation
            result = arcpy.sa.DistanceAllocation(in_source_data, in_barrier_data, in_surface_raster, in_cost_raster, in_vertical_raster, vertical_factor, in_horizontal_raster, horizontal_factor, out_distance_accumulation_raster, out_back_direction_raster, out_source_direction_raster, out_source_location_raster, source_field, source_initial_accumulation, source_maximum_accumulation, source_cost_multiplier, source_direction, distance_method)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def least_cost_corridor(self, params):
        """Least Cost Corridor

Calculates the sum of two accumulative cost distance rasters with the option to apply a threshold based on percentage or accumulative cost. Learn more about how to connect locations with corridors

        params: {"in_accumulative_cost_distance_raster1": <Raster Layer>, "in_back_direction_raster1": <Raster Layer>, "in_accumulative_cost_distance_raster2": <Raster Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_accumulative_cost_distance_raster1 = params.get("in_accumulative_cost_distance_raster1")
            if in_accumulative_cost_distance_raster1 is None:
                return {"success": False, "error": "in_accumulative_cost_distance_raster1 parameter is required"}
            in_back_direction_raster1 = params.get("in_back_direction_raster1")
            if in_back_direction_raster1 is None:
                return {"success": False, "error": "in_back_direction_raster1 parameter is required"}
            in_accumulative_cost_distance_raster2 = params.get("in_accumulative_cost_distance_raster2")
            if in_accumulative_cost_distance_raster2 is None:
                return {"success": False, "error": "in_accumulative_cost_distance_raster2 parameter is required"}
            in_back_direction_raster2 = params.get("in_back_direction_raster2")
            if in_back_direction_raster2 is None:
                return {"success": False, "error": "in_back_direction_raster2 parameter is required"}
            threshold_method = params.get("threshold_method")
            if threshold_method is None:
                return {"success": False, "error": "threshold_method parameter is required"}
            threshold = params.get("threshold")
            if threshold is None:
                return {"success": False, "error": "threshold parameter is required"}

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_accumulative_cost_distance_raster1)).replace(' ', '_')}_Least_Cost_Corridor"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Least Cost Corridor
            result = arcpy.sa.LeastCostCorridor(in_accumulative_cost_distance_raster1, in_back_direction_raster1, in_accumulative_cost_distance_raster2, in_back_direction_raster2, threshold_method, threshold)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def optimal_corridor_connections(self, params):
        """Optimal Corridor Connections

Calculates the optimal corridor connections between two or more input regions. Learn more about how to connect locations with corridors

        params: {"in_regions": <Raster Layer; Feature Layer>, "out_optimal_polygons": <Feature Class>, "in_barriers": <Raster Layer; Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_regions = params.get("in_regions")
            if in_regions is None:
                return {"success": False, "error": "in_regions parameter is required"}
            out_optimal_polygons = params.get("out_optimal_polygons")
            if out_optimal_polygons is None:
                return {"success": False, "error": "out_optimal_polygons parameter is required"}
            in_barriers = params.get("in_barriers")
            in_cost_raster = params.get("in_cost_raster")
            out_optimal_lines = params.get("out_optimal_lines")
            out_neighbor_polygons = params.get("out_neighbor_polygons")
            out_neighbor_lines = params.get("out_neighbor_lines")
            corridor_method = params.get("corridor_method")
            corridor_width = params.get("corridor_width")
            distance_method = params.get("distance_method")

            # Execute Optimal Corridor Connections
            arcpy.sa.OptimalCorridorConnections(in_regions, out_optimal_polygons, in_barriers, in_cost_raster, out_optimal_lines, out_neighbor_polygons, out_neighbor_lines, corridor_method, corridor_width, distance_method)

            self._add_to_map(out_optimal_polygons)
            return {"success": True, "output_layer": os.path.basename(out_optimal_polygons), "output_path": out_optimal_polygons}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def optimal_path_as_line(self, params):
        """Optimal Path As Line

Calculates the optimal path from a source to a destination as a line. Learn more about connecting locations with optimal paths

        params: {"in_destination_data": <Raster Layer; Feature Layer>, "in_distance_accumulation_raster": <Raster Layer>, "in_back_direction_raster": <Raster Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_destination_data = params.get("in_destination_data")
            if in_destination_data is None:
                return {"success": False, "error": "in_destination_data parameter is required"}
            in_distance_accumulation_raster = params.get("in_distance_accumulation_raster")
            if in_distance_accumulation_raster is None:
                return {"success": False, "error": "in_distance_accumulation_raster parameter is required"}
            in_back_direction_raster = params.get("in_back_direction_raster")
            if in_back_direction_raster is None:
                return {"success": False, "error": "in_back_direction_raster parameter is required"}
            out_polyline_features = params.get("out_polyline_features")
            if out_polyline_features is None:
                return {"success": False, "error": "out_polyline_features parameter is required"}
            destination_field = params.get("destination_field")
            path_type = params.get("path_type")
            create_network_paths = params.get("create_network_paths")

            # Execute Optimal Path As Line
            arcpy.sa.OptimalPathAsLine(in_destination_data, in_distance_accumulation_raster, in_back_direction_raster, out_polyline_features, destination_field, path_type, create_network_paths)

            self._add_to_map(out_polyline_features)
            return {"success": True, "output_layer": os.path.basename(out_polyline_features), "output_path": out_polyline_features}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def optimal_path_as_raster(self, params):
        """Optimal Path As Raster

Calculates the optimal path from a source to a destination as a raster. Learn more about connecting locations with optimal paths

        params: {"in_destination_data": <Raster Layer; Feature Layer>, "in_distance_accumulation_raster": <Raster Layer>, "in_back_direction_raster": <Raster Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_destination_data = params.get("in_destination_data")
            if in_destination_data is None:
                return {"success": False, "error": "in_destination_data parameter is required"}
            in_distance_accumulation_raster = params.get("in_distance_accumulation_raster")
            if in_distance_accumulation_raster is None:
                return {"success": False, "error": "in_distance_accumulation_raster parameter is required"}
            in_back_direction_raster = params.get("in_back_direction_raster")
            if in_back_direction_raster is None:
                return {"success": False, "error": "in_back_direction_raster parameter is required"}
            destination_field = params.get("destination_field")
            path_type = params.get("path_type")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_destination_data)).replace(' ', '_')}_Optimal_Path_As_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Optimal Path As Raster
            result = arcpy.sa.OptimalPathAsRaster(in_destination_data, in_distance_accumulation_raster, in_back_direction_raster, destination_field, path_type)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def optimal_region_connections(self, params):
        """Optimal Region Connections

Calculates the optimal connectivity network between two or more input regions. Learn more about connecting regions with the optimal network

        params: {"in_regions": <Raster Layer; Feature Layer>, "out_feature_class": <Feature Class>, "in_barrier_data": <Raster Layer; Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_regions = params.get("in_regions")
            if in_regions is None:
                return {"success": False, "error": "in_regions parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                return {"success": False, "error": "out_feature_class parameter is required"}
            in_barrier_data = params.get("in_barrier_data")
            in_cost_raster = params.get("in_cost_raster")
            out_neighbor_paths = params.get("out_neighbor_paths")
            distance_method = params.get("distance_method")
            connections_within_regions = params.get("connections_within_regions")

            # Execute Optimal Region Connections
            arcpy.sa.OptimalRegionConnections(in_regions, out_feature_class, in_barrier_data, in_cost_raster, out_neighbor_paths, distance_method, connections_within_regions)

            self._add_to_map(out_feature_class)
            return {"success": True, "output_layer": os.path.basename(out_feature_class), "output_path": out_feature_class}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_by_attributes(self, params):
        """Extract by Attributes

Extracts the cells of a raster based on a logical query.

        params: {"in_raster": <Raster Layer>, "where_clause": <SQL Expression>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None:
                return {"success": False, "error": "in_raster parameter is required"}
            where_clause = params.get("where_clause")
            if where_clause is None:
                return {"success": False, "error": "where_clause parameter is required"}

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_raster)).replace(' ', '_')}_Extract_by_Attributes"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract by Attributes
            result = arcpy.sa.ExtractByAttributes(in_raster, where_clause)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_by_circle(self, params):
        """Extract by Circle

Extracts the cells of a raster based on a circle by specifying the circle's center and radius.

        params: {"in_raster": <Raster Layer>, "center_point": <Point>, "radius": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None:
                return {"success": False, "error": "in_raster parameter is required"}
            center_point = params.get("center_point")
            if center_point is None:
                return {"success": False, "error": "center_point parameter is required"}
            radius = params.get("radius")
            if radius is None:
                return {"success": False, "error": "radius parameter is required"}
            extraction_area = params.get("extraction_area")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_raster)).replace(' ', '_')}_Extract_by_Circle"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract by Circle
            result = arcpy.sa.ExtractByCircle(in_raster, center_point, radius, extraction_area)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_by_mask(self, params):
        """Extract by Mask

Extracts the cells of a raster that correspond to the areas defined by a mask.

        params: {"in_raster": <Raster Layer>, "in_mask_data": <Raster Layer; Feature Layer>, "extraction_area": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None:
                return {"success": False, "error": "in_raster parameter is required"}
            in_mask_data = params.get("in_mask_data")
            if in_mask_data is None:
                return {"success": False, "error": "in_mask_data parameter is required"}
            extraction_area = params.get("extraction_area")
            analysis_extent = params.get("analysis_extent")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_raster)).replace(' ', '_')}_Extract_by_Mask"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract by Mask
            result = arcpy.sa.ExtractByMask(in_raster, in_mask_data, extraction_area, analysis_extent)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_by_points(self, params):
        """Extract by Points

Extracts the cells of a raster based on a set of coordinate points. This tool is deprecated and will be removed in a future release. The Extract by Mask tool provides enhanced functionality or performance.

        params: {"in_raster": <Raster Layer>, "points": <Point>, "extraction_area": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None:
                return {"success": False, "error": "in_raster parameter is required"}
            points = params.get("points")
            if points is None:
                return {"success": False, "error": "points parameter is required"}
            extraction_area = params.get("extraction_area")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_raster)).replace(' ', '_')}_Extract_by_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract by Points
            result = arcpy.sa.ExtractByPoints(in_raster, points, extraction_area)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_by_polygon(self, params):
        """Extract by Polygon

Extracts the cells of a raster based on a polygon by specifying the polygon's vertices. This tool is deprecated and will be removed in a future release. The Extract by Mask tool provides enhanced functionality or performance.

        params: {"in_raster": <Raster Layer>, "polygon": <Point>, "extraction_area": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None:
                return {"success": False, "error": "in_raster parameter is required"}
            polygon = params.get("polygon")
            if polygon is None:
                return {"success": False, "error": "polygon parameter is required"}
            extraction_area = params.get("extraction_area")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_raster)).replace(' ', '_')}_Extract_by_Polygon"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract by Polygon
            result = arcpy.sa.ExtractByPolygon(in_raster, polygon, extraction_area)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_by_rectangle(self, params):
        """Extract by Rectangle

Extracts the cells of a raster based on a rectangle by specifying the rectangle's extent.

        params: {"in_raster": <Raster Layer>, "extent": <Extent>, "extraction_area": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None:
                return {"success": False, "error": "in_raster parameter is required"}
            extent = params.get("extent")
            if extent is None:
                return {"success": False, "error": "extent parameter is required"}
            extraction_area = params.get("extraction_area")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_raster)).replace(' ', '_')}_Extract_by_Rectangle"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract by Rectangle
            result = arcpy.sa.ExtractByRectangle(in_raster, extent, extraction_area)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_multi_values_to_points(self, params):
        """Extract Multi Values to Points

Extracts cell values at locations specified in a point feature class from one or more rasters and records the values to the attribute table of the point feature class.

        params: {"in_point_features": <Feature Layer>, "in_rasters":<list[RasterLayer]>, "bilinear_interpolate_values": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_point_features = params.get("in_point_features")
            if in_point_features is None:
                return {"success": False, "error": "in_point_features parameter is required"}
            in_rasters = params.get("in_rasters")
            if in_rasters is None:
                return {"success": False, "error": "in_rasters parameter is required"}
            bilinear_interpolate_values = params.get("bilinear_interpolate_values")

            # Execute Extract Multi Values to Points
            arcpy.sa.ExtractMultiValuesToPoints(in_point_features, in_rasters, bilinear_interpolate_values)

            return {"success": True, "output_layer": os.path.basename(in_point_features), "output_path": in_point_features}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_values_to_points(self, params):
        """Extract Values to Points

Extracts the cell values of a raster based on a set of point features and records the values in the attribute table of an output feature class. The Extract Multi Values to Point tool provides enhanced functionality or performance.

        params: {"in_point_features": <Feature Layer>, "in_raster": <Raster Layer>, "out_point_features": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_point_features = params.get("in_point_features")
            if in_point_features is None:
                return {"success": False, "error": "in_point_features parameter is required"}
            in_raster = params.get("in_raster")
            if in_raster is None:
                return {"success": False, "error": "in_raster parameter is required"}
            out_point_features = params.get("out_point_features")
            if out_point_features is None:
                return {"success": False, "error": "out_point_features parameter is required"}
            interpolate_values = params.get("interpolate_values")
            add_attributes = params.get("add_attributes")

            # Execute Extract Values to Points
            arcpy.sa.ExtractValuesToPoints(in_point_features, in_raster, out_point_features, interpolate_values, add_attributes)

            self._add_to_map(out_point_features)
            return {"success": True, "output_layer": os.path.basename(out_point_features), "output_path": out_point_features}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def sample(self, params):
        """Sample

Creates a table or a point feature class that shows the values of cells from a raster, or a set of rasters, for defined locations. The locations are defined by raster cells, points, polylines, or polygons. Learn more about how Sample works

        params: {"in_rasters": <Raster Layer>, "in_location_data": <Raster Layer; Feature Layer>, "out_table": <Table; Point feature class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_rasters = params.get("in_rasters")
            if in_rasters is None:
                return {"success": False, "error": "in_rasters parameter is required"}
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

            # Execute Sample
            arcpy.sa.Sample(in_rasters, in_location_data, out_table, resampling_type, unique_id_field, process_as_multidimensional, acquisition_definition, statistics_type, percentile_value, buffer_distance, layout, generate_feature_class)

            # Cannot determine if it's a table or feature class, so cannot add to map reliably
            return {"success": True, "output_path": out_table}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def aggregate(self, params):
        """Aggregate

Generates a reduced-resolution version of a raster. Each output cell contains the Sum, Minimum, Maximum, Mean, or Median of the input cells that are encompassed by the extent of that cell. Learn more about how Aggregate works

        params: {"in_raster": <Raster Layer>, "cell_factor": <Long>, "aggregation_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None:
                return {"success": False, "error": "in_raster parameter is required"}
            cell_factor = params.get("cell_factor")
            if cell_factor is None:
                return {"success": False, "error": "cell_factor parameter is required"}
            aggregation_type = params.get("aggregation_type")
            extent_handling = params.get("extent_handling")
            ignore_nodata = params.get("ignore_nodata")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_raster)).replace(' ', '_')}_Aggregate"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Aggregate
            result = arcpy.sa.Aggregate(in_raster, cell_factor, aggregation_type, extent_handling, ignore_nodata)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def boundary_clean(self, params):
        """Boundary Clean

Smooths the boundary between zones in a raster. Learn more about how Boundary Clean works

        params: {"in_raster": <Raster Layer>, "sort_type": <String>, "number_of_runs": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None:
                return {"success": False, "error": "in_raster parameter is required"}
            sort_type = params.get("sort_type")
            number_of_runs = params.get("number_of_runs")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_raster)).replace(' ', '_')}_Boundary_Clean"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Boundary Clean
            result = arcpy.sa.BoundaryClean(in_raster, sort_type, number_of_runs)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def expand(self, params):
        """Expand

Expands specified zones of a raster by a specified number of cells. Learn more about how Expand works

        params: {"in_raster": <Raster Layer>, "number_cells": <Long>, "zone_values": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None:
                return {"success": False, "error": "in_raster parameter is required"}
            number_cells = params.get("number_cells")
            if number_cells is None:
                return {"success": False, "error": "number_cells parameter is required"}
            zone_values = params.get("zone_values")
            if zone_values is None:
                return {"success": False, "error": "zone_values parameter is required"}
            expand_method = params.get("expand_method")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_raster)).replace(' ', '_')}_Expand"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Expand
            result = arcpy.sa.Expand(in_raster, number_cells, zone_values, expand_method)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def majority_filter(self, params):
        """Majority Filter

Replaces cells in a raster based on the majority of their contiguous neighboring cells. Learn more about how Majority Filter works

        params: {"in_raster": <Raster Layer>, "number_neighbors": <String>, "majority_definition": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None:
                return {"success": False, "error": "in_raster parameter is required"}
            number_neighbors = params.get("number_neighbors")
            majority_definition = params.get("majority_definition")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_raster)).replace(' ', '_')}_Majority_Filter"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Majority Filter
            result = arcpy.sa.MajorityFilter(in_raster, number_neighbors, majority_definition)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def nibble(self, params):
        """Nibble

Replaces cells of a raster corresponding to a mask with the value of the nearest neighbor. Learn more about how Nibble works

        params: {"in_raster": <Raster Layer>, "in_mask_raster": <Raster Layer>, "nibble_values": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None:
                return {"success": False, "error": "in_raster parameter is required"}
            in_mask_raster = params.get("in_mask_raster")
            if in_mask_raster is None:
                return {"success": False, "error": "in_mask_raster parameter is required"}
            nibble_values = params.get("nibble_values")
            nibble_nodata = params.get("nibble_nodata")
            in_zone_raster = params.get("in_zone_raster")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_raster)).replace(' ', '_')}_Nibble"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Nibble
            result = arcpy.sa.Nibble(in_raster, in_mask_raster, nibble_values, nibble_nodata, in_zone_raster)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def region_group(self, params):
        """Region Group

For each cell in the output, the identity of the connected region to which that cell belongs is recorded. A unique number is assigned to each region. Learn more about creating individual zones with Region Group

        params: {"in_raster": <Raster Layer>, "number_neighbors": <String>, "zone_connectivity": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None:
                return {"success": False, "error": "in_raster parameter is required"}
            number_neighbors = params.get("number_neighbors")
            zone_connectivity = params.get("zone_connectivity")
            add_link = params.get("add_link")
            excluded_value = params.get("excluded_value")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_raster)).replace(' ', '_')}_Region_Group"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Region Group
            result = arcpy.sa.RegionGroup(in_raster, number_neighbors, zone_connectivity, add_link, excluded_value)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def shrink(self, params):
        """Shrink

Shrinks the selected zones by a specified number of cells by replacing them with the value of the cell that is most frequent in its neighborhood. Learn more about how Shrink works

        params: {"in_raster": <Raster Layer>, "number_cells": <Long>, "zone_values": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None:
                return {"success": False, "error": "in_raster parameter is required"}
            number_cells = params.get("number_cells")
            if number_cells is None:
                return {"success": False, "error": "number_cells parameter is required"}
            zone_values = params.get("zone_values")
            if zone_values is None:
                return {"success": False, "error": "zone_values parameter is required"}
            shrink_method = params.get("shrink_method")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_raster)).replace(' ', '_')}_Shrink"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Shrink
            result = arcpy.sa.Shrink(in_raster, number_cells, zone_values, shrink_method)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def thin(self, params):
        """Thin

Thins rasterized linear features by reducing the number of cells representing the width of the features.

        params: {"in_raster": <Raster Layer>, "background_value": <String>, "filter": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_raster = params.get("in_raster")
            if in_raster is None:
                return {"success": False, "error": "in_raster parameter is required"}
            background_value = params.get("background_value")
            filter = params.get("filter")
            corners = params.get("corners")
            maximum_thickness = params.get("maximum_thickness")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_raster)).replace(' ', '_')}_Thin"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Thin
            result = arcpy.sa.Thin(in_raster, background_value, filter, corners, maximum_thickness)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def darcy_flow(self, params):
        """Darcy Flow

Calculates the groundwater volume balance residual and other outputs for steady flow in an aquifer. Learn more about how Darcy Flow and Darcy Velocity work

        params: {"in_head_raster": <Raster Layer>, "in_porosity_raster": <Raster Layer>, "in_thickness_raster": <Raster Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_head_raster = params.get("in_head_raster")
            if in_head_raster is None:
                return {"success": False, "error": "in_head_raster parameter is required"}
            in_porosity_raster = params.get("in_porosity_raster")
            if in_porosity_raster is None:
                return {"success": False, "error": "in_porosity_raster parameter is required"}
            in_thickness_raster = params.get("in_thickness_raster")
            if in_thickness_raster is None:
                return {"success": False, "error": "in_thickness_raster parameter is required"}
            in_transmissivity_raster = params.get("in_transmissivity_raster")
            if in_transmissivity_raster is None:
                return {"success": False, "error": "in_transmissivity_raster parameter is required"}
            out_direction_raster = params.get("out_direction_raster")
            out_magnitude_raster = params.get("out_magnitude_raster")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_head_raster)).replace(' ', '_')}_Darcy_Flow"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Darcy Flow
            result = arcpy.sa.DarcyFlow(in_head_raster, in_porosity_raster, in_thickness_raster, in_transmissivity_raster, out_direction_raster, out_magnitude_raster)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def darcy_velocity(self, params):
        """Darcy Velocity

Calculates the groundwater seepage velocity vector (direction and magnitude) for steady flow in an aquifer. Learn more about how Darcy Flow and Darcy Velocity work

        params: {"in_head_raster": <Raster Layer>, "in_porosity_raster": <Raster Layer>, "in_thickness_raster": <Raster Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_head_raster = params.get("in_head_raster")
            if in_head_raster is None:
                return {"success": False, "error": "in_head_raster parameter is required"}
            in_porosity_raster = params.get("in_porosity_raster")
            if in_porosity_raster is None:
                return {"success": False, "error": "in_porosity_raster parameter is required"}
            in_thickness_raster = params.get("in_thickness_raster")
            if in_thickness_raster is None:
                return {"success": False, "error": "in_thickness_raster parameter is required"}
            in_transmissivity_raster = params.get("in_transmissivity_raster")
            if in_transmissivity_raster is None:
                return {"success": False, "error": "in_transmissivity_raster parameter is required"}
            out_magnitude_raster = params.get("out_magnitude_raster")
            if out_magnitude_raster is None:
                return {"success": False, "error": "out_magnitude_raster parameter is required"}

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_head_raster)).replace(' ', '_')}_Darcy_Velocity"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Darcy Velocity
            result = arcpy.sa.DarcyVelocity(in_head_raster, in_porosity_raster, in_thickness_raster, in_transmissivity_raster, out_magnitude_raster)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def particle_track(self, params):
        """Particle Track

Calculates the path of a particle through a velocity field, returning an ASCII file of particle tracking data and, optionally, a feature class of track information. Learn more about how Particle Track works

        params: {"in_direction_raster": <Raster Layer>, "in_magnitude_raster": <Raster Layer>, "source_point": <Point>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_direction_raster = params.get("in_direction_raster")
            if in_direction_raster is None:
                return {"success": False, "error": "in_direction_raster parameter is required"}
            in_magnitude_raster = params.get("in_magnitude_raster")
            if in_magnitude_raster is None:
                return {"success": False, "error": "in_magnitude_raster parameter is required"}
            source_point = params.get("source_point")
            if source_point is None:
                return {"success": False, "error": "source_point parameter is required"}
            out_track_file = params.get("out_track_file")
            if out_track_file is None:
                return {"success": False, "error": "out_track_file parameter is required"}
            step_length = params.get("step_length")
            tracking_time = params.get("tracking_time")
            out_track_polyline_features = params.get("out_track_polyline_features")

            # Execute Particle Track
            arcpy.sa.ParticleTrack(in_direction_raster, in_magnitude_raster, source_point, out_track_file, step_length, tracking_time, out_track_polyline_features)

            if out_track_polyline_features:
                self._add_to_map(out_track_polyline_features)
                return {"success": True, "output_layer": os.path.basename(out_track_polyline_features), "output_path": out_track_polyline_features}
            else:
                return {"success": True, "output_path": out_track_file}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def porous_puff(self, params):
        """Porous Puff

Calculates the time-dependent, two-dimensional concentration distribution in mass per volume of a solute introduced instantaneously and at a discrete point into a vertically mixed aquifer. Learn more about how Porous Puff works

        params: {"in_track_file": <File>, "in_porosity_raster": <Raster Layer>, "in_thickness_raster": <Raster Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_track_file = params.get("in_track_file")
            if in_track_file is None:
                return {"success": False, "error": "in_track_file parameter is required"}
            in_porosity_raster = params.get("in_porosity_raster")
            if in_porosity_raster is None:
                return {"success": False, "error": "in_porosity_raster parameter is required"}
            in_thickness_raster = params.get("in_thickness_raster")
            if in_thickness_raster is None:
                return {"success": False, "error": "in_thickness_raster parameter is required"}
            mass = params.get("mass")
            if mass is None:
                return {"success": False, "error": "mass parameter is required"}
            dispersion_time = params.get("dispersion_time")
            longitudinal_dispersivity = params.get("longitudinal_dispersivity")
            dispersivity_ratio = params.get("dispersivity_ratio")
            retardation_factor = params.get("retardation_factor")
            decay_coefficient = params.get("decay_coefficient")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_track_file)).replace(' ', '_')}_Porous_Puff"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Porous Puff
            result = arcpy.sa.PorousPuff(in_track_file, in_porosity_raster, in_thickness_raster, mass, dispersion_time, longitudinal_dispersivity, dispersivity_ratio, retardation_factor, decay_coefficient)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def basin(self, params):
        """Basin

Creates a raster delineating all drainage basins.

        params: {"in_flow_direction_raster": <Raster Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_flow_direction_raster = params.get("in_flow_direction_raster")
            if in_flow_direction_raster is None:
                return {"success": False, "error": "in_flow_direction_raster parameter is required"}

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_flow_direction_raster)).replace(' ', '_')}_Basin"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Basin
            result = arcpy.sa.Basin(in_flow_direction_raster)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def derive_continuous_flow(self, params):
        """Derive Continuous Flow

Generates a raster of accumulated flow into each cell from an input surface raster with no prior sink or depression filling required. Learn more about how Derive Continuous Flow works

        params: {"in_surface_raster": <Raster Layer>, "in_depressions_data": <Composite Geodataset>, "in_weight_raster": <Raster Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_surface_raster = params.get("in_surface_raster")
            if in_surface_raster is None:
                return {"success": False, "error": "in_surface_raster parameter is required"}
            in_depressions_data = params.get("in_depressions_data")
            in_weight_raster = params.get("in_weight_raster")
            out_flow_direction_raster = params.get("out_flow_direction_raster")
            flow_direction_type = params.get("flow_direction_type")
            force_flow = params.get("force_flow")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_surface_raster)).replace(' ', '_')}_Derive_Continuous_Flow"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Derive Continuous Flow
            result = arcpy.sa.DeriveContinuousFlow(in_surface_raster, in_depressions_data, in_weight_raster, out_flow_direction_raster, flow_direction_type, force_flow)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def derive_stream_as_line(self, params):
        """Derive Stream As Line

Generates stream line features from an input surface raster with no prior sink or depression filling required.

        params: {"in_surface_raster": <Raster Layer>, "out_stream_features": <Feature Class>, "in_depressions_data": <Composite Geodataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_surface_raster = params.get("in_surface_raster")
            if in_surface_raster is None:
                return {"success": False, "error": "in_surface_raster parameter is required"}
            out_stream_features = params.get("out_stream_features")
            if out_stream_features is None:
                return {"success": False, "error": "out_stream_features parameter is required"}
            in_depressions_data = params.get("in_depressions_data")
            in_weight_raster = params.get("in_weight_raster")
            accumulation_threshold = params.get("accumulation_threshold")
            stream_designation_method = params.get("stream_designation_method")
            simplify = params.get("simplify")

            # Execute Derive Stream As Line
            arcpy.sa.DeriveStreamAsLine(in_surface_raster, out_stream_features, in_depressions_data, in_weight_raster, accumulation_threshold, stream_designation_method, simplify)

            self._add_to_map(out_stream_features)
            return {"success": True, "output_layer": os.path.basename(out_stream_features), "output_path": out_stream_features}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def derive_stream_as_raster(self, params):
        """Derive Stream As Raster

Generates a stream raster from an input surface raster with no prior sink or depression filling required.

        params: {"in_surface_raster": <Raster Layer>, "in_depressions_data": <Composite Geodataset>, "in_weight_raster": <Raster Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_surface_raster = params.get("in_surface_raster")
            if in_surface_raster is None:
                return {"success": False, "error": "in_surface_raster parameter is required"}
            in_depressions_data = params.get("in_depressions_data")
            in_weight_raster = params.get("in_weight_raster")
            accumulation_threshold = params.get("accumulation_threshold")
            stream_designation_method = params.get("stream_designation_method")
            force_flow = params.get("force_flow")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_surface_raster)).replace(' ', '_')}_Derive_Stream_As_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Derive Stream As Raster
            result = arcpy.sa.DeriveStreamAsRaster(in_surface_raster, in_depressions_data, in_weight_raster, accumulation_threshold, stream_designation_method, force_flow)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def fill(self, params):
        """Fill

Fills sinks in a surface raster to remove small imperfections in the data. Learn more about how Fill works

        params: {"in_surface_raster": <Raster Layer>, "z_limit": <Double>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_surface_raster = params.get("in_surface_raster")
            if in_surface_raster is None:
                return {"success": False, "error": "in_surface_raster parameter is required"}
            z_limit = params.get("z_limit")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_surface_raster)).replace(' ', '_')}_Fill"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Fill
            result = arcpy.sa.Fill(in_surface_raster, z_limit)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def flow_accumulation(self, params):
        """Flow Accumulation

Creates a raster of accumulated flow into each cell. A weight factor can optionally be applied. Learn more about how Flow Accumulation works

        params: {"in_flow_direction_raster": <Raster Layer>, "in_weight_raster": <Raster Layer>, "data_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_flow_direction_raster = params.get("in_flow_direction_raster")
            if in_flow_direction_raster is None:
                return {"success": False, "error": "in_flow_direction_raster parameter is required"}
            in_weight_raster = params.get("in_weight_raster")
            data_type = params.get("data_type")
            flow_direction_type = params.get("flow_direction_type")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_flow_direction_raster)).replace(' ', '_')}_Flow_Accumulation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Flow Accumulation
            result = arcpy.sa.FlowAccumulation(in_flow_direction_raster, in_weight_raster, data_type, flow_direction_type)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def flow_direction(self, params):
        """Flow Direction

Creates a raster of flow direction from each cell to its downslope neighbor, or neighbors, using the D8, Multiple Flow Direction (MFD), or D-Infinity (DINF) method. Learn more about how Flow Direction works

        params: {"in_surface_raster": <Raster Layer>, "force_flow": <Boolean>, "out_drop_raster": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_surface_raster = params.get("in_surface_raster")
            if in_surface_raster is None:
                return {"success": False, "error": "in_surface_raster parameter is required"}
            force_flow = params.get("force_flow")
            out_drop_raster = params.get("out_drop_raster")
            flow_direction_type = params.get("flow_direction_type")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_surface_raster)).replace(' ', '_')}_Flow_Direction"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Flow Direction
            result = arcpy.sa.FlowDirection(in_surface_raster, force_flow, out_drop_raster, flow_direction_type)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def flow_distance(self, params):
        """Flow Distance

Computes, for each cell, the horizontal or vertical component of downslope distance, following the flow paths, to cells on a stream into which they flow. In case of multiple flow paths, minimum, weighted mean, or maximum flow distance can be computed. If an optional flow direction raster is provided, the down slope direction(s) will be limited to those defined by the input flow direction raster.

        params: {"in_stream_raster": <Raster Layer>, "in_surface_raster": <Raster Layer>, "in_flow_direction_raster": <Raster Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_stream_raster = params.get("in_stream_raster")
            if in_stream_raster is None:
                return {"success": False, "error": "in_stream_raster parameter is required"}
            in_surface_raster = params.get("in_surface_raster")
            if in_surface_raster is None:
                return {"success": False, "error": "in_surface_raster parameter is required"}
            in_flow_direction_raster = params.get("in_flow_direction_raster")
            distance_type = params.get("distance_type")
            flow_direction_type = params.get("flow_direction_type")
            statistics_type = params.get("statistics_type")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_stream_raster)).replace(' ', '_')}_Flow_Distance"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Flow Distance
            result = arcpy.sa.FlowDistance(in_stream_raster, in_surface_raster, in_flow_direction_raster, distance_type, flow_direction_type, statistics_type)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def flow_length(self, params):
        """Flow Length

Calculates the upstream or downstream distance, or weighted distance, along the flow path for each cell.

        params: {"in_flow_direction_raster": <Raster Layer>, "direction_measurement": <String>, "in_weight_raster": <Raster Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_flow_direction_raster = params.get("in_flow_direction_raster")
            if in_flow_direction_raster is None:
                return {"success": False, "error": "in_flow_direction_raster parameter is required"}
            direction_measurement = params.get("direction_measurement")
            in_weight_raster = params.get("in_weight_raster")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_flow_direction_raster)).replace(' ', '_')}_Flow_Length"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Flow Length
            result = arcpy.sa.FlowLength(in_flow_direction_raster, direction_measurement, in_weight_raster)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def sink(self, params):
        """Sink

Creates a raster identifying all sinks or areas of internal drainage. Learn more about how Sink works

        params: {"in_flow_direction_raster": <Raster Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_flow_direction_raster = params.get("in_flow_direction_raster")
            if in_flow_direction_raster is None:
                return {"success": False, "error": "in_flow_direction_raster parameter is required"}

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_flow_direction_raster)).replace(' ', '_')}_Sink"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Sink
            result = arcpy.sa.Sink(in_flow_direction_raster)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def snap_pour_point(self, params):
        """Snap Pour Point

Snaps pour points to the cell of highest flow accumulation within a specified distance.

        params: {"in_pour_point_data": <Raster Layer; Feature Layer>, "in_accumulation_raster": <Raster Layer>, "snap_distance": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_pour_point_data = params.get("in_pour_point_data")
            if in_pour_point_data is None:
                return {"success": False, "error": "in_pour_point_data parameter is required"}
            in_accumulation_raster = params.get("in_accumulation_raster")
            if in_accumulation_raster is None:
                return {"success": False, "error": "in_accumulation_raster parameter is required"}
            snap_distance = params.get("snap_distance")
            if snap_distance is None:
                return {"success": False, "error": "snap_distance parameter is required"}
            pour_point_field = params.get("pour_point_field")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_pour_point_data)).replace(' ', '_')}_Snap_Pour_Point"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Snap Pour Point
            result = arcpy.sa.SnapPourPoint(in_pour_point_data, in_accumulation_raster, snap_distance, pour_point_field)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def storage_capacity(self, params):
        """Storage Capacity

Creates a table and a chart of elevations and corresponding storage capacities for an input surface raster. The tool calculates the surface area and total volume of the underlying region at a series of elevation increments.

        params: {"in_surface_raster": <Raster Layer>, "out_table": <Table>, "in_zone_data": <Raster Layer; Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_surface_raster = params.get("in_surface_raster")
            if in_surface_raster is None:
                return {"success": False, "error": "in_surface_raster parameter is required"}
            out_table = params.get("out_table")
            if out_table is None:
                return {"success": False, "error": "out_table parameter is required"}
            in_zone_data = params.get("in_zone_data")
            if in_zone_data is None:
                return {"success": False, "error": "in_zone_data parameter is required"}
            zone_field = params.get("zone_field")
            analysis_type = params.get("analysis_type")
            min_elevation = params.get("min_elevation")
            max_elevation = params.get("max_elevation")
            increment_type = params.get("increment_type")
            increment = params.get("increment")
            z_unit = params.get("z_unit")
            out_chart = params.get("out_chart")

            # Execute Storage Capacity
            arcpy.sa.StorageCapacity(in_surface_raster, out_table, in_zone_data, zone_field, analysis_type, min_elevation, max_elevation, increment_type, increment, z_unit, out_chart)

            return {"success": True, "output_path": out_table}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def stream_link(self, params):
        """Stream Link

Assigns unique values to sections of a raster linear network between intersections.

        params: {"in_stream_raster": <Raster Layer>, "in_flow_direction_raster": <Raster Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_stream_raster = params.get("in_stream_raster")
            if in_stream_raster is None:
                return {"success": False, "error": "in_stream_raster parameter is required"}
            in_flow_direction_raster = params.get("in_flow_direction_raster")
            if in_flow_direction_raster is None:
                return {"success": False, "error": "in_flow_direction_raster parameter is required"}

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_stream_raster)).replace(' ', '_')}_Stream_Link"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Stream Link
            result = arcpy.sa.StreamLink(in_stream_raster, in_flow_direction_raster)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def stream_order(self, params):
        """Stream Order

Assigns a numeric order to segments of a raster representing branches of a linear network. Learn more about how Stream Order works

        params: {"in_stream_raster": <Raster Layer>, "in_flow_direction_raster": <Raster Layer>, "order_method": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_stream_raster = params.get("in_stream_raster")
            if in_stream_raster is None:
                return {"success": False, "error": "in_stream_raster parameter is required"}
            in_flow_direction_raster = params.get("in_flow_direction_raster")
            if in_flow_direction_raster is None:
                return {"success": False, "error": "in_flow_direction_raster parameter is required"}
            order_method = params.get("order_method")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_stream_raster)).replace(' ', '_')}_Stream_Order"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Stream Order
            result = arcpy.sa.StreamOrder(in_stream_raster, in_flow_direction_raster, order_method)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def stream_to_feature(self, params):
        """Stream to Feature

Converts a raster representing a linear network to features representing the linear network. Learn more about how Stream to Feature works

        params: {"in_stream_raster": <Raster Layer>, "in_flow_direction_raster": <Raster Layer>, "out_polyline_features": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_stream_raster = params.get("in_stream_raster")
            if in_stream_raster is None:
                return {"success": False, "error": "in_stream_raster parameter is required"}
            in_flow_direction_raster = params.get("in_flow_direction_raster")
            if in_flow_direction_raster is None:
                return {"success": False, "error": "in_flow_direction_raster parameter is required"}
            out_polyline_features = params.get("out_polyline_features")
            if out_polyline_features is None:
                return {"success": False, "error": "out_polyline_features parameter is required"}
            simplify = params.get("simplify")

            # Execute Stream to Feature
            arcpy.sa.StreamToFeature(in_stream_raster, in_flow_direction_raster, out_polyline_features, simplify)

            self._add_to_map(out_polyline_features)
            return {"success": True, "output_layer": os.path.basename(out_polyline_features), "output_path": out_polyline_features}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def watershed(self, params):
        """Watershed

Determines the contributing area above a set of cells in a raster. Learn more about how Watershed works

        params: {"in_flow_direction_raster": <Raster Layer>, "in_pour_point_data": <Raster Layer; Feature Layer>, "pour_point_field": <Field>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_flow_direction_raster = params.get("in_flow_direction_raster")
            if in_flow_direction_raster is None:
                return {"success": False, "error": "in_flow_direction_raster parameter is required"}
            in_pour_point_data = params.get("in_pour_point_data")
            if in_pour_point_data is None:
                return {"success": False, "error": "in_pour_point_data parameter is required"}
            pour_point_field = params.get("pour_point_field")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_flow_direction_raster)).replace(' ', '_')}_Watershed"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Watershed
            result = arcpy.sa.Watershed(in_flow_direction_raster, in_pour_point_data, pour_point_field)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def idw(self, params):
        """IDW

Interpolates a raster surface from points using an inverse distance weighted (IDW) technique. Learn more about how IDW works

        params: {"in_point_features": <Feature Layer>, "z_field": <Field>, "cell_size": <Analysis Cell Size>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_point_features = params.get("in_point_features")
            if in_point_features is None:
                return {"success": False, "error": "in_point_features parameter is required"}
            z_field = params.get("z_field")
            if z_field is None:
                return {"success": False, "error": "z_field parameter is required"}
            cell_size = params.get("cell_size")
            power = params.get("power")
            search_radius = params.get("search_radius")
            in_barrier_polyline_features = params.get("in_barrier_polyline_features")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_point_features)).replace(' ', '_')}_IDW"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute IDW
            result = arcpy.sa.Idw(in_point_features, z_field, cell_size, power, search_radius, in_barrier_polyline_features)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def kriging(self, params):
        """Kriging

Interpolates a raster surface from points using kriging. The Empirical Bayesian Kriging tool provides enhanced functionality or performance. Learn more about how Kriging works

        params: {"in_point_features": <Feature Layer>, "z_field": <Field>, "kriging_model": <KrigingModel>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_point_features = params.get("in_point_features")
            if in_point_features is None:
                return {"success": False, "error": "in_point_features parameter is required"}
            z_field = params.get("z_field")
            if z_field is None:
                return {"success": False, "error": "z_field parameter is required"}
            kriging_model = params.get("kriging_model")
            if kriging_model is None:
                return {"success": False, "error": "kriging_model parameter is required"}
            cell_size = params.get("cell_size")
            search_radius = params.get("search_radius")
            out_variance_prediction_raster = params.get("out_variance_prediction_raster")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_point_features)).replace(' ', '_')}_Kriging"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Kriging
            result = arcpy.sa.Kriging(in_point_features, z_field, kriging_model, cell_size, search_radius, out_variance_prediction_raster)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def natural_neighbor(self, params):
        """Natural Neighbor

Interpolates a raster surface from points using a natural neighbor technique. Learn more about how Natural Neighbor works

        params: {"in_point_features": <Feature Layer>, "z_field": <Field>, "cell_size": <Analysis Cell Size>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_point_features = params.get("in_point_features")
            if in_point_features is None:
                return {"success": False, "error": "in_point_features parameter is required"}
            z_field = params.get("z_field")
            if z_field is None:
                return {"success": False, "error": "z_field parameter is required"}
            cell_size = params.get("cell_size")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_point_features)).replace(' ', '_')}_Natural_Neighbor"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Natural Neighbor
            result = arcpy.sa.NaturalNeighbor(in_point_features, z_field, cell_size)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def spline(self, params):
        """Spline

Interpolates a raster surface from points using a two-dimensional minimum curvature spline technique. The resulting smooth surface passes exactly through the input points. Learn more about how Spline works

        params: {"in_point_features": <Feature Layer>, "z_field": <Field>, "cell_size": <Analysis Cell Size>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_point_features = params.get("in_point_features")
            if in_point_features is None:
                return {"success": False, "error": "in_point_features parameter is required"}
            z_field = params.get("z_field")
            if z_field is None:
                return {"success": False, "error": "z_field parameter is required"}
            cell_size = params.get("cell_size")
            spline_type = params.get("spline_type")
            weight = params.get("weight")
            number_points = params.get("number_points")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_point_features)).replace(' ', '_')}_Spline"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Spline
            result = arcpy.sa.Spline(in_point_features, z_field, cell_size, spline_type, weight, number_points)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def spline_with_barriers(self, params):
        """Spline with Barriers

Interpolates a raster surface, using barriers, from points using a minimum curvature spline technique. The barriers are entered as either polygon or polyline features. Learn more about how Spline with Barriers works

        params: {"in_point_features": <Feature Layer>, "z_value_field": <Field>, "input_barrier_features": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_point_features = params.get("in_point_features")
            if in_point_features is None:
                return {"success": False, "error": "in_point_features parameter is required"}
            z_value_field = params.get("z_value_field")
            if z_value_field is None:
                return {"success": False, "error": "z_value_field parameter is required"}
            input_barrier_features = params.get("input_barrier_features")
            output_cell_size = params.get("output_cell_size")
            smoothing_factor = params.get("smoothing_factor")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_point_features)).replace(' ', '_')}_Spline_with_Barriers"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Spline with Barriers
            result = arcpy.sa.SplineWithBarriers(in_point_features, z_value_field, input_barrier_features, output_cell_size, smoothing_factor)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def topo_to_raster(self, params):
        """Topo to Raster

Interpolates a hydrologically correct raster surface from point, line, and polygon data. Learn more about how Topo to Raster works

        params: {"in_topo_features": <TopoInput>, "cell_size": <Analysis Cell Size>, "extent": <Extent>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_topo_features = params.get("in_topo_features")
            if in_topo_features is None:
                return {"success": False, "error": "in_topo_features parameter is required"}
            cell_size = params.get("cell_size")
            extent = params.get("extent")
            margin = params.get("margin")
            minimum_z_value = params.get("minimum_z_value")
            maximum_z_value = params.get("maximum_z_value")
            enforce = params.get("enforce")
            data_type = params.get("data_type")
            maximum_iterations = params.get("maximum_iterations")
            roughness_penalty = params.get("roughness_penalty")
            discrete_error_factor = params.get("discrete_error_factor")
            vertical_standard_error = params.get("vertical_standard_error")
            tolerance_1 = params.get("tolerance_1")
            tolerance_2 = params.get("tolerance_2")
            out_stream_features = params.get("out_stream_features")
            out_sink_features = params.get("out_sink_features")
            out_diagnostic_file = params.get("out_diagnostic_file")
            out_parameter_file = params.get("out_parameter_file")
            profile_penalty = params.get("profile_penalty")
            out_residual_feature = params.get("out_residual_feature")
            out_stream_cliff_error_feature = params.get("out_stream_cliff_error_feature")
            out_contour_error_feature = params.get("out_contour_error_feature")

            # Generate output name and path
            output_name = "Topo_to_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Topo to Raster
            result = arcpy.sa.TopoToRaster(in_topo_features, cell_size, extent, margin, minimum_z_value, maximum_z_value, enforce, data_type, maximum_iterations, roughness_penalty, discrete_error_factor, vertical_standard_error, tolerance_1, tolerance_2, out_stream_features, out_sink_features, out_diagnostic_file, out_parameter_file, profile_penalty, out_residual_feature, out_stream_cliff_error_feature, out_contour_error_feature)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def topo_to_raster_by_file(self, params):
        """Topo to Raster by File

Interpolates a hydrologically correct raster surface from point, line, and polygon data using parameters specified in a file. Learn more about how Topo to Raster works

        params: {"in_parameter_file": <File>, "out_stream_features": <Feature Class>, "out_sink_features": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_parameter_file = params.get("in_parameter_file")
            if in_parameter_file is None:
                return {"success": False, "error": "in_parameter_file parameter is required"}
            out_stream_features = params.get("out_stream_features")
            out_sink_features = params.get("out_sink_features")
            out_residual_feature = params.get("out_residual_feature")
            out_stream_cliff_error_feature = params.get("out_stream_cliff_error_feature")
            out_contour_error_feature = params.get("out_contour_error_feature")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_parameter_file)).replace(' ', '_')}_Topo_to_Raster_by_File"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Topo to Raster by File
            result = arcpy.sa.TopoToRasterByFile(in_parameter_file, out_stream_features, out_sink_features, out_residual_feature, out_stream_cliff_error_feature, out_contour_error_feature)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def trend(self, params):
        """Trend

Interpolates a raster surface from points using a trend technique. Learn more about how Trend works

        params: {"in_point_features": <Feature Layer>, "z_field": <Field>, "cell_size": <Analysis Cell Size>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_point_features = params.get("in_point_features")
            if in_point_features is None:
                return {"success": False, "error": "in_point_features parameter is required"}
            z_field = params.get("z_field")
            if z_field is None:
                return {"success": False, "error": "z_field parameter is required"}
            cell_size = params.get("cell_size")
            order = params.get("order")
            regression_type = params.get("regression_type")
            out_rms_file = params.get("out_rms_file")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_point_features)).replace(' ', '_')}_Trend"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Trend
            result = arcpy.sa.Trend(in_point_features, z_field, cell_size, order, regression_type, out_rms_file)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def cell_statistics(self, params):
        """Cell Statistics

Calculates a per-cell statistic from multiple rasters. The available statistics are Majority, Maximum, Mean, Median, Minimum, Minority, Percentile, Range, Standard deviation, Sum, and Variety. Learn more about how Cell Statistics works

        params: {"in_rasters_or_constants": <Raster Layer; Constant>, "statistics_type": <String>, "ignore_nodata": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_rasters_or_constants = params.get("in_rasters_or_constants")
            if in_rasters_or_constants is None:
                return {"success": False, "error": "in_rasters_or_constants parameter is required"}
            statistics_type = params.get("statistics_type")
            ignore_nodata = params.get("ignore_nodata")
            process_as_multiband = params.get("process_as_multiband")
            percentile_value = params.get("percentile_value")
            percentile_interpolation_type = params.get("percentile_interpolation_type")

            # Generate output name and path
            output_name = "Cell_Statistics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Cell Statistics
            result = arcpy.sa.CellStatistics(in_rasters_or_constants, statistics_type, ignore_nodata, process_as_multiband, percentile_value, percentile_interpolation_type)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def combine(self, params):
        """Combine

Combines multiple rasters so that a unique output value is assigned to each unique combination of input values.

        params: {"in_rasters": <Raster Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_rasters = params.get("in_rasters")
            if in_rasters is None:
                return {"success": False, "error": "in_rasters parameter is required"}

            # Generate output name and path
            output_name = "Combine"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Combine
            result = arcpy.sa.Combine(in_rasters)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def equal_to_frequency(self, params):
        """Equal To Frequency

Evaluates on a cell-by-cell basis the number of times the values in a set of rasters are equal to another raster.

        params: {"in_value_raster": <Raster Layer>, "in_rasters": <Raster Layer>, "process_as_multiband": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_value_raster = params.get("in_value_raster")
            if in_value_raster is None:
                return {"success": False, "error": "in_value_raster parameter is required"}
            in_rasters = params.get("in_rasters")
            if in_rasters is None:
                return {"success": False, "error": "in_rasters parameter is required"}
            process_as_multiband = params.get("process_as_multiband")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_value_raster)).replace(' ', '_')}_Equal_To_Frequency"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Equal To Frequency
            result = arcpy.sa.EqualToFrequency(in_value_raster, in_rasters, process_as_multiband)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def greater_than_frequency(self, params):
        """Greater Than Frequency

Evaluates on a cell-by-cell basis the number of times a set of rasters is greater than another raster.

        params: {"in_value_raster": <Raster Layer>, "in_rasters": <Raster Layer>, "process_as_multiband": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_value_raster = params.get("in_value_raster")
            if in_value_raster is None:
                return {"success": False, "error": "in_value_raster parameter is required"}
            in_rasters = params.get("in_rasters")
            if in_rasters is None:
                return {"success": False, "error": "in_rasters parameter is required"}
            process_as_multiband = params.get("process_as_multiband")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_value_raster)).replace(' ', '_')}_Greater_Than_Frequency"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Greater Than Frequency
            result = arcpy.sa.GreaterThanFrequency(in_value_raster, in_rasters, process_as_multiband)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def highest_position(self, params):
        """Highest Position

Determines on a cell-by-cell basis the position of the raster with the maximum value in a set of rasters.

        params: {"in_rasters_or_constants": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_rasters_or_constants = params.get("in_rasters_or_constants")
            if in_rasters_or_constants is None:
                return {"success": False, "error": "in_rasters_or_constants parameter is required"}

            # Generate output name and path
            output_name = "Highest_Position"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Highest Position
            result = arcpy.sa.HighestPosition(in_rasters_or_constants)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def less_than_frequency(self, params):
        """Less Than Frequency

Evaluates on a cell-by-cell basis the number of times a set of rasters is less than another raster.

        params: {"in_value_raster": <Raster Layer>, "in_rasters": <Raster Layer>, "process_as_multiband": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_value_raster = params.get("in_value_raster")
            if in_value_raster is None:
                return {"success": False, "error": "in_value_raster parameter is required"}
            in_rasters = params.get("in_rasters")
            if in_rasters is None:
                return {"success": False, "error": "in_rasters parameter is required"}
            process_as_multiband = params.get("process_as_multiband")

            # Generate output name and path
            output_name = f"{os.path.basename(str(in_value_raster)).replace(' ', '_')}_Less_Than_Frequency"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Less Than Frequency
            result = arcpy.sa.LessThanFrequency(in_value_raster, in_rasters, process_as_multiband)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def lowest_position(self, params):
        """Lowest Position

Determines on a cell-by-cell basis the position of the raster with the minimum value in a set of rasters.

        params: {"in_rasters_or_constants": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_rasters_or_constants = params.get("in_rasters_or_constants")
            if in_rasters_or_constants is None:
                return {"success": False, "error": "in_rasters_or_constants parameter is required"}

            # Generate output name and path
            output_name = "Lowest_Position"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Lowest Position
            result = arcpy.sa.LowestPosition(in_rasters_or_constants)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def popularity(self, params):
        """Popularity

Determines the value in an argument list that is at a certain level of popularity on a cell-by-cell basis. The particular level of popularity (the number of occurrences of each value) is specified by the first argument.

        params: {"in_popularity_raster_or_constant": <Raster Layer; Constant>, "in_rasters": <Raster Layer>, "process_as_multiband": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_popularity_raster_or_constant = params.get("in_popularity_raster_or_constant")
            if in_popularity_raster_or_constant is None:
                return {"success": False, "error": "in_popularity_raster_or_constant parameter is required"}
            in_rasters = params.get("in_rasters")
            if in_rasters is None:
                return {"success": False, "error": "in_rasters parameter is required"}
            process_as_multiband = params.get("process_as_multiband")

            # Generate output name and path
            output_name = "Popularity"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Popularity
            result = arcpy.sa.Popularity(in_popularity_raster_or_constant, in_rasters, process_as_multiband)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def rank(self, params):
        """Rank

Ranks on a cell-by-cell basis the values from a set of input rasters and determines which values are returned based on the value of the rank input raster.

        params: {"in_rank_raster_or_constant": <Raster Layer; Constant>, "in_rasters": <Raster Layer>, "process_as_multiband": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
            in_rank_raster_or_constant = params.get("in_rank_raster_or_constant")
            if in_rank_raster_or_constant is None:
                return {"success": False, "error": "in_rank_raster_or_constant parameter is required"}
            in_rasters = params.get("in_rasters")
            if in_rasters is None:
                return {"success": False, "error": "in_rasters parameter is required"}
            process_as_multiband = params.get("process_as_multiband")

            # Generate output name and path
            output_name = "Rank"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Rank
            result = arcpy.sa.Rank(in_rank_raster_or_constant, in_rasters, process_as_multiband)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Abs"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Abs
            result = arcpy.sa.Abs(in_raster_or_constant)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Divide"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Divide
            result = arcpy.sa.Divide(in_raster_or_constant1, in_raster_or_constant2)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Exp"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Exp
            result = arcpy.sa.Exp(in_raster_or_constant)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Exp10"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Exp10
            result = arcpy.sa.Exp10(in_raster_or_constant)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Exp2"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Exp2
            result = arcpy.sa.Exp2(in_raster_or_constant)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Float"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Float
            result = arcpy.sa.Float(in_raster_or_constant)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Int"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Int
            result = arcpy.sa.Int(in_raster_or_constant)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Ln"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Ln
            result = arcpy.sa.Ln(in_raster_or_constant)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Log10"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Log10
            result = arcpy.sa.Log10(in_raster_or_constant)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Log2"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Log2
            result = arcpy.sa.Log2(in_raster_or_constant)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Minus"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Minus
            result = arcpy.sa.Minus(in_raster_or_constant1, in_raster_or_constant2)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Mod"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Mod
            result = arcpy.sa.Mod(in_raster_or_constant1, in_raster_or_constant2)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Negate"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Negate
            result = arcpy.sa.Negate(in_raster_or_constant)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Plus"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Plus
            result = arcpy.sa.Plus(in_raster_or_constant1, in_raster_or_constant2)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Power"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Power
            result = arcpy.sa.Power(in_raster_or_constant1, in_raster_or_constant2)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Round_Down"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Round Down
            result = arcpy.sa.RoundDown(in_raster_or_constant)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Round_Up"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Round Up
            result = arcpy.sa.RoundUp(in_raster_or_constant)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Square"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Square
            result = arcpy.sa.Square(in_raster_or_constant)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Square_Root"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Square Root
            result = arcpy.sa.SquareRoot(in_raster_or_constant)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

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
            output_name = "Times"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Times
            result = arcpy.sa.Times(in_raster_or_constant1, in_raster_or_constant2)
            result.save(output_path)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": os.path.basename(output_path), "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def __del__(self):
        arcpy.CheckInExtension("Spatial")