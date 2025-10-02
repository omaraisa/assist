#!/usr/bin/env python3
"""
Unified Database Population Script
Loads function declarations from multiple sources without duplication.

Sources:
1. Original function_declarations.py (existing AI functions)
2. Jules' enhanced generated_functions/ (geoprocessing tools)
3. Future: Additional sources as needed

Features:
- Deduplication by function name
- Keyword extraction and enhancement
- Category assignment
- Progress tracking and error handling
"""

import sys
import os
import json
import ast
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional, Set
import re

# Add the database module to path
sys.path.append(str(Path(__file__).parent))

from database import ArcGISToolsDatabase

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class UnifiedDatabasePopulator:
    """Unified population system for multiple function declaration sources."""

    def __init__(self, db_path: str = "app/database/arcgis_tools.db"):
        """Initialize the populator with database connection."""
        self.db = ArcGISToolsDatabase(db_path)
        self.processed_functions: Set[str] = set()
        self.stats = {
            'original_functions': 0,
            'geoprocessing_functions': 0,
            'duplicates_skipped': 0,
            'errors': 0
        }

    def populate_from_all_sources(self, generated_functions_path: str = "../generated_functions") -> Dict[str, Any]:
        """Populate database from all available sources.

        Args:
            generated_functions_path: Path to Jules' enhanced generated_functions directory

        Returns:
            Statistics about the population process
        """
        logger.info("Starting unified database population...")

        # Convert relative path to absolute based on script location
        script_dir = Path(__file__).parent
        if not Path(generated_functions_path).is_absolute():
            generated_functions_path = script_dir / generated_functions_path

        # 1. Load original function declarations
        self._populate_from_original_declarations()

        # 2. Load Jules' enhanced geoprocessing tools
        self._populate_from_generated_functions(str(generated_functions_path))

        # 3. Generate final statistics
        final_stats = self.db.get_stats()
        final_stats.update(self.stats)

        logger.info(f"Population complete! {final_stats}")
        return final_stats

    def _populate_from_original_declarations(self):
        """Load functions from the original function_declarations.py file."""
        logger.info("Loading original function declarations...")

        try:
            # Import the original declarations - adjust path based on current working directory
            script_dir = Path(__file__).parent
            ai_dir = script_dir.parent / "ai"

            if ai_dir.exists():
                sys.path.insert(0, str(ai_dir))
                from function_declarations import FunctionDeclaration
                sys.path.pop(0)  # Clean up path
            else:
                # Try relative import
                sys.path.append(str(script_dir.parent))
                from app.ai.function_declarations import FunctionDeclaration
                sys.path.pop()

            for func_name, declaration in FunctionDeclaration.functions_declarations.items():
                if func_name in self.processed_functions:
                    logger.debug(f"Skipping duplicate function: {func_name}")
                    self.stats['duplicates_skipped'] += 1
                    continue

                try:
                    # Enhance the declaration with keywords and category
                    enhanced_declaration = self._enhance_original_declaration(func_name, declaration)

                    # Insert into database
                    self.db.insert_function_declaration(
                        func_name,
                        enhanced_declaration,
                        toolbox_category=self._infer_category_from_function(func_name, declaration)
                    )

                    self.processed_functions.add(func_name)
                    self.stats['original_functions'] += 1

                except Exception as e:
                    logger.error(f"Error processing original function {func_name}: {e}")
                    self.stats['errors'] += 1

        except ImportError as e:
            logger.error(f"Could not import original function declarations: {e}")
            self.stats['errors'] += 1

    def _populate_from_generated_functions(self, base_path: str):
        """Load functions from Jules' enhanced generated_functions directory."""
        logger.info(f"Loading enhanced geoprocessing functions from {base_path}...")

        base_path = Path(base_path)
        if not base_path.exists():
            logger.warning(f"Generated functions path does not exist: {base_path}")
            return

        # Process each toolbox category
        categories = [
            'analysis', 'spatial_analyst', '3d_analyst', 'network_analyst',
            'geostatistical', 'cartography', 'conversion', 'data_management',
            'image_analyst', 'spatial_statistics', 'topographic_production',
            'business_analyst'
        ]

        for category in categories:
            category_path = base_path / category
            if not category_path.exists():
                continue

            logger.info(f"Processing category: {category}")

            # Look for generated_ai_declarations.py
            declarations_file = category_path / "generated_ai_declarations.py"
            if declarations_file.exists():
                self._process_declarations_file(declarations_file, category)

    def _process_declarations_file(self, file_path: Path, category: str):
        """Process a single declarations file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Parse the Python file to extract the declarations
            tree = ast.parse(content)

            # Look for variable assignments (should contain the declarations dict)
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name) and target.id in ['TOOL_DECLARATIONS', 'tool_declarations', 'declarations']:
                            # Evaluate the assigned value
                            declarations = self._safe_eval_ast_node(node.value)
                            if isinstance(declarations, dict):
                                self._process_declarations_dict(declarations, category)
                                break

        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
            self.stats['errors'] += 1

    def _process_declarations_dict(self, declarations: Dict[str, Any], category: str):
        """Process a dictionary of function declarations."""
        for func_name, declaration in declarations.items():
            if func_name in self.processed_functions:
                logger.debug(f"Skipping duplicate function: {func_name}")
                self.stats['duplicates_skipped'] += 1
                continue

            try:
                # Insert into database
                self.db.insert_function_declaration(func_name, declaration, category)
                self.processed_functions.add(func_name)
                self.stats['geoprocessing_functions'] += 1

            except Exception as e:
                logger.error(f"Error processing geoprocessing function {func_name}: {e}")
                self.stats['errors'] += 1

    def _enhance_original_declaration(self, func_name: str, declaration: Dict[str, Any]) -> Dict[str, Any]:
        """Enhance original function declarations with keywords and examples."""
        enhanced = declaration.copy()

        # Add keywords if not present
        if 'keywords' not in enhanced:
            enhanced['keywords'] = self._extract_keywords_from_declaration(func_name, declaration)

        # Ensure action_input_examples exists
        if 'action_input_examples' not in enhanced:
            enhanced['action_input_examples'] = []

        return enhanced

    def _extract_keywords_from_declaration(self, func_name: str, declaration: Dict[str, Any]) -> List[str]:
        """Extract keywords from function name and description."""
        keywords = []

        # Add function name parts
        name_parts = re.findall(r'[a-zA-Z]+', func_name.lower())
        keywords.extend(name_parts)

        # Add description words (excluding common stop words)
        description = declaration.get('description', '').lower()
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those'}

        desc_words = re.findall(r'\b[a-zA-Z]{3,}\b', description)  # Words with 3+ characters
        keywords.extend([word for word in desc_words if word not in stop_words])

        # Add parameter names
        for param_name in declaration.get('parameters', {}):
            param_parts = re.findall(r'[a-zA-Z]+', param_name.lower())
            keywords.extend(param_parts)

        # Remove duplicates and return
        return list(set(keywords))

    def _infer_category_from_function(self, func_name: str, declaration: Dict[str, Any]) -> str:
        """Infer toolbox category from function name and description."""
        name_lower = func_name.lower()
        desc_lower = declaration.get('description', '').lower()

        # Spatial Analyst tools
        if any(keyword in name_lower or keyword in desc_lower for keyword in
               ['slope', 'aspect', 'hillshade', 'raster', 'euclidean', 'cost', 'distance', 'interpolation']):
            return 'spatial_analyst'

        # Analysis tools
        if any(keyword in name_lower or keyword in desc_lower for keyword in
               ['buffer', 'clip', 'select', 'join', 'intersect', 'union', 'dissolve']):
            return 'analysis'

        # Data Management tools
        if any(keyword in name_lower or keyword in desc_lower for keyword in
               ['field', 'calculate', 'domain', 'statistics', 'frequency']):
            return 'data_management'

        # Dashboard tools
        if 'dashboard' in name_lower or 'chart' in name_lower:
            return 'cartography'

        # Default category
        return 'analysis'

    def _safe_eval_ast_node(self, node) -> Any:
        """Safely evaluate an AST node to extract literal values."""
        try:
            # For simple literals and containers
            if isinstance(node, ast.Dict):
                result = {}
                for key, value in zip(node.keys, node.values):
                    if isinstance(key, ast.Str):
                        key_val = key.s
                    elif isinstance(key, ast.Constant) and isinstance(key.value, str):
                        key_val = key.value
                    else:
                        continue

                    result[key_val] = self._safe_eval_ast_node(value)
                return result

            elif isinstance(node, ast.List):
                return [self._safe_eval_ast_node(item) for item in node.elts]

            elif isinstance(node, ast.Str):
                return node.s

            elif isinstance(node, ast.Constant):
                return node.value

            elif isinstance(node, ast.NameConstant):  # For True, False, None in older Python
                return node.value

            else:
                # For complex expressions, return a placeholder
                return f"<complex_expression_at_line_{node.lineno}>"

        except Exception:
            return f"<error_evaluating_node>"

def main():
    """Main entry point for the population script."""
    import argparse

    parser = argparse.ArgumentParser(description="Unified database population script")
    parser.add_argument(
        "--generated-path",
        default="../generated_functions",
        help="Path to Jules' enhanced generated_functions directory"
    )
    parser.add_argument(
        "--db-path",
        default="app/database/arcgis_tools.db",
        help="Path to the database file"
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Only validate the data sources without populating"
    )

    args = parser.parse_args()

    if args.validate_only:
        print("Validating data sources...")

        # Check if sources exist - use script-relative paths
        script_dir = Path(__file__).parent
        original_path = script_dir.parent / "ai" / "function_declarations.py"
        generated_path = Path(args.generated_path)
        if not generated_path.is_absolute():
            generated_path = script_dir / args.generated_path

        original_exists = original_path.exists()
        generated_exists = generated_path.exists()

        print(f"Original declarations: {'✓' if original_exists else '✗'} ({original_path})")
        print(f"Generated functions: {'✓' if generated_exists else '✗'} ({generated_path})")

        if generated_exists:
            total_files = sum(1 for f in generated_path.rglob("generated_ai_declarations.py"))
            print(f"Found {total_files} declaration files")

        return

    # Perform population
    populator = UnifiedDatabasePopulator(args.db_path)
    stats = populator.populate_from_all_sources(args.generated_path)

    print("\n" + "="*50)
    print("POPULATION COMPLETE")
    print("="*50)
    print(f"Original functions loaded: {stats['original_functions']}")
    print(f"Geoprocessing functions loaded: {stats['geoprocessing_functions']}")
    print(f"Duplicates skipped: {stats['duplicates_skipped']}")
    print(f"Errors encountered: {stats['errors']}")
    print(f"Total functions in database: {stats['total_functions']}")
    print(f"Total keywords: {stats['total_keywords']}")
    print("="*50)

if __name__ == "__main__":
    main()