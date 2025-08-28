#!/usr/bin/env python3
"""
Test script to verify the enhanced dashboard API with AI insights
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'Progent'))

from app.dashboard_api import _fetch_layer_fields, _prepare_field_insights_from_layer

def test_ai_insights():
    """Test the AI insights generation"""
    print("Testing AI-powered field insights generation...")

    # Fetch sample layer fields
    fields = _fetch_layer_fields("TestLayer")
    print(f"\nFetched {len(fields)} fields:")
    for field in fields:
        print(f"  - {field['field_name']} ({field['type']}): {len(field['sample_values'])} samples")

    # Generate AI insights
    insights = _prepare_field_insights_from_layer(fields)

    print(f"\nGenerated AI insights for {len(insights)} fields:")
    for field_name, insight in insights.items():
        print(f"\n{field_name}:")
        print(f"  Category: {insight.get('data_category', 'unknown')}")
        print(f"  Visualization Priority: {insight.get('visualization_priority', 0)}")
        print(f"  Potential: {insight.get('visualization_potential', 'unknown')}")
        print(f"  Story: {insight.get('data_story', 'No story')[:100]}...")
        print(f"  Chart Suitability: {insight.get('chart_suitability', {})}")

if __name__ == "__main__":
    test_ai_insights()
