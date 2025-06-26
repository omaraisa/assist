"""
This module provides function declarations in the specific formats required by different AI models.
Each AI provider has its own schema format for function/tool calling.
"""

from typing import Dict, List, Any
from .spatial_functions import SpatialFunctions

class FunctionDeclarationGenerator:
    """Generate function declarations for different AI models"""
    
    def __init__(self):
        self.spatial_functions = SpatialFunctions()
        self._function_definitions = self._generate_base_definitions()
    
    def _generate_base_definitions(self) -> Dict[str, Dict]:
        """Generate base function definitions with parameters and descriptions"""
        # Only provide the discovery function - all other functions must be discovered dynamically
        base_definitions = {
            "get_functions_declaration": {
                "name": "get_functions_declaration",
                "description": 'Get function declarations for specific functions by their IDs from the available functions list. MAKE SURE TO SEND VALID IDs. AVAILABLE FUNCTIONS: 1: select_by_attribute, 2: select_by_location, 3: get_field_statistics, 4: get_layer_summary, 5: calculate_area, 6: calculate_length, 7: get_centroid, 8: create_buffer, 9: spatial_join, 10: clip_layer, 11: calculate_distance, 12: get_current_project_path, 13: get_default_db_path, 14: get_field_definitions, 15: get_layer_type, 16: get_list_of_layer_fields, 17: get_data_source_info, 18: create_nearest_neighbor_layer, 19: get_unique_values_count, 20: calculate_empty_values, 21: get_map_layers_info, 22: get_map_tables_info, 23: get_values_frequency, 24: get_value_frequency, 25: get_coordinate_system, 26: get_attribute_table, 27: get_field_domain_values, 28: calculate_new_field.',
                "parameters": {
                    "function_ids": {
                        "type": "array",
                        "description": 'Array of function IDs (integers) to get declarations for',
                        "items": {
                            "type": "integer"
                        }
                    }
                },
                "required": ["function_ids"]
            }
        }
        
        # Do NOT add all the spatial function declarations here
        # They should be discovered dynamically via get_functions_declaration
        
        return base_definitions
    
    def get_openai_functions(self) -> List[Dict[str, Any]]:
        """Generate OpenAI function calling format"""
        functions = []
        
        for func_name, func_def in self._function_definitions.items():
            openai_func = {
                "type": "function",
                "function": {
                    "name": func_def["name"],
                    "description": func_def["description"],
                    "parameters": {
                        "type": "object",
                        "properties": {},
                        "required": func_def["required"]
                    }
                }
            }
            
            # Convert parameters to OpenAI format
            for param_name, param_def in func_def["parameters"].items():
                openai_param = {
                    "type": param_def["type"],
                    "description": param_def["description"]
                }
                
                # Add enum if present
                if "enum" in param_def:
                    openai_param["enum"] = param_def["enum"]
                
                # Add items for arrays
                if "items" in param_def:
                    openai_param["items"] = param_def["items"]
                
                openai_func["function"]["parameters"]["properties"][param_name] = openai_param
            
            functions.append(openai_func)
        
        return functions
    
    def get_gemini_functions(self) -> List[Dict[str, Any]]:
        """Generate Gemini function calling format"""
        functions = []
        
        for func_name, func_def in self._function_definitions.items():
            gemini_func = {
                "name": func_def["name"],
                "description": func_def["description"],
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": func_def["required"]
                }
            }
            
            # Convert parameters to Gemini format (similar to OpenAI but slightly different structure)
            for param_name, param_def in func_def["parameters"].items():
                gemini_param = {
                    "type": param_def["type"],
                    "description": param_def["description"]
                }
                
                # Add enum if present
                if "enum" in param_def:
                    gemini_param["enum"] = param_def["enum"]
                    
                # Add items for arrays
                if "items" in param_def:
                    gemini_param["items"] = param_def["items"]
                
                gemini_func["parameters"]["properties"][param_name] = gemini_param
            
            functions.append(gemini_func)
        
        return functions
    
    def get_claude_tools(self) -> List[Dict[str, Any]]:
        """Generate Claude/Anthropic tool calling format"""
        tools = []
        
        for func_name, func_def in self._function_definitions.items():
            claude_tool = {
                "name": func_def["name"],
                "description": func_def["description"],
                "input_schema": {
                    "type": "object",
                    "properties": {},
                    "required": func_def["required"]
                }
            }
            
            # Convert parameters to Claude format
            for param_name, param_def in func_def["parameters"].items():
                claude_param = {
                    "type": param_def["type"],
                    "description": param_def["description"]
                }
                
                # Add enum if present
                if "enum" in param_def:
                    claude_param["enum"] = param_def["enum"]
                    
                # Add items for arrays
                if "items" in param_def:
                    claude_param["items"] = param_def["items"]
                
                claude_tool["input_schema"]["properties"][param_name] = claude_param
            
            tools.append(claude_tool)
        
        return tools
    
    def get_functions_summary(self) -> str:
        """Get a summary of all available functions for AI context"""
        summary_lines = ["Available GIS Analysis Functions:"]
        
        for func_name, func_def in self._function_definitions.items():
            summary_lines.append(f"• {func_def['name']}: {func_def['description']}")
        
        return "\n".join(summary_lines)

# Create global instance for easy access
function_declarations = FunctionDeclarationGenerator()

# Export the different formats
openai_functions = function_declarations.get_openai_functions()
gemini_functions = function_declarations.get_gemini_functions() 
claude_tools = function_declarations.get_claude_tools()
functions_summary = function_declarations.get_functions_summary()
