#!/usr/bin/env python3
"""
ArcGIS Pro Analysis Tools Documentation Scraper

This script scrapes the ArcGIS Pro documentation to:
1. Discover all toolsets in the Analysis toolbox
2. Discover all tools in each toolset
3. Fetch parameter information from each tool's help page
4. Generate Python function declarations

No ArcPy dependency - runs standalone.
"""

import urllib.request
import json
import re
from datetime import datetime
import time
import argparse
import os


def fetch_page(url):
    """Fetch a webpage with error handling"""
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_toolsets_from_analysis_overview(html):
    """Extract toolset names from the analysis toolbox overview page"""
    toolsets = []

    # Look for the table content
    # The toolsets are listed in a table format
    lines = html.split('\n')

    in_table = False
    for line in lines:
        line = line.strip()
        if '| Extract |' in line or '| General |' in line:
            in_table = True
        if in_table and line.startswith('| ') and ' | ' in line:
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if len(parts) >= 1:
                toolset_name = parts[0]
                if toolset_name and toolset_name not in ['Extract', 'General', 'Overlay', 'Pairwise Overlay', 'Proximity', 'Statistics']:
                    continue  # Skip if not a known toolset
                toolsets.append(toolset_name)

    # Fallback: hardcoded list based on the page
    if not toolsets:
        toolsets = [
            'Extract',
            'General',
            'Overlay',
            'Pairwise Overlay',
            'Proximity',
            'Statistics'
        ]

    return toolsets

def extract_tools_from_toolset_overview(html, toolset_name):
    """Extract tool names from a toolset overview page"""
    tools = []

    print(f"    DEBUG: HTML length: {len(html)}")
    
    # Look for table content - try different approaches
    import re
    
    # Look for table rows with tool names
    # Pattern: <td>Tool Name</td><td>Description</td>
    td_pattern = r'<td[^>]*>([^<]+)</td>'
    matches = re.findall(td_pattern, html)
    
    print(f"    DEBUG: Found {len(matches)} <td> matches")
    for i, match in enumerate(matches[:20]):
        print(f"    DEBUG: TD {i}: {repr(match)}")
    
    # Look for specific tool names (fallback if links aren't present)
    known_tools = ['Clip', 'Select', 'Split', 'Split By Attributes', 'Table Select']
    for tool in known_tools:
        if tool in html and not any(t.get('name') == tool for t in tools):
            tools.append({"name": tool, "href": None})
            print(f"    DEBUG: Found known tool: {tool}")
    
    # Also try to find links to tool pages
    link_pattern = r'href="([^"]*\.htm)"[^>]*>([^<]+)</a>'
    links = re.findall(link_pattern, html)
    print(f"    DEBUG: Found {len(links)} links")
    for href, text in links:
        text = text.strip()
        if not text:
            continue
        # Skip links that point to the toolbox overview itself
        if text.lower().startswith('an overview') or 'toolbox' in text.lower() or 'toolset' in text.lower():
            continue
        # Normalize href
        href_val = href
        # Add full URL if relative
        if href_val.startswith('/'):
            href_val = 'https://pro.arcgis.com' + href_val
        elif href_val.startswith('http'):
            href_val = href_val
        else:
            # Relative to current toolbox path
            href_val = 'https://pro.arcgis.com/en/pro-app/latest/tool-reference/' + href_val.lstrip('./')

        tools.append({"name": text, "href": href_val})
        print(f"    DEBUG: Link: {href_val} -> {text}")

    # Deduplicate by name preserving first occurrence
    seen = set()
    dedup = []
    for t in tools:
        name = t['name'] if isinstance(t, dict) else t
        if name not in seen:
            seen.add(name)
            dedup.append(t)

    print(f"    DEBUG: Final tools: {[d['name'] for d in dedup]}")
    return dedup

def generate_tool_help_url(tool_name):
    """Generate the help URL for a tool"""
    # Convert tool name to URL slug
    slug = tool_name.lower().replace(' ', '-').replace('_', '-')
    # default to analysis toolbox; callers may override
    return f"https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/{slug}.htm"

