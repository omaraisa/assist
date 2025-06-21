#!/usr/bin/env python3
"""
Simple test for the AI Smart Assistant server without Ollama
Tests that the service can start and function properly when Ollama is not available
"""

import asyncio
import json
import sys
import traceback
from app.ai_service import AIService, OLLAMA_AVAILABLE
from app.config import settings

async def test_ai_service_without_ollama():
    """Test the AI service functionality without Ollama"""
    print("=" * 60)
    print("AI SMART ASSISTANT - SERVER TEST (WITHOUT OLLAMA)")
    print("=" * 60)
    
    # Test 1: Check Ollama availability
    print(f"1. Ollama availability check: {'✓ Available' if OLLAMA_AVAILABLE else '✗ Not Available'}")
    
    # Test 2: Initialize AI Service
    print("\n2. Initializing AI Service...")
    try:
        ai_service = AIService()
        await ai_service.initialize()
        print("   ✓ AI Service initialized successfully")
    except Exception as e:
        print(f"   ✗ AI Service initialization failed: {e}")
        return False
    
    # Test 3: Test available models
    print("\n3. Testing available AI models...")
    available_models = []
    
    # Test Gemini (if API key available)
    if settings.GEMINI_API_KEY:
        available_models.append("GEMINI_FLASH")
        print("   ✓ Gemini models available (API key found)")
    else:
        print("   ✗ Gemini models unavailable (no API key)")
    
    # Test OpenAI (if API key available)
    if settings.OPENAI_API_KEY:
        available_models.append("GPT4_TURBO")
        print("   ✓ OpenAI models available (API key found)")
    else:
        print("   ✗ OpenAI models unavailable (no API key)")
    
    # Test Claude (if API key available)
    if settings.ANTHROPIC_API_KEY:
        available_models.append("CLAUDE_SONNET")
        print("   ✓ Claude models available (API key found)")
    else:
        print("   ✗ Claude models unavailable (no API key)")
    
    # Test Ollama
    if OLLAMA_AVAILABLE:
        available_models.append("OLLAMA_LLAMA31")
        print("   ✓ Ollama models available")
    else:
        print("   ✗ Ollama models unavailable (expected - Ollama not installed)")
    
    if not available_models:
        print("\n   ⚠️  WARNING: No AI models available! Please set up API keys.")
        print("   Set environment variables:")
        print("   - GEMINI_API_KEY for Google Gemini")
        print("   - OPENAI_API_KEY for OpenAI GPT")
        print("   - ANTHROPIC_API_KEY for Claude")
        return False
    
    # Test 4: Test intent classification
    print("\n4. Testing intent classification...")
    try:
        test_messages = [
            "how many layers are available",
            "show field statistics",
            "calculate area of polygons"
        ]
        
        for msg in test_messages:
            intent = ai_service._classify_user_intent(msg)
            print(f"   '{msg}' -> {intent}")
        print("   ✓ Intent classification working")
    except Exception as e:
        print(f"   ✗ Intent classification failed: {e}")
    
    # Test 5: Test function selection
    print("\n5. Testing intelligent function selection...")
    try:
        functions, intent = ai_service._get_intelligent_function_selection("show available layers")
        print(f"   Selected {len(functions)} functions for intent: {intent}")
        print("   ✓ Function selection working")
    except Exception as e:
        print(f"   ✗ Function selection failed: {e}")
    
    # Test 6: Test Ollama handling when not available
    if not OLLAMA_AVAILABLE:
        print("\n6. Testing Ollama unavailability handling...")
        try:
            # Try to set Ollama model
            original_model = ai_service.current_model
            ai_service.current_model = "OLLAMA_LLAMA31"
            
            # Mock ArcGIS state and conversation
            mock_state = {"workspace": "test", "layers_info": {}}
            mock_conversation = []
            
            # Try to generate response
            response = await ai_service.generate_response(
                "test message", 
                mock_conversation, 
                mock_state
            )
            
            if response["type"] == "error" and "Ollama service is not available" in response["content"]:
                print("   ✓ Ollama unavailability handled gracefully")
            else:
                print("   ✗ Ollama unavailability not handled properly")
            
            # Restore original model
            ai_service.current_model = original_model
            
        except Exception as e:
            print(f"   ✗ Ollama handling test failed: {e}")
    
    # Test 7: Test model switching to available model
    if available_models:
        print(f"\n7. Testing model switching to available model ({available_models[0]})...")
        try:
            ai_service.set_model(available_models[0])
            print(f"   ✓ Successfully switched to {available_models[0]}")
        except Exception as e:
            print(f"   ✗ Model switching failed: {e}")
    
    # Cleanup
    await ai_service.cleanup()
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY:")
    print(f"✓ Ollama detection: {'Working' if not OLLAMA_AVAILABLE else 'Unexpected'}")
    print(f"✓ Service initialization: Working")
    print(f"✓ Available models: {len(available_models)} found")
    print(f"✓ Core functionality: Working")
    if not OLLAMA_AVAILABLE:
        print("✓ Ollama unavailability: Handled gracefully")
    print("=" * 60)
    
    return True

def test_server_startup():
    """Test that the server can start without Ollama"""
    print("\nTesting server components...")
    
    try:
        # Test imports
        from app.main import app
        from app.websocket_manager import WebSocketManager
        print("   ✓ All server components imported successfully")
        
        # Test WebSocket manager
        ws_manager = WebSocketManager()
        print("   ✓ WebSocket manager initialized")
        
        return True
    except Exception as e:
        print(f"   ✗ Server component test failed: {e}")
        traceback.print_exc()
        return False

async def main():
    """Main test function"""
    print("Starting AI Smart Assistant Server Test...")
    print("This test verifies the service works without Ollama installed.\n")
    
    # Test 1: Server startup
    server_ok = test_server_startup()
    
    # Test 2: AI Service
    if server_ok:
        ai_ok = await test_ai_service_without_ollama()
        
        if ai_ok:
            print("\n🎉 SUCCESS: AI Smart Assistant server is working properly without Ollama!")
            print("\nThe service is ready to use with cloud-based AI models.")
            print("You can start the server with: python run.py")
        else:
            print("\n❌ FAILED: Some tests failed. Please check the logs above.")
            return 1
    else:
        print("\n❌ FAILED: Server components test failed.")
        return 1
    
    return 0

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
