#!/usr/bin/env python3
"""
Simple test script to verify dashboard structure and aggregation chart functionality
"""

import json
import sys
import os

# Add the app directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.main import _parse_dashboard_data, prepare_chart_data_from_insights

def test_dashboard_parsing():
    """Test the dashboard parsing functionality"""

    # Sample dashboard data with aggregation chart
    sample_dashboard = {
        "charts": [
            {
                "chart_type": "bar",
                "data_category": "aggregation",
                "aggregation_info": {
                    "data": [
                        {"category": "Operator A", "value": 150.5},
                        {"category": "Operator B", "value": 200.3},
                        {"category": "Operator C", "value": 175.8}
                    ],
                    "x_field": "operator",
                    "y_field": "gallons_sold_july_91",
                    "aggregation_type": "mean"
                },
                "title": "Mean of gallons_sold_july_91 by operator"
            }
        ],
        "field_insights": {
            "operator": {"data_type": "text", "unique_values": 3},
            "gallons_sold_july_91": {"data_type": "numeric", "min": 100, "max": 300}
        }
    }

    print("Testing dashboard parsing with aggregation chart...")

    try:
        # Test parsing
        parsed_data = _parse_dashboard_data(sample_dashboard)
        print(f"Parsed data keys: {list(parsed_data.keys())}")

        # Test chart preparation
        charts = prepare_chart_data_from_insights(parsed_data)
        print(f"Number of charts prepared: {len(charts)}")

        if charts:
            chart = charts[0]
            print(f"Chart type: {chart.get('type')}")
            print(f"Chart data points: {len(chart.get('data', []))}")
            print(f"Sample data point: {chart.get('data', [])[0] if chart.get('data') else 'None'}")

        print("✅ Test passed - aggregation chart parsing works!")

    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_dashboard_parsing()
