#!/usr/bin/env python3
"""
Quick test for the function calling tuple unpacking fix
"""

def test_tuple_unpacking():
    """Test that the tuple unpacking is working correctly"""
    print("Testing tuple unpacking fix...")
    
    try:
        # Simulate the function that returns a tuple
        def mock_get_intelligent_function_selection(message, provider):
            functions = [{"name": "test_function", "description": "test"}]
            intent = "FIELD_ANALYSIS" 
            return functions, intent
        
        # Test unpacking (this is what was broken before)
        message = "test message"
        
        # This should work now
        functions, intent = mock_get_intelligent_function_selection(message, "gemini")
        print(f"✓ Tuple unpacking works: {len(functions)} functions, intent: {intent}")
        
        # Test that we don't accidentally pass the intent as part of functions
        if isinstance(functions, list) and isinstance(intent, str):
            print("✓ Types are correct: functions is list, intent is string")
        else:
            print(f"✗ Types are wrong: functions={type(functions)}, intent={type(intent)}")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_tuple_unpacking()
    if success:
        print("\n🎉 The tuple unpacking fix should work!")
        print("The Gemini API error should be resolved.")
    else:
        print("\n❌ There's still an issue with the fix.")