def generate_toolset_overview_url(toolset_name):
    """Generate the overview URL for a toolset"""
    slug = toolset_name.lower().replace(' ', '-')
    return f"https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/an-overview-of-the-{slug}-toolset.htm"

def generate_toolset_overview_url_for_toolbox(toolbox_slug):
    """Generate the overview URL for a toolbox slug (e.g., cartography).

    Some toolboxes use '-toolbox' in the overview page name (for example cartography),
    so prefer '-toolbox' suffix.
    """
    return f"https://pro.arcgis.com/en/pro-app/latest/tool-reference/{toolbox_slug}/an-overview-of-the-{toolbox_slug}-toolbox.htm"

def generate_tool_help_url_for_toolbox(toolbox_slug, tool_name):
    slug = tool_name.lower().replace(' ', '-').replace('_', '-')
    return f"https://pro.arcgis.com/en/pro-app/latest/tool-reference/{toolbox_slug}/{slug}.htm"

def extract_summary_from_tool_page(html):
    """Extract the Summary section from a tool's help page"""
    # Find the Summary section
    summary_start = html.find('<div class="section1 summary')
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
            # Extract name - take only the first line or main text
            name_cell = cells[0]
            # Remove HTML tags and get the main parameter name
            name = re.sub(r'<[^>]+>', '', name_cell).strip()
            # Take only the first part before any line breaks or additional text
            name = name.split('\n')[0].split('<')[0].strip()

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
    clean = re.sub(r'\s*\([^)]*\)', '', name)  # Remove (optional) and other parentheses
    clean = re.sub(r'[\[\]]', '', clean)  # Remove brackets
    clean = re.sub(r'[^a-zA-Z0-9_]', '_', clean)  # Replace special chars with _
    clean = re.sub(r'_+', '_', clean)  # Multiple underscores to single
    clean = clean.strip('_').lower()  # Remove leading/trailing underscores and lowercase

    # Additional cleaning: remove repeated patterns that might appear due to HTML formatting
    # Handle cases like "split_fieldssplit_fields" -> "split_fields"
    # Collapse repeated adjacent substrings (length >=3)
    try:
        clean = re.sub(r'(.{3,}?)(?:\1)+', r'\1', clean)
    except re.error:
        pass

    # Remove consecutive duplicate underscore-delimited tokens
    tokens = clean.split('_') if clean else []
    dedup_tokens = []
    prev = None
    for t in tokens:
        if not t:
            continue
        if t == prev:
            # skip exact duplicate
            continue
        dedup_tokens.append(t)
        prev = t
    if dedup_tokens:
        clean = '_'.join(dedup_tokens)

    # Final cleanup
    clean = clean.strip('_')
    if not clean:
        clean = 'unnamed_param'

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
            param_lines.append(f'        {clean_name} = params.get("{clean_name}")')
            param_lines.append(f'        if {clean_name} is None:')
            param_lines.append(f'            return {{"success": False, "error": "{clean_name} parameter is required"}}')
        else:
            param_lines.append(f'        {clean_name} = params.get("{clean_name}")')

    # Build arcpy call arguments - pass variables directly
    arcpy_args = []
    for param in parameters:
        clean_name = clean_parameter_name(param["name"])
        arcpy_args.append(clean_name)

    # Convert tool name to valid ArcPy function name (remove spaces)
    arcpy_tool_name = tool_name.replace(' ', '').replace('-', '')

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
            output_name = f"{{{required_params[0] if required_params else 'params'}.replace(' ', '_')}}_{tool_name.replace(' ', '_')}"
            aprx = arcpy.mp.ArcGISProject("CURRENT")
            output_path = os.path.join(aprx.defaultGeodatabase, output_name)
            output_path = arcpy.CreateUniqueName(output_path)

            # Execute {tool_name}
            arcpy.{arcpy_tool_name}({', '.join(arcpy_args)})

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

