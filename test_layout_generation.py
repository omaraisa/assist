#!/usr/bin/env python3
"""
Test script for generating new dashboard layout with fields array
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from app.spatial_functions import SpatialFunctions

def test_layout_generation():
    """Test that new layout generation uses fields array format"""
    sf = SpatialFunctions()
    
    print("Testing layout generation with sample data...")
    
    # Create sample field insights for testing
    sample_insights = {
        "Population": {
            "ai_insights": {
                "chart_suitability": {"bar": 0.9, "histogram": 0.8},
                "visualization_potential": "high",
                "visualization_priority": 8
            }
        },
        "Income": {
            "ai_insights": {
                "chart_suitability": {"histogram": 0.9, "box_plot": 0.7},
                "visualization_potential": "high", 
                "visualization_priority": 7
            }
        }
    }
    
    # Test chart recommendations
    chart_recs = sf.recommend_chart_types(sample_insights)
    print(f"Chart recommendations: {chart_recs}")
    
    # Test layout planning
    layout = sf.plan_dashboard_layout(chart_recs)
    print(f"Generated layout: {layout}")
    
    # Verify the layout uses fields array
    for widget in layout.get("dashboard_layout", []):
        fields = widget.get("fields", [])
        print(f"Widget {widget.get('id')}: fields={fields}, chart_type={widget.get('chart_type')}")
        if fields:
            print(f"  Primary field (fields[0]): {fields[0]}")

if __name__ == "__main__":
    test_layout_generation()
