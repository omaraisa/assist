import json
import os
import uuid
import random
from datetime import datetime
from typing import Dict, List, Any
from .ai.function_declarations import FunctionDeclaration

# Build AVAILABLE_FUNCTIONS dynamically from the authoritative declarations
# The numeric IDs are assigned deterministically based on the declaration order.

AVAILABLE_FUNCTIONS = {
    1: "select_by_attribute",
    2: "select_by_location",
    3: "get_field_statistics",
    4: "get_layer_summary",
    5: "calculate_area",
    6: "calculate_length",
    7: "get_centroid",
    8: "create_buffer",
    9: "spatial_join",
    10: "clip_layer",
    11: "calculate_distance",
    12: "get_current_project_path",
    13: "get_default_db_path",
    14: "get_field_definitions",
    15: "get_layer_type",
    16: "get_list_of_layer_fields",
    17: "get_data_source_info",
    18: "create_nearest_neighbor_layer",
    19: "get_unique_values_count",
    20: "calculate_empty_values",
    21: "get_map_layers_info",
    22: "get_map_tables_info",
    23: "get_values_frequency",
    24: "get_value_frequency",
    25: "get_coordinate_system",
    26: "clear_selection",
    27: "get_field_domain_values",
    28: "calculate_new_field",
    29: "analyze_layer_fields",
    30: "generate_smart_dashboard_layout",
    31: "optimize_dashboard_layout",
    32: "recommend_chart_types",
    33: "get_current_dashboard_layout",
    34: "get_field_stories_and_samples",
    35: "get_current_dashboard_charts",
    36: "update_dashboard_charts",
    37: "raster_calculator",
    38: "reclassify",
    39: "zonal_statistics_as_table",
    40: "slope",
    41: "aspect",
    42: "hillshade",
    43: "extract_by_mask",
    44: "clip_raster",
    45: "resample",
    46: "get_raster_properties",
    47: "raster_to_point",
    48: "raster_to_polygon",
    49: "raster_to_polyline",
    50: "feature_to_raster",
    51: "polygon_to_raster",
    52: "point_to_raster",
    53: "idw_interpolation",
    54: "kriging_interpolation",
    55: "spline_interpolation",
    56: "natural_neighbor",
    57: "euclidean_distance",
    58: "euclidean_allocation",
    59: "euclidean_direction",
    60: "cost_distance",
    61: "cost_allocation",
    62: "cost_path",
    63: "weighted_overlay",
    64: "weighted_sum",
    65: "extract_by_attribute",
    66: "mosaic_to_new_raster",
    67: "combine_rasters",
    68: "invert_selection"
}

try:
	decls = FunctionDeclaration.functions_declarations
	# Preserve declaration order; assign IDs starting at 1
	for i, name in enumerate(decls.keys(), start=1):
		AVAILABLE_FUNCTIONS[i] = name
except Exception:
	AVAILABLE_FUNCTIONS = {}

def format_available_functions() -> str:
	"""Return a compact single-line listing like '1: name, 2: name'"""
	parts = [f"{k}: {v}" for k, v in sorted(AVAILABLE_FUNCTIONS.items())]
	return ", ".join(parts)


