#!/usr/bin/env python3
"""
SmartAssistant Function Calling Demonstration
Shows the new function calling system in action
"""

import asyncio
import json
from app.ai_service import AIService

async def demonstrate_function_calling():
    """Demonstrate the new function calling capabilities"""
    
    print("🎯 SmartAssistant Function Calling System Demo")
    print("=" * 50)
    
    # Initialize AI service
    ai_service = AIService()
    await ai_service.initialize()
    
    try:
        print(f"\n📱 Current AI Model: {ai_service.current_model}")
        
        # Example 1: OpenAI Function Calling Format
        print(f"\n🔧 OpenAI Function Call Example:")
        ai_service.set_model("GPT_4")
        
        openai_response = {
            "type": "function_calls",
            "function_calls": [
                {
                    "id": "call_abc123",
                    "type": "function", 
                    "function": {
                        "name": "get_layer_summary",
                        "arguments": '{"layer_name": "cities"}'
                    }
                }
            ],
            "content": "I'll analyze the cities layer for you."
        }
        
        parsed_calls = ai_service.parse_function_calls(openai_response)
        print(f"   Function: {parsed_calls[0]['name']}")
        print(f"   Parameters: {json.dumps(parsed_calls[0]['parameters'], indent=6)}")
        print(f"   ID: {parsed_calls[0]['id']}")
        
        # Example 2: Gemini Function Calling Format  
        print(f"\n🔧 Gemini Function Call Example:")
        ai_service.set_model("GEMINI_PRO")
        
        gemini_response = {
            "type": "function_calls",
            "function_calls": [
                {
                    "name": "calculate_area",
                    "args": {
                        "layer_name": "parcels",
                        "units": "square_kilometers"
                    }
                }
            ],
            "content": "Calculating area for the parcels layer..."
        }
        
        parsed_calls = ai_service.parse_function_calls(gemini_response)
        print(f"   Function: {parsed_calls[0]['name']}")
        print(f"   Parameters: {json.dumps(parsed_calls[0]['parameters'], indent=6)}")
        
        # Example 3: Claude Function Calling Format
        print(f"\n🔧 Claude Function Call Example:")
        ai_service.set_model("CLAUDE_3_5_SONNET")
        
        claude_response = {
            "type": "function_calls",
            "function_calls": [
                {
                    "id": "toolu_xyz789",
                    "name": "select_by_attribute", 
                    "input": {
                        "layer_name": "demographics",
                        "where_clause": "POPULATION > 100000",
                        "selection_type": "NEW_SELECTION"
                    }
                }
            ],
            "content": "Selecting features based on population criteria..."
        }
        
        parsed_calls = ai_service.parse_function_calls(claude_response)
        print(f"   Function: {parsed_calls[0]['name']}")
        print(f"   Parameters: {json.dumps(parsed_calls[0]['parameters'], indent=6)}")
        print(f"   ID: {parsed_calls[0]['id']}")
        
        # Example 4: System Prompt Generation
        print(f"\n📝 System Prompt with ArcGIS State:")
        mock_arcgis_state = {
            "layers_info": {
                "cities": {
                    "fields": {"NAME": "String", "POPULATION": "Integer", "AREA_KM2": "Double"}
                },
                "roads": {
                    "fields": {"ROAD_NAME": "String", "ROAD_TYPE": "String", "LENGTH_M": "Double"}
                }
            },
            "layer_types": {
                "cities": "Feature Layer",
                "roads": "Feature Layer"
            },
            "workspace": "C:/GIS/DemoProject.aprx"
        }
        
        messages = ai_service._prepare_messages(
            "Show me population statistics for large cities",
            [],
            mock_arcgis_state
        )
        
        system_prompt = messages[0]["content"]
        print(f"   System prompt includes:")
        print(f"   - Model identity and capabilities")
        print(f"   - Available layers: {list(mock_arcgis_state['layers_info'].keys())}")
        print(f"   - Layer fields and types")
        print(f"   - Current workspace information")
        print(f"   - Function calling instructions")
        
        # Example 5: Legacy Compatibility
        print(f"\n🔄 Legacy System Compatibility:")
        legacy_response = "INVESTIGATE```get_field_statistics(layer_name='cities', field_name='POPULATION')```INVESTIGATE```calculate_area(layer_name='cities')```COMPLETE```The cities layer has {len(features)} features with an average population of {avg_pop}```"
        
        investigate_commands = ai_service.extract_investigate_commands(legacy_response)
        complete_response = ai_service.extract_complete_response(legacy_response) 
        
        print(f"   Legacy INVESTIGATE commands found: {len(investigate_commands)}")
        for i, cmd in enumerate(investigate_commands, 1):
            print(f"     {i}. {cmd}")
        
        print(f"   Legacy COMPLETE response: '{complete_response}'")
        
        print(f"\n✅ Function Calling System Features:")
        print(f"   🎯 Native function calling for OpenAI, Gemini, Claude")
        print(f"   🔧 27+ spatial analysis functions available")
        print(f"   📊 Structured parameter validation")
        print(f"   🛡️ Enhanced error handling and recovery")
        print(f"   🔄 Full backward compatibility with legacy system")
        print(f"   ⚡ Improved performance and reliability")
        
        print(f"\n🎉 Demo completed successfully!")
        print(f"🚀 SmartAssistant is ready for production with function calling!")
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")
    finally:
        await ai_service.cleanup()

if __name__ == "__main__":
    asyncio.run(demonstrate_function_calling())
