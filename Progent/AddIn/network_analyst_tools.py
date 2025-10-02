# Corrected ArcGIS Pro network-analyst Progent Functions
import arcpy
import os

class NetworkAnalystTools:
    """A collection of network analyst tools generated from ArcGIS Pro documentation."""

    def _add_to_map(self, path):
        try:
            aprx = arcpy.mp.ArcGISProject('CURRENT')
            map_obj = aprx.activeMap
            if map_obj:
                map_obj.addDataFromPath(path)
        except Exception as e:
            print(f'Could not add {path} to map: {e}')

    def add_field_to_analysis_layer(self, params):
        """
        Adds a field to a sublayer of a network analysis layer.
        """
        try:
            arcpy.CheckOutExtension("Network")
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

            result = arcpy.na.AddFieldToAnalysisLayer(
                in_network_analysis_layer, sub_layer, field_name, field_type,
                field_precision, field_scale, field_length, field_alias, field_is_nullable
            )

            output_layer = result.getOutput(0)
            return {"success": True, "output_layer": output_layer, "output_path": output_layer}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def make_network_dataset_layer(self, params):
        """
        Creates a network dataset layer from a network dataset.
        """
        try:
            # This tool is in the na module, but it's a layer creation tool.
            in_network_dataset = params.get("in_network_dataset")
            if in_network_dataset is None:
                return {"success": False, "error": "in_network_dataset parameter is required"}
            output_layer = params.get("output_layer")
            if output_layer is None:
                return {"success": False, "error": "output_layer parameter is required"}

            draw_elements = params.get("draw_elements")

            result = arcpy.na.MakeNetworkDatasetLayer(in_network_dataset, output_layer, draw_elements)

            output_layer_obj = result.getOutput(0)
            self._add_to_map(output_layer_obj.name)
            return {"success": True, "output_layer": output_layer_obj.name, "output_path": output_layer_obj.name}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def integrate(self, params):
        """
        Analyzes the coordinate locations of feature vertices among features in one or more feature classes.
        This is a Data Management tool.
        """
        try:
            in_features = params.get("in_featuresfeature_layer_long") # Corrected param name
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            cluster_tolerance = params.get("cluster_tolerance")

            arcpy.management.Integrate(in_features, cluster_tolerance)

            return {"success": True, "message": f"Successfully ran Integrate on {in_features}."}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def create_turn_feature_class(self, params):
        """
        Creates a turn feature class to store turn features that model turning movements in a network dataset.
        """
        try:
            arcpy.CheckOutExtension("Network")
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

            result = arcpy.na.CreateTurnFeatureClass(
                out_location, out_feature_class_name, maximum_edges, in_network_dataset,
                in_template_feature_class, spatial_reference, config_keyword, spatial_grid_1,
                spatial_grid_2, spatial_grid_3, has_z
            )

            output_fc = result.getOutput(0)
            self._add_to_map(output_fc)
            return {"success": True, "output_layer": os.path.basename(output_fc), "output_path": output_fc}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def increase_maximum_edges(self, params):
        """
        Increases the maximum number of edges per turn in a turn feature class.
        """
        try:
            arcpy.CheckOutExtension("Network")
            in_turn_features = params.get("in_turn_features")
            if in_turn_features is None:
                return {"success": False, "error": "in_turn_features parameter is required"}
            maximum_edges = params.get("maximum_edges")
            if maximum_edges is None:
                return {"success": False, "error": "maximum_edges parameter is required"}

            result = arcpy.na.IncreaseMaximumEdges(in_turn_features, maximum_edges)

            return {"success": True, "output_layer": result.getOutput(0)}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def populate_alternate_id_fields(self, params):
        """
        Creates and populates additional fields on the turn feature classes that reference the edges by alternate IDs.
        """
        try:
            arcpy.CheckOutExtension("Network")
            in_network_dataset = params.get("in_network_dataset")
            if in_network_dataset is None:
                return {"success": False, "error": "in_network_dataset parameter is required"}
            alternate_id_field_name = params.get("alternate_id_field_name")
            if alternate_id_field_name is None:
                return {"success": False, "error": "alternate_id_field_name parameter is required"}

            arcpy.na.PopulateAlternateIDFields(in_network_dataset, alternate_id_field_name)

            return {"success": True, "message": "Alternate ID fields populated successfully."}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def turn_table_to_turn_feature_class(self, params):
        """
        Converts an ArcView turn table or ArcInfo Workstation coverage turn table to an ArcGIS turn feature class.
        """
        try:
            arcpy.CheckOutExtension("Network")
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

            result = arcpy.na.TurnTableToTurnFeatureClass(
                in_turn_table, reference_line_features, out_feature_class_name, reference_nodes_table,
                maximum_edges, config_keyword, spatial_grid_1, spatial_grid_2, spatial_grid_3
            )

            output_fc = result.getOutput(0)
            self._add_to_map(output_fc)
            return {"success": True, "output_layer": os.path.basename(output_fc), "output_path": output_fc}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def update_by_alternate_id_fields(self, params):
        """
        Updates all the edge references in turn feature classes using an alternate ID field.
        """
        try:
            arcpy.CheckOutExtension("Network")
            in_network_dataset = params.get("in_network_dataset")
            if in_network_dataset is None:
                return {"success": False, "error": "in_network_dataset parameter is required"}
            alternate_id_field_name = params.get("alternate_id_field_name")
            if alternate_id_field_name is None:
                return {"success": False, "error": "alternate_id_field_name parameter is required"}

            arcpy.na.UpdateByAlternateIDFields(in_network_dataset, alternate_id_field_name)

            return {"success": True, "message": "Updated by alternate ID fields successfully."}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def update_by_geometry(self, params):
        """
        Updates all the edge references in the turn feature class using the geometry of the turn features.
        """
        try:
            arcpy.CheckOutExtension("Network")
            in_turn_features = params.get("in_turn_features")
            if in_turn_features is None:
                return {"success": False, "error": "in_turn_features parameter is required"}

            result = arcpy.na.UpdateByGeometry(in_turn_features)

            return {"success": True, "output_layer": result.getOutput(0)}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def create_network_dataset(self, params):
        """
        Creates a network dataset in an existing feature dataset.
        """
        try:
            arcpy.CheckOutExtension("Network")
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

            result = arcpy.na.CreateNetworkDataset(
                feature_dataset, out_name, source_feature_class_names, elevation_model
            )

            output_network = result.getOutput(0)
            # A network dataset isn't a layer to be added to a map directly, but we can return its path.
            return {"success": True, "output_network": output_network}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def create_network_dataset_from_template(self, params):
        """
        Creates a new network dataset with the schema contained in the input template file (.xml).
        """
        try:
            arcpy.CheckOutExtension("Network")
            network_dataset_template = params.get("network_dataset_template")
            if network_dataset_template is None:
                return {"success": False, "error": "network_dataset_template parameter is required"}
            output_feature_dataset = params.get("output_feature_dataset")
            if output_feature_dataset is None:
                return {"success": False, "error": "output_feature_dataset parameter is required"}

            result = arcpy.na.CreateNetworkDatasetFromTemplate(network_dataset_template, output_feature_dataset)

            output_network = result.getOutput(0)
            return {"success": True, "output_network": output_network}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def create_template_from_network_dataset(self, params):
        """
        Creates a file containing the schema of an existing network dataset.
        """
        try:
            arcpy.CheckOutExtension("Network")
            network_dataset = params.get("network_dataset")
            if network_dataset is None:
                return {"success": False, "error": "network_dataset parameter is required"}
            output_network_dataset_template = params.get("output_network_dataset_template")
            if output_network_dataset_template is None:
                # Create a default output file path
                temp_folder = arcpy.env.scratchFolder
                output_network_dataset_template = os.path.join(temp_folder, "network_template.xml")

            result = arcpy.na.CreateTemplateFromNetworkDataset(network_dataset, output_network_dataset_template)

            return {"success": True, "output_file": result.getOutput(0)}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def dissolve_network(self, params):
        """
        Creates a network dataset that minimizes the number of line features required to correctly model the input network.
        """
        try:
            arcpy.CheckOutExtension("Network")
            in_network_dataset = params.get("in_network_dataset")
            if in_network_dataset is None:
                return {"success": False, "error": "in_network_dataset parameter is required"}
            out_workspace_location = params.get("out_workspace_location")
            if out_workspace_location is None:
                return {"success": False, "error": "out_workspace_location parameter is required"}

            result = arcpy.na.DissolveNetwork(in_network_dataset, out_workspace_location)

            # This tool returns the path to the new network dataset
            return {"success": True, "output_network": result.getOutput(0)}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def share_as_route_layers(self, params):
        """
        Shares the results of network analyses as route layer items in a portal.
        """
        try:
            arcpy.CheckOutExtension("Network")
            in_network_analysis_layer = params.get("in_network_analysis_layer")
            if in_network_analysis_layer is None:
                return {"success": False, "error": "in_network_analysis_layer parameter is required"}
            summary = params.get("summary")
            if summary is None:
                return {"success": False, "error": "summary parameter is required"}
            tags = params.get("tags")
            if tags is None:
                return {"success": False, "error": "tags parameter is required"}

            route_name_prefix = params.get("route_name_prefix")
            portal_folder_name = params.get("portal_folder_name")
            share_with = params.get("share_with")
            groups = params.get("groups")

            result = arcpy.na.ShareAsRouteLayers(
                in_network_analysis_layer, summary, tags, route_name_prefix,
                portal_folder_name, share_with, groups
            )

            # This tool returns a list of portal item IDs.
            return {"success": True, "output_items": result.getOutput(0)}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def solve(self, params):
        """
        Solves the network analysis layer problem based on its network locations and properties.
        """
        try:
            arcpy.CheckOutExtension("Network")
            in_network_analysis_layer = params.get("in_network_analysis_layer")
            if in_network_analysis_layer is None:
                return {"success": False, "error": "in_network_analysis_layer parameter is required"}

            ignore_invalids = params.get("ignore_invalids", "IGNORE")
            terminate_on_solve_error = params.get("terminate_on_solve_error", "TERMINATE")
            simplification_tolerance = params.get("simplification_tolerance")
            overrides = params.get("overrides")

            result = arcpy.na.Solve(
                in_network_analysis_layer, ignore_invalids, terminate_on_solve_error,
                simplification_tolerance, overrides
            )

            solve_succeeded = result.solveSucceeded
            if not solve_succeeded:
                # Get the messages from the result object
                messages = result.getMessages(1) # 1 for errors
                return {"success": False, "error": messages}

            output_layer = result.getOutput(0)
            return {"success": True, "output_layer": output_layer, "output_path": output_layer}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def select_layer_by_location(self, params):
        """
        Selects features based on a spatial relationship to features in another dataset.
        This is a Data Management tool, not a Network Analyst tool.
        """
        try:
            in_layer = params.get("in_layer")
            if in_layer is None:
                return {"success": False, "error": "in_layer parameter is required"}
            overlap_type = params.get("overlap_type")
            if overlap_type is None:
                return {"success": False, "error": "overlap_type parameter is required"}
            select_features = params.get("select_features")

            search_distance = params.get("search_distance")
            selection_type = params.get("selection_type", "NEW_SELECTION")
            invert_spatial_relationship = params.get("invert_spatial_relationship")

            # This tool is in the management toolbox
            result = arcpy.management.SelectLayerByLocation(
                in_layer, overlap_type, select_features, search_distance,
                selection_type, invert_spatial_relationship
            )

            output_layer = result.getOutput(0)
            return {"success": True, "output_layer": output_layer, "output_path": output_layer}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def copy_features(self, params):
        """
        Copies features from the input feature class or layer to a new feature class.
        This is a Data Management tool, not a Network Analyst tool.
        """
        try:
            in_features = params.get("in_features")
            if in_features is None:
                return {"success": False, "error": "in_features parameter is required"}
            out_feature_class = params.get("out_feature_class")
            if out_feature_class is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                out_feature_class = arcpy.CreateUniqueName("CopiedFeatures", aprx.defaultGeodatabase)

            config_keyword = params.get("config_keyword")
            spatial_grid_1 = params.get("spatial_grid_1")
            spatial_grid_2 = params.get("spatial_grid_2")
            spatial_grid_3 = params.get("spatial_grid_3")

            result = arcpy.management.CopyFeatures(
                in_features, out_feature_class, config_keyword, spatial_grid_1, spatial_grid_2, spatial_grid_3
            )

            output_layer = result.getOutput(0)
            self._add_to_map(output_layer)
            return {"success": True, "output_layer": os.path.basename(output_layer), "output_path": output_layer}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def build_network(self, params):
        """
        Reconstructs the network connectivity and attribute information of a network dataset.
        """
        try:
            arcpy.CheckOutExtension("Network")
            in_network_dataset = params.get("in_network_dataset")
            if in_network_dataset is None:
                return {"success": False, "error": "in_network_dataset parameter is required"}

            force_full_build = params.get("force_full_build")

            arcpy.na.BuildNetwork(in_network_dataset, force_full_build)

            return {"success": True, "message": f"Successfully built network for {in_network_dataset}."}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def make_route_analysis_layer(self, params):
        """
        Makes a route network analysis layer and sets its analysis properties.
        """
        try:
            arcpy.CheckOutExtension("Network")
            network_data_source = params.get("network_data_source")
            if network_data_source is None:
                return {"success": False, "error": "network_data_source parameter is required"}
            layer_name = params.get("layer_name")
            if layer_name is None:
                return {"success": False, "error": "layer_name parameter is required"}

            travel_mode = params.get("travel_mode")
            sequence = params.get("sequence")
            time_of_day = params.get("time_of_day")
            time_zone = params.get("time_zone")
            line_shape = params.get("line_shape")
            accumulate_attributes = params.get("accumulate_attributes")
            generate_directions_on_solve = params.get("generate_directions_on_solve")
            time_zone_for_time_fields = params.get("time_zone_for_time_fields")
            ignore_invalid_locations = params.get("ignore_invalid_locations")

            result = arcpy.na.MakeRouteAnalysisLayer(
                network_data_source, layer_name, travel_mode, sequence, time_of_day, time_zone, line_shape,
                accumulate_attributes, generate_directions_on_solve, time_zone_for_time_fields,
                ignore_invalid_locations
            )

            output_layer = result.getOutput(0)
            self._add_to_map(output_layer.name)
            return {"success": True, "output_layer": output_layer.name, "output_path": output_layer.name}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def make_service_area_analysis_layer(self, params):
        """
        Makes a service area network analysis layer and sets its analysis properties.
        """
        try:
            arcpy.CheckOutExtension("Network")
            network_data_source = params.get("network_data_source")
            if network_data_source is None:
                return {"success": False, "error": "network_data_source parameter is required"}
            layer_name = params.get("layer_name")
            if layer_name is None:
                return {"success": False, "error": "layer_name parameter is required"}

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

            result = arcpy.na.MakeServiceAreaAnalysisLayer(
                network_data_source, layer_name, travel_mode, travel_direction, cutoffs, time_of_day, time_zone,
                output_type, polygon_detail, geometry_at_overlaps, geometry_at_cutoffs, polygon_trim_distance,
                exclude_sources_from_polygon_generation, accumulate_attributes, ignore_invalid_locations
            )

            output_layer = result.getOutput(0)
            self._add_to_map(output_layer.name)
            return {"success": True, "output_layer": output_layer.name, "output_path": output_layer.name}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def make_vehicle_routing_problem_analysis_layer(self, params):
        """
        Creates a vehicle routing problem (VRP) network analysis layer and sets its analysis properties.
        """
        try:
            arcpy.CheckOutExtension("Network")
            network_data_source = params.get("network_data_source")
            if network_data_source is None:
                return {"success": False, "error": "network_data_source parameter is required"}
            layer_name = params.get("layer_name")
            if layer_name is None:
                return {"success": False, "error": "layer_name parameter is required"}

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

            result = arcpy.na.MakeVehicleRoutingProblemAnalysisLayer(
                network_data_source, layer_name, travel_mode, time_units, distance_units, default_date,
                time_zone_for_time_fields, line_shape, time_window_factor, excess_transit_factor,
                generate_directions_on_solve, spatial_clustering, ignore_invalid_locations
            )

            output_layer = result.getOutput(0)
            self._add_to_map(output_layer.name)
            return {"success": True, "output_layer": output_layer.name, "output_path": output_layer.name}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def make_waste_collection_analysis_layer(self, params):
        """
        Creates a waste collection network analysis layer and sets its analysis properties.
        """
        try:
            arcpy.CheckOutExtension("Network")
            network_data_source = params.get("network_data_source")
            if network_data_source is None:
                return {"success": False, "error": "network_data_source parameter is required"}
            layer_name = params.get("layer_name")
            if layer_name is None:
                return {"success": False, "error": "layer_name parameter is required"}

            travel_mode = params.get("travel_mode")
            time_units = params.get("time_units")
            distance_units = params.get("distance_units")
            route_start_time = params.get("route_start_time")
            max_route_total_time = params.get("max_route_total_time")
            stop_collection_mode = params.get("stop_collection_mode")

            result = arcpy.na.MakeWasteCollectionAnalysisLayer(
                network_data_source, layer_name, travel_mode, time_units, distance_units,
                route_start_time, max_route_total_time, stop_collection_mode
            )

            output_layer = result.getOutput(0)
            self._add_to_map(output_layer.name)
            return {"success": True, "output_layer": output_layer.name, "output_path": output_layer.name}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def make_closest_facility_analysis_layer(self, params):
        """
        Makes a closest facility network analysis layer and sets its analysis properties.
        """
        try:
            arcpy.CheckOutExtension("Network")
            network_data_source = params.get("network_data_source")
            if network_data_source is None:
                return {"success": False, "error": "network_data_source parameter is required"}
            layer_name = params.get("layer_name")
            if layer_name is None:
                return {"success": False, "error": "layer_name parameter is required"}

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

            result = arcpy.na.MakeClosestFacilityAnalysisLayer(
                network_data_source, layer_name, travel_mode, travel_direction, cutoff, number_of_facilities_to_find,
                time_of_day, time_zone, time_of_day_usage, line_shape, accumulate_attributes,
                generate_directions_on_solve, ignore_invalid_locations
            )

            output_layer = result.getOutput(0)
            self._add_to_map(output_layer.name)
            return {"success": True, "output_layer": output_layer.name, "output_path": output_layer.name}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def make_last_mile_delivery_analysis_layer(self, params):
        """
        Creates a last mile delivery network analysis layer and sets its analysis properties.
        """
        try:
            arcpy.CheckOutExtension("Network")
            network_data_source = params.get("network_data_source")
            if network_data_source is None:
                return {"success": False, "error": "network_data_source parameter is required"}
            layer_name = params.get("layer_name")
            if layer_name is None:
                return {"success": False, "error": "layer_name parameter is required"}

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

            result = arcpy.na.MakeLastMileDeliveryAnalysisLayer(
                network_data_source, layer_name, travel_mode, time_units, distance_units, earliest_route_start_date,
                earliest_route_start_time, max_route_total_time, time_zone_for_time_fields, sequence_gap,
                ignore_invalid_order_locations, line_shape, generate_directions_on_solve
            )

            output_layer = result.getOutput(0)
            self._add_to_map(output_layer.name)
            return {"success": True, "output_layer": output_layer.name, "output_path": output_layer.name}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def make_location_allocation_analysis_layer(self, params):
        """
        Makes a location-allocation network analysis layer and sets its analysis properties.
        """
        try:
            arcpy.CheckOutExtension("Network")
            network_data_source = params.get("network_data_source")
            if network_data_source is None:
                return {"success": False, "error": "network_data_source parameter is required"}
            layer_name = params.get("layer_name")
            if layer_name is None:
                return {"success": False, "error": "layer_name parameter is required"}

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

            result = arcpy.na.MakeLocationAllocationAnalysisLayer(
                network_data_source, layer_name, travel_mode, travel_direction, problem_type, cutoff,
                number_of_facilities_to_find, decay_function_type, decay_function_parameter_value,
                target_market_share, capacity, time_of_day, time_zone, line_shape,
                accumulate_attributes, ignore_invalid_locations
            )

            output_layer = result.getOutput(0)
            self._add_to_map(output_layer.name)
            return {"success": True, "output_layer": output_layer.name, "output_path": output_layer.name}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def make_od_cost_matrix_analysis_layer(self, params):
        """
        Makes an origin destination (OD) cost matrix network analysis layer and sets its analysis properties.
        """
        try:
            arcpy.CheckOutExtension("Network")
            network_data_source = params.get("network_data_source")
            if network_data_source is None:
                return {"success": False, "error": "network_data_source parameter is required"}
            layer_name = params.get("layer_name")
            if layer_name is None:
                return {"success": False, "error": "layer_name parameter is required"}

            travel_mode = params.get("travel_mode")
            cutoff = params.get("cutoff")
            number_of_destinations_to_find = params.get("number_of_destinations_to_find")
            time_of_day = params.get("time_of_day")
            time_zone = params.get("time_zone")
            line_shape = params.get("line_shape")
            accumulate_attributes = params.get("accumulate_attributes")
            ignore_invalid_locations = params.get("ignore_invalid_locations")

            result = arcpy.na.MakeODCostMatrixAnalysisLayer(
                network_data_source, layer_name, travel_mode, cutoff, number_of_destinations_to_find,
                time_of_day, time_zone, line_shape, accumulate_attributes, ignore_invalid_locations
            )

            output_layer = result.getOutput(0)
            self._add_to_map(output_layer.name)
            return {"success": True, "output_layer": output_layer.name, "output_path": output_layer.name}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def copy_network_analysis_layer(self, params):
        """
        Copies a network analysis layer to a duplicate layer.
        """
        try:
            arcpy.CheckOutExtension("Network")
            in_network_analysis_layer = params.get("in_network_analysis_layer")
            if in_network_analysis_layer is None:
                return {"success": False, "error": "in_network_analysis_layer parameter is required"}
            out_layer_name = params.get("out_layer_name")
            if out_layer_name is None:
                return {"success": False, "error": "out_layer_name parameter is required"}

            result = arcpy.na.CopyNetworkAnalysisLayer(in_network_analysis_layer, out_layer_name)

            output_layer = result.getOutput(0)
            self._add_to_map(output_layer.name)
            return {"success": True, "output_layer": output_layer.name, "output_path": output_layer.name}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def copy_traversed_source_features(self, params):
        """
        Creates two feature classes and a table with information about the edges, junctions, and turns that are traversed.
        """
        try:
            arcpy.CheckOutExtension("Network")
            input_network_analysis_layer = params.get("input_network_analysis_layer")
            if input_network_analysis_layer is None:
                return {"success": False, "error": "input_network_analysis_layer parameter is required"}
            output_location = params.get("output_location")
            if output_location is None:
                aprx = arcpy.mp.ArcGISProject("CURRENT")
                output_location = aprx.defaultGeodatabase

            edge_feature_class_name = params.get("edge_feature_class_name")
            if edge_feature_class_name is None:
                edge_feature_class_name = arcpy.CreateUniqueName("TraversedEdges", output_location)

            junction_feature_class_name = params.get("junction_feature_class_name")
            if junction_feature_class_name is None:
                junction_feature_class_name = arcpy.CreateUniqueName("TraversedJunctions", output_location)

            turn_table_name = params.get("turn_table_name")
            if turn_table_name is None:
                turn_table_name = arcpy.CreateUniqueName("TraversedTurns", output_location)

            result = arcpy.na.CopyTraversedSourceFeatures(
                input_network_analysis_layer, output_location, edge_feature_class_name,
                junction_feature_class_name, turn_table_name
            )

            # This tool outputs multiple datasets. We will add them all to the map.
            output_edges = result.getOutput(0)
            output_junctions = result.getOutput(1)

            self._add_to_map(output_edges)
            self._add_to_map(output_junctions)

            return {
                "success": True,
                "output_edges": output_edges,
                "output_junctions": output_junctions,
                "output_turns": result.getOutput(2) # This is a table
            }

        except Exception as e:
            return {"success": False, "error": str(e)}

    def delete_network_analysis_layer(self, params):
        """
        Deletes a network analysis layer and its analysis data.
        """
        try:
            arcpy.CheckOutExtension("Network")
            in_network_analysis_layers = params.get("in_network_analysis_layers")
            if in_network_analysis_layers is None:
                return {"success": False, "error": "in_network_analysis_layers parameter is required"}

            arcpy.na.DeleteNetworkAnalysisLayer(in_network_analysis_layers)

            return {"success": True, "message": f"Successfully deleted {in_network_analysis_layers}."}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def directions(self, params):
        """
        Generates turn-by-turn directions from a network analysis layer with routes.
        """
        try:
            arcpy.CheckOutExtension("Network")
            in_network_analysis_layer = params.get("in_network_analysis_layer")
            if in_network_analysis_layer is None:
                return {"success": False, "error": "in_network_analysis_layer parameter is required"}
            file_type = params.get("file_type")
            if file_type is None:
                return {"success": False, "error": "file_type parameter is required"}
            out_directions_file = params.get("out_directions_file")
            if out_directions_file is None:
                # Create a default output file path
                temp_folder = arcpy.env.scratchFolder
                out_directions_file = os.path.join(temp_folder, "directions.txt")

            report_units = params.get("report_units")
            if report_units is None:
                return {"success": False, "error": "report_units parameter is required"}

            report_time = params.get("report_time")
            time_attribute = params.get("time_attribute")
            language = params.get("language")
            style_name = params.get("style_name")
            stylesheet = params.get("stylesheet")

            result = arcpy.na.Directions(
                in_network_analysis_layer, file_type, out_directions_file, report_units,
                report_time, time_attribute, language, style_name, stylesheet
            )

            # This tool outputs a file, not a layer.
            return {"success": True, "output_file": result.getOutput(0)}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def add_locations(self, params):
        """
        Adds input features or records to a network analysis layer.
        """
        try:
            arcpy.CheckOutExtension("Network")
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
            search_criteria = params.get("search_criteriasource_snaptype") # Corrected param name
            match_type = params.get("match_type")
            append = params.get("append")
            snap_to_position_along_network = params.get("snap_to_position_along_network")
            snap_offset = params.get("snap_offset")
            exclude_restricted_elements = params.get("exclude_restricted_elements")
            search_query = params.get("search_querysource_expression") # Corrected param name
            allow_auto_relocate = params.get("allow_auto_relocate")

            result = arcpy.na.AddLocations(
                in_network_analysis_layer, sub_layer, in_table, field_mappings, search_tolerance,
                sort_field, search_criteria, match_type, append, snap_to_position_along_network,
                snap_offset, exclude_restricted_elements, search_query, allow_auto_relocate
            )

            output_layer = result.getOutput(0)
            return {"success": True, "output_layer": output_layer, "output_path": output_layer}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def add_fleet_routing_breaks(self, params):
        """
        Creates breaks in a Vehicle Routing Problem (VRP) layer.
        """
        try:
            arcpy.CheckOutExtension("Network")
            in_vrp_layer = params.get("in_vrp_layer")
            if in_vrp_layer is None:
                return {"success": False, "error": "in_vrp_layer parameter is required"}

            target_route = params.get("target_route")
            break_type = params.get("break_type")
            time_window_properties = params.get("time_window_properties")
            travel_time_properties = params.get("travel_time_properties")
            work_time_properties = params.get("work_time_properties")
            append_to_existing_breaks = params.get("append_to_existing_breaks")

            result = arcpy.na.AddFleetRoutingBreaks(
                in_vrp_layer, target_route, break_type, time_window_properties,
                travel_time_properties, work_time_properties, append_to_existing_breaks
            )

            output_layer = result.getOutput(0)
            return {"success": True, "output_layer": output_layer, "output_path": output_layer}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def add_fleet_routing_routes(self, params):
        """
        Creates routes in a vehicle routing problem, last mile delivery, or waste collection analysis layer.
        """
        try:
            arcpy.CheckOutExtension("Network")
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

            result = arcpy.na.AddFleetRoutingRoutes(
                in_vrp_layer, number_of_routes, route_name_prefix, start_depot_name, end_depot_name,
                earliest_start_time, latest_start_time, max_order_count, capacities, route_constraints,
                costs, additional_route_time, append_to_existing_routes, date_and_time, waste_capacities,
                start_time, route_time_distance_constraints, depot_service_time
            )

            output_layer = result.getOutput(0)
            return {"success": True, "output_layer": output_layer, "output_path": output_layer}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def calculate_locations(self, params):
        """
        Locates input features on a network and adds fields to the input features that describe the network locations.
        """
        try:
            arcpy.CheckOutExtension("Network")
            in_point_features = params.get("in_point_features")
            if in_point_features is None:
                return {"success": False, "error": "in_point_features parameter is required"}
            in_network_dataset = params.get("in_network_dataset")
            if in_network_dataset is None:
                return {"success": False, "error": "in_network_dataset parameter is required"}

            search_tolerance = params.get("search_tolerance")
            search_criteria = params.get("search_criteriasource_snaptype") # Corrected
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
            search_query = params.get("search_querysource_expression") # Corrected
            travel_mode = params.get("travel_mode")

            # This tool modifies the input features in-place.
            arcpy.na.CalculateLocations(
                in_point_features, in_network_dataset, search_tolerance, search_criteria, match_type,
                source_id_field, source_oid_field, position_field, side_field, snap_x_field, snap_y_field,
                distance_field, snap_z_field, location_field, exclude_restricted_elements, search_query, travel_mode
            )

            return {"success": True, "output_layer": in_point_features, "output_path": in_point_features}

        except Exception as e:
            return {"success": False, "error": str(e)}