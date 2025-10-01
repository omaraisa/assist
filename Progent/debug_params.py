#!/usr/bin/env python3
"""
Debug parameter names
"""

import urllib.request
import json
import re

def fetch_page(url):
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        return None

def extract_parameters_from_tool_page(html):
    parameters = []
    python_start = html.find('<a class="tab-title js-tab gptab" val="python">Python</a>')
    if python_start == -1:
        return parameters
    python_article_start = html.find('<article class="tab-section js-tab-section">', python_start)
    if python_article_start == -1:
        return parameters
    python_article_end = html.find('</article>', python_article_start)
    if python_article_end == -1:
        python_article_end = len(html)
    python_section = html[python_article_start:python_article_end]
    table_start = python_section.find('<table class="gptoolparamtbl">')
    if table_start == -1:
        return parameters
    table_end = python_section.find('</table>', table_start)
    if table_end == -1:
        table_end = len(python_section)
    table_html = python_section[table_start:table_end]
    row_pattern = r'<tr[^>]*>(.*?)</tr>'
    rows = re.findall(row_pattern, table_html, re.DOTALL)
    for row in rows:
        if 'th_p' in row or 'Name' in row:
            continue
        cell_pattern = r'<td[^>]*>(.*?)</td>'
        cells = re.findall(cell_pattern, row, re.DOTALL)
        if len(cells) >= 3:
            name = re.sub(r'<[^>]+>', '', cells[0]).strip()
            explanation = re.sub(r'<[^>]+>', '', cells[1]).strip()
            datatype = re.sub(r'<[^>]+>', '', cells[2]).strip()
            if name and explanation and datatype:
                parameters.append({
                    'name': name,
                    'explanation': explanation,
                    'datatype': datatype
                })
    return parameters

url = 'https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/buffer.htm'
html = fetch_page(url)
if html:
    parameters = extract_parameters_from_tool_page(html)
    print('Raw parameter names from HTML:')
    for i, p in enumerate(parameters):
        has_optional = '(Optional)' in p['name']
        print(f'{i+1}. "{p["name"]}" - contains "(Optional)": {has_optional}')