# Generated ArcGIS Pro network-analyst Progent Functions
# Generated on 2025-10-01T14:55:06.012052
# Total tools: 34

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

    def add_field_to_analysis_layer(self, params):
        """Add Field To Analysis Layer

Adds a field to a sublayer of a network analysis layer.

        params: {"in_network_analysis_layer": <Network Analyst Layer>, "sub_layer": <String>, "field_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_network_analysis_layer = params.get("in_network_analysis_layer")
        if in_network_analysis_layer is None:
            return {"success": False, "error": "in_network_analysis_layer parameter is required"}
        sub_layer = params.get("sub_layer")
        if sub_layer is None:
            return {"success": False, "error": "sub_layer parameter is required"}
        field_name = params.get("field_name")
        if field_name is None:
            return {"success": False, "error": "field_name parameter is required"}
        field_type = params.get("field_type")
        if field_type is None:
            return {"success": False, "error": "field_type parameter is required"}
        field_precision = params.get("field_precision")
        field_scale = params.get("field_scale")
        field_length = params.get("field_length")
        field_alias = params.get("field_alias")
        field_is_nullable = params.get("field_is_nullable")

            # Generate output name and path
            output_name = f"{in_network_analysis_layer.replace(' ', '_')}_Add_Field_To_Analysis_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Field To Analysis Layer
            arcpy.AddFieldToAnalysisLayer(in_network_analysis_layer, sub_layer, field_name, field_type, field_precision, field_scale, field_length, field_alias, field_is_nullable)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_locations(self, params):
        """Add Locations

