"""
Function Declarations for AI Models
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
}

# Generate AVAILABLE_FUNCTIONS dynamically from functions_declarations
AVAILABLE_FUNCTIONS = {i + 1: name for i, name in enumerate(functions_declarations.keys())}

def get_functions_declaration(function_ids: list[int]) -> dict:
    """
    Returns the signature and description of functions by their IDs.
    """
    result = {}
    for func_id in function_ids:
        if func_id in AVAILABLE_FUNCTIONS:
            func_name = AVAILABLE_FUNCTIONS[func_id]
            if func_name in functions_declarations:
                result[func_name] = functions_declarations[func_name]
    return result
