# Generated ArcGIS Pro spatial-analyst Progent Functions
# Generated on 2025-10-01T14:46:02.619661
# Total tools: 208

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
            output_name = f"{in_conditional_raster.replace(' ', '_')}_Con"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Con
            arcpy.Con(in_conditional_raster, in_true_raster_or_constant, in_false_raster_or_constant, where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def pick(self, params):
        """Pick

The value from a position raster is used to determine from which raster in a list of input rasters the output cell value will be obtained.

        params: {"in_position_raster": <Raster Layer>, "in_rasters_or_constantsin_raster_or_constant": <Raster Layer; Constant>, "process_as_multiband": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_position_raster = params.get("in_position_raster")
        if in_position_raster is None:
            return {"success": False, "error": "in_position_raster parameter is required"}
        in_rasters_or_constantsin_raster_or_constant = params.get("in_rasters_or_constantsin_raster_or_constant")
        if in_rasters_or_constantsin_raster_or_constant is None:
            return {"success": False, "error": "in_rasters_or_constantsin_raster_or_constant parameter is required"}
        process_as_multiband = params.get("process_as_multiband")

            # Generate output name and path
            output_name = f"{in_position_raster.replace(' ', '_')}_Pick"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Pick
            arcpy.Pick(in_position_raster, in_rasters_or_constantsin_raster_or_constant, process_as_multiband)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def set_None(self, params):
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
            output_name = f"{in_conditional_raster.replace(' ', '_')}_Set_Null"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Set Null
            arcpy.SetNull(in_conditional_raster, in_false_raster_or_constant, where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_features_numerator.replace(' ', '_')}_Calculate_Kernel_Density_Ratio"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Kernel Density Ratio
            arcpy.CalculateKernelDensityRatio(in_features_numerator, in_features_denominator, population_field_numerator, population_field_denominator, cell_size, search_radius_numerator, search_radius_denominator, out_cell_values, method, in_barriers_numerator, in_barriers_denominator)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_features.replace(' ', '_')}_Kernel_Density"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Kernel Density
            arcpy.KernelDensity(in_features, population_field, cell_size, search_radius, area_unit_scale_factor, out_cell_values, method, in_barriers)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_polyline_features.replace(' ', '_')}_Line_Density"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Line Density
            arcpy.LineDensity(in_polyline_features, population_field, cell_size, search_radius, area_unit_scale_factor)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_point_features.replace(' ', '_')}_Point_Density"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Point Density
            arcpy.PointDensity(in_point_features, population_field, cell_size, neighborhood, area_unit_scale_factor)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_features.replace(' ', '_')}_Space_Time_Kernel_Density"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Space Time Kernel Density
            arcpy.SpaceTimeKernelDensity(in_features, population_field, elevation_field, elevation_field_unit, time_field, cell_size, kernel_search_radius_xy, kernel_search_radius_z, kernel_search_time_window, resultant_values, method, min_elevation, max_elevation, elevation_interval, elevation_unit, start_time, end_time, time_interval, time_interval_unit, out_voxel_layer)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_source_data.replace(' ', '_')}_Distance_Accumulation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Distance Accumulation
            arcpy.DistanceAccumulation(in_source_data, in_barrier_data, in_surface_raster, in_cost_raster, in_vertical_raster, vertical_factor, in_horizontal_raster, horizontal_factor, out_back_direction_raster, out_source_direction_raster, out_source_location_raster, source_initial_accumulation, source_maximum_accumulation, source_cost_multiplier, source_direction, distance_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_source_data.replace(' ', '_')}_Distance_Allocation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Distance Allocation
            arcpy.DistanceAllocation(in_source_data, in_barrier_data, in_surface_raster, in_cost_raster, in_vertical_raster, vertical_factor, in_horizontal_raster, horizontal_factor, out_distance_accumulation_raster, out_back_direction_raster, out_source_direction_raster, out_source_location_raster, source_field, source_initial_accumulation, source_maximum_accumulation, source_cost_multiplier, source_direction, distance_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_accumulative_cost_distance_raster1.replace(' ', '_')}_Least_Cost_Corridor"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Least Cost Corridor
            arcpy.LeastCostCorridor(in_accumulative_cost_distance_raster1, in_back_direction_raster1, in_accumulative_cost_distance_raster2, in_back_direction_raster2, threshold_method, threshold)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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

            # Generate output name and path
            output_name = f"{in_regions.replace(' ', '_')}_Optimal_Corridor_Connections"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Optimal Corridor Connections
            arcpy.OptimalCorridorConnections(in_regions, out_optimal_polygons, in_barriers, in_cost_raster, out_optimal_lines, out_neighbor_polygons, out_neighbor_lines, corridor_method, corridor_width, distance_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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

            # Generate output name and path
            output_name = f"{in_destination_data.replace(' ', '_')}_Optimal_Path_As_Line"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Optimal Path As Line
            arcpy.OptimalPathAsLine(in_destination_data, in_distance_accumulation_raster, in_back_direction_raster, out_polyline_features, destination_field, path_type, create_network_paths)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_destination_data.replace(' ', '_')}_Optimal_Path_As_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Optimal Path As Raster
            arcpy.OptimalPathAsRaster(in_destination_data, in_distance_accumulation_raster, in_back_direction_raster, destination_field, path_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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

            # Generate output name and path
            output_name = f"{in_regions.replace(' ', '_')}_Optimal_Region_Connections"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Optimal Region Connections
            arcpy.OptimalRegionConnections(in_regions, out_feature_class, in_barrier_data, in_cost_raster, out_neighbor_paths, distance_method, connections_within_regions)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_raster.replace(' ', '_')}_Extract_by_Attributes"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract by Attributes
            arcpy.ExtractbyAttributes(in_raster, where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_raster.replace(' ', '_')}_Extract_by_Circle"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract by Circle
            arcpy.ExtractbyCircle(in_raster, center_point, radius, extraction_area)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_raster.replace(' ', '_')}_Extract_by_Mask"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract by Mask
            arcpy.ExtractbyMask(in_raster, in_mask_data, extraction_area, analysis_extent)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_by_points(self, params):
        """Extract by Points

Extracts the cells of a raster based on a set of coordinate points. This tool is deprecated and will be removed in a future release. The Extract by Mask tool provides enhanced functionality or performance.

        params: {"in_raster": <Raster Layer>, "pointspoint": <Point>, "extraction_area": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        pointspoint = params.get("pointspoint")
        if pointspoint is None:
            return {"success": False, "error": "pointspoint parameter is required"}
        extraction_area = params.get("extraction_area")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Extract_by_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract by Points
            arcpy.ExtractbyPoints(in_raster, pointspoint, extraction_area)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_by_polygon(self, params):
        """Extract by Polygon

Extracts the cells of a raster based on a polygon by specifying the polygon's vertices. This tool is deprecated and will be removed in a future release. The Extract by Mask tool provides enhanced functionality or performance.

        params: {"in_raster": <Raster Layer>, "polygonpoint": <Point>, "extraction_area": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        polygonpoint = params.get("polygonpoint")
        if polygonpoint is None:
            return {"success": False, "error": "polygonpoint parameter is required"}
        extraction_area = params.get("extraction_area")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Extract_by_Polygon"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract by Polygon
            arcpy.ExtractbyPolygon(in_raster, polygonpoint, extraction_area)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_by_rectangle(self, params):
        """Extract by Rectangle

Extracts the cells of a raster based on a rectangle by specifying the rectangle's extent.

        params: {"in_raster": <Raster Layer>, "rectangleextent": <Extent>, "extraction_area": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        rectangleextent = params.get("rectangleextent")
        if rectangleextent is None:
            return {"success": False, "error": "rectangleextent parameter is required"}
        extraction_area = params.get("extraction_area")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Extract_by_Rectangle"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract by Rectangle
            arcpy.ExtractbyRectangle(in_raster, rectangleextent, extraction_area)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def extract_multi_values_to_points(self, params):
        """Extract Multi Values to Points

Extracts cell values at locations specified in a point feature class from one or more rasters and records the values to the attribute table of the point feature class.

        params: {"in_point_features": <Feature Layer>, "bilinear_interpolate_values": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_point_features = params.get("in_point_features")
        if in_point_features is None:
            return {"success": False, "error": "in_point_features parameter is required"}
        bilinear_interpolate_values = params.get("bilinear_interpolate_values")

            # Generate output name and path
            output_name = f"{in_point_features.replace(' ', '_')}_Extract_Multi_Values_to_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract Multi Values to Points
            arcpy.ExtractMultiValuestoPoints(in_point_features, bilinear_interpolate_values)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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

            # Generate output name and path
            output_name = f"{in_point_features.replace(' ', '_')}_Extract_Values_to_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Extract Values to Points
            arcpy.ExtractValuestoPoints(in_point_features, in_raster, out_point_features, interpolate_values, add_attributes)

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
            output_name = f"{in_raster.replace(' ', '_')}_Aggregate"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Aggregate
            arcpy.Aggregate(in_raster, cell_factor, aggregation_type, extent_handling, ignore_nodata)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_raster.replace(' ', '_')}_Boundary_Clean"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Boundary Clean
            arcpy.BoundaryClean(in_raster, sort_type, number_of_runs)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def expand(self, params):
        """Expand

Expands specified zones of a raster by a specified number of cells. Learn more about how Expand works

        params: {"in_raster": <Raster Layer>, "number_cells": <Long>, "zone_valueszone_value": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        number_cells = params.get("number_cells")
        if number_cells is None:
            return {"success": False, "error": "number_cells parameter is required"}
        zone_valueszone_value = params.get("zone_valueszone_value")
        if zone_valueszone_value is None:
            return {"success": False, "error": "zone_valueszone_value parameter is required"}
        expand_method = params.get("expand_method")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Expand"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Expand
            arcpy.Expand(in_raster, number_cells, zone_valueszone_value, expand_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_raster.replace(' ', '_')}_Majority_Filter"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Majority Filter
            arcpy.MajorityFilter(in_raster, number_neighbors, majority_definition)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_raster.replace(' ', '_')}_Nibble"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Nibble
            arcpy.Nibble(in_raster, in_mask_raster, nibble_values, nibble_nodata, in_zone_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_raster.replace(' ', '_')}_Region_Group"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Region Group
            arcpy.RegionGroup(in_raster, number_neighbors, zone_connectivity, add_link, excluded_value)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def shrink(self, params):
        """Shrink

Shrinks the selected zones by a specified number of cells by replacing them with the value of the cell that is most frequent in its neighborhood. Learn more about how Shrink works

        params: {"in_raster": <Raster Layer>, "number_cells": <Long>, "zone_valueszone_value": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        number_cells = params.get("number_cells")
        if number_cells is None:
            return {"success": False, "error": "number_cells parameter is required"}
        zone_valueszone_value = params.get("zone_valueszone_value")
        if zone_valueszone_value is None:
            return {"success": False, "error": "zone_valueszone_value parameter is required"}
        shrink_method = params.get("shrink_method")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Shrink"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Shrink
            arcpy.Shrink(in_raster, number_cells, zone_valueszone_value, shrink_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_raster.replace(' ', '_')}_Thin"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Thin
            arcpy.Thin(in_raster, background_value, filter, corners, maximum_thickness)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_head_raster.replace(' ', '_')}_Darcy_Flow"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Darcy Flow
            arcpy.DarcyFlow(in_head_raster, in_porosity_raster, in_thickness_raster, in_transmissivity_raster, out_direction_raster, out_magnitude_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_head_raster.replace(' ', '_')}_Darcy_Velocity"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Darcy Velocity
            arcpy.DarcyVelocity(in_head_raster, in_porosity_raster, in_thickness_raster, in_transmissivity_raster, out_magnitude_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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

            # Generate output name and path
            output_name = f"{in_direction_raster.replace(' ', '_')}_Particle_Track"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Particle Track
            arcpy.ParticleTrack(in_direction_raster, in_magnitude_raster, source_point, out_track_file, step_length, tracking_time, out_track_polyline_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_track_file.replace(' ', '_')}_Porous_Puff"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Porous Puff
            arcpy.PorousPuff(in_track_file, in_porosity_raster, in_thickness_raster, mass, dispersion_time, longitudinal_dispersivity, dispersivity_ratio, retardation_factor, decay_coefficient)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_flow_direction_raster.replace(' ', '_')}_Basin"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Basin
            arcpy.Basin(in_flow_direction_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_surface_raster.replace(' ', '_')}_Derive_Continuous_Flow"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Derive Continuous Flow
            arcpy.DeriveContinuousFlow(in_surface_raster, in_depressions_data, in_weight_raster, out_flow_direction_raster, flow_direction_type, force_flow)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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

            # Generate output name and path
            output_name = f"{in_surface_raster.replace(' ', '_')}_Derive_Stream_As_Line"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Derive Stream As Line
            arcpy.DeriveStreamAsLine(in_surface_raster, out_stream_features, in_depressions_data, in_weight_raster, accumulation_threshold, stream_designation_method, simplify)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_surface_raster.replace(' ', '_')}_Derive_Stream_As_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Derive Stream As Raster
            arcpy.DeriveStreamAsRaster(in_surface_raster, in_depressions_data, in_weight_raster, accumulation_threshold, stream_designation_method, force_flow)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_surface_raster.replace(' ', '_')}_Fill"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Fill
            arcpy.Fill(in_surface_raster, z_limit)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_flow_direction_raster.replace(' ', '_')}_Flow_Accumulation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Flow Accumulation
            arcpy.FlowAccumulation(in_flow_direction_raster, in_weight_raster, data_type, flow_direction_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_surface_raster.replace(' ', '_')}_Flow_Direction"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Flow Direction
            arcpy.FlowDirection(in_surface_raster, force_flow, out_drop_raster, flow_direction_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_stream_raster.replace(' ', '_')}_Flow_Distance"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Flow Distance
            arcpy.FlowDistance(in_stream_raster, in_surface_raster, in_flow_direction_raster, distance_type, flow_direction_type, statistics_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_flow_direction_raster.replace(' ', '_')}_Flow_Length"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Flow Length
            arcpy.FlowLength(in_flow_direction_raster, direction_measurement, in_weight_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_flow_direction_raster.replace(' ', '_')}_Sink"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Sink
            arcpy.Sink(in_flow_direction_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_pour_point_data.replace(' ', '_')}_Snap_Pour_Point"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Snap Pour Point
            arcpy.SnapPourPoint(in_pour_point_data, in_accumulation_raster, snap_distance, pour_point_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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

            # Generate output name and path
            output_name = f"{in_surface_raster.replace(' ', '_')}_Storage_Capacity"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Storage Capacity
            arcpy.StorageCapacity(in_surface_raster, out_table, in_zone_data, zone_field, analysis_type, min_elevation, max_elevation, increment_type, increment, z_unit, out_chart)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_stream_raster.replace(' ', '_')}_Stream_Link"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Stream Link
            arcpy.StreamLink(in_stream_raster, in_flow_direction_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_stream_raster.replace(' ', '_')}_Stream_Order"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Stream Order
            arcpy.StreamOrder(in_stream_raster, in_flow_direction_raster, order_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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

            # Generate output name and path
            output_name = f"{in_stream_raster.replace(' ', '_')}_Stream_to_Feature"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Stream to Feature
            arcpy.StreamtoFeature(in_stream_raster, in_flow_direction_raster, out_polyline_features, simplify)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_flow_direction_raster.replace(' ', '_')}_Watershed"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Watershed
            arcpy.Watershed(in_flow_direction_raster, in_pour_point_data, pour_point_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_point_features.replace(' ', '_')}_IDW"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute IDW
            arcpy.IDW(in_point_features, z_field, cell_size, power, search_radius, in_barrier_polyline_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def kriging(self, params):
        """Kriging

Interpolates a raster surface from points using kriging. The Empirical Bayesian Kriging tool provides enhanced functionality or performance. Learn more about how Kriging works

        params: {"in_point_features": <Feature Layer>, "z_field": <Field>, "semivariogram_propskriging_model": <KrigingModel>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_point_features = params.get("in_point_features")
        if in_point_features is None:
            return {"success": False, "error": "in_point_features parameter is required"}
        z_field = params.get("z_field")
        if z_field is None:
            return {"success": False, "error": "z_field parameter is required"}
        semivariogram_propskriging_model = params.get("semivariogram_propskriging_model")
        if semivariogram_propskriging_model is None:
            return {"success": False, "error": "semivariogram_propskriging_model parameter is required"}
        cell_size = params.get("cell_size")
        search_radius = params.get("search_radius")
        out_variance_prediction_raster = params.get("out_variance_prediction_raster")

            # Generate output name and path
            output_name = f"{in_point_features.replace(' ', '_')}_Kriging"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Kriging
            arcpy.Kriging(in_point_features, z_field, semivariogram_propskriging_model, cell_size, search_radius, out_variance_prediction_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_point_features.replace(' ', '_')}_Natural_Neighbor"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Natural Neighbor
            arcpy.NaturalNeighbor(in_point_features, z_field, cell_size)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_point_features.replace(' ', '_')}_Spline"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Spline
            arcpy.Spline(in_point_features, z_field, cell_size, spline_type, weight, number_points)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def spline_with_barriers(self, params):
        """Spline with Barriers

Interpolates a raster surface, using barriers, from points using a minimum curvature spline technique. The barriers are entered as either polygon or polyline features. Learn more about how Spline with Barriers works

        params: {"input_point_featuresin_point_features": <Feature Layer>, "z_value_field": <Field>, "input_barrier_features": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_point_featuresin_point_features = params.get("input_point_featuresin_point_features")
        if input_point_featuresin_point_features is None:
            return {"success": False, "error": "input_point_featuresin_point_features parameter is required"}
        z_value_field = params.get("z_value_field")
        if z_value_field is None:
            return {"success": False, "error": "z_value_field parameter is required"}
        input_barrier_features = params.get("input_barrier_features")
        output_cell_size = params.get("output_cell_size")
        smoothing_factor = params.get("smoothing_factor")

            # Generate output name and path
            output_name = f"{input_point_featuresin_point_features.replace(' ', '_')}_Spline_with_Barriers"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Spline with Barriers
            arcpy.SplinewithBarriers(input_point_featuresin_point_features, z_value_field, input_barrier_features, output_cell_size, smoothing_factor)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def topo_to_raster(self, params):
        """Topo to Raster

Interpolates a hydrologically correct raster surface from point, line, and polygon data. Learn more about how Topo to Raster works

        params: {"in_topo_featurestopo_input": <TopoInput>, "cell_size": <Analysis Cell Size>, "extent": <Extent>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_topo_featurestopo_input = params.get("in_topo_featurestopo_input")
        if in_topo_featurestopo_input is None:
            return {"success": False, "error": "in_topo_featurestopo_input parameter is required"}
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
            output_name = f"{in_topo_featurestopo_input.replace(' ', '_')}_Topo_to_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Topo to Raster
            arcpy.TopotoRaster(in_topo_featurestopo_input, cell_size, extent, margin, minimum_z_value, maximum_z_value, enforce, data_type, maximum_iterations, roughness_penalty, discrete_error_factor, vertical_standard_error, tolerance_1, tolerance_2, out_stream_features, out_sink_features, out_diagnostic_file, out_parameter_file, profile_penalty, out_residual_feature, out_stream_cliff_error_feature, out_contour_error_feature)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_parameter_file.replace(' ', '_')}_Topo_to_Raster_by_File"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Topo to Raster by File
            arcpy.TopotoRasterbyFile(in_parameter_file, out_stream_features, out_sink_features, out_residual_feature, out_stream_cliff_error_feature, out_contour_error_feature)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

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
            output_name = f"{in_point_features.replace(' ', '_')}_Trend"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Trend
            arcpy.Trend(in_point_features, z_field, cell_size, order, regression_type, out_rms_file)

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


    def combine(self, params):
        """Combine

Combines multiple rasters so that a unique output value is assigned to each unique combination of input values.

        params: {"in_rastersin_raster": <Raster Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rastersin_raster = params.get("in_rastersin_raster")
        if in_rastersin_raster is None:
            return {"success": False, "error": "in_rastersin_raster parameter is required"}

            # Generate output name and path
            output_name = f"{in_rastersin_raster.replace(' ', '_')}_Combine"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Combine
            arcpy.Combine(in_rastersin_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def equal_to_frequency(self, params):
        """Equal To Frequency

Evaluates on a cell-by-cell basis the number of times the values in a set of rasters are equal to another raster.

        params: {"in_value_raster": <Raster Layer>, "in_rastersin_raster": <Raster Layer>, "process_as_multiband": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_value_raster = params.get("in_value_raster")
        if in_value_raster is None:
            return {"success": False, "error": "in_value_raster parameter is required"}
        in_rastersin_raster = params.get("in_rastersin_raster")
        if in_rastersin_raster is None:
            return {"success": False, "error": "in_rastersin_raster parameter is required"}
        process_as_multiband = params.get("process_as_multiband")

            # Generate output name and path
            output_name = f"{in_value_raster.replace(' ', '_')}_Equal_To_Frequency"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Equal To Frequency
            arcpy.EqualToFrequency(in_value_raster, in_rastersin_raster, process_as_multiband)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def greater_than_frequency(self, params):
        """Greater Than Frequency

Evaluates on a cell-by-cell basis the number of times a set of rasters is greater than another raster.

        params: {"in_value_raster": <Raster Layer>, "in_rastersin_raster": <Raster Layer>, "process_as_multiband": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_value_raster = params.get("in_value_raster")
        if in_value_raster is None:
            return {"success": False, "error": "in_value_raster parameter is required"}
        in_rastersin_raster = params.get("in_rastersin_raster")
        if in_rastersin_raster is None:
            return {"success": False, "error": "in_rastersin_raster parameter is required"}
        process_as_multiband = params.get("process_as_multiband")

            # Generate output name and path
            output_name = f"{in_value_raster.replace(' ', '_')}_Greater_Than_Frequency"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Greater Than Frequency
            arcpy.GreaterThanFrequency(in_value_raster, in_rastersin_raster, process_as_multiband)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def highest_position(self, params):
        """Highest Position

Determines on a cell-by-cell basis the position of the raster with the maximum value in a set of rasters.

        params: {"in_rasters_or_constantsin_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rasters_or_constantsin_raster_or_constant = params.get("in_rasters_or_constantsin_raster_or_constant")
        if in_rasters_or_constantsin_raster_or_constant is None:
            return {"success": False, "error": "in_rasters_or_constantsin_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_rasters_or_constantsin_raster_or_constant.replace(' ', '_')}_Highest_Position"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Highest Position
            arcpy.HighestPosition(in_rasters_or_constantsin_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def less_than_frequency(self, params):
        """Less Than Frequency

Evaluates on a cell-by-cell basis the number of times a set of rasters is less than another raster.

        params: {"in_value_raster": <Raster Layer>, "in_rastersin_raster": <Raster Layer>, "process_as_multiband": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_value_raster = params.get("in_value_raster")
        if in_value_raster is None:
            return {"success": False, "error": "in_value_raster parameter is required"}
        in_rastersin_raster = params.get("in_rastersin_raster")
        if in_rastersin_raster is None:
            return {"success": False, "error": "in_rastersin_raster parameter is required"}
        process_as_multiband = params.get("process_as_multiband")

            # Generate output name and path
            output_name = f"{in_value_raster.replace(' ', '_')}_Less_Than_Frequency"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Less Than Frequency
            arcpy.LessThanFrequency(in_value_raster, in_rastersin_raster, process_as_multiband)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def lowest_position(self, params):
        """Lowest Position

Determines on a cell-by-cell basis the position of the raster with the minimum value in a set of rasters.

        params: {"in_rasters_or_constantsin_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rasters_or_constantsin_raster_or_constant = params.get("in_rasters_or_constantsin_raster_or_constant")
        if in_rasters_or_constantsin_raster_or_constant is None:
            return {"success": False, "error": "in_rasters_or_constantsin_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_rasters_or_constantsin_raster_or_constant.replace(' ', '_')}_Lowest_Position"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Lowest Position
            arcpy.LowestPosition(in_rasters_or_constantsin_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def popularity(self, params):
        """Popularity

Determines the value in an argument list that is at a certain level of popularity on a cell-by-cell basis. The particular level of popularity (the number of occurrences of each value) is specified by the first argument.

        params: {"in_popularity_raster_or_constant": <Raster Layer; Constant>, "in_rastersin_raster": <Raster Layer>, "process_as_multiband": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_popularity_raster_or_constant = params.get("in_popularity_raster_or_constant")
        if in_popularity_raster_or_constant is None:
            return {"success": False, "error": "in_popularity_raster_or_constant parameter is required"}
        in_rastersin_raster = params.get("in_rastersin_raster")
        if in_rastersin_raster is None:
            return {"success": False, "error": "in_rastersin_raster parameter is required"}
        process_as_multiband = params.get("process_as_multiband")

            # Generate output name and path
            output_name = f"{in_popularity_raster_or_constant.replace(' ', '_')}_Popularity"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Popularity
            arcpy.Popularity(in_popularity_raster_or_constant, in_rastersin_raster, process_as_multiband)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def rank(self, params):
        """Rank

Ranks on a cell-by-cell basis the values from a set of input rasters and determines which values are returned based on the value of the rank input raster.

        params: {"in_rank_raster_or_constant": <Raster Layer; Constant>, "in_rastersin_raster": <Raster Layer>, "process_as_multiband": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rank_raster_or_constant = params.get("in_rank_raster_or_constant")
        if in_rank_raster_or_constant is None:
            return {"success": False, "error": "in_rank_raster_or_constant parameter is required"}
        in_rastersin_raster = params.get("in_rastersin_raster")
        if in_rastersin_raster is None:
            return {"success": False, "error": "in_rastersin_raster parameter is required"}
        process_as_multiband = params.get("process_as_multiband")

            # Generate output name and path
            output_name = f"{in_rank_raster_or_constant.replace(' ', '_')}_Rank"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Rank
            arcpy.Rank(in_rank_raster_or_constant, in_rastersin_raster, process_as_multiband)

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


    def bitwise_and(self, params):
        """Bitwise And

Performs a Bitwise And operation on the binary values of two input rasters. Learn more about how Bitwise Math tools work

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Bitwise_And"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Bitwise And
            arcpy.BitwiseAnd(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def bitwise_left_shift(self, params):
        """Bitwise Left Shift

Performs a Bitwise Left Shift operation on the binary values of two input rasters. Learn more about how Bitwise Math tools work

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Bitwise_Left_Shift"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Bitwise Left Shift
            arcpy.BitwiseLeftShift(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def bitwise_not(self, params):
        """Bitwise Not

Performs a Bitwise Not (complement) operation on the binary value of an input raster. Learn more about how Bitwise Math tools work

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Bitwise_Not"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Bitwise Not
            arcpy.BitwiseNot(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def bitwise_or(self, params):
        """Bitwise Or

Performs a Bitwise Or operation on the binary values of two input rasters. Learn more about how Bitwise Math tools work

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Bitwise_Or"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Bitwise Or
            arcpy.BitwiseOr(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def bitwise_right_shift(self, params):
        """Bitwise Right Shift

Performs a Bitwise Right Shift operation on the binary values of two input rasters. Learn more about how Bitwise Math tools work

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Bitwise_Right_Shift"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Bitwise Right Shift
            arcpy.BitwiseRightShift(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def bitwise_xor(self, params):
        """Bitwise XOr

Performs a Bitwise eXclusive Or operation on the binary values of two input rasters. Learn more about how Bitwise Math tools work

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Bitwise_XOr"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Bitwise XOr
            arcpy.BitwiseXOr(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def boolean_and(self, params):
        """Boolean And

Performs a Boolean And operation on the cell values of two input rasters. If both input values are true (non-zero), the output value is 1. If one or both inputs are false (zero), the output is 0. Learn more about how the Boolean math tools work

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Boolean_And"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Boolean And
            arcpy.BooleanAnd(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def boolean_not(self, params):
        """Boolean Not

Performs a Boolean Not (complement) operation on the cell values of the input raster. If the input values are true (non-zero), the output value is 0. If the input values are false (zero), the output is 1. Learn more about how the Boolean math tools work

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Boolean_Not"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Boolean Not
            arcpy.BooleanNot(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def boolean_or(self, params):
        """Boolean Or

Performs a Boolean Or operation on the cell values of two input rasters. If one or both input values are true (non-zero), the output value is 1. If both input values are false (zero), the output is 0. Learn more about how the Boolean math tools work

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Boolean_Or"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Boolean Or
            arcpy.BooleanOr(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def boolean_xor(self, params):
        """Boolean XOr

Performs a Boolean eXclusive Or operation on the cell values of two input rasters. If one input value is true (non-zero) and the other false (zero), the output is 1. If both input values are true or both are false, the output is 0. Learn more about how the Boolean math tools work

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Boolean_XOr"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Boolean XOr
            arcpy.BooleanXOr(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def combinatorial_and(self, params):
        """Combinatorial And

Performs a Combinatorial And operation on the cell values of two input rasters. If both input values are true (non-zero), the output is a different value for each unique combination of input values. If one or both inputs are false (zero), the output value is 0. Learn more about how Combinatorial tools work

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Combinatorial_And"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Combinatorial And
            arcpy.CombinatorialAnd(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def combinatorial_or(self, params):
        """Combinatorial Or

Performs a Combinatorial Or operation on the cell values of two input rasters. If either input value is true (non-zero), the output is a different value for each unique combination of input values. If both inputs are false (zero), the output value is 0. Learn more about how Combinatorial tools work

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Combinatorial_Or"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Combinatorial Or
            arcpy.CombinatorialOr(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def combinatorial_xor(self, params):
        """Combinatorial XOr

Performs a Combinatorial eXclusive Or operation on the cell values of two input rasters. If one input value is true (non-zero) and the other false (zero), the output is a different value for each unique combination of input values. If both inputs are true or both are false, the output value is 0. Learn more about how Combinatorial tools work

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Combinatorial_XOr"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Combinatorial XOr
            arcpy.CombinatorialXOr(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def equal_to(self, params):
        """Equal To

Performs a Relational equal-to operation on two inputs on a cell-by-cell basis. Returns 1 for cells where the first raster equals the second raster and 0 for cells where it does not. Learn more about how the Relational Math tools work

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Equal_To"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Equal To
            arcpy.EqualTo(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def greater_than(self, params):
        """Greater Than

Performs a Relational greater-than operation on two inputs on a cell-by-cell basis. Returns 1 for cells where the first raster is greater than the second raster and 0 for cells if it is not. Learn more about how the Relational Math tools work

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Greater_Than"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Greater Than
            arcpy.GreaterThan(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def greater_than_equal(self, params):
        """Greater Than Equal

Performs a Relational greater-than-or-equal-to operation on two inputs on a cell-by-cell basis. Returns 1 for cells where the first raster is greater than or equal to the second raster and 0 if it is not. Learn more about how the Relational Math tools work

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Greater_Than_Equal"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Greater Than Equal
            arcpy.GreaterThanEqual(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def less_than(self, params):
        """Less Than

Performs a Relational less-than operation on two inputs on a cell-by-cell basis. Returns 1 for cells where the first raster is less than the second raster and 0 if it is not. Learn more about how the Relational Math tools work

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Less_Than"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Less Than
            arcpy.LessThan(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def less_than_equal(self, params):
        """Less Than Equal

Performs a Relational less-than-or-equal-to operation on two inputs on a cell-by-cell basis. Returns 1 for cells where the first raster is less than or equal to the second raster and 0 where it is not. Learn more about how the Relational Math tools work

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Less_Than_Equal"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Less Than Equal
            arcpy.LessThanEqual(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def not_equal(self, params):
        """Not Equal

Performs a Relational not-equal-to operation on two inputs on a cell-by-cell basis. Returns 1 for cells where the first raster is not equal to the second raster and 0 for cells where it is equal. Learn more about how the Relational Math tools work

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Not_Equal"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Not Equal
            arcpy.NotEqual(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def diff(self, params):
        """Diff

Determines which values from the first input are logically different from the values of the second input on a cell-by-cell basis. If the values on the two inputs are different, the value on the first input is output. If the values on the two inputs are the same, the output is 0.

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Diff"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Diff
            arcpy.Diff(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def inlist(self, params):
        """InList

Determines which values from the first input are contained in a set of other inputs, on a cell-by-cell basis. For each cell, if the value of the first input raster is found in any of the list of other inputs, that value will be assigned to the output raster. If it is not found, the output cell will be NoData.

        params: {"in_raster_or_constant": <Raster Layer; Constant>, "in_raster_or_constantsin_raster_or_constant": <Raster Layer; Constant>, "process_as_multiband": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}
        in_raster_or_constantsin_raster_or_constant = params.get("in_raster_or_constantsin_raster_or_constant")
        if in_raster_or_constantsin_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constantsin_raster_or_constant parameter is required"}
        process_as_multiband = params.get("process_as_multiband")

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_InList"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute InList
            arcpy.InList(in_raster_or_constant, in_raster_or_constantsin_raster_or_constant, process_as_multiband)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def is_None(self, params):
        """Is Null

Determines which values from the input raster are NoData on a cell-by-cell basis. Returns a value of 1 if the input value is NoData and 0 for cells that are not.

        params: {"in_raster": <Raster Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Is_Null"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Is Null
            arcpy.IsNull(in_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def over(self, params):
        """Over

For the cell values in the first input that are not 0, the output value will be that of the first input. Where the cell values are 0, the output will be that of the second input raster.

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_Over"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Over
            arcpy.Over(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def test(self, params):
        """Test

Performs a Boolean evaluation of the input raster using a logical expression. When the expression evaluates to true, the output cell value is 1. If the expression is false, the output cell value is 0.

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
            output_name = f"{in_raster.replace(' ', '_')}_Test"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Test
            arcpy.Test(in_raster, where_clause)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def acos(self, params):
        """ACos

Calculates the inverse cosine of cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_ACos"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute ACos
            arcpy.ACos(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def acosh(self, params):
        """ACosH

Calculates the inverse hyperbolic cosine of cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_ACosH"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute ACosH
            arcpy.ACosH(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def asin(self, params):
        """ASin

Calculates the inverse sine of cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_ASin"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute ASin
            arcpy.ASin(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def asinh(self, params):
        """ASinH

Calculates the inverse hyperbolic sine of cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_ASinH"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute ASinH
            arcpy.ASinH(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def atan(self, params):
        """ATan

Calculates the inverse tangent of cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_ATan"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute ATan
            arcpy.ATan(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def atan2(self, params):
        """ATan2

Calculates the inverse tangent (based on x,y) of cells in a raster.

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
            output_name = f"{in_raster_or_constant1.replace(' ', '_')}_ATan2"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute ATan2
            arcpy.ATan2(in_raster_or_constant1, in_raster_or_constant2)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def atanh(self, params):
        """ATanH

Calculates the inverse hyperbolic tangent of cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_ATanH"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute ATanH
            arcpy.ATanH(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def cos(self, params):
        """Cos

Calculates the cosine of cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Cos"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Cos
            arcpy.Cos(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def cosh(self, params):
        """CosH

Calculates the hyperbolic cosine of cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_CosH"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute CosH
            arcpy.CosH(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def sin(self, params):
        """Sin

Calculates the sine of cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Sin"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Sin
            arcpy.Sin(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def sinh(self, params):
        """SinH

Calculates the hyperbolic sine of cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_SinH"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute SinH
            arcpy.SinH(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def tan(self, params):
        """Tan

Calculates the tangent of cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_Tan"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Tan
            arcpy.Tan(in_raster_or_constant)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def tanh(self, params):
        """TanH

Calculates the hyperbolic tangent of cells in a raster.

        params: {"in_raster_or_constant": <Raster Layer; Constant>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_or_constant = params.get("in_raster_or_constant")
        if in_raster_or_constant is None:
            return {"success": False, "error": "in_raster_or_constant parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster_or_constant.replace(' ', '_')}_TanH"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute TanH
            arcpy.TanH(in_raster_or_constant)

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


    def dimensional_moving_statistics(self, params):
        """Dimensional Moving Statistics

Calculates statistics over a moving window on multidimensional data along a specified dimension.

        params: {"in_raster": <Raster Layer>, "dimension": <String>, "backward_window": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        dimension = params.get("dimension")
        backward_window = params.get("backward_window")
        forward_window = params.get("forward_window")
        nodata_handling = params.get("nodata_handling")
        statistics_type = params.get("statistics_type")
        percentile_value = params.get("percentile_value")
        percentile_interpolation_type = params.get("percentile_interpolation_type")
        circular_wrap_value = params.get("circular_wrap_value")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Dimensional_Moving_Statistics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Dimensional Moving Statistics
            arcpy.DimensionalMovingStatistics(in_raster, dimension, backward_window, forward_window, nodata_handling, statistics_type, percentile_value, percentile_interpolation_type, circular_wrap_value)

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


    def band_collection_statistics(self, params):
        """Band Collection Statistics

Calculates the statistics for a set of raster bands. Learn more about how Band Collection Statistics works

        params: {"in_raster_bandsin_raster_band": <Raster Layer>, "out_stat_file": <File>, "compute_matrices": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_bandsin_raster_band = params.get("in_raster_bandsin_raster_band")
        if in_raster_bandsin_raster_band is None:
            return {"success": False, "error": "in_raster_bandsin_raster_band parameter is required"}
        out_stat_file = params.get("out_stat_file")
        if out_stat_file is None:
            return {"success": False, "error": "out_stat_file parameter is required"}
        compute_matrices = params.get("compute_matrices")

            # Generate output name and path
            output_name = f"{in_raster_bandsin_raster_band.replace(' ', '_')}_Band_Collection_Statistics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Band Collection Statistics
            arcpy.BandCollectionStatistics(in_raster_bandsin_raster_band, out_stat_file, compute_matrices)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def class_probability(self, params):
        """Class Probability

Creates a multiband raster of probability bands, with one band being created for each class represented in the input signature file. Learn more about how Class Probability works

        params: {"in_raster_bandsin_raster_band": <Raster Layer>, "in_signature_file": <File>, "maximum_output_value": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_bandsin_raster_band = params.get("in_raster_bandsin_raster_band")
        if in_raster_bandsin_raster_band is None:
            return {"success": False, "error": "in_raster_bandsin_raster_band parameter is required"}
        in_signature_file = params.get("in_signature_file")
        if in_signature_file is None:
            return {"success": False, "error": "in_signature_file parameter is required"}
        maximum_output_value = params.get("maximum_output_value")
        a_priori_probabilities = params.get("a_priori_probabilities")
        in_a_priori_file = params.get("in_a_priori_file")

            # Generate output name and path
            output_name = f"{in_raster_bandsin_raster_band.replace(' ', '_')}_Class_Probability"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Class Probability
            arcpy.ClassProbability(in_raster_bandsin_raster_band, in_signature_file, maximum_output_value, a_priori_probabilities, in_a_priori_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_signatures(self, params):
        """Create Signatures

Creates an ASCII signature file of classes defined by input sample data and a set of raster bands. Learn more about how Create Signatures works

        params: {"in_raster_bandsin_raster_band": <Raster Layer>, "in_sample_data": <Raster Layer; Feature Layer>, "out_signature_file": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_bandsin_raster_band = params.get("in_raster_bandsin_raster_band")
        if in_raster_bandsin_raster_band is None:
            return {"success": False, "error": "in_raster_bandsin_raster_band parameter is required"}
        in_sample_data = params.get("in_sample_data")
        if in_sample_data is None:
            return {"success": False, "error": "in_sample_data parameter is required"}
        out_signature_file = params.get("out_signature_file")
        if out_signature_file is None:
            return {"success": False, "error": "out_signature_file parameter is required"}
        compute_covariance = params.get("compute_covariance")
        sample_field = params.get("sample_field")

            # Generate output name and path
            output_name = f"{in_raster_bandsin_raster_band.replace(' ', '_')}_Create_Signatures"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Signatures
            arcpy.CreateSignatures(in_raster_bandsin_raster_band, in_sample_data, out_signature_file, compute_covariance, sample_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def dendrogram(self, params):
        """Dendrogram

Constructs a tree diagram (dendrogram) showing attribute distances between sequentially merged classes in a signature file. Learn more about how Dendrogram works

        params: {"in_signature_file": <File>, "out_dendrogram_file": <File>, "distance_calculation": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_signature_file = params.get("in_signature_file")
        if in_signature_file is None:
            return {"success": False, "error": "in_signature_file parameter is required"}
        out_dendrogram_file = params.get("out_dendrogram_file")
        if out_dendrogram_file is None:
            return {"success": False, "error": "out_dendrogram_file parameter is required"}
        distance_calculation = params.get("distance_calculation")
        line_width = params.get("line_width")

            # Generate output name and path
            output_name = f"{in_signature_file.replace(' ', '_')}_Dendrogram"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Dendrogram
            arcpy.Dendrogram(in_signature_file, out_dendrogram_file, distance_calculation, line_width)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def edit_signatures(self, params):
        """Edit Signatures

Edits and updates a signature file by merging, renumbering, and deleting class signatures. Learn more about how Edit Signatures works

        params: {"in_raster_bandsin_raster_band": <Raster Layer>, "in_signature_file": <File>, "in_signature_remap_file": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_bandsin_raster_band = params.get("in_raster_bandsin_raster_band")
        if in_raster_bandsin_raster_band is None:
            return {"success": False, "error": "in_raster_bandsin_raster_band parameter is required"}
        in_signature_file = params.get("in_signature_file")
        if in_signature_file is None:
            return {"success": False, "error": "in_signature_file parameter is required"}
        in_signature_remap_file = params.get("in_signature_remap_file")
        if in_signature_remap_file is None:
            return {"success": False, "error": "in_signature_remap_file parameter is required"}
        out_signature_file = params.get("out_signature_file")
        if out_signature_file is None:
            return {"success": False, "error": "out_signature_file parameter is required"}
        sample_interval = params.get("sample_interval")

            # Generate output name and path
            output_name = f"{in_raster_bandsin_raster_band.replace(' ', '_')}_Edit_Signatures"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Edit Signatures
            arcpy.EditSignatures(in_raster_bandsin_raster_band, in_signature_file, in_signature_remap_file, out_signature_file, sample_interval)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def iso_cluster(self, params):
        """Iso Cluster

Uses an isodata clustering algorithm to determine the characteristics of the natural groupings of cells in multidimensional attribute space and stores the results in an output ASCII signature file. Learn more about how Iso Cluster works

        params: {"in_raster_bandsin_raster_band": <Raster Layer>, "out_signature_file": <File>, "number_classes": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_bandsin_raster_band = params.get("in_raster_bandsin_raster_band")
        if in_raster_bandsin_raster_band is None:
            return {"success": False, "error": "in_raster_bandsin_raster_band parameter is required"}
        out_signature_file = params.get("out_signature_file")
        if out_signature_file is None:
            return {"success": False, "error": "out_signature_file parameter is required"}
        number_classes = params.get("number_classes")
        if number_classes is None:
            return {"success": False, "error": "number_classes parameter is required"}
        number_iterations = params.get("number_iterations")
        min_class_size = params.get("min_class_size")
        sample_interval = params.get("sample_interval")

            # Generate output name and path
            output_name = f"{in_raster_bandsin_raster_band.replace(' ', '_')}_Iso_Cluster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Iso Cluster
            arcpy.IsoCluster(in_raster_bandsin_raster_band, out_signature_file, number_classes, number_iterations, min_class_size, sample_interval)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def iso_cluster_unsupervised_classification(self, params):
        """Iso Cluster Unsupervised Classification

Performs unsupervised classification on a series of input raster bands using the Iso Cluster and Maximum Likelihood Classification tools.

        params: {"input_raster_bandsin_raster_band": <Raster Layer; Mosaic Layer>, "number_of_classes": <Long>, "minimum_class_size": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_raster_bandsin_raster_band = params.get("input_raster_bandsin_raster_band")
        if input_raster_bandsin_raster_band is None:
            return {"success": False, "error": "input_raster_bandsin_raster_band parameter is required"}
        number_of_classes = params.get("number_of_classes")
        if number_of_classes is None:
            return {"success": False, "error": "number_of_classes parameter is required"}
        minimum_class_size = params.get("minimum_class_size")
        sample_interval = params.get("sample_interval")
        output_signature_fileout_signature_file = params.get("output_signature_fileout_signature_file")

            # Generate output name and path
            output_name = f"{input_raster_bandsin_raster_band.replace(' ', '_')}_Iso_Cluster_Unsupervised_Classification"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Iso Cluster Unsupervised Classification
            arcpy.IsoClusterUnsupervisedClassification(input_raster_bandsin_raster_band, number_of_classes, minimum_class_size, sample_interval, output_signature_fileout_signature_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def maximum_likelihood_classification(self, params):
        """Maximum Likelihood Classification

Performs a maximum likelihood classification on a set of raster bands and creates a classified raster as output. Learn more about how Maximum Likelihood Classification works

        params: {"in_raster_bandsin_raster_band": <Raster Layer>, "in_signature_file": <File>, "reject_fraction": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_bandsin_raster_band = params.get("in_raster_bandsin_raster_band")
        if in_raster_bandsin_raster_band is None:
            return {"success": False, "error": "in_raster_bandsin_raster_band parameter is required"}
        in_signature_file = params.get("in_signature_file")
        if in_signature_file is None:
            return {"success": False, "error": "in_signature_file parameter is required"}
        reject_fraction = params.get("reject_fraction")
        a_priori_probabilities = params.get("a_priori_probabilities")
        in_a_priori_file = params.get("in_a_priori_file")
        out_confidence_raster = params.get("out_confidence_raster")

            # Generate output name and path
            output_name = f"{in_raster_bandsin_raster_band.replace(' ', '_')}_Maximum_Likelihood_Classification"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Maximum Likelihood Classification
            arcpy.MaximumLikelihoodClassification(in_raster_bandsin_raster_band, in_signature_file, reject_fraction, a_priori_probabilities, in_a_priori_file, out_confidence_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def principal_components(self, params):
        """Principal Components

Performs Principal Component Analysis (PCA) on a set of raster bands and generates a single multiband raster as output. Learn more about how Principal Components works

        params: {"in_raster_bandsin_raster_band": <Raster Layer>, "number_components": <Long>, "out_data_file": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster_bandsin_raster_band = params.get("in_raster_bandsin_raster_band")
        if in_raster_bandsin_raster_band is None:
            return {"success": False, "error": "in_raster_bandsin_raster_band parameter is required"}
        number_components = params.get("number_components")
        out_data_file = params.get("out_data_file")

            # Generate output name and path
            output_name = f"{in_raster_bandsin_raster_band.replace(' ', '_')}_Principal_Components"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Principal Components
            arcpy.PrincipalComponents(in_raster_bandsin_raster_band, number_components, out_data_file)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def block_statistics(self, params):
        """Block Statistics

Partitions the input into non-overlapping blocks and calculates the statistic of the values within each block. The value is assigned to all of the cells in each block in the output. Learn more about how Block Statistics works

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

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Block_Statistics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Block Statistics
            arcpy.BlockStatistics(in_raster, neighborhood, statistics_type, ignore_nodata)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def filter(self, params):
        """Filter

Performs either a smoothing (Low pass) or edge-enhancing (High pass) filter on a raster. Learn more about how Filter works

        params: {"in_raster": <Raster Layer>, "filter_type": <String>, "ignore_nodata": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        filter_type = params.get("filter_type")
        ignore_nodata = params.get("ignore_nodata")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Filter"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Filter
            arcpy.Filter(in_raster, filter_type, ignore_nodata)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def focal_flow(self, params):
        """Focal Flow

Determines the flow of the values in the input raster within each cell's immediate neighborhood. Learn more about how Focal Flow works

        params: {"in_surface_raster": <Raster Layer>, "threshold_value": <Double>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_surface_raster = params.get("in_surface_raster")
        if in_surface_raster is None:
            return {"success": False, "error": "in_surface_raster parameter is required"}
        threshold_value = params.get("threshold_value")

            # Generate output name and path
            output_name = f"{in_surface_raster.replace(' ', '_')}_Focal_Flow"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Focal Flow
            arcpy.FocalFlow(in_surface_raster, threshold_value)

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


    def line_statistics(self, params):
        """Line Statistics

Calculates a statistic on the attributes of lines in a circular neighborhood around each output cell. Learn more about how Line Statistics works

        params: {"in_polyline_features": <Feature Layer>, "field": <Field>, "cell_size": <Analysis Cell Size>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_polyline_features = params.get("in_polyline_features")
        if in_polyline_features is None:
            return {"success": False, "error": "in_polyline_features parameter is required"}
        field = params.get("field")
        if field is None:
            return {"success": False, "error": "field parameter is required"}
        cell_size = params.get("cell_size")
        search_radius = params.get("search_radius")
        statistics_type = params.get("statistics_type")

            # Generate output name and path
            output_name = f"{in_polyline_features.replace(' ', '_')}_Line_Statistics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Line Statistics
            arcpy.LineStatistics(in_polyline_features, field, cell_size, search_radius, statistics_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def point_statistics(self, params):
        """Point Statistics

Calculates a statistic on the points in a neighborhood around each output cell. Learn more about how Point Statistics works

        params: {"in_point_features": <Feature Layer>, "field": <Field>, "cell_size": <Analysis Cell Size>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_point_features = params.get("in_point_features")
        if in_point_features is None:
            return {"success": False, "error": "in_point_features parameter is required"}
        field = params.get("field")
        if field is None:
            return {"success": False, "error": "field parameter is required"}
        cell_size = params.get("cell_size")
        neighborhood = params.get("neighborhood")
        statistics_type = params.get("statistics_type")

            # Generate output name and path
            output_name = f"{in_point_features.replace(' ', '_')}_Point_Statistics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Point Statistics
            arcpy.PointStatistics(in_point_features, field, cell_size, neighborhood, statistics_type)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def fuzzy_membership(self, params):
        """Fuzzy Membership

Transforms  the input raster   into a 0 to 1 scale, indicating the strength of a membership in a set, based on a specified fuzzification algorithm. A value of 1 indicates full membership in the fuzzy set, with membership decreasing to 0, indicating it is not a member of the fuzzy set. Learn more about how Fuzzy Membership works

        params: {"in_raster": <Raster Layer>, "fuzzy_function": <Fuzzy function>, "hedge": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        fuzzy_function = params.get("fuzzy_function")
        hedge = params.get("hedge")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Fuzzy_Membership"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Fuzzy Membership
            arcpy.FuzzyMembership(in_raster, fuzzy_function, hedge)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def fuzzy_overlay(self, params):
        """Fuzzy Overlay

Combine fuzzy membership rasters data together, based on selected overlay type. Learn more about how Fuzzy Overlay works

        params: {"in_rastersin_raster": <Raster Layer>, "overlay_type": <String>, "gamma": <Double>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_rastersin_raster = params.get("in_rastersin_raster")
        if in_rastersin_raster is None:
            return {"success": False, "error": "in_rastersin_raster parameter is required"}
        overlay_type = params.get("overlay_type")
        gamma = params.get("gamma")

            # Generate output name and path
            output_name = f"{in_rastersin_raster.replace(' ', '_')}_Fuzzy_Overlay"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Fuzzy Overlay
            arcpy.FuzzyOverlay(in_rastersin_raster, overlay_type, gamma)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def locate_regions(self, params):
        """Locate Regions

Identifies the best regions, or groups of contiguous cells, from an input utility (suitability) raster that satisfy a specified evaluation criterion and that meet identified shape, size, number, and interregion distance constraints. This tool uses a parameterized region-growing (PRG) algorithm to grow candidate regions from seed cells by adding neighboring cells to the region that best preserves the specified shape but also maximizes utility for the region. Using a selection algorithm and an evaluation criterion—such as the highest average value—the best region or regions are selected from the candidate regions that meet identified size and spatial constraints. An example of a spatial constraint would be maintaining a certain minimum distance between regions. Learn more about how the Locate Regions tool works

        params: {"in_raster": <Raster Layer>, "total_area": <Double>, "area_units": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        total_area = params.get("total_area")
        area_units = params.get("area_units")
        number_of_regions = params.get("number_of_regions")
        region_shape = params.get("region_shape")
        region_orientation = params.get("region_orientation")
        shape_tradeoff = params.get("shape_tradeoff")
        evaluation_method = params.get("evaluation_method")
        minimum_area = params.get("minimum_area")
        maximum_area = params.get("maximum_area")
        minimum_distance = params.get("minimum_distance")
        maximum_distance = params.get("maximum_distance")
        distance_units = params.get("distance_units")
        in_existing_regions = params.get("in_existing_regions")
        number_of_neighbors = params.get("number_of_neighbors")
        no_islands = params.get("no_islands")
        region_seeds = params.get("region_seeds")
        region_resolution = params.get("region_resolution")
        selection_method = params.get("selection_method")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Locate_Regions"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Locate Regions
            arcpy.LocateRegions(in_raster, total_area, area_units, number_of_regions, region_shape, region_orientation, shape_tradeoff, evaluation_method, minimum_area, maximum_area, minimum_distance, maximum_distance, distance_units, in_existing_regions, number_of_neighbors, no_islands, region_seeds, region_resolution, selection_method)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def weighted_overlay(self, params):
        """Weighted Overlay

Overlays several rasters using a common measurement scale and weights each according to its importance. Learn more about how Weighted Overlay works

        params: {"in_weighted_overlay_table": <WOTable>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_weighted_overlay_table = params.get("in_weighted_overlay_table")
        if in_weighted_overlay_table is None:
            return {"success": False, "error": "in_weighted_overlay_table parameter is required"}

            # Generate output name and path
            output_name = f"{in_weighted_overlay_table.replace(' ', '_')}_Weighted_Overlay"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Weighted Overlay
            arcpy.WeightedOverlay(in_weighted_overlay_table)

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


    def create_constant_raster(self, params):
        """Create Constant Raster

Creates a raster of a constant value within the extent and cell size of the analysis window.

        params: {"constant_value": <Double>, "data_type": <String>, "cell_size": <Analysis Cell Size>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        constant_value = params.get("constant_value")
        if constant_value is None:
            return {"success": False, "error": "constant_value parameter is required"}
        data_type = params.get("data_type")
        cell_size = params.get("cell_size")
        extent = params.get("extent")

            # Generate output name and path
            output_name = f"{constant_value.replace(' ', '_')}_Create_Constant_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Constant Raster
            arcpy.CreateConstantRaster(constant_value, data_type, cell_size, extent)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_normal_raster(self, params):
        """Create Normal Raster

Creates a raster of random values with a normal (Gaussian) distribution within the extent and cell size of the analysis window.

        params: {"cell_size": <Analysis Cell Size>, "extent": <Envelope; Extent>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        cell_size = params.get("cell_size")
        extent = params.get("extent")

            # Generate output name and path
            output_name = f"{params.replace(' ', '_')}_Create_Normal_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Normal Raster
            arcpy.CreateNormalRaster(cell_size, extent)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_random_raster(self, params):
        """Create Random Raster

Creates a raster of random floating-point values between 0.0 and 1.0 within the extent and cell size of the analysis window. The Create Random Raster tool in the Data Management toolbox provides enhanced functionality or performance.

        params: {"seed_value": <Double>, "cell_size": <Analysis Cell Size>, "extent": <Envelope; Extent>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        seed_value = params.get("seed_value")
        cell_size = params.get("cell_size")
        extent = params.get("extent")

            # Generate output name and path
            output_name = f"{params.replace(' ', '_')}_Create_Random_Raster"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Random Raster
            arcpy.CreateRandomRaster(seed_value, cell_size, extent)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def lookup(self, params):
        """Lookup

Creates a raster by looking up values in another field in the table of the input raster.

        params: {"in_raster": <Raster Layer>, "lookup_field": <Field>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        lookup_field = params.get("lookup_field")
        if lookup_field is None:
            return {"success": False, "error": "lookup_field parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Lookup"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Lookup
            arcpy.Lookup(in_raster, lookup_field)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def reclass_by_ascii_file(self, params):
        """Reclass by ASCII File

Reclassifies (or changes) the values of the input cells of a raster using an ASCII remap file. Learn more about how Reclass by ASCII File works

        params: {"in_raster": <Raster Layer>, "in_remap_file": <File>, "missing_values": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_remap_file = params.get("in_remap_file")
        if in_remap_file is None:
            return {"success": False, "error": "in_remap_file parameter is required"}
        missing_values = params.get("missing_values")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Reclass_by_ASCII_File"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Reclass by ASCII File
            arcpy.ReclassbyASCIIFile(in_raster, in_remap_file, missing_values)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def reclass_by_table(self, params):
        """Reclass by Table

Reclassifies (or changes) the values of the input cells of a raster using a remap table.

        params: {"in_raster": <Raster Layer>, "in_remap_table": <Table View>, "from_value_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_remap_table = params.get("in_remap_table")
        if in_remap_table is None:
            return {"success": False, "error": "in_remap_table parameter is required"}
        from_value_field = params.get("from_value_field")
        if from_value_field is None:
            return {"success": False, "error": "from_value_field parameter is required"}
        to_value_field = params.get("to_value_field")
        if to_value_field is None:
            return {"success": False, "error": "to_value_field parameter is required"}
        output_value_field = params.get("output_value_field")
        if output_value_field is None:
            return {"success": False, "error": "output_value_field parameter is required"}
        missing_values = params.get("missing_values")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Reclass_by_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Reclass by Table
            arcpy.ReclassbyTable(in_raster, in_remap_table, from_value_field, to_value_field, output_value_field, missing_values)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def reclassify(self, params):
        """Reclassify

Reclassifies (or changes) the values in a raster.

        params: {"in_raster": <Raster Layer>, "reclass_field": <Field>, "remap": <Remap>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        reclass_field = params.get("reclass_field")
        if reclass_field is None:
            return {"success": False, "error": "reclass_field parameter is required"}
        remap = params.get("remap")
        if remap is None:
            return {"success": False, "error": "remap parameter is required"}
        missing_values = params.get("missing_values")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Reclassify"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Reclassify
            arcpy.Reclassify(in_raster, reclass_field, remap, missing_values)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def rescale_by_function(self, params):
        """Rescale by Function

Rescales the input raster values by applying a selected transformation function and transforming the resulting values onto a specified continuous evaluation scale. Learn more about how Rescale by Function works

        params: {"in_raster": <Raster Layer>, "transformation_function": <Transformation function>, "from_scale": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        transformation_function = params.get("transformation_function")
        from_scale = params.get("from_scale")
        to_scale = params.get("to_scale")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Rescale_by_Function"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Rescale by Function
            arcpy.RescalebyFunction(in_raster, transformation_function, from_scale, to_scale)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def slice(self, params):
        """Slice

Slices or reclassifies the range of values of the input cells into zones (classes). The available data classification methods are equal interval, equal area (quantile), natural breaks, standard deviation (mean-centered), standard deviation (mean as a break), defined interval, and geometric interval.

        params: {"in_raster": <Raster Layer>, "number_zones": <Long>, "slice_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        number_zones = params.get("number_zones")
        slice_type = params.get("slice_type")
        base_output_zone = params.get("base_output_zone")
        nodata_to_value = params.get("nodata_to_value")
        class_interval_size = params.get("class_interval_size")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Slice"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Slice
            arcpy.Slice(in_raster, number_zones, slice_type, base_output_zone, nodata_to_value, class_interval_size)

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


    def area_solar_radiation(self, params):
        """Area Solar Radiation

Derives incoming solar radiation from a raster surface. This tool is deprecated and will be removed in a future release. The Raster Solar Radiation tool provides enhanced functionality or performance.

        params: {"in_surface_raster": <Raster Layer>, "latitude": <Double>, "sky_size": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_surface_raster = params.get("in_surface_raster")
        if in_surface_raster is None:
            return {"success": False, "error": "in_surface_raster parameter is required"}
        latitude = params.get("latitude")
        sky_size = params.get("sky_size")
        time_configuration = params.get("time_configuration")
        day_interval = params.get("day_interval")
        hour_interval = params.get("hour_interval")
        each_interval = params.get("each_interval")
        z_factor = params.get("z_factor")
        slope_aspect_input_type = params.get("slope_aspect_input_type")
        calculation_directions = params.get("calculation_directions")
        zenith_divisions = params.get("zenith_divisions")
        azimuth_divisions = params.get("azimuth_divisions")
        diffuse_model_type = params.get("diffuse_model_type")
        diffuse_proportion = params.get("diffuse_proportion")
        transmittivity = params.get("transmittivity")
        out_direct_radiation_raster = params.get("out_direct_radiation_raster")
        out_diffuse_radiation_raster = params.get("out_diffuse_radiation_raster")
        out_direct_duration_raster = params.get("out_direct_duration_raster")

            # Generate output name and path
            output_name = f"{in_surface_raster.replace(' ', '_')}_Area_Solar_Radiation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Area Solar Radiation
            arcpy.AreaSolarRadiation(in_surface_raster, latitude, sky_size, time_configuration, day_interval, hour_interval, each_interval, z_factor, slope_aspect_input_type, calculation_directions, zenith_divisions, azimuth_divisions, diffuse_model_type, diffuse_proportion, transmittivity, out_direct_radiation_raster, out_diffuse_radiation_raster, out_direct_duration_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def feature_solar_radiation(self, params):
        """Feature Solar Radiation

Calculates the incoming solar insolation for input points or polygon features relative to the surface (ground) on Earth or the Moon. The input features can represent locations or engineered surfaces by specifying attributes to define size, height, and orientation for analysis relative to the ground. Solar insolation is calculated as the amount of solar radiation energy received during an amount of time for each feature. Values are represented as totals and averages for the area of the feature and have units, kilowatt hours (kWh) and kilowatt hours per square meter (kWh/m2), respectively. Learn more about how Feature Solar Radiation works

        params: {"in_surface_raster": <Raster Layer>, "in_features": <Feature Layer>, "unique_id_field": <Field>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_surface_raster = params.get("in_surface_raster")
        if in_surface_raster is None:
            return {"success": False, "error": "in_surface_raster parameter is required"}
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        unique_id_field = params.get("unique_id_field")
        if unique_id_field is None:
            return {"success": False, "error": "unique_id_field parameter is required"}
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}
        start_date_time = params.get("start_date_time")
        if start_date_time is None:
            return {"success": False, "error": "start_date_time parameter is required"}
        end_date_time = params.get("end_date_time")
        if end_date_time is None:
            return {"success": False, "error": "end_date_time parameter is required"}
        time_zone = params.get("time_zone")
        adjust_dst = params.get("adjust_dst")
        use_time_interval = params.get("use_time_interval")
        interval_unit = params.get("interval_unit")
        interval = params.get("interval")
        feature_offset = params.get("feature_offset")
        feature_area = params.get("feature_area")
        feature_slope = params.get("feature_slope")
        feature_aspect = params.get("feature_aspect")
        neighborhood_distance = params.get("neighborhood_distance")
        use_adaptive_neighborhood = params.get("use_adaptive_neighborhood")
        diffuse_model_type = params.get("diffuse_model_type")
        diffuse_proportion = params.get("diffuse_proportion")
        transmittivity = params.get("transmittivity")
        analysis_target_device = params.get("analysis_target_device")
        out_join_layer = params.get("out_join_layer")
        sunmap_grid_level = params.get("sunmap_grid_level")

            # Generate output name and path
            output_name = f"{in_surface_raster.replace(' ', '_')}_Feature_Solar_Radiation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Feature Solar Radiation
            arcpy.FeatureSolarRadiation(in_surface_raster, in_features, unique_id_field, out_table, start_date_time, end_date_time, time_zone, adjust_dst, use_time_interval, interval_unit, interval, feature_offset, feature_area, feature_slope, feature_aspect, neighborhood_distance, use_adaptive_neighborhood, diffuse_model_type, diffuse_proportion, transmittivity, analysis_target_device, out_join_layer, sunmap_grid_level)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def points_solar_radiation(self, params):
        """Points Solar Radiation

Derives incoming solar radiation for specific locations in a point feature class or location table. This tool is deprecated and will be removed in a future release. The Feature Solar Radiation tool provides enhanced functionality or performance.

        params: {"in_surface_raster": <Raster Layer>, "in_points_feature_or_table": <Feature Layer; Table View>, "out_global_radiation_features": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_surface_raster = params.get("in_surface_raster")
        if in_surface_raster is None:
            return {"success": False, "error": "in_surface_raster parameter is required"}
        in_points_feature_or_table = params.get("in_points_feature_or_table")
        if in_points_feature_or_table is None:
            return {"success": False, "error": "in_points_feature_or_table parameter is required"}
        out_global_radiation_features = params.get("out_global_radiation_features")
        if out_global_radiation_features is None:
            return {"success": False, "error": "out_global_radiation_features parameter is required"}
        height_offset = params.get("height_offset")
        latitude = params.get("latitude")
        sky_size = params.get("sky_size")
        time_configuration = params.get("time_configuration")
        day_interval = params.get("day_interval")
        hour_interval = params.get("hour_interval")
        each_interval = params.get("each_interval")
        z_factor = params.get("z_factor")
        slope_aspect_input_type = params.get("slope_aspect_input_type")
        calculation_directions = params.get("calculation_directions")
        zenith_divisions = params.get("zenith_divisions")
        azimuth_divisions = params.get("azimuth_divisions")
        diffuse_model_type = params.get("diffuse_model_type")
        diffuse_proportion = params.get("diffuse_proportion")
        transmittivity = params.get("transmittivity")
        out_direct_radiation_features = params.get("out_direct_radiation_features")
        out_diffuse_radiation_features = params.get("out_diffuse_radiation_features")
        out_direct_duration_features = params.get("out_direct_duration_features")

            # Generate output name and path
            output_name = f"{in_surface_raster.replace(' ', '_')}_Points_Solar_Radiation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Points Solar Radiation
            arcpy.PointsSolarRadiation(in_surface_raster, in_points_feature_or_table, out_global_radiation_features, height_offset, latitude, sky_size, time_configuration, day_interval, hour_interval, each_interval, z_factor, slope_aspect_input_type, calculation_directions, zenith_divisions, azimuth_divisions, diffuse_model_type, diffuse_proportion, transmittivity, out_direct_radiation_features, out_diffuse_radiation_features, out_direct_duration_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def raster_solar_radiation(self, params):
        """Raster Solar Radiation

Calculates the incoming solar insolation for every raster cell of a digital surface model for Earth or the Moon. Solar insolation is calculated as the amount of solar radiation energy received per unit area during an amount of time and is measured in units, kilowatt hours per square meter (kWh/m2). Learn more about how Raster Solar Radiation works

        params: {"in_surface_raster": <Raster Layer>, "start_date_time": <Date>, "end_date_time": <Date>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_surface_raster = params.get("in_surface_raster")
        if in_surface_raster is None:
            return {"success": False, "error": "in_surface_raster parameter is required"}
        start_date_time = params.get("start_date_time")
        if start_date_time is None:
            return {"success": False, "error": "start_date_time parameter is required"}
        end_date_time = params.get("end_date_time")
        if end_date_time is None:
            return {"success": False, "error": "end_date_time parameter is required"}
        in_analysis_mask = params.get("in_analysis_mask")
        in_slope_raster = params.get("in_slope_raster")
        in_aspect_raster = params.get("in_aspect_raster")
        out_direct_radiation_raster = params.get("out_direct_radiation_raster")
        out_diffuse_radiation_raster = params.get("out_diffuse_radiation_raster")
        out_duration_raster = params.get("out_duration_raster")
        time_zone = params.get("time_zone")
        adjust_dst = params.get("adjust_dst")
        use_time_interval = params.get("use_time_interval")
        interval_unit = params.get("interval_unit")
        interval = params.get("interval")
        neighborhood_distance = params.get("neighborhood_distance")
        use_adaptive_neighborhood = params.get("use_adaptive_neighborhood")
        diffuse_model_type = params.get("diffuse_model_type")
        diffuse_proportion = params.get("diffuse_proportion")
        transmittivity = params.get("transmittivity")
        analysis_target_device = params.get("analysis_target_device")
        sunmap_grid_level = params.get("sunmap_grid_level")

            # Generate output name and path
            output_name = f"{in_surface_raster.replace(' ', '_')}_Raster_Solar_Radiation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Raster Solar Radiation
            arcpy.RasterSolarRadiation(in_surface_raster, start_date_time, end_date_time, in_analysis_mask, in_slope_raster, in_aspect_raster, out_direct_radiation_raster, out_diffuse_radiation_raster, out_duration_raster, time_zone, adjust_dst, use_time_interval, interval_unit, interval, neighborhood_distance, use_adaptive_neighborhood, diffuse_model_type, diffuse_proportion, transmittivity, analysis_target_device, sunmap_grid_level)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def solar_radiation_graphics(self, params):
        """Solar Radiation Graphics

Derives raster representations of a hemispherical viewshed, sun map, and sky map, which are used in the calculation of direct, diffuse, and global solar radiation. This tool is deprecated and will be removed in a future release. The Raster Solar Radiation tool provides enhanced functionality or performance.

        params: {"in_surface_raster": <Raster Layer>, "in_points_feature_or_table": <Feature Layer; Table View>, "sky_size": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_surface_raster = params.get("in_surface_raster")
        if in_surface_raster is None:
            return {"success": False, "error": "in_surface_raster parameter is required"}
        in_points_feature_or_table = params.get("in_points_feature_or_table")
        sky_size = params.get("sky_size")
        height_offset = params.get("height_offset")
        calculation_directions = params.get("calculation_directions")
        latitude = params.get("latitude")
        time_configuration = params.get("time_configuration")
        day_interval = params.get("day_interval")
        hour_interval = params.get("hour_interval")
        out_sunmap_raster = params.get("out_sunmap_raster")
        zenith_divisions = params.get("zenith_divisions")
        azimuth_divisions = params.get("azimuth_divisions")
        out_skymap_raster = params.get("out_skymap_raster")

            # Generate output name and path
            output_name = f"{in_surface_raster.replace(' ', '_')}_Solar_Radiation_Graphics"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Solar Radiation Graphics
            arcpy.SolarRadiationGraphics(in_surface_raster, in_points_feature_or_table, sky_size, height_offset, calculation_directions, latitude, time_configuration, day_interval, hour_interval, out_sunmap_raster, zenith_divisions, azimuth_divisions, out_skymap_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_surface_information(self, params):
        """Add Surface Information

Attributes input features with height-based statistical information derived from the overlapping portions of a surface.

        params: {"in_feature_class": <Feature Layer>, "in_surface": <LAS Dataset Layer; Mosaic Layer; Raster Layer; Terrain Layer; TIN Layer>, "out_property": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_feature_class = params.get("in_feature_class")
        if in_feature_class is None:
            return {"success": False, "error": "in_feature_class parameter is required"}
        in_surface = params.get("in_surface")
        if in_surface is None:
            return {"success": False, "error": "in_surface parameter is required"}
        out_property = params.get("out_property")
        if out_property is None:
            return {"success": False, "error": "out_property parameter is required"}
        method = params.get("method")
        sample_distance = params.get("sample_distance")
        z_factor = params.get("z_factor")
        pyramid_level_resolution = params.get("pyramid_level_resolution")
        noise_filtering = params.get("noise_filtering")

            # Generate output name and path
            output_name = f"{in_feature_class.replace(' ', '_')}_Add_Surface_Information"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Surface Information
            arcpy.AddSurfaceInformation(in_feature_class, in_surface, out_property, method, sample_distance, z_factor, pyramid_level_resolution, noise_filtering)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def aspect(self, params):
        """Aspect

Derives the aspect from each cell of a raster surface. The aspect identifies the compass direction that the downhill slope faces for each location. The Surface Parameters tool provides a newer implementation and enhanced functionality. Learn more about how Aspect works

        params: {"in_raster": <Raster Layer>, "method": <String>, "z_unit": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        method = params.get("method")
        z_unit = params.get("z_unit")
        project_geodesic_azimuths = params.get("project_geodesic_azimuths")
        analysis_target_device = params.get("analysis_target_device")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Aspect"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Aspect
            arcpy.Aspect(in_raster, method, z_unit, project_geodesic_azimuths, analysis_target_device)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def contour(self, params):
        """Contour

Creates a feature class of contours from a raster surface. Learn more about how Contouring works

        params: {"in_raster": <Raster Layer>, "out_polyline_features": <Feature Class>, "contour_interval": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_polyline_features = params.get("out_polyline_features")
        if out_polyline_features is None:
            return {"success": False, "error": "out_polyline_features parameter is required"}
        contour_interval = params.get("contour_interval")
        if contour_interval is None:
            return {"success": False, "error": "contour_interval parameter is required"}
        base_contour = params.get("base_contour")
        z_factor = params.get("z_factor")
        contour_type = params.get("contour_type")
        max_vertices_per_feature = params.get("max_vertices_per_feature")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Contour"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Contour
            arcpy.Contour(in_raster, out_polyline_features, contour_interval, base_contour, z_factor, contour_type, max_vertices_per_feature)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def contour_list(self, params):
        """Contour List

Creates a feature class of selected contour values from a raster surface. Learn more about how Contouring works

        params: {"in_raster": <Raster Layer>, "out_polyline_features": <Feature Class>, "contour_valuescontour_value": <Double>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_polyline_features = params.get("out_polyline_features")
        if out_polyline_features is None:
            return {"success": False, "error": "out_polyline_features parameter is required"}
        contour_valuescontour_value = params.get("contour_valuescontour_value")
        if contour_valuescontour_value is None:
            return {"success": False, "error": "contour_valuescontour_value parameter is required"}

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Contour_List"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Contour List
            arcpy.ContourList(in_raster, out_polyline_features, contour_valuescontour_value)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def contour_with_barriers(self, params):
        """Contour with Barriers

Creates contours from a raster surface. The inclusion of barrier features allows you to independently generate contours on either side of a barrier.

        params: {"in_raster": <Raster Layer; Raster Dataset; Mosaic Layer; Mosaic Dataset>, "out_contour_feature_class": <Feature Class>, "in_barrier_features": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_contour_feature_class = params.get("out_contour_feature_class")
        if out_contour_feature_class is None:
            return {"success": False, "error": "out_contour_feature_class parameter is required"}
        in_barrier_features = params.get("in_barrier_features")
        in_contour_type = params.get("in_contour_type")
        in_contour_values_file = params.get("in_contour_values_file")
        explicit_only = params.get("explicit_only")
        in_base_contour = params.get("in_base_contour")
        in_contour_interval = params.get("in_contour_interval")
        in_indexed_contour_interval = params.get("in_indexed_contour_interval")
        in_contour_listin_explicit_contour = params.get("in_contour_listin_explicit_contour")
        in_z_factor = params.get("in_z_factor")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Contour_with_Barriers"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Contour with Barriers
            arcpy.ContourwithBarriers(in_raster, out_contour_feature_class, in_barrier_features, in_contour_type, in_contour_values_file, explicit_only, in_base_contour, in_contour_interval, in_indexed_contour_interval, in_contour_listin_explicit_contour, in_z_factor)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def curvature(self, params):
        """Curvature

Calculates the curvature of a raster surface and, optionally, includes profile and plan curvature. The Surface Parameters tool provides a newer implementation and enhanced functionality. Learn more about how Curvature works

        params: {"in_raster": <Raster Layer>, "z_factor": <Double>, "out_profile_curve_raster": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        z_factor = params.get("z_factor")
        out_profile_curve_raster = params.get("out_profile_curve_raster")
        out_plan_curve_raster = params.get("out_plan_curve_raster")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Curvature"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Curvature
            arcpy.Curvature(in_raster, z_factor, out_profile_curve_raster, out_plan_curve_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def cut_fill(self, params):
        """Cut Fill

Calculates the volume change between two surfaces. This is typically used for cut and fill operations. Learn more about how Cut Fill works

        params: {"in_before_surface": <Raster Layer>, "in_after_surface": <Raster Layer>, "z_factor": <Double>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_before_surface = params.get("in_before_surface")
        if in_before_surface is None:
            return {"success": False, "error": "in_before_surface parameter is required"}
        in_after_surface = params.get("in_after_surface")
        if in_after_surface is None:
            return {"success": False, "error": "in_after_surface parameter is required"}
        z_factor = params.get("z_factor")

            # Generate output name and path
            output_name = f"{in_before_surface.replace(' ', '_')}_Cut_Fill"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Cut Fill
            arcpy.CutFill(in_before_surface, in_after_surface, z_factor)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def feature_preserving_smoothing(self, params):
        """Feature Preserving Smoothing

Smooths a surface raster by removing noise while preserving features. Learn more about how Feature Preserving Smoothing works

        params: {"in_raster": <Raster Layer>, "distance_units": <String>, "neighborhood_distance": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        distance_units = params.get("distance_units")
        neighborhood_distance = params.get("neighborhood_distance")
        normal_difference_threshold = params.get("normal_difference_threshold")
        number_iterations = params.get("number_iterations")
        maximum_elevation_change = params.get("maximum_elevation_change")
        z_unit = params.get("z_unit")
        analysis_target_device = params.get("analysis_target_device")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Feature_Preserving_Smoothing"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Feature Preserving Smoothing
            arcpy.FeaturePreservingSmoothing(in_raster, distance_units, neighborhood_distance, normal_difference_threshold, number_iterations, maximum_elevation_change, z_unit, analysis_target_device)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def geodesic_viewshed(self, params):
        """Geodesic Viewshed

Determines the raster surface locations visible to a set of observer features using geodesic methods. Learn more about how the Geodesic Viewshed tool works

        params: {"in_raster": <Raster Layer>, "in_observer_features": <Feature Layer>, "out_agl_raster": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_observer_features = params.get("in_observer_features")
        if in_observer_features is None:
            return {"success": False, "error": "in_observer_features parameter is required"}
        out_agl_raster = params.get("out_agl_raster")
        analysis_type = params.get("analysis_type")
        vertical_error = params.get("vertical_error")
        out_observer_region_relationship_table = params.get("out_observer_region_relationship_table")
        refractivity_coefficient = params.get("refractivity_coefficient")
        surface_offset = params.get("surface_offset")
        observer_elevation = params.get("observer_elevation")
        observer_offset = params.get("observer_offset")
        inner_radius = params.get("inner_radius")
        inner_radius_is_3d = params.get("inner_radius_is_3d")
        outer_radius = params.get("outer_radius")
        outer_radius_is_3d = params.get("outer_radius_is_3d")
        horizontal_start_angle = params.get("horizontal_start_angle")
        horizontal_end_angle = params.get("horizontal_end_angle")
        vertical_upper_angle = params.get("vertical_upper_angle")
        vertical_lower_angle = params.get("vertical_lower_angle")
        analysis_method = params.get("analysis_method")
        analysis_target_device = params.get("analysis_target_device")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Geodesic_Viewshed"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Geodesic Viewshed
            arcpy.GeodesicViewshed(in_raster, in_observer_features, out_agl_raster, analysis_type, vertical_error, out_observer_region_relationship_table, refractivity_coefficient, surface_offset, observer_elevation, observer_offset, inner_radius, inner_radius_is_3d, outer_radius, outer_radius_is_3d, horizontal_start_angle, horizontal_end_angle, vertical_upper_angle, vertical_lower_angle, analysis_method, analysis_target_device)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def geomorphon_landforms(self, params):
        """Geomorphon Landforms

Calculates the geomorphon pattern of each cell of an input surface raster and classifies calculated geomorphons into common landform types. Learn more about how Geomorphon Landforms works

        params: {"in_surface_raster": <Raster Layer>, "out_geomorphons_raster": <Raster Dataset>, "angle_threshold": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_surface_raster = params.get("in_surface_raster")
        if in_surface_raster is None:
            return {"success": False, "error": "in_surface_raster parameter is required"}
        out_geomorphons_raster = params.get("out_geomorphons_raster")
        angle_threshold = params.get("angle_threshold")
        distance_units = params.get("distance_units")
        search_distance = params.get("search_distance")
        skip_distance = params.get("skip_distance")
        z_unit = params.get("z_unit")

            # Generate output name and path
            output_name = f"{in_surface_raster.replace(' ', '_')}_Geomorphon_Landforms"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Geomorphon Landforms
            arcpy.GeomorphonLandforms(in_surface_raster, out_geomorphons_raster, angle_threshold, distance_units, search_distance, skip_distance, z_unit)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def hillshade(self, params):
        """Hillshade

Creates a shaded relief from a surface raster by considering the illumination source angle and shadows. Learn more about how Hillshade works

        params: {"in_raster": <Raster Layer>, "azimuth": <Double>, "altitude": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        azimuth = params.get("azimuth")
        altitude = params.get("altitude")
        model_shadows = params.get("model_shadows")
        z_factor = params.get("z_factor")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Hillshade"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Hillshade
            arcpy.Hillshade(in_raster, azimuth, altitude, model_shadows, z_factor)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def interpolate_shape(self, params):
        """Interpolate Shape

Creates 3D features by interpolating z-values from a surface. Learn more about how Interpolate Shape works

        params: {"in_surface": <LAS Dataset Layer; Mosaic Layer; Raster Layer; Terrain Layer; TIN Layer; Image Service>, "in_feature_class": <Feature Layer>, "out_feature_class": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_surface = params.get("in_surface")
        if in_surface is None:
            return {"success": False, "error": "in_surface parameter is required"}
        in_feature_class = params.get("in_feature_class")
        if in_feature_class is None:
            return {"success": False, "error": "in_feature_class parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        sample_distance = params.get("sample_distance")
        z_factor = params.get("z_factor")
        method = params.get("method")
        vertices_only = params.get("vertices_only")
        pyramid_level_resolution = params.get("pyramid_level_resolution")
        preserve_features = params.get("preserve_features")

            # Generate output name and path
            output_name = f"{in_surface.replace(' ', '_')}_Interpolate_Shape"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Interpolate Shape
            arcpy.InterpolateShape(in_surface, in_feature_class, out_feature_class, sample_distance, z_factor, method, vertices_only, pyramid_level_resolution, preserve_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def multiscale_surface_deviation(self, params):
        """Multiscale Surface Deviation

Calculates the maximum deviation from the mean value across a range of spatial scales. Learn more about how Multiscale Surface Deviation works

        params: {"in_raster": <Raster Layer>, "out_scale_raster": <Raster Dataset>, "distance_units": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_scale_raster = params.get("out_scale_raster")
        distance_units = params.get("distance_units")
        min_scale = params.get("min_scale")
        max_scale = params.get("max_scale")
        base_increment = params.get("base_increment")
        nonlinearity = params.get("nonlinearity")
        analysis_target_device = params.get("analysis_target_device")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Multiscale_Surface_Deviation"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Multiscale Surface Deviation
            arcpy.MultiscaleSurfaceDeviation(in_raster, out_scale_raster, distance_units, min_scale, max_scale, base_increment, nonlinearity, analysis_target_device)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def multiscale_surface_difference(self, params):
        """Multiscale Surface Difference

Calculates the maximum difference from the mean elevation across a range of spatial scales. Learn more about how Multiscale Surface Difference works.

        params: {"in_raster": <Raster Layer>, "out_scale_raster": <Raster Dataset>, "distance_units": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_scale_raster = params.get("out_scale_raster")
        distance_units = params.get("distance_units")
        min_scale = params.get("min_scale")
        max_scale = params.get("max_scale")
        increment = params.get("increment")
        analysis_target_device = params.get("analysis_target_device")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Multiscale_Surface_Difference"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Multiscale Surface Difference
            arcpy.MultiscaleSurfaceDifference(in_raster, out_scale_raster, distance_units, min_scale, max_scale, increment, analysis_target_device)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def multiscale_surface_percentile(self, params):
        """Multiscale Surface Percentile

Calculates the most extreme percentile across a range of spatial scales. Learn more about how Multiscale Surface Percentile works

        params: {"in_raster": <Raster Layer>, "out_scale_raster": <Raster Dataset>, "distance_units": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        out_scale_raster = params.get("out_scale_raster")
        distance_units = params.get("distance_units")
        min_scale = params.get("min_scale")
        max_scale = params.get("max_scale")
        base_increment = params.get("base_increment")
        nonlinearity = params.get("nonlinearity")
        analysis_target_device = params.get("analysis_target_device")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Multiscale_Surface_Percentile"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Multiscale Surface Percentile
            arcpy.MultiscaleSurfacePercentile(in_raster, out_scale_raster, distance_units, min_scale, max_scale, base_increment, nonlinearity, analysis_target_device)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def observer_points(self, params):
        """Observer Points

Identifies which observer points are visible from each raster surface location. The Geodesic Viewshed tool provides enhanced functionality or performance. Learn more about how Observer Points works

        params: {"in_raster": <Raster Layer>, "in_observer_point_features": <Feature Layer>, "z_factor": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_observer_point_features = params.get("in_observer_point_features")
        if in_observer_point_features is None:
            return {"success": False, "error": "in_observer_point_features parameter is required"}
        z_factor = params.get("z_factor")
        curvature_correction = params.get("curvature_correction")
        refractivity_coefficient = params.get("refractivity_coefficient")
        out_agl_raster = params.get("out_agl_raster")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Observer_Points"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Observer Points
            arcpy.ObserverPoints(in_raster, in_observer_point_features, z_factor, curvature_correction, refractivity_coefficient, out_agl_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def slope(self, params):
        """Slope

Identifies the slope (gradient or steepness) from each cell of a raster. The Surface Parameters tool provides a newer implementation and enhanced functionality. Learn more about how Slope works

        params: {"in_raster": <Raster Layer>, "output_measurement": <String>, "z_factor": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        output_measurement = params.get("output_measurement")
        z_factor = params.get("z_factor")
        method = params.get("method")
        z_unit = params.get("z_unit")
        analysis_target_device = params.get("analysis_target_device")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Slope"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Slope
            arcpy.Slope(in_raster, output_measurement, z_factor, method, z_unit, analysis_target_device)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def surface_parameters(self, params):
        """Surface Parameters

Determines parameters of a raster surface such as aspect, slope, and curvatures. Learn more about how Surface Parameters works

        params: {"in_raster": <Raster Layer>, "parameter_type": <String>, "local_surface_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        parameter_type = params.get("parameter_type")
        local_surface_type = params.get("local_surface_type")
        neighborhood_distance = params.get("neighborhood_distance")
        use_adaptive_neighborhood = params.get("use_adaptive_neighborhood")
        z_unit = params.get("z_unit")
        output_slope_measurement = params.get("output_slope_measurement")
        project_geodesic_azimuths = params.get("project_geodesic_azimuths")
        use_equatorial_aspect = params.get("use_equatorial_aspect")
        in_analysis_mask = params.get("in_analysis_mask")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Surface_Parameters"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Surface Parameters
            arcpy.SurfaceParameters(in_raster, parameter_type, local_surface_type, neighborhood_distance, use_adaptive_neighborhood, z_unit, output_slope_measurement, project_geodesic_azimuths, use_equatorial_aspect, in_analysis_mask)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def viewshed(self, params):
        """Viewshed

Determines the raster surface locations visible to a set of observer features. The Geodesic Viewshed tool provides enhanced functionality or performance. Learn more about how Viewshed works

        params: {"in_raster": <Raster Layer>, "in_observer_features": <Feature Layer>, "z_factor": <Double>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_observer_features = params.get("in_observer_features")
        if in_observer_features is None:
            return {"success": False, "error": "in_observer_features parameter is required"}
        z_factor = params.get("z_factor")
        curvature_correction = params.get("curvature_correction")
        refractivity_coefficient = params.get("refractivity_coefficient")
        out_agl_raster = params.get("out_agl_raster")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Viewshed"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Viewshed
            arcpy.Viewshed(in_raster, in_observer_features, z_factor, curvature_correction, refractivity_coefficient, out_agl_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def visibility(self, params):
        """Visibility

Determines the raster surface locations visible to a set of observer features, or identifies which observer points are visible from each raster surface location. The Geodesic Viewshed tool provides enhanced functionality or performance.

        params: {"in_raster": <Raster Layer>, "in_observer_features": <Feature Layer>, "out_agl_raster": <Raster Dataset>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_raster = params.get("in_raster")
        if in_raster is None:
            return {"success": False, "error": "in_raster parameter is required"}
        in_observer_features = params.get("in_observer_features")
        if in_observer_features is None:
            return {"success": False, "error": "in_observer_features parameter is required"}
        out_agl_raster = params.get("out_agl_raster")
        analysis_type = params.get("analysis_type")
        nonvisible_cell_value = params.get("nonvisible_cell_value")
        z_factor = params.get("z_factor")
        curvature_correction = params.get("curvature_correction")
        refractivity_coefficient = params.get("refractivity_coefficient")
        surface_offset = params.get("surface_offset")
        observer_elevation = params.get("observer_elevation")
        observer_offset = params.get("observer_offset")
        inner_radius = params.get("inner_radius")
        outer_radius = params.get("outer_radius")
        horizontal_start_angle = params.get("horizontal_start_angle")
        horizontal_end_angle = params.get("horizontal_end_angle")
        vertical_upper_angle = params.get("vertical_upper_angle")
        vertical_lower_angle = params.get("vertical_lower_angle")

            # Generate output name and path
            output_name = f"{in_raster.replace(' ', '_')}_Visibility"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Visibility
            arcpy.Visibility(in_raster, in_observer_features, out_agl_raster, analysis_type, nonvisible_cell_value, z_factor, curvature_correction, refractivity_coefficient, surface_offset, observer_elevation, observer_offset, inner_radius, outer_radius, horizontal_start_angle, horizontal_end_angle, vertical_upper_angle, vertical_lower_angle)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def tabulate_area(self, params):
        """Tabulate Area

Calculates cross-tabulated areas between two datasets and outputs a table.

        params: {"in_zone_data": <Raster Layer; Feature Layer>, "zone_field": <Field>, "in_class_data": <Raster Layer; Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_zone_data = params.get("in_zone_data")
        if in_zone_data is None:
            return {"success": False, "error": "in_zone_data parameter is required"}
        zone_field = params.get("zone_field")
        if zone_field is None:
            return {"success": False, "error": "zone_field parameter is required"}
        in_class_data = params.get("in_class_data")
        if in_class_data is None:
            return {"success": False, "error": "in_class_data parameter is required"}
        class_field = params.get("class_field")
        if class_field is None:
            return {"success": False, "error": "class_field parameter is required"}
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}
        processing_cell_size = params.get("processing_cell_size")
        classes_as_rows = params.get("classes_as_rows")

            # Generate output name and path
            output_name = f"{in_zone_data.replace(' ', '_')}_Tabulate_Area"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Tabulate Area
            arcpy.TabulateArea(in_zone_data, zone_field, in_class_data, class_field, out_table, processing_cell_size, classes_as_rows)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def zonal_characterization(self, params):
        """Zonal Characterization

Summarizes the values of multiple rasters within the zones of another dataset and reports the results as a table. Learn more about how zonal statistics tools work

        params: {"in_zone_raster_or_features": <Raster Layer; Feature Layer>, "out_statistics_table": <Table>, "out_statistics_features": <Feature Class>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_zone_raster_or_features = params.get("in_zone_raster_or_features")
        if in_zone_raster_or_features is None:
            return {"success": False, "error": "in_zone_raster_or_features parameter is required"}
        out_statistics_table = params.get("out_statistics_table")
        if out_statistics_table is None:
            return {"success": False, "error": "out_statistics_table parameter is required"}
        out_statistics_features = params.get("out_statistics_features")
        zone_field = params.get("zone_field")
        ignore_nodata = params.get("ignore_nodata")
        percentile_values = params.get("percentile_values")
        percentile_interpolation_type = params.get("percentile_interpolation_type")
        circular_calculation = params.get("circular_calculation")
        circular_wrap_value = params.get("circular_wrap_value")
        process_as_multidimensional = params.get("process_as_multidimensional")
        add_zone_attributes = params.get("add_zone_attributes")

            # Generate output name and path
            output_name = f"{in_zone_raster_or_features.replace(' ', '_')}_Zonal_Characterization"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Zonal Characterization
            arcpy.ZonalCharacterization(in_zone_raster_or_features, out_statistics_table, out_statistics_features, zone_field, ignore_nodata, percentile_values, percentile_interpolation_type, circular_calculation, circular_wrap_value, process_as_multidimensional, add_zone_attributes)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def zonal_fill(self, params):
        """Zonal Fill

Fills zones using the minimum cell value from a weight raster along the zone boundary.

        params: {"in_zone_raster": <Raster Layer>, "in_weight_raster": <Raster Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_zone_raster = params.get("in_zone_raster")
        if in_zone_raster is None:
            return {"success": False, "error": "in_zone_raster parameter is required"}
        in_weight_raster = params.get("in_weight_raster")
        if in_weight_raster is None:
            return {"success": False, "error": "in_weight_raster parameter is required"}

            # Generate output name and path
            output_name = f"{in_zone_raster.replace(' ', '_')}_Zonal_Fill"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Zonal Fill
            arcpy.ZonalFill(in_zone_raster, in_weight_raster)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def zonal_geometry(self, params):
        """Zonal Geometry

Calculates the specified geometry measure (area, perimeter, thickness, or the characteristics of an ellipse) for each zone in a dataset. Learn more about how Zonal Geometry works

        params: {"in_zone_data": <Raster Layer; Feature Layer>, "zone_field": <Field>, "geometry_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_zone_data = params.get("in_zone_data")
        if in_zone_data is None:
            return {"success": False, "error": "in_zone_data parameter is required"}
        zone_field = params.get("zone_field")
        if zone_field is None:
            return {"success": False, "error": "zone_field parameter is required"}
        geometry_type = params.get("geometry_type")
        cell_size = params.get("cell_size")

            # Generate output name and path
            output_name = f"{in_zone_data.replace(' ', '_')}_Zonal_Geometry"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Zonal Geometry
            arcpy.ZonalGeometry(in_zone_data, zone_field, geometry_type, cell_size)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def zonal_geometry_as_table(self, params):
        """Zonal Geometry As Table

Calculates the geometry measures (area, perimeter, thickness, and the characteristics of an ellipse) for each zone in a dataset and reports the results as a table. Learn more about how Zonal Geometry works

        params: {"in_zone_data": <Raster Layer; Feature Layer>, "zone_field": <Field>, "out_table": <Table>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_zone_data = params.get("in_zone_data")
        if in_zone_data is None:
            return {"success": False, "error": "in_zone_data parameter is required"}
        zone_field = params.get("zone_field")
        if zone_field is None:
            return {"success": False, "error": "zone_field parameter is required"}
        out_table = params.get("out_table")
        if out_table is None:
            return {"success": False, "error": "out_table parameter is required"}
        processing_cell_size = params.get("processing_cell_size")

            # Generate output name and path
            output_name = f"{in_zone_data.replace(' ', '_')}_Zonal_Geometry_As_Table"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Zonal Geometry As Table
            arcpy.ZonalGeometryAsTable(in_zone_data, zone_field, out_table, processing_cell_size)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def zonal_histogram(self, params):
        """Zonal Histogram

Creates a table and a histogram graph that show the frequency distribution of cell values on the value input for each unique zone.

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
        out_graph = params.get("out_graph")
        zones_as_rows = params.get("zones_as_rows")

            # Generate output name and path
            output_name = f"{in_zone_data.replace(' ', '_')}_Zonal_Histogram"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Zonal Histogram
            arcpy.ZonalHistogram(in_zone_data, zone_field, in_value_raster, out_table, out_graph, zones_as_rows)

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
