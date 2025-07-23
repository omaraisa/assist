from app.spatial_functions import SpatialFunctions
import json
import os

# Show the enhanced AI prompt
if os.path.exists('smart_dashboard.json'):
    with open('smart_dashboard.json', 'r', encoding='utf-8') as f:
        dashboard_data = json.load(f)
    
    field_insights = dashboard_data.get('field_insights', {})
    sf = SpatialFunctions()
    
    filter_result = sf._filter_relevant_fields(field_insights)
    relevant_fields = filter_result["filtered_insights"]
    relationships = sf._analyze_field_relationships(relevant_fields)
    summaries = sf._create_field_summaries(relevant_fields)
    
    enhanced_prompt = sf._build_enhanced_chart_recommendation_prompt(
        summaries, relationships, None
    )
    
    print("=== ENHANCED AI PROMPT PREVIEW ===")
    print(enhanced_prompt)
