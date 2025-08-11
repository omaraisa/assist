#!/usr/bin/env python3
"""
Test script for multi-field support in dashboard system
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

# Import directly from app module
from app.spatial_functions import SpatialFunctions

def test_chart_recommendations():
    """Test that chart recommendations work with new fields array format"""
    sf = SpatialFunctions()
    
    # Test get_current_dashboard_charts - should return fields array
    print("Testing get_current_dashboard_charts...")
    result = sf.get_current_dashboard_charts()
    print(f"Success: {result.get('success')}")
    
    if result.get('success'):
        charts = result.get('charts', [])
        print(f"Found {len(charts)} charts")
        for i, chart in enumerate(charts[:3]):  # Show first 3
            print(f"  Chart {i+1}: fields={chart.get('fields')}, chart_type={chart.get('chart_type')}")
            
            # Test that we can access fields[0] for backward compatibility
            fields = chart.get('fields', [])
            if fields:
                print(f"    Primary field (fields[0]): {fields[0]}")
    
    print()
    
    # Test layout retrieval with fields
    print("Testing get_current_dashboard_layout...")
    layout_result = sf.get_current_dashboard_layout()
    print(f"Success: {layout_result.get('success')}")
    
    if layout_result.get('success'):
        widgets = layout_result.get('widgets', [])
        print(f"Found {len(widgets)} widgets")
        for i, widget in enumerate(widgets[:3]):  # Show first 3
            fields = widget.get('fields', [])
            print(f"  Widget {i+1}: id={widget.get('id')}, fields={fields}")
            if fields:
                print(f"    Primary field (fields[0]): {fields[0]}")

if __name__ == "__main__":
    test_chart_recommendations()
