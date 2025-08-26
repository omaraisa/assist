import sys
import os
import json

# Add the parent directory to the Python path to allow importing from 'app'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.dashboard_api import (
    mission_generate_dashboard,
    mission_get_layout,
    mission_get_charts,
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

    # Test 1: Generate dashboard with smart default
    print("\n[Test 1] Generate dashboard with smart default (source=None)")
    cleanup()
    result = mission_generate_dashboard("parcels", source=None)
    assert result.get("success"), f"Test 1 Failed: {result.get('message')}"
    assert result.get("is_dashboard_update"), "Test 1 Failed: is_dashboard_update flag missing."
    assert result.get("chart_count") > 0, "Test 1 Failed: No charts were generated."
    print("Test 1 Passed: Dashboard generated and refresh flag is present.")

    # Test 2: Get layout and charts
    print("\n[Test 2] Get dashboard layout and charts")
    layout_result = mission_get_layout()
    charts_result = mission_get_charts()
    assert layout_result.get("success"), f"Test 2 Failed: Could not get layout."
    assert charts_result.get("success"), f"Test 2 Failed: Could not get charts."
    initial_chart_count = len(charts_result.get("data", []))
    assert initial_chart_count == 6, f"Test 2 Failed: Expected 6 charts, got {initial_chart_count}."
    print(f"Test 2 Passed: Retrieved layout and {initial_chart_count} charts.")

    # Test 3: Add new charts
    print("\n[Test 3] Add new charts")
    new_chart_data = [{"fields": ["NewField1"], "chart_type": "pie"}]
    result = mission_add_charts(new_chart_data)
    assert result.get("success"), f"Test 3 Failed: {result.get('message')}"
    assert result.get("is_dashboard_update"), "Test 3 Failed: is_dashboard_update flag missing."
    charts_result = mission_get_charts()
    assert len(charts_result.get("data", [])) == initial_chart_count + 1, "Test 3 Failed: Chart count did not increase."
    print("Test 3 Passed: New chart added and refresh flag is present.")

    # Test 4: Update a chart
    print("\n[Test 4] Update a chart with full replacement")
    update_payload = {
        "index": 0,
        "chart": {"id": "completely_new_chart", "field_name": "UpdatedField", "chart_type": "donut", "title": "Updated Chart"}
    }
    result = mission_update_charts([update_payload])
    assert result.get("success"), f"Test 4 Failed: {result.get('message')}"
    assert result.get("is_dashboard_update"), "Test 4 Failed: is_dashboard_update flag missing."
    charts_result = mission_get_charts()
    assert charts_result.get("data")[0].get("id") == "completely_new_chart", "Test 4 Failed: Chart was not fully replaced."
    print("Test 4 Passed: Chart fully replaced and refresh flag is present.")

    # Test 5: Delete charts
    print("\n[Test 5] Delete charts")
    charts_before_delete = mission_get_charts().get("data", [])
    count_before_delete = len(charts_before_delete)
    indices_to_delete = [0, count_before_delete - 1]
    result = mission_delete_charts(indices=indices_to_delete)
    assert result.get("success"), f"Test 5 Failed: {result.get('message')}"
    assert result.get("is_dashboard_update"), "Test 5 Failed: is_dashboard_update flag missing."
    charts_after_delete = mission_get_charts().get("data", [])
    assert len(charts_after_delete) == count_before_delete - 2, "Test 5 Failed: Chart count is incorrect after deleting."
    print("Test 5 Passed: Charts deleted and refresh flag is present.")

    # Test 6: Verify Layout Logic
    print("\n[Test 6] Verify layout logic changes")
    cleanup()
    # 1 chart -> 1 column
    mission_add_charts([{"fields": ["F1"], "chart_type": "bar"}])
    layout = mission_get_layout()['data']
    assert layout['grid_template_columns'] == '1fr', f"Test 6.1 Failed: Expected 1fr, got {layout['grid_template_columns']}"
    print("  - Passed: 1 chart -> 1 column")
    # 3 charts -> 2 columns
    mission_add_charts([{"fields": ["F2"], "chart_type": "bar"}, {"fields": ["F3"], "chart_type": "bar"}])
    layout = mission_get_layout()['data']
    assert layout['grid_template_columns'] == '1fr 1fr', f"Test 6.2 Failed: Expected 1fr 1fr, got {layout['grid_template_columns']}"
    print("  - Passed: 3 charts -> 2 columns")
    # 5 charts -> 3 columns
    mission_add_charts([{"fields": ["F4"], "chart_type": "bar"}, {"fields": ["F5"], "chart_type": "bar"}])
    layout = mission_get_layout()['data']
    assert layout['grid_template_columns'] == '1fr 1fr 1fr', f"Test 6.3 Failed: Expected 1fr 1fr 1fr, got {layout['grid_template_columns']}"
    print("  - Passed: 5 charts -> 3 columns")
    # Delete back to 4 charts -> 2 columns
    mission_delete_charts([0])
    layout = mission_get_layout()['data']
    assert layout['grid_template_columns'] == '1fr 1fr', f"Test 6.4 Failed: Expected 1fr 1fr, got {layout['grid_template_columns']}"
    print("  - Passed: 4 charts -> 2 columns")
    print("Test 6 Passed: Layout logic is responsive.")

    print("\n--- All smoke tests passed successfully! ---")
    cleanup()

if __name__ == "__main__":
    run_tests()
