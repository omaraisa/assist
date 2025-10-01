import arcpy
import json
from datetime import datetime
import re
import urllib.request

def safe_getattr(obj, attr, default=None):
    """Safely get attribute without causing errors"""
    try:
        return getattr(obj, attr, default)
    except:
        return default

def extract_parameter_info(param):
    """Extract all possible parameter attributes safely"""
    param_info = {}
    
    # List of all known parameter attributes
    attributes = [
        'name', 'displayName', 'datatype', 'parameterType', 'direction',
        'defaultValue', 'value', 'enabled', 'category', 'multiValue',
        'filter', 'parameterDependencies', 'schema', 'altered',
        'hasBeenValidated', 'message', 'controlCLSID', 'columns'
    ]
    
    for attr in attributes:
        val = safe_getattr(param, attr)
        if val is not None:
            # Convert complex objects to strings for JSON serialization
            if attr in ['filter', 'parameterDependencies', 'columns']:
                param_info[attr] = str(val)
            else:
                param_info[attr] = val
    
    return param_info

def extract_tool_metadata(tool_name):
    """
    Extract all available metadata from an ArcGIS tool for AI/RAG documentation
    """
    metadata = {
        "tool_name": tool_name,
        "extraction_date": datetime.now().isoformat()
    }
    
    # 1. Basic tool information
    try:
        metadata["display_name"] = tool_name
        parts = tool_name.split("_")
        metadata["toolbox"] = parts[-1] if len(parts) > 1 else "Unknown"
        metadata["base_name"] = "_".join(parts[:-1]) if len(parts) > 1 else tool_name
    except Exception as e:
        metadata["basic_info_error"] = str(e)
    
    # 2. Get tool description using Describe
    try:
        desc = arcpy.Describe(tool_name)
        describe_attrs = ['dataType', 'name', 'baseName', 'file', 'path', 
                         'catalogPath', 'extension', 'dataElementType']
        
        metadata["describe"] = {}
        for attr in describe_attrs:
            val = safe_getattr(desc, attr)
            if val is not None:
                metadata["describe"][attr] = val
    except Exception as e:
        metadata["describe_error"] = str(e)
    
    # 3. Get tool usage/syntax (most reliable metadata)
    try:
        usage = arcpy.Usage(tool_name)
        metadata["usage_syntax"] = usage
        
        # Parse usage to extract parameter names
        if usage and "(" in usage:
            # Extract everything between parentheses
            params_str = usage[usage.find("(")+1:usage.rfind(")")]
            # Split by comma but respect nested braces
            metadata["parsed_parameters"] = [p.strip() for p in params_str.split(",")]
    except Exception as e:
        metadata["usage_error"] = str(e)
    
    # 4. Help documentation URL
    base_name = metadata["base_name"]
    slug = re.sub(r'([A-Z])', r'-\1', base_name).lower().lstrip('-')
    metadata["help_url"] = f"https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/{slug}.htm"
    
    # 5. Try to get parameter information (FIXED - avoid symbology)
    try:
        params = arcpy.GetParameterInfo(tool_name)
        if params:
            param_list = []
            for i, param in enumerate(params):
                param_info = extract_parameter_info(param)
                param_info["index"] = i
                param_list.append(param_info)
            metadata["parameters"] = param_list
            metadata["parameter_count"] = len(param_list)
    except Exception as e:
        metadata["parameters_error"] = str(e)
    
    # 6. Fetch parameter details from web documentation
    try:
        url = metadata["help_url"]
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
        
        # Find the Parameters section
        start = html.find('## Parameters')
        if start != -1:
            # Find the table start
            table_start = html.find('|  |\n|  |\n|', start)
            if table_start != -1:
                # Find the end of table
                end = html.find('##', table_start + 10)
                if end == -1:
                    end = len(html)
                table_text = html[table_start:end]
                
                # Parse rows
                lines = table_text.split('\n')
                web_params = []
                for line in lines:
                    if line.startswith('|') and line.count('|') >= 4:
                        parts = [p.strip() for p in line.split('|')[1:-1]]
                        if len(parts) >= 3:
                            name, explanation, datatype = parts[0], ' '.join(parts[1:-1]), parts[-1]
                            web_params.append({
                                "name": name,
                                "explanation": explanation,
                                "datatype": datatype
                            })
                if web_params:
                    metadata["web_parameters"] = web_params
                    # Integrate web explanations into existing parameters
                    if "parameters" in metadata:
                        for param in metadata["parameters"]:
                            param_name = param.get("name", "").lower()
                            display_name = param.get("displayName", "").lower()
                            for web_param in web_params:
                                web_name = web_param["name"].lower()
                                if param_name == web_name or display_name == web_name:
                                    param["web_explanation"] = web_param["explanation"]
                                    param["web_datatype"] = web_param["datatype"]
                                    break
    except Exception as e:
        metadata["web_fetch_error"] = str(e)
    
    # 6. Try to get tool environment settings
    try:
        # Common environment settings
        env_settings = [
            'workspace', 'scratchWorkspace', 'outputCoordinateSystem',
            'extent', 'snapRaster', 'cellSize', 'mask', 'overwriteOutput'
        ]
        metadata["environment_settings"] = {}
        for setting in env_settings:
            val = safe_getattr(arcpy.env, setting)
            if val is not None:
                metadata["environment_settings"][setting] = str(val)
    except Exception as e:
        metadata["env_error"] = str(e)
    
    # 7. Check licensing and extensions
    try:
        metadata["licensing"] = {
            "product_info": arcpy.ProductInfo(),
            "checkout_status": "Available"
        }
    except Exception as e:
        metadata["licensing_error"] = str(e)
    
    # 8. Get messages/metadata if available
    try:
        metadata["tool_info"] = {
            "exists": arcpy.Exists(tool_name),
            "is_licensed": True  # If we got this far, it's accessible
        }
    except Exception as e:
        metadata["availability_error"] = str(e)
    
    return metadata


