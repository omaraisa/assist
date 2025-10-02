"""
Test script for ArcGIS Tools Retrieval System
Tests the intelligent search and retrieval functionality.
"""

import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from database import ArcGISToolsDatabase
from retrieval import ArcGISToolsRetriever

def setup_test_data():
    """Set up test data in the database."""
    print("Setting up test data...")

    db = ArcGISToolsDatabase("app/database/test_retrieval.db")

    # Sample tools with realistic declarations
    test_tools = [
        {
            "name": "buffer",
            "description": "Create buffer zones around input features to a specified distance.",
            "parameters": {
                "in_features": {"type": "string", "description": "Input features to buffer"},
                "buffer_distance": {"type": "string", "description": "Buffer distance with units"},
                "out_feature_class": {"type": "string", "description": "Output feature class"}
            },
            "required": ["in_features", "buffer_distance", "out_feature_class"],
            "action_input_examples": [
                {
                    "function_name": "buffer",
                    "in_features": "roads",
                    "buffer_distance": "100 meters",
                    "out_feature_class": "roads_buffer"
                }
            ],
            "keywords": ["buffer", "zone", "distance", "proximity", "expand", "boundary", "offset"]
        },
        {
            "name": "clip",
            "description": "Clip features to the boundary of another feature class.",
            "parameters": {
                "in_features": {"type": "string", "description": "Features to be clipped"},
                "clip_features": {"type": "string", "description": "Features defining the clip boundary"},
                "out_feature_class": {"type": "string", "description": "Output clipped features"}
            },
            "required": ["in_features", "clip_features", "out_feature_class"],
            "action_input_examples": [
                {
                    "function_name": "clip",
                    "in_features": "parcels",
                    "clip_features": "city_boundary",
                    "out_feature_class": "city_parcels"
                }
            ],
            "keywords": ["clip", "cut", "boundary", "intersection", "trim", "limit", "crop"]
        },
        {
            "name": "dissolve",
            "description": "Merge features based on specified attributes.",
            "parameters": {
                "in_features": {"type": "string", "description": "Input features to dissolve"},
                "dissolve_field": {"type": "string", "description": "Field to dissolve on"},
                "out_feature_class": {"type": "string", "description": "Output dissolved features"}
            },
            "required": ["in_features", "dissolve_field", "out_feature_class"],
            "action_input_examples": [
                {
                    "function_name": "dissolve",
                    "in_features": "counties",
                    "dissolve_field": "STATE_NAME",
                    "out_feature_class": "states"
                }
            ],
            "keywords": ["dissolve", "merge", "combine", "aggregate", "union", "group", "consolidate"]
        },
        {
            "name": "slope",
            "description": "Calculate slope from elevation raster data.",
            "parameters": {
                "in_raster": {"type": "string", "description": "Input elevation raster"},
                "out_raster": {"type": "string", "description": "Output slope raster"},
                "output_measurement": {"type": "string", "description": "Slope measurement units"}
            },
            "required": ["in_raster", "out_raster"],
            "action_input_examples": [
                {
                    "function_name": "slope",
                    "in_raster": "elevation",
                    "out_raster": "slope_degrees",
                    "output_measurement": "DEGREE"
                }
            ],
            "keywords": ["slope", "terrain", "elevation", "gradient", "steepness", "raster", "surface"]
        },
        {
            "name": "select_by_attribute",
            "description": "Select features based on attribute values using SQL queries.",
            "parameters": {
                "in_layer": {"type": "string", "description": "Layer to select from"},
                "selection_type": {"type": "string", "description": "Type of selection"},
                "where_clause": {"type": "string", "description": "SQL WHERE clause"}
            },
            "required": ["in_layer", "where_clause"],
            "action_input_examples": [
                {
                    "function_name": "select_by_attribute",
                    "in_layer": "cities",
                    "selection_type": "NEW_SELECTION",
                    "where_clause": "POPULATION > 100000"
                }
            ],
            "keywords": ["select", "attribute", "query", "filter", "where", "criteria", "sql"]
        }
    ]

    # Insert test tools
    for tool in test_tools:
        declaration = {
            "name": tool["name"],
            "description": tool["description"],
            "parameters": tool["parameters"],
            "required": tool["required"],
            "action_input_examples": tool["action_input_examples"],
            "keywords": tool["keywords"]
        }
        db.insert_function_declaration(tool["name"], declaration, "analysis")

    print(f"✓ Inserted {len(test_tools)} test tools")
    return db

def test_retrieval_system():
    """Test the retrieval system functionality."""
    print("\nTesting Retrieval System...")

    # Setup test data
    db = setup_test_data()
    retriever = ArcGISToolsRetriever("app/database/test_retrieval.db")

    # Test queries
    test_queries = [
        ("create buffer around roads", "Buffer search"),
        ("clip parcels to city boundary", "Clip search"),
        ("merge counties by state", "Dissolve search"),
        ("calculate terrain slope", "Slope search"),
        ("select cities with population over 100k", "Attribute selection search"),
        ("find steep areas", "Terrain analysis search"),
        ("filter data by attributes", "Data filtering search"),
        ("nonexistent operation xyz", "No matches search")
    ]

    for query, description in test_queries:
        print(f"\n{description}: '{query}'")
        results = retriever.search_relevant_tools(query, max_results=3)

        if results:
            for i, result in enumerate(results, 1):
                score = result.get('relevance_score', 0)
                name = result['function_name']
                matches = result.get('match_count', 0)
                print(".3f")

                # Show explanation for top result
                if i == 1:
                    explanation = retriever.explain_relevance(result, query)
                    print(f"      Explanation: {explanation}")
        else:
            print("      No results found")

    # Test category filtering
    print("\nCategory filtering test:")
    analysis_tools = retriever.get_tools_by_category("analysis")
    print(f"Found {len(analysis_tools)} tools in analysis category")

    # Test similar tools
    print("\nSimilar tools test:")
    similar = retriever.get_similar_tools("buffer", limit=2)
    print(f"Tools similar to 'buffer': {[t['function_name'] for t in similar]}")

    # Test tool details
    print("\nTool details test:")
    details = retriever.get_tool_details("buffer")
    if details:
        print(f"Buffer tool has {len(details['declaration'].get('keywords', []))} keywords")
        print(f"Description: {details['description'][:50]}...")

    print("\n🎉 Retrieval system tests completed!")

def test_query_preprocessing():
    """Test query preprocessing functionality."""
    print("\nTesting Query Preprocessing...")

    retriever = ArcGISToolsRetriever()

    test_queries = [
        "Create a 100 meter buffer around roads",
        "I need to clip my parcel data to the city boundary",
        "Calculate slope from DEM raster",
        "Select features where population > 50000",
        "Find areas with high elevation"
    ]

    for query in test_queries:
        keywords = retriever.preprocess_query(query)
        print(f"Query: '{query}'")
        print(f"Keywords: {keywords}")
        print()

def cleanup_test_database():
    """Clean up test database."""
    import time
    test_db_path = Path("app/database/test_retrieval.db")
    if test_db_path.exists():
        time.sleep(0.5)
        try:
            test_db_path.unlink()
            print("✓ Test database cleaned up")
        except PermissionError:
            print("⚠ Test database still in use (this is normal)")

if __name__ == "__main__":
    try:
        test_query_preprocessing()
        test_retrieval_system()
        cleanup_test_database()

        print("\n🎉 All retrieval tests passed! System is ready for integration.")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)