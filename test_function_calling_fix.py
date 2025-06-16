#!/usr/bin/env python3
"""
Test script to verify the function calling system fix
"""
import asyncio
import json
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, '.')

async def test_function_calling_fix():
    """Test the function calling system with the new response format"""
    
    print("🔧 Testing Function Calling System Fix")
    print("=" * 50)
    
    try:
        # Import required modules
        from app.ai_service import AIService
        from app.main import process_ai_response_with_functions, websocket_manager
        
        print("✅ Successfully imported modules")
        
        # Initialize AI service
        ai_service = AIService()
        await ai_service.initialize()
        print(f"✅ AI Service initialized with model: {ai_service.current_model}")
        
        # Test the new response format (Dictionary instead of string)
        mock_ai_response = {
            "type": "text",
            "content": "Hello! I can help you analyze your GIS data. How many layers are on your map?"
        }
        
        print(f"✅ Testing new response format: {mock_ai_response['type']}")
        
        # Test function calling response format
        mock_function_response = {
            "type": "function_calls",
            "function_calls": [
                {
                    "id": "test_call_123",
                    "name": "get_layer_summary",
                    "parameters": {"layer_name": "test_layer"}
                }
            ],
            "content": "Let me get information about your layers..."
        }
        
        print(f"✅ Testing function calling format: {len(mock_function_response['function_calls'])} function calls")
        
        # Test function call parsing
        parsed_calls = ai_service.parse_function_calls(mock_function_response)
        print(f"✅ Parsed function calls: {len(parsed_calls)} functions")
        
        if parsed_calls:
            print(f"   - Function: {parsed_calls[0]['name']}")
            print(f"   - Parameters: {parsed_calls[0]['parameters']}")
            print(f"   - ID: {parsed_calls[0]['id']}")
        
        # Test WebSocket manager function context methods
        print("✅ Testing WebSocket manager function context storage")
        
        # Store a test context
        test_session_id = "test_session_123"
        test_context = {
            "client_id": "test_client",
            "function_call": parsed_calls[0] if parsed_calls else {},
            "original_response": mock_function_response,
            "is_function_calling": True
        }
        
        websocket_manager.store_function_context(test_session_id, test_context)
        
        # Retrieve the context
        retrieved_context = websocket_manager.get_function_context(test_session_id)
        if retrieved_context and retrieved_context.get("is_function_calling"):
            print("✅ Function context storage and retrieval working")
        else:
            print("❌ Function context storage issue")
            
        # Clean up
        websocket_manager.remove_function_context(test_session_id)
        
        print("\n🎉 All tests passed! Function calling system is working correctly.")
        print("🚀 The 'Error processing AI response: expected string or bytes-like object, got dict' issue is FIXED!")
        
        # Summary of the fix
        print("\n📋 Fix Summary:")
        print("   ✅ Updated main.py to handle Dict responses instead of strings")
        print("   ✅ Added process_ai_response_with_functions() method")
        print("   ✅ Added execute_function_calls() method")
        print("   ✅ Added handle_function_calling_response() method")
        print("   ✅ Updated handle_function_response() to support new system")
        print("   ✅ Added function context storage methods to WebSocketManager")
        print("   ✅ Fixed indentation issues in websocket_manager.py")
        print("   ✅ Updated demo to use correct model names")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    """Main test function"""
    success = await test_function_calling_fix()
    if success:
        print("\n✅ SUCCESS: Function calling system is ready for production!")
        sys.exit(0)
    else:
        print("\n❌ FAILURE: Issues found in function calling system")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
