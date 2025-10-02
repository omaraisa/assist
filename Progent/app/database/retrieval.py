"""
ArcGIS Tools Retrieval Service
Provides intelligent search and retrieval of ArcGIS geoprocessing tools for RAG system.
"""

import re
import logging
from typing import List, Dict, Any, Optional, Tuple
from collections import Counter
import math

# Add current directory to path for imports
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from database import ArcGISToolsDatabase

logger = logging.getLogger(__name__)

class ArcGISToolsRetriever:
    """Intelligent retrieval system for ArcGIS geoprocessing tools."""

    def __init__(self, db_path: str = "app/database/arcgis_tools.db"):
        """Initialize retriever with database connection.

        Args:
            db_path: Path to the SQLite database
        """
        self.db = ArcGISToolsDatabase(db_path)
        self._load_stop_words()

    def _load_stop_words(self):
        """Load common stop words to filter out from queries."""
        self.stop_words = {
            'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
            'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
            'to', 'was', 'will', 'with', 'would', 'i', 'me', 'my', 'myself',
            'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself',
            'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
            'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs',
            'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these',
            'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'will',
            'would', 'could', 'should', 'may', 'might', 'must', 'shall'
        }

    def preprocess_query(self, query: str) -> List[str]:
        """Preprocess user query to extract meaningful keywords.

        Args:
            query: Raw user query

        Returns:
            List of processed keywords
        """
        # Convert to lowercase
        query = query.lower()

        # Remove punctuation and special characters
        query = re.sub(r'[^\w\s]', ' ', query)

        # Split into words
        words = query.split()

        # Remove stop words and short words
        keywords = [word for word in words if word not in self.stop_words and len(word) > 2]

        # Remove duplicates while preserving order
        seen = set()
        unique_keywords = []
        for keyword in keywords:
            if keyword not in seen:
                unique_keywords.append(keyword)
                seen.add(keyword)

        logger.debug(f"Query '{query}' -> keywords: {unique_keywords}")
        return unique_keywords

    def search_relevant_tools(self, query: str, max_results: int = 10,
                            min_score: float = 0.1) -> List[Dict[str, Any]]:
        """Search for relevant tools based on user query.

        Args:
            query: User query string
            max_results: Maximum number of results to return
            min_score: Minimum relevance score (0-1)

        Returns:
            List of relevant tools with scores and metadata
        """
        # Preprocess query
        keywords = self.preprocess_query(query)

        if not keywords:
            logger.warning("No valid keywords found in query")
            return []

        # Search database
        db_results = self.db.search_functions_by_keywords(keywords, limit=max_results * 2)

        if not db_results:
            logger.info(f"No tools found for keywords: {keywords}")
            return []

        # Calculate relevance scores
        scored_results = []
        for result in db_results:
            score = self._calculate_relevance_score(result, keywords, query)
            if score >= min_score:
                result['relevance_score'] = score
                scored_results.append(result)

        # Sort by relevance score
        scored_results.sort(key=lambda x: x['relevance_score'], reverse=True)

        # Return top results
        final_results = scored_results[:max_results]

        logger.info(f"Found {len(final_results)} relevant tools for query: '{query}'")
        return final_results

    def _calculate_relevance_score(self, tool_result: Dict[str, Any],
                                 query_keywords: List[str], original_query: str) -> float:
        """Calculate relevance score for a tool based on query match.

        Args:
            tool_result: Tool result from database
            query_keywords: Processed query keywords
            original_query: Original user query

        Returns:
            Relevance score between 0 and 1
        """
        score = 0.0
        tool_keywords = set(tool_result.get('matched_keywords', []))
        query_keywords_set = set(query_keywords)

        # Base score from keyword matches
        matched_keywords = tool_keywords.intersection(query_keywords_set)
        keyword_match_score = len(matched_keywords) / len(query_keywords) if query_keywords else 0

        # Boost for exact matches and higher match counts
        exact_match_boost = 1.0 if len(matched_keywords) == len(query_keywords) else 0.8
        keyword_match_score *= exact_match_boost

        # Description relevance
        declaration = tool_result.get('declaration', {})
        description = declaration.get('description', '').lower()
        description_matches = sum(1 for keyword in query_keywords if keyword in description)
        description_score = description_matches / len(query_keywords) if query_keywords else 0

        # Function name relevance
        function_name = tool_result.get('function_name', '').lower()
        name_matches = sum(1 for keyword in query_keywords if keyword in function_name)
        name_score = name_matches / len(query_keywords) * 0.5 if query_keywords else 0  # Lower weight

        # Category relevance bonus
        category = tool_result.get('toolbox_category', '').lower()
        category_keywords = {
            'analysis': ['analyze', 'analysis', 'statistics', 'calculate'],
            'spatial_analyst': ['spatial', 'raster', 'terrain', 'surface', 'distance'],
            '3d_analyst': ['3d', 'terrain', 'surface', 'elevation', 'tin'],
            'network_analyst': ['network', 'route', 'path', 'transport', 'connectivity'],
            'geostatistical': ['statistics', 'interpolation', 'kriging', 'idw'],
            'cartography': ['map', 'layout', 'symbol', 'label', 'cartographic'],
            'conversion': ['convert', 'export', 'import', 'format', 'transform'],
            'data_management': ['data', 'manage', 'organize', 'clean', 'repair']
        }

        category_score = 0.0
        if category in category_keywords:
            category_matches = len(set(category_keywords[category]).intersection(query_keywords_set))
            category_score = category_matches * 0.2  # Small bonus

        # Combine scores with weights
        total_score = (
            keyword_match_score * 0.6 +      # Keywords are most important
            description_score * 0.25 +       # Description is secondary
            name_score * 0.1 +               # Function name is least important
            category_score * 0.05            # Category gives small bonus
        )

        # Normalize to 0-1 range
        final_score = min(total_score, 1.0)

        logger.debug(f"Tool {tool_result['function_name']}: score={final_score:.3f} "
                    f"(keywords={keyword_match_score:.3f}, desc={description_score:.3f}, "
                    f"name={name_score:.3f}, cat={category_score:.3f})")

        return final_score

    def get_tools_for_task(self, task_description: str, max_tools: int = 5) -> List[Dict[str, Any]]:
        """Get most relevant tools for a specific GIS task.

        Args:
            task_description: Description of the GIS task
            max_tools: Maximum number of tools to return

        Returns:
            List of relevant tools with their declarations
        """
        return self.search_relevant_tools(task_description, max_tools)

    def get_tool_details(self, function_name: str) -> Optional[Dict[str, Any]]:
        """Get complete details for a specific tool.

        Args:
            function_name: Name of the function

        Returns:
            Complete tool declaration or None if not found
        """
        return self.db.get_function_by_name(function_name)

    def get_tools_by_category(self, category: str, limit: int = None) -> List[Dict[str, Any]]:
        """Get all tools in a specific category.

        Args:
            category: Toolbox category (e.g., 'analysis', 'spatial_analyst')
            limit: Maximum number of tools to return

        Returns:
            List of tools in the category
        """
        return self.db.get_functions_by_category(category)[:limit] if limit else self.db.get_functions_by_category(category)

    def get_similar_tools(self, function_name: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Find tools similar to a given function based on keywords.

        Args:
            function_name: Name of the reference function
            limit: Maximum number of similar tools to return

        Returns:
            List of similar tools
        """
        # Get the reference tool
        ref_tool = self.get_tool_details(function_name)
        if not ref_tool:
            return []

        # Use its keywords to find similar tools
        keywords = ref_tool['declaration'].get('keywords', [])
        if not keywords:
            return []

        # Search for tools with similar keywords
        similar_tools = self.db.search_functions_by_keywords(keywords, limit=limit + 1)

        # Remove the reference tool itself
        similar_tools = [tool for tool in similar_tools if tool['function_name'] != function_name]

        return similar_tools[:limit]

    def explain_relevance(self, tool_result: Dict[str, Any], query: str) -> str:
        """Generate explanation for why a tool is relevant to a query.

        Args:
            tool_result: Tool result with relevance score
            query: Original user query

        Returns:
            Human-readable explanation
        """
        keywords = self.preprocess_query(query)
        matched_keywords = tool_result.get('matched_keywords', [])
        function_name = tool_result['function_name']
        declaration = tool_result.get('declaration', {})
        description = declaration.get('description', '')

        explanation_parts = []

        if matched_keywords:
            matched_list = ', '.join(f"'{k}'" for k in matched_keywords[:3])
            explanation_parts.append(f"matches keywords: {matched_list}")

        if any(keyword in description.lower() for keyword in keywords):
            explanation_parts.append("description contains relevant terms")

        if any(keyword in function_name.lower() for keyword in keywords):
            explanation_parts.append("function name is relevant")

        score = tool_result.get('relevance_score', 0)
        confidence = "high" if score > 0.7 else "medium" if score > 0.4 else "low"

        explanation = f"This tool has {confidence} relevance ({score:.1f}) because it {' and '.join(explanation_parts)}."

        return explanation

    def get_search_stats(self) -> Dict[str, Any]:
        """Get statistics about the tool database and search capabilities."""
        db_stats = self.db.get_stats()

        return {
            'database_stats': db_stats,
            'search_capabilities': {
                'supports_keyword_search': True,
                'supports_category_filtering': True,
                'supports_similarity_search': True,
                'max_results_limit': 50
            }
        }


# Convenience functions for easy integration
def search_arcgis_tools(query: str, max_results: int = 10) -> List[Dict[str, Any]]:
    """Search ArcGIS tools by natural language query.

    Args:
        query: Natural language description of desired GIS operation
        max_results: Maximum number of tools to return

    Returns:
        List of relevant tools with declarations and relevance scores
    """
    retriever = ArcGISToolsRetriever()
    return retriever.search_relevant_tools(query, max_results)

def get_tool_declaration(function_name: str) -> Optional[Dict[str, Any]]:
    """Get complete declaration for a specific ArcGIS tool.

    Args:
        function_name: Name of the ArcGIS tool function

    Returns:
        Complete tool declaration or None if not found
    """
    retriever = ArcGISToolsRetriever()
    return retriever.get_tool_details(function_name)

def get_tools_by_category(category: str) -> List[Dict[str, Any]]:
    """Get all tools in a specific ArcGIS toolbox category.

    Args:
        category: Toolbox category (e.g., 'analysis', 'spatial_analyst')

    Returns:
        List of tools in the category
    """
    retriever = ArcGISToolsRetriever()
    return retriever.get_tools_by_category(category)