"""
ArcGIS Tools Database Population Script
Parses all generated_ai_declarations.py files and populates the database.
"""

import sys
import os
import json
import ast
import logging
from pathlib import Path
from typing import Dict, Any, List
import importlib.util

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from database.database import ArcGISToolsDatabase

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DatabasePopulator:
    """Populates the ArcGIS tools database from declaration files."""

    def __init__(self, generated_functions_path: str = "generated_functions"):
        """Initialize populator.

        Args:
            generated_functions_path: Path to generated_functions directory
        """
        self.generated_functions_path = Path(generated_functions_path)
        self.db = ArcGISToolsDatabase()
        self.stats = {
            'files_processed': 0,
            'functions_added': 0,
            'errors': 0
        }

    def populate_database(self) -> Dict[str, Any]:
        """Main method to populate database from all declaration files."""
        logger.info("Starting database population...")

        if not self.generated_functions_path.exists():
            raise FileNotFoundError(f"Generated functions path not found: {self.generated_functions_path}")

        # Find all generated_ai_declarations.py files
        declaration_files = list(self.generated_functions_path.rglob("generated_ai_declarations.py"))

        if not declaration_files:
            logger.warning("No generated_ai_declarations.py files found!")
            return self.stats

        logger.info(f"Found {len(declaration_files)} declaration files")

        # Process each file
        for file_path in declaration_files:
            try:
                self._process_declaration_file(file_path)
            except Exception as e:
                logger.error(f"Error processing {file_path}: {e}")
                self.stats['errors'] += 1

        # Log final statistics
        logger.info("Database population completed!")
        logger.info(f"Files processed: {self.stats['files_processed']}")
        logger.info(f"Functions added: {self.stats['functions_added']}")
        logger.info(f"Errors: {self.stats['errors']}")

        # Get database stats
        db_stats = self.db.get_stats()
        logger.info(f"Total functions in database: {db_stats['total_functions']}")
        logger.info(f"Functions by category: {db_stats['functions_by_category']}")

        return {**self.stats, **db_stats}

    def _process_declaration_file(self, file_path: Path):
        """Process a single declaration file."""
        logger.info(f"Processing: {file_path}")

        # Determine toolbox category from path
        toolbox_category = self._get_toolbox_category(file_path)

        # Load the declarations
        declarations = self._load_declarations_from_file(file_path)

        if not declarations:
            logger.warning(f"No declarations found in {file_path}")
            return

        # Insert each declaration
        for func_name, declaration in declarations.items():
            try:
                self.db.insert_function_declaration(
                    function_name=func_name,
                    declaration=declaration,
                    toolbox_category=toolbox_category
                )
                self.stats['functions_added'] += 1
            except Exception as e:
                logger.error(f"Error inserting {func_name}: {e}")
                self.stats['errors'] += 1

        self.stats['files_processed'] += 1
        logger.info(f"Processed {len(declarations)} functions from {toolbox_category}")

    def _get_toolbox_category(self, file_path: Path) -> str:
        """Determine toolbox category from file path."""
        # Extract category from parent directory name
        parent_dir = file_path.parent.name

        # Map common directory names to categories
        category_mapping = {
            'analysis': 'analysis',
            'spatial-analyst': 'spatial_analyst',
            'spatial_analyst': 'spatial_analyst',
            '3d-analyst': '3d_analyst',
            '3d_analyst': '3d_analyst',
            'business-analyst': 'business_analyst',
            'business_analyst': 'business_analyst',
            'cartography': 'cartography',
            'conversion': 'conversion',
            'data-management': 'data_management',
            'data_management': 'data_management',
            'geostatistical-analyst': 'geostatistical_analyst',
            'geostatistical_analyst': 'geostatistical_analyst',
            'image-analyst': 'image_analyst',
            'image_analyst': 'image_analyst',
            'network-analyst': 'network_analyst',
            'network_analyst': 'network_analyst',
            'spatial-statistics': 'spatial_statistics',
            'spatial_statistics': 'spatial_statistics',
            'topographic-production': 'topographic_production',
            'topographic_production': 'topographic_production'
        }

        return category_mapping.get(parent_dir.lower(), parent_dir.lower())

    def _load_declarations_from_file(self, file_path: Path) -> Dict[str, Any]:
        """Load function declarations from a Python file."""
        try:
            # Read the file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Try to parse as Python AST to find variable assignments
            tree = ast.parse(content)

            declarations = {}

            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    # Look for variable assignments
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            var_name = target.id
                            if var_name.endswith('_declarations') or 'declaration' in var_name.lower():
                                # Try to evaluate the assigned value
                                try:
                                    # Create a safe evaluation context
                                    safe_globals = {
                                        '__builtins__': {
                                            'True': True, 'False': False, 'None': None,
                                            'dict': dict, 'list': list, 'str': str, 'int': int, 'float': float
                                        }
                                    }

                                    # Evaluate the AST node
                                    value = eval(compile(ast.Expression(body=node.value), '<string>', 'eval'), safe_globals)

                                    if isinstance(value, dict):
                                        declarations.update(value)
                                        logger.debug(f"Found declarations in variable: {var_name}")

                                except Exception as e:
                                    logger.debug(f"Could not evaluate {var_name}: {e}")

            # If AST parsing didn't work, try direct JSON parsing
            if not declarations:
                declarations = self._try_json_parsing(content)

            return declarations

        except Exception as e:
            logger.error(f"Error loading declarations from {file_path}: {e}")
            return {}

    def _try_json_parsing(self, content: str) -> Dict[str, Any]:
        """Try to extract JSON-like structures from file content."""
        declarations = {}

        # Look for JSON-like structures in the content
        lines = content.split('\n')
        current_function = None
        brace_count = 0
        json_buffer = []

        for line in lines:
            line = line.strip()

            if '{' in line:
                brace_count += line.count('{')
            if '}' in line:
                brace_count += line.count('}')

            # Look for function name patterns
            if '"' in line and '":' in line and brace_count == 0:
                # This might be a function declaration start
                if current_function and json_buffer:
                    # Process previous function
                    json_str = '\n'.join(json_buffer)
                    try:
                        declaration = json.loads(json_str)
                        declarations[current_function] = declaration
                    except:
                        pass

                # Extract new function name
                parts = line.split('":')
                if parts:
                    current_function = parts[0].strip('"')
                    json_buffer = [line]
                    brace_count = line.count('{') - line.count('}')
            elif current_function:
                json_buffer.append(line)
                brace_count += line.count('{') - line.count('}')

        # Process last function
        if current_function and json_buffer:
            json_str = '\n'.join(json_buffer)
            try:
                # Clean up the JSON string
                json_str = json_str.replace('"""', '"').replace("'''", "'")
                declaration = json.loads(json_str)
                declarations[current_function] = declaration
            except Exception as e:
                logger.debug(f"Could not parse JSON for {current_function}: {e}")

        return declarations

    def clear_database(self):
        """Clear all data from database."""
        logger.warning("Clearing all data from database...")
        with self.db.conn.cursor() as cursor:
            cursor.execute('DELETE FROM function_keywords')
            cursor.execute('DELETE FROM function_examples')
            cursor.execute('DELETE FROM function_declarations')
            cursor.execute('DELETE FROM keywords')
            self.db.conn.commit()
        logger.info("Database cleared")

    def validate_declarations(self, declarations: Dict[str, Any]) -> List[str]:
        """Validate function declarations for required fields."""
        errors = []

        for func_name, declaration in declarations.items():
            if not isinstance(declaration, dict):
                errors.append(f"{func_name}: Declaration must be a dictionary")
                continue

            # Check required fields
            required_fields = ['name', 'description', 'parameters']
            for field in required_fields:
                if field not in declaration:
                    errors.append(f"{func_name}: Missing required field '{field}'")

            # Check for keywords (should be present after Jules enhancement)
            if 'keywords' not in declaration:
                errors.append(f"{func_name}: Missing keywords field (waiting for Jules)")

            # Check for examples (should be present after Jules enhancement)
            if 'action_input_examples' not in declaration:
                errors.append(f"{func_name}: Missing action_input_examples field (waiting for Jules)")

        return errors


