#!/usr/bin/env python3
"""
Test script to verify cancellation functionality
"""

import asyncio
import websockets
import json
import uuid

async def test_cancellation():
    """Test the cancellation feature"""
    uri = "ws://localhost:8000/ws"
    
    try:
        async with websockets.connect(uri) as websocket:
            client_id = str(uuid.uuid4())
            
            # Register as a chatbot client
            await websocket.send(json.dumps({
                "type": "client_register",
                "client_type": "chatbot",
                "client_id": client_id
            }))
            
            print("Connected and registered as chatbot client")
            
            # Send a test message
            await websocket.send(json.dumps({
                "type": "user_message",
                "content": "Tell me about the layers in my ArcGIS Pro project",
                "model": "GEMINI_FLASH"
            }))
            
            print("Sent test message")
            
            # Wait a short time then send cancel
            await asyncio.sleep(1)
            
            await websocket.send(json.dumps({
                "type": "cancel_request"
            }))
            
            print("Sent cancel request")
            
            # Listen for responses
            timeout = 10
            start_time = asyncio.get_event_loop().time()
            
            while asyncio.get_event_loop().time() - start_time < timeout:
                try:
                    message = await asyncio.wait_for(websocket.recv(), timeout=1.0)
                    data = json.loads(message)
                    print(f"Received: {data.get('type', 'unknown')} - {data.get('message', '')[:100]}")
                    
                    if data.get('type') == 'cancelled':
                        print("✅ Cancellation confirmed!")
                        break
                        
                except asyncio.TimeoutError:
                    continue
            
    except Exception as e:
        print(f"❌ Test failed: {e}")

if __name__ == "__main__":
    print("Testing cancellation functionality...")
    asyncio.run(test_cancellation())
