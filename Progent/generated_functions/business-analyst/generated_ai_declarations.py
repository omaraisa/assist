# Generated ArcGIS Pro business-analyst AI Function Declarations
# Generated on 2025-10-01T15:00:45.089603
# Total tools: 46

functions_declarations = {
    "calculate_market_penetration": {
        "name": "calculate_market_penetration",
        "description": "Calculates the market penetration based on the number of customers within an area compared to a demographic variable such as total population. An optional report can be created detailing the market penetration.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature class that will be used for calculating market penetration."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class that contains the calculated market penetration features."
                },
                "id_field": {
                        "type": "string",
                        "description": "A unique ID field in the market penetration layer."
                },
                "market_penetration_base_field": {
                        "type": "string",
                        "description": "The field containing the values that will be used to calculate market penetration. This field will be used as the denominator and represents your market\u2014for example, Total Population or Total Househol..."
                },
                "in_customer_features": {
                        "type": "string",
                        "description": "The input feature class containing the points for the customer\r\nlayer."
                },
                "area_description_field": {
                        "type": "string",
                        "description": "The field that will be used to describe each feature in the market penetration layer.",
                        "default": None
                },
                "weight_field": {
                        "type": "string",
                        "description": "The field in the customer layer that will be used as a weight to calculate market penetration rather than customer counts.",
                        "default": None
                },
                "create_report": {
                        "type": "string",
                        "description": "Specifies whether a summary report will be created.\r\nCREATE_REPORT\u2014A summary report will be created.DO_NOT_CREATE_REPORT\u2014A summary report will not be created. This is the default.",
                        "default": None
                },
                "store_id": {
                        "type": "string",
                        "description": "A unique identifier associated with each store for each trade area.",
                        "default": None
                },
                "link_field": {
                        "type": "string",
                        "description": "An ID that assigns a trade area to a customer.",
                        "default": None
                },
                "report_title": {
                        "type": "string",
                        "description": "The title of the report.",
                        "default": None
                },
                "report_folder": {
                        "type": "string",
                        "description": "The output directory that will contain the report.",
                        "default": None
                },
                "report_format": {
                        "type": "string",
                        "description": "Specifies the format  one or more output report formats.PDF\u2014The report will be in PDF format. This is the default.XLSX\u2014The report will be in XLSX format.HTML\u2014The report will be in HTML format.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "id_field",
                "market_penetration_base_field",
                "in_customer_features"
        ]
},
    "color_coded_layer": {
        "name": "color_coded_layer",
        "description": "Creates multilevel, scale-dependent choropleth layers from a variable describing a business, demographic, consumer, or landscape characteristic.",
        "parameters": {
                "classification_variable": {
                        "type": "string",
                        "description": "A variable that will display as a color-coded map."
                },
                "out_layer_name": {
                        "type": "string",
                        "description": "The name of the color-coded layer that will be added to the map."
                },
                "classification_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to calculate  the class breaks.NATURAL_BREAKS\u2014Natural breaks classes are based on natural groupings inherent in the data. Class breaks that best group similar va..."
                },
                "number_of_classes": {
                        "type": "string",
                        "description": "The number of data classification breaks that will appear on the map. The default value is 5."
                },
                "area_of_interest": {
                        "type": "string",
                        "description": "The feature layer that will be used to determine the geographic extent of the analysis.",
                        "default": None
                },
                "out_dataset_path": {
                        "type": "string",
                        "description": "The geodatabase in which the output feature dataset will be created.",
                        "default": None
                },
                "out_dataset_name": {
                        "type": "string",
                        "description": "The name of the feature dataset in the output geodatabase in which the color-coded layer feature classes will be created.",
                        "default": None
                },
                "boundary_mode": {
                        "type": "string",
                        "description": "Specifies the types of boundaries that will be used to create levels in the color-coded group layer.STANDARD_GEOGRAPHIES\u2014Boundaries will be levels of standard geographies. This is the default.H3_HEXAG...",
                        "default": None
                },
                "secondary_variable": {
                        "type": "string",
                        "description": "A second variable that will display as a color-coded map.",
                        "default": None
                },
                "grid_size": {
                        "type": "string",
                        "description": "Specifies the grid size that will be used to create the bivariate color symbology.TWO_BY_TWO\u2014A 4-class bivariate color scheme will be used.THREE_BY_THREE\u2014A 9-class bivariate color scheme will be used....",
                        "default": None
                },
                "renderer_type": {
                        "type": "string",
                        "description": "Specifies the type of symbology that will be used.BIVARIATE\u2014Two variables will be displayed using a grid color scheme.GRADUATED_COLORS\u2014Varying color shades will be displayed across geographical areas....",
                        "default": None
                }
        },
        "required": [
                "classification_variable",
                "out_layer_name",
                "classification_method",
                "number_of_classes"
        ]
},
    "enrich_layer": {
        "name": "enrich_layer",
        "description": "Enriches data by adding demographic and landscape facts about the people and places that surround or are inside data locations. The output is a duplicate of the input with additional attribute fields. This tool requires an ArcGIS Online organizational account or a locally stored or installed dataset. This tool uses detailed aggregation and apportionment settings to summarize data.  The Apportion Polygon tool is similar to this tool. However, Apportion Polygon uses user-specified apportionment. Enrich Layer uses U.S. Census Block points or global settlement points for apportionment. For more information, see Data apportionment.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The features that will be enriched."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output layer containing both the input attributes and user-selected attributes. Selected attributes are summarized from underlying demographic boundaries. Only the area inside the input boundary i..."
                },
                "variables": {
                        "type": "string",
                        "description": "The variables that will be summarized and added to the output feature class."
                },
                "buffer_type": {
                        "type": "string",
                        "description": "Specifies the area that will be enriched.\r\nThe default value is STRAIGHT_LINE_DISTANCE.Input line features can only use the STRAIGHT_LINE_DISTANCE distance option.",
                        "default": None
                },
                "distance": {
                        "type": "string",
                        "description": "The distance or size of an area to enrich, for example, a 1-mile buffer or 5-minute walk time. Units correspond to the polygon type. The default value is 1.",
                        "default": None
                },
                "unit": {
                        "type": "string",
                        "description": "The units associated with the distance parameter. The default value is MILES.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "variables"
        ]
},
    "find_nearby_locations": {
        "name": "find_nearby_locations",
        "description": "Identifies locations closest to the input features based on a selected distance type. The number of points in the output is defined by limiting the count or percentage of location points to return or by limiting the distance from the input points.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The point layer to be measured to or from the in_location_points parameter value."
                },
                "id_field": {
                        "type": "string",
                        "description": "A field containing unique identifiers for each input feature."
                },
                "in_location_points": {
                        "type": "string",
                        "description": "The layer that will be used to generate the output with distance and direction attributes to or from the in_features parameter value."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output location point features."
                },
                "distance_type": {
                        "type": "string",
                        "description": "The calculated distance based on the method of travel. Straight Line is the default value.",
                        "default": None
                },
                "units": {
                        "type": "string",
                        "description": "The measurement units, in distance or time, that will be used when calculating nearby locations.",
                        "default": None
                },
                "distance_limit": {
                        "type": "string",
                        "description": "The analysis extent measured in distance or time.",
                        "default": None
                },
                "number_limit": {
                        "type": "string",
                        "description": "The numeric limit of the in_location_points value."
                },
                "percent_limit": {
                        "type": "string",
                        "description": "The closest points, as a percentage of the points of the in_location_points value."
                },
                "create_report": {
                        "type": "string",
                        "description": "Specifies whether an output report will be created.CREATE_REPORT\u2014A report will be created.DO_NOT_CREATE_REPORT\u2014A report will not be created. This is the default.",
                        "default": None
                },
                "report_title": {
                        "type": "string",
                        "description": "The title of the output report.",
                        "default": None
                },
                "report_folder": {
                        "type": "string",
                        "description": "The directory that will contain the output report.",
                        "default": None
                },
                "report_format": {
                        "type": "string",
                        "description": "The output report formats. The default value is InfographicHTML. Additional available formats are PDF, XLSX, S.XLSX, HTML, S.XML, ZIP, CVS, PAGX, and InfographicPDF.",
                        "default": None
                },
                "report_fields": {
                        "type": "string",
                        "description": "The additional fields that will be added to the report.",
                        "default": None
                },
                "travel_direction": {
                        "type": "string",
                        "description": "Specifies whether travel times or distances will be measured from location points to input features or from input features to location points.TOWARD_STORES\u2014The direction of travel will be from locatio...",
                        "default": None
                },
                "time_of_day": {
                        "type": "string",
                        "description": "The time at which travel will begin.",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "Specifies the time zone that will be used for the time_of_day parameter.UTC\u2014Coordinated universal time (UTC) will be used. Choose this option if you want the best location for a specific time, such as...",
                        "default": None
                },
                "search_tolerance": {
                        "type": "string",
                        "description": "The maximum distance that input points can be from the network. Points located beyond the search tolerance will be excluded from processing.",
                        "default": None
                },
                "location_name": {
                        "type": "string",
                        "description": "A field from the input in_location_points parameter. This field contains the name or ID for each input point used in the Find Nearby Locations report.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "id_field",
                "in_location_points",
                "out_feature_class",
                "number_limit",
                "percent_limit"
        ]
},
    "generate_desire_lines": {
        "name": "generate_desire_lines",
        "description": "Generates a series of lines from each customer to an associated store location. These lines are often called spider diagrams. The tool can also generate an optional Wind Rose report from the output. Note:This tool is similar to the Generate Origin-Destination Links tool in the Analysis toolbox Proximity toolset.",
        "parameters": {
                "in_stores_layer": {
                        "type": "string",
                        "description": "The input point layer representing store or facility locations."
                },
                "in_customers_layer": {
                        "type": "string",
                        "description": "The input point layer representing customers or patrons."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The resultant feature class that will be added to the Contents pane."
                },
                "store_id_field": {
                        "type": "string",
                        "description": "A unique ID field representing a store or facility location."
                },
                "link_field": {
                        "type": "string",
                        "description": "An ID field used to assign individual customers to stores."
                },
                "distance_type": {
                        "type": "string",
                        "description": "The method of travel that will be used for distance calculation. Straight Line is the default value. When using Portal for ArcGIS or local data sources, travel mode options are dynamically populated.",
                        "default": None
                },
                "units": {
                        "type": "string",
                        "description": "The type of distance- or time-measuring units that will be used when calculating minimal distance.",
                        "default": None
                },
                "cutoff": {
                        "type": "string",
                        "description": "The distance beyond which customers will be considered outliers and excluded from consideration during desire line generation.",
                        "default": None
                },
                "travel_direction": {
                        "type": "string",
                        "description": "Specifies the direction of travel that will be used between stores and demand points.TOWARD_STORES\u2014The direction of travel will be from demand points to stores.\r\nThis is the default.AWAY_FROM_STORES\u2014T...",
                        "default": None
                },
                "time_of_day": {
                        "type": "string",
                        "description": "The time at which travel begins.",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "Specifies the time zone that will be used for the time_of_day parameter.UTC\u2014Coordinated universal time (UTC) will be used. Choose this option if you want to choose the best location for a specific tim...",
                        "default": None
                },
                "create_report": {
                        "type": "string",
                        "description": "Specifies whether a Wind Rose report will be created.CREATE_REPORT\u2014A report will be created.DO_NOT_CREATE_REPORT\u2014A report will not be created. This is the default.",
                        "default": None
                },
                "report_title": {
                        "type": "string",
                        "description": "The title of the Wind Rose report.",
                        "default": None
                },
                "report_folder": {
                        "type": "string",
                        "description": "The output directory that will contain the Wind Rose report.",
                        "default": None
                },
                "report_format": {
                        "type": "string",
                        "description": "One or more output report formats. The default value is PDF. Additional available formats are XLSX, HTML, CSV, and PAGX.",
                        "default": None
                }
        },
        "required": [
                "in_stores_layer",
                "in_customers_layer",
                "out_feature_class",
                "store_id_field",
                "link_field"
        ]
},
    "generate_grids_and_hexagons": {
        "name": "generate_grids_and_hexagons",
        "description": "Creates features with vector-based square grid cells, hexagons, or H3 hexagons for a given area.",
        "parameters": {
                "area_of_interest": {
                        "type": "string",
                        "description": "The input feature class that will be used to define the extent of the grid or hexagon layer."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class that will contain the grid or hexagon features."
                },
                "cell_type": {
                        "type": "string",
                        "description": "Specifies the cell type that will be created in the output.SQUARE\u2014Regular four-sided polygons with equal side lengths will be created. This is the default.HEXAGON\u2014Regular six-sided polygons with equal...",
                        "default": None
                },
                "enrich_type": {
                        "type": "string",
                        "description": "Specifies the method that will be used for variable enrichment.ENRICH_CELL\u2014Enrichment will be performed on the cell_type parameter value.ENRICH_BUFFER\u2014Enrichment will be performed on a buffer around t...",
                        "default": None
                },
                "cell_size": {
                        "type": "string",
                        "description": "The size of the cell to generate squares or hexagons. The default value is 1 square mile.",
                        "default": None
                },
                "h3_resolution": {
                        "type": "string",
                        "description": "The resolution that will be used to generate the H3 hexagons. A value of 15 represents the finest resolution. The default value is 7.",
                        "default": None
                },
                "variables": {
                        "type": "string",
                        "description": "A list of variables that will be appended to the output.",
                        "default": None
                },
                "distance_type": {
                        "type": "string",
                        "description": "Specifies the method of travel that will be used for the buffer calculation.",
                        "default": None
                },
                "distance": {
                        "type": "string",
                        "description": "The distance that will be used for the buffer calculations.",
                        "default": None
                },
                "units": {
                        "type": "string",
                        "description": "The units that will be used for the distance parameter.",
                        "default": None
                },
                "out_enriched_buffers": {
                        "type": "string",
                        "description": "The feature class that will contain the enriched buffers.",
                        "default": None
                },
                "travel_direction": {
                        "type": "string",
                        "description": "Specifies the direction of travel that will be used between the center of the cell and the buffer boundary.TOWARD_STORES\u2014The direction of travel will be from location points to input features. This is...",
                        "default": None
                },
                "time_of_day": {
                        "type": "string",
                        "description": "The time at which the travel will begin.",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "Specifies the time zone that will be used for the time_of_day parameter.UTC\u2014Coordinated universal time (UTC) will be used. Choose this option if you want the best location for a specific time, such as...",
                        "default": None
                },
                "search_tolerance": {
                        "type": "string",
                        "description": "The maximum distance that input points can be from the network. Points located beyond the search tolerance will be excluded from processing.",
                        "default": None
                },
                "polygon_detail": {
                        "type": "string",
                        "description": "Specifies the level of detail that will be used for the output drive time polygons. STANDARD\u2014The optimal setting that combines processing speed with overall accuracy will be used. This is the default....",
                        "default": None
                },
                "out_centroids": {
                        "type": "string",
                        "description": "The feature class that will contain the cell centroids.",
                        "default": None
                }
        },
        "required": [
                "area_of_interest",
                "out_feature_class"
        ]
},
    "generate_points_from_business_listings": {
        "name": "generate_points_from_business_listings",
        "description": "Generates a point feature layer from a business point location search.",
        "parameters": {
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will contain the returned businesses."
                },
                "in_search_features": {
                        "type": "string",
                        "description": "The area that will be used to search for businesses. Selected features supersede the feature class and will be used as the search area.",
                        "default": None
                },
                "search_terms": {
                        "type": "string",
                        "description": "The terms that will be used to search for businesses. You can use terms such as business name or business type keywords. If this parameter is not set, all businesses from the in_search_features parame...",
                        "default": None
                },
                "exact_match": {
                        "type": "string",
                        "description": "Specifies whether only the text provided for the search_terms parameter will be returned from the search.EXACT_MATCH\u2014Only exact matches to the text provided for the search_terms parameter will be retu...",
                        "default": None
                },
                "match_name_only": {
                        "type": "string",
                        "description": "Specifies whether the search will be limited to the business name only.MATCH_NAME_ONLY\u2014Only exact matches to the business name provided for the search_terms parameter will be returned.MATCH_ALL_FIELDS...",
                        "default": None
                },
                "filtersfilter_name_filter_value_include": {
                        "type": "string",
                        "description": "The filters that will be applied to the search_terms parameter.filter_name\u2014Set the filter by the dataset field.filter_value\u2014Set the filter by applying a value to the selected field.include\u2014Set the fil...",
                        "default": None
                },
                "max_count": {
                        "type": "string",
                        "description": "The limit for the number of returned \r\nfeatures. The default value is 1,000,000 for local data and 5,000 for online data hosted by ArcGIS Online.The record limit when using\r\non-premises hosted data is...",
                        "default": None
                },
                "business_dataset": {
                        "type": "string",
                        "description": "The dataset that will be used in the business search.",
                        "default": None
                },
                "find_related_poi": {
                        "type": "string",
                        "description": "Specifies whether semantic search will be used to find related items to the search terms.FIND_RELATED_POI\u2014Semantic search will be used.IGNORE_RELATED_POI\u2014Semantic search will not be used. This is the ..."
                },
                "style": {
                        "type": "string",
                        "description": "Specifies the point symbology that will be used for the output feature class.Location\u2014The data will be displayed using a single symbol. This is the default.Place\u2014The data will be displayed using thema...",
                        "default": None
                }
        },
        "required": [
                "out_feature_class",
                "find_related_poi"
        ]
},
    "huff_model": {
        "name": "huff_model",
        "description": "Creates a probability surface to predict the sales potential of an area based on distance and an attractiveness factor.",
        "parameters": {
                "in_facility_features": {
                        "type": "string",
                        "description": "An input point feature layer representing existing facility locations. It is the first feature from the layer or the feature selected when a selection is available."
                },
                "facility_id_field": {
                        "type": "string",
                        "description": "A unique ID field for existing facilities."
                },
                "in_candidate_features": {
                        "type": "string",
                        "description": "An input point feature layer representing new candidate facility locations. It is the first feature from the layer or the feature selected when a selection is available."
                },
                "candidate_id_field": {
                        "type": "string",
                        "description": "A unique ID field for candidate facilities."
                },
                "in_sales_potential_features": {
                        "type": "string",
                        "description": "An input point or polygon feature layer used to calculate the sales potential. It is either all features from a layer or only selected features when a selection is available."
                },
                "sales_potential_id_field": {
                        "type": "string",
                        "description": "A unique ID field for sales potential features."
                },
                "sales_potential_field": {
                        "type": "string",
                        "description": "The field containing the values that will be used to calculate the sales potential."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will contain the tool results representing the probability of sales."
                },
                "attractiveness_variablesexisting_facilities_value_candidates_location_value_exponent": {
                        "type": "string",
                        "description": "The attribute fields that indicate the attractiveness of each competitor. In many cases, the size of the facility is used as a substitute for attractiveness and will be a multivalue table. An addition..."
                },
                "distance_exponent": {
                        "type": "string",
                        "description": "The distance exponent is generally a negative number because attractiveness decreases when distance increases. The default value is -1.5."
                },
                "distance_type": {
                        "type": "string",
                        "description": "The type of distance, based on method of travel, that will be used. The default value is Straight Line.",
                        "default": None
                },
                "distance_units": {
                        "type": "string",
                        "description": "The distance-measuring units that will be used when calculating distance.",
                        "default": None
                },
                "out_distance_matrix": {
                        "type": "string",
                        "description": "The name and location of the matrix table of distance calculations. The IDs for the in_facility_features and in_candidate_features parameters must be unique.",
                        "default": None
                },
                "travel_direction": {
                        "type": "string",
                        "description": "Specifies the direction of travel that will be used between stores and sales potential features.TOWARD_STORES\u2014The direction of travel will be from sales potential features to stores. This is the defau...",
                        "default": None
                },
                "time_of_day": {
                        "type": "string",
                        "description": "The time and date that will be used when calculating distance.",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "Specifies the time zone that will be used for the time_of_day parameter.TIME_ZONE_AT_LOCATION\u2014The time zone in which the territories are located will be used. This is the default.UTC\u2014Coordinated unive...",
                        "default": None
                }
        },
        "required": [
                "in_facility_features",
                "facility_id_field",
                "in_candidate_features",
                "candidate_id_field",
                "in_sales_potential_features",
                "sales_potential_id_field",
                "sales_potential_field",
                "out_feature_class",
                "attractiveness_variablesexisting_facilities_value_candidates_location_value_exponent",
                "distance_exponent"
        ]
},
    "huff_model_calibration": {
        "name": "huff_model_calibration",
        "description": "Calculates exponent values for use in the Huff Model tool.",
        "parameters": {
                "in_facility_features": {
                        "type": "string",
                        "description": "The input point feature class representing competitors or existing stores."
                },
                "facility_id_field": {
                        "type": "string",
                        "description": "A unique ID field representing a store or facility location."
                },
                "in_customer_features": {
                        "type": "string",
                        "description": "The input point feature class representing customer locations."
                },
                "link_field": {
                        "type": "string",
                        "description": "The field that will be used as an ID to assign individual customers to a facility or store."
                },
                "in_sales_potential_features": {
                        "type": "string",
                        "description": "The input polygon feature class used to determine the potential sales market."
                },
                "sales_potential_id_field": {
                        "type": "string",
                        "description": "A unique ID field representing the sales potential area."
                },
                "out_calibration": {
                        "type": "string",
                        "description": "The output calibration file that will contain the calibrated Huff model results, which is the exponent values for the attractiveness variables and distance. The output file extension will be *.huffmod..."
                },
                "attractiveness_variables": {
                        "type": "string",
                        "description": "The fields that will be used to determine the attractiveness of each competitor. In many\r\ncases, the size of the store is used as a substitute for\r\nattractiveness."
                },
                "customer_weight_field": {
                        "type": "string",
                        "description": "A calculated weighted value field assigned to each customer.",
                        "default": None
                },
                "distance_type": {
                        "type": "string",
                        "description": "The method of travel that will be used to calculate distance. The default value is Straight Line.",
                        "default": None
                },
                "distance_units": {
                        "type": "string",
                        "description": "The distance-measuring units that will be used when calculating distance.",
                        "default": None
                },
                "travel_direction": {
                        "type": "string",
                        "description": "Specifies the direction of travel that will be used between stores and sales potential features.TOWARD_STORES\u2014The direction of travel will be from sales potential features to stores. This is the defau...",
                        "default": None
                },
                "time_of_day": {
                        "type": "string",
                        "description": "The time and date that will be used when calculating distance.",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "Specifies the time zone that will be used for the time_of_day parameter.TIME_ZONE_AT_LOCATION\u2014The time zone in which the territories are located will be used. This is the default.UTC\u2014Coordinated unive...",
                        "default": None
                }
        },
        "required": [
                "in_facility_features",
                "facility_id_field",
                "in_customer_features",
                "link_field",
                "in_sales_potential_features",
                "sales_potential_id_field",
                "out_calibration",
                "attractiveness_variables"
        ]
},
    "import_business_analyst_report_template": {
        "name": "import_business_analyst_report_template",
        "description": "Imports an online report so that it can run locally using a locally installed ArcGIS Business Analyst dataset. This tool is the underlying engine that runs the Import Template interactive workflow from the Catalog pane. This tool is ideal for performing more advanced automated tasks, such as importing templates through Python scripting or programmatically modifying data paths. The Import Template workflow will run the tool in the background and add its information to the Geoprocessing history.",
        "parameters": {
                "online_report_template_id": {
                        "type": "string",
                        "description": "The report template ID."
                },
                "output_folder": {
                        "type": "string",
                        "description": "The local folder where the report template items will be imported.",
                        "default": None
                },
                "dataset_id": {
                        "type": "string",
                        "description": "The dataset that will be used to populate the report variables.",
                        "default": None
                },
                "config": {
                        "type": "string",
                        "description": "A JSON string specifying where the report's SDCX variables will be stored. The config options are as follows:id\u2014The portal item ID of the SDCX.download\u2014True or false. Set to true to download the SDCX,...",
                        "default": None
                }
        },
        "required": [
                "online_report_template_id"
        ]
},
    "summary_reports": {
        "name": "summary_reports",
        "description": "Creates infographic and summary reports for a boundary layer using standard or custom templates.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The boundary layer containing one or more polygons that will be used to create reports."
                },
                "report_templates": {
                        "type": "string",
                        "description": "One or more report templates that will be used to create the summary report. You must be signed in to ArcGIS Online or have Business Analyst Data installed."
                },
                "reports_folder": {
                        "type": "string",
                        "description": "The output location where the summary reports will be saved."
                },
                "summarization_options": {
                        "type": "string",
                        "description": "Specifies how the data will be displayed in a report.INDIVIDUAL_FEATURES\u2014Selected report templates will be returned for each individual trade area polygon. This is the default.WHOLE_LAYER\u2014Selected rep...",
                        "default": None
                },
                "single_report": {
                        "type": "string",
                        "description": "Specifies whether a single output will be created or a separate file will be created for each report.CREATE_SINGLE_REPORT\u2014All reports will be combined into a single output.CREATE_REPORT_PER_TEMPLATE\u2014A...",
                        "default": None
                },
                "formats": {
                        "type": "string",
                        "description": "The report output format. The default value is PDF.",
                        "default": None
                },
                "store_id_field": {
                        "type": "string",
                        "description": "The field that will be used to group data for each site in output reports. These field values are not displayed in the header.",
                        "default": None
                },
                "store_name_field": {
                        "type": "string",
                        "description": "The field values that will be displayed in the output report headers that identify the site corresponding to each polygon's data.",
                        "default": None
                },
                "store_address_field": {
                        "type": "string",
                        "description": "The store address associated with each trade area.",
                        "default": None
                },
                "store_latitude_field": {
                        "type": "string",
                        "description": "The field that will contain the latitude coordinates (y field).",
                        "default": None
                },
                "store_longitude_field": {
                        "type": "string",
                        "description": "The field that will contain the longitude coordinates (x field).",
                        "default": None
                },
                "ring_id_field": {
                        "type": "string",
                        "description": "The field that will control the presentation order of data for inputs with multiple polygons per site.",
                        "default": None
                },
                "area_description_field": {
                        "type": "string",
                        "description": "The field that will be displayed as the output template header with values corresponding to each input polygon's data.",
                        "default": None
                },
                "title": {
                        "type": "string",
                        "description": "The title in the report header.",
                        "default": None
                },
                "subtitle": {
                        "type": "string",
                        "description": "The subtitle in the report header. The default value is Prepared by Business Analyst Pro.",
                        "default": None
                },
                "report_per_feature": {
                        "type": "string",
                        "description": "Specifies whether a single report or multiple reports will be created.CREATE_REPORT_PER_FEATURE\u2014A report will be created for each feature.CREATE_SINGLE_REPORT\u2014A single report will be created. This is ...",
                        "default": None
                },
                "add_infographic_header": {
                        "type": "string",
                        "description": "Specifies whether a header will be added to the infographic.ENABLE_INFOGRAPHIC_HEADER\u2014A header will be added to the infographic.DISABLE_INFOGRAPHIC_HEADER\u2014A header will not be added to the infographic...",
                        "default": None
                },
                "add_infographic_footer": {
                        "type": "string",
                        "description": "Specifies whether a footer will be added to the infographic.ENABLE_INFOGRAPHIC_FOOTER\u2014A footer will be added to the infographic.DISABLE_INFOGRAPHIC_FOOTER\u2014A footer will not be added to the infographic...",
                        "default": None
                },
                "add_infographic_data_source": {
                        "type": "string",
                        "description": "Specifies whether the data source will be added to the infographic.ENABLE_INFOGRAPHIC_DATA_SOURCE\u2014The data source will be added to the infographic.DISABLE_INFOGRAPHIC_DATA_SOURCE\u2014The data source will ...",
                        "default": None
                },
                "report_style": {
                        "type": "string",
                        "description": "Specifies the style that will be used for the Esri report.CLASSIC\u2014The generated Esri report will use the traditional style. This is the default.MODERN\u2014The generated Esri report will use the updated st...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "report_templates",
                "reports_folder"
        ]
},
    "generate_sdcx_index": {
        "name": "generate_sdcx_index",
        "description": "Creates an index for a Statistical Data Collection (SDCX). The index will improve performance when using the custom data in analysis tools such as Enrich Layer.",
        "parameters": {
                "sdcx_file": {
                        "type": "string",
                        "description": "The input Statistical Data Collection file (.sdcx)."
                }
        },
        "required": [
                "sdcx_file"
        ]
},
    "add_field_based_suitability_criteria": {
        "name": "add_field_based_suitability_criteria",
        "description": "Adds criteria based on the numerical fields existing in the input layer.",
        "parameters": {
                "in_analysis_layer": {
                        "type": "string",
                        "description": "The Suitability Analysis layer that will be used in the analysis."
                },
                "fields": {
                        "type": "string",
                        "description": "The numeric fields from which the suitability criteria will be determined."
                }
        },
        "required": [
                "in_analysis_layer",
                "fields"
        ]
},
    "add_point_layer_based_suitability_criteria": {
        "name": "add_point_layer_based_suitability_criteria",
        "description": "Adds criteria based on spatial relationships between the input layer and a specified point layer.",
        "parameters": {
                "in_analysis_layer": {
                        "type": "string",
                        "description": "The Suitability Analysis layer that will be used in the analysis."
                },
                "site_layer_id_field": {
                        "type": "string",
                        "description": "A field containing unique values for each record in the Suitability Analysis layer."
                },
                "in_point_features": {
                        "type": "string",
                        "description": "The layer containing point locations that will be added as criteria based on the spatial relationship to the Suitability Analysis layer."
                },
                "criteria_type": {
                        "type": "string",
                        "description": "Specifies the type of spatial relationship that will be used as criteria.COUNT\u2014A count of points that fall within each Suitability Analysis layer polygon will be used as criteria. This is the default...."
                },
                "distance_type": {
                        "type": "string",
                        "description": "The method of travel that will be used to calculate the minimal distance.",
                        "default": None
                },
                "units": {
                        "type": "string",
                        "description": "The unit of measure that will be used when calculating minimal distance.",
                        "default": None
                },
                "in_site_centers_features": {
                        "type": "string",
                        "description": "The point layer that will be used as site centers. This point layer will replace default polygon centroids of the Suitability Analysis layer.",
                        "default": None
                },
                "site_centers_id_field": {
                        "type": "string",
                        "description": "A field in the in_site_centers_features parameter value that uniquely identifies each record.",
                        "default": None
                },
                "weight_field": {
                        "type": "string",
                        "description": "Numeric fields that exist in a point layer that will be selected for weighting."
                },
                "statistics_type": {
                        "type": "string",
                        "description": "Specifies the type of statistical operation that will be applied to the weighted field.SUM\u2014The total of the field values will be calculated for each point feature.AVE\u2014The average field value will be c...",
                        "default": None
                },
                "cutoff_distance": {
                        "type": "string",
                        "description": "The distance beyond which points will not be considered in the calculation.",
                        "default": None
                }
        },
        "required": [
                "in_analysis_layer",
                "site_layer_id_field",
                "in_point_features",
                "criteria_type",
                "weight_field"
        ]
},
    "add_variable_based_suitability_criteria": {
        "name": "add_variable_based_suitability_criteria",
        "description": "Adds criteria based on the values calculated for the input layer using the Enrich Layer tool.",
        "parameters": {
                "in_analysis_layer": {
                        "type": "string",
                        "description": "The Suitability Analysis layer that will be used in the analysis."
                },
                "variables": {
                        "type": "string",
                        "description": "The variables from which the suitability criteria will be determined."
                }
        },
        "required": [
                "in_analysis_layer",
                "variables"
        ]
},
    "calculate_suitability_score": {
        "name": "calculate_suitability_score",
        "description": "Calculates or recalculates a suitability score.",
        "parameters": {
                "in_analysis_layer": {
                        "type": "string",
                        "description": "The Suitability Analysis Layer that will be used in the analysis."
                }
        },
        "required": [
                "in_analysis_layer"
        ]
},
    "make_suitability_analysis_layer": {
        "name": "make_suitability_analysis_layer",
        "description": "Creates a Suitability Analysis group layer for an input site's polygonal layer.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The feature layer that will be used in the creation of the Suitability Analysis layer."
                },
                "layer_name": {
                        "type": "string",
                        "description": "The name of the output Suitability Analysis layer that will be created."
                },
                "out_dataset_path": {
                        "type": "string",
                        "description": "The geodatabase that will contain the output feature dataset.",
                        "default": None
                },
                "out_dataset_name": {
                        "type": "string",
                        "description": "The name of the output feature dataset that will contain the collection of suitability analysis layer feature classes.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "layer_name"
        ]
},
    "remove_suitability_criteria": {
        "name": "remove_suitability_criteria",
        "description": "Removes criteria from a suitability analysis layer.",
        "parameters": {
                "in_analysis_layer": {
                        "type": "string",
                        "description": "The suitability analysis layer from which criteria will be removed."
                },
                "drop_criteria": {
                        "type": "string",
                        "description": "A list of criteria to be removed from a suitability analysis layer."
                }
        },
        "required": [
                "in_analysis_layer",
                "drop_criteria"
        ]
},
    "set_criteria_properties": {
        "name": "set_criteria_properties",
        "description": "Defines parameters for criteria.",
        "parameters": {
                "in_analysis_layer": {
                        "type": "string",
                        "description": "The Suitability Analysis layer that will be used in the analysis."
                },
                "criteria_propertiescriterion_title_weight_influence_ideal_value_minimum_value_maximum_value_enabled": {
                        "type": "string",
                        "description": "The input features that will be used to set up the criteria properties.criterion\u2014The field, point, or variable that will be used to calculate the suitability score.title\u2014The name of the criteria.weigh..."
                },
                "criteria_score_preset": {
                        "type": "string",
                        "description": "Specifies the preprocessing and combination method that will be used when calculating the final score.SUM_SCALED\u2014The sum of scaled values with scores representing the distribution of values for each c...",
                        "default": None
                },
                "preprocessing": {
                        "type": "string",
                        "description": "Specifies the method that will be used to convert the input\r\nvariables to a standardized scale.MINMAX\u2014 Variables will be scaled between 0 and 1 using the minimum and maximum values of each variable. T...",
                        "default": None
                },
                "criteria_score_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to combine the scaled\r\nvariables into a single value.SUM\u2014 The values will be added. This is the default.MEAN\u2014 The arithmetic (additive) mean of the values will b...",
                        "default": None
                },
                "final_score_method": {
                        "type": "string",
                        "description": "Specifies the method that will be used to scale the combined score. This parameter will determine the final score.METHOD_0_1\u2014The final score will be calculated with the lowest value of 0 and the highe...",
                        "default": None
                }
        },
        "required": [
                "in_analysis_layer",
                "criteria_propertiescriterion_title_weight_influence_ideal_value_minimum_value_maximum_value_enabled"
        ]
},
    "set_target_site": {
        "name": "set_target_site",
        "description": "Adds a target site to a Suitability Analysis group layer. A target site is typically a trade area around a high-performing location, such as a store or clinic. Criteria values in the target site are used to score candidate sites that are closest in value to the target site.",
        "parameters": {
                "in_analysis_layer": {
                        "type": "string",
                        "description": "The Suitability Analysis layer that will be used in the analysis."
                },
                "target_site_layer": {
                        "type": "string",
                        "description": "The layer that contains the target site.",
                        "default": None
                },
                "target_site_feature_id": {
                        "type": "string",
                        "description": "The feature from the target site layer that will be added to the group layer as the target site.",
                        "default": None
                }
        },
        "required": [
                "in_analysis_layer"
        ]
},
    "analyze_market_area_gap": {
        "name": "analyze_market_area_gap",
        "description": "Generates a layer that displays the gap between total customers and expected customers. Learn more about Analyze Market Area Gap outputs",
        "parameters": {
                "customer_layer": {
                        "type": "string",
                        "description": "A point layer representing customers."
                },
                "target_profile": {
                        "type": "string",
                        "description": "A segmentation profile representing the segments that will be analyzed. The target profile typically represents your customer segmentation profile."
                },
                "base_profile": {
                        "type": "string",
                        "description": "A segmentation profile representing the base profile segments that will be used for comparison. The base profile typically represents your market area segmentation profile."
                },
                "geography_level": {
                        "type": "string",
                        "description": "The geography level that will be used to define the market area gap analysis layer."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing the market area gap analysis."
                },
                "target_group": {
                        "type": "string",
                        "description": "A collection of segments grouped into targets. Targets represent segments that are selected based on similar characteristics\u2014for example, segments that have high index and percent composition."
                },
                "core_target": {
                        "type": "string",
                        "description": "A group of segments that make up a large percentage of your customer base and have an above average index, indicating likelihood to be a customer."
                },
                "developmental_target": {
                        "type": "string",
                        "description": "A group of segments that make up a significant percentage of your customers and of the market area but do not have an above average index."
                },
                "boundary_layer": {
                        "type": "string",
                        "description": "The boundary that determines the layer extent. If no value is provided, the entire country will be used.",
                        "default": None
                },
                "create_report": {
                        "type": "string",
                        "description": "Specifies whether a  gap analysis report will be created.CREATE_REPORT\u2014A gap analysis report will be created.DO_NOT_CREATE_REPORT\u2014A gap analysis report will not be created. This is the default.",
                        "default": None
                },
                "report_title": {
                        "type": "string",
                        "description": "The title of the report.",
                        "default": None
                },
                "report_folder": {
                        "type": "string",
                        "description": "The output location where the report will be saved.",
                        "default": None
                },
                "report_format": {
                        "type": "string",
                        "description": "Specifies the format of the output report.PDF\u2014The report will be in PDF format. This is the default.XLSX\u2014The report will be in XLSX format.HTML\u2014The report will be in HTML format.CSV\u2014The report will be...",
                        "default": None
                }
        },
        "required": [
                "customer_layer",
                "target_profile",
                "base_profile",
                "geography_level",
                "out_feature_class",
                "target_group",
                "core_target",
                "developmental_target"
        ]
},
    "analyze_market_potential": {
        "name": "analyze_market_potential",
        "description": "Generates a layer that displays expected customers by a selected geography level. Learn more about Analyze Market Potential outputs",
        "parameters": {
                "target_profile": {
                        "type": "string",
                        "description": "A segmentation profile representing the segments that will be analyzed. The target profile typically represents your customer segmentation profile."
                },
                "base_profile": {
                        "type": "string",
                        "description": "A segmentation profile representing the base profile segments that will be used for comparison. The base profile typically represents your market area segmentation profile."
                },
                "geography_level": {
                        "type": "string",
                        "description": "The geography level that will be used to define the market potential layer."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing the market potential analysis."
                },
                "boundary_layer": {
                        "type": "string",
                        "description": "The boundary that determines the layer extent. If no value is provided, the entire country will be used.",
                        "default": None
                },
                "create_report": {
                        "type": "string",
                        "description": "Specifies whether a market potential report will be created.CREATE_REPORT\u2014A market potential report will be created.DO_NOT_CREATE_REPORT\u2014A market potential report will not be created. This is the defa...",
                        "default": None
                },
                "report_title": {
                        "type": "string",
                        "description": "The title of the report.",
                        "default": None
                },
                "report_folder": {
                        "type": "string",
                        "description": "The output location where the report will be saved.",
                        "default": None
                },
                "report_format": {
                        "type": "string",
                        "description": "Specifies the format of the output report.PDF\u2014The report will be in PDF format. This is the default.XLSX\u2014The report will be in XLSX format.HTML\u2014The report will be in HTML format.CSV\u2014The report will be...",
                        "default": None
                }
        },
        "required": [
                "target_profile",
                "base_profile",
                "geography_level",
                "out_feature_class"
        ]
},
    "create_target_group": {
        "name": "create_target_group",
        "description": "Creates a new target group. A target group is a container for targets that you create, name, and populate with segments from a locally installed Business Analyst dataset.",
        "parameters": {
                "target_group": {
                        "type": "string",
                        "description": "The name of the output target group file."
                },
                "input_type": {
                        "type": "string",
                        "description": "Specifies a list of the targets that will be added to the new target group.name\u2014The name of the target.segments\u2014The segments that will be added to the target.color\u2014The color associated with the segmen..."
                }
        },
        "required": [
                "target_group",
                "input_type"
        ]
},
    "export_segmentation_profile": {
        "name": "export_segmentation_profile",
        "description": "Exports a segmentation profile to a table.",
        "parameters": {
                "in_profile": {
                        "type": "string",
                        "description": "The segmentation file that will be exported."
                },
                "out_table_name": {
                        "type": "string",
                        "description": "The name of the table that will be created."
                }
        },
        "required": [
                "in_profile",
                "out_table_name"
        ]
},
    "generate

