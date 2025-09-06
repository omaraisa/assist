import json
import os
from datetime import datetime
from typing import Dict, List
from .ai.function_declarations import FunctionDeclaration

# Build AVAILABLE_FUNCTIONS dynamically from the authoritative declarations
# The numeric IDs are assigned deterministically based on the declaration order.

AVAILABLE_FUNCTIONS = {}

# Let the dynamic loading below handle all function assignments

try:
	decls = FunctionDeclaration.functions_declarations

	pass
except Exception:
	AVAILABLE_FUNCTIONS = {}

def format_available_functions() -> str:
	"""Return a compact single-line listing like '1: name, 2: name'"""
	parts = [f"{k}: {v}" for k, v in sorted(AVAILABLE_FUNCTIONS.items())]
	return ", ".join(parts)





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
def generate_dashboard_for_target_layer(layer_name: str, analysis_type: str = "overview", theme: str = "default", field_insights: Dict = None) -> Dict:
    """Generate smart dashboard layout using field insights with enhanced filtering"""
    try:
        if not field_insights:
            return {"success": False, "error": "Field insights are required for dashboard generation"}
        
        # Enhanced field categorization and filtering
        textual_fields = []
        numerical_fields = []
        excluded_fields = []

        for field_name, field_info in field_insights.items():
            data_category = field_info.get("data_category", "")
            unique_count = field_info.get("unique_count", 0)
            total_records = field_info.get("total_records", 1)
            field_name_lower = field_name.lower()

            # Skip system fields and problematic fields
            if any(skip_field in field_name_lower for skip_field in [
                'objectid', 'shape', 'globalid', 'fid', 'oid', 'geometry'
            ]):
                excluded_fields.append(field_info)
                continue

            # Skip coordinate-like fields and ID-like fields
            if data_category in ["continuous_numeric", "categorical_numeric"]:
                uniqueness_ratio = unique_count / total_records if total_records > 0 else 0
                field_type = field_info.get("field_type", "").lower()
                is_constant = unique_count == 1
                is_all_unique = unique_count == total_records
                is_high_unique = uniqueness_ratio > 0.9
                is_coordinate_name = any(coord in field_name_lower for coord in ['lat', 'lon', 'x', 'y', 'coord', 'longitude', 'latitude'])
                if is_constant or is_all_unique or is_high_unique or is_coordinate_name:
                    excluded_fields.append(field_info)
                    continue
                else:
                    numerical_fields.append(field_info)

            # Include good textual fields
            elif data_category in ["categorical_text", "text", "name_field"]:
                uniqueness_ratio = unique_count / total_records if total_records > 0 else 0
                is_all_unique = unique_count == total_records
                is_high_unique = uniqueness_ratio > 0.9
                if is_all_unique or is_high_unique:
                    excluded_fields.append(field_info)
                    continue
                else:
                    textual_fields.append(field_info)

        # Sort fields by quality (unique count for textual, visualization priority for numerical)
        textual_fields.sort(key=lambda x: x.get("unique_count", 0), reverse=True)
        numerical_fields.sort(key=lambda x: x.get("visualization_priority", 0), reverse=True)

        # Combine good fields for dashboard
        good_fields = textual_fields + numerical_fields
        print(f"DEBUG: Found {len(textual_fields)} textual fields, {len(numerical_fields)} numerical fields")
        print(f"DEBUG: Excluded {len(excluded_fields)} unsuitable fields")
        print(f"DEBUG: Total good fields for dashboard: {len(good_fields)}")

        # Select top fields for the dashboard (limit to 6)
        top_fields = good_fields[:6]
        print(f"DEBUG: Selected top {len(top_fields)} fields for dashboard")
        
        # Generate chart configurations for each selected field
        charts = []
        print(f"DEBUG: Processing {len(top_fields)} fields for charts")
        for i, field_info in enumerate(top_fields):
            field_name = field_info.get('field_name', 'unknown')
            print(f"DEBUG: Processing field {i+1}: {field_name}")
            chart_config = _create_chart_from_field(field_info, theme)
            if chart_config:
                charts.append(chart_config)
                print(f"DEBUG: Added chart config for field {field_name}")
            else:
                print(f"DEBUG: No chart config created for field {field_name}")
        
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
        
        # Save to progent_dashboard.json (adjacent to this module)
        dashboard_path = os.path.join(os.path.dirname(__file__), '..', 'progent_dashboard.json')
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
        dashboard_path = os.path.join(os.path.dirname(__file__), '..', 'progent_dashboard.json')
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
        dashboard_path = os.path.join(os.path.dirname(__file__), '..', 'progent_dashboard.json')
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
        dashboard_path = os.path.join(os.path.dirname(__file__), '..', 'progent_dashboard.json')
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
    """Update specific dashboard charts by index in progent_dashboard.json"""
    try:
        dashboard_path = os.path.join(os.path.dirname(__file__), '..', 'progent_dashboard.json')
        if not os.path.exists(dashboard_path):
            return {"success": False, "error": "Dashboard file not found"}
        
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "charts" not in data:
            data["charts"] = []
        if "layout" not in data:
            data["layout"] = {"grid_template_columns": "1fr 1fr", "gap": "20px", "items": []}
        if "items" not in data["layout"]:
            data["layout"]["items"] = []
        
        updated_count = 0
        
        # Update specific charts by index
        for chart_update in charts_data:
            index = chart_update.get("index")
            chart = chart_update.get("chart")
            
            if index is None or chart is None:
                continue
                
            # Validate index
            if not isinstance(index, int) or index < 0 or index >= len(data["charts"]):
                continue
            
            # Update the chart at the specified index
            fields = chart.get("fields", [])
            chart_type = chart.get("chart_type", "bar")
            category_field = chart.get("category_field")
            series = chart.get("series", [])
            title = chart.get("title")
            theme = chart.get("theme", data.get("theme", "default"))
            
            if fields:
                # If category_field is not specified, use the first field as category
                if not category_field:
                    category_field = fields[0]
                    series_fields = fields[1:] if len(fields) > 1 else []
                else:
                    # If category_field is specified, remove it from series_fields if it's in fields
                    series_fields = [f for f in fields if f != category_field]
                
                # If series is provided, use it instead of deriving from fields
                if series:
                    series_fields = [s.get("field") for s in series]
                
                # Update the chart
                chart_config = {
                    "id": f"chart_{category_field}_{'_'.join(series_fields) if series_fields else ''}",
                    "field_name": category_field,
                    "chart_type": chart_type,
                    "title": title or f"Analysis of {category_field}",
                    "theme": theme
                }
                
                # Add multi-field support for grouped charts
                if series_fields and chart_type in ["grouped_bar", "bar", "column"]:
                    chart_config["category_field"] = category_field
                    chart_config["series"] = [
                        {"field": field, "name": field, "aggregation": "sum"} for field in series_fields
                    ]
                    chart_config["fields"] = [category_field] + series_fields  # Store all fields with category first
                    chart_config["aggregation"] = "sum"  # Specify aggregation type
                
                data["charts"][index] = chart_config
                
                # Update corresponding layout item
                if index < len(data["layout"]["items"]):
                    layout_item = {
                        "id": chart_config["id"],
                        "chart_type": chart_type,
                        "field_name": category_field,
                        "grid_area": f"chart-{index+1}"
                    }
                    
                    # Add fields to layout item for multi-field charts
                    if series_fields:
                        layout_item["fields"] = [category_field] + series_fields
                    
                    data["layout"]["items"][index] = layout_item
                
                updated_count += 1
        
        data["generation_timestamp"] = _get_timestamp()
        
        # Save updated data
        with open(dashboard_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        return {
            "success": True,
            "message": f"Updated {updated_count} charts in dashboard"
        }
        
    except Exception as e:
        return {"success": False, "error": str(e)}


def delete_charts_from_dashboard(indices: list) -> dict:
    """Delete charts from dashboard by their indices"""
    try:
        dashboard_path = "./Progent/progent_dashboard.json"
        
        if not os.path.exists(dashboard_path):
            return {"success": False, "error": "Dashboard file not found"}
            
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "charts" not in data:
            return {"success": False, "error": "No charts found in dashboard"}
        
        # Sort indices in descending order to delete from end first
        # This prevents index shifting issues
        sorted_indices = sorted(indices, reverse=True)
        
        deleted_count = 0
        original_count = len(data["charts"])
        
        for index in sorted_indices:
            if 0 <= index < len(data["charts"]):
                del data["charts"][index]
                deleted_count += 1
            else:
                return {"success": False, "error": f"Index {index} is out of range (0-{original_count-1})"}
        
        # Update layout items if they exist
        if "layout" in data and "items" in data["layout"]:
            # Remove corresponding layout items
            sorted_indices = sorted(indices, reverse=True)
            for index in sorted_indices:
                if 0 <= index < len(data["layout"]["items"]):
                    del data["layout"]["items"][index]
        
        # Update timestamp
        data["generation_timestamp"] = _get_timestamp()
        
        # Save updated data
        with open(dashboard_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        return {
            "success": True,
            "message": f"Deleted {deleted_count} charts from dashboard",
            "remaining_charts": len(data["charts"])
        }
        
    except Exception as e:
        return {"success": False, "error": str(e)}


def update_dashboard_layout(layout_updates: dict) -> dict:
    """Update dashboard layout configuration"""
    try:
        dashboard_path = "./Progent/progent_dashboard.json"

        if not os.path.exists(dashboard_path):
            return {"success": False, "error": "Dashboard file not found"}

        with open(dashboard_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if "layout" not in data:
            data["layout"] = {"grid_template_columns": "1fr 1fr 1fr", "gap": "20px", "items": []}

        # Update grid template columns if provided
        if "grid_template_columns" in layout_updates:
            data["layout"]["grid_template_columns"] = layout_updates["grid_template_columns"]

        # Update specific chart items if provided
        if "items" in layout_updates:
            # Create a mapping of current items by ID for easy lookup
            current_items = {item["id"]: item for item in data["layout"]["items"]}
            current_charts = {chart["id"]: chart for chart in data.get("charts", [])}

            # Update items based on the new order provided
            updated_items = []
            updated_charts = []
            for i, item_update in enumerate(layout_updates["items"]):
                item_id = item_update.get("id")
                if item_id and item_id in current_items:
                    # Copy the existing item and update its grid_area
                    updated_item = current_items[item_id].copy()
                    if "grid_area" in item_update:
                        updated_item["grid_area"] = item_update["grid_area"]
                    updated_items.append(updated_item)

                    # Also reorder the corresponding chart
                    if item_id in current_charts:
                        updated_charts.append(current_charts[item_id])

            # Replace the layout items and charts with the updated order
            if updated_items:
                data["layout"]["items"] = updated_items
                data["charts"] = updated_charts

        # Update timestamp
        data["generation_timestamp"] = _get_timestamp()

        # Save updated data
        with open(dashboard_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        return {
            "success": True,
            "message": "Dashboard layout updated successfully"
        }

    except Exception as e:
        return {"success": False, "error": str(e)}