Adds input features or records to a network analysis layer. The inputs are added to specific sublayers such as stops and barriers. When the network analysis layer references a network dataset as its network data source, the tool calculates the network locations of the inputs, unless precalculated network location fields are mapped from the inputs. Learn more about how the Add Locations tool locates analysis  inputs on the network

        params: {"in_network_analysis_layer": <Network Analyst Layer>, "sub_layer": <String>, "in_table": <Table View>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_network_analysis_layer = params.get("in_network_analysis_layer")
        if in_network_analysis_layer is None:
            return {"success": False, "error": "in_network_analysis_layer parameter is required"}
        sub_layer = params.get("sub_layer")
        if sub_layer is None:
            return {"success": False, "error": "sub_layer parameter is required"}
        in_table = params.get("in_table")
        if in_table is None:
            return {"success": False, "error": "in_table parameter is required"}
        field_mappings = params.get("field_mappings")
        search_tolerance = params.get("search_tolerance")
        sort_field = params.get("sort_field")
        search_criteriasource_snaptype = params.get("search_criteriasource_snaptype")
        match_type = params.get("match_type")
        append = params.get("append")
        snap_to_position_along_network = params.get("snap_to_position_along_network")
        snap_offset = params.get("snap_offset")
        exclude_restricted_elements = params.get("exclude_restricted_elements")
        search_querysource_expression = params.get("search_querysource_expression")
        allow_auto_relocate = params.get("allow_auto_relocate")

            # Generate output name and path
            output_name = f"{in_network_analysis_layer.replace(' ', '_')}_Add_Locations"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Locations
            arcpy.AddLocations(in_network_analysis_layer, sub_layer, in_table, field_mappings, search_tolerance, sort_field, search_criteriasource_snaptype, match_type, append, snap_to_position_along_network, snap_offset, exclude_restricted_elements, search_querysource_expression, allow_auto_relocate)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_fleet_routing_breaks(self, params):
        """Add Fleet Routing Breaks

Creates breaks in a Vehicle Routing Problem (VRP) layer.

        params: {"in_vrp_layer": <Network Analyst Layer>, "target_route": <String>, "break_type": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_vrp_layer = params.get("in_vrp_layer")
        if in_vrp_layer is None:
            return {"success": False, "error": "in_vrp_layer parameter is required"}
        target_route = params.get("target_route")
        break_type = params.get("break_type")
        time_window_properties = params.get("time_window_properties")
        travel_time_properties = params.get("travel_time_properties")
        work_time_properties = params.get("work_time_properties")
        append_to_existing_breaks = params.get("append_to_existing_breaks")

            # Generate output name and path
            output_name = f"{in_vrp_layer.replace(' ', '_')}_Add_Fleet_Routing_Breaks"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Fleet Routing Breaks
            arcpy.AddFleetRoutingBreaks(in_vrp_layer, target_route, break_type, time_window_properties, travel_time_properties, work_time_properties, append_to_existing_breaks)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def add_fleet_routing_routes(self, params):
        """Add Fleet Routing Routes

Creates routes in a vehicle routing problem, last mile delivery, or waste collection analysis layer. This tool will append rows to the Routes sublayer and can add rows with specific settings while creating a unique name field.

        params: {"in_vrp_layer": <Network Analyst Layer>, "number_of_routes": <Long>, "route_name_prefix": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_vrp_layer = params.get("in_vrp_layer")
        if in_vrp_layer is None:
            return {"success": False, "error": "in_vrp_layer parameter is required"}
        number_of_routes = params.get("number_of_routes")
        route_name_prefix = params.get("route_name_prefix")
        start_depot_name = params.get("start_depot_name")
        end_depot_name = params.get("end_depot_name")
        earliest_start_time = params.get("earliest_start_time")
        latest_start_time = params.get("latest_start_time")
        max_order_count = params.get("max_order_count")
        capacities = params.get("capacities")
        route_constraints = params.get("route_constraints")
        costs = params.get("costs")
        additional_route_time = params.get("additional_route_time")
        append_to_existing_routes = params.get("append_to_existing_routes")
        date_and_time = params.get("date_and_time")
        waste_capacities = params.get("waste_capacities")
        start_time = params.get("start_time")
        route_time_distance_constraints = params.get("route_time_distance_constraints")
        depot_service_time = params.get("depot_service_time")

            # Generate output name and path
            output_name = f"{in_vrp_layer.replace(' ', '_')}_Add_Fleet_Routing_Routes"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Add Fleet Routing Routes
            arcpy.AddFleetRoutingRoutes(in_vrp_layer, number_of_routes, route_name_prefix, start_depot_name, end_depot_name, earliest_start_time, latest_start_time, max_order_count, capacities, route_constraints, costs, additional_route_time, append_to_existing_routes, date_and_time, waste_capacities, start_time, route_time_distance_constraints, depot_service_time)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def calculate_locations(self, params):
        """Calculate Locations

Locates input features on a network and adds fields  to the input features that describe the network locations. The tool is used to precalculate the network locations of inputs that will be used in a Network Analyst workflow, improving performance of the analysis at solve time.  The tool stores the calculated network locations of the inputs in fields in the input data. Learn more about locating features on a network Learn more about precalculating network locations

        params: {"in_point_features": <Table View>, "in_network_dataset": <Network Dataset Layer>, "search_tolerance": <Linear Unit>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_point_features = params.get("in_point_features")
        if in_point_features is None:
            return {"success": False, "error": "in_point_features parameter is required"}
        in_network_dataset = params.get("in_network_dataset")
        search_tolerance = params.get("search_tolerance")
        search_criteriasource_snaptype = params.get("search_criteriasource_snaptype")
        match_type = params.get("match_type")
        source_id_field = params.get("source_id_field")
        source_oid_field = params.get("source_oid_field")
        position_field = params.get("position_field")
        side_field = params.get("side_field")
        snap_x_field = params.get("snap_x_field")
        snap_y_field = params.get("snap_y_field")
        distance_field = params.get("distance_field")
        snap_z_field = params.get("snap_z_field")
        location_field = params.get("location_field")
        exclude_restricted_elements = params.get("exclude_restricted_elements")
        search_querysource_expression = params.get("search_querysource_expression")
        travel_mode = params.get("travel_mode")

            # Generate output name and path
            output_name = f"{in_point_features.replace(' ', '_')}_Calculate_Locations"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Calculate Locations
            arcpy.CalculateLocations(in_point_features, in_network_dataset, search_tolerance, search_criteriasource_snaptype, match_type, source_id_field, source_oid_field, position_field, side_field, snap_x_field, snap_y_field, distance_field, snap_z_field, location_field, exclude_restricted_elements, search_querysource_expression, travel_mode)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def copy_network_analysis_layer(self, params):
        """Copy Network Analysis Layer

Copies a network analysis layer 
to a duplicate layer. The new layer will have the same analysis settings and network data source as the original layer and a copy of the original layer's analysis data.

        params: {"in_network_analysis_layer": <Network Analyst Layer>, "out_layer_name": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_network_analysis_layer = params.get("in_network_analysis_layer")
        if in_network_analysis_layer is None:
            return {"success": False, "error": "in_network_analysis_layer parameter is required"}
        out_layer_name = params.get("out_layer_name")

            # Generate output name and path
            output_name = f"{in_network_analysis_layer.replace(' ', '_')}_Copy_Network_Analysis_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Copy Network Analysis Layer
            arcpy.CopyNetworkAnalysisLayer(in_network_analysis_layer, out_layer_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def copy_traversed_source_features(self, params):
        """Copy Traversed Source Features

Creates two feature classes and a table, which together contain information about the edges, junctions, and turns that are traversed while solving a network analysis layer. Learn about the output from Copy Traversed Source Features

        params: {"input_network_analysis_layer": <Network Analyst Layer>, "output_location": <Workspace; Feature Dataset>, "edge_feature_class_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        input_network_analysis_layer = params.get("input_network_analysis_layer")
        if input_network_analysis_layer is None:
            return {"success": False, "error": "input_network_analysis_layer parameter is required"}
        output_location = params.get("output_location")
        if output_location is None:
            return {"success": False, "error": "output_location parameter is required"}
        edge_feature_class_name = params.get("edge_feature_class_name")
        if edge_feature_class_name is None:
            return {"success": False, "error": "edge_feature_class_name parameter is required"}
        junction_feature_class_name = params.get("junction_feature_class_name")
        if junction_feature_class_name is None:
            return {"success": False, "error": "junction_feature_class_name parameter is required"}
        turn_table_name = params.get("turn_table_name")
        if turn_table_name is None:
            return {"success": False, "error": "turn_table_name parameter is required"}

            # Generate output name and path
            output_name = f"{input_network_analysis_layer.replace(' ', '_')}_Copy_Traversed_Source_Features"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Copy Traversed Source Features
            arcpy.CopyTraversedSourceFeatures(input_network_analysis_layer, output_location, edge_feature_class_name, junction_feature_class_name, turn_table_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def delete_network_analysis_layer(self, params):
        """Delete Network Analysis Layer

Deletes a network analysis layer and its analysis data.

        params: {"in_network_analysis_layers": <Network Analyst Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_network_analysis_layers = params.get("in_network_analysis_layers")
        if in_network_analysis_layers is None:
            return {"success": False, "error": "in_network_analysis_layers parameter is required"}

            # Generate output name and path
            output_name = f"{in_network_analysis_layers.replace(' ', '_')}_Delete_Network_Analysis_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Delete Network Analysis Layer
            arcpy.DeleteNetworkAnalysisLayer(in_network_analysis_layers)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def directions(self, params):
        """Directions

Generates turn-by-turn directions from a network analysis layer with routes. The directions can be written to a file in text, XML, or HTML format. If you provide an appropriate style sheet, the directions can be written to any other file format.

        params: {"in_network_analysis_layer": <Network Analyst Layer>, "file_type": <String>, "out_directions_file": <File>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_network_analysis_layer = params.get("in_network_analysis_layer")
        if in_network_analysis_layer is None:
            return {"success": False, "error": "in_network_analysis_layer parameter is required"}
        file_type = params.get("file_type")
        if file_type is None:
            return {"success": False, "error": "file_type parameter is required"}
        out_directions_file = params.get("out_directions_file")
        if out_directions_file is None:
            return {"success": False, "error": "out_directions_file parameter is required"}
        report_units = params.get("report_units")
        if report_units is None:
            return {"success": False, "error": "report_units parameter is required"}
        report_time = params.get("report_time")
        time_attribute = params.get("time_attribute")
        language = params.get("language")
        style_name = params.get("style_name")
        stylesheet = params.get("stylesheet")

            # Generate output name and path
            output_name = f"{in_network_analysis_layer.replace(' ', '_')}_Directions"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Directions
            arcpy.Directions(in_network_analysis_layer, file_type, out_directions_file, report_units, report_time, time_attribute, language, style_name, stylesheet)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_closest_facility_analysis_layer(self, params):
        """Make Closest Facility Analysis Layer

Makes a closest facility network analysis layer and sets its analysis properties. A closest facility analysis layer is useful in determining the closest facility or facilities to an incident based on a specified travel mode. The layer can be created using a local network dataset or a service hosted online or in a portal.

        params: {"network_data_source": <Network Dataset Layer;String>, "layer_name": <String>, "travel_mode": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        network_data_source = params.get("network_data_source")
        if network_data_source is None:
            return {"success": False, "error": "network_data_source parameter is required"}
        layer_name = params.get("layer_name")
        travel_mode = params.get("travel_mode")
        travel_direction = params.get("travel_direction")
        cutoff = params.get("cutoff")
        number_of_facilities_to_find = params.get("number_of_facilities_to_find")
        time_of_day = params.get("time_of_day")
        time_zone = params.get("time_zone")
        time_of_day_usage = params.get("time_of_day_usage")
        line_shape = params.get("line_shape")
        accumulate_attributes = params.get("accumulate_attributes")
        generate_directions_on_solve = params.get("generate_directions_on_solve")
        ignore_invalid_locations = params.get("ignore_invalid_locations")

            # Generate output name and path
            output_name = f"{network_data_source.replace(' ', '_')}_Make_Closest_Facility_Analysis_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make Closest Facility Analysis Layer
            arcpy.MakeClosestFacilityAnalysisLayer(network_data_source, layer_name, travel_mode, travel_direction, cutoff, number_of_facilities_to_find, time_of_day, time_zone, time_of_day_usage, line_shape, accumulate_attributes, generate_directions_on_solve, ignore_invalid_locations)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_last_mile_delivery_analysis_layer(self, params):
        """Make Last Mile Delivery Analysis Layer

Creates a last mile delivery network analysis layer and sets its analysis properties. A last mile delivery analysis layer is useful for optimizing a set of routes using a fleet of vehicles. The layer can be created using a local network dataset or a service hosted online or in a portal.

        params: {"network_data_source": <Network Dataset Layer;String>, "layer_name": <String>, "travel_mode": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        network_data_source = params.get("network_data_source")
        if network_data_source is None:
            return {"success": False, "error": "network_data_source parameter is required"}
        layer_name = params.get("layer_name")
        travel_mode = params.get("travel_mode")
        time_units = params.get("time_units")
        distance_units = params.get("distance_units")
        earliest_route_start_date = params.get("earliest_route_start_date")
        earliest_route_start_time = params.get("earliest_route_start_time")
        max_route_total_time = params.get("max_route_total_time")
        time_zone_for_time_fields = params.get("time_zone_for_time_fields")
        sequence_gap = params.get("sequence_gap")
        ignore_invalid_order_locations = params.get("ignore_invalid_order_locations")
        line_shape = params.get("line_shape")
        generate_directions_on_solve = params.get("generate_directions_on_solve")

            # Generate output name and path
            output_name = f"{network_data_source.replace(' ', '_')}_Make_Last_Mile_Delivery_Analysis_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make Last Mile Delivery Analysis Layer
            arcpy.MakeLastMileDeliveryAnalysisLayer(network_data_source, layer_name, travel_mode, time_units, distance_units, earliest_route_start_date, earliest_route_start_time, max_route_total_time, time_zone_for_time_fields, sequence_gap, ignore_invalid_order_locations, line_shape, generate_directions_on_solve)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_location_allocation_analysis_layer(self, params):
        """Make Location-Allocation Analysis Layer

Makes a location-allocation network analysis layer and sets its analysis properties. A location-allocation analysis layer is useful for choosing a given number of facilities from a set of potential locations so that a demand will be allocated to facilities in an optimal and efficient manner. The layer can be created using a local network dataset or a service hosted online or in a portal.

        params: {"network_data_source": <Network Dataset Layer;String>, "layer_name": <String>, "travel_mode": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        network_data_source = params.get("network_data_source")
        if network_data_source is None:
            return {"success": False, "error": "network_data_source parameter is required"}
        layer_name = params.get("layer_name")
        travel_mode = params.get("travel_mode")
        travel_direction = params.get("travel_direction")
        problem_type = params.get("problem_type")
        cutoff = params.get("cutoff")
        number_of_facilities_to_find = params.get("number_of_facilities_to_find")
        decay_function_type = params.get("decay_function_type")
        decay_function_parameter_value = params.get("decay_function_parameter_value")
        target_market_share = params.get("target_market_share")
        capacity = params.get("capacity")
        time_of_day = params.get("time_of_day")
        time_zone = params.get("time_zone")
        line_shape = params.get("line_shape")
        accumulate_attributes = params.get("accumulate_attributes")
        ignore_invalid_locations = params.get("ignore_invalid_locations")

            # Generate output name and path
            output_name = f"{network_data_source.replace(' ', '_')}_Make_Location-Allocation_Analysis_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make Location-Allocation Analysis Layer
            arcpy.MakeLocationAllocationAnalysisLayer(network_data_source, layer_name, travel_mode, travel_direction, problem_type, cutoff, number_of_facilities_to_find, decay_function_type, decay_function_parameter_value, target_market_share, capacity, time_of_day, time_zone, line_shape, accumulate_attributes, ignore_invalid_locations)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_od_cost_matrix_analysis_layer(self, params):
        """Make OD Cost Matrix Analysis Layer

Makes an origin destination (OD) cost matrix network analysis layer and sets its analysis properties. An OD cost matrix analysis layer is useful for representing a matrix of costs going from a set of origin locations to a set of destination locations. The layer can be created using a local network dataset or a service hosted online or in a portal.

        params: {"network_data_source": <Network Dataset Layer;String>, "layer_name": <String>, "travel_mode": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        network_data_source = params.get("network_data_source")
        if network_data_source is None:
            return {"success": False, "error": "network_data_source parameter is required"}
        layer_name = params.get("layer_name")
        travel_mode = params.get("travel_mode")
        cutoff = params.get("cutoff")
        number_of_destinations_to_find = params.get("number_of_destinations_to_find")
        time_of_day = params.get("time_of_day")
        time_zone = params.get("time_zone")
        line_shape = params.get("line_shape")
        accumulate_attributes = params.get("accumulate_attributes")
        ignore_invalid_locations = params.get("ignore_invalid_locations")

            # Generate output name and path
            output_name = f"{network_data_source.replace(' ', '_')}_Make_OD_Cost_Matrix_Analysis_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make OD Cost Matrix Analysis Layer
            arcpy.MakeODCostMatrixAnalysisLayer(network_data_source, layer_name, travel_mode, cutoff, number_of_destinations_to_find, time_of_day, time_zone, line_shape, accumulate_attributes, ignore_invalid_locations)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_route_analysis_layer(self, params):
        """Make Route Analysis Layer

Makes a route network analysis layer and sets its analysis properties. A route network analysis layer is useful for determining the best route between a set of network locations based on a specified network cost. The layer can be created using a local network dataset or a routing service hosted online or in a portal.

        params: {"network_data_source": <Network Dataset Layer;String>, "layer_name": <String>, "travel_mode": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        network_data_source = params.get("network_data_source")
        if network_data_source is None:
            return {"success": False, "error": "network_data_source parameter is required"}
        layer_name = params.get("layer_name")
        travel_mode = params.get("travel_mode")
        sequence = params.get("sequence")
        time_of_day = params.get("time_of_day")
        time_zone = params.get("time_zone")
        line_shape = params.get("line_shape")
        accumulate_attributes = params.get("accumulate_attributes")
        generate_directions_on_solve = params.get("generate_directions_on_solve")
        time_zone_for_time_fields = params.get("time_zone_for_time_fields")
        ignore_invalid_locations = params.get("ignore_invalid_locations")

            # Generate output name and path
            output_name = f"{network_data_source.replace(' ', '_')}_Make_Route_Analysis_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make Route Analysis Layer
            arcpy.MakeRouteAnalysisLayer(network_data_source, layer_name, travel_mode, sequence, time_of_day, time_zone, line_shape, accumulate_attributes, generate_directions_on_solve, time_zone_for_time_fields, ignore_invalid_locations)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_service_area_analysis_layer(self, params):
        """Make Service Area Analysis Layer

Makes a service area network analysis layer and sets its analysis properties. A service area analysis layer is useful in determining the area of accessibility within a given cutoff cost from a facility location. The layer can be created using a local network dataset or a routing service hosted online or in a portal.

        params: {"network_data_source": <Network Dataset Layer;String>, "layer_name": <String>, "travel_mode": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        network_data_source = params.get("network_data_source")
        if network_data_source is None:
            return {"success": False, "error": "network_data_source parameter is required"}
        layer_name = params.get("layer_name")
        travel_mode = params.get("travel_mode")
        travel_direction = params.get("travel_direction")
        cutoffs = params.get("cutoffs")
        time_of_day = params.get("time_of_day")
        time_zone = params.get("time_zone")
        output_type = params.get("output_type")
        polygon_detail = params.get("polygon_detail")
        geometry_at_overlaps = params.get("geometry_at_overlaps")
        geometry_at_cutoffs = params.get("geometry_at_cutoffs")
        polygon_trim_distance = params.get("polygon_trim_distance")
        exclude_sources_from_polygon_generation = params.get("exclude_sources_from_polygon_generation")
        accumulate_attributes = params.get("accumulate_attributes")
        ignore_invalid_locations = params.get("ignore_invalid_locations")

            # Generate output name and path
            output_name = f"{network_data_source.replace(' ', '_')}_Make_Service_Area_Analysis_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make Service Area Analysis Layer
            arcpy.MakeServiceAreaAnalysisLayer(network_data_source, layer_name, travel_mode, travel_direction, cutoffs, time_of_day, time_zone, output_type, polygon_detail, geometry_at_overlaps, geometry_at_cutoffs, polygon_trim_distance, exclude_sources_from_polygon_generation, accumulate_attributes, ignore_invalid_locations)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_vehicle_routing_problem_analysis_layer(self, params):
        """Make Vehicle Routing Problem Analysis Layer

Creates a vehicle routing problem (VRP) network analysis layer and sets its analysis properties. A VRP analysis layer is useful for optimizing a set of routes using a fleet of vehicles. The layer can be created using a local network dataset or a service hosted online or in a portal.

        params: {"network_data_source": <Network Dataset Layer; String>, "layer_name": <String>, "travel_mode": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        network_data_source = params.get("network_data_source")
        if network_data_source is None:
            return {"success": False, "error": "network_data_source parameter is required"}
        layer_name = params.get("layer_name")
        travel_mode = params.get("travel_mode")
        time_units = params.get("time_units")
        distance_units = params.get("distance_units")
        default_date = params.get("default_date")
        time_zone_for_time_fields = params.get("time_zone_for_time_fields")
        line_shape = params.get("line_shape")
        time_window_factor = params.get("time_window_factor")
        excess_transit_factor = params.get("excess_transit_factor")
        generate_directions_on_solve = params.get("generate_directions_on_solve")
        spatial_clustering = params.get("spatial_clustering")
        ignore_invalid_locations = params.get("ignore_invalid_locations")

            # Generate output name and path
            output_name = f"{network_data_source.replace(' ', '_')}_Make_Vehicle_Routing_Problem_Analysis_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make Vehicle Routing Problem Analysis Layer
            arcpy.MakeVehicleRoutingProblemAnalysisLayer(network_data_source, layer_name, travel_mode, time_units, distance_units, default_date, time_zone_for_time_fields, line_shape, time_window_factor, excess_transit_factor, generate_directions_on_solve, spatial_clustering, ignore_invalid_locations)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_waste_collection_analysis_layer(self, params):
        """Make Waste Collection Analysis Layer

Creates a waste collection network analysis layer and sets its analysis properties. A waste collection analysis layer is useful for optimizing a set of routes using a fleet of vehicles to pick up municipal waste. The layer can be created using a network dataset.

        params: {"network_data_source": <Network Dataset Layer;String>, "layer_name": <String>, "travel_mode": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        network_data_source = params.get("network_data_source")
        if network_data_source is None:
            return {"success": False, "error": "network_data_source parameter is required"}
        layer_name = params.get("layer_name")
        travel_mode = params.get("travel_mode")
        time_units = params.get("time_units")
        distance_units = params.get("distance_units")
        route_start_time = params.get("route_start_time")
        max_route_total_time = params.get("max_route_total_time")
        stop_collection_mode = params.get("stop_collection_mode")

            # Generate output name and path
            output_name = f"{network_data_source.replace(' ', '_')}_Make_Waste_Collection_Analysis_Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make Waste Collection Analysis Layer
            arcpy.MakeWasteCollectionAnalysisLayer(network_data_source, layer_name, travel_mode, time_units, distance_units, route_start_time, max_route_total_time, stop_collection_mode)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def share_as_route_layers(self, params):
        """Share As Route Layers

Shares the results of network analyses as route layer items in a portal.  A route layer includes all the information for a route such as the stops assigned to the route or the orders serviced by a route, as well as the travel directions. A route layer item can be used by various applications, such as ArcGIS Navigator to provide route guidance for mobile workers, the Directions pane in Map Viewer Classic to further customize the route contained in the route layer, and ArcGIS Pro to create a route analysis layer from a route layer.

        params: {"in_network_analysis_layer": <File; Network Analyst Layer>, "summary": <String>, "tags": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_network_analysis_layer = params.get("in_network_analysis_layer")
        if in_network_analysis_layer is None:
            return {"success": False, "error": "in_network_analysis_layer parameter is required"}
        summary = params.get("summary")
        tags = params.get("tags")
        route_name_prefix = params.get("route_name_prefix")
        portal_folder_name = params.get("portal_folder_name")
        share_with = params.get("share_with")
        groups = params.get("groups")

            # Generate output name and path
            output_name = f"{in_network_analysis_layer.replace(' ', '_')}_Share_As_Route_Layers"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Share As Route Layers
            arcpy.ShareAsRouteLayers(in_network_analysis_layer, summary, tags, route_name_prefix, portal_folder_name, share_with, groups)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def solve(self, params):
        """Solve

Solves the network analysis layer problem based on its network locations and properties.

        params: {"in_network_analysis_layer": <Network Analyst Layer>, "ignore_invalids": <Boolean>, "terminate_on_solve_error": <Boolean>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_network_analysis_layer = params.get("in_network_analysis_layer")
        if in_network_analysis_layer is None:
            return {"success": False, "error": "in_network_analysis_layer parameter is required"}
        ignore_invalids = params.get("ignore_invalids")
        terminate_on_solve_error = params.get("terminate_on_solve_error")
        simplification_tolerance = params.get("simplification_tolerance")
        overrides = params.get("overrides")

            # Generate output name and path
            output_name = f"{in_network_analysis_layer.replace(' ', '_')}_Solve"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Solve
            arcpy.Solve(in_network_analysis_layer, ignore_invalids, terminate_on_solve_error, simplification_tolerance, overrides)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def select_layer_by_location(self, params):
        """Select Layer By Location

Selects features  based on a spatial relationship to features in another dataset or the same dataset. Each feature in the Input Features parameter is evaluated using the features in the  Selecting Features parameter. If the specified Relationship parameter value is met, the input feature is selected. Learn more about Select By Location including image examples of relationships

        params: {"in_layer": <Feature Layer; Raster Layer; Mosaic Layer>, "overlap_type": <String>, "select_features": <Feature Layer>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_layer = params.get("in_layer")
        if in_layer is None:
            return {"success": False, "error": "in_layer parameter is required"}
        overlap_type = params.get("overlap_type")
        select_features = params.get("select_features")
        search_distance = params.get("search_distance")
        selection_type = params.get("selection_type")
        invert_spatial_relationship = params.get("invert_spatial_relationship")

            # Generate output name and path
            output_name = f"{in_layer.replace(' ', '_')}_Select_Layer_By_Location"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Select Layer By Location
            arcpy.SelectLayerByLocation(in_layer, overlap_type, select_features, search_distance, selection_type, invert_spatial_relationship)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def copy_features(self, params):
        """Copy Features

Copies features from the input feature class or layer to a new feature class.

        params: {"in_features": <Feature Layer>, "out_feature_class": <Feature Class>, "config_keyword": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_features = params.get("in_features")
        if in_features is None:
            return {"success": False, "error": "in_features parameter is required"}
        out_feature_class = params.get("out_feature_class")
        if out_feature_class is None:
            return {"success": False, "error": "out_feature_class parameter is required"}
        config_keyword = params.get("config_keyword")
        spatial_grid_1 = params.get("spatial_grid_1")
        spatial_grid_2 = params.get("spatial_grid_2")
        spatial_grid_3 = params.get("spatial_grid_3")

            # Generate output name and path
            output_name = f"{in_features.replace(' ', '_')}_Copy_Features"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Copy Features
            arcpy.CopyFeatures(in_features, out_feature_class, config_keyword, spatial_grid_1, spatial_grid_2, spatial_grid_3)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def build_network(self, params):
        """Build Network

Reconstructs the network connectivity and attribute information of a network dataset. The network dataset must be rebuilt after edits are made to the attributes or the features of a participating source feature class. After the source features are edited, the tool establishes the network connectivity only in the areas that have been edited to speed up the build process; however, when the network attributes are edited, the entire extent of the network dataset is rebuilt. This may be a slow operation on a large network dataset. Learn more about which network dataset edits require a rebuild

        params: {"in_network_dataset": <Network Dataset Layer>, "force_full_build": <Boolean>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_network_dataset = params.get("in_network_dataset")
        if in_network_dataset is None:
            return {"success": False, "error": "in_network_dataset parameter is required"}
        force_full_build = params.get("force_full_build")

            # Generate output name and path
            output_name = f"{in_network_dataset.replace(' ', '_')}_Build_Network"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Build Network
            arcpy.BuildNetwork(in_network_dataset, force_full_build)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_network_dataset(self, params):
        """Create Network Dataset

Creates a network dataset in an existing feature dataset. The network dataset can be used to perform network analysis on the data in the feature dataset.

        params: {"feature_dataset": <Feature Dataset>, "out_name": <String>, "source_feature_class_names": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        feature_dataset = params.get("feature_dataset")
        if feature_dataset is None:
            return {"success": False, "error": "feature_dataset parameter is required"}
        out_name = params.get("out_name")
        if out_name is None:
            return {"success": False, "error": "out_name parameter is required"}
        source_feature_class_names = params.get("source_feature_class_names")
        if source_feature_class_names is None:
            return {"success": False, "error": "source_feature_class_names parameter is required"}
        elevation_model = params.get("elevation_model")
        if elevation_model is None:
            return {"success": False, "error": "elevation_model parameter is required"}

            # Generate output name and path
            output_name = f"{feature_dataset.replace(' ', '_')}_Create_Network_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Network Dataset
            arcpy.CreateNetworkDataset(feature_dataset, out_name, source_feature_class_names, elevation_model)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_network_dataset_from_template(self, params):
        """Create Network Dataset From Template

Creates a new network dataset with the schema contained in the input template file (.xml). All the feature classes and input tables required for creating the network dataset must already exist before this tool is executed.

        params: {"network_dataset_template": <File>, "output_feature_dataset": <Feature Dataset>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        network_dataset_template = params.get("network_dataset_template")
        if network_dataset_template is None:
            return {"success": False, "error": "network_dataset_template parameter is required"}
        output_feature_dataset = params.get("output_feature_dataset")
        if output_feature_dataset is None:
            return {"success": False, "error": "output_feature_dataset parameter is required"}

            # Generate output name and path
            output_name = f"{network_dataset_template.replace(' ', '_')}_Create_Network_Dataset_From_Template"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Network Dataset From Template
            arcpy.CreateNetworkDatasetFromTemplate(network_dataset_template, output_feature_dataset)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_template_from_network_dataset(self, params):
        """Create Template From Network Dataset

Creates a file containing the schema of an existing network dataset. This template file can then be used to create a new network dataset with the same schema.

        params: {"network_dataset": <Network Dataset Layer>, "output_network_dataset_template": <File>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        network_dataset = params.get("network_dataset")
        if network_dataset is None:
            return {"success": False, "error": "network_dataset parameter is required"}
        output_network_dataset_template = params.get("output_network_dataset_template")
        if output_network_dataset_template is None:
            return {"success": False, "error": "output_network_dataset_template parameter is required"}

            # Generate output name and path
            output_name = f"{network_dataset.replace(' ', '_')}_Create_Template_From_Network_Dataset"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Template From Network Dataset
            arcpy.CreateTemplateFromNetworkDataset(network_dataset, output_network_dataset_template)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def dissolve_network(self, params):
        """Dissolve Network

Creates a network dataset that minimizes the number of line features required to correctly model the input network dataset. The more efficient output network dataset reduces the time required to solve analyses, draw results, and generate driving directions. This tool outputs a new network dataset and source feature classes; the input network dataset and its source features remain unchanged.

        params: {"in_network_dataset": <Network Dataset Layer>, "out_workspace_location": <Workspace>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_network_dataset = params.get("in_network_dataset")
        if in_network_dataset is None:
            return {"success": False, "error": "in_network_dataset parameter is required"}
        out_workspace_location = params.get("out_workspace_location")
        if out_workspace_location is None:
            return {"success": False, "error": "out_workspace_location parameter is required"}

            # Generate output name and path
            output_name = f"{in_network_dataset.replace(' ', '_')}_Dissolve_Network"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Dissolve Network
            arcpy.DissolveNetwork(in_network_dataset, out_workspace_location)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def make_network_dataset___layer(self, params):
        """Make Network Dataset   Layer

Creates a network dataset layer from a network  dataset. A network dataset is opened each time the network dataset is used as input to a geoprocessing tool. Opening a network dataset is expensive, as they contain advanced data structures and tables that are read and cached. A network dataset layer, which opens the dataset only a single time, will perform better in subsequent tools than reusing the network dataset.

        params: {"in_network_dataset": <Network Dataset Layer>, "output_layer": <Network Dataset Layer>, "draw_elements": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_network_dataset = params.get("in_network_dataset")
        if in_network_dataset is None:
            return {"success": False, "error": "in_network_dataset parameter is required"}
        output_layer = params.get("output_layer")
        if output_layer is None:
            return {"success": False, "error": "output_layer parameter is required"}
        draw_elements = params.get("draw_elements")

            # Generate output name and path
            output_name = f"{in_network_dataset.replace(' ', '_')}_Make_Network_Dataset___Layer"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Make Network Dataset   Layer
            arcpy.MakeNetworkDatasetLayer(in_network_dataset, output_layer, draw_elements)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def integrate(self, params):
        """Integrate

Analyzes the coordinate locations of feature vertices among features in one or more feature classes. Those that fall within a specified distance of one another are assumed to represent the same location and are assigned a common coordinate value (in other words, they are colocated). The tool also adds vertices where feature vertices are within the x,y tolerance of an edge and where line segments intersect. Integrate performs
the following processing tasks: Vertices within the x,y tolerance of one another will be assigned the same coordinate location.When a vertex of one feature is within the x,y tolerance of an edge of any other feature, a new vertex will be inserted on the edge.When line segments intersect, a vertex will be inserted at the point of intersection for each feature involved in the intersection. An alternate tool is available for vector data integration. See the Pairwise Integrate documentation for details.

        params: {"in_featuresfeature_layer_long": <Value Table>, "cluster_tolerance": <Linear Unit>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_featuresfeature_layer_long = params.get("in_featuresfeature_layer_long")
        if in_featuresfeature_layer_long is None:
            return {"success": False, "error": "in_featuresfeature_layer_long parameter is required"}
        cluster_tolerance = params.get("cluster_tolerance")

            # Generate output name and path
            output_name = f"{in_featuresfeature_layer_long.replace(' ', '_')}_Integrate"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Integrate
            arcpy.Integrate(in_featuresfeature_layer_long, cluster_tolerance)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_turn_feature_class(self, params):
        """Create Turn Feature Class

Creates a turn feature class to store turn features that model turning movements in a network dataset.

        params: {"out_location": <Workspace; Feature Dataset>, "out_feature_class_name": <String>, "maximum_edges": <Long>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        out_location = params.get("out_location")
        if out_location is None:
            return {"success": False, "error": "out_location parameter is required"}
        out_feature_class_name = params.get("out_feature_class_name")
        if out_feature_class_name is None:
            return {"success": False, "error": "out_feature_class_name parameter is required"}
        maximum_edges = params.get("maximum_edges")
        in_network_dataset = params.get("in_network_dataset")
        in_template_feature_class = params.get("in_template_feature_class")
        spatial_reference = params.get("spatial_reference")
        config_keyword = params.get("config_keyword")
        spatial_grid_1 = params.get("spatial_grid_1")
        spatial_grid_2 = params.get("spatial_grid_2")
        spatial_grid_3 = params.get("spatial_grid_3")
        has_z = params.get("has_z")

            # Generate output name and path
            output_name = f"{out_location.replace(' ', '_')}_Create_Turn_Feature_Class"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Create Turn Feature Class
            arcpy.CreateTurnFeatureClass(out_location, out_feature_class_name, maximum_edges, in_network_dataset, in_template_feature_class, spatial_reference, config_keyword, spatial_grid_1, spatial_grid_2, spatial_grid_3, has_z)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def increase_maximum_edges(self, params):
        """Increase Maximum Edges

Increases the maximum number of edges per turn in a turn feature class.

        params: {"in_turn_features": <Feature Layer>, "maximum_edges": <Long>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_turn_features = params.get("in_turn_features")
        if in_turn_features is None:
            return {"success": False, "error": "in_turn_features parameter is required"}
        maximum_edges = params.get("maximum_edges")
        if maximum_edges is None:
            return {"success": False, "error": "maximum_edges parameter is required"}

            # Generate output name and path
            output_name = f"{in_turn_features.replace(' ', '_')}_Increase_Maximum_Edges"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Increase Maximum Edges
            arcpy.IncreaseMaximumEdges(in_turn_features, maximum_edges)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def populate_alternate_id_fields(self, params):
        """Populate Alternate ID Fields

Creates and populates additional fields on the turn feature classes that reference the edges in the network  by alternate IDs. The alternate IDs help maintain the integrity of the turn features if the edge sources are edited in such a way that their ObjectID values change. Learn more about turns in a network dataset

        params: {"in_network_dataset": <Network Dataset Layer>, "alternate_id_field_name": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_network_dataset = params.get("in_network_dataset")
        if in_network_dataset is None:
            return {"success": False, "error": "in_network_dataset parameter is required"}
        alternate_id_field_name = params.get("alternate_id_field_name")
        if alternate_id_field_name is None:
            return {"success": False, "error": "alternate_id_field_name parameter is required"}

            # Generate output name and path
            output_name = f"{in_network_dataset.replace(' ', '_')}_Populate_Alternate_ID_Fields"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Populate Alternate ID Fields
            arcpy.PopulateAlternateIDFields(in_network_dataset, alternate_id_field_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def turn_table_to_turn_feature_class(self, params):
        """Turn Table To Turn Feature Class

Converts an ArcView turn table or ArcInfo Workstation coverage turn table to an ArcGIS turn feature class.

        params: {"in_turn_table": <Table View>, "reference_line_features": <Feature Class>, "out_feature_class_name": <String>, ...}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_turn_table = params.get("in_turn_table")
        if in_turn_table is None:
            return {"success": False, "error": "in_turn_table parameter is required"}
        reference_line_features = params.get("reference_line_features")
        if reference_line_features is None:
            return {"success": False, "error": "reference_line_features parameter is required"}
        out_feature_class_name = params.get("out_feature_class_name")
        if out_feature_class_name is None:
            return {"success": False, "error": "out_feature_class_name parameter is required"}
        reference_nodes_table = params.get("reference_nodes_table")
        maximum_edges = params.get("maximum_edges")
        config_keyword = params.get("config_keyword")
        spatial_grid_1 = params.get("spatial_grid_1")
        spatial_grid_2 = params.get("spatial_grid_2")
        spatial_grid_3 = params.get("spatial_grid_3")

            # Generate output name and path
            output_name = f"{in_turn_table.replace(' ', '_')}_Turn_Table_To_Turn_Feature_Class"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Turn Table To Turn Feature Class
            arcpy.TurnTableToTurnFeatureClass(in_turn_table, reference_line_features, out_feature_class_name, reference_nodes_table, maximum_edges, config_keyword, spatial_grid_1, spatial_grid_2, spatial_grid_3)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def update_by_alternate_id_fields(self, params):
        """Update By Alternate ID Fields

Updates all the edge references in turn feature classes using an alternate ID field to identify the corresponding edge features for each turn. Use this tool after making edits to the edge source feature classes that alter ObjectID values. Learn more about turns in a network dataset

        params: {"in_network_dataset": <Network Dataset Layer>, "alternate_id_field_name": <String>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_network_dataset = params.get("in_network_dataset")
        if in_network_dataset is None:
            return {"success": False, "error": "in_network_dataset parameter is required"}
        alternate_id_field_name = params.get("alternate_id_field_name")
        if alternate_id_field_name is None:
            return {"success": False, "error": "alternate_id_field_name parameter is required"}

            # Generate output name and path
            output_name = f"{in_network_dataset.replace(' ', '_')}_Update_By_Alternate_ID_Fields"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Update By Alternate ID Fields
            arcpy.UpdateByAlternateIDFields(in_network_dataset, alternate_id_field_name)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}


    def update_by_geometry(self, params):
        """Update By Geometry

Updates all the edge references in the turn feature class using the geometry of the turn features. This tool is useful when the IDs listed for the turn can no longer find the edges participating in the turn due to edits to the underlying edges.

        params: {"in_turn_features": <Feature Layer>}
        Returns: {"success": True, "output_layer": <output_name>, "output_path": <output_path>} or error
        """
        try:
        in_turn_features = params.get("in_turn_features")
        if in_turn_features is None:
            return {"success": False, "error": "in_turn_features parameter is required"}

            # Generate output name and path
            output_name = f"{in_turn_features.replace(' ', '_')}_Update_By_Geometry"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute Update By Geometry
            arcpy.UpdateByGeometry(in_turn_features)

            self._add_to_map(output_path)
            return {"success": True, "output_layer": output_name, "output_path": output_path}

        except Exception as e:
            return {"success": False, "error": str(e)}