customer_segmentation_profile": {
        "name": "generate\r\ncustomer_segmentation_profile",
        "description": "Creates a segmentation profile with an existing customer layer.",
        "parameters": {
                "in_customers_layer": {
                        "type": "string",
                        "description": "The input point feature class that represents existing customers."
                },
                "in_segmentation_base": {
                        "type": "string",
                        "description": "The segmentation base for the profile that will be created. Available options are provided by the segmentation dataset in use."
                },
                "out_profile": {
                        "type": "string",
                        "description": "The name of the segmentation profile file that will be created."
                },
                "in_volume_field": {
                        "type": "string",
                        "description": "The field containing volume information from which the profile can be created. For example, you can create a profile using the sales for each customer.",
                        "default": None
                }
        },
        "required": [
                "in_customers_layer",
                "in_segmentation_base",
                "out_profile"
        ]
},
    "generate

market_area_segmentation_profile": {
        "name": "generate\r\nmarket_area_segmentation_profile",
        "description": "Creates a segmentation profile by summarizing segments from standard geography boundaries within the input area.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input feature class with polygon features that will be used to create a segmentation area profile."
                },
                "segmentation_base": {
                        "type": "string",
                        "description": "The segmentation base for the profile being created. The available options are provided by the segmentation dataset in use."
                },
                "out_profile": {
                        "type": "string",
                        "description": "The name of the segmentation profile file that will be created."
                }
        },
        "required": [
                "in_features",
                "segmentation_base",
                "out_profile"
        ]
},
    "generate

