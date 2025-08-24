import json
from app.progent_functions import update_dashboard_charts, get_current_dashboard_charts

print('CURRENT:', json.dumps(get_current_dashboard_charts(), indent=2, ensure_ascii=False))

charts = [
    {
        "index": 4,
    # Place category first, then numeric fields; explicitly set primary_field
    "fields": ["operator", "gallons_sold_july_91", "gallons_sold_july_95"],
    "primary_field": "gallons_sold_july_91",
    "chart_type": "bar",
    "category_field": "operator"
    }
]

res = update_dashboard_charts(charts)
print('RES:', json.dumps(res, indent=2, ensure_ascii=False))

print('AFTER:', json.dumps(get_current_dashboard_charts(), indent=2, ensure_ascii=False))
I 