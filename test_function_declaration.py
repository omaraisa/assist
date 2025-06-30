#!/usr/bin/env python3
"""
Test script to verify get_functions_declaration is properly included
"""

import sys
import os
import asyncio
import logging

# Add the current directory to Python path so we can import from app
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)

async def test_function_declaration_inclusion():
    """Test that get_functions_declaration is properly included in messages"""
    
    print("🧪 Testing get_functions_declaration inclusion")
    print("=" * 50)
    
    try:
        # Import after path setup
        from app.ai_service import AIService
        from app.config import settings
        
        # Mock ArcGIS state - minimal
        mock_arcgis_state = {
            "workspace": "C:/Test/Test.gdb",
            "layers_info": {
                "schools": {
                    "fields": {
                        "OBJECTID": {"type": "esriFieldTypeOID"},
                        "NAME": {"type": "esriFieldTypeString"}
                    }
                }
            }
        }
        
        # Initialize AI service
        ai_service = AIService()
        await ai_service.initialize()
        
        print(f"🤖 Using AI Model: {ai_service.current_model}")
        
        # Test 1: Fresh conversation - should include function declaration
        print("\n📝 Test 1: Fresh conversation")
        messages = ai_service._prepare_messages(
            user_message="Create a buffer around schools",
            conversation_history=[],
            arcgis_state=mock_arcgis_state,
            client_id="test_client"
        )
        
        # Check if get_functions_declaration is included
        has_declaration = False
        for msg in messages:
            if "get_functions_declaration" in msg.get("content", "") and "Function Declaration:" in msg.get("content", ""):
                has_declaration = True
                print("✅ get_functions_declaration found in fresh conversation")
                break
        
        if not has_declaration:
            print("❌ get_functions_declaration NOT found in fresh conversation")
        
        # Test 2: Conversation with existing declaration - should NOT duplicate
        print("\n📝 Test 2: Conversation with existing declaration")
        history_with_declaration = [
            {"role": "user", "content": "Hi"},
            {"role": "system", "content": """AVAILABLE FUNCTION: get_functions_declaration

Function Declaration:
{
    "name": "get_functions_declaration",
    "description": "Get function declarations for specific functions...",
    "parameters": {
        "function_ids": {
            "type": "array",
            "description": "Array of function IDs (integers) to get declarations for",
            "items": {
                "type": "integer"
            }
        }
    },
    "required": ["function_ids"]
}"""}
        ]
        
        messages2 = ai_service._prepare_messages(
            user_message="Create a buffer around schools",
            conversation_history=history_with_declaration,
            arcgis_state=mock_arcgis_state,
            client_id="test_client"
        )
        
        # Count how many times get_functions_declaration appears
        declaration_count = 0
        for msg in messages2:
            if "get_functions_declaration" in msg.get("content", "") and "Function Declaration:" in msg.get("content", ""):
                declaration_count += 1
        
        print(f"Found {declaration_count} get_functions_declaration instances")
        if declaration_count == 1:
            print("✅ get_functions_declaration appears exactly once (no duplication)")
        else:
            print(f"❌ get_functions_declaration appears {declaration_count} times (should be 1)")
        
        # Print message structure for debugging
        print(f"\nTotal messages: {len(messages2)}")
        for i, msg in enumerate(messages2):
            print(f"Message {i+1}: {msg['role']} - {len(msg['content'])} chars")
        
        # Clean up
        await ai_service.cleanup()
        
        print("\n🎉 Test completed!")
        
    except Exception as e:
        print(f"\n❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_function_declaration_inclusion())
