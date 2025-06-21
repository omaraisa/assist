#!/usr/bin/env python3
"""
Simple test to check Ollama availability and basic service functionality
"""

import sys
import traceback

def test_imports():
    """Test basic imports"""
    print("Testing imports...")
    
    try:
        from app.config import settings
        print("✓ Config imported")
    except Exception as e:
        print(f"✗ Config import failed: {e}")
        return False
    
    try:
        from app.ai_service import OLLAMA_AVAILABLE, AIService
        print(f"✓ AI Service imported - Ollama Available: {OLLAMA_AVAILABLE}")
    except Exception as e:
        print(f"✗ AI Service import failed: {e}")
        traceback.print_exc()
        return False
    
    return True

def test_ollama_detection():
    """Test Ollama server detection"""
    print("\nTesting Ollama detection...")
    
    try:
        from app.ai_service import _test_ollama_server
        is_running = _test_ollama_server()
        print(f"✓ Ollama server test: {'Running' if is_running else 'Not running'}")
        return True
    except Exception as e:
        print(f"✗ Ollama detection test failed: {e}")
        return False

def test_ai_service_basic():
    """Test basic AI service functionality"""
    print("\nTesting AI Service initialization...")
    
    try:
        from app.ai_service import AIService
        service = AIService()
        print("✓ AI Service created successfully")
        
        # Test available models
        available_models = []
        from app.config import settings
        
        if settings.GEMINI_API_KEY:
            available_models.append("Gemini")
        if settings.OPENAI_API_KEY:
            available_models.append("OpenAI")
        if settings.ANTHROPIC_API_KEY:
            available_models.append("Claude")
        
        print(f"✓ Available cloud models: {available_models}")
        
        if not available_models:
            print("⚠️  No API keys found - cloud models unavailable")
        
        return True
    except Exception as e:
        print(f"✗ AI Service test failed: {e}")
        traceback.print_exc()
        return False

def main():
    """Main test function"""
    print("=" * 50)
    print("AI SMART ASSISTANT - SIMPLE TEST")
    print("=" * 50)
    
    success = True
    
    success &= test_imports()
    success &= test_ollama_detection()
    success &= test_ai_service_basic()
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 All basic tests passed!")
        print("The service should work without Ollama.")
    else:
        print("❌ Some tests failed.")
    print("=" * 50)
    
    return 0 if success else 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        traceback.print_exc()
        sys.exit(1)
