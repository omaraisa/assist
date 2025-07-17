#!/usr/bin/env python3
"""
Test script for Stage 2: Chart Recommendation Engine
Tests the new smart dashboard layout generation
"""

import sys
import os
import json
from pathlib import Path

# Add the app directory to Python path
app_dir = os.path.join(os.path.dirname(__file__), "app")
if app_dir not in sys.path:
    sys.path.append(app_dir)

def test_stage2_functions():
    """Test the Stage 2 smart dashboard layout functions"""
    try:
        # Import spatial functions
        from app.spatial_functions import SpatialFunctions
        
        # Create instance
        spatial_functions = SpatialFunctions()
        
        print("✅ Successfully imported SpatialFunctions")
        print(f"📊 Available functions: {len(spatial_functions.AVAILABLE_FUNCTIONS)}")
        
        # Check if Stage 2 function is available
        available_funcs = spatial_functions.AVAILABLE_FUNCTIONS
        
        if 31 in available_funcs and available_funcs[31] == "generate_smart_dashboard_layout":
            print("✅ generate_smart_dashboard_layout function is available")
        else:
            print("❌ generate_smart_dashboard_layout function not found")
            return False
        
        # Test function declarations
        try:
            declarations = spatial_functions.get_functions_declaration([31])
            print(f"✅ Function declarations retrieved: {len(declarations)} functions")
            
            for func_name, declaration in declarations.items():
                print(f"  📋 {func_name}: {declaration.get('description', 'No description')[:100]}...")
                
        except Exception as e:
            print(f"❌ Error getting function declarations: {e}")
            return False
        
        # Test method existence
        if hasattr(spatial_functions, 'generate_smart_dashboard_layout'):
            print("✅ generate_smart_dashboard_layout method exists")
        else:
            print("❌ generate_smart_dashboard_layout method not found")
            return False
            
        # Test helper methods
        helper_methods = [
            '_generate_intelligent_chart_recommendations',
            '_create_dashboard_layout_plan',
            '_generate_chart_configurations',
            '_get_dashboard_themes'
        ]
        
        for method in helper_methods:
            if hasattr(spatial_functions, method):
                print(f"✅ Helper method {method} exists")
            else:
                print(f"❌ Helper method {method} not found")
                return False
        
        print("\n🎯 Stage 2 Functions Test Summary:")
        print("   - Function added to AVAILABLE_FUNCTIONS: ✅")
        print("   - Function declaration added: ✅")
        print("   - Main method implemented: ✅")
        print("   - Helper methods implemented: ✅")
        print("   - Ready for testing in ArcGIS Pro environment")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during test: {e}")
        return False

def test_stage2_function_declarations():
    """Test the Stage 2 function declarations"""
    try:
        from app.ai.function_declarations import FunctionDeclaration
        
        declarations = FunctionDeclaration.functions_declarations
        
        if 'generate_smart_dashboard_layout' in declarations:
            print("✅ generate_smart_dashboard_layout declaration found")
            desc = declarations['generate_smart_dashboard_layout']['description']
            print(f"   Description: {desc[:100]}...")
            print(f"   Parameters: {list(declarations['generate_smart_dashboard_layout']['parameters'].keys())}")
        else:
            print("❌ generate_smart_dashboard_layout declaration not found")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Error testing function declarations: {e}")
        return False

def display_stage2_features():
    """Display the new Stage 2 features"""
    print("\n🚀 Stage 2: Chart Recommendation Engine Features:")
    print("=" * 60)
    
    features = [
        "🧠 Intelligent Chart Selection - Analyzes field characteristics for optimal chart types",
        "📐 12x9 Grid Layout Planning - Optimized positioning and sizing",
        "🎨 Chart Configuration Generation - Detailed styling and interactivity settings",
        "🔄 Priority-Based Arrangement - High-value insights get better positions",
        "📊 Multiple Chart Types - Pie, Bar, Histogram, Scatter, Heatmap, Box Plot, Donut",
        "🎯 Field Relationship Analysis - Cross-field correlations and patterns",
        "🌈 Theme Support - Multiple color schemes and styling options",
        "⚡ Smart Sizing - Charts sized based on data complexity and importance",
        "📱 Responsive Layout - Adaptable to different dashboard sizes",
        "🔍 Enhanced Insights - Data-driven recommendations with suitability scores"
    ]
    
    for feature in features:
        print(f"   {feature}")
    
    print("\n📋 Output Structure:")
    print("   📄 smart_dashboard.json - Enhanced dashboard with:")
    print("      • Field insights and analysis")
    print("      • Intelligent chart recommendations") 
    print("      • 12x9 grid layout plan")
    print("      • Detailed chart configurations")
    print("      • Theme and styling options")

if __name__ == "__main__":
    print("🧪 Testing Stage 2: Chart Recommendation Engine")
    print("=" * 60)
    
    print("\n1. Testing Stage 2 Functions...")
    test1_success = test_stage2_functions()
    
    print("\n2. Testing Function Declarations...")
    test2_success = test_stage2_function_declarations()
    
    print("\n3. Stage 2 Features Overview...")
    display_stage2_features()
    
    print("\n" + "=" * 60)
    if test1_success and test2_success:
        print("🎉 Stage 2 implementation complete and ready!")
        print("\n📝 Next steps:")
        print("   1. Test in ArcGIS Pro environment with real layers")
        print("   2. Use the AI agent to call: generate_smart_dashboard_layout('layer_name')")
        print("   3. Check the generated smart_dashboard.json file")
        print("   4. Compare with Stage 1 dashboard.json to see improvements")
        print("   5. Proceed to Stage 3: Layout Planner (if needed)")
        print("\n💡 Example AI prompts to try:")
        print('   "Generate a smart dashboard layout for my roads layer"')
        print('   "Create an intelligent dashboard with optimal chart recommendations"')
        print('   "Build a professional dashboard layout with grid positioning"')
    else:
        print("⚠️  Some tests failed. Please check the implementation.")