def main():
    """Main function to run the population script."""
    import argparse

    parser = argparse.ArgumentParser(description='Populate ArcGIS tools database')
    parser.add_argument('--path', default='generated_functions',
                       help='Path to generated_functions directory')
    parser.add_argument('--clear', action='store_true',
                       help='Clear database before population')
    parser.add_argument('--validate-only', action='store_true',
                       help='Only validate declarations without inserting')

    args = parser.parse_args()

    try:
        populator = DatabasePopulator(args.path)

        if args.clear:
            populator.clear_database()

        if args.validate_only:
            # Find and validate all files
            declaration_files = list(Path(args.path).rglob("generated_ai_declarations.py"))
            all_errors = []

            for file_path in declaration_files:
                declarations = populator._load_declarations_from_file(file_path)
                errors = populator.validate_declarations(declarations)
                all_errors.extend(errors)

            if all_errors:
                logger.error("Validation errors found:")
                for error in all_errors:
                    logger.error(f"  {error}")
            else:
                logger.info("All declarations are valid!")

        else:
            # Full population
            stats = populator.populate_database()

            print("\nPopulation Summary:")
            print(f"Files processed: {stats['files_processed']}")
            print(f"Functions added: {stats['functions_added']}")
            print(f"Errors: {stats['errors']}")
            print(f"Total functions in DB: {stats.get('total_functions', 0)}")

    except Exception as e:
        logger.error(f"Population failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()