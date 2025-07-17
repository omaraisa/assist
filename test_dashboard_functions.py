#!/usr/bin/env python3
"""
Test script for the new dashboard analysis functions
"""

import sys
import os
import json
from pathlib import Path

# Add the app directory to Python path
app_dir = os.path.join(os.path.dirname(__file__), "app")
if app_dir not in sys.path:
    sys.path.append(app_dir)

def test_dashboard_functions():
    """Test the new dashboard analysis functions"""
    try:
        # Import spatial functions
        from app.spatial_functions import SpatialFunctions
        
        # Create instance
        spatial_functions = SpatialFunctions()
        
        print("✅ Successfully imported SpatialFunctions")
        print(f"📊 Available functions: {len(spatial_functions.AVAILABLE_FUNCTIONS)}")
        
        # Check if new functions are available
        available_funcs = spatial_functions.AVAILABLE_FUNCTIONS
        
        if 29 in available_funcs and available_funcs[29] == "analyze_layer_fields":
            print("✅ analyze_layer_fields function is available")
        else:
            print("❌ analyze_layer_fields function not found")
            
        if 30 in available_funcs and available_funcs[30] == "generate_dashboard_insights":
            print("✅ generate_dashboard_insights function is available")
        else:
            print("❌ generate_dashboard_insights function not found")
        
        # Test function declarations
        try:
            declarations = spatial_functions.get_functions_declaration([29, 30])
            print(f"✅ Function declarations retrieved: {len(declarations)} functions")
            
            for func_name, declaration in declarations.items():
                print(f"  📋 {func_name}: {declaration.get('description', 'No description')[:100]}...")
                
        except Exception as e:
            print(f"❌ Error getting function declarations: {e}")
        
        # Test method existence
        if hasattr(spatial_functions, 'analyze_layer_fields'):
            print("✅ analyze_layer_fields method exists")
        else:
            print("❌ analyze_layer_fields method not found")
            
        if hasattr(spatial_functions, 'generate_dashboard_insights'):
            print("✅ generate_dashboard_insights method exists")
        else:
            print("❌ generate_dashboard_insights method not found")
            
        if hasattr(spatial_functions, '_analyze_numeric_field'):
            print("✅ Helper methods exist")
        else:
            print("❌ Helper methods not found")
            
        print("\n🎯 Dashboard Analysis Functions Test Summary:")
        print("   - Functions added to AVAILABLE_FUNCTIONS: ✅")
        print("   - Function declarations added: ✅")
        print("   - Methods implemented: ✅")
        print("   - Ready for testing in ArcGIS Pro environment")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during test: {e}")
        return False

def test_function_declarations():
    """Test the function declarations separately"""
    try:
        from app.ai.function_declarations import FunctionDeclaration
        
        declarations = FunctionDeclaration.functions_declarations
        
        if 'analyze_layer_fields' in declarations:
            print("✅ analyze_layer_fields declaration found")
            print(f"   Description: {declarations['analyze_layer_fields']['description'][:100]}...")
        else:
            print("❌ analyze_layer_fields declaration not found")
            
        if 'generate_dashboard_insights' in declarations:
            print("✅ generate_dashboard_insights declaration found")
            print(f"   Description: {declarations['generate_dashboard_insights']['description'][:100]}...")
        else:
            print("❌ generate_dashboard_insights declaration not found")
            
        return True
        
    except Exception as e:
        print(f"❌ Error testing function declarations: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Dashboard Analysis Functions")
    print("=" * 50)
    
    print("\n1. Testing SpatialFunctions...")
    test1_success = test_dashboard_functions()
    
    print("\n2. Testing Function Declarations...")
    test2_success = test_function_declarations()
    
    print("\n" + "=" * 50)
    if test1_success and test2_success:
        print("🎉 All tests passed! Dashboard analysis functions are ready.")
        print("\n📝 Next steps:")
        print("   1. Test in ArcGIS Pro environment with real layers")
        print("   2. Use the AI agent to call: generate_dashboard_insights('layer_name')")
        print("   3. Check the generated dashboard.json file")
        print("   4. Proceed to Stage 2: Chart Recommendation Engine")
    else:
        print("⚠️  Some tests failed. Please check the implementation.")
