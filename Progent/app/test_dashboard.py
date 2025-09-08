# import sys
# import os
# sys.path.append(os.path.dirname(__file__))

from .main import transform_dashboard_for_frontend
import json
from pathlib import Path

# Load and test the dashboard transformation
# The path is relative to the Progent directory, where the test is run from.
dashboard_file = Path('progent_dashboard.json')
with open(dashboard_file, 'r', encoding='utf-8') as f:
    dashboard_data = json.load(f)

print('Testing dashboard transformation...')
result = transform_dashboard_for_frontend(dashboard_data)

if 'error' in result:
    print('ERROR:', result['error'])
else:
    print('SUCCESS: Dashboard transformed')
    print('Charts count:', len(result.get('charts', [])))
    if result.get('charts'):
        print('First chart type:', result['charts'][0].get('type'))
        print('First chart x_field:', result['charts'][0].get('x_field'))
        print('First chart y_field:', result['charts'][0].get('y_field'))
