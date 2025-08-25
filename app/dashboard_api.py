import json
import os
from typing import Dict, List, Any

DASHBOARD_FILE = "progent_dashboard.json"

# --- Private Helper Functions ---

def _load_dashboard() -> Dict:
    """
    Safely loads the dashboard data from progent_dashboard.json.
    Returns a default skeleton if the file doesn't exist.
    """
    if not os.path.exists(DASHBOARD_FILE):
        return {
            "dashboard_title": "New Dashboard",
            "charts": [],
            "layout": {"items": []},
            "field_insights": {}
        }
    try:
        with open(DASHBOARD_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {
            "dashboard_title": "New Dashboard",
            "charts": [],
            "layout": {"items": []},
            "field_insights": {}
        }

def _save_dashboard(data: Dict) -> bool:
    """
    Saves the provided data to progent_dashboard.json.
    Returns True on success, False on failure.
    """
    try:
        with open(DASHBOARD_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except IOError:
        return False

def _fetch_layer_fields(layer_name: str) -> List[Dict]:
    """
    Placeholder adapter to fetch and standardize field info from a GIS layer.
    In a real implementation, this would call arcpy.ListFields().

    Returns a list of field metadata dictionaries.
    """
    # This is a mock response for demonstration purposes.
    print(f"DEV: Simulating fetch for layer '{layer_name}'")
    return [
        {"field_name": "building_type", "type": "categorical", "sample_values": ["residential", "commercial"]},
        {"field_name": "height", "type": "numeric", "sample_values": [10, 25, 12.5]},
        {"field_name": "construction_year", "type": "date", "sample_values": ["2005-10-01", "2018-03-15"]},
        {"field_name": "area_sqm", "type": "numeric", "sample_values": [500, 1200.75]},
    ]

def _prepare_field_insights_from_layer(fields: List[Dict]) -> Dict:
    """
    Placeholder to generate minimal field_insights from standardized field info.
    In a real implementation, this might involve more sophisticated analysis.
    """
    insights = {}
    for i, field in enumerate(fields):
        insights[field["field_name"]] = {
            "field_name": field["field_name"],
            "data_category": f"{field['type']}",
            "visualization_priority": 8 - i, # Simple prioritization
            "data_story": f"Insight for {field['field_name']}",
            "sample_values": field["sample_values"],
            "chart_suitability": {"bar": 0.8, "pie": 0.7} if field['type'] == 'categorical' else {"histogram": 0.9}
        }
    return insights

from datetime import datetime

# --- Internal Canonical Generator ---

def _create_chart_from_field(field_info: Dict, theme: str) -> Dict:
    """Create chart configuration from field information"""
    try:
        field_name = field_info.get("field_name")
        data_category = field_info.get("data_category", "unknown")
        chart_suitability = field_info.get("chart_suitability", {})
        visualization_potential = field_info.get("visualization_potential", "low")

        if visualization_potential == "low" or not chart_suitability:
            return None

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
            return {"grid_template_columns": "1fr", "gap": "20px", "items": []}

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

        return {"grid_template_columns": grid_cols, "gap": "20px", "items": layout_items}

    except Exception as e:
        print(f"Error arranging charts in layout: {e}")
        return {"grid_template_columns": "1fr", "gap": "20px", "items": []}


def _get_timestamp() -> str:
    """Get current timestamp in ISO format"""
    return datetime.now().isoformat()


def _internal_generate_smart_dashboard_layout(layer_name: str, field_insights: Dict, analysis_type: str = "overview", theme: str = "default") -> Dict:
    """
    Internal canonical generator for creating a smart dashboard layout.
    This function is not exposed directly to the AI agent.
    """
    try:
        if not field_insights:
            return {"success": False, "error": "Field insights are required"}

        prioritized_fields = sorted(
            field_insights.values(),
            key=lambda x: x.get("visualization_priority", 0),
            reverse=True
        )

        top_fields = prioritized_fields[:6]
        charts = []
        for field_info in top_fields:
            chart_config = _create_chart_from_field(field_info, theme)
            if chart_config:
                charts.append(chart_config)

        layout = _arrange_charts_in_layout(charts)

        result = {
            "layer_name": layer_name,
            "dashboard_title": f"{analysis_type.title()} Dashboard for {layer_name}",
            "theme": theme,
            "layout": layout,
            "charts": charts,
            "field_insights": field_insights,
            "generation_timestamp": _get_timestamp()
        }

        if _save_dashboard(result):
            return {
                "success": True,
                "message": f"Dashboard successfully generated for '{layer_name}' with {len(charts)} charts.",
                "chart_count": len(charts)
            }
        else:
            return {"success": False, "error": "Failed to save dashboard"}

    except Exception as e:
        return {"success": False, "error": str(e)}

# --- Public Mission-Wrapper Functions ---

def mission_generate_dashboard(layer_name: str, source: str = None, field_insights: Dict = None) -> Dict:
    """
    Generates a smart dashboard for a given layer.

    Args:
        layer_name (str): The name of the layer to analyze.
        source (str, optional): "layer" to fetch fresh field data, or "dashboard" to use existing data.
                                Defaults to "dashboard" if a dashboard exists, otherwise "layer".
        field_insights (Dict, optional): Pre-computed field insights. If provided, these are used directly.

    Returns:
        Dict: A dictionary with success status and a message.
    """
    if not layer_name:
        return {"success": False, "message": "Layer name is required."}

    # Determine the source if not specified
    if source is None:
        source = "dashboard" if os.path.exists(DASHBOARD_FILE) else "layer"

    if source == "layer":
        print("DEV: Generating dashboard from layer fields.")
        fields = _fetch_layer_fields(layer_name)
        insights = _prepare_field_insights_from_layer(fields)
    elif source == "dashboard":
        print("DEV: Generating dashboard from existing dashboard field_insights.")
        dashboard_data = _load_dashboard()
        insights = dashboard_data.get("field_insights")
        if not insights:
            return {"success": False, "message": "No field insights found in the existing dashboard."}
    else:
        return {"success": False, "message": f"Invalid source: {source}. Must be 'layer' or 'dashboard'."}

    # If explicit field_insights are passed, they override everything
    if field_insights:
        insights = field_insights

    return _internal_generate_smart_dashboard_layout(layer_name, insights)


def mission_get_layout() -> Dict:
    """
    Retrieves the current dashboard layout, including charts and their arrangement.
    """
    dashboard_data = _load_dashboard()
    layout = dashboard_data.get("layout", {})
    charts = dashboard_data.get("charts", [])
    return {
        "success": True,
        "message": "Layout retrieved successfully.",
        "data": {
            "layout": layout,
            "charts": charts
        }
    }

def mission_get_charts() -> Dict:
    """
    Retrieves a simplified list of current dashboard charts.
    """
    dashboard_data = _load_dashboard()
    charts = dashboard_data.get("charts", [])
    chart_info = [
        {"id": c.get("id"), "fields": c.get("field_name"), "chart_type": c.get("chart_type")}
        for c in charts
    ]
    return {
        "success": True,
        "message": f"Retrieved {len(chart_info)} charts.",
        "data": chart_info
    }


def mission_get_field_info(field_name: str = None) -> Dict:
    """
    Retrieves information about fields from the dashboard's field_insights.

    Args:
        field_name (str, optional): The specific field to get info for. If None, returns info for all fields.

    Returns:
        Dict: A dictionary containing the field information.
    """
    dashboard_data = _load_dashboard()
    insights = dashboard_data.get("field_insights", {})

    if field_name:
        if field_name in insights:
            return {"success": True, "message": f"Info for field '{field_name}'.", "data": insights[field_name]}
        else:
            return {"success": False, "message": f"Field '{field_name}' not found."}
    else:
        return {"success": True, "message": "All field info retrieved.", "data": insights}


def mission_update_charts(charts_data: List[Dict]) -> Dict:
    """
    Updates existing charts in the dashboard.

    Args:
        charts_data (List[Dict]): A list of dictionaries, each with "index", "fields", and "chart_type".
                                  Example: [{"index": 1, "fields": ["height"], "chart_type": "histogram"}]
    """
    dashboard_data = _load_dashboard()
    charts = dashboard_data.get("charts", [])

    for update_info in charts_data:
        index = update_info.get("index")
        if index is not None and 0 <= index < len(charts):
            if "fields" in update_info:
                charts[index]["field_name"] = update_info["fields"][0]
                charts[index]["fields"] = update_info["fields"]
            if "chart_type" in update_info:
                charts[index]["chart_type"] = update_info["chart_type"]

    dashboard_data["charts"] = charts
    if _save_dashboard(dashboard_data):
        return {"success": True, "message": "Charts updated successfully."}
    else:
        return {"success": False, "message": "Failed to save updated dashboard."}


def mission_add_charts(new_charts: List[Dict]) -> Dict:
    """
    Adds new charts to the dashboard.

    Args:
        new_charts (List[Dict]): A list of new chart definitions.
                                 Example: [{"fields": ["new_field"], "chart_type": "pie"}]
    """
    dashboard_data = _load_dashboard()
    charts = dashboard_data.get("charts", [])

    for chart_def in new_charts:
        field_name = chart_def.get("fields", [f"new_chart_{len(charts)}"])[0]
        new_chart = {
            "id": f"chart_{field_name}_{len(charts)}",
            "field_name": field_name,
            "fields": chart_def.get("fields"),
            "chart_type": chart_def.get("chart_type", "bar"),
            "title": f"Analysis of {field_name}",
            "theme": "default"
        }
        charts.append(new_chart)

    dashboard_data["charts"] = charts
    dashboard_data["layout"] = _arrange_charts_in_layout(charts) # Re-arrange layout

    if _save_dashboard(dashboard_data):
        return {"success": True, "message": f"Added {len(new_charts)} new charts."}
    else:
        return {"success": False, "message": "Failed to save new charts."}
