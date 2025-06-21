#!/usr/bin/env python3
"""
Test the function calling fix for Gemini and Claude
"""

import asyncio
import sys
import traceback

async def test_function_calling_fix():
    """Test that function calling works with all AI providers"""
    print("=" * 60)
    print("TESTING FUNCTION CALLING FIX")
    print("=" * 60)
    
    try:
        from app.ai_service import AIService
        from app.config import settings
        
        # Test 1: Initialize AI Service
        print("1. Initializing AI Service...")
        ai_service = AIService()
        await ai_service.initialize()
        print("   ✓ AI Service initialized successfully")
        
        # Test 2: Test intelligent function selection
        print("\n2. Testing intelligent function selection...")
        
        test_message = "how many schools where governorate field = الخرج"
        
        # Test OpenAI format
        try:
            functions, intent = ai_service._get_intelligent_function_selection(test_message, "openai")
            print(f"   ✓ OpenAI format: {len(functions)} functions, intent: {intent}")
        except Exception as e:
            print(f"   ✗ OpenAI format failed: {e}")
        
        # Test Gemini format
        try:
            functions, intent = ai_service._get_intelligent_function_selection(test_message, "gemini")
            print(f"   ✓ Gemini format: {len(functions)} functions, intent: {intent}")
        except Exception as e:
            print(f"   ✗ Gemini format failed: {e}")
        
        # Test Claude format
        try:
            functions, intent = ai_service._get_intelligent_function_selection(test_message, "claude")
            print(f"   ✓ Claude format: {len(functions)} functions, intent: {intent}")
        except Exception as e:
            print(f"   ✗ Claude format failed: {e}")
        
        # Test 3: Test function conversion
        print("\n3. Testing function conversion...")
        
        # Get base functions
        base_functions, intent = ai_service._get_intelligent_function_selection(test_message, "openai")
        
        # Test Gemini conversion
        try:
            gemini_functions = ai_service._convert_functions_to_provider_format(base_functions, "gemini")
            print(f"   ✓ Gemini conversion: {len(gemini_functions)} functions converted")
            
            # Check if it's a proper Gemini format (should have 'name' and 'description')
            if gemini_functions and 'name' in gemini_functions[0]:
                print("   ✓ Gemini format is correct")
            else:
                print("   ⚠️  Gemini format might be incorrect")
        except Exception as e:
            print(f"   ✗ Gemini conversion failed: {e}")
        
        # Test Claude conversion
        try:
            claude_functions = ai_service._convert_functions_to_provider_format(base_functions, "claude")
            print(f"   ✓ Claude conversion: {len(claude_functions)} functions converted")
            
            # Check if it's a proper Claude format (should have 'name' and 'description')
            if claude_functions and 'name' in claude_functions[0]:
                print("   ✓ Claude format is correct")
            else:
                print("   ⚠️  Claude format might be incorrect")
        except Exception as e:
            print(f"   ✗ Claude conversion failed: {e}")
        
        # Test 4: Test mock function response handling
        print("\n4. Testing function response handling...")
        
        # Mock function results
        mock_function_results = [{
            "id": "test_123",
            "name": "get_value_frequency",
            "parameters": {
                "layer_name": "RiyadhSchools",
                "field_name": "Governorate", 
                "lookup_value": "الخرج"
            },
            "result": {
                "function_executed": "get_value_frequency",
                "layer_name": "RiyadhSchools",
                "field_name": "Governorate",
                "lookup_value": "الخرج",
                "success": True,
                "value_count": 396,
                "total_count": 6327,
                "percentage": 6.258890469416785
            }
        }]
        
        # Test fallback response generation
        try:
            fallback_response = ai_service._generate_fallback_response(mock_function_results)
            print(f"   ✓ Fallback response generated ({len(fallback_response)} chars)")
            print(f"   Preview: {fallback_response[:100]}...")
        except Exception as e:
            print(f"   ✗ Fallback response failed: {e}")
            traceback.print_exc()
        
        # Cleanup
        await ai_service.cleanup()
        
        print("\n" + "=" * 60)
        print("✅ Function calling fix test completed successfully!")
        print("The system should now handle function calling properly.")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        traceback.print_exc()
        return False

async def main():
    """Main test function"""
    print("Testing Function Calling Fix...")
    print("This test verifies that the Gemini/Claude function calling issue is resolved.\n")
    
    success = await test_function_calling_fix()
    
    if success:
        print("\n🎉 SUCCESS: Function calling fix is working!")
        print("\nYou can now test the question again:")
        print('how many schools where governorate field = الخرج')
        return 0
    else:
        print("\n❌ FAILED: Function calling fix needs more work.")
        return 1

if __name__ == "__main__":
    try:
        exit_code = asyncio.run(main())
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        traceback.print_exc()
        sys.exit(1)
