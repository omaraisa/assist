import json
import os
from datetime import datetime
from typing import Dict, List, Any

DASHBOARD_FILE = "progent_dashboard.json"

# Private helper functions

def _get_timestamp() -> str:
    """Get current timestamp in ISO format"""
    return datetime.now().isoformat()

def _load_dashboard() -> Dict:
    """
    Safely loads the dashboard file.
    Returns dashboard data or a default skeleton if the file doesn't exist or is empty.
    """
    if not os.path.exists(DASHBOARD_FILE) or os.path.getsize(DASHBOARD_FILE) == 0:
        return {
            "success": True,
            "is_dashboard_update": False,
            "layer_name": None,
            "dashboard_title": "New Dashboard",
            "theme": "default",
            "layout": {"grid_template_columns": "1fr", "gap": "20px", "items": []},
            "charts": [],
            "field_insights": {},
            "generation_timestamp": _get_timestamp()
        }
    try:
        with open(DASHBOARD_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading dashboard file: {e}")
        return {
            "success": False, "error": str(e), "charts": [], "field_insights": {},
            "layout": {"grid_template_columns": "1fr", "gap": "20px", "items": []}
        }

def _save_dashboard(data: Dict) -> bool:
    """Saves the dashboard data to the dashboard file."""
    try:
        with open(DASHBOARD_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"Error saving dashboard file: {e}")
        return False

def _fetch_layer_fields(layer_name: str) -> List[Dict]:
    """Placeholder function to simulate fetching fields from a GIS layer."""
    print(f"Simulating fetch for layer: {layer_name}")
    return [
        {"field_name": "Acres", "type": "numeric", "sample_values": [10.2, 5.5, 23.1]},
        {"field_name": "LandUse", "type": "categorical", "sample_values": ["Residential", "Commercial", "Residential"]},
        {"field_name": "Owner", "type": "categorical", "sample_values": ["Corp", "Smith", "Corp"]},
        {"field_name": "LastUpdate", "type": "date", "sample_values": ["2023-01-15", "2022-08-20", "2023-02-10"]},
        {"field_name": "Value", "type": "numeric", "sample_values": [150000, 320000, 120000]},
        {"field_name": "TaxRate", "type": "numeric", "sample_values": [0.015, 0.02, 0.015]},
    ]

def _prepare_field_insights_from_layer(fields: List[Dict]) -> Dict:
    """Minimalist adapter to create field_insights from raw field metadata."""
    insights = {}
    for i, field in enumerate(fields):
        field_name = field.get("field_name")
        insights[field_name] = {
            "field_name": field_name,
            "data_category": "numeric" if field.get("type") == "numeric" else "categorical",
            "visualization_priority": 10 - i if field.get("type") == "numeric" else 5 - i,
            "chart_suitability": {"bar": 0.8, "pie": 0.5} if field.get("type") == "categorical" else {"histogram": 0.9, "bar": 0.6},
            "data_story": f"Analysis of {field_name}",
            "visualization_potential": "high" if field.get("type") == "numeric" else "medium",
            "sample_values": field.get("sample_values", [])
        }
    return insights

def _create_chart_from_field(field_info: Dict, theme: str) -> Dict:
    """Create chart configuration from field information"""
    field_name = field_info.get("field_name")
    best_chart_type = max(field_info.get("chart_suitability", {}).items(), key=lambda x: x[1])[0] if field_info.get("chart_suitability") else "bar"
    return {
        "id": f"chart_{field_name}",
        "field_name": field_name,
        "chart_type": best_chart_type,
        "title": field_info.get("data_story", f"Analysis of {field_name}"),
        "theme": theme
    }

def _rebuild_layout(charts: List[Dict]) -> Dict:
    """Rebuilds the entire layout based on the current list of charts."""
    num_charts = len(charts)
    if num_charts == 1:
        grid_cols = "1fr"
    elif 2 <= num_charts <= 4:
        grid_cols = "1fr 1fr"
    elif 5 <= num_charts <= 9:
        grid_cols = "1fr 1fr 1fr"
    else: # 10+ charts
        grid_cols = "1fr 1fr 1fr 1fr"

    layout_items = []
    for i, chart in enumerate(charts):
        layout_items.append({
            "id": chart.get("id"),
            "chart_type": chart.get("chart_type"),
            "field_name": chart.get("field_name"),
            "grid_area": f"chart-{i+1}"
        })
    return {"grid_template_columns": grid_cols, "gap": "20px", "items": layout_items}

# Canonical dashboard generator
def generate_smart_dashboard_layout(layer_name: str, field_insights: Dict, theme: str = "default") -> Dict:
    """Generate smart dashboard layout using field insights"""
    prioritized_fields = sorted(field_insights.values(), key=lambda x: x.get("visualization_priority", 0), reverse=True)
    top_fields = prioritized_fields[:6]
    charts = [chart for field_info in top_fields if (chart := _create_chart_from_field(field_info, theme))]

    result = {
        "layer_name": layer_name,
        "dashboard_title": f"Smart Dashboard for {layer_name}",
        "theme": theme,
        "charts": charts,
        "layout": _rebuild_layout(charts),
        "field_insights": field_insights,
        "generation_timestamp": _get_timestamp()
    }

    if _save_dashboard(result):
        return {"success": True, "is_dashboard_update": True, "message": f"Dashboard generated for '{layer_name}' with {len(charts)} charts.", "chart_count": len(charts)}
    return {"success": False, "message": "Failed to save dashboard."}

# Mission-oriented wrapper functions
def mission_generate_dashboard(layer_name: str, source: str = None, field_insights: Dict = None) -> Dict:
    """
    Mission: Generate a new dashboard.
    If 'source' is not provided, it intelligently decides. If the dashboard is empty, it uses 'layer'; otherwise, it uses 'dashboard'.
    """
    try:
        dashboard_data = _load_dashboard()
        # If source is not specified, make an intelligent choice
        if source is None:
            source = "layer" if not dashboard_data.get("charts") else "dashboard"

        final_insights = field_insights
        if not final_insights:
            if source == "layer":
                fields = _fetch_layer_fields(layer_name)
                final_insights = _prepare_field_insights_from_layer(fields)
            else: # source == "dashboard"
                final_insights = dashboard_data.get("field_insights")

        if not final_insights:
            return {"success": False, "message": "Could not get field insights to generate dashboard."}

        return generate_smart_dashboard_layout(layer_name, field_insights=final_insights)
    except Exception as e:
        return {"success": False, "message": str(e)}

def mission_get_layout() -> Dict:
    """Mission: Get the current dashboard layout."""
    data = _load_dashboard()
    return {"success": True, "message": "Layout retrieved.", "data": data.get("layout", {})}

def mission_get_charts() -> Dict:
    """Mission: Get the current dashboard charts."""
    data = _load_dashboard()
    return {"success": True, "message": "Charts retrieved.", "data": data.get("charts", [])}

def mission_get_field_info(field_name: str = None) -> Dict:
    """Mission: Get information about fields in the dashboard."""
    insights = _load_dashboard().get("field_insights", {})
    if field_name:
        return {"success": True, "data": insights.get(field_name)} if field_name in insights else {"success": False, "message": f"Field '{field_name}' not found."}
    return {"success": True, "message": "All field info retrieved.", "data": insights}

def mission_update_charts(charts_data: List[Dict]) -> Dict:
    """
    Mission: Update existing charts by replacing them.
    Payload is a list of dicts, each with 'index' and the new 'chart' object.
    """
    dashboard = _load_dashboard()
    charts = dashboard.get("charts", [])
    updated_count = 0
    for update in charts_data:
        index = update.get("index")
        new_chart_data = update.get("chart")
        if index is not None and new_chart_data and 0 <= index < len(charts):
            charts[index] = new_chart_data # Full replacement
            updated_count += 1

    dashboard["charts"] = charts
    dashboard["layout"] = _rebuild_layout(charts) # Rebuild layout to reflect potential changes
    if _save_dashboard(dashboard):
        return {"success": True, "is_dashboard_update": True, "message": f"Successfully updated {updated_count} charts.", "data": {"updated_count": updated_count}}
    return {"success": False, "message": "Failed to save updated dashboard."}

def mission_add_charts(new_charts: List[Dict]) -> Dict:
    """Mission: Add new charts to the dashboard."""
    dashboard = _load_dashboard()
    charts = dashboard.get("charts", [])
    for i, new_chart in enumerate(new_charts):
        if "fields" in new_chart and "chart_type" in new_chart:
            chart_to_add = {
                "id": f"chart_new_{len(charts) + i}",
                "field_name": new_chart.get("fields")[0],
                "title": f"Analysis of {new_chart.get('fields')[0]}",
                **new_chart
            }
            charts.append(chart_to_add)

    dashboard["charts"] = charts
    dashboard["layout"] = _rebuild_layout(charts)
    if _save_dashboard(dashboard):
        return {"success": True, "is_dashboard_update": True, "message": f"Successfully added {len(new_charts)} new charts.", "data": {"added_count": len(new_charts)}}
    return {"success": False, "message": "Failed to save dashboard with new charts."}

def mission_delete_charts(indices: List[int]) -> Dict:
    """
    Mission: Delete charts from the dashboard by their indices.
    """
    dashboard = _load_dashboard()
    charts = dashboard.get("charts", [])

    # Sort indices in reverse order to avoid index shifting issues during deletion
    sorted_indices = sorted(indices, reverse=True)
    deleted_count = 0
    for index in sorted_indices:
        if 0 <= index < len(charts):
            charts.pop(index)
            deleted_count += 1

    dashboard["charts"] = charts
    dashboard["layout"] = _rebuild_layout(charts) # Rebuild layout after deletion
    if _save_dashboard(dashboard):
        return {"success": True, "is_dashboard_update": True, "message": f"Successfully deleted {deleted_count} charts.", "data": {"deleted_count": deleted_count}}
    return {"success": False, "message": "Failed to save dashboard after deleting charts."}