def generate_function_declaration(tool_name, parameters, summary=""):
    """Generate both progent function and AI declaration"""
    progent_func = generate_progent_function(tool_name, parameters, summary)
    ai_decl = generate_ai_declaration(tool_name, parameters, summary)

    return progent_func, ai_decl

def main():
    parser = argparse.ArgumentParser(description="ArcGIS Pro toolbox documentation scraper")
    parser.add_argument('--toolbox', default='cartography', help='Toolbox slug to scrape (e.g., cartography, conversion, data-management)')
    parser.add_argument('--outdir', default=os.path.join(os.path.dirname(__file__), 'generated_functions'), help='Output base directory')
    args = parser.parse_args()

    toolbox_slug = args.toolbox
    outdir = args.outdir

    print(f"ArcGIS Pro toolbox documentation scraper for toolbox: {toolbox_slug}")
    print("=" * 60)

    # Step 1: Get toolbox overview page
    if toolbox_slug == 'analysis':
        overview_url = "https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/an-overview-of-the-analysis-toolbox.htm"
    else:
        overview_url = generate_toolset_overview_url_for_toolbox(toolbox_slug)

    html = fetch_page(overview_url)
    if not html:
        print(f"Failed to fetch overview page: {overview_url}")
        return

    # For analysis toolbox, extract toolsets; for other toolboxes, treat overview as listing tools
    all_tools = {}
    total_tools = 0

    if toolbox_slug == 'analysis':
        toolsets = extract_toolsets_from_analysis_overview(html)
        print(f"Found {len(toolsets)} toolsets: {', '.join(toolsets)}")
        print("\n2. Discovering tools in each toolset...")
        for toolset in toolsets:
            print(f"\n  Processing {toolset} toolset...")
            toolset_url = generate_toolset_overview_url(toolset)
            t_html = fetch_page(toolset_url)
            if not t_html:
                print(f"    Failed to fetch {toolset} overview")
                continue
            tools = extract_tools_from_toolset_overview(t_html, toolset)
            all_tools[toolset] = tools
            total_tools += len(tools)
            print(f"    Found {len(tools)} tools: {', '.join(tools)}")
    else:
        # For non-analysis toolboxes the overview page typically lists the tools directly
        tools = extract_tools_from_toolset_overview(html, toolbox_slug)

        # Expand toolset overview links (many toolboxes list toolsets first)
        expanded_tools = []
        for t in tools:
            if isinstance(t, dict) and t.get('href') and 'an-overview-of-' in t.get('href'):
                # This is likely a toolset overview; fetch and extract tools from it
                print(f"  Expanding toolset {t.get('name')} -> {t.get('href')}")
                t_html = fetch_page(t.get('href'))
                if not t_html:
                    print(f"    Failed to fetch toolset page: {t.get('href')}")
                    continue
                sub_tools = extract_tools_from_toolset_overview(t_html, t.get('name'))
                # sub_tools are dicts with hrefs or names
                expanded_tools.extend(sub_tools)
                # be polite
                time.sleep(0.3)
            else:
                expanded_tools.append(t)

        all_tools[toolbox_slug] = expanded_tools
        total_tools = len(expanded_tools)
        print(f"Found {total_tools} tools in toolbox {toolbox_slug}")

    print(f"\nTotal tools discovered: {total_tools}")

    # Step 3: For each tool, fetch parameters and generate declarations
    print("\n3. Fetching tool documentation and generating declarations...")
    progent_functions = []
    ai_declarations = []
    tool_metadata = []

    for toolset, tools in all_tools.items():
        print(f"\n  Processing {toolset} ({len(tools)} tools)...")

        for i, tool in enumerate(tools, 1):
            # tool can be a dict {name, href} or a plain name
            if isinstance(tool, dict):
                tool_name = tool.get('name')
                tool_href = tool.get('href')
            else:
                tool_name = tool
                tool_href = None

            print(f"    [{i}/{len(tools)}] {tool_name}")

            # help page URL per toolbox
            if toolbox_slug == 'analysis':
                help_url = generate_tool_help_url(tool_name)
            else:
                # If link was discovered on the overview page, use that href
                if tool_href:
                    help_url = tool_href
                else:
                    help_url = generate_tool_help_url_for_toolbox(toolbox_slug, tool_name)

            # Fetch page
            t_html = fetch_page(help_url)
            if not t_html:
                print(f"      Failed to fetch {help_url}")
                continue

            # Extract summary
            summary = extract_summary_from_tool_page(t_html)
            print(f"      Summary: {summary[:100]}{'...' if len(summary) > 100 else ''}")
            
            # Extract parameters
            parameters = extract_parameters_from_tool_page(t_html)
            print(f"      Extracted {len(parameters)} parameters")

            # Generate both function formats
            if parameters:
                progent_func, ai_decl = generate_function_declaration(tool_name, parameters, summary)
                progent_functions.append(progent_func)
                ai_declarations.append(ai_decl)

            # Store metadata
            tool_metadata.append({
                "toolset": toolset,
                "tool_name": tool_name,
                "help_url": help_url,
                "parameters": parameters,
                "summary": summary,
                "extraction_date": datetime.now().isoformat()
            })

            # Small delay to be respectful
            time.sleep(0.5)

    # Step 4: Save results into per-toolbox output folder
    print("\n4. Saving results...")

    toolbox_outdir = os.path.join(outdir, toolbox_slug)
    os.makedirs(toolbox_outdir, exist_ok=True)

    # Save progent functions
    progent_path = os.path.join(toolbox_outdir, 'generated_progent_functions.py')
    with open(progent_path, 'w', encoding='utf-8') as f:
        f.write(f"# Generated ArcGIS Pro {toolbox_slug} Progent Functions\n")
        f.write(f"# Generated on {datetime.now().isoformat()}\n")
        f.write(f"# Total tools: {len(progent_functions)}\n\n")
        f.write("import arcpy\n")
        f.write("import os\n\n")
        f.write("class GeneratedSpatialFunctions:\n")
        f.write("    \"\"\"Generated spatial analysis functions in progent.pyt format\"\"\"\n\n")
        f.write("    def _add_to_map(self, path):\n")
        f.write("        try:\n")
        f.write("            aprx = arcpy.mp.ArcGISProject('CURRENT')\n")
        f.write("            map_obj = aprx.activeMap\n")
        f.write("            map_obj.addDataFromPath(path)\n")
        f.write("        except Exception as e:\n")
        f.write("            print(f'Could not add {path} to map: {e}')\n\n")
        f.write("\n\n".join(progent_functions))

    # Save AI declarations
    ai_path = os.path.join(toolbox_outdir, 'generated_ai_declarations.py')
    with open(ai_path, 'w', encoding='utf-8') as f:
        f.write(f"# Generated ArcGIS Pro {toolbox_slug} AI Function Declarations\n")
        f.write(f"# Generated on {datetime.now().isoformat()}\n")
        f.write(f"# Total tools: {len(ai_declarations)}\n\n")
        f.write("functions_declarations = {\n")
        for i, decl in enumerate(ai_declarations):
            func_name = decl['name']
            f.write(f'    "{func_name}": ')
            json.dump(decl, f, indent=8)
            if i < len(ai_declarations) - 1:
                f.write(',\n')
            else:
                f.write('\n')
        f.write('}\n')

    # Save metadata
    metadata_path = os.path.join(toolbox_outdir, 'tools_metadata.json')
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump({
            "extraction_info": {
                "date": datetime.now().isoformat(),
                "total_toolsets": len(all_tools),
                "total_tools": len(progent_functions),
                "toolbox": toolbox_slug
            },
            "tools": tool_metadata
        }, f, indent=2, ensure_ascii=False)

    print("Progent functions saved to:", progent_path)
    print("AI declarations saved to:", ai_path)
    print("Metadata saved to:", metadata_path)
    print(f"Successfully processed {len(progent_functions)} tools with parameters")


if __name__ == "__main__":
    main()