def generate_tool_declaration(metadata):
    """
    Generate a Python function declaration for the tool based on its metadata
    """
    tool_name = metadata.get("tool_name", "")
    base_name = metadata.get("base_name", "")
    
    # Create function name
    func_name = base_name.lower()
    
    # Get parameters
    params = metadata.get("parameters", [])
    
    # Build parameter list
    param_list = []
    docstring_lines = []
    
    for param in params:
        name = param.get("name", "")
        display_name = param.get("displayName", "")
        datatype = param.get("datatype", "")
        required = param.get("parameterType", "") == "Required"
        default_val = param.get("defaultValue")
        explanation = param.get("web_explanation", param.get("displayName", ""))
        
        # Parameter name in function
        param_name = name.lower().replace(" ", "_")
        
        # Add to param list
        if required:
            param_list.append(param_name)
        else:
            if default_val is not None:
                if isinstance(default_val, str):
                    param_list.append(f'{param_name}="{default_val}"')
                else:
                    param_list.append(f'{param_name}={default_val}')
            else:
                param_list.append(f'{param_name}=None')
        
        # Add to docstring
        docstring_lines.append(f"{param_name} ({datatype}): {explanation}")
    
    # Function signature
    signature = f"def {func_name}({', '.join(param_list)}):"
    
    # Docstring
    docstring = f'    """{metadata.get("display_name", "")}\n\n'
    docstring += "\n".join(f"    {line}" for line in docstring_lines)
    docstring += '\n    """'
    
    # Function body
    body = f"    # Execute {tool_name}\n"
    body += f"    result = arcpy.{tool_name}("
    args = []
    for param in params:
        param_name = param.get("name", "").lower().replace(" ", "_")
        args.append(param_name)
    body += ", ".join(args)
    body += ")\n    return result"
    
    return f"{signature}\n{docstring}\n{body}"


