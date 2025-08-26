import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.dashboard_api import (
    mission_generate_dashboard,
    mission_get_layout,
    mission_get_charts,
    mission_update_charts,
    mission_add_charts,
    mission_delete_charts,
    mission_update_layout,
    DASHBOARD_FILE
)

def cleanup():
    """Remove the dashboard file if it exists."""
    if os.path.exists(DASHBOARD_FILE):
        os.remove(DASHBOARD_FILE)
    print(f"Cleaned up {DASHBOARD_FILE}.")

def run_tests():
    """Runs a series of smoke tests for the dashboard API."""
    print("--- Running Dashboard API Smoke Tests ---")

    # Test 1: Generate dashboard with smart default
    print("\n[Test 1] Generate dashboard")
    cleanup()
    result = mission_generate_dashboard("parcels")
    assert result.get("success") and result.get("is_dashboard_update"), "Test 1 Failed: Dashboard generation failed or missing refresh flag."
    print("Test 1 Passed.")

    # Test 2: Add a multi-field chart (to test data model fix)
    print("\n[Test 2] Add multi-field chart")
    multi_field_chart = {
        "field_name": ["sales_2022", "sales_2023"], # Pass list to simulate agent
        "chart_type": "bar",
        "category_field": "operator",
        "title": "Sales by Operator"
    }
    result = mission_add_charts([multi_field_chart])
    assert result.get("success") and result.get("is_dashboard_update"), "Test 2 Failed: Adding multi-field chart failed."
    charts = mission_get_charts()['data']
    last_chart = charts[-1]
    assert last_chart['field_name'] == 'sales_2022', "Test 2 Failed: `field_name` was not correctly set to the first item in the list."
    assert last_chart['fields'] == ["sales_2022", "sales_2023"], "Test 2 Failed: `fields` array was not correctly preserved."
    print("Test 2 Passed: Multi-field chart added correctly.")

    # Test 3: Update layout (columns)
    print("\n[Test 3] Update overall layout")
    layout_update = {"grid_template_columns": "repeat(4, 1fr)"}
    result = mission_update_layout(layout_update)
    assert result.get("success") and result.get("is_dashboard_update"), "Test 3 Failed: Layout update failed."
    layout = mission_get_layout()['data']
    assert layout['grid_template_columns'] == "repeat(4, 1fr)", f"Test 3 Failed: Grid columns not updated. Got {layout['grid_template_columns']}"
    print("Test 3 Passed: Grid columns updated.")

    # Test 4: Update layout (individual item span)
    print("\n[Test 4] Update individual item layout")
    item_layout_update = {
        "items": [
            {"index": 0, "grid_area": "1 / 1 / 2 / 3"} # Make first chart span 2 columns
        ]
    }
    result = mission_update_layout(item_layout_update)
    assert result.get("success") and result.get("is_dashboard_update"), "Test 4 Failed: Item layout update failed."
    layout = mission_get_layout()['data']
    assert layout['items'][0]['grid_area'] == "1 / 1 / 2 / 3", "Test 4 Failed: Item grid_area not updated."
    print("Test 4 Passed: Individual chart layout updated.")

    # Test 5: Verify responsive layout logic from _rebuild_layout
    print("\n[Test 5] Verify responsive layout logic")
    cleanup()
    mission_add_charts([{"fields": ["F1"], "chart_type": "bar"}]) # 1 chart
    layout = mission_get_layout()['data']
    assert layout['grid_template_columns'] == '1fr', "Test 5.1 Failed: 1 chart should be 1 column."
    mission_add_charts([{"fields": ["F2"], "chart_type": "bar"}, {"fields": ["F3"], "chart_type": "bar"}]) # 3 charts
    layout = mission_get_layout()['data']
    assert layout['grid_template_columns'] == '1fr 1fr', "Test 5.2 Failed: 3 charts should be 2 columns."
    mission_add_charts([{"fields": ["F4"], "chart_type": "bar"}, {"fields": ["F5"], "chart_type": "bar"}]) # 5 charts
    layout = mission_get_layout()['data']
    assert layout['grid_template_columns'] == '1fr 1fr 1fr', "Test 5.3 Failed: 5 charts should be 3 columns."
    mission_delete_charts(indices=[0, 1, 2, 3]) # 1 chart left
    layout = mission_get_layout()['data']
    assert layout['grid_template_columns'] == '1fr', "Test 5.4 Failed: 1 chart should be 1 column after deletion."
    print("Test 5 Passed: Layout logic is responsive.")

    print("\n--- All smoke tests passed successfully! ---")
    cleanup()

if __name__ == "__main__":
    run_tests()
