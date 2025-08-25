"""
Function Declarations for AI Models
"""

class FunctionDeclaration:
    """Store function declarations for different AI models

    Provides a simple mapping `functions_declarations` where keys are
    function names and values are small metadata objects (description,
    and optionally parameters). This is used by the AI layer to know
    what functions are available and their purpose.
    """

    functions_declarations = {
        "select_by_attribute": {
            "name": "select_by_attribute",
            "description": "Execute attribute-based selection on a GIS layer using SQL-like WHERE clause conditions.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to perform selection on"
                },
                "where_clause": {
                    "type": "string",
                    "description": "SQL WHERE clause for attribute selection (e.g., 'POPULATION > 1000000')"
                },
                "selection_type": {
                    "type": "string",
                    "description": "Type of selection to perform",
                    "enum": ["NEW_SELECTION", "ADD_TO_SELECTION", "REMOVE_FROM_SELECTION", "SUBSET_SELECTION"],
                    "default": "NEW_SELECTION"
                }
            },
            "required": ["layer_name", "where_clause"]
        },
        
        "select_by_location": {
            "name": "select_by_location",
            "description": "Execute spatial selection between two layers based on their spatial relationship.",
            "parameters": {
                "input_layer": {
                    "type": "string",
                    "description": "The input layer to select features from"
                },
                "select_layer": {
                    "type": "string", 
                    "description": "The layer used to define the spatial selection criteria"
                },
                "relationship": {
                    "type": "string",
                    "description": "Spatial relationship for selection",
                    "enum": ["INTERSECT", "WITHIN", "CONTAINS", "WITHIN_A_DISTANCE", "HAVE_THEIR_CENTER_IN", 
                            "COMPLETELY_CONTAINS", "COMPLETELY_WITHIN", "CLOSEST", "BOUNDARY_TOUCHES", 
                            "SHARE_A_LINE_SEGMENT_WITH", "CROSSED_BY_THE_OUTLINE_OF"],
                    "default": "INTERSECT"
                }
            },
            "required": ["input_layer", "select_layer"]
        },
        
        # Rest of the function declarations can be added here

        "get_field_statistics": {
            "name": "get_field_statistics",
            "description": "Calculate comprehensive statistical analysis for a numeric field in a GIS layer.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer containing the field"
                },
                "field_name": {
                    "type": "string",
                    "description": "The name of the numeric field to analyze"
                },
                "where_clause": {
                    "type": "string",
                    "description": "Optional SQL WHERE clause to filter records before calculation",
                    "default": None
                }
            },
            "required": ["layer_name", "field_name"]
        },
        
        "get_layer_summary": {
            "name": "get_layer_summary",
            "description": "Get comprehensive summary information about a GIS layer including geometry type, feature count, fields, and spatial reference.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to summarize"
                }
            },
            "required": ["layer_name"]
        },
        
        "calculate_area": {
            "name": "calculate_area",
            "description": "Calculate area measurements for all polygon features in a layer with unit conversion options.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the polygon layer"
                },
                "units": {
                    "type": "string",
                    "description": "Units for area calculation",
                    "enum": ["square_meters", "square_kilometers", "acres", "hectares"],
                    "default": "square_meters"
                }
            },
            "required": ["layer_name"]
        },
        
        "calculate_length": {
            "name": "calculate_length",
            "description": "Calculate length measurements for all line features in a layer with unit conversion options.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the line layer"
                },
                "units": {
                    "type": "string",
                    "description": "Units for length calculation",
                    "enum": ["meters", "kilometers", "feet", "miles"],
                    "default": "meters"
                }
            },
            "required": ["layer_name"]
        },
        
        "get_centroid": {
            "name": "get_centroid",
            "description": "Get centroid coordinates (X, Y) for all features in a layer, useful for spatial analysis and visualization.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to get centroids from"
                }
            },
            "required": ["layer_name"]
        },
        
        "create_buffer": {
            "name": "create_buffer",
            "description": "Create buffer zones around features at a specified distance, useful for proximity analysis.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to buffer"
                },
                "distance": {
                    "type": "number",
                    "description": "Buffer distance (positive number)"
                },
                "units": {
                    "type": "string",
                    "description": "Units for buffer distance",
                    "enum": ["meters", "kilometers", "feet", "miles"],
                    "default": "meters"
                }
            },
            "required": ["layer_name", "distance"]
        },
        
        "spatial_join": {
            "name": "spatial_join",
            "description": "Perform spatial join between two layers based on their spatial relationship, combining attributes from both layers.",
            "parameters": {
                "target_layer": {
                    "type": "string",
                    "description": "The target layer that will receive joined attributes"
                },
                "join_layer": {
                    "type": "string",
                    "description": "The layer providing attributes to join"
                },
                "join_operation": {
                    "type": "string",
                    "description": "Spatial relationship for the join operation",
                    "enum": ["intersect", "within", "contains", "closest"],
                    "default": "intersect"
                }
            },
            "required": ["target_layer", "join_layer"]
        },
        
        "clip_layer": {
            "name": "clip_layer",
            "description": "Clip input layer features using the boundary of a clip layer, extracting only the portions that fall within the clip boundary.",
            "parameters": {
                "input_layer": {
                    "type": "string",
                    "description": "The layer to be clipped"
                },
                "clip_layer": {
                    "type": "string",
                    "description": "The layer defining the clip boundary"
                }
            },
            "required": ["input_layer", "clip_layer"]
        },
        
        "calculate_distance": {
            "name": "calculate_distance",
            "description": "Calculate the distance between two geographic points using the Haversine formula for accurate earth-surface distances.",
            "parameters": {
                "point1": {
                    "type": "array",
                    "description": "First point as [longitude, latitude] coordinates",
                    "items": {"type": "number"}
                },
                "point2": {
                    "type": "array",
                    "description": "Second point as [longitude, latitude] coordinates", 
                    "items": {"type": "number"}
                },
                "units": {
                    "type": "string",
                    "description": "Units for distance calculation",
                    "enum": ["meters", "kilometers", "miles"],
                    "default": "meters"
                }
            },
            "required": ["point1", "point2"]
        },
        
        "get_current_project_path": {
            "name": "get_current_project_path",
            "description": "Get the file path of the current ArcGIS Pro project (.aprx file).",
            "parameters": {},
            "required": []
        },
        
        "get_default_db_path": {
            "name": "get_default_db_path", 
            "description": "Get the path to the default geodatabase for the current ArcGIS Pro project.",
            "parameters": {},
            "required": []
        },
        
        "get_field_definitions": {
            "name": "get_field_definitions",
            "description": "Get detailed information about all fields in a layer including data types, lengths, aliases, and nullability.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to examine"
                }
            },
            "required": ["layer_name"]
        },
        
        "get_layer_type": {
            "name": "get_layer_type",
            "description": "Determine the type of a layer (Feature Layer, Raster, Table, etc.) for understanding data structure.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to examine"
                }
            },
            "required": ["layer_name"]
        },
        
        "get_list_of_layer_fields": {
            "name": "get_list_of_layer_fields",
            "description": "Get a list of field names for a given GIS layer.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to list fields from"
                }
            },
            "required": ["layer_name"]
        },
        
        "get_data_source_info": {
            "name": "get_data_source_info",
            "description": "Get information about the data source (file path, database connection, etc.) for a layer.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to examine"
                }
            },
            "required": ["layer_name"]
        },
        
        "create_nearest_neighbor_layer": {
            "name": "create_nearest_neighbor_layer",
            "description": "Create a new layer with nearest neighbor analysis, adding fields for nearest neighbor ID and distance with statistical summary.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer for nearest neighbor analysis"
                },
                "id_field": {
                    "type": "string",
                    "description": "The field to use as unique identifier",
                    "default": "OBJECTID"
                }
            },
            "required": ["layer_name"]
        },
        
        "get_unique_values_count": {
            "name": "get_unique_values_count",
            "description": "Count the number of unique values in a field, useful for understanding data diversity and categorical analysis.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer containing the field"
                },
                "field_name": {
                    "type": "string",
                    "description": "The name of the field to analyze"
                }
            },
            "required": ["layer_name", "field_name"]
        },
        
        "calculate_empty_values": {
            "name": "calculate_empty_values",
            "description": "Calculate the number of empty (null or blank) values in a field for data quality assessment.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer containing the field"
                },
                "field_name": {
                    "type": "string",
                    "description": "The name of the field to analyze"
                }
            },
            "required": ["layer_name", "field_name"]
        },
        
        "get_map_layers_info": {
            "name": "get_map_layers_info",
            "description": "Get comprehensive information about all layers in the current ArcGIS Pro map including names, types, visibility, and data sources.",
            "parameters": {},
            "required": []
        },
        
        "get_map_tables_info": {
            "name": "get_map_tables_info",
            "description": "Get information about all standalone tables in the current ArcGIS Pro map.",
            "parameters": {},
            "required": []
        },
        
        "get_values_frequency": {
            "name": "get_values_frequency",
            "description": "Get frequency distribution of all values in a field, showing how often each value appears.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer containing the field"
                },
                "field_name": {
                    "type": "string",
                    "description": "The name of the field to analyze"
                }
            },
            "required": ["layer_name", "field_name"]
        },
        
        "get_value_frequency": {
            "name": "get_value_frequency",
            "description": "Get the frequency count for a specific value in a field.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer containing the field"
                },
                "field_name": {
                    "type": "string",
                    "description": "The name of the field to analyze"
                },
                "lookup_value": {
                    "type": "string",
                    "description": "The specific value to count"
                }
            },
            "required": ["layer_name", "field_name", "lookup_value"]
        },
        
        "get_coordinate_system": {
            "name": "get_coordinate_system",
            "description": "Get coordinate system information for a layer including CRS name, code, type, and units.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to examine"
                }
            },
            "required": ["layer_name"]
        },
        
        "clear_selection": {
            "name": "clear_selection",
            "description": "Clears the current selection for a given layer.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to clear selection from."
                }
            },
            "required": ["layer_name"]
        },

        "get_field_domain_values": {
            "name": "get_field_domain_values",
            "description": "Get domain values for coded value fields, showing allowed values and their descriptions.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer containing the field"
                },
                "field_name": {
                    "type": "string",
                    "description": "The name of the field with domain values"
                }
            },
            "required": ["layer_name", "field_name"]
        },
        
        "calculate_new_field": {
            "name": "calculate_new_field",
            "description": "Add a new field to a layer and calculate its values using static values or Python expressions referencing other fields.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer"
                },
                "new_field_name": {
                    "type": "string",
                    "description": "Name for the new field"
                },
                "field_value": {
                    "type": "string",
                    "description": "Value or Python expression to calculate. Use !FIELD_NAME! to reference other fields (e.g., '!AREA! / !POPULATION!')"
                },
                "field_type": {
                    "type": "string",
                    "description": "Data type for the new field",
                    "enum": ["TEXT", "DOUBLE", "LONG", "SHORT", "DATE"],
                    "default": "TEXT"
                }
            },
            "required": ["layer_name", "new_field_name", "field_value"]
        },
        
        "generate_smart_dashboard_layout": {
            "name": "generate_smart_dashboard_layout",
            "description": "[DEPRECATED] Use mission_generate_dashboard instead. Generates sophisticated dashboard layouts with optimized chart recommendations, detailed configurations, and positioning",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to generate smart dashboard layout for"
                }
            },
            "required": ["layer_name"]
        },
        "get_current_dashboard_layout": {
            "name": "get_current_dashboard_layout",
            "description": "[DEPRECATED] Use mission_get_layout instead. Get the current dashboard layout from the smart_dashboard.json file.",
            "parameters": {},
            "returns": {
                "widgets": "List of minimal widget info (id, x, y, w, h, fields)",
                "success": "True if loaded, False if error"
            }
        },
        "get_dashboard_fields_info": {
            "name": "get_dashboard_fields_info",
            "description": "[DEPRECATED] Use mission_get_field_info instead. Returns a summary for each field from smart_dashboard.json",
            "parameters": {},
            "returns": {
                "fields": "List of dicts with field_name, data_story, and sample_values",
                "success": "True if loaded, False if error"
            }
        },
        "get_current_dashboard_charts": {
            "name": "get_current_dashboard_charts",
            "description": "[DEPRECATED] Use mission_get_charts instead. Get the current charts from the dashboard layout in smart_dashboard.json.",
            "parameters": {},
            "returns": {
                "charts": "List of dicts with fields and chart_type",
                "success": "True if loaded, False if error"
            }
        },
        "update_dashboard_charts": {
            "name": "update_dashboard_charts",
            "description": "[DEPRECATED] Use mission_update_charts instead. Takes a list of {fields, chart_type} dicts and updates widgets in the dashboard.",
            "parameters": {
                "charts": {
                    "type": "array",
                    "description": "List of dicts with fields (array of strings) and chart_type (string)",
                    "items": {
                        "type": "object",
                        "properties": {
                            "fields": {"type": "array", "items": {"type": "string"}},
                            "chart_type": {"type": "string"}
                        },
                        "required": ["fields", "chart_type"]
                    }
                }
            },
            "required": ["charts"],
            "returns": {
                "updated_count": "Number of widgets updated",
                "success": "True if updated, False if error"
            }
        },

        # New Mission-Oriented Dashboard API
        "mission_generate_dashboard": {
            "name": "mission_generate_dashboard",
            "description": "Generates a new dashboard for a layer. Use the 'source' parameter to specify whether to use live layer data or cached dashboard data.",
            "parameters": {
                "layer_name": {"type": "string", "description": "The name of the layer to generate the dashboard for."},
                "source": {"type": "string", "description": "Source of field information, either 'layer' or 'dashboard'. Defaults to 'dashboard'.", "enum": ["layer", "dashboard"], "default": "dashboard"},
                "field_insights": {"type": "object", "description": "Optional. Pre-computed field insights to use for generation.", "default": None}
            },
            "required": ["layer_name"]
        },
        "mission_get_layout": {
            "name": "mission_get_layout",
            "description": "Retrieves the layout of the current dashboard.",
            "parameters": {},
            "required": []
        },
        "mission_get_charts": {
            "name": "mission_get_charts",
            "description": "Retrieves the list of chart configurations from the current dashboard.",
            "parameters": {},
            "required": []
        },
        "mission_get_field_info": {
            "name": "mission_get_field_info",
            "description": "Retrieves metadata and insights for fields stored in the current dashboard.",
            "parameters": {
                "field_name": {"type": "string", "description": "Optional. The name of a specific field to get information for.", "default": None}
            },
            "required": []
        },
        "mission_update_charts": {
            "name": "mission_update_charts",
            "description": "Updates one or more charts in the current dashboard.",
            "parameters": {
                "charts_data": {
                    "type": "array",
                    "description": "A list of objects, where each object specifies a chart to update by its 'index' and includes the new chart data.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "index": {"type": "integer", "description": "The zero-based index of the chart to update."},
                            "fields": {"type": "array", "items": {"type": "string"}},
                            "chart_type": {"type": "string"}
                        },
                        "required": ["index"]
                    }
                }
            },
            "required": ["charts_data"]
        },
        "mission_add_charts": {
            "name": "mission_add_charts",
            "description": "Adds one or more new charts to the current dashboard.",
            "parameters": {
                "new_charts": {
                    "type": "array",
                    "description": "A list of chart configuration objects to add to the dashboard.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "fields": {"type": "array", "items": {"type": "string"}},
                            "chart_type": {"type": "string"}
                        },
                        "required": ["fields", "chart_type"]
                    }
                }
            },
            "required": ["new_charts"]
        },
      
        "raster_calculator": {
            "name": "raster_calculator",
            "description": "Performs a map algebra expression using the raster calculator. Note: The 'expression' should be a valid Python string using arcpy.sa.Raster objects. Example payload: {\"function_name\":\"raster_calculator\",\"arguments\":{\"expression\":\"Raster('raster1') - Raster('raster2')\",\"output_raster\":\"raster_difference\"}}. Replace 'raster1' and 'raster2' with your actual raster layer names or paths.",
            "parameters": {
                "expression": {
                    "type": "string",
                    "description": "A map algebra expression."
                },
                "output_raster": {
                    "type": "string",
                    "description": "The output raster file."
                }
            },
            "required": ["expression", "output_raster"]
        },
        "reclassify": {
            "name": "reclassify",
            "description": "Reclassifies the values in a raster.",
            "parameters": {
                "in_raster": {
                    "type": "string",
                    "description": "The input raster to be reclassified."
                },
                "reclass_field": {
                    "type": "string",
                    "description": "Field denoting the values to be reclassified."
                },
                "remap": {
                    "type": "string",
                    "description": "A remap object that defines how to reclassify the values."
                },
                "out_raster": {
                    "type": "string",
                    "description": "The output reclassified raster."
                }
            },
            "required": ["in_raster", "reclass_field", "remap", "out_raster"]
        },
        "zonal_statistics_as_table": {
            "name": "zonal_statistics_as_table",
            "description": "Calculates statistics on a raster within the zones of another dataset and reports the results as a table.",
            "parameters": {
                "in_zone_data": {
                    "type": "string",
                    "description": "The dataset that defines the zones."
                },
                "zone_field": {
                    "type": "string",
                    "description": "The field that contains the values that define each zone."
                },
                "in_value_raster": {
                    "type": "string",
                    "description": "The raster that contains the values on which to calculate a statistic."
                },
                "out_table": {
                    "type": "string",
                    "description": "The output table."
                },
                "statistics_type": {
                    "type": "string",
                    "description": "The statistic type to be calculated.",
                    "enum": ["MEAN", "MAJORITY", "MAXIMUM", "MEDIAN", "MINORITY", "RANGE", "STD", "SUM", "VARIETY"],
                    "default": "MEAN"
                }
            },
            "required": ["in_zone_data", "zone_field", "in_value_raster", "out_table"]
        },
        "slope": {
            "name": "slope",
            "description": "Calculates the slope of a raster surface.",
            "parameters": {
                "in_raster": {
                    "type": "string",
                    "description": "The input surface raster."
                },
                "out_raster": {
                    "type": "string",
                    "description": "The output slope raster."
                },
                "output_measurement": {
                    "type": "string",
                    "description": "The output measurement units.",
                    "enum": ["DEGREE", "PERCENT_RISE"],
                    "default": "DEGREE"
                }
            },
            "required": ["in_raster", "out_raster"]
        },
        "aspect": {
            "name": "aspect",
            "description": "Calculates the aspect of a raster surface.",
            "parameters": {
                "in_raster": {
                    "type": "string",
                    "description": "The input surface raster."
                },
                "out_raster": {
                    "type": "string",
                    "description": "The output aspect raster."
                }
            },
            "required": ["in_raster", "out_raster"]
        },
        "hillshade": {
            "name": "hillshade",
            "description": "Creates a hillshade from a raster surface.",
            "parameters": {
                "in_raster": {
                    "type": "string",
                    "description": "The input surface raster."
                },
                "out_raster": {
                    "type": "string",
                    "description": "The output hillshade raster."
                },
                "azimuth": {
                    "type": "integer",
                    "description": "The azimuth angle of the light source.",
                    "default": 315
                },
                "altitude": {
                    "type": "integer",
                    "description": "The altitude angle of the light source.",
                    "default": 45
                }
            },
            "required": ["in_raster", "out_raster"]
        },
        "extract_by_mask": {
            "name": "extract_by_mask",
            "description": "Extracts the cells of a raster that correspond to the areas defined by a mask.",
            "parameters": {
                "in_raster": {
                    "type": "string",
                    "description": "The input raster to be extracted."
                },
                "in_mask_data": {
                    "type": "string",
                    "description": "The dataset to be used as a mask."
                },
                "out_raster": {
                    "type": "string",
                    "description": "The output raster."
                }
            },
            "required": ["in_raster", "in_mask_data", "out_raster"]
        },
        "clip_raster": {
            "name": "clip_raster",
            "description": "Clips a raster dataset.",
            "parameters": {
                "in_raster": {
                    "type": "string",
                    "description": "The input raster to be clipped."
                },
                "out_raster": {
                    "type": "string",
                    "description": "The output clipped raster."
                },
                "in_template_dataset": {
                    "type": "string",
                    "description": "A raster or feature class to use as a template."
                },
                "clipping_geometry": {
                    "type": "string",
                    "description": "Specifies whether to use the extent of the template or the features within it.",
                    "enum": ["ClippingGeometry", "NONE"],
                    "default": "ClippingGeometry"
                }
            },
            "required": ["in_raster", "out_raster", "in_template_dataset"]
        },
        "resample": {
            "name": "resample",
            "description": "Resamples a raster dataset.",
            "parameters": {
                "in_raster": {
                    "type": "string",
                    "description": "The input raster to be resampled."
                },
                "out_raster": {
                    "type": "string",
                    "description": "The output resampled raster."
                },
                "cell_size": {
                    "type": "string",
                    "description": "The cell size for the output raster."
                },
                "resampling_type": {
                    "type": "string",
                    "description": "The resampling technique to use.",
                    "enum": ["NEAREST", "BILINEAR", "CUBIC", "MAJORITY"],
                    "default": "NEAREST"
                }
            },
            "required": ["in_raster", "out_raster", "cell_size"]
        },
        "get_raster_properties": {
            "name": "get_raster_properties",
            "description": "Gets properties of a raster dataset.",
            "parameters": {
                "in_raster": {
                    "type": "string",
                    "description": "The input raster."
                }
            },
            "required": ["in_raster"]
        },
        "raster_to_point": {
            "name": "raster_to_point",
            "description": "Converts a raster dataset to point features.",
            "parameters": {
                "in_raster": {"type": "string", "description": "The input raster."},
                "out_point_features": {"type": "string", "description": "The output point feature class."}
            },
            "required": ["in_raster", "out_point_features"]
        },
        "raster_to_polygon": {
            "name": "raster_to_polygon",
            "description": "Converts a raster dataset to polygon features.",
            "parameters": {
                "in_raster": {"type": "string", "description": "The input raster."},
                "out_polygon_features": {"type": "string", "description": "The output polygon feature class."}
            },
            "required": ["in_raster", "out_polygon_features"]
        },
        "raster_to_polyline": {
            "name": "raster_to_polyline",
            "description": "Converts a raster dataset to polyline features.",
            "parameters": {
                "in_raster": {"type": "string", "description": "The input raster."},
                "out_polyline_features": {"type": "string", "description": "The output polyline feature class."}
            },
            "required": ["in_raster", "out_polyline_features"]
        },
        "feature_to_raster": {
            "name": "feature_to_raster",
            "description": "Converts features to a raster dataset.",
            "parameters": {
                "in_features": {"type": "string", "description": "The input features."},
                "field": {"type": "string", "description": "The field used to assign values to the output raster."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_features", "field", "out_raster"]
        },
        "polygon_to_raster": {
            "name": "polygon_to_raster",
            "description": "Converts polygon features to a raster dataset.",
            "parameters": {
                "in_features": {"type": "string", "description": "The input polygon features."},
                "value_field": {"type": "string", "description": "The field used to assign values to the output raster."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_features", "value_field", "out_raster"]
        },
        "point_to_raster": {
            "name": "point_to_raster",
            "description": "Converts point features to a raster dataset.",
            "parameters": {
                "in_features": {"type": "string", "description": "The input point features."},
                "value_field": {"type": "string", "description": "The field used to assign values to the output raster."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_features", "value_field", "out_raster"]
        },
        "idw_interpolation": {
            "name": "idw_interpolation",
            "description": "Interpolates a raster surface from points using an inverse distance weighted (IDW) technique.",
            "parameters": {
                "in_point_features": {"type": "string", "description": "The input point features."},
                "z_field": {"type": "string", "description": "The field that holds the height or magnitude value for each point."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_point_features", "z_field", "out_raster"]
        },
        "kriging_interpolation": {
            "name": "kriging_interpolation",
            "description": "Interpolates a raster surface from points using kriging.",
            "parameters": {
                "in_point_features": {"type": "string", "description": "The input point features."},
                "z_field": {"type": "string", "description": "The field that holds the height or magnitude value for each point."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_point_features", "z_field", "out_raster"]
        },
        "spline_interpolation": {
            "name": "spline_interpolation",
            "description": "Interpolates a raster surface from points using a spline.",
            "parameters": {
                "in_point_features": {"type": "string", "description": "The input point features."},
                "z_field": {"type": "string", "description": "The field that holds the height or magnitude value for each point."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_point_features", "z_field", "out_raster"]
        },
        "natural_neighbor": {
            "name": "natural_neighbor",
            "description": "Interpolates a raster surface from points using natural neighbor.",
            "parameters": {
                "in_point_features": {"type": "string", "description": "The input point features."},
                "z_field": {"type": "string", "description": "The field that holds the height or magnitude value for each point."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_point_features", "z_field", "out_raster"]
        },
        "euclidean_distance": {
            "name": "euclidean_distance",
            "description": "Calculates for each cell the Euclidean distance to the closest source.",
            "parameters": {
                "in_source_data": {"type": "string", "description": "The input source data."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_source_data", "out_raster"]
        },
        "euclidean_allocation": {
            "name": "euclidean_allocation",
            "description": "Calculates, for each cell, the nearest source based on Euclidean distance.",
            "parameters": {
                "in_source_data": {"type": "string", "description": "The input source data."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_source_data", "out_raster"]
        },
        "euclidean_direction": {
            "name": "euclidean_direction",
            "description": "Calculates, for each cell, the direction in degrees to the nearest source.",
            "parameters": {
                "in_source_data": {"type": "string", "description": "The input source data."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_source_data", "out_raster"]
        },
        "cost_distance": {
            "name": "cost_distance",
            "description": "Calculates the least accumulative cost distance for each cell to the nearest source over a cost surface.",
            "parameters": {
                "in_source_data": {"type": "string", "description": "The input source data."},
                "in_cost_raster": {"type": "string", "description": "A raster defining the impedance or cost to move planimetrically through each cell."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_source_data", "in_cost_raster", "out_raster"]
        },
        "cost_allocation": {
            "name": "cost_allocation",
            "description": "Calculates, for each cell, its least-cost source based on the least accumulative cost over a cost surface.",
            "parameters": {
                "in_source_data": {"type": "string", "description": "The input source data."},
                "in_cost_raster": {"type": "string", "description": "A raster defining the impedance or cost to move planimetrically through each cell."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_source_data", "in_cost_raster", "out_raster"]
        },
        "cost_path": {
            "name": "cost_path",
            "description": "Calculates the least-cost path from a source to a destination.",
            "parameters": {
                "in_destination_data": {"type": "string", "description": "The input destination data."},
                "in_cost_distance_raster": {"type": "string", "description": "The cost distance raster to be used to determine the least-cost path."},
                "in_cost_backlink_raster": {"type": "string", "description": "The cost backlink raster to be used to determine the path."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_destination_data", "in_cost_distance_raster", "in_cost_backlink_raster", "out_raster"]
        },
        "weighted_overlay": {
            "name": "weighted_overlay",
            "description": "Overlays several rasters using a common measurement scale and weights each according to its importance.",
            "parameters": {
                "overlay_table": {"type": "string", "description": "The weighted overlay table."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["overlay_table", "out_raster"]
        },
        "weighted_sum": {
            "name": "weighted_sum",
            "description": "Overlays several rasters, multiplying each by their given weight and summing them together.",
            "parameters": {
                "in_rasters": {"type": "string", "description": "The weighted sum table."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_rasters", "out_raster"]
        },
        "extract_by_attribute": {
            "name": "extract_by_attribute",
            "description": "Extracts cells from a raster based on a logical query.",
            "parameters": {
                "in_raster": {"type": "string", "description": "The input raster."},
                "where_clause": {"type": "string", "description": "A logical expression to select a subset of raster cells."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_raster", "where_clause", "out_raster"]
        },
        "mosaic_to_new_raster": {
            "name": "mosaic_to_new_raster",
            "description": "Mosaics multiple raster datasets into a new raster dataset.",
            "parameters": {
                "input_rasters": {"type": "array", "items": {"type": "string"}, "description": "A list of input rasters."},
                "output_location": {"type": "string", "description": "The folder where the output raster will be stored."},
                "raster_dataset_name_with_extension": {"type": "string", "description": "The name of the output raster."},
                "pixel_type": {"type": "string", "description": "The pixel type of the output raster."},
                "number_of_bands": {"type": "integer", "description": "The number of bands of the output raster."}
            },
            "required": ["input_rasters", "output_location", "raster_dataset_name_with_extension", "pixel_type", "number_of_bands"]
        },
        "combine_rasters": {
            "name": "combine_rasters",
            "description": "Combines multiple rasters so that a unique output value is assigned to each unique combination of input values.",
            "parameters": {
                "in_rasters": {"type": "array", "items": {"type": "string"}, "description": "A list of input rasters."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_rasters", "out_raster"]
        },
        "extract_by_mask": {
            "name": "extract_by_mask",
            "description": "Extracts the cells of a raster that correspond to the areas defined by a mask.",
            "parameters": {
                "in_raster": {"type": "string", "description": "The input raster to be extracted."},
                "in_mask_data": {"type": "string", "description": "The dataset to be used as a mask."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_raster", "in_mask_data", "out_raster"]
        },
        "invert_selection": {
            "name": "invert_selection",
            "description": "Invert the current selection on a layer.",
            "parameters": {
                "layer_name": {"type": "string", "description": "The name of the layer."}
            },
            "required": ["layer_name"]
        },
        
        "add_dashboard_charts": {
            "name": "add_dashboard_charts",
            "description": "Append new charts to the current dashboard. Use this function to add charts to a dashboard that already exists. Each chart definition should include 'fields' (required) and optional 'chart_type', 'title', 'category_field', or 'primary_field'.",
            "parameters": {
                "new_charts": {
                    "type": "array",
                    "description": "Array of chart definitions to append to the dashboard",
                    "items": {
                        "type": "object",
                        "properties": {
                            "fields": {
                                "type": "array",
                                "items": {"type": "string"},
                                "description": "Array of field names for the chart (required)"
                            },
                            "chart_type": {
                                "type": "string", 
                                "description": "Type of chart (bar, pie, histogram, etc.)",
                                "default": "bar"
                            },
                            "title": {
                                "type": "string",
                                "description": "Custom title for the chart"
                            },
                            "category_field": {
                                "type": "string",
                                "description": "Field to use as category axis (for grouped charts)"
                            },
                            "primary_field": {
                                "type": "string", 
                                "description": "Field to use as primary value field"
                            }
                        },
                        "required": ["fields"]
                    }
                }
            },
            "required": ["new_charts"]
        }
    }
