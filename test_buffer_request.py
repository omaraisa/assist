#!/usr/bin/env python3
"""
Test script to simulate a buffer request and see the AI's response
"""

import asyncio
import json
import sys
import os

# Add the app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from ai_service import AIService
from spatial_functions import SpatialFunctions

async def test_buffer_request():
    """Test the AI's response to a buffer creation request"""
    
    # Initialize AI service
    ai_service = AIService()
    await ai_service.initialize()
    
    # Test request
    user_message = "I need you make buffer for RiyadhSchools layer by 3 km"
    
    # Simulated conversation history and ArcGIS state
    conversation_history = []
    arcgis_state = {
        "layers": [
            {"name": "RiyadhSchools", "type": "Point", "visible": True},
            {"name": "Roads", "type": "Polyline", "visible": True}
        ]
    }
    
    print(f"🤖 Processing request: {user_message}")
    print("=" * 60)
    
    try:
        # Generate AI response
        response = await ai_service.generate_response(
            user_message=user_message,
            conversation_history=conversation_history,
            arcgis_state=arcgis_state,
            client_id="test_client"
        )
        
        print(f"📤 AI Response Type: {response.get('type')}")
        print(f"📝 Content: {response.get('content', 'No content')}")
        
        if response.get('type') == 'function_calls':
            print("🔧 Function calls detected:")
            function_calls = response.get('function_calls', [])
            for i, call in enumerate(function_calls, 1):
                print(f"  {i}. {call.get('name')} - {call.get('parameters')}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
    
    # Cleanup
    if ai_service.session:
        await ai_service.session.close()

if __name__ == "__main__":
    asyncio.run(test_buffer_request())