segmentation_profile_report": {
        "name": "generate\r\nsegmentation_profile_report",
        "description": "Creates a report that displays segments of your customers and compares them to the study area (base profile).",
        "parameters": {
                "target_profile": {
                        "type": "string",
                        "description": "A segmentation profile representing the segments that will be profiled. The target profile typically represents your customer segmentation profile."
                },
                "base_profile": {
                        "type": "string",
                        "description": "A segmentation profile representing the base profile segments. This is the segmentation that will be used for comparison. The base profile typically represents your market area segmentation profile."
                },
                "report_title": {
                        "type": "string",
                        "description": "The title of the report.",
                        "default": None
                },
                "report_folder": {
                        "type": "string",
                        "description": "The output location where the report will be saved.",
                        "default": None
                },
                "report_format": {
                        "type": "string",
                        "description": "Specifies the format of the output report.PDF\u2014The report will be in PDF format. This is the default.XLSX\u2014The report will be in XLSX format.HTML\u2014The report will be in HTML format.CSV\u2014The report will be...",
                        "default": None
                }
        },
        "required": [
                "target_profile",
                "base_profile"
        ]
},
    "generate_survey_report_for_profile": {
        "name": "generate_survey_report_for_profile",
        "description": "Displays characteristics from the consumer survey data for your target profile to determine customer lifestyle habits and preferences.",
        "parameters": {
                "target_profile": {
                        "type": "string",
                        "description": "A segmentation profile representing the segments that will be analyzed. The target profile typically represents your customer segmentation profile."
                },
                "base_profile": {
                        "type": "string",
                        "description": "A segmentation profile representing the base profile segments. This is the segmentation used for comparison. The base profile typically represents your market area segmentation profile."
                },
                "survey_category": {
                        "type": "string",
                        "description": "A category that contains characteristics from the consumer survey."
                },
                "report_folder": {
                        "type": "string",
                        "description": "The output location where the report will be saved."
                },
                "sort_column": {
                        "type": "string",
                        "description": "Specifies the column that will be used to sort the report.EXPECTED_NUMBER\u2014The report will be sorted based on counts\u2014for example, number of adults. This is the default.INDEX\u2014The report will be sorted b...",
                        "default": None
                },
                "sort_order": {
                        "type": "string",
                        "description": "Specifies the order of the report, based on the sort column, in ascending or descending order.ASCENDING\u2014The report will be sorted in ascending order.DESCENDING\u2014The report will be sorted in descending ...",
                        "default": None
                },
                "report_title": {
                        "type": "string",
                        "description": "The title of the report.",
                        "default": None
                },
                "report_format": {
                        "type": "string",
                        "description": "Specifies the format of the output report.PDF\u2014The report will be in PDF format. This is the default.XLSX\u2014The report will be in XLSX format.HTML\u2014The report will be in HTML format.CSV\u2014The report will be...",
                        "default": None
                }
        },
        "required": [
                "target_profile",
                "base_profile",
                "survey_category",
                "report_folder"
        ]
},
    "generate_survey_report_for_targets": {
        "name": "generate_survey_report_for_targets",
        "description": "Displays the top characteristics, in each of the selected survey categories, of your Core and Developmental target groups, as well as your overall customer profile.",
        "parameters": {
                "target_profile": {
                        "type": "string",
                        "description": "A segmentation profile representing the segments that will be analyzed. The target profile typically represents your customer segmentation profile."
                },
                "target_group": {
                        "type": "string",
                        "description": "A collection of segments grouped into targets. Targets represent segments that are selected based on similar characteristics, for example, segments that have high index and percent composition."
                },
                "core_target": {
                        "type": "string",
                        "description": "A group of segments that comprise a large percentage of your customer base and have an above average index, indicating likelihood to be a customer."
                },
                "developmental_target": {
                        "type": "string",
                        "description": "A group of segments that comprise a significant percentage of your customers and of the market area but do not have an above average index."
                },
                "report_folder": {
                        "type": "string",
                        "description": "The output location where the report will be saved."
                },
                "report_type": {
                        "type": "string",
                        "description": "Specifies the survey characteristics that will be added to the report.UNDERSTANDING_YOUR_TARGET\u2014Media-related characteristics will be added to the report, for example, reading, watching, and listening...",
                        "default": None
                },
                "survey_categories": {
                        "type": "string",
                        "description": "A category that contains the characteristics from the consumer survey.",
                        "default": None
                },
                "report_title": {
                        "type": "string",
                        "description": "The title of the report.",
                        "default": None
                },
                "report_format": {
                        "type": "string",
                        "description": "Specifies the format of the output report.PDF\u2014The report will be in PDF format. This is the default.XLSX\u2014The report will be in XLSX format.HTML\u2014The report will be in HTML format.CSV\u2014The report will be...",
                        "default": None
                }
        },
        "required": [
                "target_profile",
                "target_group",
                "core_target",
                "developmental_target",
                "report_folder"
        ]
},
    "generate_target_group_layer": {
        "name": "generate_target_group_layer",
        "description": "Generates a layer that identifies geographies that contain selected segments and categorized groups based on targets.",
        "parameters": {
                "geography_level": {
                        "type": "string",
                        "description": "The geography level that will be used to define the target layer."
                },
                "segmentation_base": {
                        "type": "string",
                        "description": "The segmentation base for the profile being created. The available options are provided by the segmentation dataset in use."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class for the target layer."
                },
                "target_group": {
                        "type": "string",
                        "description": "A user-created group of targets. This is used if the dataset supports target groups."
                },
                "boundary_layer": {
                        "type": "string",
                        "description": "The boundary that will determine the layer extent.",
                        "default": None
                }
        },
        "required": [
                "geography_level",
                "segmentation_base",
                "out_feature_class",
                "target_group"
        ]
},
    "generate_target_layer": {
        "name": "generate_target_layer",
        "description": "Creates a layer that identifies geographies that contain selected segments and geographies that do not contain selected segments.",
        "parameters": {
                "geography_level": {
                        "type": "string",
                        "description": "The geography level that will be used to define the target layer."
                },
                "segmentation_base": {
                        "type": "string",
                        "description": "The segmentation base for the profile being created. The available options are provided by the segmentation dataset in use."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class for the target layer."
                },
                "input_type": {
                        "type": "string",
                        "description": "Specifies the target input type.USE_TARGET_GROUP\u2014A target group will be used as the input type.SELECT_SEGMENTS\u2014Segments will be used as the input type. One or more segments can compose a target."
                },
                "target_group": {
                        "type": "string",
                        "description": "The target group, if the dataset supports target groups.",
                        "default": None
                },
                "target": {
                        "type": "string",
                        "description": "A target from the target_group parameter value.",
                        "default": None
                },
                "segments": {
                        "type": "string",
                        "description": "The segments from the provided dataset.",
                        "default": None
                },
                "boundary_layer": {
                        "type": "string",
                        "description": "The boundary that will determine the layer extent.",
                        "default": None
                }
        },
        "required": [
                "geography_level",
                "segmentation_base",
                "out_feature_class",
                "input_type"
        ]
},
    "generate_target_penetration_layer": {
        "name": "generate_target_penetration_layer",
        "description": "Generates a layer based on the percent of penetration of selected segments, providing a detailed view of the concentrations of the target segments.",
        "parameters": {
                "geography_level": {
                        "type": "string",
                        "description": "The geography level that will be used to define the target layer."
                },
                "segmentation_base": {
                        "type": "string",
                        "description": "The segmentation base for the profile being created. The available options are provided by the segmentation dataset in use."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class for the target layer."
                },
                "input_type": {
                        "type": "string",
                        "description": "Specifies the target input type.USE_TARGET_GROUP\u2014A target group will be used as the input type.SELECT_SEGMENTS\u2014Selected segments will be used as the input type. One or more segments can compose a targ..."
                },
                "target_group": {
                        "type": "string",
                        "description": "A user-created group of targets. This parameter is used when the dataset supports target groups.",
                        "default": None
                },
                "target": {
                        "type": "string",
                        "description": "A target from the target_group parameter value.",
                        "default": None
                },
                "segments": {
                        "type": "string",
                        "description": "The segments from the provided dataset.",
                        "default": None
                },
                "boundary_layer": {
                        "type": "string",
                        "description": "The boundary that will determine the extent of the analysis.",
                        "default": None
                }
        },
        "required": [
                "geography_level",
                "segmentation_base",
                "out_feature_class",
                "input_type"
        ]
},
    "import_segmentation_profile": {
        "name": "import_segmentation_profile",
        "description": "Generates a segmentation profile from a table.",
        "parameters": {
                "in_table": {
                        "type": "string",
                        "description": "The input table with segmentation information."
                },
                "segmentation_base": {
                        "type": "string",
                        "description": "The segmentation base for the profile being created. Available options are provided by the segmentation dataset in use."
                },
                "out_profile": {
                        "type": "string",
                        "description": "The name of the segmentation file that will be created."
                },
                "segment_id_field": {
                        "type": "string",
                        "description": "A string field that contains the segmentation code."
                },
                "count_field": {
                        "type": "string",
                        "description": "A numeric field that contains segment count information."
                },
                "total_volume_field": {
                        "type": "string",
                        "description": "A numeric field that contains volume information.",
                        "default": None
                }
        },
        "required": [
                "in_table",
                "segmentation_base",
                "out_profile",
                "segment_id_field",
                "count_field"
        ]
},
    "import_survey_profiles": {
        "name": "import_survey_profiles",
        "description": "Imports segmentation profiles consisting of survey variable data.",
        "parameters": {
                "profiles": {
                        "type": "string",
                        "description": "The categories of survey variables that can be selected for importing as profiles."
                },
                "out_folder": {
                        "type": "string",
                        "description": "The folder that will contain the imported profiles."
                }
        },
        "required": [
                "profiles",
                "out_folder"
        ]
},
    "assign_customers_by_distance": {
        "name": "assign_customers_by_distance",
        "description": "Assigns customers to the closest store based on a selected distance type.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point feature layer representing customers."
                },
                "in_store_features": {
                        "type": "string",
                        "description": "The input point feature layer representing store or facilities."
                },
                "store_id_field": {
                        "type": "string",
                        "description": "A unique ID field for in_store_features."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "A point layer containing customers with assigned store or facility and distance."
                },
                "link_field": {
                        "type": "string",
                        "description": "A new field that contains the assigned store or facility ID.",
                        "default": None
                },
                "distance_type": {
                        "type": "string",
                        "description": "The method of travel used to calculate the distance between customers and stores.",
                        "default": None
                },
                "distance_units": {
                        "type": "string",
                        "description": "The units that will be used to measure the selected distance type.",
                        "default": None
                },
                "travel_direction": {
                        "type": "string",
                        "description": "Specifies the direction of travel that will be used between stores or facilities and customers.TOWARD_STORES\u2014The direction of travel will be from customers to stores. This is the default.AWAY_FROM_STO...",
                        "default": None
                },
                "time_of_day": {
                        "type": "string",
                        "description": "The time and date that will be used when calculating distance.",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "Specifies the time zone that will be used for the time_of_day parameter.TIME_ZONE_AT_LOCATION\u2014The time zone in which the territories are located will be used. This is the default.UTC\u2014Coordinated unive...",
                        "default": None
                },
                "search_tolerance": {
                        "type": "string",
                        "description": "The maximum distance that input points can be from the network. Points located beyond the search tolerance will be excluded from processing.The parameter requires a distance value and units for the to...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "in_store_features",
                "store_id_field",
                "out_feature_class"
        ]
},
    "generate_approximate_drive_times": {
        "name": "generate_approximate_drive_times",
        "description": "Creates trade areas that approximate the size, shape, and area of existing polygons using available routes from the selected distance type.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input  polygon feature layer."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing the drive time polygons."
                },
                "distance_type": {
                        "type": "string",
                        "description": "The method of travel used to create the output polygons."
                },
                "units": {
                        "type": "string",
                        "description": "The distance units to be used with the threshold values.",
                        "default": None
                },
                "in_stores_layer": {
                        "type": "string",
                        "description": "A point layer that will be used as the starting point for creating network service areas.",
                        "default": None
                },
                "store_id_field": {
                        "type": "string",
                        "description": "The ID that uniquely identifies each in_stores_layer point.",
                        "default": None
                },
                "link_field": {
                        "type": "string",
                        "description": "The ID that uniquely identifies each in_features point.",
                        "default": None
                },
                "iterations_limit": {
                        "type": "string",
                        "description": "The maximum number of drive times that can be used to find the optimal threshold limit.",
                        "default": None
                },
                "minimum_step": {
                        "type": "string",
                        "description": "The minimum increment distance or time\u2014for example, 1 mile or 1 min\u2014that will be used between iterations to expand until the threshold is reached.",
                        "default": None
                },
                "target_percent_diff": {
                        "type": "string",
                        "description": "The maximum difference between the target value and threshold value when determining the threshold drive time, for example, 5 percent. The default value is 5.",
                        "default": None
                },
                "travel_direction": {
                        "type": "string",
                        "description": "Specifies the direction of travel toward or away from stores.TOWARD_STORES\u2014  The direction of travel will be toward stores. This is the default.AWAY_FROM_STORES\u2014 The direction of travel will be away f...",
                        "default": None
                },
                "time_of_day": {
                        "type": "string",
                        "description": "The time and date that will be used when calculating distance.",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "Specifies the time zone that will be used for the time_of_day parameter.TIME_ZONE_AT_LOCATION\u2014The time zone in which the territories are located will be used. This is the default.UTC\u2014Coordinated unive...",
                        "default": None
                },
                "search_tolerance": {
                        "type": "string",
                        "description": "The maximum distance that input points can be from the network.The default value is 5000 meters.",
                        "default": None
                },
                "polygon_detail": {
                        "type": "string",
                        "description": "Specifies the level of detail that will be used for the output drive time polygons.STANDARD\u2014Polygons with a standard level of detail will be created. This is the default.GENERALIZED\u2014Generalized polygo...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "distance_type"
        ]
},
    "generate_customer_derived_trade_areas": {
        "name": "generate_customer_derived_trade_areas",
        "description": "Creates trade areas around stores based on the number of customers or volume attribute of each customer.",
        "parameters": {
                "in_stores_layer": {
                        "type": "string",
                        "description": "A point layer representing store or facility locations."
                },
                "store_id_field": {
                        "type": "string",
                        "description": "The unique ID field representing a store or facility location."
                },
                "in_customers_layer": {
                        "type": "string",
                        "description": "An input point layer representing customers or patrons."
                },
                "link_field": {
                        "type": "string",
                        "description": "An ID field that will be used to assign individual customers to stores."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output trade area feature class."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies the type of customer-derived trade area that will be generated.SIMPLE\u2014A generalized trade area based on the percentages of customers corresponding to each store will be generated.AMOEBA\u2014Poin..."
                },
                "rings": {
                        "type": "string",
                        "description": "The values that will be used to represent the percentage of customers, for example, total count or a customer attribute and total sales assigned to each store. Each value represents one trade area pol..."
                },
                "customer_aggregation_type": {
                        "type": "string",
                        "description": "Specifies the type of aggregation that will be used.COUNT\u2014Percentage-based trade areas will be calculated using the geographic locations of customers. This is the default.WEIGHT\u2014Percentage-based trade..."
                },
                "customer_weight_field": {
                        "type": "string",
                        "description": "The field that will be used to calculate the trade areas. This is based on either the number of customers (count) or the calculated weighted value assigned to each customer.",
                        "default": None
                },
                "exclude_outlying_customers": {
                        "type": "string",
                        "description": "Specifies whether outlying customers will be excluded from the trade area generation.EXCLUDE_OUTLIERS\u2014Outlying customers will be excluded.ALL_POINTS\u2014Outlying customers will not be excluded; all custom...",
                        "default": None
                },
                "cutoff_distance": {
                        "type": "string",
                        "description": "The distance beyond which customers will be considered outliers and excluded from consideration during trade area generation.",
                        "default": None
                },
                "dissolve_option": {
                        "type": "string",
                        "description": "Specifies whether polygons of the entire area will be created or the polygons will be split into individual features. When the method parameter is set to THRESHOLD_DRIVETIMES, the only available optio...",
                        "default": None
                },
                "use_customer_centroids": {
                        "type": "string",
                        "description": "Specifies whether the centroid of your customer area will be used to calculate trade areas outward from this point.USE_CENTROIDS\u2014The centroid of customer points will be used to calculate trade areas.U...",
                        "default": None
                },
                "distance_type": {
                        "type": "string",
                        "description": "The method of travel that will be used to calculate the distance.",
                        "default": None
                },
                "units": {
                        "type": "string",
                        "description": "The units that will be used for the distance values.",
                        "default": None
                },
                "travel_direction": {
                        "type": "string",
                        "description": "Specifies the direction of travel toward or away from stores.TOWARD_STORES\u2014  The direction of travel will be toward stores. This is the default.AWAY_FROM_STORES\u2014 The direction of travel will be away f...",
                        "default": None
                },
                "time_of_day": {
                        "type": "string",
                        "description": "The time and date that will be used when calculating distance.",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "Specifies the time zone that will be used for the time_of_day parameter.TIME_ZONE_AT_LOCATION\u2014The time zone in which the territories are located will be used. This is the default.UTC\u2014Coordinated unive...",
                        "default": None
                },
                "search_tolerance": {
                        "type": "string",
                        "description": "The maximum distance that input points can be from the network. Points located beyond the search tolerance will be excluded from processing.This parameter requires a distance value and units for the t...",
                        "default": None
                },
                "polygon_detail": {
                        "type": "string",
                        "description": "Specifies the level of detail that will be used for the output drive time polygons.STANDARD\u2014 Polygons with a standard level of detail will be created. This is the default.GENERALIZED\u2014Generalized polyg...",
                        "default": None
                },
                "iterations_limit": {
                        "type": "string",
                        "description": "Restricts the number of drive times that can be used to find the optimal threshold limit.",
                        "default": None
                },
                "minimum_step": {
                        "type": "string",
                        "description": "The minimum increment distance or time\u2014for example, 1 mile or 1 minute\u2014that will be used between iterations to expand until the threshold is reached.",
                        "default": None
                },
                "target_percent_diff": {
                        "type": "string",
                        "description": "The maximum percentage difference between the target value and threshold value that will be used when determining the threshold drive time, for example, 5 percent. The default value is 5.",
                        "default": None
                }
        },
        "required": [
                "in_stores_layer",
                "store_id_field",
                "in_customers_layer",
                "link_field",
                "out_feature_class",
                "method",
                "rings",
                "customer_aggregation_type"
        ]
},
    "generate_drive_time_trade_area": {
        "name": "generate_drive_time_trade_area",
        "description": "Creates a feature class of trade areas around point features based on travel time and distance.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point feature layer."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing the drive time polygons."
                },
                "distance_type": {
                        "type": "string",
                        "description": "The method of travel that will be used for drive time calculation."
                },
                "distances": {
                        "type": "string",
                        "description": "The distances that will be used for drive time calculations."
                },
                "units": {
                        "type": "string",
                        "description": "The units that will be used for the distance values. The default value is miles.",
                        "default": None
                },
                "id_field": {
                        "type": "string",
                        "description": "A unique ID field for existing facilities.",
                        "default": None
                },
                "dissolve_option": {
                        "type": "string",
                        "description": "Specifies whether overlapping or nonoverlapping service areas for a single location will be used when multiple distances are specified.\r\nOVERLAP\u2014 Each polygon will include the area reachable from the ...",
                        "default": None
                },
                "remove_overlap": {
                        "type": "string",
                        "description": "Specifies whether overlapping concentric rings will be created or overlap will be removed from multiple locations in relation to one another.REMOVE_OVERLAP\u2014Polygons will be split and the overlap betwe...",
                        "default": None
                },
                "travel_direction": {
                        "type": "string",
                        "description": "Specifies the direction of travel toward or away from stores.TOWARD_STORES\u2014  The direction of travel will be toward stores. This is the default.AWAY_FROM_STORES\u2014 The direction of travel will be away f...",
                        "default": None
                },
                "time_of_day": {
                        "type": "string",
                        "description": "The time and date that will be used when calculating distance.",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "Specifies the time zone that will be used for the time_of_day parameter.TIME_ZONE_AT_LOCATION\u2014The time zone in which the territories are located will be used. This is the default.UTC\u2014Coordinated unive...",
                        "default": None
                },
                "search_tolerance": {
                        "type": "string",
                        "description": "The maximum distance that input points can be from the network. Points located beyond the search tolerance will be excluded from processing.This parameter requires a distance value and units for the t...",
                        "default": None
                },
                "polygon_detail": {
                        "type": "string",
                        "description": "Specifies the level of detail that will be used for the output drive time polygons.STANDARD\u2014 Polygons with a standard level of detail will be created. This is the default.GENERALIZED\u2014Generalized polyg...",
                        "default": None
                },
                "input_method": {
                        "type": "string",
                        "description": "Specifies the type of value that will be used for each drive time.VALUES\u2014A constant value will be used (all trade areas will be the same size). This is the default.EXPRESSION\u2014 The values from a field ...",
                        "default": None
                },
                "expression": {
                        "type": "string",
                        "description": "A fields-based expression used to calculate drive time.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "distance_type",
                "distances"
        ]
},
    "generate_geographies_from_overlay": {
        "name": "generate_geographies_from_overlay",
        "description": "Generates trade areas from the features of an input standard geography level that has a specified spatial relationship with the input.",
        "parameters": {
                "geography_level": {
                        "type": "string",
                        "description": "The geography level that will be used to define the trade area."
                },
                "in_features": {
                        "type": "string",
                        "description": "The features that will be used to extract the standard geography level features by the specified spatial relationship. It can be either all features from the layer or only those selected once a select..."
                },
                "id_field": {
                        "type": "string",
                        "description": "The field that will be used to identify the in_features parameter value\u2014for example, the IDs of drive time polygons."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature containing the trade area."
                },
                "overlap_type": {
                        "type": "string",
                        "description": "Specifies how the subgeography will be selected from the boundary layer.INTERSECT\u2014If any of the subgeography features touch or intersect the boundary layer, they will be included in the output layer. ...",
                        "default": None
                },
                "ratios": {
                        "type": "string",
                        "description": "Specifies how percentages will be calculated. The percentages are generated based on how much each geography\r\nintersects the boundary layer and appends the values to the\r\ngeography layer.\r\nNO_RATIOS\u2014N...",
                        "default": None
                }
        },
        "required": [
                "geography_level",
                "in_features",
                "id_field",
                "out_feature_class"
        ]
},
    "generate_standard_geography_trade_areas": {
        "name": "generate_standard_geography_trade_areas",
        "description": "Creates trade areas based on predefined named statistical areas. This tool does not consume credits.",
        "parameters": {
                "geography_level": {
                        "type": "string",
                        "description": "The geography level that will be used to define the trade area."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature containing the trade area."
                },
                "input_type": {
                        "type": "string",
                        "description": "Specifies whether the geography IDs will be from a table or a list.TABLE\u2014The input IDs will be from a table.LIST\u2014The input IDs will be from a list. This is the default.",
                        "default": None
                },
                "in_ids_table": {
                        "type": "string",
                        "description": "The input table with IDs that will be used to select geographies that will define the trade area.",
                        "default": None
                },
                "geography_key_field": {
                        "type": "string",
                        "description": "A field in the in_ids_table parameter value that identifies the records that will be included in the output.",
                        "default": None
                },
                "ids_list": {
                        "type": "string",
                        "description": "The input list of comma-separated geography IDs.",
                        "default": None
                },
                "summarize_duplicates": {
                        "type": "string",
                        "description": "Specifies whether duplicate fields in the table containing\r\nmatching geography IDs will be summarized.SUMMARIZE_DUPLICATES\u2014The numeric fields for all duplicate records will be summarized.USE_FIRST\u2014The...",
                        "default": None
                },
                "group_field": {
                        "type": "string",
                        "description": "The field that will be used to perform a group by operation.",
                        "default": None
                },
                "dissolve_output": {
                        "type": "string",
                        "description": "Specifies whether the output will be dissolved based on the group_field parameter value.DISSOLVE\u2014The output will be dissolved.DONT_DISSOLVE\u2014The output will not be dissolved. This is the default.",
                        "default": None
                }
        },
        "required": [
                "geography_level",
                "out_feature_class"
        ]
},
    "generate_threshold_drive_times": {
        "name": "generate_threshold_drive_times",
        "description": "Creates a feature class of network distance trade areas that expand around point features until criteria is reached.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point feature layer."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing the drive time polygons."
                },
                "threshold_variable": {
                        "type": "string",
                        "description": "The selected Business Analyst dataset variable to which the threshold value will be applied.Threshold variables must be numeric. No other statistic type is supported."
                },
                "threshold_values": {
                        "type": "string",
                        "description": "The threshold variable value that will determine the size of the output rings. The rings will expand until they contain the threshold value of the selected variable."
                },
                "distance_type": {
                        "type": "string",
                        "description": "The method of travel that will be used to create the output polygons."
                },
                "units": {
                        "type": "string",
                        "description": "The distance units that will be used with the threshold values.",
                        "default": None
                },
                "id_field": {
                        "type": "string",
                        "description": "The ID that uniquely identifies each input point and is included in the output as an attribute.",
                        "default": None
                },
                "travel_direction": {
                        "type": "string",
                        "description": "Specifies the direction of travel toward or away from stores.TOWARD_STORES\u2014  The direction of travel will be toward stores. This is the default.AWAY_FROM_STORES\u2014 The direction of travel will be away f...",
                        "default": None
                },
                "time_of_day": {
                        "type": "string",
                        "description": "The time and date that will be used when calculating distance.",
                        "default": None
                },
                "time_zone": {
                        "type": "string",
                        "description": "Specifies the time zone that will be used for the Time of Day parameter.TIME_ZONE_AT_LOCATION\u2014The time zone in which the territories are located will be used. This is the default.UTC\u2014Coordinated unive...",
                        "default": None
                },
                "search_tolerance": {
                        "type": "string",
                        "description": "The maximum distance that input points can be from the network.The default value is 5,000 meters.",
                        "default": None
                },
                "polygon_detail": {
                        "type": "string",
                        "description": "Specifies the level of detail that will be used for the output drive time polygons.STANDARD\u2014Polygons with a standard level of detail will be created. This is the default.GENERALIZED\u2014Generalized polygo...",
                        "default": None
                },
                "iterations_limit": {
                        "type": "string",
                        "description": "Restricts the number of drive times that can be used to find the optimal threshold limit.",
                        "default": None
                },
                "minimum_step": {
                        "type": "string",
                        "description": "The minimum distance between one threshold area candidate and the next as the model approaches the threshold value to prevent infinite iterations.",
                        "default": None
                },
                "target_percent_diff": {
                        "type": "string",
                        "description": "The maximum percentage difference between the target value and threshold value that will be used when determining the threshold drive time, for example, 5 percent. The default value is 5.",
                        "default": None
                },
                "input_method": {
                        "type": "string",
                        "description": "Specifies the type of value that will be used for each drive time.VALUES\u2014A constant value will be used (all trade areas will be the same size). This is the default.EXPRESSION\u2014The values from a field o...",
                        "default": None
                },
                "expression": {
                        "type": "string",
                        "description": "A fields-based expression that will be used to calculate drive time.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "threshold_variable",
                "threshold_values",
                "distance_type"
        ]
},
    "generate_threshold_rings": {
        "name": "generate_threshold_rings",
        "description": "Creates a feature class of ring trade areas that expand around point features until the threshold value is reached.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input point feature layer."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class containing the threshold rings."
                },
                "threshold_variable": {
                        "type": "string",
                        "description": "The selected Business Analyst dataset variable to which the threshold value will be applied.Threshold variables must be numeric. No other statistic type is supported."
                },
                "threshold_values": {
                        "type": "string",
                        "description": "The threshold variable value that will determine the size of the output rings. The rings will expand until they contain the threshold value of the selected variable."
                },
                "units": {
                        "type": "string",
                        "description": "The distance units that will be used with the threshold values.",
                        "default": None
                },
                "id_field": {
                        "type": "string",
                        "description": "The ID that uniquely identifies each input point and is included in the output as an attribute.",
                        "default": None
                },
                "input_method": {
                        "type": "string",
                        "description": "Specifies the type of value that will be used for each drive time.VALUES\u2014A constant value will be used (all trade areas will be the same size). This is the default.EXPRESSION\u2014The values from a field o...",
                        "default": None
                },
                "expression": {
                        "type": "string",
                        "description": "A fields-based expression that will be used to calculate the radii.",
                        "default": None
                },
                "minimum_step": {
                        "type": "string",
                        "description": "The minimum distance between one threshold area candidate and the next as the model approaches the threshold value to prevent infinite iterations.",
                        "default": None
                },
                "target_percent_diff": {
                        "type": "string",
                        "description": "The maximum percentage difference between the target value and threshold value that will be used when determining the threshold drive time, for example, 5 percent. The default value is 5.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class",
                "threshold_variable",
                "threshold_values"
        ]
},
    "generate_trade_area_rings": {
        "name": "generate_trade_area_rings",
        "description": "Creates rings around point locations.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features containing the center points for the rings."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class that will contain the output ring features."
                },
                "radii": {
                        "type": "string",
                        "description": "The distances, in ascending size, used to create rings around the input features.",
                        "default": None
                },
                "units": {
                        "type": "string",
                        "description": "The linear unit to be used with the distance values.",
                        "default": None
                },
                "id_field": {
                        "type": "string",
                        "description": "A unique ID field in the ring center layer.",
                        "default": None
                },
                "remove_overlap": {
                        "type": "string",
                        "description": "Creates overlapping concentric rings or removes overlap.REMOVE_OVERLAP\u2014Thiessen polygons are used to remove overlap between output ring polygons.KEEP_OVERLAP\u2014Output ring features are created with over...",
                        "default": None
                },
                "dissolve_option": {
                        "type": "string",
                        "description": "Specifies whether overlapping or nonoverlapping service areas for a single location will be used when multiple distances are specified.\r\nOVERLAP\u2014Each polygon will include the area reachable from the f...",
                        "default": None
                },
                "input_method": {
                        "type": "string",
                        "description": "Specifies the type of value that is to be used for each drive time.VALUES\u2014Uses a constant value (all trade areas will be the same size). This is the default.EXPRESSION\u2014The values from a field or an ex...",
                        "default": None
                },
                "expression": {
                        "type": "string",
                        "description": "A fields-based expression to calculate the radii.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "measure_cannibalization": {
        "name": "measure_cannibalization",
        "description": "Calculates the amount of overlap between two or more polygons. Overlap refers to the extent of the polygons beyond intersection. An optional report can be created detailing overlapped statistics.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input polygon features that will be analyzed for overlap."
                },
                "area_id_field": {
                        "type": "string",
                        "description": "The field that uniquely identifies each feature in the input layer."
                },
                "area_description_field": {
                        "type": "string",
                        "description": "The field that describes each feature in the input layer."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The output feature class that will contain the areas of overlap found in the input layer."
                },
                "store_id_field": {
                        "type": "string",
                        "description": "The unique ID that associates a store with each polygon when the inputs are trade areas.",
                        "default": None
                },
                "create_report": {
                        "type": "string",
                        "description": "Specifies whether a report will be generated.CREATE_REPORT\u2014A report will be generated.DO_NOT_CREATE_REPORT\u2014A report will not be generated. This is the default.",
                        "default": None
                },
                "report_title": {
                        "type": "string",
                        "description": "The title of the report. The default value is Measure Cannibalization.",
                        "default": None
                },
                "report_folder": {
                        "type": "string",
                        "description": "The output location where the report will be saved.",
                        "default": None
                },
                "report_format": {
                        "type": "string",
                        "description": "The output format or formats of the report.",
                        "default": None
                },
                "variables": {
                        "type": "string",
                        "description": "One or more variables that will be used to calculate additional overlap metrics\u2014for example, the total number of people and households in intersection areas, or the percentage of the total number of p...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "area_id_field",
                "area_description_field",
                "out_feature_class"
        ]
},
    "remove_overlap": {
        "name": "remove_overlap",
        "description": "Removes overlap between two or more areas to form adjacent boundaries.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features containing the overlapping polygons."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class containing the new trade area features."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies how the overlap between trade areas will be removed.CENTER_LINE\u2014 Overlap will be removed by creating a border that evenly distributes the area of intersection between polygons. This is the d...",
                        "default": None
                },
                "define_trade_area": {
                        "type": "string",
                        "description": "Specifies whether ring overlap in a trade area will be removed.DEFINE_TRADE_AREA\u2014Overlap will only be removed between polygons with equal values in the ring_id_field parameter.DO_NOT_DEFINE_TRADE_AREA...",
                        "default": None
                },
                "ring_id_field": {
                        "type": "string",
                        "description": "A field from the input  that defines common trade areas. Overlap between polygons will only be removed if their values in this field are equal.",
                        "default": None
                },
                "weight_field": {
                        "type": "string",
                        "description": "A field from the input used to influence removal of overlap based on its values.",
                        "default": None
                },
                "store_id": {
                        "type": "string",
                        "description": "A unique ID field in the stores feature layer.",
                        "default": None
                },
                "in_stores_layer": {
                        "type": "string",
                        "description": "The input features containing the center points for the overlapping\r\ntrade areas.",
                        "default": None
                },
                "link_field": {
                        "type": "string",
                        "description": "A unique ID field representing a store or facility location.",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
},
    "remove_overlap_(multiple)": {
        "name": "remove_overlap_(multiple)",
        "description": "Removes overlap between polygons contained in multiple input layers.",
        "parameters": {
                "in_features": {
                        "type": "string",
                        "description": "The input features containing the overlapping polygons."
                },
                "out_feature_class": {
                        "type": "string",
                        "description": "The feature class containing the new trade area features."
                },
                "method": {
                        "type": "string",
                        "description": "Specifies how the overlap between trade areas will be removed.\r\nCENTER_LINE\u2014Overlap will be removed by creating a border that evenly distributes the overlapping area between polygons. This is the simp...",
                        "default": None
                },
                "join_attributes": {
                        "type": "string",
                        "description": "Specifies the attributes of the input layers that will be transferred to the output.ALL\u2014All attributes from the input features will be transferred to the output feature class. This is the default.NO_F...",
                        "default": None
                }
        },
        "required": [
                "in_features",
                "out_feature_class"
        ]
}
}
