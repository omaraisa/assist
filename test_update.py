import sys
import os
import json

# Change to the Progent directory
os.chdir('Progent')
sys.path.insert(0, '.')

from app.progent_functions import add_dashboard_charts, get_current_dashboard_charts, update_dashboard_charts

print('=== Adding test charts ===')
result = add_dashboard_charts([
    {'fields': ['DistrictID'], 'chart_type': 'histogram'},
    {'fields': ['operator'], 'chart_type': 'bar'}
])
print(json.dumps(result, indent=2))

print('\n=== Getting current charts ===')
result = get_current_dashboard_charts()
print(json.dumps(result, indent=2))

print('\n=== Updating chart at index 0 ===')
result = update_dashboard_charts([{
    'index': 0, 
    'chart': {'fields': ['DistrictID'], 'chart_type': 'pie'}
}])
print(json.dumps(result, indent=2))

print('\n=== Getting charts after update ===')
result = get_current_dashboard_charts()
print(json.dumps(result, indent=2))
