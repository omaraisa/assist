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
            "required": ["layer_name", "where_clause"],
            "action_input_examples": [
                {"function_name": "select_by_attribute", "layer_name": "Cities", "where_clause": "POPULATION > 100000"}
            ]
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
            "required": ["input_layer", "select_layer"],
            "action_input_examples": [
                {"function_name": "select_by_location", "input_layer": "Parcels", "select_layer": "Flood_Zones", "relationship": "INTERSECT"}
            ]
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
            "required": ["layer_name", "field_name"],
            "action_input_examples": [
                {"function_name": "get_field_statistics", "layer_name": "Counties", "field_name": "POP2020"}
            ]
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
            "required": ["layer_name"],
            "action_input_examples": [
                {"function_name": "get_layer_summary", "layer_name": "Roads"}
            ]
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
            "required": ["layer_name"],
            "action_input_examples": [
                {"function_name": "calculate_area", "layer_name": "Parks", "units": "acres"}
            ]
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
            "required": ["layer_name"],
            "action_input_examples": [
                {"function_name": "calculate_length", "layer_name": "Rivers", "units": "miles"}
            ]
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
            "required": ["layer_name"],
            "action_input_examples": [
                {"function_name": "get_centroid", "layer_name": "States"}
            ]
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
            "required": ["layer_name", "distance"],
            "action_input_examples": [
                {"function_name": "create_buffer", "layer_name": "Schools", "distance": 500, "units": "meters"}
            ]
        },
        
        "spatial_join": {
            "name": "spatial_join",
            "description": "Perform spatial join between two layers based on their spatial relationship, combining attributes from both layers. Supports various spatial relationships and provides detailed error messages.",
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
                    "enum": ["intersects", "contains", "within", "touches", "overlaps", "crosses", "closest"],
                    "default": "intersects"
                },
                "output_name": {
                    "type": "string",
                    "description": "Optional custom name for the output layer. If not provided, a name will be generated automatically.",
                    "default": None
                }
            },
            "required": ["target_layer", "join_layer"],
            "action_input_examples": [
                {"function_name": "spatial_join", "target_layer": "Hospitals", "join_layer": "Zip_Codes", "join_operation": "within"},
                {"function_name": "spatial_join", "target_layer": "Schools", "join_layer": "Districts", "join_operation": "intersects", "output_name": "Schools_in_Districts"}
            ]
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
            "required": ["input_layer", "clip_layer"],
            "action_input_examples": [
                {"function_name": "clip_layer", "input_layer": "Roads", "clip_layer": "City_Boundary"}
            ]
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
            "required": ["point1", "point2"],
            "action_input_examples": [
                {"function_name": "calculate_distance", "point1": [-74.0060, 40.7128], "point2": [-118.2437, 34.0522], "units": "kilometers"}
            ]
        },
        
        "get_current_project_path": {
            "name": "get_current_project_path",
            "description": "Get the file path of the current ArcGIS Pro project (.aprx file).",
            "parameters": {},
            "required": [],
            "action_input_examples": [
                {"function_name": "get_current_project_path"}
            ]
        },
        
        "get_default_db_path": {
            "name": "get_default_db_path", 
            "description": "Get the path to the default geodatabase for the current ArcGIS Pro project.",
            "parameters": {},
            "required": [],
            "action_input_examples": [
                {"function_name": "get_default_db_path"}
            ]
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
            "required": ["layer_name"],
            "action_input_examples": [
                {"function_name": "get_field_definitions", "layer_name": "Buildings"}
            ]
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
            "required": ["layer_name"],
            "action_input_examples": [
                {"function_name": "get_layer_type", "layer_name": "Elevation"}
            ]
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
            "required": ["layer_name"],
            "action_input_examples": [
                {"function_name": "get_list_of_layer_fields", "layer_name": "Land_Use"}
            ]
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
            "required": ["layer_name"],
            "action_input_examples": [
                {"function_name": "get_data_source_info", "layer_name": "Water_Mains"}
            ]
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
            "required": ["layer_name"],
            "action_input_examples": [
                {"function_name": "create_nearest_neighbor_layer", "layer_name": "Fire_Stations"}
            ]
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
            "required": ["layer_name", "field_name"],
            "action_input_examples": [
                {"function_name": "get_unique_values_count", "layer_name": "Parcels", "field_name": "Zoning_Class"}
            ]
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
            "required": ["layer_name", "field_name"],
            "action_input_examples": [
                {"function_name": "calculate_empty_values", "layer_name": "Addresses", "field_name": "Street_Name"}
            ]
        },
        
        "get_map_layers_info": {
            "name": "get_map_layers_info",
            "description": "Get comprehensive information about all layers in the current ArcGIS Pro map including names, types, visibility, and data sources.",
            "parameters": {},
            "required": [],
            "action_input_examples": [
                {"function_name": "get_map_layers_info"}
            ]
        },
        
        "get_map_tables_info": {
            "name": "get_map_tables_info",
            "description": "Get information about all standalone tables in the current ArcGIS Pro map.",
            "parameters": {},
            "required": [],
            "action_input_examples": [
                {"function_name": "get_map_tables_info"}
            ]
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
            "required": ["layer_name", "field_name"],
            "action_input_examples": [
                {"function_name": "get_values_frequency", "layer_name": "Crime_Incidents", "field_name": "Crime_Type"}
            ]
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
            "required": ["layer_name", "field_name", "lookup_value"],
            "action_input_examples": [
                {"function_name": "get_value_frequency", "layer_name": "Crime_Incidents", "field_name": "Crime_Type", "lookup_value": "Burglary"}
            ]
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
            "required": ["layer_name"],
            "action_input_examples": [
                {"function_name": "get_coordinate_system", "layer_name": "World_Cities"}
            ]
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
            "required": ["layer_name"],
            "action_input_examples": [
                {"function_name": "clear_selection", "layer_name": "Cities"}
            ]
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
            "required": ["layer_name", "field_name"],
            "action_input_examples": [
                {"function_name": "get_field_domain_values", "layer_name": "Pipes", "field_name": "Material"}
            ]
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
            "required": ["layer_name", "new_field_name", "field_value"],
            "action_input_examples": [
                {"function_name": "calculate_new_field", "layer_name": "Districts", "new_field_name": "Population_Density", "field_value": "!POPULATION! / !AREA_SQKM!", "field_type": "DOUBLE"}
            ]
        },

        # New Dashboard API
        "generate_dashboard_for_target_layer": {
            "name": "generate_dashboard_for_target_layer",
            "description": "Creates a complete new dashboard from scratch for a GIS layer. Use this function when user asks to 'create dashboard', 'generate dashboard', or 'build dashboard'. This analyzes the layer data automatically and creates a comprehensive dashboard with multiple charts and insights. Field insights are automatically fetched from ArcGIS Pro if not provided.",
            "parameters": {
                "layer_name": {"type": "string", "description": "The name of the layer for the dashboard."},
                "analysis_type": {"type": "string", "description": "Type of analysis to perform.", "enum": ["overview", "detailed", "statistical"], "default": "overview"},
                "theme": {"type": "string", "description": "Visual theme for the dashboard.", "enum": ["default", "dark", "light"], "default": "default"},
                "field_insights": {"type": "object", "description": "Optional. Pre-computed field insights. If not provided, will be automatically fetched from the layer in ArcGIS Pro.", "default": None}
            },
            "required": ["layer_name"],
            "action_input_examples": [
                {"function_name": "generate_dashboard_for_target_layer", "layer_name": "Mosques", "analysis_type": "overview"},
                {"function_name": "generate_dashboard_for_target_layer", "layer_name": "Population_Data", "analysis_type": "detailed", "theme": "dark"}
            ]
        },
        "get_current_dashboard_layout": {
            "name": "get_current_dashboard_layout",
            "description": "Retrieves the layout of the current dashboard.",
            "parameters": {},
            "required": [],
            "action_input_examples": [
                {"function_name": "get_current_dashboard_layout"}
            ]
        },
        "get_current_dashboard_charts": {
            "name": "get_current_dashboard_charts",
            "description": "Retrieves the list of chart configurations from the current dashboard.",
            "parameters": {},
            "required": [],
            "action_input_examples": [
                {"function_name": "get_current_dashboard_charts"}
            ]
        },
        "get_dashboard_field_detailed_description": {
            "name": "get_dashboard_field_detailed_description",
            "description": "Retrieves metadata and insights for fields stored in the current dashboard.",
            "parameters": {
                "field_name": {"type": "string", "description": "Optional. The name of a specific field to get information for.", "default": None}
            },
            "required": [],
            "action_input_examples": [
                {"function_name": "get_dashboard_field_detailed_description"},
                {"function_name": "get_dashboard_field_detailed_description", "field_name": "Population"}
            ]
        },
        "update_dashboard_charts": {
            "name": "update_dashboard_charts",
            "description": "Updates the configuration of existing dashboard charts including chart type, title, theme, fields, category_field, and series_fields at specified indices. Can change field configurations and regenerate chart data based on new settings. For the fields array, ensure the category field is listed first to be used as the category field.",
            "parameters": {
                "charts_data": {
                    "type": "array",
                    "description": "A list of objects, each specifying a chart to update. Must contain 'index' and the new 'chart' object with configuration.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "index": {"type": "integer", "description": "The zero-based index of the chart to update."},
                            "chart": {
                                "type": "object",
                                "description": "The new chart configuration object.",
                                "properties": {
                                    "chart_type": {"type": "string", "description": "The type of chart (e.g., bar, column, pie)."},
                                    "title": {"type": "string", "description": "The title of the chart."},
                                    "theme": {"type": "string", "description": "The visual theme of the chart."},
                                    "fields": {
                                        "type": "array",
                                        "description": "List of field names. The first field will be used as the category field if category_field is not specified.",
                                        "items": {"type": "string"}
                                    },
                                    "category_field": {"type": "string", "description": "The field to use as the category field. If not specified, the first field in 'fields' will be used."},
                                    "series": {
                                        "type": "array",
                                        "description": "List of series fields for multi-series charts.",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "field": {"type": "string", "description": "The field name for the series."},
                                                "name": {"type": "string", "description": "The display name for the series."}
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "required": ["index", "chart"]
                    }
                }
            },
            "required": ["charts_data"],
            "action_input_examples": [
                {"function_name": "update_dashboard_charts", "charts_data": [{"index": 0, "chart": {"chart_type": "bar", "title": "Population by District", "fields": ["District", "Population"]}}]},
                {"function_name": "update_dashboard_charts", "charts_data": [{"index": 1, "chart": {"chart_type": "pie", "title": "Crime Rate Distribution", "fields": ["Crime_Rate_Per_1000"], "theme": "dark"}}]}
            ]
        },
        "delete_charts_from_dashboard": {
            "name": "delete_charts_from_dashboard",
            "description": "Deletes one or more charts from the dashboard using their indices.",
            "parameters": {
                "indices": {
                    "type": "array",
                    "description": "A list of zero-based integer indices of the charts to delete.",
                    "items": {"type": "integer"}
                }
            },
            "required": ["indices"],
            "action_input_examples": [
                {"function_name": "delete_charts_from_dashboard", "indices": [0, 2]},
                {"function_name": "delete_charts_from_dashboard", "indices": [1]}
            ]
        },
        "update_dashboard_layout": {
            "name": "update_dashboard_layout",
            "description": "Updates the overall dashboard layout, such as changing the number of columns, or updates the layout of specific chart items, such as their grid area to make them span multiple columns/rows.",
            "parameters": {
                "layout_updates": {
                    "type": "object",
                    "description": "An object containing layout updates. Can have 'grid_template_columns' for the whole grid, or an 'items' array for specific charts.",
                    "properties": {
                        "grid_template_columns": {"type": "string", "description": "e.g., '1fr 1fr 1fr' for three columns."},
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "index": {"type": "integer", "description": "The index of the chart item to update."},
                                    "grid_area": {"type": "string", "description": "The new grid area, e.g., 'span 2 / span 2'."}
                                },
                                "required": ["index"]
                            }
                        }
                    }
                }
        },
            "required": ["layout_updates"],
            "action_input_examples": [
                {"function_name": "update_dashboard_layout", "layout_updates": {"grid_template_columns": "1fr 1fr 1fr"}},
                {"function_name": "update_dashboard_layout", "layout_updates": {"items": [{"index": 0, "grid_area": "span 2 / span 1"}]}}
            ]
        },
      
        "add_chart_to_dashboard": {
            "name": "add_chart_to_dashboard",
            "description": "Adds a new chart to the existing dashboard with fresh data generation. Use this for complex charts requiring aggregations or calculations in ArcGIS Pro. The function computes data on the fly and appends the chart to the current dashboard without replacing it.",
            "parameters": {
                "layer_name": {"type": "string", "description": "The name of the layer to create the chart from."},
                "chart_type": {
                    "type": "string",
                    "description": "The type of chart to create.",
                    "enum": ["bar", "column", "pie", "line", "scatter", "histogram"],
                    "default": "bar"
                },
                "fields": {
                    "type": "array",
                    "description": "List of field names to include in the chart. For aggregated charts, this can include numeric fields to aggregate.",
                    "items": {"type": "string"}
                },
                "category_field": {
                    "type": "string",
                    "description": "Optional field to categorize/group the data by (e.g., for bar charts showing sums per category).",
                    "default": None
                },
                "aggregation": {
                    "type": "string",
                    "description": "Aggregation method for numeric fields when grouped by category_field.",
                    "enum": ["sum", "mean", "avg", "count", "min", "max"],
                    "default": "sum"
                },
                "title": {
                    "type": "string",
                    "description": "Optional title for the chart.",
                    "default": None
                },
                "theme": {
                    "type": "string",
                    "description": "Visual theme for the chart, options: default, dark, light.",
                    "enum": ["default", "dark", "light"],
                    "default": "default"
                },
                "where_clause": {
                    "type": "string",
                    "description": "Optional SQL WHERE clause to filter data before generating the chart.",
                    "default": None
                }
            },
            "required": ["layer_name", "chart_type", "fields"],
            "action_input_examples": [
                {"function_name": "add_chart_to_dashboard", "layer_name": "Mosques", "chart_type": "bar", "fields": ["Development_Stage"], "title": "Mosque Development Stages"},
                {"function_name": "add_chart_to_dashboard", "layer_name": "Population_Data", "chart_type": "pie", "fields": ["District", "Population"], "category_field": "District", "aggregation": "sum", "title": "Population by District"}
            ]
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
            "required": ["expression", "output_raster"],
            "action_input_examples": [
                {"function_name": "raster_calculator", "expression": "Raster('DEM') > 1500", "output_raster": "High_Elevation"}
            ]
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
            "required": ["in_raster", "reclass_field", "remap", "out_raster"],
            "action_input_examples": [
                {"function_name": "reclassify", "in_raster": "Land_Cover", "reclass_field": "Value", "remap": "1 1;2 1;3 2", "out_raster": "Reclassified_Land_Cover"}
            ]
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
            "required": ["in_zone_data", "zone_field", "in_value_raster", "out_table"],
            "action_input_examples": [
                {"function_name": "zonal_statistics_as_table", "in_zone_data": "Watersheds", "zone_field": "Watershed_ID", "in_value_raster": "Precipitation", "out_table": "Precip_Stats", "statistics_type": "MEAN"}
            ]
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
            "required": ["in_raster", "out_raster"],
            "action_input_examples": [
                {"function_name": "slope", "in_raster": "DEM", "out_raster": "Slope_Map", "output_measurement": "PERCENT_RISE"}
            ]
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
            "required": ["in_raster", "out_raster"],
            "action_input_examples": [
                {"function_name": "aspect", "in_raster": "DEM", "out_raster": "Aspect_Map"}
            ]
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
            "required": ["in_raster", "out_raster"],
            "action_input_examples": [
                {"function_name": "hillshade", "in_raster": "DEM", "out_raster": "Hillshade_Effect", "azimuth": 270, "altitude": 60}
            ]
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
            "required": ["in_raster", "in_mask_data", "out_raster"],
            "action_input_examples": [
                {"function_name": "extract_by_mask", "in_raster": "Global_Population", "in_mask_data": "Country_Boundary", "out_raster": "Country_Population"}
            ]
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
            "required": ["in_raster", "out_raster", "in_template_dataset"],
            "action_input_examples": [
                {"function_name": "clip_raster", "in_raster": "State_Vegetation", "out_raster": "County_Vegetation", "in_template_dataset": "County_Boundary"}
            ]
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
            "required": ["in_raster", "out_raster", "cell_size"],
            "action_input_examples": [
                {"function_name": "resample", "in_raster": "High_Res_DEM", "out_raster": "Low_Res_DEM", "cell_size": "30 30", "resampling_type": "BILINEAR"}
            ]
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
            "required": ["in_raster"],
            "action_input_examples": [
                {"function_name": "get_raster_properties", "in_raster": "DEM"}
            ]
        },
        "raster_to_point": {
            "name": "raster_to_point",
            "description": "Converts a raster dataset to point features.",
            "parameters": {
                "in_raster": {"type": "string", "description": "The input raster."},
                "out_point_features": {"type": "string", "description": "The output point feature class."}
            },
            "required": ["in_raster", "out_point_features"],
            "action_input_examples": [
                {"function_name": "raster_to_point", "in_raster": "Temperature_Grid", "out_point_features": "Temp_Readings"}
            ]
        },
        "raster_to_polygon": {
            "name": "raster_to_polygon",
            "description": "Converts a raster dataset to polygon features.",
            "parameters": {
                "in_raster": {"type": "string", "description": "The input raster."},
                "out_polygon_features": {"type": "string", "description": "The output polygon feature class."}
            },
            "required": ["in_raster", "out_polygon_features"],
            "action_input_examples": [
                {"function_name": "raster_to_polygon", "in_raster": "Land_Use_Grid", "out_polygon_features": "Land_Use_Polygons"}
            ]
        },
        "raster_to_polyline": {
            "name": "raster_to_polyline",
            "description": "Converts a raster dataset to polyline features.",
            "parameters": {
                "in_raster": {"type": "string", "description": "The input raster."},
                "out_polyline_features": {"type": "string", "description": "The output polyline feature class."}
            },
            "required": ["in_raster", "out_polyline_features"],
            "action_input_examples": [
                {"function_name": "raster_to_polyline", "in_raster": "Stream_Grid", "out_polyline_features": "Stream_Lines"}
            ]
        },
        "feature_to_raster": {
            "name": "feature_to_raster",
            "description": "Converts features to a raster dataset.",
            "parameters": {
                "in_features": {"type": "string", "description": "The input features."},
                "field": {"type": "string", "description": "The field used to assign values to the output raster."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_features", "field", "out_raster"],
            "action_input_examples": [
                {"function_name": "feature_to_raster", "in_features": "Weather_Stations", "field": "Temperature", "out_raster": "Temp_Raster"}
            ]
        },
        "polygon_to_raster": {
            "name": "polygon_to_raster",
            "description": "Converts polygon features to a raster dataset.",
            "parameters": {
                "in_features": {"type": "string", "description": "The input polygon features."},
                "value_field": {"type": "string", "description": "The field used to assign values to the output raster."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_features", "value_field", "out_raster"],
            "action_input_examples": [
                {"function_name": "polygon_to_raster", "in_features": "Soil_Types", "value_field": "Soil_Code", "out_raster": "Soil_Grid"}
            ]
        },
        "point_to_raster": {
            "name": "point_to_raster",
            "description": "Converts point features to a raster dataset.",
            "parameters": {
                "in_features": {"type": "string", "description": "The input point features."},
                "value_field": {"type": "string", "description": "The field used to assign values to the output raster."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_features", "value_field", "out_raster"],
            "action_input_examples": [
                {"function_name": "point_to_raster", "in_features": "Elevation_Points", "value_field": "Elevation", "out_raster": "DEM_from_points"}
            ]
        },
        "idw_interpolation": {
            "name": "idw_interpolation",
            "description": "Interpolates a raster surface from points using an inverse distance weighted (IDW) technique.",
            "parameters": {
                "in_point_features": {"type": "string", "description": "The input point features."},
                "z_field": {"type": "string", "description": "The field that holds the height or magnitude value for each point."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_point_features", "z_field", "out_raster"],
            "action_input_examples": [
                {"function_name": "idw_interpolation", "in_point_features": "Rainfall_Gauges", "z_field": "Rainfall_mm", "out_raster": "Rainfall_Surface"}
            ]
        },
        "kriging_interpolation": {
            "name": "kriging_interpolation",
            "description": "Interpolates a raster surface from points using kriging.",
            "parameters": {
                "in_point_features": {"type": "string", "description": "The input point features."},
                "z_field": {"type": "string", "description": "The field that holds the height or magnitude value for each point."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_point_features", "z_field", "out_raster"],
            "action_input_examples": [
                {"function_name": "kriging_interpolation", "in_point_features": "Ozone_Monitors", "z_field": "Ozone_Level", "out_raster": "Ozone_Surface"}
            ]
        },
        "spline_interpolation": {
            "name": "spline_interpolation",
            "description": "Interpolates a raster surface from points using a spline.",
            "parameters": {
                "in_point_features": {"type": "string", "description": "The input point features."},
                "z_field": {"type": "string", "description": "The field that holds the height or magnitude value for each point."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_point_features", "z_field", "out_raster"],
            "action_input_examples": [
                {"function_name": "spline_interpolation", "in_point_features": "Water_Table_Wells", "z_field": "Water_Depth", "out_raster": "Water_Table_Surface"}
            ]
        },
        "natural_neighbor": {
            "name": "natural_neighbor",
            "description": "Interpolates a raster surface from points using natural neighbor.",
            "parameters": {
                "in_point_features": {"type": "string", "description": "The input point features."},
                "z_field": {"type": "string", "description": "The field that holds the height or magnitude value for each point."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_point_features", "z_field", "out_raster"],
            "action_input_examples": [
                {"function_name": "natural_neighbor", "in_point_features": "Air_Quality_Sensors", "z_field": "PM2_5", "out_raster": "PM25_Surface"}
            ]
        },
        "euclidean_distance": {
            "name": "euclidean_distance",
            "description": "Calculates for each cell the Euclidean distance to the closest source.",
            "parameters": {
                "in_source_data": {"type": "string", "description": "The input source data."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_source_data", "out_raster"],
            "action_input_examples": [
                {"function_name": "euclidean_distance", "in_source_data": "Hospitals", "out_raster": "Distance_to_Hospitals"}
            ]
        },
        "euclidean_allocation": {
            "name": "euclidean_allocation",
            "description": "Calculates, for each cell, the nearest source based on Euclidean distance.",
            "parameters": {
                "in_source_data": {"type": "string", "description": "The input source data."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_source_data", "out_raster"],
            "action_input_examples": [
                {"function_name": "euclidean_allocation", "in_source_data": "Fire_Stations", "out_raster": "Fire_Station_Zones"}
            ]
        },
        "euclidean_direction": {
            "name": "euclidean_direction",
            "description": "Calculates, for each cell, the direction in degrees to the nearest source.",
            "parameters": {
                "in_source_data": {"type": "string", "description": "The input source data."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_source_data", "out_raster"],
            "action_input_examples": [
                {"function_name": "euclidean_direction", "in_source_data": "Cell_Towers", "out_raster": "Direction_to_Towers"}
            ]
        },
        "cost_distance": {
            "name": "cost_distance",
            "description": "Calculates the least accumulative cost distance for each cell to the nearest source over a cost surface.",
            "parameters": {
                "in_source_data": {"type": "string", "description": "The input source data."},
                "in_cost_raster": {"type": "string", "description": "A raster defining the impedance or cost to move planimetrically through each cell."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_source_data", "in_cost_raster", "out_raster"],
            "action_input_examples": [
                {"function_name": "cost_distance", "in_source_data": "Trailheads", "in_cost_raster": "Slope_Cost", "out_raster": "Hiking_Cost_Distance"}
            ]
        },
        "cost_allocation": {
            "name": "cost_allocation",
            "description": "Calculates, for each cell, its least-cost source based on the least accumulative cost over a cost surface.",
            "parameters": {
                "in_source_data": {"type": "string", "description": "The input source data."},
                "in_cost_raster": {"type": "string", "description": "A raster defining the impedance or cost to move planimetrically through each cell."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_source_data", "in_cost_raster", "out_raster"],
            "action_input_examples": [
                {"function_name": "cost_allocation", "in_source_data": "Distribution_Centers", "in_cost_raster": "Travel_Time", "out_raster": "Delivery_Zones"}
            ]
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
            "required": ["in_destination_data", "in_cost_distance_raster", "in_cost_backlink_raster", "out_raster"],
            "action_input_examples": [
                {"function_name": "cost_path", "in_destination_data": "Campsite", "in_cost_distance_raster": "Hiking_Cost_Distance", "in_cost_backlink_raster": "Hiking_Cost_Backlink", "out_raster": "Optimal_Trail"}
            ]
        },
        "weighted_overlay": {
            "name": "weighted_overlay",
            "description": "Overlays several rasters using a common measurement scale and weights each according to its importance.",
            "parameters": {
                "overlay_table": {"type": "string", "description": "The weighted overlay table."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["overlay_table", "out_raster"],
            "action_input_examples": [
                {"function_name": "weighted_overlay", "overlay_table": "('Slope' 0.5; 'Aspect' 0.2; 'Land_Use' 0.3)", "out_raster": "Suitability_Map"}
            ]
        },
        "weighted_sum": {
            "name": "weighted_sum",
            "description": "Overlays several rasters, multiplying each by their given weight and summing them together.",
            "parameters": {
                "in_rasters": {"type": "string", "description": "The weighted sum table."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_rasters", "out_raster"],
            "action_input_examples": [
                {"function_name": "weighted_sum", "in_rasters": "('Slope' 'Weight_Slope'; 'Aspect' 'Weight_Aspect')", "out_raster": "Habitat_Score"}
            ]
        },
        "extract_by_attribute": {
            "name": "extract_by_attribute",
            "description": "Extracts cells from a raster based on a logical query.",
            "parameters": {
                "in_raster": {"type": "string", "description": "The input raster."},
                "where_clause": {"type": "string", "description": "A logical expression to select a subset of raster cells."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_raster", "where_clause", "out_raster"],
            "action_input_examples": [
                {"function_name": "extract_by_attribute", "in_raster": "Elevation", "where_clause": "Value > 1000", "out_raster": "High_Elevation_Areas"}
            ]
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
            "required": ["input_rasters", "output_location", "raster_dataset_name_with_extension", "pixel_type", "number_of_bands"],
            "action_input_examples": [
                {"function_name": "mosaic_to_new_raster", "input_rasters": ["Tile1.tif", "Tile2.tif"], "output_location": "/path/to/output", "raster_dataset_name_with_extension": "Mosaic.tif", "pixel_type": "8_BIT_UNSIGNED", "number_of_bands": 3}
            ]
        },
        "combine_rasters": {
            "name": "combine_rasters",
            "description": "Combines multiple rasters so that a unique output value is assigned to each unique combination of input values.",
            "parameters": {
                "in_rasters": {"type": "array", "items": {"type": "string"}, "description": "A list of input rasters."},
                "out_raster": {"type": "string", "description": "The output raster."}
            },
            "required": ["in_rasters", "out_raster"],
            "action_input_examples": [
                {"function_name": "combine_rasters", "in_rasters": ["Slope_Class", "Aspect_Class"], "out_raster": "Combined_Classes"}
            ]
        },
        "invert_selection": {
            "name": "invert_selection",
            "description": "Invert the current selection on a layer.",
            "parameters": {
                "layer_name": {"type": "string", "description": "The name of the layer."}
            },
            "required": ["layer_name"],
            "action_input_examples": [
                {"function_name": "invert_selection", "layer_name": "Parcels_For_Sale"}
            ]
        }
    }
    