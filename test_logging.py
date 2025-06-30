#!/usr/bin/env python3
"""
Quick test script to verify AI service logging and basic functionality
"""

import sys
import os
import asyncio
import logging

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)

async def test_ai_logging():
    """Test the AI service with enhanced logging"""
    
    print("🔍 Testing AI Service Logging")
    print("=" * 40)
    
    try:
        from app.ai_service import AIService
        from app.config import settings
        
        # Mock simple ArcGIS state
        mock_arcgis_state = {
            "workspace": "C:/Test/Test.gdb",
            "layers_info": {
                "Governorates": {
                    "fields": {
                        "OBJECTID": {"type": "esriFieldTypeOID"},
                        "NAME": {"type": "esriFieldTypeString"}
                    }
                },
                "RiyadhSchools": {
                    "fields": {
                        "OBJECTID": {"type": "esriFieldTypeOID"},
                        "NAME": {"type": "esriFieldTypeString"}
                    }
                }
            },
            "layer_types": {"Governorates": "Polygon", "RiyadhSchools": "Point"}
        }
        
        # Initialize AI service
        ai_service = AIService()
        await ai_service.initialize()
        
        # Use GPT if available to avoid Gemini rate limits
        if settings.OPENAI_API_KEY:
            ai_service.set_model("GPT4O")
            print(f"🤖 Using model: {ai_service.current_model}")
        else:
            print(f"⚠️  Using default model: {ai_service.current_model}")
        
        # Test with the exact message from your log
        print("\n📝 Testing with buffer request...")
        
        response = await ai_service.generate_response(
            user_message="buffer Governorates layer by 3 km then select all RiyadhSchools that intersect with this buffer",
            conversation_history=[],
            arcgis_state=mock_arcgis_state,
            client_id="test_client"
        )
        
        print(f"\n✅ Response received!")
        print(f"Type: {response.get('type', 'unknown')}")
        print(f"Content preview: {str(response.get('content', ''))[:200]}...")
        
        if response.get('function_calls'):
            print(f"Function calls detected: {len(response.get('function_calls', []))}")
            for i, call in enumerate(response.get('function_calls', [])):
                print(f"  {i+1}. {call.get('name', 'unknown')}")
        
        # Clean up
        await ai_service.cleanup()
        
        print("\n🎉 Test completed!")
        
    except Exception as e:
        print(f"\n❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_ai_logging())
