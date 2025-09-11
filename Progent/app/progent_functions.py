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


def reindex_last_chart_to_position(target_position: int) -> Dict:
    """Simple reindexing: Cut the last chart and paste it at target position"""
    try:
        dashboard_path = os.path.join(os.path.dirname(__file__), '..', 'progent_dashboard.json')
        if not os.path.exists(dashboard_path):
            return {"success": False, "error": "Dashboard file not found"}
        
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "charts" not in data or len(data["charts"]) == 0:
            return {"success": False, "error": "No charts found in dashboard"}
        
        charts = data["charts"]
        layout_items = data.get("layout", {}).get("items", [])
        
        # Validate target position
        if target_position < 0 or target_position >= len(charts):
            return {"success": False, "error": f"Target position {target_position} is out of range"}
        
        # If already at target position, nothing to do
        if target_position == len(charts) - 1:
            return {"success": True, "message": "Chart already at target position"}
        
        # Step 1: Cut the last chart and its layout item
        last_chart = charts.pop()  # Remove from end
        last_layout_item = None
        if len(layout_items) > 0:
            last_layout_item = layout_items.pop()  # Remove from end
        
        # Step 2: Paste at target position (this shifts everything else to the right)
        charts.insert(target_position, last_chart)
        if last_layout_item and len(layout_items) >= target_position:
            layout_items.insert(target_position, last_layout_item)
        
        # Step 3: Update timestamp and save
        data["generation_timestamp"] = _get_timestamp()
        
        with open(dashboard_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        return {
            "success": True,
            "message": f"Reindexed chart to position {target_position}",
            "is_dashboard_update": True
        }
        
    except Exception as e:
        return {"success": False, "error": str(e)}


def move_last_chart_to_position(target_position: int) -> Dict:
    """Move the last chart in the dashboard to the specified position (legacy function)"""
    return reindex_last_chart_to_position(target_position)


def get_current_dashboard_layout() -> Dict:
    """Get current dashboard layout from progent_dashboard.json"""
    try:
        dashboard_path = os.path.join(os.path.dirname(__file__), '..', 'progent_dashboard.json')
        if not os.path.exists(dashboard_path):
            return {"success": False, "error": "Dashboard file not found"}
        
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        charts = data.get("charts", [])
        chart_summary = []
        for i, chart in enumerate(charts):
            chart_summary.append(f"[{i}] {chart.get('title', 'Untitled')} ({chart.get('chart_type', 'unknown')})")
        
        return {
            "success": True,
            "grid_columns": data.get("layout", {}).get("grid_template_columns", "1fr 1fr 1fr"),
            "charts": chart_summary
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


def get_dashboard_field_detailed_description() -> Dict:
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
    """
    Simple proxy function: Delete chart, then add new chart.
    """
    try:
        dashboard_path = os.path.join(os.path.dirname(__file__), '..', 'progent_dashboard.json')
        if not os.path.exists(dashboard_path):
            return {"success": False, "error": "Dashboard file not found"}

        with open(dashboard_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if "charts" not in data:
            return {"success": False, "error": "No charts found in dashboard"}

        # Only handle the first chart update for simplicity
        if not charts_data:
            return {"success": False, "error": "No chart data provided"}

        chart_update = charts_data[0]
        index = chart_update.get("index")
        chart = chart_update.get("chart")

        if index is None or chart is None:
            return {"success": False, "error": "Chart update missing 'index' or 'chart' field"}

        # Validate index
        if not isinstance(index, int) or index < 0 or index >= len(data["charts"]):
            return {"success": False, "error": f"Index {index} is out of range (0-{len(data['charts'])-1})"}

        # Step 1: Delete the chart at the specified index
        delete_result = delete_charts_from_dashboard([index])
        if not delete_result.get("success"):
            return {"success": False, "error": f"Failed to delete chart: {delete_result.get('error')}"}

        # Step 2: Prepare parameters for add_chart_to_dashboard
        add_params = {
            "layer_name": data.get("layer_name", "Unknown Layer"),
            "chart_type": chart.get("chart_type", "bar"),
            "fields": chart.get("fields", []),
            "title": chart.get("title", "Updated Chart"),
            "theme": chart.get("theme", "default")
        }

        # Handle field configuration properly
        fields = chart.get("fields", [])
        if len(fields) >= 2:
            # If multiple fields, first is category, second is value field
            add_params["category_field"] = fields[0]
            add_params["fields"] = [fields[1]]  # Main field for aggregation
            add_params["aggregation"] = chart.get("aggregation", "sum")
        elif len(fields) == 1:
            # Single field - use as main field
            add_params["fields"] = fields
            if chart.get("category_field"):
                add_params["category_field"] = chart.get("category_field")
                add_params["aggregation"] = chart.get("aggregation", "sum")

        # Add optional parameters
        if chart.get("where_clause"):
            add_params["where_clause"] = chart.get("where_clause")

        # Return parameters for websocket call to add_chart_to_dashboard + reindex info
        return {
            "success": True,
            "message": f"Chart at index {index} deleted. Ready to add new chart and reindex.",
            "charts_to_add": [add_params],
            "original_index": index,  # Store the original index for reindexing
            "requires_websocket_calls": True,
            "requires_reindexing": True,
            "is_dashboard_update": False  # Will be true after websocket calls complete
        }

    except Exception as e:
        return {"success": False, "error": str(e)}


def delete_charts_from_dashboard(indices: list) -> dict:
    """Delete charts from dashboard by their indices"""
    try:
        dashboard_path = os.path.join(os.path.dirname(__file__), '..', 'progent_dashboard.json')
        
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
            "remaining_charts": len(data["charts"]),
            "is_dashboard_update": True
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
            "message": "Dashboard layout updated successfully",
            "is_dashboard_update": True
        }

    except Exception as e:
        return {"success": False, "error": str(e)}