# Dashboard manipulation functions (server-side)
def generate_smart_dashboard_layout(layer_name: str, analysis_type: str = "overview", theme: str = "default", field_insights: Dict = None) -> Dict:
    """Generate smart dashboard layout using field insights"""
    try:
        if not field_insights:
            return {"success": False, "error": "Field insights are required for dashboard generation"}
        
        # Step 2: Prioritize fields based on AI insights
        print(f"DEBUG: Field insights keys: {list(field_insights.keys())}")
        print(f"DEBUG: Total fields for prioritization: {len(field_insights)}")
        
        prioritized_fields = sorted(
            field_insights.values(),
            key=lambda x: x.get("visualization_priority", 0),
            reverse=True
        )
        
        print(f"DEBUG: Prioritized fields count: {len(prioritized_fields)}")
        for i, field in enumerate(prioritized_fields[:3]):  # Show top 3
            print(f"DEBUG: Field {i+1}: {field.get('field_name', 'unknown')} priority: {field.get('visualization_priority', 0)}")
        
        # Step 3: Select top fields for the dashboard (e.g., top 6)
        top_fields = prioritized_fields[:6]
        print(f"DEBUG: Selected top {len(top_fields)} fields for dashboard")
        
        # Step 4: Generate chart configurations for each selected field
        charts = []
        print(f"DEBUG: Processing {len(top_fields)} top fields for charts")
        for i, field_info in enumerate(top_fields):
            print(f"DEBUG: Processing field {i+1}: {field_info.get('field_name', 'unknown')}")
            chart_config = _create_chart_from_field(field_info, theme)
            if chart_config:
                charts.append(chart_config)
                print(f"DEBUG: Added chart config for field {field_info.get('field_name', 'unknown')}")
            else:
                print(f"DEBUG: No chart config created for field {field_info.get('field_name', 'unknown')}")
        
        print(f"DEBUG: Total charts created: {len(charts)}")
        
        # Step 5: Arrange charts into a layout
        layout = _arrange_charts_in_layout(charts)
        
        result = {
            "success": True,
            "is_dashboard_update": True,
            "layer_name": layer_name,
            "dashboard_title": f"{analysis_type.title()} Dashboard for {layer_name}",
            "theme": theme,
            "layout": layout,
            "charts": charts,
            "field_insights": field_insights,
            "generation_timestamp": _get_timestamp()
        }
        
        # Save to progent_dashboard.json
        dashboard_path = "progent_dashboard.json"
        with open(dashboard_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4, ensure_ascii=False)
        
        # Return simple acknowledgment to AI (to save API credits)
        return {
            "success": True,
            "is_dashboard_update": True,
            "message": f"Dashboard successfully generated for '{layer_name}' with {len(charts)} charts",
            "layer_name": layer_name,
            "chart_count": len(charts),
            "dashboard_saved": True
        }
        
    except Exception as e:
        return {"success": False, "error": str(e)}


def _create_chart_from_field(field_info: Dict, theme: str) -> Dict:
    """Create chart configuration from field information"""
    try:
        field_name = field_info.get("field_name")
        data_category = field_info.get("data_category", "unknown")
        chart_suitability = field_info.get("chart_suitability", {})
        visualization_potential = field_info.get("visualization_potential", "low")
        
        if visualization_potential == "low" or not chart_suitability:
            return None
        
        # Get the best chart type
        best_chart_type = max(chart_suitability.items(), key=lambda x: x[1])[0] if chart_suitability else "bar"
        
        chart_config = {
            "id": f"chart_{field_name}",
            "field_name": field_name,
            "chart_type": best_chart_type,
            "data_category": data_category,
            "title": field_info.get("data_story", f"Analysis of {field_name}"),
            "visualization_potential": visualization_potential,
            "chart_suitability": chart_suitability,
            "theme": theme
        }
        
        return chart_config
        
    except Exception as e:
        print(f"Error creating chart for field: {e}")
        return None


def _arrange_charts_in_layout(charts: List[Dict]) -> Dict:
    """Arrange charts in a responsive grid layout"""
    try:
        num_charts = len(charts)
        if num_charts == 0:
            return {
                "grid_template_columns": "1fr",
                "gap": "20px",
                "items": []
            }
        
        # Determine grid layout based on number of charts
        if num_charts <= 2:
            grid_cols = "1fr 1fr"
        elif num_charts <= 4:
            grid_cols = "1fr 1fr"
        else:
            grid_cols = "1fr 1fr 1fr"
        
        layout_items = []
        for i, chart in enumerate(charts):
            layout_items.append({
                "id": chart.get("id", f"chart_{i}"),
                "chart_type": chart.get("chart_type", "bar"),
                "field_name": chart.get("field_name", f"field_{i}"),
                "grid_area": f"chart-{i+1}"
            })
        
        return {
            "grid_template_columns": grid_cols,
            "gap": "20px",
            "items": layout_items
        }
        
    except Exception as e:
        print(f"Error arranging charts in layout: {e}")
        return {
            "grid_template_columns": "1fr",
            "gap": "20px", 
            "items": []
        }


