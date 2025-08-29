import json
import os
from datetime import datetime
from typing import Dict, List, Any
from pathlib import Path

# Get the directory of this file (Progent directory)
BASE_DIR = Path(__file__).parent.parent
DASHBOARD_FILE = BASE_DIR / "progent_dashboard.json"

def _get_timestamp() -> str:
    """Get current timestamp in ISO format"""
    return datetime.now().isoformat()

def _load_dashboard() -> Dict:
    """
    Safely loads the dashboard file.
    Returns dashboard data or empty structure if file doesn't exist.
    """
    if not os.path.exists(DASHBOARD_FILE):
        return {
            "layer_name": None,
            "dashboard_title": "No Dashboard",
            "theme": "default",
            "charts": [],
            "layout": {"grid_template_columns": "1fr", "gap": "20px", "items": []},
            "field_insights": {},
            "generation_timestamp": _get_timestamp()
        }
    
    try:
        with open(DASHBOARD_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading dashboard file: {e}")
        return {
            "layer_name": None,
            "dashboard_title": "Error Loading Dashboard",
            "theme": "default", 
            "charts": [],
            "layout": {"grid_template_columns": "1fr", "gap": "20px", "items": []},
            "field_insights": {},
            "error": str(e)
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
    """
    Fetch fields from a GIS layer.
    Gets real data from the dashboard JSON (sent from ArcGIS Pro).
    Returns empty list if no data is available for the specified layer.
    """
    # Try to get real field data from dashboard JSON first
    dashboard_data = _load_dashboard()
    current_layer = dashboard_data.get("layer_name")
    
    # Check if we have data for the requested layer
    if dashboard_data.get("field_insights") and current_layer == layer_name:
        fields = []
        for field_name, insights in dashboard_data["field_insights"].items():
            # Reconstruct field info from insights
            data_category = insights.get("data_category", "unknown")
            if data_category in ["continuous_numeric", "categorical_numeric"]:
                field_type = "numeric"
            elif data_category in ["categorical_text", "categorical_codes", "name_field"]:
                field_type = "categorical"
            elif data_category == "date":
                field_type = "date"
            else:
                field_type = "categorical"  # default

            field_info = {
                "field_name": field_name,
                "type": field_type,
                "sample_values": insights.get("sample_values", [])
            }
            fields.append(field_info)

        if fields:
            print(f"Using real field data from dashboard JSON for layer: {layer_name}")
            return fields
    
    # No data available for this layer
    print(f"No field data available for layer: {layer_name} (current data is for: {current_layer})")
    return []

def _prepare_field_insights_from_layer(fields: List[Dict]) -> Dict:
    """Enhanced adapter to create field_insights using AI-powered analysis."""
    insights = {}
    for field in fields:
        field_name = field.get("field_name")

        # Analyze field data to get detailed statistics
        field_analysis = _analyze_field_data(field)

        # Generate AI insights using the powerful analysis function
        ai_insights = _generate_ai_insights(field_analysis, field_name)

        insights[field_name] = ai_insights

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

def _analyze_field_data(field: Dict) -> Dict:
    """Analyze field data to extract detailed statistics for AI insights generation."""
    field_name = field.get("field_name", "")
    field_type = field.get("type", "unknown")
    sample_values = field.get("sample_values", [])

    if not sample_values:
        return {
            "data_category": "unknown",
            "unique_count": 0,
            "total_records": 0,
            "null_percentage": 100.0
        }

    total_records = len(sample_values)
    unique_values = list(set(sample_values))
    unique_count = len(unique_values)
    null_count = sum(1 for v in sample_values if v is None or str(v).lower() in ['null', 'none', ''])
    null_percentage = (null_count / total_records) * 100 if total_records > 0 else 0

    analysis = {
        "data_category": "unknown",
        "unique_count": unique_count,
        "total_records": total_records,
        "null_percentage": null_percentage,
        "sample_values": sample_values  # Keep all samples from ArcGIS Pro
    }

    if field_type == "numeric":
        try:
            numeric_values = [float(v) for v in sample_values if v is not None and str(v).lower() not in ['null', 'none', '']]
            if numeric_values:
                analysis["data_category"] = "continuous_numeric"
                analysis["min_value"] = min(numeric_values)
                analysis["max_value"] = max(numeric_values)
                analysis["average_value"] = sum(numeric_values) / len(numeric_values)

                # Check if it's actually categorical numeric (few unique values)
                if unique_count <= 10:
                    analysis["data_category"] = "categorical_numeric"
        except (ValueError, TypeError):
            analysis["data_category"] = "categorical_text"

    elif field_type == "categorical":
        analysis["data_category"] = "categorical_text"

    elif field_type == "date":
        analysis["data_category"] = "date"
        try:
            from datetime import datetime
            date_values = []
            for v in sample_values:
                if v and str(v).lower() not in ['null', 'none', '']:
                    try:
                        if isinstance(v, str):
                            date_values.append(datetime.fromisoformat(v.replace('Z', '+00:00')))
                        else:
                            date_values.append(v)
                    except:
                        continue

            if date_values:
                analysis["min_date"] = str(min(date_values))
                analysis["max_date"] = str(max(date_values))
        except:
            pass

    return analysis

def _generate_ai_insights(field_info: Dict, field_name: str) -> Dict:
    """
    Step 2 Enhancement: Generate AI-ready insights for better chart selection
    Provides rich, descriptive analysis that enables intelligent chart recommendations
    """
    try:
        data_category = field_info.get("data_category", "unknown")
        unique_count = field_info.get("unique_count", 0)
        total_records = field_info.get("total_records", 1)
        null_percentage = field_info.get("null_percentage", 0)

        ai_insights = {
            "field_name": field_name,
            "data_category": data_category,
            "data_story": "",
            "visualization_potential": "low",
            "chart_suitability": {},
            "data_patterns": {},
            "analytical_value": "medium",
            "distribution_characteristics": "",
            "visualization_priority": 5,  # 1-10 scale
            "sample_values": field_info.get("sample_values", [])
        }

        # Generate data story based on field characteristics
        if data_category == "categorical_text":
            diversity_ratio = unique_count / total_records if total_records > 0 else 0

            if unique_count <= 5:
                ai_insights["data_story"] = f"'{field_name}' contains {unique_count} distinct categories with clear groupings, ideal for showing proportional relationships."
                ai_insights["visualization_potential"] = "high"
                ai_insights["visualization_priority"] = 9
                ai_insights["chart_suitability"] = {
                    "pie": 0.95, "donut": 0.90, "bar": 0.85, "column": 0.80
                }
            elif unique_count <= 15:
                ai_insights["data_story"] = f"'{field_name}' has {unique_count} categories, suitable for comparative analysis and ranking visualizations."
                ai_insights["visualization_potential"] = "high"
                ai_insights["visualization_priority"] = 8
                ai_insights["chart_suitability"] = {
                    "bar": 0.90, "column": 0.85, "horizontal_bar": 0.80, "pie": 0.70
                }
            elif unique_count <= 30:
                ai_insights["data_story"] = f"'{field_name}' contains {unique_count} categories, best visualized with scrollable or grouped displays."
                ai_insights["visualization_potential"] = "medium"
                ai_insights["visualization_priority"] = 6
                ai_insights["chart_suitability"] = {
                    "bar": 0.75, "treemap": 0.70, "grouped_bar": 0.65
                }
            else:
                ai_insights["data_story"] = f"'{field_name}' has high cardinality ({unique_count} categories), requiring aggregation or filtering for effective visualization."
                ai_insights["visualization_potential"] = "low"
                ai_insights["visualization_priority"] = 3
                ai_insights["chart_suitability"] = {
                    "word_cloud": 0.60, "top_n_bar": 0.55
                }

        elif data_category == "continuous_numeric":
            value_range = field_info.get("max_value", 0) - field_info.get("min_value", 0)
            avg_value = field_info.get("average_value", 0)
            min_val = field_info.get("min_value", 0)
            max_val = field_info.get("max_value", 0)

            # Analyze distribution characteristics
            if value_range > 0:
                cv = (value_range / 4) / avg_value if avg_value != 0 else 0  # Approximate coefficient of variation

                if cv < 0.3:
                    ai_insights["distribution_characteristics"] = "Low variability - values clustered around the mean"
                    ai_insights["data_story"] = f"'{field_name}' shows consistent values (range: {min_val:.2f} to {max_val:.2f}), good for trend analysis."
                elif cv < 1.0:
                    ai_insights["distribution_characteristics"] = "Moderate variability - normal distribution likely"
                    ai_insights["data_story"] = f"'{field_name}' displays moderate variation (range: {min_val:.2f} to {max_val:.2f}), suitable for distribution analysis."
                else:
                    ai_insights["distribution_characteristics"] = "High variability - potential outliers present"
                    ai_insights["data_story"] = f"'{field_name}' shows high variation (range: {min_val:.2f} to {max_val:.2f}), may contain outliers worth investigating."
            else:
                ai_insights["data_story"] = f"'{field_name}' contains constant or near-constant values, limited visualization value."

            ai_insights["visualization_potential"] = "high" if value_range > 0 else "low"
            ai_insights["visualization_priority"] = 8 if value_range > 0 else 2
            ai_insights["chart_suitability"] = {
                "histogram": 0.90, "box_plot": 0.85, "density_plot": 0.80, "violin_plot": 0.75
            } if value_range > 0 else {"summary_stats": 0.30}

        elif data_category == "categorical_numeric":
            ai_insights["data_story"] = f"'{field_name}' represents discrete numeric categories ({unique_count} values), ideal for count-based visualizations."
            ai_insights["visualization_potential"] = "high"
            ai_insights["visualization_priority"] = 7
            ai_insights["chart_suitability"] = {
                "bar": 0.85, "column": 0.80, "pie": 0.75 if unique_count <= 8 else 0.50
            }

        elif data_category == "free_text":
            ai_insights["data_story"] = f"'{field_name}' contains free-form text with {unique_count} unique entries, suitable for text analysis."
            ai_insights["visualization_potential"] = "low"
            ai_insights["visualization_priority"] = 2
            ai_insights["chart_suitability"] = {
                "word_cloud": 0.60, "text_length_histogram": 0.40
            }

        elif data_category == "date":
            ai_insights["data_story"] = f"'{field_name}' contains temporal data spanning from {field_info.get('min_date', 'unknown')} to {field_info.get('max_date', 'unknown')}."
            ai_insights["visualization_potential"] = "high"
            ai_insights["visualization_priority"] = 8
            ai_insights["chart_suitability"] = {
                "timeline": 0.90, "line_chart": 0.85, "date_histogram": 0.80
            }

        # Add data quality insights
        if null_percentage > 50:
            ai_insights["data_story"] += f" Data quality concern: {null_percentage:.1f}% missing values."
            ai_insights["visualization_priority"] = max(1, ai_insights["visualization_priority"] - 3)
        elif null_percentage > 20:
            ai_insights["data_story"] += f" Note: {null_percentage:.1f}% missing values present."
            ai_insights["visualization_priority"] = max(1, ai_insights["visualization_priority"] - 1)

        # Determine analytical value
        if ai_insights["visualization_priority"] >= 8:
            ai_insights["analytical_value"] = "high"
        elif ai_insights["visualization_priority"] >= 5:
            ai_insights["analytical_value"] = "medium"

        return ai_insights

    except Exception as e:
        return {
            "field_name": field_name,
            "data_category": "unknown",
            "data_story": f"Analysis of {field_name}",
            "visualization_potential": "low",
            "chart_suitability": {"bar": 0.5},
            "analytical_value": "low",
            "visualization_priority": 1,
            "error": str(e)
        }

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
                if not fields:
                    return {"success": False, "message": f"No field data available for layer '{layer_name}'. Please ensure ArcGIS Pro has analyzed this layer and sent the data to the server."}
                final_insights = _prepare_field_insights_from_layer(fields)
            else: # source == "dashboard"
                final_insights = dashboard_data.get("field_insights")
                if not final_insights:
                    return {"success": False, "message": "No field insights available in current dashboard. Please generate a new dashboard from layer data first."}

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
            # Ensure field_name is a string, not a list, to prevent downstream errors.
            # The 'fields' key can hold the list for multi-field charts.
            if 'field_name' in new_chart_data and isinstance(new_chart_data['field_name'], list):
                new_chart_data['fields'] = new_chart_data['field_name']
                new_chart_data['field_name'] = new_chart_data['fields'][0]

            charts[index] = new_chart_data # Full replacement
            updated_count += 1

    dashboard["charts"] = charts
    dashboard["layout"] = _rebuild_layout(charts)
    if _save_dashboard(dashboard):
        return {"success": True, "is_dashboard_update": True, "message": f"Successfully updated {updated_count} charts.", "data": {"updated_count": updated_count}}
    return {"success": False, "message": "Failed to save updated dashboard."}

def mission_add_charts(new_charts: List[Dict], index: int = None) -> Dict:
    """
    Mission: Add or insert new charts into the dashboard.
    If index is provided, charts are inserted at that position. Otherwise, they are appended.
    """
    dashboard = _load_dashboard()
    charts = dashboard.get("charts", [])

    # Process new charts to ensure data model is correct
    processed_charts = []
    for i, new_chart in enumerate(new_charts):
        if 'field_name' in new_chart and isinstance(new_chart['field_name'], list):
            new_chart['fields'] = new_chart['field_name']
            new_chart['field_name'] = new_chart['fields'][0]

        if ("fields" in new_chart or "field_name" in new_chart) and "chart_type" in new_chart:
            if "field_name" in new_chart and "fields" not in new_chart:
                new_chart["fields"] = [new_chart["field_name"]]

            primary_field = new_chart.get("field_name", new_chart.get("fields")[0])

            chart_to_add = {
                "id": f"chart_new_{len(charts) + i}",
                "title": f"Analysis of {primary_field}",
                **new_chart,
                "field_name": primary_field,
            }
            processed_charts.append(chart_to_add)

    # Insert or append the new charts
    if index is not None and 0 <= index <= len(charts):
        charts[index:index] = processed_charts
    else:
        charts.extend(processed_charts)

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

def mission_update_layout(layout_updates: Dict) -> Dict:
    """
    Mission: Update the dashboard's overall layout properties or individual item layouts.
    """
    dashboard = _load_dashboard()

    if "grid_template_columns" in layout_updates:
        dashboard["layout"]["grid_template_columns"] = layout_updates["grid_template_columns"]

    if "items" in layout_updates and isinstance(layout_updates["items"], list):
        for item_update in layout_updates["items"]:
            index = item_update.get("index")
            if index is not None and 0 <= index < len(dashboard["layout"]["items"]):
                dashboard["layout"]["items"][index].update(item_update)

    if _save_dashboard(dashboard):
        return {"success": True, "is_dashboard_update": True, "message": "Dashboard layout updated successfully."}
    return {"success": False, "message": "Failed to save updated dashboard layout."}
