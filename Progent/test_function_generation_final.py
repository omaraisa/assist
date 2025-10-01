#!/usr/bin/env python3
"""
Test script to generate progent.pyt style functions and AI declarations
"""

import urllib.request
import json
import re
from datetime import datetime
import time

def fetch_page(url):
    """Fetch a webpage with error handling"""
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_summary_from_tool_page(html):
    """Extract the Summary section from a tool's help page"""
    # Find the Summary section
    summary_start = html.find('<div class="section1 summary"')
    if summary_start == -1:
        return ""

    # Find the end of the summary div
    summary_end = html.find('</div>', summary_start)
    if summary_end == -1:
        return ""

    summary_html = html[summary_start:summary_end]

    # Extract text from <p> tags
    import re
    p_pattern = r'<p[^>]*>(.*?)</p>'
    paragraphs = re.findall(p_pattern, summary_html, re.DOTALL)

    # Clean up the text
    summary_text = ""
    for p in paragraphs:
        # Remove HTML tags
        clean_p = re.sub(r'<[^>]+>', '', p).strip()
        if clean_p:
            summary_text += clean_p + " "

    return summary_text.strip()

def extract_parameters_from_tool_page(html):
    """Extract parameters from a tool's help page"""
    parameters = []

    # Find the Python tab section (not the Dialog tab)
    # Look for the Python tab content
    python_start = html.find('<a class="tab-title js-tab gptab" val="python">Python</a>')
    if python_start == -1:
        return parameters

    # Find the Python article section
    python_article_start = html.find('<article class="tab-section js-tab-section">', python_start)
    if python_article_start == -1:
        return parameters

    # Find the end of this article
    python_article_end = html.find('</article>', python_article_start)
    if python_article_end == -1:
        python_article_end = len(html)

    python_section = html[python_article_start:python_article_end]

    # Find the parameter table in the Python section
    table_start = python_section.find('<table class="gptoolparamtbl">')
    if table_start == -1:
        return parameters

    table_end = python_section.find('</table>', table_start)
    if table_end == -1:
        table_end = len(python_section)

    table_html = python_section[table_start:table_end]

    # Parse table rows
    import re
    # Find all table rows
    row_pattern = r'<tr[^>]*>(.*?)</tr>'
    rows = re.findall(row_pattern, table_html, re.DOTALL)

    for row in rows:
        # Skip header row
        if 'th_p' in row or 'Name' in row:
            continue

        # Extract cells
        cell_pattern = r'<td[^>]*>(.*?)</td>'
        cells = re.findall(cell_pattern, row, re.DOTALL)

        if len(cells) >= 3:
            name = re.sub(r'<[^>]+>', '', cells[0]).strip()
            explanation = re.sub(r'<[^>]+>', '', cells[1]).strip()
            datatype = re.sub(r'<[^>]+>', '', cells[2]).strip()

            if name and explanation and datatype:
                parameters.append({
                    "name": name,
                    "explanation": explanation,
                    "datatype": datatype
                })

    return parameters

def clean_parameter_name(name):
    """Clean parameter name to be a valid Python identifier"""
    # Remove (optional), brackets, special chars, and make lowercase with underscores
    clean = re.sub(r'\s*\([^)]*\)', '', name)  # Remove (optional)
    clean = re.sub(r'[\[\]]', '', clean)  # Remove brackets
    clean = re.sub(r'[^a-zA-Z0-9_]', '_', clean)  # Replace special chars with _
    clean = re.sub(r'_+', '_', clean)  # Multiple underscores to single
    clean = clean.strip('_').lower()  # Remove leading/trailing underscores and lowercase
    return clean

def generate_progent_function(tool_name, parameters, summary=""):
    """Generate a progent.pyt style function"""
    func_name = tool_name.lower().replace(' ', '_').replace('-', '_')

    # Build parameter extraction and validation
    param_lines = []
    required_params = []

    for i, param in enumerate(parameters):
        original_name = param["name"]
        clean_name = clean_parameter_name(original_name)

        # Check if parameter is required (doesn't contain "(Optional)")
        is_required = "(Optional)" not in original_name

        if is_required:
            required_params.append(clean_name)
            param_lines.append(f'    {clean_name} = params.get("{clean_name}")')
            param_lines.append(f'    if {clean_name} is None:')
            param_lines.append(f'        return {{"success": False, "error": "{clean_name} parameter is required"}}')
        else:
            param_lines.append(f'    {clean_name} = params.get("{clean_name}")')

    # Build arcpy call arguments
    arcpy_args = []
    for param in parameters:
        clean_name = clean_parameter_name(param["name"])
        arcpy_args.append(f'r"{{{clean_name}}}"')

    # Function template
    function = f'''    def {func_name}(self, params):
        """{tool_name}

{summary if summary else f'Execute {tool_name} geoprocessing tool.'}

        params: {{{', '.join([f'"{clean_parameter_name(p["name"])}": <{p["datatype"]}>' for p in parameters[:3]])}{', ...' if len(parameters) > 3 else ''}}}
        Returns: {{"success": True, "output_layer": <output_name>, "output_path": <output_path>}} or error
        """
        try:
{chr(10).join(param_lines)}

            # Generate output name and path
            output_name = f"{{{required_params[0] if required_params else 'params'}.replace(' ', '_')}}_{tool_name}"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute {tool_name}
            arcpy.{tool_name}({', '.join(arcpy_args)})

            self._add_to_map(output_path)
            return {{"success": True, "output_layer": output_name, "output_path": output_path}}

        except Exception as e:
            return {{"success": False, "error": str(e)}}
'''

    return function

def generate_ai_declaration(tool_name, parameters, summary=""):
    """Generate AI function declaration in the format used by function_declarations.py"""
    func_name = tool_name.lower().replace(' ', '_').replace('-', '_')

    # Build parameters dict
    params_dict = {}
    required = []

    for i, param in enumerate(parameters):
        param_name = clean_parameter_name(param["name"])
        original_name = param["name"]

        param_def = {
            "type": "string",  # Simplified - could map datatypes better
            "description": param["explanation"][:200] + "..." if len(param["explanation"]) > 200 else param["explanation"]
        }

        # Check if parameter is required (doesn't contain "(Optional)")
        is_required = "(Optional)" not in original_name

        if is_required:
            required.append(param_name)
        else:
            param_def["default"] = None

        params_dict[param_name] = param_def

    declaration = {
        "name": func_name,
        "description": summary if summary else f'Execute {tool_name} geoprocessing tool.',
        "parameters": params_dict,
        "required": required
    }

    return declaration

# Test with Buffer tool
print("Testing improved function generation with Buffer tool...")
url = "https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/buffer.htm"
html = fetch_page(url)
if html:
    summary = extract_summary_from_tool_page(html)
    parameters = extract_parameters_from_tool_page(html)

    print(f"Summary: {summary[:100]}{'...' if len(summary) > 100 else ''}")
    print(f"Parameters found: {len(parameters)}")
    for p in parameters[:3]:
        print(f"  - {p['name']} -> {clean_parameter_name(p['name'])} ({p['datatype']}): {p['explanation'][:50]}{'...' if len(p['explanation']) > 50 else ''}")

    print("\n" + "="*60)
    print("GENERATED PROGENT FUNCTION:")
    print("="*60)
    progent_func = generate_progent_function("Buffer", parameters, summary)
    print(progent_func)

    print("\n" + "="*60)
    print("GENERATED AI DECLARATION:")
    print("="*60)
    ai_decl = generate_ai_declaration("Buffer", parameters, summary)
    print(json.dumps(ai_decl, indent=2))
else:
    print("Failed to fetch Buffer tool page")