def _get_timestamp() -> str:
    """Get current timestamp in ISO format"""
    return datetime.now().isoformat()


def get_current_dashboard_layout() -> Dict:
    """Get current dashboard layout from progent_dashboard.json"""
    try:
        dashboard_path = "progent_dashboard.json"
        if not os.path.exists(dashboard_path):
            return {"success": False, "error": "Dashboard file not found"}
        
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return {
            "success": True,
            "layout": data.get("layout", {}),
            "charts": data.get("charts", [])
        }
        
    except Exception as e:
        return {"success": False, "error": str(e)}


def get_current_dashboard_charts() -> Dict:
    """Get current dashboard charts from progent_dashboard.json"""
    try:
        dashboard_path = "progent_dashboard.json"
        if not os.path.exists(dashboard_path):
            return {"success": False, "error": "Dashboard file not found"}
        
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        charts = data.get("charts", [])
        chart_pairs = []
        
        for chart in charts:
            chart_pairs.append({
                "fields": [chart.get("field_name")],
                "chart_type": chart.get("chart_type")
            })
        
        return {
            "success": True,
            "charts": chart_pairs
        }
        
    except Exception as e:
        return {"success": False, "error": str(e)}


def get_field_stories_and_samples() -> Dict:
    """Get field stories and samples from progent_dashboard.json"""
    try:
        dashboard_path = "progent_dashboard.json"
        if not os.path.exists(dashboard_path):
            return {"success": False, "error": "Dashboard file not found"}
        
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        field_insights = data.get("field_insights", {})
        stories = {}
        
        for field_name, field_data in field_insights.items():
            stories[field_name] = {
                "field_name": field_name,
                "data_story": field_data.get("data_story", ""),
                "sample_values": field_data.get("sample_values", [])
            }
        
        return {
            "success": True,
            "field_stories": stories
        }
        
    except Exception as e:
        return {"success": False, "error": str(e)}


def update_dashboard_charts(charts_data: List[Dict]) -> Dict:
    """Update dashboard charts in progent_dashboard.json"""
    try:
        dashboard_path = "progent_dashboard.json"
        if not os.path.exists(dashboard_path):
            return {"success": False, "error": "Dashboard file not found"}
        
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update charts
        updated_charts = []
        layout_items = []
        
        for i, chart_data in enumerate(charts_data):
            fields = chart_data.get("fields", [])
            chart_type = chart_data.get("chart_type", "bar")
            
            if fields:
                field_name = fields[0]  # Use first field
                
                chart_config = {
                    "id": f"chart_{field_name}",
                    "field_name": field_name,
                    "chart_type": chart_type,
                    "title": f"Analysis of {field_name}",
                    "theme": data.get("theme", "default")
                }
                
                updated_charts.append(chart_config)
                
                layout_items.append({
                    "id": chart_config["id"],
                    "chart_type": chart_type,
                    "field_name": field_name,
                    "grid_area": f"chart-{i+1}"
                })
        
        # Update layout
        num_charts = len(updated_charts)
        if num_charts <= 2:
            grid_cols = "1fr 1fr"
        elif num_charts <= 4:
            grid_cols = "1fr 1fr"
        else:
            grid_cols = "1fr 1fr 1fr"
        
        data["charts"] = updated_charts
        data["layout"] = {
            "grid_template_columns": grid_cols,
            "gap": "20px",
            "items": layout_items
        }
        data["generation_timestamp"] = _get_timestamp()
        
        # Save updated data
        with open(dashboard_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        return {
            "success": True,
            "message": f"Updated {len(updated_charts)} charts in dashboard"
        }
        
    except Exception as e:
        return {"success": False, "error": str(e)}

