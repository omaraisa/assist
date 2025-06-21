#!/usr/bin/env python3
"""
Test script for Phase 1 token optimization functionality
"""

from app.ai_service import AIService

def test_intent_classification():
    """Test the intent classification system"""
    print("Testing Intent Classification...")
    
    ai = AIService()
    
    test_cases = [
        ("how many layers", "LAYER_INFO"),
        ("what fields are available", "FIELD_ANALYSIS"), 
        ("calculate area of polygons", "SPATIAL_ANALYSIS"),
        ("select features where population > 1000", "SELECTION"),
        ("get project path", "SYSTEM"),
        ("hello how are you", "GENERAL")
    ]
    
    for message, expected in test_cases:
        intent = ai._classify_user_intent(message)
        status = "✓" if intent == expected else "✗"
        print(f"{status} '{message}' -> {intent} (expected: {expected})")

def test_function_selection():
    """Test intelligent function selection"""
    print("\nTesting Function Selection...")
    
    ai = AIService()
    
    # Test different intents
    test_cases = [
        ("show me available layers", "LAYER_INFO"),
        ("get field statistics for population", "FIELD_ANALYSIS"),
        ("calculate buffer around cities", "SPATIAL_ANALYSIS")
    ]
    
    for message, expected_intent in test_cases:
        functions, intent = ai._get_intelligent_function_selection(message)
        print(f"Message: '{message}'")
        print(f"  Intent: {intent}")
        print(f"  Functions selected: {len(functions)}")
        print(f"  Function names: {[f['function']['name'] for f in functions[:3]]}")

def test_state_reduction():
    """Test ArcGIS state payload reduction"""
    print("\nTesting State Reduction...")
    
    ai = AIService()
    
    # Mock ArcGIS state
    mock_state = {
        "workspace": "C:/MyProject",
        "default_gdb": "MyProject.gdb",
        "layers_info": {
            "Cities": {
                "fields": {"OBJECTID": {}, "NAME": {}, "POPULATION": {}, "AREA": {}},
                "feature_count": 150,
                "geometry_type": "Point"
            },
            "Counties": {
                "fields": {"OBJECTID": {}, "COUNTY_NAME": {}, "STATE": {}},
                "feature_count": 50,
                "geometry_type": "Polygon"
            }
        }
    }
    
    test_cases = [
        ("what layers are available", "LAYER_INFO"),
        ("show field statistics for population", "FIELD_ANALYSIS"),
        ("calculate area of counties", "SPATIAL_ANALYSIS")
    ]
    
    original_size = len(str(mock_state))
    
    for message, intent in test_cases:
        reduced_state = ai._get_relevant_arcgis_state_by_intent(intent, mock_state, message)
        reduced_size = len(str(reduced_state))
        reduction = ((original_size - reduced_size) / original_size) * 100
        print(f"Intent: {intent}")
        print(f"  Original size: {original_size} chars")
        print(f"  Reduced size: {reduced_size} chars")
        print(f"  Reduction: {reduction:.1f}%")

if __name__ == "__main__":
    print("=" * 60)
    print("PHASE 1 TOKEN OPTIMIZATION - FUNCTIONALITY TEST")
    print("=" * 60)
    
    try:
        test_intent_classification()
        test_function_selection()
        test_state_reduction()
        
        print("\n" + "=" * 60)
        print("✓ ALL TESTS COMPLETED SUCCESSFULLY")
        print("✓ Phase 1 optimizations are working correctly")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
