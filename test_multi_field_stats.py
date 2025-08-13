"""
Test script for multi-field statistics generation
This will help you test the new multi-field chart data generation functions
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from spatial_functions import SpatialFunctions
import json

def test_multi_field_statistics():
    """Test the new multi-field statistics generation"""
    
    # Initialize spatial functions
    spatial_func = SpatialFunctions()
    
    # Test layer name (replace with your actual layer name)
    layer_name = "jeddah_fuel_stations_ai"  # From your reduced dashboard
    
    print("🧪 Testing Multi-Field Statistics Generation")
    print("=" * 50)
    
    # Test 1: Scatter plot (2 numeric fields)
    print("\n1. Testing Scatter Plot (2 numeric fields)")
    scatter_fields = ["gallons_sold_july_91", "gallons_sold_july_95"]
    scatter_result = spatial_func.generate_multi_field_statistics(
        layer_name, scatter_fields, "scatter"
    )
    
    if scatter_result.get("success"):
        print(f"✅ Scatter plot generated: {scatter_result['statistics']['total_points']} points")
        print(f"   Correlation: {scatter_result['statistics']['correlation']:.3f}")
    else:
        print(f"❌ Scatter plot failed: {scatter_result.get('error')}")
    
    # Test 2: Bar chart (categorical + numeric)
    print("\n2. Testing Bar Chart (categorical + numeric)")
    bar_fields = ["operator", "gallons_sold_july_91"]
    bar_result = spatial_func.generate_multi_field_statistics(
        layer_name, bar_fields, "bar"
    )
    
    if bar_result.get("success"):
        print(f"✅ Bar chart generated: {bar_result['statistics']['categories']} categories")
    else:
        print(f"❌ Bar chart failed: {bar_result.get('error')}")
    
    # Test 3: Pie chart (single categorical)
    print("\n3. Testing Pie Chart (single categorical)")
    pie_fields = ["has_ev_charging"]
    pie_result = spatial_func.generate_multi_field_statistics(
        layer_name, pie_fields, "pie"
    )
    
    if pie_result.get("success"):
        print(f"✅ Pie chart generated: {pie_result['statistics']['total_categories']} categories")
    else:
        print(f"❌ Pie chart failed: {pie_result.get('error')}")
    
    # Test 4: Histogram (single numeric)
    print("\n4. Testing Histogram (single numeric)")
    hist_fields = ["customer_satisfaction_score"]
    hist_result = spatial_func.generate_multi_field_statistics(
        layer_name, hist_fields, "histogram"
    )
    
    if hist_result.get("success"):
        print(f"✅ Histogram generated: {hist_result['statistics']['num_bins']} bins")
    else:
        print(f"❌ Histogram failed: {hist_result.get('error')}")
    
    # Test 5: Generate data for specific widget
    print("\n5. Testing Widget-Specific Data Generation")
    widget_result = spatial_func.generate_widget_chart_data(
        layer_name, 
        fields=["convenience_store_sales", "non_fuel_revenue"], 
        chart_type="scatter"
    )
    
    if widget_result.get("success"):
        print(f"✅ Widget data generated for {widget_result['chart_type']} chart")
    else:
        print(f"❌ Widget data failed: {widget_result.get('error')}")
    
    # Test 6: Generate all dashboard data
    print("\n6. Testing Complete Dashboard Data Generation")
    all_data_result = spatial_func.generate_all_dashboard_data(layer_name)
    
    if all_data_result.get("success"):
        successful = all_data_result.get("successful_widgets", 0)
        total = all_data_result.get("total_widgets", 0)
        print(f"✅ Dashboard data generated: {successful}/{total} widgets successful")
        
        if all_data_result.get("errors"):
            print(f"   ⚠️  Errors encountered: {len(all_data_result['errors'])}")
            for error in all_data_result["errors"][:3]:  # Show first 3 errors
                print(f"      - {error}")
        
        # Save sample output for inspection
        sample_widget = list(all_data_result["widget_data"].keys())[0] if all_data_result["widget_data"] else None
        if sample_widget:
            sample_data = all_data_result["widget_data"][sample_widget]
            with open("sample_chart_data.json", "w") as f:
                json.dump(sample_data, f, indent=2)
            print(f"   💾 Sample chart data saved to 'sample_chart_data.json'")
    else:
        print(f"❌ Dashboard data generation failed: {all_data_result.get('error')}")
    
    print("\n" + "=" * 50)
    print("🎯 Test Complete!")
    print("\nNext steps:")
    print("1. Check 'sample_chart_data.json' to see the Chart.js format")
    print("2. Use 'generate_widget_chart_data()' in your frontend API")
    print("3. Use 'generate_all_dashboard_data()' for full dashboard refresh")

if __name__ == "__main__":
    test_multi_field_statistics()
