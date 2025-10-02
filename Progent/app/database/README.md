# ArcGIS Tools Database System

A SQLite-based RAG (Retrieval-Augmented Generation) system for ArcGIS geoprocessing tools that enables intelligent tool discovery and recommendation.

## Overview

This system solves the token limit problem when working with large numbers of ArcGIS tools (700+) by providing:

- **Keyword-based search** to find relevant tools before LLM calls
- **Relevance scoring** to rank tools by usefulness
- **Category filtering** for toolbox-specific queries
- **Similarity search** to find related tools
- **Scalable storage** ready for future vector embeddings

## Architecture

```
User Query → Query Preprocessing → Keyword Search → Relevance Scoring → Ranked Results
                                      ↓
Database (SQLite) ← Tool Declarations ← Population Script ← Jules Enhanced Files
```

## Database Schema

### Tables

1. **function_declarations**
   - `id`: Primary key
   - `function_name`: Tool function name (unique)
   - `declaration`: Full JSON declaration
   - `description`: Tool description
   - `toolbox_category`: Category (analysis, spatial_analyst, etc.)
   - `created_at/updated_at`: Timestamps

2. **keywords**
   - `id`: Primary key
   - `keyword`: Unique keyword text

3. **function_keywords** (junction table)
   - Links functions to their keywords
   - Includes relevance scores for future weighting

4. **function_examples**
   - Stores usage examples for each function

## Quick Start

### 1. Database Setup

```python
from app.database.database import ArcGISToolsDatabase

# Initialize database
db = ArcGISToolsDatabase()

# Insert a function declaration
declaration = {
    "name": "buffer",
    "description": "Create buffer zones around features",
    "parameters": {...},
    "keywords": ["buffer", "zone", "distance", "proximity"],
    "action_input_examples": [...]
}

db.insert_function_declaration("buffer", declaration, "analysis")
```

### 2. Unified Population (Load All Sources)

```bash
cd app/database

# Validate data sources before populating
python unified_populate.py --validate-only

# Populate from all sources (original + Jules' enhanced files)
python unified_populate.py --generated-path ../generated_functions

# Custom database path
python unified_populate.py --db-path app/database/arcgis_tools.db --generated-path ../generated_functions
```

### 3. Intelligent Search

```python
from app.database.retrieval import search_arcgis_tools

# Search for relevant tools
results = search_arcgis_tools("create buffer around roads", max_results=5)

for result in results:
    print(f"{result['function_name']}: {result['relevance_score']:.2f}")
    print(f"Description: {result['declaration']['description']}")
```

## API Reference

### ArcGISToolsDatabase

#### Methods

- `insert_function_declaration(name, declaration, category)` - Add/update tool
- `get_function_by_name(name)` - Get specific tool
- `search_functions_by_keywords(keywords, limit, min_matches)` - Keyword search
- `get_functions_by_category(category)` - Get tools by category
- `get_stats()` - Database statistics

### ArcGISToolsRetriever

#### Methods

- `search_relevant_tools(query, max_results, min_score)` - Intelligent search
- `get_tools_for_task(description, max_tools)` - Task-based search
- `get_similar_tools(function_name, limit)` - Find similar tools
- `explain_relevance(result, query)` - Explain why tool is relevant

### Convenience Functions

```python
from app.database.retrieval import (
    search_arcgis_tools,      # Main search function
    get_tool_declaration,     # Get specific tool
    get_tools_by_category     # Category search
)
```

## Usage Examples

### Basic Search

```python
# Natural language search
results = search_arcgis_tools("calculate slope from elevation data")

# Get top 3 results
for tool in results[:3]:
    print(f"🔧 {tool['function_name']}")
    print(f"📝 {tool['description']}")
    print(f"🎯 Relevance: {tool['relevance_score']:.2f}")
    print()
```

### Category-Specific Search

```python
# Get all spatial analyst tools
spatial_tools = get_tools_by_category("spatial_analyst")

# Search within category
terrain_tools = search_arcgis_tools("terrain analysis", max_results=10)
```

### Integration with AI Service

```python
# Before calling LLM, get relevant tools
user_query = "I need to buffer roads and calculate slope"
relevant_tools = search_arcgis_tools(user_query, max_results=5)

# Extract declarations for LLM context
tool_declarations = []
for tool in relevant_tools:
    if tool['relevance_score'] > 0.3:  # Filter by relevance
        tool_declarations.append(tool['declaration'])

# Now call LLM with focused context instead of 700+ tools
llm_response = call_llm_with_tools(user_query, tool_declarations)
```

## Data Sources & Deduplication

The system supports loading function declarations from multiple sources:

### Sources
1. **Original AI Functions** (`app/ai/function_declarations.py`)
   - Existing AI layer functions (dashboard, spatial analysis, etc.)
   - Enhanced with automatic keyword extraction

2. **Geoprocessing Tools** (`generated_functions/`)
   - Jules' enhanced ArcGIS toolbox functions
   - Already include keywords and examples

3. **Future Sources** - Extensible architecture

### Deduplication Strategy
- **Primary Key**: Function name uniqueness
- **Conflict Resolution**: First source wins (original functions prioritized)
- **Logging**: Tracks skipped duplicates and errors
- **Statistics**: Complete population metrics

### Population Process
```python
# Unified population handles all sources automatically
populator = UnifiedDatabasePopulator()
stats = populator.populate_from_all_sources("../generated_functions")

print(f"Loaded {stats['original_functions']} original + {stats['geoprocessing_functions']} geoprocessing tools")
print(f"Skipped {stats['duplicates_skipped']} duplicates")
```

## Testing

Run the test suite:

```bash
cd app/database

# Test database functionality
python test_database.py

# Test retrieval system
python test_retrieval.py
```

## Performance Characteristics

- **Database Size**: ~50MB for 700+ tools with examples and keywords
- **Search Speed**: <100ms for keyword searches
- **Scalability**: SQLite handles thousands of tools efficiently
- **Memory Usage**: Minimal - loads results on demand

## Future Enhancements

### Vector Search (Phase 2)
```python
# Planned: Semantic similarity search
similar_tools = retriever.semantic_search("create zones around points", top_k=5)
```

### Advanced Features
- **Tool chaining recommendations**
- **Parameter compatibility checking**
- **Usage pattern analysis**
- **Performance optimization suggestions**

## Dependencies

- `sqlite3` (built-in Python)
- No external packages required for basic functionality
- Optional: `sentence-transformers` for future vector search

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure correct Python path setup
2. **Database Locked**: Close all connections before operations
3. **No Results**: Check keyword matching and relevance thresholds

### Debug Mode

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Enable detailed logging
retriever = ArcGISToolsRetriever()
results = retriever.search_relevant_tools("buffer roads", max_results=5)
```

## Integration Checklist

- [ ] Database schema created
- [ ] Population script ready
- [ ] Retrieval system tested
- [ ] AI service integration planned
- [ ] Documentation complete
- [ ] Wait for Jules to enhance declarations
- [ ] Run population script
- [ ] Test end-to-end RAG system

---

**Status**: Ready for integration. Waiting for Jules to complete function declaration enhancements before database population.