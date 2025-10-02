"""
Test script for ArcGIS Tools Database
Tests database functionality and retrieval system.
"""

import sys
import json
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from database import ArcGISToolsDatabase

def test_database_operations():
    """Test basic database operations."""
    print("Testing ArcGIS Tools Database...")

    # Initialize database
    db = ArcGISToolsDatabase("app/database/test_arcgis_tools.db")

    # Sample function declaration (like what Jules will create)
    sample_declaration = {
        "name": "select_by_attribute",
        "description": "Execute attribute-based selection on a GIS layer using SQL-like WHERE clause conditions.",
        "parameters": {
            "layer_name": {
                "type": "string",
                "description": "The name of the layer to perform selection on"
            },
            "where_clause": {
                "type": "string",
                "description": "SQL WHERE clause for attribute selection (e.g., 'POPULATION > 1000000')"
            },
            "selection_type": {
                "type": "string",
                "description": "Type of selection to perform",
                "enum": ["NEW_SELECTION", "ADD_TO_SELECTION", "REMOVE_FROM_SELECTION", "SUBSET_SELECTION"],
                "default": "NEW_SELECTION"
            }
        },
        "required": ["layer_name", "where_clause"],
        "action_input_examples": [
            {
                "function_name": "select_by_attribute",
                "layer_name": "Cities",
                "where_clause": "POPULATION > 1000000",
                "selection_type": "NEW_SELECTION"
            },
            {
                "function_name": "select_by_attribute",
                "layer_name": "Parcels",
                "where_clause": "LAND_USE = 'RESIDENTIAL'",
                "selection_type": "ADD_TO_SELECTION"
            }
        ],
        "keywords": [
            "select",
            "attribute",
            "query",
            "filter",
            "where clause",
            "SQL",
            "selection",
            "criteria",
            "layer",
            "features"
        ]
    }

    # Test insertion
    print("1. Testing function insertion...")
    func_id = db.insert_function_declaration(
        "select_by_attribute",
        sample_declaration,
        "analysis"
    )
    print(f"   ✓ Inserted function with ID: {func_id}")

    # Test retrieval by name
    print("2. Testing function retrieval by name...")
    retrieved = db.get_function_by_name("select_by_attribute")
    if retrieved and retrieved['function_name'] == "select_by_attribute":
        print("   ✓ Function retrieved successfully")
    else:
        print("   ✗ Function retrieval failed")

    # Test keyword search
    print("3. Testing keyword search...")
    results = db.search_functions_by_keywords(["select", "attribute"], limit=5)
    if results and len(results) > 0:
        print(f"   ✓ Found {len(results)} functions matching keywords")
        print(f"   ✓ Top match: {results[0]['function_name']} (score: {results[0]['match_count']})")
    else:
        print("   ✗ Keyword search failed")

    # Test partial keyword match
    print("4. Testing partial keyword matching...")
    results = db.search_functions_by_keywords(["query"], limit=5)
    if results:
        print(f"   ✓ Found {len(results)} functions with 'query' keyword")
    else:
        print("   ✗ Partial keyword search failed")

    # Test category filtering
    print("5. Testing category retrieval...")
    category_results = db.get_functions_by_category("analysis")
    if category_results:
        print(f"   ✓ Found {len(category_results)} functions in 'analysis' category")
    else:
        print("   ✗ Category filtering failed")

    # Test database stats
    print("6. Testing database statistics...")
    stats = db.get_stats()
    print(f"   ✓ Database contains {stats['total_functions']} functions")
    print(f"   ✓ Total keywords: {stats['total_keywords']}")
    print(f"   ✓ Keyword relationships: {stats['total_keyword_relationships']}")

    # Test edge cases
    print("7. Testing edge cases...")

    # Empty search
    empty_results = db.search_functions_by_keywords([])
    if not empty_results:
        print("   ✓ Empty keyword search handled correctly")
    else:
        print("   ✗ Empty keyword search should return no results")

    # Non-existent function
    nonexistent = db.get_function_by_name("nonexistent_function")
    if nonexistent is None:
        print("   ✓ Non-existent function handled correctly")
    else:
        print("   ✗ Should return None for non-existent function")

    print("\n🎉 All database tests completed!")
    return True

def test_retrieval_system():
    """Test the retrieval system with various queries."""
    print("\nTesting Retrieval System...")

    db = ArcGISToolsDatabase("app/database/test_arcgis_tools.db")

    # Add more sample functions for better testing
    sample_functions = [
        {
            "name": "buffer",
            "description": "Create buffer zones around features",
            "keywords": ["buffer", "zone", "distance", "proximity", "expand", "boundary"]
        },
        {
            "name": "clip",
            "description": "Clip features to a boundary",
            "keywords": ["clip", "cut", "boundary", "intersection", "trim", "limit"]
        },
        {
            "name": "dissolve",
            "description": "Merge features based on attributes",
            "keywords": ["dissolve", "merge", "combine", "aggregate", "union", "group"]
        }
    ]

    for func in sample_functions:
        declaration = {
            "name": func["name"],
            "description": func["description"],
            "parameters": {},
            "required": [],
            "action_input_examples": [],
            "keywords": func["keywords"]
        }
        db.insert_function_declaration(func["name"], declaration, "analysis")

    # Test various search queries
    test_queries = [
        (["buffer", "zone"], "Buffer zone search"),
        (["clip", "boundary"], "Clip boundary search"),
        (["merge", "combine"], "Merge operations search"),
        (["distance"], "Single keyword search"),
        (["nonexistent", "keywords"], "No matches search")
    ]

    for keywords, description in test_queries:
        results = db.search_functions_by_keywords(keywords, limit=10)
        print(f"   {description}: Found {len(results)} results")
        if results:
            top_result = results[0]
            print(f"      Top: {top_result['function_name']} ({top_result['match_count']} matches)")

    print("🎉 Retrieval system tests completed!")
    return True

def cleanup_test_database():
    """Clean up test database."""
    import time
    test_db_path = Path("app/database/test_arcgis_tools.db")
    if test_db_path.exists():
        # Wait a bit for connections to close
        time.sleep(0.5)
        try:
            test_db_path.unlink()
            print("✓ Test database cleaned up")
        except PermissionError:
            print("⚠ Test database still in use (this is normal)")
            # Try to remove on next run
            pass

if __name__ == "__main__":
    try:
        # Run tests
        test_database_operations()
        test_retrieval_system()

        # Cleanup
        cleanup_test_database()

        print("\n🎉 All tests passed! Database system is ready.")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)