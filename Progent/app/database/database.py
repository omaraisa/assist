"""
ArcGIS Geoprocessing Tools Database Schema
SQLite database for storing function declarations with keyword-based retrieval for RAG system.
"""

import sqlite3
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ArcGISToolsDatabase:
    """SQLite database for ArcGIS geoprocessing tool declarations."""

    def __init__(self, db_path: str = "app/database/arcgis_tools.db"):
        """Initialize database connection.

        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = None
        self._create_tables()

    def _create_tables(self):
        """Create database tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Main function declarations table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS function_declarations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    function_name TEXT UNIQUE NOT NULL,
                    declaration TEXT NOT NULL,  -- Full JSON declaration
                    toolbox_category TEXT,  -- analysis, spatial_analyst, etc.
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            # Keywords table for many-to-many relationship
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS keywords (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    keyword TEXT UNIQUE NOT NULL
                )
            ''')

            # Junction table for function-keyword relationships
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS function_keywords (
                    function_id INTEGER,
                    keyword_id INTEGER,
                    relevance_score REAL DEFAULT 1.0,  -- For future weighting
                    FOREIGN KEY (function_id) REFERENCES function_declarations (id) ON DELETE CASCADE,
                    FOREIGN KEY (keyword_id) REFERENCES keywords (id) ON DELETE CASCADE,
                    PRIMARY KEY (function_id, keyword_id)
                )
            ''')

            # Examples table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS function_examples (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    function_id INTEGER,
                    example_json TEXT NOT NULL,  -- JSON string of example parameters
                    description TEXT,
                    FOREIGN KEY (function_id) REFERENCES function_declarations (id) ON DELETE CASCADE
                )
            ''')

            # Search optimization indexes
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_function_name ON function_declarations(function_name)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_toolbox_category ON function_declarations(toolbox_category)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_keyword ON keywords(keyword)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_function_keywords ON function_keywords(function_id, keyword_id)')

            conn.commit()
            logger.info("Database tables created successfully")

    def insert_function_declaration(self, function_name: str, declaration: Dict[str, Any],
                                  toolbox_category: str = None) -> int:
        """Insert or update a function declaration.

        Args:
            function_name: Name of the function
            declaration: Full JSON declaration dict
            toolbox_category: Category like 'analysis', 'spatial_analyst', etc.

        Returns:
            Function ID
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Insert/update function declaration
            cursor.execute('''
                INSERT OR REPLACE INTO function_declarations
                (function_name, declaration, toolbox_category, updated_at)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
            ''', (
                function_name,
                json.dumps(declaration),
                toolbox_category or 'unknown'
            ))

            function_id = cursor.lastrowid
            if not function_id:  # If REPLACE was used, get existing ID
                cursor.execute('SELECT id FROM function_declarations WHERE function_name = ?',
                             (function_name,))
                function_id = cursor.fetchone()[0]

            # Handle keywords
            if 'keywords' in declaration:
                self._insert_keywords_with_conn(cursor, function_id, declaration['keywords'])

            # Handle examples
            if 'action_input_examples' in declaration:
                self._insert_examples_with_conn(cursor, function_id, declaration['action_input_examples'])

            conn.commit()
            logger.info(f"Inserted/updated function: {function_name}")
            return function_id

    def _insert_keywords_with_conn(self, cursor, function_id: int, keywords: List[str]):
        """Insert keywords for a function using provided cursor."""
        for keyword in keywords:
            # Insert keyword if it doesn't exist
            cursor.execute('INSERT OR IGNORE INTO keywords (keyword) VALUES (?)', (keyword,))
            cursor.execute('SELECT id FROM keywords WHERE keyword = ?', (keyword,))
            keyword_id = cursor.fetchone()[0]

            # Link function to keyword
            cursor.execute('''
                INSERT OR REPLACE INTO function_keywords (function_id, keyword_id)
                VALUES (?, ?)
            ''', (function_id, keyword_id))

    def _insert_examples_with_conn(self, cursor, function_id: int, examples: List[Dict[str, Any]]):
        """Insert examples for a function using provided cursor."""
        # Clear existing examples
        cursor.execute('DELETE FROM function_examples WHERE function_id = ?', (function_id,))

        # Insert new examples
        for example in examples:
            cursor.execute('''
                INSERT INTO function_examples (function_id, example_json, description)
                VALUES (?, ?, ?)
            ''', (
                function_id,
                json.dumps(example),
                example.get('description', '')
            ))

    def search_functions_by_keywords(self, query_keywords: List[str], limit: int = 20,
                                   min_matches: int = 1) -> List[Dict[str, Any]]:
        """Search functions by keywords using intersection matching.

        Args:
            query_keywords: List of keywords to search for
            limit: Maximum number of results
            min_matches: Minimum number of keyword matches required

        Returns:
            List of function declarations with match scores
        """
        if not query_keywords:
            return []

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Build query for keyword matching
            placeholders = ','.join('?' * len(query_keywords))
            query = f'''
                SELECT fd.function_name, fd.declaration, fd.toolbox_category,
                       COUNT(fk.keyword_id) as match_count,
                       GROUP_CONCAT(k.keyword) as matched_keywords
                FROM function_declarations fd
                JOIN function_keywords fk ON fd.id = fk.function_id
                JOIN keywords k ON fk.keyword_id = k.id
                WHERE k.keyword IN ({placeholders})
                GROUP BY fd.id
                HAVING match_count >= ?
                ORDER BY match_count DESC, fd.function_name
                LIMIT ?
            '''

            params = query_keywords + [min_matches, limit]
            cursor.execute(query, params)

            results = []
            for row in cursor.fetchall():
                function_name, declaration_json, category, match_count, matched_keywords = row
                declaration = json.loads(declaration_json)

                results.append({
                    'function_name': function_name,
                    'declaration': declaration,
                    'toolbox_category': category,
                    'match_count': match_count,
                    'matched_keywords': matched_keywords.split(',') if matched_keywords else []
                })

            return results

    def get_function_by_name(self, function_name: str) -> Optional[Dict[str, Any]]:
        """Get a specific function declaration by name."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT declaration, toolbox_category
                FROM function_declarations
                WHERE function_name = ?
            ''', (function_name,))

            row = cursor.fetchone()
            if row:
                declaration_json, category = row
                return {
                    'function_name': function_name,
                    'declaration': json.loads(declaration_json),
                    'toolbox_category': category
                }
            return None

    def get_all_functions(self, limit: int = None) -> List[Dict[str, Any]]:
        """Get all function declarations."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            query = 'SELECT function_name, declaration, toolbox_category FROM function_declarations'
            if limit:
                query += f' LIMIT {limit}'

            cursor.execute(query)

            results = []
            for row in cursor.fetchall():
                function_name, declaration_json, category = row
                results.append({
                    'function_name': function_name,
                    'declaration': json.loads(declaration_json),
                    'toolbox_category': category
                })

            return results

    def get_functions_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Get functions by toolbox category."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                SELECT function_name, declaration
                FROM function_declarations
                WHERE toolbox_category = ?
                ORDER BY function_name
            ''', (category,))

            results = []
            for row in cursor.fetchall():
                function_name, declaration_json = row
                results.append({
                    'function_name': function_name,
                    'declaration': json.loads(declaration_json),
                    'toolbox_category': category
                })

            return results

    def get_stats(self) -> Dict[str, Any]:
        """Get database statistics."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            stats = {}

            # Total functions
            cursor.execute('SELECT COUNT(*) FROM function_declarations')
            stats['total_functions'] = cursor.fetchone()[0]

            # Functions by category
            cursor.execute('''
                SELECT toolbox_category, COUNT(*)
                FROM function_declarations
                GROUP BY toolbox_category
            ''')
            stats['functions_by_category'] = dict(cursor.fetchall())

            # Total keywords
            cursor.execute('SELECT COUNT(*) FROM keywords')
            stats['total_keywords'] = cursor.fetchone()[0]

            # Total keyword relationships
            cursor.execute('SELECT COUNT(*) FROM function_keywords')
            stats['total_keyword_relationships'] = cursor.fetchone()[0]

            return stats

    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()

# Convenience functions for easy use
def init_database(db_path: str = "app/database/arcgis_tools.db") -> ArcGISToolsDatabase:
    """Initialize and return database instance."""
    return ArcGISToolsDatabase(db_path)

def search_tools(query: str, limit: int = 20) -> List[Dict[str, Any]]:
    """Search tools by query string (space-separated keywords)."""
    keywords = [k.strip().lower() for k in query.split() if k.strip()]
    db = ArcGISToolsDatabase()
    return db.search_functions_by_keywords(keywords, limit)