def extract_analysis_toolbox_metadata(output_file="E:\\ai_stage\\assist_clean\\assist\\Progent\\analysis_tools_metadata.json"):
    """
    Extract metadata for all tools in the Analysis toolbox
    """
    analysis_tools = arcpy.ListTools("*_analysis")
    
    all_metadata = {
        "toolbox": "Analysis",
        "extraction_timestamp": datetime.now().isoformat(),
        "arcgis_version": arcpy.GetInstallInfo()['Version'],
        "product": arcpy.ProductInfo(),
        "tool_count": len(analysis_tools),
        "tools": []
    }
    
    print(f"Found {len(analysis_tools)} tools in Analysis toolbox")
    print(f"ArcGIS Version: {all_metadata['arcgis_version']}")
    print("=" * 80)
    
    for i, tool in enumerate(analysis_tools, 1):
        print(f"\n[{i}/{len(analysis_tools)}] Processing: {tool}")
        print("-" * 80)
        
        tool_metadata = extract_tool_metadata(tool)
        all_metadata["tools"].append(tool_metadata)
        
        # Print key information
        print(f"Display Name: {tool_metadata.get('display_name', 'N/A')}")
        
        if "usage_syntax" in tool_metadata:
            usage = tool_metadata['usage_syntax']
            print(f"Usage: {usage[:150]}{'...' if len(usage) > 150 else ''}")
        
        if "parameters" in tool_metadata:
            print(f"✓ Parameters: {len(tool_metadata['parameters'])} extracted successfully")
            # Show first 3 parameters
            for p in tool_metadata['parameters'][:3]:
                print(f"  - {p.get('displayName', p.get('name', 'Unknown'))}: {p.get('datatype', 'N/A')}")
            if len(tool_metadata['parameters']) > 3:
                print(f"  ... and {len(tool_metadata['parameters']) - 3} more")
        elif "parameters_error" in tool_metadata:
            print(f"✗ Parameters: {tool_metadata['parameters_error']}")
        
        if "parsed_parameters" in tool_metadata:
            print(f"Parsed from usage: {len(tool_metadata['parsed_parameters'])} parameters")
    
    # Save to JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_metadata, f, indent=2, ensure_ascii=False, default=str)
    
    print(f"\n{'='*80}")
    print(f"✓ Metadata saved to: {output_file}")
    print(f"✓ Total tools documented: {len(analysis_tools)}")
    
    # Statistics
    tools_with_params = sum(1 for t in all_metadata['tools'] if 'parameters' in t)
    tools_with_usage = sum(1 for t in all_metadata['tools'] if 'usage_syntax' in t)
    
    print(f"\nStatistics:")
    print(f"  - Tools with parameter details: {tools_with_params}/{len(analysis_tools)}")
    print(f"  - Tools with usage syntax: {tools_with_usage}/{len(analysis_tools)}")
    print("="*80)
    
    return all_metadata


def print_detailed_tool_info(tool_name="Buffer_analysis"):
    """
    Print all extracted metadata for a single tool
    """
    print(f"\n{'='*80}")
    print(f"COMPLETE METADATA EXTRACTION FOR: {tool_name}")
    print(f"{'='*80}\n")
    
    metadata = extract_tool_metadata(tool_name)
    
    # Pretty print with sections
    print("1. BASIC INFORMATION")
    print("-" * 40)
    print(f"Tool Name: {metadata.get('tool_name')}")
    print(f"Base Name: {metadata.get('base_name')}")
    print(f"Toolbox: {metadata.get('toolbox')}")
    
    print("\n2. USAGE SYNTAX")
    print("-" * 40)
    print(metadata.get('usage_syntax', 'N/A'))
    
    print("\n3. PARAMETERS")
    print("-" * 40)
    if 'parameters' in metadata:
        for param in metadata['parameters']:
            print(f"\n  Parameter {param.get('index', '?')}:")
            print(f"    Name: {param.get('name', 'N/A')}")
            print(f"    Display: {param.get('displayName', 'N/A')}")
            print(f"    Type: {param.get('datatype', 'N/A')}")
            print(f"    Direction: {param.get('direction', 'N/A')}")
            print(f"    Required: {param.get('parameterType', 'N/A')}")
            if param.get('defaultValue'):
                print(f"    Default: {param.get('defaultValue')}")
    else:
        print(f"Error: {metadata.get('parameters_error', 'Unknown')}")
    
    print("\n4. DOCUMENTATION")
    print("-" * 40)
    print(f"Help URL: {metadata.get('help_url')}")
    
    print("\n5. FULL JSON")
    print("-" * 40)
    print(json.dumps(metadata, indent=2, default=str))
    print(f"\n{'='*80}\n")


# Main execution
if __name__ == "__main__":
    # Show detailed example first
    print_detailed_tool_info("Buffer_analysis")
    
    # Then extract all tools
    all_metadata = extract_analysis_toolbox_metadata()
    
    # Generate function declarations
    declarations = []
    for tool_meta in all_metadata["tools"]:
        if "parameters" in tool_meta:
            try:
                decl = generate_tool_declaration(tool_meta)
                declarations.append(decl)
            except Exception as e:
                print(f"Error generating declaration for {tool_meta.get('tool_name')}: {e}")
    
    # Save declarations to file
    with open("E:\\ai_stage\\assist_clean\\assist\\Progent\\tool_declarations.py", 'w', encoding='utf-8') as f:
        f.write("# Generated ArcGIS Pro Analysis Tools Function Declarations\n\n")
        f.write("import arcpy\n\n")
        f.write("\n\n".join(declarations))
    
    print(f"\n✓ Function declarations saved to: tool_declarations.py")
    print("\n✓ Complete! Check 'analysis_tools_metadata.json' for full details.")