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
    mission_delete_charts,
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

    # Test 1: Generate dashboard with smart default (no file exists)
    print("\n[Test 1] Generate dashboard with smart default (source=None)")
    cleanup()
    result = mission_generate_dashboard("parcels", source=None)
    assert result.get("success"), f"Test 1 Failed: {result.get('message')}"
    assert result.get("chart_count") > 0, "Test 1 Failed: No charts were generated."
    print("Test 1 Passed: Dashboard generated using smart default.")

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
    initial_chart_count = len(result.get("data", []))
    assert initial_chart_count > 0, "Test 3 Failed: No charts found."
    print(f"Test 3 Passed: Retrieved {initial_chart_count} charts.")

    # Test 4: Add new charts
    print("\n[Test 4] Add new charts")
    new_chart_data = [{"fields": ["NewField1"], "chart_type": "pie"}]
    result = mission_add_charts(new_chart_data)
    assert result.get("success"), f"Test 4 Failed: {result.get('message')}"
    assert result.get("data", {}).get("added_count") == 1, "Test 4 Failed: Incorrect number of charts added."
    charts_result = mission_get_charts()
    assert len(charts_result.get("data", [])) == initial_chart_count + 1, "Test 4 Failed: Total chart count is incorrect after adding."
    print("Test 4 Passed: New chart added.")

    # Test 5: Update a chart (full replacement)
    print("\n[Test 5] Update a chart with full replacement")
    original_chart_id = charts_result.get("data")[0]['id']
    update_payload = {
        "index": 0,
        "chart": {"id": "completely_new_chart", "field_name": "UpdatedField", "chart_type": "donut", "title": "Updated Chart"}
    }
    result = mission_update_charts([update_payload])
    assert result.get("success"), f"Test 5 Failed: {result.get('message')}"
    charts_result = mission_get_charts()
    assert charts_result.get("data")[0].get("id") == "completely_new_chart", "Test 5 Failed: Chart ID was not replaced."
    assert charts_result.get("data")[0].get("chart_type") == "donut", "Test 5 Failed: Chart type was not updated."
    print("Test 5 Passed: Chart fully replaced.")

    # Test 6: Delete charts
    print("\n[Test 6] Delete charts")
    charts_before_delete = mission_get_charts().get("data", [])
    count_before_delete = len(charts_before_delete)
    # Delete the first and last chart
    indices_to_delete = [0, count_before_delete - 1]
    result = mission_delete_charts(indices=indices_to_delete)
    assert result.get("success"), f"Test 6 Failed: {result.get('message')}"
    assert result.get("data", {}).get("deleted_count") == 2, "Test 6 Failed: Incorrect number of charts deleted."
    charts_after_delete = mission_get_charts().get("data", [])
    assert len(charts_after_delete) == count_before_delete - 2, "Test 6 Failed: Chart count is incorrect after deleting."
    # Check that the deleted chart is gone
    assert charts_after_delete[0].get("id") != "completely_new_chart", "Test 6 Failed: Chart at index 0 was not deleted correctly."
    print("Test 6 Passed: Charts deleted successfully.")

    print("\n--- All smoke tests passed successfully! ---")
    cleanup()

if __name__ == "__main__":
    run_tests()
