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
    Returns dashboard data or a default skeleton if the file doesn't exist.
    """
    if not os.path.exists(DASHBOARD_FILE):
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
        # Return a default skeleton on error
        return {
            "success": False,
            "error": str(e),
            "layer_name": None,
            "dashboard_title": "Error Dashboard",
            "theme": "default",
            "layout": {"grid_template_columns": "1fr", "gap": "20px", "items": []},
            "charts": [],
            "field_insights": {},
            "generation_timestamp": _get_timestamp()
        }

def _save_dashboard(data: Dict) -> bool:
    """
    Saves the dashboard data to the dashboard file.
    Returns True on success, False on failure.
    """
    try:
        with open(DASHBOARD_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"Error saving dashboard file: {e}")
        return False

def _fetch_layer_fields(layer_name: str) -> List[Dict]:
    """
    Placeholder function to simulate fetching fields from a GIS layer.
    In a real implementation, this would involve a call to the ArcGIS Pro client.
    Returns a list of field metadata dictionaries.
    """
    # This is a simulation. In a real scenario, this would trigger a request
    # to the ArcGIS Pro client to get layer field details.
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
    """
    Minimalist adapter to create field_insights from raw field metadata.
    This is a simplified version for demonstration. The real `analyze_layer_fields`
    would produce much richer insights.
    """
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


# Canonical dashboard generator (moved from progent_functions.py)

def generate_smart_dashboard_layout(layer_name: str, analysis_type: str = "overview", theme: str = "default", field_insights: Dict = None) -> Dict:
    """Generate smart dashboard layout using field insights"""
    try:
        if not field_insights:
            return {"success": False, "error": "Field insights are required for dashboard generation"}

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

        if _save_dashboard(result):
            return {
                "success": True,
                "is_dashboard_update": True,
                "message": f"Dashboard successfully generated for '{layer_name}' with {len(charts)} charts",
                "layer_name": layer_name,
                "chart_count": len(charts),
                "dashboard_saved": True
            }
        else:
            return {"success": False, "error": "Failed to save dashboard file."}

    except Exception as e:
        return {"success": False, "error": str(e)}


def _create_chart_from_field(field_info: Dict, theme: str) -> Dict:
    """Create chart configuration from field information"""
    field_name = field_info.get("field_name")
    data_category = field_info.get("data_category", "unknown")
    chart_suitability = field_info.get("chart_suitability", {})
    visualization_potential = field_info.get("visualization_potential", "low")

    if visualization_potential == "low" or not chart_suitability:
        return None

    best_chart_type = max(chart_suitability.items(), key=lambda x: x[1])[0] if chart_suitability else "bar"

    return {
        "id": f"chart_{field_name}",
        "field_name": field_name,
        "chart_type": best_chart_type,
        "data_category": data_category,
        "title": field_info.get("data_story", f"Analysis of {field_name}"),
        "visualization_potential": visualization_potential,
        "chart_suitability": chart_suitability,
        "theme": theme
    }


def _arrange_charts_in_layout(charts: List[Dict]) -> Dict:
    """Arrange charts in a responsive grid layout"""
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

    return {
        "grid_template_columns": grid_cols,
        "gap": "20px",
        "items": layout_items
    }

# Mission-oriented wrapper functions

def mission_generate_dashboard(layer_name: str, source: str = "dashboard", field_insights: Dict = None) -> Dict:
    """
    Mission: Generate a new dashboard.
    - If source is 'layer', it fetches field info from the GIS layer.
    - If source is 'dashboard', it uses existing field_insights from progent_dashboard.json.
    - If field_insights are provided directly, it uses them.
    """
    try:
        final_insights = None
        if field_insights:
            final_insights = field_insights
        elif source == "layer":
            # In a real scenario, we might need to trigger a call to the ArcGIS client here.
            # For now, we use the simulated fetch and prepare functions.
            fields = _fetch_layer_fields(layer_name)
            final_insights = _prepare_field_insights_from_layer(fields)
        else: # source == "dashboard"
            dashboard_data = _load_dashboard()
            final_insights = dashboard_data.get("field_insights")

        if not final_insights:
            return {"success": False, "message": "Could not get field insights to generate dashboard."}

        # Call the canonical generator
        return generate_smart_dashboard_layout(layer_name, field_insights=final_insights)

    except Exception as e:
        return {"success": False, "message": str(e)}


def mission_get_layout() -> Dict:
    """Mission: Get the current dashboard layout."""
    try:
        data = _load_dashboard()
        return {"success": True, "message": "Layout retrieved.", "data": data.get("layout", {})}
    except Exception as e:
        return {"success": False, "message": str(e)}


def mission_get_charts() -> Dict:
    """Mission: Get the current dashboard charts."""
    try:
        data = _load_dashboard()
        return {"success": True, "message": "Charts retrieved.", "data": data.get("charts", [])}
    except Exception as e:
        return {"success": False, "message": str(e)}


def mission_get_field_info(field_name: str = None) -> Dict:
    """Mission: Get information about fields in the dashboard."""
    try:
        data = _load_dashboard()
        insights = data.get("field_insights", {})
        if field_name:
            if field_name in insights:
                return {"success": True, "message": f"Info for field '{field_name}' retrieved.", "data": insights[field_name]}
            else:
                return {"success": False, "message": f"Field '{field_name}' not found in dashboard."}
        return {"success": True, "message": "All field info retrieved.", "data": insights}
    except Exception as e:
        return {"success": False, "message": str(e)}


def mission_update_charts(charts_data: List[Dict]) -> Dict:
    """
    Mission: Update existing charts in the dashboard.
    Payload should be a list of dictionaries, each with 'index', 'fields', and 'chart_type'.
    """
    try:
        dashboard = _load_dashboard()
        existing_charts = dashboard.get("charts", [])
        updated_count = 0

        for chart_update in charts_data:
            index = chart_update.get("index")
            if index is not None and 0 <= index < len(existing_charts):
                # Simple update: replace the chart at the given index
                existing_charts[index].update(chart_update)
                updated_count += 1

        dashboard["charts"] = existing_charts
        if _save_dashboard(dashboard):
            return {"success": True, "message": f"Successfully updated {updated_count} charts.", "data": {"updated_count": updated_count}}
        else:
            return {"success": False, "message": "Failed to save updated dashboard."}

    except Exception as e:
        return {"success": False, "message": str(e)}


def mission_add_charts(new_charts: List[Dict]) -> Dict:
    """
    Mission: Add new charts to the dashboard.
    Payload should be a list of chart dictionaries.
    """
    try:
        dashboard = _load_dashboard()

        for new_chart in new_charts:
            # Basic validation
            if "fields" in new_chart and "chart_type" in new_chart:
                # Assign a new ID
                new_id = f"chart_new_{len(dashboard.get('charts', [])) + 1}"
                chart_to_add = {
                    "id": new_id,
                    "field_name": new_chart.get("fields")[0],
                    "title": f"Analysis of {new_chart.get('fields')[0]}",
                    **new_chart
                }
                dashboard.setdefault("charts", []).append(chart_to_add)

        # Naive layout update: just append to items
        # A more sophisticated implementation would recalculate the grid.
        for chart in dashboard.get("charts", []):
            if not any(item['id'] == chart['id'] for item in dashboard['layout'].get('items',[])):
                 dashboard['layout'].setdefault('items', []).append({
                    "id": chart['id'],
                    "chart_type": chart['chart_type'],
                    "field_name": chart['field_name'],
                    "grid_area": f"chart-{len(dashboard['layout']['items']) + 1}"
                 })


        if _save_dashboard(dashboard):
            return {"success": True, "message": f"Successfully added {len(new_charts)} new charts.", "data": {"added_count": len(new_charts)}}
        else:
            return {"success": False, "message": "Failed to save dashboard with new charts."}

    except Exception as e:
        return {"success": False, "message": str(e)}
