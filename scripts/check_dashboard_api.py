import sys
import os
import json

# Add the app directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.dashboard_api import (
    mission_generate_dashboard,
    mission_get_layout,
    mission_get_charts,
    mission_get_field_info,
    mission_update_charts,
    mission_add_charts
)

def run_tests():
    """Runs a series of smoke tests for the dashboard API."""
    print("--- Running Dashboard API Smoke Tests ---")

    # Test 1: Generate dashboard from layer
    print("\n1. Testing mission_generate_dashboard (source='layer')")
    result = mission_generate_dashboard("buildings", source="layer")
    assert result["success"], f"Test 1 Failed: {result.get('message')}"
    print("   ... Passed")

    # Test 2: Generate dashboard from existing dashboard
    print("\n2. Testing mission_generate_dashboard (source='dashboard')")
    result = mission_generate_dashboard("buildings", source="dashboard")
    assert result["success"], f"Test 2 Failed: {result.get('message')}"
    print("   ... Passed")

    # Test 3: Get layout
    print("\n3. Testing mission_get_layout")
    result = mission_get_layout()
    assert result["success"], f"Test 3 Failed: {result.get('message')}"
    assert "layout" in result["data"] and "charts" in result["data"], "Test 3 Failed: Layout or charts missing"
    print("   ... Passed")

    # Test 4: Get charts
    print("\n4. Testing mission_get_charts")
    result = mission_get_charts()
    assert result["success"], f"Test 4 Failed: {result.get('message')}"
    assert isinstance(result["data"], list), "Test 4 Failed: Data is not a list"
    print("   ... Passed")

    # Test 5: Get all field info
    print("\n5. Testing mission_get_field_info (all fields)")
    result = mission_get_field_info()
    assert result["success"], f"Test 5 Failed: {result.get('message')}"
    assert isinstance(result["data"], dict), "Test 5 Failed: Data is not a dict"
    print("   ... Passed")

    # Test 6: Get single field info
    print("\n6. Testing mission_get_field_info (single field)")
    result = mission_get_field_info("height")
    assert result["success"], f"Test 6 Failed: {result.get('message')}"
    assert result["data"]["field_name"] == "height", "Test 6 Failed: Incorrect field info"
    print("   ... Passed")

    # Test 7: Add new charts
    print("\n7. Testing mission_add_charts")
    new_charts = [
        {"fields": ["storeys"], "chart_type": "histogram"},
        {"fields": ["owner"], "chart_type": "pie"}
    ]
    result = mission_add_charts(new_charts)
    assert result["success"], f"Test 7 Failed: {result.get('message')}"
    print("   ... Passed")

    # Test 8: Update charts
    print("\n8. Testing mission_update_charts")
    updates = [
        {"index": 0, "fields": ["building_type_updated"], "chart_type": "bar"},
    ]
    result = mission_update_charts(updates)
    assert result["success"], f"Test 8 Failed: {result.get('message')}"
    print("   ... Passed")

    print("\n--- All Dashboard API Smoke Tests Passed! ---")

if __name__ == "__main__":
    # Clean up dashboard file before running tests
    if os.path.exists("progent_dashboard.json"):
        os.remove("progent_dashboard.json")

    run_tests()

    # Clean up after tests
    if os.path.exists("progent_dashboard.json"):
        os.remove("progent_dashboard.json")
