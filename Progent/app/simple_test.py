import json
from pathlib import Path

# Test the core dashboard transformation logic without FastAPI dependencies
def test_dashboard_parsing():
    dashboard_file = Path('../progent_dashboard.json')
    with open(dashboard_file, 'r', encoding='utf-8') as f:
        dashboard_data = json.load(f)

    print('Dashboard data loaded successfully')
    print('Charts count:', len(dashboard_data.get('charts', [])))

    # Check for aggregation charts
    charts = dashboard_data.get('charts', [])
    has_aggregation = any(chart.get('data_category') == 'aggregation' for chart in charts)
    print('Has aggregation charts:', has_aggregation)

    if has_aggregation:
        aggregation_charts = [chart for chart in charts if chart.get('data_category') == 'aggregation']
        print('Aggregation charts found:', len(aggregation_charts))
        for chart in aggregation_charts:
            print(f'  - {chart.get("title", "Unknown")}')
            agg_info = chart.get('aggregation_info', {})
            if agg_info:
                print(f'    Numeric field: {agg_info.get("numeric_field", "N/A")}')
                print(f'    Category field: {agg_info.get("category_field", "N/A")}')
                data = agg_info.get('data', {})
                if data:
                    print(f'    Data points: {len(data.get("labels", []))}')

    return dashboard_data

if __name__ == '__main__':
    test_dashboard_parsing()
