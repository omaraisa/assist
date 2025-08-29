import sys
import os
import json

# Change to the Progent directory
os.chdir('Progent')
sys.path.insert(0, '.')

from app.progent_functions import get_current_dashboard_layout, update_dashboard_layout

print('=== Current Layout Before Update ===')
result = get_current_dashboard_layout()
print(json.dumps(result, indent=2))

print('\n=== Updating Layout (Moving first chart to end) ===')
update_result = update_dashboard_layout({
    "items": [
        {"id": "chart_operator", "grid_area": "chart-1"},
        {"id": "chart_Long", "grid_area": "chart-2"},
        {"id": "chart_DistrictID", "grid_area": "chart-3"}
    ]
})
print(json.dumps(update_result, indent=2))

print('\n=== Current Layout After Update ===')
result = get_current_dashboard_layout()
print(json.dumps(result, indent=2))
