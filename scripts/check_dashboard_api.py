import sys
import os
import json

# Add the parent directory to the Python path to allow importing from 'app'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.dashboard_api import (
    mission_generate_dashboard,
    mission_get_layout,
    mission_get_charts,
    mission_get_field_info,
    mission_update_charts,
    mission_add_charts,
    DASHBOARD_FILE
)

def cleanup():
    """Remove the dashboard file if it exists."""
    if os.path.exists(DASHBOARD_FILE):
        os.remove(DASHBOARD_FILE)
    print("Cleaned up dashboard file.")

def run_tests():
    """Runs a series of smoke tests for the dashboard API."""
    print("--- Running Dashboard API Smoke Tests ---")

    # Test 1: Generate dashboard from layer
    print("\n[Test 1] Generate dashboard from source: 'layer'")
    cleanup()
    result = mission_generate_dashboard("parcels", source="layer")
    assert result.get("success"), f"Test 1 Failed: {result.get('message')}"
    assert result.get("chart_count") > 0, "Test 1 Failed: No charts were generated."
    print("Test 1 Passed: Dashboard generated from layer.")

    # Test 2: Get layout
    print("\n[Test 2] Get dashboard layout")
    result = mission_get_layout()
    assert result.get("success"), f"Test 2 Failed: {result.get('message')}"
    assert "grid_template_columns" in result.get("data", {}), "Test 2 Failed: Layout is missing grid info."
    print("Test 2 Passed: Layout retrieved.")

    # Test 3: Get charts
    print("\n[Test 3] Get dashboard charts")
    result = mission_get_charts()
    assert result.get("success"), f"Test 3 Failed: {result.get('message')}"
    assert isinstance(result.get("data", []), list), "Test 3 Failed: Charts data is not a list."
    assert len(result.get("data", [])) > 0, "Test 3 Failed: No charts found."
    print("Test 3 Passed: Charts retrieved.")

    # Test 4: Get field info (all fields)
    print("\n[Test 4] Get all field info")
    result = mission_get_field_info()
    assert result.get("success"), f"Test 4 Failed: {result.get('message')}"
    assert isinstance(result.get("data", {}), dict), "Test 4 Failed: Field info is not a dict."
    assert "Acres" in result.get("data", {}), "Test 4 Failed: Expected field 'Acres' not found."
    print("Test 4 Passed: All field info retrieved.")

    # Test 5: Get field info (one field)
    print("\n[Test 5] Get single field info")
    result = mission_get_field_info("LandUse")
    assert result.get("success"), f"Test 5 Failed: {result.get('message')}"
    assert result.get("data", {}).get("field_name") == "LandUse", "Test 5 Failed: Incorrect field info returned."
    print("Test 5 Passed: Single field info retrieved.")

    # Test 6: Add new charts
    print("\n[Test 6] Add new charts")
    new_chart_data = [
        {"fields": ["NewField1"], "chart_type": "pie"},
        {"fields": ["NewField2", "Category"], "chart_type": "bar"}
    ]
    result = mission_add_charts(new_chart_data)
    assert result.get("success"), f"Test 6 Failed: {result.get('message')}"
    assert result.get("data", {}).get("added_count") == 2, "Test 6 Failed: Incorrect number of charts added."
    charts_result = mission_get_charts()
    assert len(charts_result.get("data", [])) == 6 + 2, "Test 6 Failed: Total chart count is incorrect after adding."
    print("Test 6 Passed: New charts added.")

    # Test 7: Update a chart
    print("\n[Test 7] Update a chart")
    update_data = [{"index": 0, "chart_type": "donut", "title": "Updated Acres Chart"}]
    result = mission_update_charts(update_data)
    assert result.get("success"), f"Test 7 Failed: {result.get('message')}"
    charts_result = mission_get_charts()
    assert charts_result.get("data", [])[0].get("chart_type") == "donut", "Test 7 Failed: Chart type was not updated."
    print("Test 7 Passed: Chart updated.")

    # Test 8: Generate dashboard from existing dashboard data
    print("\n[Test 8] Generate dashboard from source: 'dashboard'")
    # No cleanup here, we want to use the existing file
    result = mission_generate_dashboard("parcels", source="dashboard")
    assert result.get("success"), f"Test 8 Failed: {result.get('message')}"
    assert result.get("chart_count") > 0, "Test 8 Failed: No charts were generated from dashboard source."
    print("Test 8 Passed: Dashboard generated from existing dashboard data.")


    print("\n--- All smoke tests passed successfully! ---")
    cleanup()

if __name__ == "__main__":
    run_tests()
