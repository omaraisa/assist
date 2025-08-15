"""
Function Declarations for AI Models
"""

class FunctionDeclaration:
    """Generate function declarations for different AI models"""
    
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
        
        "get_attribute_table": {
            "name": "get_attribute_table",
            "description": "Get attribute table data from a layer with pagination support. Use with caution as it can return large datasets.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer"
                },
                "start_row": {
                    "type": "integer",
                    "description": "Starting row index (0-based)",
                    "default": 0
                },
                "row_count": {
                    "type": "integer",
                    "description": "Number of rows to return",
                    "default": 100
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
        
        "analyze_layer_fields": {
            "name": "analyze_layer_fields",
            "description": "Analyze all fields in a GIS layer to understand their characteristics for dashboard generation. Returns detailed field metadata including data types, unique values, null percentages, statistical summaries, and data categories (numeric, categorical, date, etc.).",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to analyze"
                }
            },
            "required": ["layer_name"]
        },
        

        "generate_smart_dashboard_layout": {
            "name": "generate_smart_dashboard_layout",
            "description": "Stage 2: Enhanced Chart Recommendation Engine with intelligent chart selection and 12x6 grid layout planning. Generates sophisticated dashboard layouts with optimized chart recommendations, detailed configurations, and positioning. This is the main function for Stage 2 of dashboard generation.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to generate smart dashboard layout for"
                }
            },
            "required": ["layer_name"]
        },
        "optimize_dashboard_layout": {
            "name": "optimize_dashboard_layout",
            "description": "Validate and arrange a dashboard layout for a 12x6 grid. Checks widget positions, sizes, overlap, and grid fit. Saves the layout to smart_dashboard.json if valid. Returns validation results and the layout.",
            "parameters": {
                "layout": {
                    "type": "array",
                    "description": "Array of dashboard widget objects to validate. Each object must include: id (string), x (int), y (int), w (int), h (int). Optionally, field(s) and chart_type can be included for AI awareness.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string", "description": "Unique widget identifier"},
                            "x": {"type": "integer", "description": "Left grid position (0-11)"},
                            "y": {"type": "integer", "description": "Top grid position (0-5)"},
                            "w": {"type": "integer", "description": "Widget width (columns)"},
                            "h": {"type": "integer", "description": "Widget height (rows)"}
                        },
                        "required": ["id", "x", "y", "w", "h"]
                    }
                }
            },
            "required": ["layout"],
            "returns": {
                "optimized_layout": "The validated layout array (same as input if valid)",
                "success": "True if layout is valid, False if errors found",
                "errors": "List of error messages if validation fails"
            }
        },
        "get_current_dashboard_layout": {
            "name": "get_current_dashboard_layout",
            "description": "Get the current dashboard layout from the smart_dashboard.json file. Returns a list of widgets with id, x, y, w, h, and fields.",
            "parameters": {},
            "returns": {
                "widgets": "List of minimal widget info (id, x, y, w, h, fields)",
                "success": "True if loaded, False if error"
            }
        },
        "get_field_stories_and_samples": {
            "name": "get_field_stories_and_samples",
            "description": "Returns a summary for each field: field_name, data_story, and sample_values from smart_dashboard.json. Handles empty or invalid JSON files gracefully.",
            "parameters": {},
            "returns": {
                "fields": "List of dicts with field_name, data_story, and sample_values",
                "success": "True if loaded, False if error"
            }
        },
        "get_current_dashboard_charts": {
            "name": "get_current_dashboard_charts",
            "description": "Get the current [fields, chart_type] pairs from the dashboard layout in smart_dashboard.json. Returns a list of dicts: {'fields': [...], 'chart_type': ...}",
            "parameters": {},
            "returns": {
                "charts": "List of dicts with fields and chart_type",
                "success": "True if loaded, False if error"
            }
        },
        "update_dashboard_charts": {
            "name": "update_dashboard_charts",
            "description": "Updates the dashboard layout with a new set of charts. The `fields` parameter can be a list of strings (for simple charts) or a dictionary mapping field roles (e.g., x_axis, y_axis, category) for more complex charts.",
            "parameters": {
                "charts": {
                    "type": "array",
                    "description": "List of chart configuration objects. Each object should have 'fields' and 'chart_type'.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "fields": {
                                "type": ["array", "object"],
                                "description": "Either an array of field names or an object mapping roles like 'x_axis', 'y_axis' to field names."
                            },
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
        "update_chart_by_id": {
            "name": "update_chart_by_id",
            "description": "Updates a single chart on the dashboard by its unique widget ID. This allows for targeted changes to a specific chart's type or data fields.",
            "parameters": {
                "widget_id": {
                    "type": "string",
                    "description": "The unique ID of the widget to update (e.g., 'widget_fieldName')."
                },
                "chart_config": {
                    "type": "object",
                    "description": "An object containing the new chart configuration. It must have 'chart_type' and 'fields'.",
                    "properties": {
                        "chart_type": {
                            "type": "string",
                            "description": "The new type for the chart (e.g., 'bar', 'pie', 'scatter')."
                        },
                        "fields": {
                            "type": ["array", "object"],
                            "description": "The new fields for the chart. Can be a list of strings or a dictionary mapping roles (e.g., x_axis, y_axis)."
                        }
                    },
                    "required": ["chart_type", "fields"]
                }
            },
            "required": ["widget_id", "chart_config"],
            "returns": {
                "success": "True if the chart was updated successfully.",
                "widget_id": "The ID of the updated widget.",
                "error": "A description of the error if the update failed."
            }
        },
        "recommend_chart_types": {
            "name": "recommend_chart_types",
            "description": "Enhanced AI-Powered Chart Type Recommendation System (Step 3). Analyzes both single-field characteristics and multi-field relationships to recommend diverse chart types that avoid the 'too many histograms' problem. Features: field relationship detection for scatter plots/grouped charts, token-efficient AI prompts, chart diversity optimization, and integration with existing retry mechanisms.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to analyze for enhanced chart recommendations"
                },
                "target_field": {
                    "type": "string",
                    "description": "Optional specific field to focus chart recommendations on"
                }
            },
            "required": ["layer_name"]
        },
        "plan_dashboard_layout": {
            "name": "plan_dashboard_layout",
            "description": "AI-Powered Dashboard Layout Planning System. Uses AI to create optimal dashboard layouts that maximize space utilization and visual effectiveness. Works with chart recommendations to create intelligent 12x6 grid layouts with proper positioning and sizing.",
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to plan dashboard layout for"
                },
                "chart_recommendations": {
                    "type": "array",
                    "description": "Optional array of chart recommendation objects. If not provided, will use existing recommendations or generate new ones",
                    "items": {
                        "type": "object"
                    }
                }
            },
            "required": ["layer_name"]
        },
    }
