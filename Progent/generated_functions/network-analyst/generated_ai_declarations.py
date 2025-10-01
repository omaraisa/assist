# Generated ArcGIS Pro network-analyst AI Function Declarations
# Generated on 2025-10-01T14:55:06.013049
# Total tools: 34

functions_declarations = {
    "add_field_to_analysis_layer": {
        "name": "add_field_to_analysis_layer",
        "description": "Adds a field to a sublayer of a network analysis layer.",
        "parameters": {
                "in_network_analysis_layer": {
                        "type": "string",
                        "description": "The network analysis layer to which the new field will be added."
                },
                "sub_layer": {
                        "type": "string",
                        "description": "The sublayer of the network analysis layer to which the new field will be added."
                },
                "field_name": {
                        "type": "string",
                        "description": "The name of the field that will be added to the specified sublayer of the network analysis layer."
                },
                "field_type": {
                        "type": "string",
                        "description": "Specifies the field type that will be used in the creation of the new field.LONG\u2014The field type will be long. Long fields support whole numbers between -2,147,483,648 and 2,147,483,647.TEXT\u2014The field ..."
                },
                "field_precision": {
                        "type": "string",
                        "description": "Legacy:This parameter is deprecated and maintained only for backward compatibility.",
                        "default": None
                },
                "field_scale": {
                        "type": "string",
                        "description": "Legacy:This parameter is deprecated and maintained only for backward compatibility.",
                        "default": None
                },
                "field_length": {
                        "type": "string",
                        "description": "The length of the field. This sets the maximum number of allowable characters for each record of the field. If no field length is provided, a length of 255 will be used.The field length applies only t...",
                        "default": None
                },
                "field_alias": {
                        "type": "string",
                        "description": "The alternate name for the field. This name is used to describe cryptic field names. This parameter only applies to geodatabases.",
                        "default": None
                },
                "field_is_Noneable": {
                        "type": "string",
                        "description": "Specifies whether the field can contain None values. Null values are different from zero or empty fields and are only supported for fields in a geodatabase.NULLABLE\u2014The field can contain None values. ...",
                        "default": None
                }
        },
        "required": [
                "in_network_analysis_layer",
                "sub_layer",
                "field_name",
                "field_type"
        ]
},
    "add_locations": {
        "name": "add_locations",
        "description": "Adds input features or records to a network analysis layer. The inputs are added to specific sublayers such as stops and barriers. When the network analysis layer references a network dataset as its network data source, the tool calculates the network locations of the inputs, unless precalculated network location fields are mapped from the inputs. Learn more about how the Add Locations tool locates analysis  inputs on the network",
        "parameters": {
                "in_network_analysis_layer": {
                        "type": "string",
                        "description": "The network analysis layer to which the network analysis objects will be added."
                },
                "sub_layer": {
                        "type": "string",
                        "description": "The name of the sublayer of the network analysis layer to which the network analysis objects will be added."
                },
                "in_table": {
                        "type": "string",
                        "description": "The feature class or table containing the locations to be added to the network analysis sublayer."
                },
                "field_mappings": {
                        "type": "string",
                        "description": "The mapping between the input fields of the network analysis sublayer to which locations will be added  and the fields in the input data or specified constants.Input sublayers of network analysis laye...",
                        "default": None
                },
                "search_tolerance": {
                        "type": "string",
                        "description": "The maximum search distance that will be used when locating the input features on the network. Features that are outside the search tolerance will be left unlocated. The parameter includes a value and...",
                        "default": None
                },
                "sort_field": {
                        "type": "string",
                        "description": "The field on which the network analysis objects will be sorted as they are added to the network analysis layer. The default is the ObjectID field in the input feature class or table.",
                        "default": None
                },
                "search_criteriasource_snaptype": {
                        "type": "string",
                        "description": "The edge and junction sources in the network dataset that will be searched when locating inputs on the network. For example, if the network dataset references separate feature classes representing str...",
                        "default": None
                },
                "match_type": {
                        "type": "string",
                        "description": "Legacy:This parameter is deprecated and maintained only for backward compatibility. Inputs will always be matched to the closest network source among all the sources used for locating, corresponding t...",
                        "default": None
                },
                "append": {
                        "type": "string",
                        "description": "Specifies whether new network analysis objects will be appended to existing objects.\r\nAPPEND\u2014The new network analysis objects will be appended to the existing set of objects in the selected sublayer. ...",
                        "default": None
                },
                "snap_to_position_along_network": {
                        "type": "string",
                        "description": "Specifies whether the inputs will be snapped to their calculated  network locations or represented at their original geographic location.To use curb approach in the analysis to control which side of t...",
                        "default": None
                },
                "snap_offset": {
                        "type": "string",
                        "description": "An offset distance that will be applied when snapping a point to the network. An offset distance of zero means the point will be coincident with the network feature (typically a line). To offset the p...",
                        "default": None
                },
                "exclude_restricted_elements": {
                        "type": "string",
                        "description": "Legacy:This parameter is deprecated and maintained only for backward compatibility. Analysis inputs will never be located on network elements that are restricted, corresponding to a parameter value of...",
                        "default": None
                },
                "search_querysource_expression": {
                        "type": "string",
                        "description": "A query that restricts the search to a subset of the features within a source feature class. This is useful if you don't want to find features that may be unsuited for a network location. For example,...",
                        "default": None
                },
                "allow_auto_relocate": {
                        "type": "string",
                        "description": "Specifies whether inputs with existing network location fields can be automatically relocated at solve time to ensure valid, routable location fields for the analysis.\r\n\r\nALLOW\u2014 Points located on rest...",
                        "default": None
                }
        },
        "required": [
                "in_network_analysis_layer",
                "sub_layer",
                "in_table"
        ]
},
    "add_fleet_routing_breaks": {
        "name": "add_fleet_routing_breaks",
        "description": "Creates breaks in a Vehicle Routing Problem (VRP) layer.",
        "parameters": {
                "in_vrp_layer": {
                        "type": "string",
                        "description": "The vehicle routing problem analysis layer to which the breaks will be added."
                },
                "target_route": {
                        "type": "string",
                        "description": "The route the breaks will apply to. \u202fIf this parameter is not specified, breaks will be created for\r\neach existing route.",
                        "default": None
                },
                "break_type": {
                        "type": "string",
                        "description": "Specifies the type of breaks that will be added.TIME_WINDOW_BREAK\u2014 Breaks will take place during a specific time window. This is the default.MAXIMUM_TRAVEL_TIME_BREAK\u2014 Breaks will take place after a c...",
                        "default": None
                },
                "time_window_properties": {
                        "type": "string",
                        "description": "Specifies a time range within which the break will begin. To set up a time window break, use two time-of-day values.The properties below are enabled when the Break Type parameter is set to Time Window...",
                        "default": None
                },
                "travel_time_properties": {
                        "type": "string",
                        "description": "Specifies how long a person can travel before the break is required.\r\nThe properties below are enabled when the Break Type parameter is set to Maximum Travel Time Break.Is Paid\u2014A Boolean value indicat...",
                        "default": None
                },
                "work_time_properties": {
                        "type": "string",
                        "description": "Specifies how long a person can work before a break is required.\r\nThe properties below are enabled when the Break Type parameter is set to Maximum Work Time Break.Is Paid\u2014A Boolean value indicating wh...",
                        "default": None
                },
                "append_to_existing_breaks": {
                        "type": "string",
                        "description": "Specifies whether new breaks will be appended to the existing breaks attribute table.APPEND\u2014New breaks will be\r\nappended to the existing set in the breaks attribute\r\ntable. This is the default.CLEAR\u2014E...",
                        "default": None
                }
        },
        "required": [
                "in_vrp_layer"
        ]
},
    "add_fleet_routing_routes": {
        "name": "add_fleet_routing_routes",
        "description": "Creates routes in a vehicle routing problem, last mile delivery, or waste collection analysis layer. This tool will append rows to the Routes sublayer and can add rows with specific settings while creating a unique name field.",
        "parameters": {
                "in_vrp_layer": {
                        "type": "string",
                        "description": "The \u202fvehicle routing problem, last mile delivery, or waste collection analysis layer to which routes will be added."
                },
                "number_of_routes": {
                        "type": "string",
                        "description": "The number of routes that will be added.",
                        "default": None
                },
                "route_name_prefix": {
                        "type": "string",
                        "description": "A qualifier that will be added to the name of every route. For example, a route name prefix of WeekdayRoute would be used as the starting text for every route\u2019s name with an incrementing numerical suf...",
                        "default": None
                },
                "start_depot_name": {
                        "type": "string",
                        "description": "The name of the starting depot for the route.If this value is None, the route will begin from the first order assigned. Omitting the start depot is useful when the vehicle's starting location is unkno...",
                        "default": None
                },
                "end_depot_name": {
                        "type": "string",
                        "description": "The name of the ending depot for the route.If this value is None, the route will end at the last order assigned.For vehicle routing problem layers, when this value is None, the start_depot_name parame...",
                        "default": None
                },
                "earliest_start_time": {
                        "type": "string",
                        "description": "The earliest allowable start time for the route in a vehicle routing problem layer.This parameter is used by the solver in conjunction with the time window of the starting depot provided in the Depots...",
                        "default": None
                },
                "latest_start_time": {
                        "type": "string",
                        "description": "The latest allowable start time for the route in a vehicle routing problem layer.This parameter has a default time-only value of 10:00:00 a.m., which is interpreted as 10:00:00 a.m. on the date provid...",
                        "default": None
                },
                "max_order_count": {
                        "type": "string",
                        "description": "The maximum allowable number of orders on the route. The default value is 30 for vehicle routing problem layers and None for last mile delivery layers. If no value is specified, the default value is u...",
                        "default": None
                },
                "capacities": {
                        "type": "string",
                        "description": "The maximum amount (volume, weight, quantity, and so on) that can be carried by the vehicle. A\r\nNone value is the same as zero.  A maximum of nine\r\ncapacity fields are allowed, but use only the number...",
                        "default": None
                },
                "route_constraints": {
                        "type": "string",
                        "description": "The constraints that will be placed on routes to limit total time, total travel time, and total distance.Max Total Time\u2014The maximum allowable route duration. The route duration includes travel times a...",
                        "default": None
                },
                "costs": {
                        "type": "string",
                        "description": "The costs that may be incurred by the route in a solution.Fixed Cost\u2014A fixed monetary cost that is incurred only if the route is used in a solution (that is, it has orders assigned to it).  Cost Per U...",
                        "default": None
                },
                "additional_route_time": {
                        "type": "string",
                        "description": "Additional route time options.Start Depot Service Time\u2014The service time at the starting depot. This can be used to model the time spent loading the vehicle.  End Depot Service Time\u2014The service time at...",
                        "default": None
                },
                "append_to_existing_routes": {
                        "type": "string",
                        "description": "Specifies whether new routes will be appended to the existing routes attribute table.APPEND\u2014New routes will be\r\nappended to the existing set in the routes attribute\r\ntable. This is the default.CLEAR\u2014E...",
                        "default": None
                },
                "date_and_time": {
                        "type": "string",
                        "description": "Additional date and time properties for a last mile delivery layer. Earliest Route Start Date\u2014The earliest start date for added routes. If this property is not specified, the routes will use the layer...",
                        "default": None
                },
                "waste_capacities": {
                        "type": "string",
                        "description": "The capacities for routes in a waste collection layer. MaxBins_1\u2014The maximum number of waste bins for fraction 1 that the vehicle can collect before it must be emptied.MaxWeight_1\u2014The maximum physical...",
                        "default": None
                },
                "start_time": {
                        "type": "string",
                        "description": "Additional date and time properties for a waste collection layer. Start Time\u2014The starting time for the route.  If this property is not specified, the routes will use the layer's default start time. Ov...",
                        "default": None
                },
                "route_time_distance_constraints": {
                        "type": "string",
                        "description": "The constraints that will be placed on routes to limit total time and distance.Max Total Time\u2014The maximum allowable route duration. The route duration includes travel times as well as service and wait...",
                        "default": None
                },
                "depot_service_time": {
                        "type": "string",
                        "description": "Additional route time properties.Start Depot Service Time\u2014The service time at the starting depot. This can be used to model the time spent loading the vehicle.  End Depot Service Time\u2014The service time...",
                        "default": None
                }
        },
        "required": [
                "in_vrp_layer"
        ]
},
    "calculate_locations": {
        "name": "calculate_locations",
        "description": "Locates input features on a network and adds fields  to the input features that describe the network locations. The tool is used to precalculate the network locations of inputs that will be used in a Network Analyst workflow, improving performance of the analysis at solve time.  The tool stores the calculated network locations of the inputs in fields in the input data. Learn more about locating features on a network Learn more about precalculating network locations",
        "parameters": {
                "in_point_features": {
                        "type": "string",
                        "description": "The input features for which the network locations will be calculated.  For line and polygon features, since the network location information is stored in a BLOB field, only geodatabase feature classe..."
                },
                "in_network_dataset": {
                        "type": "string",
                        "description": "The network dataset that will be used to calculate the locations.\r\nThis parameter is required unless a sublayer of a network analysis layer is used as input features. In that case, don't specify a val...",
                        "default": None
                },
                "search_tolerance": {
                        "type": "string",
                        "description": "The maximum search distance that will be used when locating the input features on the network. Features that are outside the search tolerance will be left unlocated. The parameter includes a value and...",
                        "default": None
                },
                "search_criteriasource_snaptype": {
                        "type": "string",
                        "description": "The edge and junction sources in the network dataset that will be searched when locating inputs on the network. For example, if the network dataset references separate feature classes representing str...",
                        "default": None
                },
                "match_type": {
                        "type": "string",
                        "description": "Legacy:This parameter is deprecated and maintained only for backward compatibility. Inputs will always be matched to the closest network source among all the sources used for locating, corresponding t...",
                        "default": None
                },
                "source_id_field": {
                        "type": "string",
                        "description": "The name of the field to be created or updated that will be populated with the  ID of the network dataset source feature class  for the input feature's computed network location. The default value is ...",
                        "default": None
                },
                "source_oid_field": {
                        "type": "string",
                        "description": "The name of the field to be created or updated that will be populated with  the ObjectID field value of the network dataset source feature class for the input feature's  computed network location. The...",
                        "default": None
                },
                "position_field": {
                        "type": "string",
                        "description": "The name of the field to be created or updated describing the computed network location's percent along the network element where it was located. The default value is PosAlong.The parameter is not use...",
                        "default": None
                },
                "side_field": {
                        "type": "string",
                        "description": "The name of the field to be created or updated describing the side of the  network edge where the computed network location is located. The default value is  SideOfEdge.The parameter is not used when ...",
                        "default": None
                },
                "snap_x_field": {
                        "type": "string",
                        "description": "The name of the field to be created or updated with the x-coordinate of the computed network location. The default value is SnapX.The parameter is not used when calculating locations for line or polyg...",
                        "default": None
                },
                "snap_y_field": {
                        "type": "string",
                        "description": "The name of the field to be created or updated with the y-coordinate of the computed network location. The default value is SnapY.The parameter is not used when calculating locations for line or polyg...",
                        "default": None
                },
                "distance_field": {
                        "type": "string",
                        "description": "The name of the field to be created or updated describing the distance in meters of the original point feature from its computed network location. The default value is  DistanceToNetworkInMeters.The p...",
                        "default": None
                },
                "snap_z_field": {
                        "type": "string",
                        "description": "The name of the field to be created or updated with the z-coordinate of the computed network location. The default value is SnapZ.The parameter is used only when the input network dataset supports con...",
                        "default": None
                },
                "location_field": {
                        "type": "string",
                        "description": "The name of the field to be created or updated with the location ranges of the computed network locations for line or polygon features. The default value is Locations. The parameter is used only when ...",
                        "default": None
                },
                "exclude_restricted_elements": {
                        "type": "string",
                        "description": "Legacy:This parameter is deprecated and maintained only for backward compatibility. Analysis inputs will never be located on network elements that are restricted, corresponding to a parameter value of...",
                        "default": None
                },
                "search_querysource_expression": {
                        "type": "string",
                        "description": "A query that restricts the search to a subset of the features within a source feature class. This is useful if you don't want to find features that may be unsuited for a network location. For example,...",
                        "default": None
                },
                "travel_mode": {
                        "type": "string",
                        "description": "The name of the travel mode that will be used.If you specify a travel mode, the travel mode settings, such as\r\nrestrictions and impedance attributes, will be considered when\r\ncalculating network locat...",
                        "default": None
                }
        },
        "required": [
                "in_point_features"
        ]
},
    "copy_network_analysis_layer": {
        "name": "copy_network_analysis_layer",
        "description": "Copies a network analysis layer \r\nto a duplicate layer. The new layer will have the same analysis settings and network data source as the original layer and a copy of the original layer's analysis data.",
        "parameters": {
                "in_network_analysis_layer": {
                        "type": "string",
                        "description": "The network analysis layer to copy."
                },
                "out_layer_name": {
                        "type": "string",
                        "description": "The name of the network analysis layer that will be created.",
                        "default": None
                }
        },
        "required": [
                "in_network_analysis_layer"
        ]
},
    "copy_traversed_source_features": {
        "name": "copy_traversed_source_features",
        "description": "Creates two feature classes and a table, which together contain information about the edges, junctions, and turns that are traversed while solving a network analysis layer. Learn about the output from Copy Traversed Source Features",
        "parameters": {
                "input_network_analysis_layer": {
                        "type": "string",
                        "description": "The network analysis layer from which traversed source features will be copied. If the network analysis layer does not have a valid result, the layer will be solved to produce one."
                },
                "output_location": {
                        "type": "string",
                        "description": "The workspace where the output table and two feature classes will be saved."
                },
                "edge_feature_class_name": {
                        "type": "string",
                        "description": "The name of the feature class that will contain information about the traversed edge source features. If the solved network analysis layer doesn't traverse any edge features, an empty feature class wi..."
                },
                "junction_feature_class_name": {
                        "type": "string",
                        "description": "The name of the feature class that will contain information about the traversed junction source features, including system junctions and relevant points from the input network analysis layer. If the s..."
                },
                "turn_table_name": {
                        "type": "string",
                        "description": "The name of the table that will contain information about the traversed global turns and turn features that scale cost for the underlying edges. If the solved network analysis layer doesn't traverse a..."
                }
        },
        "required": [
                "input_network_analysis_layer",
                "output_location",
                "edge_feature_class_name",
                "junction_feature_class_name",
                "turn_table_name"
        ]
},
    "delete_network_analysis_layer": {
        "name": "delete_network_analysis_layer",
        "description": "Deletes a network analysis layer and its analysis data.",
        "parameters": {
                "in_network_analysis_layers": {
                        "type": "string",
                        "description": "The network analysis layer or layers to delete."
                }
        },
        "required": [
                "in_network_analysis_layers"
        ]
},
    "directions": {
        "name": "directions",
        "description": "Generates turn-by-turn directions from a network analysis layer with routes. The directions can be written to a file in text, XML, or HTML format. If you provide an appropriate style sheet, the directions can be written to any other file format.",
        "parameters": {
                "in_network_analysis_layer": {
                        "type": "string",
                        "description": "The network analysis layer for which directions will be generated. Directions can be generated only for route, closest facility, and vehicle routing problem network analysis layers.Caution:This tool d..."
                },
                "file_type": {
                        "type": "string",
                        "description": "Specifies the format that will be used for the output directions file. This parameter is ignored if the style sheet parameter has a value.XML\u2014The output directions file will be generated as an .xml fi..."
                },
                "out_directions_file": {
                        "type": "string",
                        "description": "If you provide a style sheet for the stylesheet parameter, ensure that the file suffix for the out_directions_file value matches the file type the style sheet produces."
                },
                "report_units": {
                        "type": "string",
                        "description": "Specifies the linear units that will be used in the directions file. For example, even if the impedance attribute has units of meters, you can show directions in miles. \r\n\r\n\r\nFeet\u2014The linear units wil..."
                },
                "report_time": {
                        "type": "string",
                        "description": "Specifies whether travel time will be reported in the directions file.NO_REPORT_TIME\u2014Travel time will not be reported in the directions file. REPORT_TIME\u2014Travel time will be reported in the directions...",
                        "default": None
                },
                "time_attribute": {
                        "type": "string",
                        "description": "The time-based cost attribute that will be used to provide travel times in the directions. The cost attribute must exist on the network dataset used by the input network analysis layer. For vehicle ro...",
                        "default": None
                },
                "language": {
                        "type": "string",
                        "description": "The language that will be used for driving directions.Use a two- or five-character language code representing one of the available languages for directions generation for this parameter value. In Pyth...",
                        "default": None
                },
                "style_name": {
                        "type": "string",
                        "description": "Specifies the formatting style that will be used for directions.NA Desktop\u2014Printable turn-by-turn directions will be used.NA Navigation\u2014Turn-by-turn directions designed for an in-vehicle navigation de...",
                        "default": None
                },
                "stylesheet": {
                        "type": "string",
                        "description": "The style sheet\r\nthat will be used for generating a formatted output file type (such as PDF, Word, or HTML). The suffix of the file in the output directions file parameter must match the file type tha...",
                        "default": None
                }
        },
        "required": [
                "in_network_analysis_layer",
                "file_type",
                "out_directions_file",
                "report_units"
        ]
},
    "make_closest_facility_analysis_layer": {
        "name": "make_closest_facility_analysis_layer",
        "description": "Makes a closest facility network analysis layer and sets its analysis properties. A closest facility analysis layer is useful in determining the closest facility or facilities to an incident based on a specified travel mode. The layer can be created using a local network dataset or a service hosted online or in a portal.",
        "parameters": {
                "network_data_source": {
                        "type": "string",
                        "description": "The network dataset or service on which the network analysis will be performed.The parameter can be specified using one of the following:The catalog path to the network datasetA network dataset layer ..."
                },
                "layer_name": {
                        "type": "string",
                        "description": "The name of the network analysis layer that will be created.",
                        "default": None
                },
                "travel_mode": {
                        "type": "string",
                        "description": "The name of the travel mode that will be used in the analysis. The travel mode represents a collection of network settings, such as travel restrictions and U-turn policies, that determine how a pedest...",
                        "default": None
                },
                "travel_direction": {
                        "type": "string",
                        "description": "Specifies the direction of travel between facilities and incidents.\r\nTO_FACILITIES\u2014Direction of travel is  from incidents to facilities. Retail stores commonly use this setting, since they are concern...",
                        "default": None
                },
                "cutoff": {
                        "type": "string",
                        "description": "The  impedance value at which to stop searching for facilities for a given incident in the units of the impedance attribute used by the travel_mode value. This cutoff can be overridden on a per-incide...",
                        "default": None
                },
                "number_of_facilities_to_find": {
                        "type": "string",
                        "description": "The number of closest facilities to find per incident. This default can be overridden by specifying an individual value for the TargetFacilityCount  property in the incidents sublayer.\r\n The default n...",
                        "default": None
                },
                "time_of_day": {
                        "type": "string",
                        "description": "The time and date at which the routes will begin or end. \r\n The interpretation of this value  depends on whether time_of_day_usage is set to be the start time or the end time of the route.\r\nIf you cho...",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "Specifies the time zone for the time_of_day parameter.\r\nLOCAL_TIME_AT_LOCATIONS\u2014The time_of_day parameter refers to the time zone in which the facilities or incidents are located. This is the default....",
                        "default": None
                },
                "time_of_day_usage": {
                        "type": "string",
                        "description": "Specifies whether the value of the time_of_day parameter represents the arrival or departure time for the route or routes.START_TIME\u2014The time_of_day parameter value is interpreted as the departure tim...",
                        "default": None
                },
                "line_shape": {
                        "type": "string",
                        "description": "Specifies the shape type that will be used for the route features that are output by the analysis.\r\nRegardless of the output shape type specified, the best route is always determined by the network im...",
                        "default": None
                },
                "accumulate_attributes": {
                        "type": "string",
                        "description": "A list of cost attributes to be accumulated during analysis. These accumulated attributes are for reference only; the solver only uses the cost attribute used by the designated travel mode when solvin...",
                        "default": None
                },
                "generate_directions_on_solve": {
                        "type": "string",
                        "description": "Specifies whether directions will be generated when running the analysis.DIRECTIONS\u2014Turn-by-turn directions will be generated on solve.NO_DIRECTIONS\u2014Turn-by-turn directions will not be generated on so...",
                        "default": None
                },
                "ignore_invalid_locations": {
                        "type": "string",
                        "description": "Specifies whether invalid input locations will be ignored. Typically, locations are invalid if they cannot be located on the network. When invalid locations are ignored, the solver will skip them and ...",
                        "default": None
                }
        },
        "required": [
                "network_data_source"
        ]
},
    "make_last_mile_delivery_analysis_layer": {
        "name": "make_last_mile_delivery_analysis_layer",
        "description": "Creates a last mile delivery network analysis layer and sets its analysis properties. A last mile delivery analysis layer is useful for optimizing a set of routes using a fleet of vehicles. The layer can be created using a local network dataset or a service hosted online or in a portal.",
        "parameters": {
                "network_data_source": {
                        "type": "string",
                        "description": "The network dataset or service on which the network analysis will be performed.\t\t\t\t\tThe network must have at least one travel mode, one cost attribute with time units, and one cost attribute with dist..."
                },
                "layer_name": {
                        "type": "string",
                        "description": "The name of the network analysis layer that will be created.",
                        "default": None
                },
                "travel_mode": {
                        "type": "string",
                        "description": "The name of the travel mode that will be used in the analysis. The travel mode represents a collection of network settings, such as travel restrictions and U-turn policies, that determine how a pedest...",
                        "default": None
                },
                "time_units": {
                        "type": "string",
                        "description": "Specifies the time units that will be used by the analysis layer's properties and the temporal fields of the analysis layer's sublayers and tables (network analysis classes). This value does not need ...",
                        "default": None
                },
                "distance_units": {
                        "type": "string",
                        "description": "Specifies the distance units that will be used by the analysis layer's properties and the distance fields of the analysis layer's sublayers and tables (network analysis classes). This value does not n...",
                        "default": None
                },
                "earliest_route_start_date": {
                        "type": "string",
                        "description": "The default earliest start date for \r\nroutes.  This date is used for all routes for which the EarliestStartDate field in the Routes sublayer is None. When no parameter value is specified, all rows in ...",
                        "default": None
                },
                "earliest_route_start_time": {
                        "type": "string",
                        "description": "The default earliest start time for \r\nroutes.  This time of day is used for all routes for which the EarliestStartTime field in the Routes sublayer is None. When no parameter value is specified, all r...",
                        "default": None
                },
                "max_route_total_time": {
                        "type": "string",
                        "description": "The maximum allowed total time for each route. The value can be any positive number.The value is used for all routes for which the MaxTotalTime field in the Routes sublayer is None. When no parameter ...",
                        "default": None
                },
                "time_zone_for_time_fields": {
                        "type": "string",
                        "description": "Specifies the time zone that will be used for the input date-time fields supported by the tool. LOCAL_TIME_AT_LOCATIONS\u2014  The date-time values associated with the orders or depots will be in the time ...",
                        "default": None
                },
                "sequence_gap": {
                        "type": "string",
                        "description": "The gap in numerical values to leave in the Sequence field in the Orders sublayer between adjacent orders when the analysis is solved.  The value acts as a multiplier for the actual sequence of orders...",
                        "default": None
                },
                "ignore_invalid_order_locations": {
                        "type": "string",
                        "description": "Specifies whether invalid order locations will be ignored.\r\nSKIP\u2014Invalid order locations will be ignored so that the analysis will succeed using only valid locations.HALT\u2014Invalid order locations will ...",
                        "default": None
                },
                "line_shape": {
                        "type": "string",
                        "description": "Specifies the shape type that will be used for the route features that are output by the analysis.\r\nALONG_NETWORK\u2014The output routes will have the exact shape of the underlying network sources. The out...",
                        "default": None
                },
                "generate_directions_on_solve": {
                        "type": "string",
                        "description": "Specifies whether directions will be generated when the analysis is solved.DIRECTIONS\u2014Turn-by-turn directions will be generated on solve.NO_DIRECTIONS\u2014Turn-by-turn directions will not be generated on ...",
                        "default": None
                }
        },
        "required": [
                "network_data_source"
        ]
},
    "make_location_allocation_analysis_layer": {
        "name": "make_location_allocation_analysis_layer",
        "description": "Makes a location-allocation network analysis layer and sets its analysis properties. A location-allocation analysis layer is useful for choosing a given number of facilities from a set of potential locations so that a demand will be allocated to facilities in an optimal and efficient manner. The layer can be created using a local network dataset or a service hosted online or in a portal.",
        "parameters": {
                "network_data_source": {
                        "type": "string",
                        "description": "The network dataset or service on which the network analysis will be performed.The parameter can be specified using one of the following:The catalog path to the network datasetA network dataset layer ..."
                },
                "layer_name": {
                        "type": "string",
                        "description": "The name of the network analysis layer that will be created.",
                        "default": None
                },
                "travel_mode": {
                        "type": "string",
                        "description": "The name of the travel mode that will be used in the analysis. The travel mode represents a collection of network settings, such as travel restrictions and U-turn policies, that determine how a pedest...",
                        "default": None
                },
                "travel_direction": {
                        "type": "string",
                        "description": "Specifies the direction of travel between facilities and demand points when calculating the network costs.FROM_FACILITIES\u2014Direction of travel is from facilities to demand points. This is the default. ...",
                        "default": None
                },
                "problem_type": {
                        "type": "string",
                        "description": "The problem type that will be solved. The choice of the problem type depends on the kind of facility being located. Different kinds of facilities have different priorities and constraints.MINIMIZE_IMP...",
                        "default": None
                },
                "cutoff": {
                        "type": "string",
                        "description": "The maximum impedance at which a demand point can be allocated to a facility in the units of the impedance attribute used by the specified Travel Mode value. The maximum impedance is measured by the l...",
                        "default": None
                },
                "number_of_facilities_to_find": {
                        "type": "string",
                        "description": "The number of facilities that the solver will locate.  The default value is  1.The facilities with a FacilityType value of Required are always part of the solution when there are more facilities to fi...",
                        "default": None
                },
                "decay_function_type": {
                        "type": "string",
                        "description": "The equation that will be used for transforming the network cost between facilities and demand points. This parameter, along with the Decay Function Parameter Value parameter, specifies how severely t...",
                        "default": None
                },
                "decay_function_parameter_value": {
                        "type": "string",
                        "description": "A parameter value for the equations specified in the decay_function_type parameter. This parameter value is ignored when the decay_function_type parameter is set to LINEAR. For the POWER and EXPONENTI...",
                        "default": None
                },
                "target_market_share": {
                        "type": "string",
                        "description": "The target market share, as a percentage, to solve for when the problem_type parameter is set to TARGET_MARKET_SHARE. It is the percentage of the total demand weight that you want the solution facilit...",
                        "default": None
                },
                "capacity": {
                        "type": "string",
                        "description": "The default capacity of facilities when the problem_type parameter is set to MAXIMIZE_CAPACITATED_COVERAGE. This parameter is ignored for all other problem types.\r\nFacilities have a Capacity property,...",
                        "default": None
                },
                "time_of_day": {
                        "type": "string",
                        "description": "The time and date of  departure. The departure time can be  from facilities or demand points, depending on whether travel_direction is  set to TO_FACILITIES or FROM_FACILITIES.\r\nIf you chose a traffic...",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "The time zone of the Time of Day parameter.\r\nLOCAL_TIME_AT_LOCATIONS\u2014The time of day parameter refers to the time zone in which the facilities or demand points are located. If the travel direction is ...",
                        "default": None
                },
                "line_shape": {
                        "type": "string",
                        "description": "Specifies the output line shape.NO_LINES\u2014No shape will be generated for the output of the analysis. This is useful if you are solving a very large problem and are interested only in a solution table a...",
                        "default": None
                },
                "accumulate_attributes": {
                        "type": "string",
                        "description": "A list of cost attributes to be accumulated during analysis. These accumulated attributes are for reference only; the solver only uses the cost attribute used by the designated travel mode when solvin...",
                        "default": None
                },
                "ignore_invalid_locations": {
                        "type": "string",
                        "description": "Specifies whether invalid input locations will be ignored. Typically, locations are invalid if they cannot be located on the network. When invalid locations are ignored, the solver will skip them and ...",
                        "default": None
                }
        },
        "required": [
                "network_data_source"
        ]
},
    "make_od_cost_matrix_analysis_layer": {
        "name": "make_od_cost_matrix_analysis_layer",
        "description": "Makes an origin destination (OD) cost matrix network analysis layer and sets its analysis properties. An OD cost matrix analysis layer is useful for representing a matrix of costs going from a set of origin locations to a set of destination locations. The layer can be created using a local network dataset or a service hosted online or in a portal.",
        "parameters": {
                "network_data_source": {
                        "type": "string",
                        "description": "The network dataset or service on which the network analysis will be performed.The parameter can be specified using one of the following:The catalog path to the network datasetA network dataset layer ..."
                },
                "layer_name": {
                        "type": "string",
                        "description": "The name of the network analysis layer that will be created.",
                        "default": None
                },
                "travel_mode": {
                        "type": "string",
                        "description": "The name of the travel mode that will be used in the analysis. The travel mode represents a collection of network settings, such as travel restrictions and U-turn policies, that determine how a pedest...",
                        "default": None
                },
                "cutoff": {
                        "type": "string",
                        "description": "The  impedance value at which to stop searching for destinations for a given origin. This value will be in the units of the impedance attribute used by the chosen travel mode.  No destinations beyond ...",
                        "default": None
                },
                "number_of_destinations_to_find": {
                        "type": "string",
                        "description": "The number of destinations to find per origin. The default can be overridden by specifying an individual value for the TargetDestinationCount property in the origins sublayer.\r\n By default, no limit i...",
                        "default": None
                },
                "time_of_day": {
                        "type": "string",
                        "description": "The departure time from origins.\r\nIf you chose a traffic-based impedance attribute, the solution will be generated given dynamic traffic conditions at the time of day specified here. A date and time c...",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "The time zone of the Time of Day parameter.\r\nLOCAL_TIME_AT_LOCATIONS\u2014The Time of Day parameter refers to the time zone in which the origins are located. This is the default.  UTC\u2014The Time of Day param...",
                        "default": None
                },
                "line_shape": {
                        "type": "string",
                        "description": "Specifies the output line shape.NO_LINES\u2014No shape will be generated for the output origin-destination route pair. This is useful when you have a large number of origins and destinations and are intere...",
                        "default": None
                },
                "accumulate_attributes": {
                        "type": "string",
                        "description": "A list of cost attributes to be accumulated during analysis. These accumulated attributes are for reference only; the solver only uses the cost attribute used by the designated travel mode when solvin...",
                        "default": None
                },
                "ignore_invalid_locations": {
                        "type": "string",
                        "description": "Specifies whether invalid input locations will be ignored. Typically, locations are invalid if they cannot be located on the network. When invalid locations are ignored, the solver will skip them and ...",
                        "default": None
                }
        },
        "required": [
                "network_data_source"
        ]
},
    "make_route_analysis_layer": {
        "name": "make_route_analysis_layer",
        "description": "Makes a route network analysis layer and sets its analysis properties. A route network analysis layer is useful for determining the best route between a set of network locations based on a specified network cost. The layer can be created using a local network dataset or a routing service hosted online or in a portal.",
        "parameters": {
                "network_data_source": {
                        "type": "string",
                        "description": "The network dataset or service on which the network analysis will be performed.The parameter can be specified using one of the following:The catalog path to the network datasetA network dataset layer ..."
                },
                "layer_name": {
                        "type": "string",
                        "description": "The name of the network analysis layer that will be created.",
                        "default": None
                },
                "travel_mode": {
                        "type": "string",
                        "description": "The name of the travel mode to use in the analysis. The travel mode represents a collection of network settings, such as travel restrictions and U-turn policies, that determine how a pedestrian, car, ...",
                        "default": None
                },
                "sequence": {
                        "type": "string",
                        "description": "Specifies whether the input stops must be visited in a particular order when calculating the optimal route. This option changes the route analysis from a shortest-path problem to a traveling salespers...",
                        "default": None
                },
                "time_of_day": {
                        "type": "string",
                        "description": "The start date and time for the route. Route start time is typically used to find routes based on the impedance attribute that varies with the time of the day. For example, a start time of 7:00 a.m. c...",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "Specifies the time zone of the time_of_day  parameter.\r\nLOCAL_TIME_AT_LOCATIONS\u2014The time_of_day parameter refers to the time zone in which the first stop of a route is located. This is the default.If ...",
                        "default": None
                },
                "line_shape": {
                        "type": "string",
                        "description": "Specifies the shape type that will be used for the route features that are output by the analysis.\r\nALONG_NETWORK\u2014The output routes will have the exact shape of the underlying network sources. The out...",
                        "default": None
                },
                "accumulate_attributes": {
                        "type": "string",
                        "description": "A list of cost attributes to be accumulated during analysis. These accumulated attributes are for reference only; the solver only uses the cost attribute used by the designated travel mode when solvin...",
                        "default": None
                },
                "generate_directions_on_solve": {
                        "type": "string",
                        "description": "Specifies whether directions will be generated when  running the analysis.\r\nDIRECTIONS\u2014Turn-by-turn directions will be generated on solve. This is the default.NO_DIRECTIONS\u2014Turn-by-turn directions wil...",
                        "default": None
                },
                "time_zone_for_time_fields": {
                        "type": "string",
                        "description": "Specifies the time zone that will be used to interpret the time fields included in the input tables, such as the fields used for time windows.\r\nLOCAL_TIME_AT_LOCATIONS\u2014The dates and times in the time ...",
                        "default": None
                },
                "ignore_invalid_locations": {
                        "type": "string",
                        "description": "Specifies whether invalid input locations will be ignored. Typically, locations are invalid if they cannot be located on the network. When invalid locations are ignored, the solver will skip them and ...",
                        "default": None
                }
        },
        "required": [
                "network_data_source"
        ]
},
    "make_service_area_analysis_layer": {
        "name": "make_service_area_analysis_layer",
        "description": "Makes a service area network analysis layer and sets its analysis properties. A service area analysis layer is useful in determining the area of accessibility within a given cutoff cost from a facility location. The layer can be created using a local network dataset or a routing service hosted online or in a portal.",
        "parameters": {
                "network_data_source": {
                        "type": "string",
                        "description": "The network dataset or service on which the network analysis will be performed.The parameter can be specified using one of the following:The catalog path to the network datasetA network dataset layer ..."
                },
                "layer_name": {
                        "type": "string",
                        "description": "The name of the network analysis layer that will be created.",
                        "default": None
                },
                "travel_mode": {
                        "type": "string",
                        "description": "The name of the travel mode that will be used in the analysis. The travel mode represents a collection of network settings, such as travel restrictions and U-turn policies, that determine how a pedest...",
                        "default": None
                },
                "travel_direction": {
                        "type": "string",
                        "description": "Specifies the direction of travel to or from the facilities.\r\nFROM_FACILITIES\u2014The direction of travel is away from the facilities. This is the default.TO_FACILITIES\u2014The direction of travel is toward t...",
                        "default": None
                },
                "cutoffs": {
                        "type": "string",
                        "description": "The extent of the service area to be calculated in the units of the impedance attribute used by the selected travel mode.  For example, when analyzing driving time, a cutoff value of 10  means that th...",
                        "default": None
                },
                "time_of_day": {
                        "type": "string",
                        "description": "The time to depart from or arrive at the facilities of the service area layer. The interpretation of this value as a departure or arrival time  depends on whether travel is away from or toward the fac...",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "Specifies the time zone for the time of day parameter.LOCAL_TIME_AT_LOCATIONS\u2014The time of day parameter will use the time zone or zones in which the facilities are located. The start or end times of t...",
                        "default": None
                },
                "output_type": {
                        "type": "string",
                        "description": "Specifies the type of output to be generated.\r\nService area output can be line features representing the roads reachable before the  cutoffs are exceeded or the polygon features encompassing these lin...",
                        "default": None
                },
                "polygon_detail": {
                        "type": "string",
                        "description": "Specifies the level of detail of the output polygons.\r\nSTANDARD\u2014Polygons with a standard level of detail will be created. This is the default.GENERALIZED\u2014Generalized polygons will be created using the...",
                        "default": None
                },
                "geometry_at_overlaps": {
                        "type": "string",
                        "description": "Specifies the behavior of service-area output from multiple facilities in relation to one another.OVERLAP\u2014Individual polygons or sets of lines for each facility will be created. The polygons or lines ...",
                        "default": None
                },
                "geometry_at_cutoffs": {
                        "type": "string",
                        "description": "Specifies the behavior of service area output for a single  facility when multiple cutoff values are specified. This parameter does not apply to line output.RINGS\u2014Each polygon will include only the ar...",
                        "default": None
                },
                "polygon_trim_distance": {
                        "type": "string",
                        "description": "The service area polygon trim distance.  The polygon trim distance is the distance the service area polygon will extend from the road when no other reachable roads are nearby, similar to a line buffer...",
                        "default": None
                },
                "exclude_sources_from_polygon_generation": {
                        "type": "string",
                        "description": "The network dataset edge sources that will be excluded when generating service area polygons. Polygons will not be generated around the excluded sources, even though they are traversed in the analysis...",
                        "default": None
                },
                "accumulate_attributes": {
                        "type": "string",
                        "description": "A list of cost attributes to be accumulated during analysis. These accumulated attributes are for reference only; the solver only uses the cost attribute used by the designated travel mode when solvin...",
                        "default": None
                },
                "ignore_invalid_locations": {
                        "type": "string",
                        "description": "Specifies whether invalid input locations will be ignored. Typically, locations are invalid if they cannot be located on the network. When invalid locations are ignored, the solver will skip them and ...",
                        "default": None
                }
        },
        "required": [
                "network_data_source"
        ]
},
    "make_vehicle_routing_problem_analysis_layer": {
        "name": "make_vehicle_routing_problem_analysis_layer",
        "description": "Creates a vehicle routing problem (VRP) network analysis layer and sets its analysis properties. A VRP analysis layer is useful for optimizing a set of routes using a fleet of vehicles. The layer can be created using a local network dataset or a service hosted online or in a portal.",
        "parameters": {
                "network_data_source": {
                        "type": "string",
                        "description": "The network dataset or service on which the network analysis will be performed. Use the portal URL for a service."
                },
                "layer_name": {
                        "type": "string",
                        "description": "The name of the VRP network analysis layer to create.",
                        "default": None
                },
                "travel_mode": {
                        "type": "string",
                        "description": "The name of the travel mode to use in the analysis. The travel mode represents a collection of network settings, such as travel restrictions and U-turn policies, that determine how a pedestrian, car, ...",
                        "default": None
                },
                "time_units": {
                        "type": "string",
                        "description": "Specifies the time units to be used by the temporal fields of the analysis layer's sublayers and tables (network analysis classes). This value does not need to match the units of the time cost attribu...",
                        "default": None
                },
                "distance_units": {
                        "type": "string",
                        "description": "Specifies the distance units to be used by the distance fields of the analysis layer's sublayers and tables (network analysis classes). This value does not need to match the units of the optional dist...",
                        "default": None
                },
                "default_date": {
                        "type": "string",
                        "description": "The implied date for time field values that don't have a date specified with the time. If a time field for an order object, such as TimeWindowStart, has a time-only value, the date is assumed to be th...",
                        "default": None
                },
                "time_zone_for_time_fields": {
                        "type": "string",
                        "description": "Specifies the time zone to be used for the input date-time fields supported by the tool. LOCAL_TIME_AT_LOCATIONS\u2014  The date-time values associated with the orders or depots will be in the time zone in...",
                        "default": None
                },
                "line_shape": {
                        "type": "string",
                        "description": "Specifies the shape type that will be used for the route features that are output by the analysis.\r\nALONG_NETWORK\u2014The output routes will have the exact shape of the underlying network sources. The out...",
                        "default": None
                },
                "time_window_factor": {
                        "type": "string",
                        "description": "Specifies the importance of honoring time windows without causing violations. A time window violation occurs when a route arrives at an order, depot, or break after a time window has closed. The viola...",
                        "default": None
                },
                "excess_transit_factor": {
                        "type": "string",
                        "description": "Specifies the importance of reducing excess transit time. Excess transit time is the amount of time exceeding the time required to travel directly between paired orders. The excess time results from b...",
                        "default": None
                },
                "generate_directions_on_solve": {
                        "type": "string",
                        "description": "Specifies whether directions will be generated. DIRECTIONS\u2014Turn-by-turn directions will be generated on solve. This is the default.NO_DIRECTIONS\u2014Turn-by-turn directions will not be generated on solve.",
                        "default": None
                },
                "spatial_clustering": {
                        "type": "string",
                        "description": "Specifies whether spatial clustering will be used.CLUSTER\u2014The orders assigned to an individual route will be spatially clustered. Clustering orders tends to keep routes in smaller areas and reduce how...",
                        "default": None
                },
                "ignore_invalid_locations": {
                        "type": "string",
                        "description": "Specifies whether invalid input locations will be ignored.\r\nSKIP\u2014Invalid input locations will be ignored so that the analysis will succeed using only valid locations.HALT\u2014Invalid locations will not be...",
                        "default": None
                }
        },
        "required": [
                "network_data_source"
        ]
},
    "make_waste_collection_analysis_layer": {
        "name": "make_waste_collection_analysis_layer",
        "description": "Creates a waste collection network analysis layer and sets its analysis properties. A waste collection analysis layer is useful for optimizing a set of routes using a fleet of vehicles to pick up municipal waste. The layer can be created using a network dataset.",
        "parameters": {
                "network_data_source": {
                        "type": "string",
                        "description": "The network dataset on which the network analysis will be performed.\t\t\t\t\tThe network must have at least one travel mode, one cost attribute with time units, and one cost attribute with distance units."
                },
                "layer_name": {
                        "type": "string",
                        "description": "The name of the network analysis layer that will be created.",
                        "default": None
                },
                "travel_mode": {
                        "type": "string",
                        "description": "The name of the travel mode that will be used in the analysis. The travel mode represents a collection of network settings, such as travel restrictions and U-turn policies, that determine how a pedest...",
                        "default": None
                },
                "time_units": {
                        "type": "string",
                        "description": "Specifies the time units that will be used by the analysis layer's properties and the temporal fields of the analysis layer's sublayers and tables (network analysis classes). This value does not need ...",
                        "default": None
                },
                "distance_units": {
                        "type": "string",
                        "description": "Specifies the distance units that will be used by the analysis layer's properties and the distance fields of the analysis layer's sublayers and tables (network analysis classes). This value does not n...",
                        "default": None
                },
                "route_start_time": {
                        "type": "string",
                        "description": "The default start time for \r\nroutes.  This time of day is used for all routes for which the StartTime field in the Routes sublayer is None. When no parameter value is specified, all rows in the Routes...",
                        "default": None
                },
                "max_route_total_time": {
                        "type": "string",
                        "description": "The maximum allowed total time for each route. The value can be any positive number.This value will be used for all routes for which the MaxTotalTime field in the Routes sublayer is None. When no valu...",
                        "default": None
                },
                "stop_collection_mode": {
                        "type": "string",
                        "description": "Specifies the default stop collection mode for each stop.  This value can be one of the options listed below, or it can be left blank (the default).This value will be used for all stops for which the ...",
                        "default": None
                }
        },
        "required": [
                "network_data_source"
        ]
},
    "share_as_route_layers": {
        "name": "share_as_route_layers",
        "description": "Shares the results of network analyses as route layer items in a portal.  A route layer includes all the information for a route such as the stops assigned to the route or the orders serviced by a route, as well as the travel directions. A route layer item can be used by various applications, such as ArcGIS Navigator to provide route guidance for mobile workers, the Directions pane in Map Viewer Classic to further customize the route contained in the route layer, and ArcGIS Pro to create a route analysis layer from a route layer.",
        "parameters": {
                "in_network_analysis_layer": {
                        "type": "string",
                        "description": "The network analysis layer from which the route layer items will be created. The network analysis layer should already be solved.Route, Closest facility, Vehicle routing problem, and Last mile deliver..."
                },
                "summary": {
                        "type": "string",
                        "description": "The summary that will be used by the route layer items. The summary is displayed as part of the item information for the route layer item. If no value is provided, default summary text\u2014Route and direc...",
                        "default": None
                },
                "tags": {
                        "type": "string",
                        "description": "The tags that will be used to describe and identify the route layer items. Individual tags are separated with commas. The route name is always included as a tag even when no other value is provided.",
                        "default": None
                },
                "route_name_prefix": {
                        "type": "string",
                        "description": "A qualifier that will be added to the title of every route\r\nlayer item. For example, a route name prefix of Monday morning deliveries can be used to group all route layer items created from a route an...",
                        "default": None
                },
                "portal_folder_name": {
                        "type": "string",
                        "description": "The folder in your personal online\r\nworkspace where the route layer items will be created. If a\r\nfolder with the provided name does not exist, a folder will be\r\ncreated. If a folder with the provided ...",
                        "default": None
                },
                "share_with": {
                        "type": "string",
                        "description": "Specifies who can access the route layer items.EVERYBODY\u2014 The route layer items will be public and can be accessed by anyone with the URL to the items.MYCONTENT\u2014 The route layer items will only be sha...",
                        "default": None
                },
                "groups": {
                        "type": "string",
                        "description": "The list of groups with which the route layer items will be shared. This parameter is applicable only when the share_with parameter is set to MYGROUPS.",
                        "default": None
                }
        },
        "required": [
                "in_network_analysis_layer"
        ]
},
    "solve": {
        "name": "solve",
        "description": "Solves the network analysis layer problem based on its network locations and properties.",
        "parameters": {
                "in_network_analysis_layer": {
                        "type": "string",
                        "description": "The network analysis layer on which the analysis will be computed."
                },
                "ignore_invalids": {
                        "type": "string",
                        "description": "Specifies whether invalid input locations will be ignored. Typically, locations are invalid if they cannot be located on the network. When invalid locations are ignored, the solver will skip them and ...",
                        "default": None
                },
                "terminate_on_solve_error": {
                        "type": "string",
                        "description": "Specifies whether the tool will stop running and terminate if an error is encountered during the solve.TERMINATE\u2014The tool will stop running and terminate when the solver encounters an error. This is t...",
                        "default": None
                },
                "simplification_tolerance": {
                        "type": "string",
                        "description": "The tolerance that determines the degree of simplification for the output geometry. If a tolerance is specified, it must be greater than zero. You\r\ncan choose a preferred unit; the default unit is dec...",
                        "default": None
                },
                "overrides": {
                        "type": "string",
                        "description": "Note:This parameter is for internal use only.",
                        "default": None
                }
        },
        "required": [
                "in_network_analysis_layer"
        ]
},
    "select_layer_by_location": {
        "name": "select_layer_by_location",
        "description": "Selects features  based on a spatial relationship to features in another dataset or the same dataset. Each feature in the Input Features parameter is evaluated using the features in the  Selecting Features parameter. If the specified Relationship parameter value is met, the input feature is selected. Learn more about Select By Location including image examples of relationships",
        "parameters": {
                "in_layer": {
                        "type": "string",
                        "description": "The features that will be evaluated using the select_features parameter values.  The selection will be applied to these features."
                },
                "overlap_type": {
                        "type": "string",
                        "description": "Specifies the spatial relationship that will be evaluated.INTERSECT\u2014The features in the input layer will be selected if they intersect a selecting feature. This is the default. INTERSECT_3D\u2014The featur...",
                        "default": None
                },
                "select_features": {
                        "type": "string",
                        "description": "The features in the Input Features parameter will be selected based on their relationship to the features from this layer or feature class.",
                        "default": None
                },
                "search_distance": {
                        "type": "string",
                        "description": "The distance that will be searched. This parameter is only valid if the overlap_type  parameter is set to INTERSECT, INTERSECT_3D, WITHIN_A_DISTANCE, WITHIN_A_DISTANCE_3D, WITHIN_A_DISTANCE_GEODESIC, ...",
                        "default": None
                },
                "selection_type": {
                        "type": "string",
                        "description": "Specifies how the selection will be applied to the input and how it will be combined with an existing selection.  This tool does not include an option to clear an existing selection; use the  Select L...",
                        "default": None
                },
                "invert_spatial_relationship": {
                        "type": "string",
                        "description": "Specifies whether the spatial relationship evaluation result or the opposite result will be used.  For example, this parameter can be used to get a list of features that do not intersect or are not wi...",
                        "default": None
                }
        },
        "required": [
                "in_layer"
        ]
},
    "copy_features": {
        "name": "copy_features",
        "description": "Copies features from the input feature class or layer to a new feature class.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The features to be copied."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class which will be created and to which the features will be copied."
                },
                "config_keyword": {
                        "type": "string",
                        "description": "Geodatabase configuration keyword to be applied if the output is a geodatabase.",
                        "default": None
                },
                "spatial_grid_1": {
                        "type": "string",
                        "description": "This parameter has been deprecated in ArcGIS Pro.  Any value you enter is ignored.",
                        "default": None
                },
                "spatial_grid_2": {
                        "type": "string",
                        "description": "This parameter has been deprecated in ArcGIS Pro.  Any value you enter is ignored.",
                        "default": None
                },
                "spatial_grid_3": {
                        "type": "string",
                        "description": "This parameter has been deprecated in ArcGIS Pro.  Any value you enter is ignored.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "build_network": {
        "name": "build_network",
        "description": "Reconstructs the network connectivity and attribute information of a network dataset. The network dataset must be rebuilt after edits are made to the attributes or the features of a participating source feature class. After the source features are edited, the tool establishes the network connectivity only in the areas that have been edited to speed up the build process; however, when the network attributes are edited, the entire extent of the network dataset is rebuilt. This may be a slow operation on a large network dataset. Learn more about which network dataset edits require a rebuild",
        "parameters": {
                "in_network_dataset": {
                        "type": "string",
                        "description": "The network dataset to be built."
                },
                "force_full_build": {
                        "type": "string",
                        "description": "Specifies whether the full network will be built or only the parts of the network in dirty areas.\r\nFORCE_FULL_BUILD\u2014The full network will be built.NO_FORCE_FULL_BUILD\u2014Only the parts of the network tha...",
                        "default": None
                }
        },
        "required": [
                "in_network_dataset"
        ]
},
    "create_network_dataset": {
        "name": "create_network_dataset",
        "description": "Creates a network dataset in an existing feature dataset. The network dataset can be used to perform network analysis on the data in the feature dataset.",
        "parameters": {
                "feature_dataset": {
                        "type": "string",
                        "description": "The feature dataset where the network dataset\r\nwill be created. The feature dataset should contain the source feature classes that will participate in the network dataset.If the feature dataset is in ..."
                },
                "out_name": {
                        "type": "string",
                        "description": "The name of the network dataset to be created. The feature_dataset parameter value and its parent geodatabase must not already contain a network dataset with this name."
                },
                "source_feature_class_names": {
                        "type": "string",
                        "description": "The names of the feature classes to be included in the network dataset as network source features. Specify this parameter as a list of strings.You must choose at least one line feature class that is n..."
                },
                "elevation_model": {
                        "type": "string",
                        "description": "Specifies the model that will be used to control vertical connectivity in the network dataset.\r\nLearn more about vertical connectivityELEVATION_FIELDS\u2014 Coincident endpoints with the same elevation fie..."
                }
        },
        "required": [
                "feature_dataset",
                "out_name",
                "source_feature_class_names",
                "elevation_model"
        ]
},
    "create_network_dataset_from_template": {
        "name": "create_network_dataset_from_template",
        "description": "Creates a new network dataset with the schema contained in the input template file (.xml). All the feature classes and input tables required for creating the network dataset must already exist before this tool is executed.",
        "parameters": {
                "network_dataset_template": {
                        "type": "string",
                        "description": "The  template file (.xml)  created by the Create Template From Network Dataset tool containing the schema of the output network dataset to be created."
                },
                "output_feature_dataset": {
                        "type": "string",
                        "description": "The feature dataset containing the feature classes that will take part in the network dataset being created.\r\nThe network will be created in this dataset using the name specified in the network datase..."
                }
        },
        "required": [
                "network_dataset_template",
                "output_feature_dataset"
        ]
},
    "create_template_from_network_dataset": {
        "name": "create_template_from_network_dataset",
        "description": "Creates a file containing the schema of an existing network dataset. This template file can then be used to create a new network dataset with the same schema.",
        "parameters": {
                "network_dataset": {
                        "type": "string",
                        "description": "The network dataset whose schema will be written to the output template file."
                },
                "output_network_dataset_template": {
                        "type": "string",
                        "description": "The output file (.xml) that will contain the schema of the input network dataset."
                }
        },
        "required": [
                "network_dataset",
                "output_network_dataset_template"
        ]
},
    "dissolve_network": {
        "name": "dissolve_network",
        "description": "Creates a network dataset that minimizes the number of line features required to correctly model the input network dataset. The more efficient output network dataset reduces the time required to solve analyses, draw results, and generate driving directions. This tool outputs a new network dataset and source feature classes; the input network dataset and its source features remain unchanged.",
        "parameters": {
                "in_network_dataset": {
                        "type": "string",
                        "description": "The network dataset to be dissolved.  The input network dataset must be a file or personal geodatabase network dataset with exactly one edge source. Any number of junction sources and turn sources is ..."
                },
                "out_workspace_location": {
                        "type": "string",
                        "description": "The geodatabase workspace in which to create the dissolved network dataset. The workspace must be an ArcGIS 10 geodatabase or later, and it must be a different geodatabase than the one where the input..."
                }
        },
        "required": [
                "in_network_dataset",
                "out_workspace_location"
        ]
},
    "make_network_dataset___layer": {
        "name": "make_network_dataset___layer",
        "description": "Creates a network dataset layer from a network  dataset. A network dataset is opened each time the network dataset is used as input to a geoprocessing tool. Opening a network dataset is expensive, as they contain advanced data structures and tables that are read and cached. A network dataset layer, which opens the dataset only a single time, will perform better in subsequent tools than reusing the network dataset.",
        "parameters": {
                "in_network_dataset": {
                        "type": "string",
                        "description": "The network dataset from which to make the new layer."
                },
                "output_layer": {
                        "type": "string",
                        "description": "The name of the network dataset layer to be\r\ncreated. The layer can be used as an input\r\nto any geoprocessing tool that accepts a network dataset layer as\r\ninput.\r\nNote:The output layer  created is te..."
                },
                "draw_elements": {
                        "type": "string",
                        "description": "This parameter is not yet supported in ArcGIS Pro.",
                        "default": None
                }
        },
        "required": [
                "in_network_dataset",
                "output_layer"
        ]
},
    "integrate": {
        "name": "integrate",
        "description": "Analyzes the coordinate locations of feature vertices among features in one or more feature classes. Those that fall within a specified distance of one another are assumed to represent the same location and are assigned a common coordinate value (in other words, they are colocated). The tool also adds vertices where feature vertices are within the x,y tolerance of an edge and where line segments intersect. Integrate performs\r\nthe following processing tasks: Vertices within the x,y tolerance of one another will be assigned the same coordinate location.When a vertex of one feature is within the x,y tolerance of an edge of any other feature, a new vertex will be inserted on the edge.When line segments intersect, a vertex will be inserted at the point of intersection for each feature involved in the intersection. An alternate tool is available for vector data integration. See the Pairwise Integrate documentation for details.",
        "parameters": {
                "in_featuresfeature_layer_long": {
                        "type": "string",
                        "description": "The feature classes that will be integrated. When the distance between features is small in comparison to the tolerance, the vertices or points will be clustered (moved to be coincident).The feature c..."
                },
                "cluster_tolerance": {
                        "type": "string",
                        "description": "The distance that determines the range in which feature vertices are made coincident. To minimize undesired movement of vertices, the x,y tolerance should be small. If no value is provided, the x,y to...",
                        "default": None
                }
        },
        "required": [
                "in_featuresfeature_layer_long"
        ]
},
    "create_turn_feature_class": {
        "name": "create_turn_feature_class",
        "description": "Creates a turn feature class to store turn features that model turning movements in a network dataset.",
        "parameters": {
                "out_location": {
                        "type": "string",
                        "description": "The  file, workgroup, or enterprise geodatabase, or the folder where the output turn feature class will be created. The workspace must already exist."
                },
                "out_feature_class_name": {
                        "type": "string",
                        "description": "The name of the turn feature class the will be created."
                },
                "maximum_edges": {
                        "type": "string",
                        "description": "The maximum number of edges that turns in the new turn feature class can model. The default value is 5. The maximum value is 50.",
                        "default": None
                },
                "in_network_dataset": {
                        "type": "string",
                        "description": "The network dataset in which the turn feature class will participate. The resulting turn feature class will be added as a turn source to the network dataset. If no network dataset is provided, the tur...",
                        "default": None
                },
                "in_template_feature_class": {
                        "type": "string",
                        "description": "The feature class that will be used as a template to define the attribute schema of the new turn feature class.If the template feature class has the following fields, they will not be created in the o...",
                        "default": None
                },
                "spatial_reference": {
                        "type": "string",
                        "description": "The spatial reference that will be applied to the output turn feature class. This parameter is ignored if the output location is a geodatabase feature dataset, as the output turn feature class will in...",
                        "default": None
                },
                "config_keyword": {
                        "type": "string",
                        "description": "The configuration keyword that will determine the storage parameters of the new turn feature class. This parameter is used only if the output location is a workgroup or enterprise geodatabase.",
                        "default": None
                },
                "spatial_grid_1": {
                        "type": "string",
                        "description": "This parameter is not supported.  Any value provided will be ignored.",
                        "default": None
                },
                "spatial_grid_2": {
                        "type": "string",
                        "description": "This parameter is not supported.  Any value provided will be ignored.",
                        "default": None
                },
                "spatial_grid_3": {
                        "type": "string",
                        "description": "This parameter is not supported.  Any value provided will be ignored.",
                        "default": None
                },
                "has_z": {
                        "type": "string",
                        "description": "Specifies whether the coordinates in the turn feature class with have elevation (z) values.ENABLED\u2014The coordinates in the turn feature class will have elevation (z) values. Use this value if the input...",
                        "default": None
                }
        },
        "required": [
                "out_location",
                "out_feature_class_name"
        ]
},
    "increase_maximum_edges": {
        "name": "increase_maximum_edges",
        "description": "Increases the maximum number of edges per turn in a turn feature class.",
        "parameters": {
                "in_turn_features": {
                        "type": "string",
                        "description": "The turn feature class that is having its maximum number of edges raised."
                },
                "maximum_edges": {
                        "type": "string",
                        "description": "The new maximum number of edges in the input turn feature class. The value must be at least one higher than the existing maximum number of edges and cannot be greater than 50."
                }
        },
        "required": [
                "in_turn_features",
                "maximum_edges"
        ]
},
    "populate_alternate_id_fields": {
        "name": "populate_alternate_id_fields",
        "description": "Creates and populates additional fields on the turn feature classes that reference the edges in the network  by alternate IDs. The alternate IDs help maintain the integrity of the turn features if the edge sources are edited in such a way that their ObjectID values change. Learn more about turns in a network dataset",
        "parameters": {
                "in_network_dataset": {
                        "type": "string",
                        "description": "The network dataset whose turn feature classes will receive alternate ID fields. The fields will be created on all of the turn feature classes added as a turn source to the network dataset."
                },
                "alternate_id_field_name": {
                        "type": "string",
                        "description": "The name of the alternate ID field on the edge feature sources of the network dataset. All edge feature sources referenced by turns must have the same name for the alternate ID field."
                }
        },
        "required": [
                "in_network_dataset",
                "alternate_id_field_name"
        ]
},
    "turn_table_to_turn_feature_class": {
        "name": "turn_table_to_turn_feature_class",
        "description": "Converts an ArcView turn table or ArcInfo Workstation coverage turn table to an ArcGIS turn feature class.",
        "parameters": {
                "in_turn_table": {
                        "type": "string",
                        "description": "The .dbf file or INFO turn table from which the new turn feature class will be created.\r\nINFO tables do not support mixed case path names on Linux and Solaris."
                },
                "reference_line_features": {
                        "type": "string",
                        "description": "The line feature class to which the input turn table refers. The feature class must be a source in a network dataset."
                },
                "out_feature_class_name": {
                        "type": "string",
                        "description": "The name of the new turn feature class to create."
                },
                "reference_nodes_table": {
                        "type": "string",
                        "description": "The nodes.dbf table in the .nws folder containing the original ArcView GIS network in which the input turn table participated.This parameter is ignored if the input turn table is an INFO table.If the ...",
                        "default": None
                },
                "maximum_edges": {
                        "type": "string",
                        "description": "The maximum number of edges per turn in the new turn feature class. The default value is 5. The maximum value is 50.",
                        "default": None
                },
                "config_keyword": {
                        "type": "string",
                        "description": "Specifies the configuration keyword that determines the storage parameters of the output turn feature class. This parameter is used only if the output turn feature class is created in a workgroup or e...",
                        "default": None
                },
                "spatial_grid_1": {
                        "type": "string",
                        "description": "This parameter has been deprecated in ArcGIS Pro.  Any value you enter is ignored.",
                        "default": None
                },
                "spatial_grid_2": {
                        "type": "string",
                        "description": "This parameter has been deprecated in ArcGIS Pro.  Any value you enter is ignored.",
                        "default": None
                },
                "spatial_grid_3": {
                        "type": "string",
                        "description": "This parameter has been deprecated in ArcGIS Pro.  Any value you enter is ignored.",
                        "default": None
                }
        },
        "required": [
                "in_turn_table",
                "reference_line_features",
                "out_feature_class_name"
        ]
},
    "update_by_alternate_id_fields": {
        "name": "update_by_alternate_id_fields",
        "description": "Updates all the edge references in turn feature classes using an alternate ID field to identify the corresponding edge features for each turn. Use this tool after making edits to the edge source feature classes that alter ObjectID values. Learn more about turns in a network dataset",
        "parameters": {
                "in_network_dataset": {
                        "type": "string",
                        "description": "The network dataset whose turn feature classes will be updated by their alternate ID fields."
                },
                "alternate_id_field_name": {
                        "type": "string",
                        "description": "The name of the alternate ID field on the edge feature sources of the network dataset. All edge feature sources referenced by turns must have the same name for the alternate ID field."
                }
        },
        "required": [
                "in_network_dataset",
                "alternate_id_field_name"
        ]
},
    "update_by_geometry": {
        "name": "update_by_geometry",
        "description": "Updates all the edge references in the turn feature class using the geometry of the turn features. This tool is useful when the IDs listed for the turn can no longer find the edges participating in the turn due to edits to the underlying edges.",
        "parameters": {
                "in_turn_features": {
                        "type": "string",
                        "description": "The turn feature class to be updated."
                }
        },
        "required": [
                "in_turn_features"
        ]
}
}
