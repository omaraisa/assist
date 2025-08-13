"""
Function Declarations for AI Models
"""

class FunctionDeclaration:
    """Generate function declarations for different AI models"""
    
    # Note: All chart-related functions (e.g., chart recommendations, dashboard layout planning) do not accept more than two fields per chart.
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
        # ... rest of the function declarations ...
        "recommend_chart_types": {
            "name": "recommend_chart_types",
            "description": (
                "Enhanced AI-Powered Chart Type Recommendation System (Step 3). "
                "Analyzes both single-field characteristics and multi-field relationships to recommend diverse chart types that avoid the 'too many histograms' problem. "
                "Features: field relationship detection for scatter plots/grouped charts, token-efficient AI prompts, chart diversity optimization, and integration with existing retry mechanisms. "
                "Note: No chart accepts more than two fields."
            ),
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
            "description": (
                "AI-Powered Dashboard Layout Planning System. Uses AI to create optimal dashboard layouts that maximize space utilization and visual effectiveness. "
                "Works with chart recommendations to create intelligent 12x6 grid layouts with proper positioning and sizing. "
                "Note: No chart accepts more than two fields."
            ),
            "parameters": {
                "layer_name": {
                    "type": "string",
                    "description": "The name of the layer to plan dashboard layout for"
                },
                "chart_recommendations": {
                    "type": "array",
                    "description": (
                        "Optional array of chart recommendation objects. If not provided, will use existing recommendations or generate new ones. "
                        "Note: Each chart recommendation must not contain more than two fields."
                    ),
                    "items": {
                        "type": "object"
                    }
                }
            },
            "required": ["layer_name"]
        },
        # ... rest of the function declarations ...
    }
