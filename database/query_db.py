#!/usr/bin/env python3
"""
Query interface for AutoHotkey Documentation Database.
Provides easy Python API for searching and querying documentation.
"""

import os
import psycopg2
from psycopg2.extras import RealDictCursor
from typing import List, Dict, Optional, Tuple
import json

class AHKDocsDB:
    """Interface for querying AutoHotkey documentation database."""

    def __init__(self, connection_string: str = None):
        """Initialize database connection."""
        if connection_string is None:
            # Build from environment variables
            db_config = {
                'dbname': os.getenv('POSTGRES_DB', 'ahk_docs'),
                'user': os.getenv('POSTGRES_USER', 'postgres'),
                'password': os.getenv('POSTGRES_PASSWORD', 'postgres'),
                'host': os.getenv('POSTGRES_HOST', 'localhost'),
                'port': os.getenv('POSTGRES_PORT', '5432')
            }
            connection_string = f"dbname={db_config['dbname']} user={db_config['user']} " \
                              f"password={db_config['password']} host={db_config['host']} " \
                              f"port={db_config['port']}"

        self.conn = psycopg2.connect(connection_string)
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)

    def search(self, query: str, doc_type: str = None, category: str = None, limit: int = 20) -> List[Dict]:
        """Full-text search across documentation."""
        self.cursor.execute("""
            SELECT * FROM search_documents(%s, %s, %s, %s)
        """, (query, doc_type, category, limit))
        return [dict(row) for row in self.cursor.fetchall()]

    def get_document(self, title: str = None, doc_id: int = None) -> Optional[Dict]:
        """Get a specific document by title or ID."""
        if doc_id:
            self.cursor.execute("""
                SELECT * FROM v_documents_complete WHERE id = %s
            """, (doc_id,))
        elif title:
            self.cursor.execute("""
                SELECT * FROM v_documents_complete WHERE title = %s
            """, (title,))
        else:
            return None

        result = self.cursor.fetchone()
        return dict(result) if result else None

    def get_function(self, function_name: str) -> Optional[Dict]:
        """Get function details with parameters."""
        self.cursor.execute("""
            SELECT * FROM v_functions_complete WHERE function_name = %s
        """, (function_name,))

        result = self.cursor.fetchone()
        return dict(result) if result else None

    def get_object(self, object_name: str) -> Optional[Dict]:
        """Get object details with methods and properties."""
        self.cursor.execute("""
            SELECT * FROM v_objects_complete WHERE object_name = %s
        """, (object_name,))

        result = self.cursor.fetchone()
        return dict(result) if result else None

    def list_functions(self, limit: int = 100) -> List[Dict]:
        """List all functions."""
        self.cursor.execute("""
            SELECT function_name, return_type, title, file_path
            FROM v_functions_complete
            ORDER BY function_name
            LIMIT %s
        """, (limit,))
        return [dict(row) for row in self.cursor.fetchall()]

    def list_objects(self, limit: int = 100) -> List[Dict]:
        """List all objects."""
        self.cursor.execute("""
            SELECT object_name, extends, title, file_path
            FROM v_objects_complete
            ORDER BY object_name
            LIMIT %s
        """, (limit,))
        return [dict(row) for row in self.cursor.fetchall()]

    def get_code_examples(self, document_title: str) -> List[Dict]:
        """Get code examples for a document."""
        self.cursor.execute("""
            SELECT ce.code, ce.language, ce.description
            FROM code_examples ce
            JOIN documents d ON ce.document_id = d.id
            WHERE d.title = %s
            ORDER BY ce.example_order
        """, (document_title,))
        return [dict(row) for row in self.cursor.fetchall()]

    def get_sections(self, document_title: str) -> List[Dict]:
        """Get all sections for a document."""
        self.cursor.execute("""
            SELECT s.heading, s.heading_level, s.section_type, s.content
            FROM sections s
            JOIN documents d ON s.document_id = d.id
            WHERE d.title = %s
            ORDER BY s.section_order
        """, (document_title,))
        return [dict(row) for row in self.cursor.fetchall()]

    def get_related_documents(self, document_title: str, limit: int = 10) -> List[Dict]:
        """Get related documents."""
        # First get document ID
        doc = self.get_document(title=document_title)
        if not doc:
            return []

        self.cursor.execute("""
            SELECT * FROM get_related_documents(%s, %s)
        """, (doc['id'], limit))
        return [dict(row) for row in self.cursor.fetchall()]

    def find_functions_by_parameter(self, param_name: str) -> List[Dict]:
        """Find functions that have a specific parameter."""
        self.cursor.execute("""
            SELECT DISTINCT f.function_name, fp.param_name, fp.param_type, d.file_path
            FROM functions f
            JOIN function_parameters fp ON f.id = fp.function_id
            JOIN documents d ON f.document_id = d.id
            WHERE fp.param_name ILIKE %s
            ORDER BY f.function_name
        """, (f'%{param_name}%',))
        return [dict(row) for row in self.cursor.fetchall()]

    def find_objects_with_method(self, method_name: str) -> List[Dict]:
        """Find objects that have a specific method."""
        self.cursor.execute("""
            SELECT o.object_name, om.method_name, d.file_path
            FROM objects o
            JOIN object_methods om ON o.id = om.object_id
            JOIN documents d ON o.document_id = d.id
            WHERE om.method_name ILIKE %s
            ORDER BY o.object_name
        """, (f'%{method_name}%',))
        return [dict(row) for row in self.cursor.fetchall()]

    def get_statistics(self) -> Dict:
        """Get database statistics."""
        stats = {}

        # Document counts
        self.cursor.execute("""
            SELECT doc_type, COUNT(*) as count
            FROM documents
            GROUP BY doc_type
        """)
        stats['documents_by_type'] = {row['doc_type']: row['count'] for row in self.cursor.fetchall()}

        # Total counts
        self.cursor.execute("SELECT COUNT(*) as count FROM documents")
        stats['total_documents'] = self.cursor.fetchone()['count']

        self.cursor.execute("SELECT COUNT(*) as count FROM functions")
        stats['total_functions'] = self.cursor.fetchone()['count']

        self.cursor.execute("SELECT COUNT(*) as count FROM objects")
        stats['total_objects'] = self.cursor.fetchone()['count']

        self.cursor.execute("SELECT COUNT(*) as count FROM code_examples")
        stats['total_code_examples'] = self.cursor.fetchone()['count']

        self.cursor.execute("SELECT COUNT(*) as count FROM sections")
        stats['total_sections'] = self.cursor.fetchone()['count']

        return stats

    def close(self):
        """Close database connection."""
        self.cursor.close()
        self.conn.close()


def format_result(result: Dict, result_type: str = 'search'):
    """Format query result for display."""
    if result_type == 'search':
        print(f"\nTitle: {result.get('title')}")
        print(f"Type: {result.get('doc_type')}")
        print(f"Path: {result.get('file_path')}")
        print(f"Rank: {result.get('rank', 0):.4f}")
        if result.get('snippet'):
            print(f"Snippet: {result['snippet']}")
        print("-" * 70)

    elif result_type == 'function':
        print(f"\nFunction: {result.get('function_name')}")
        print(f"Syntax: {result.get('syntax', 'N/A')}")
        print(f"Returns: {result.get('return_type', 'N/A')}")
        if result.get('parameters'):
            print(f"\nParameters:")
            for param in result['parameters']:
                opt = ' (optional)' if param.get('optional') else ''
                print(f"  - {param['name']}: {param.get('type', 'Any')}{opt}")
                if param.get('description'):
                    print(f"    {param['description'][:100]}...")
        print("-" * 70)

    elif result_type == 'object':
        print(f"\nObject: {result.get('object_name')}")
        if result.get('extends'):
            print(f"Extends: {result['extends']}")
        if result.get('properties'):
            print(f"Properties: {', '.join(result['properties'])}")
        if result.get('methods'):
            print(f"Methods: {', '.join(result['methods'])}")
        print(f"Path: {result.get('file_path')}")
        print("-" * 70)


def interactive_mode():
    """Interactive query mode."""
    print("\n" + "=" * 70)
    print("AutoHotkey Documentation Database - Interactive Mode")
    print("=" * 70)
    print("\nCommands:")
    print("  search <query>           - Full-text search")
    print("  function <name>          - Get function details")
    print("  object <name>            - Get object details")
    print("  list functions           - List all functions")
    print("  list objects             - List all objects")
    print("  examples <title>         - Get code examples")
    print("  stats                    - Database statistics")
    print("  quit                     - Exit")
    print("")

    db = AHKDocsDB()

    try:
        while True:
            try:
                cmd = input("\n> ").strip()

                if not cmd:
                    continue

                if cmd == 'quit':
                    break

                elif cmd.startswith('search '):
                    query = cmd[7:]
                    results = db.search(query, limit=5)
                    if results:
                        print(f"\nFound {len(results)} results:")
                        for result in results:
                            format_result(result, 'search')
                    else:
                        print("\nNo results found")

                elif cmd.startswith('function '):
                    func_name = cmd[9:]
                    result = db.get_function(func_name)
                    if result:
                        format_result(result, 'function')
                    else:
                        print(f"\nFunction '{func_name}' not found")

                elif cmd.startswith('object '):
                    obj_name = cmd[7:]
                    result = db.get_object(obj_name)
                    if result:
                        format_result(result, 'object')
                    else:
                        print(f"\nObject '{obj_name}' not found")

                elif cmd == 'list functions':
                    results = db.list_functions(limit=20)
                    print(f"\nFunctions ({len(results)} shown):")
                    for r in results:
                        print(f"  - {r['function_name']}: {r.get('return_type', 'N/A')}")

                elif cmd == 'list objects':
                    results = db.list_objects(limit=20)
                    print(f"\nObjects ({len(results)} shown):")
                    for r in results:
                        extends = f" extends {r['extends']}" if r.get('extends') else ""
                        print(f"  - {r['object_name']}{extends}")

                elif cmd.startswith('examples '):
                    title = cmd[9:]
                    examples = db.get_code_examples(title)
                    if examples:
                        print(f"\nCode examples for '{title}':")
                        for i, ex in enumerate(examples, 1):
                            print(f"\nExample {i} ({ex['language']}):")
                            if ex['description']:
                                print(f"  {ex['description']}")
                            print(f"```{ex['language']}")
                            print(ex['code'][:500])  # Limit output
                            if len(ex['code']) > 500:
                                print("...")
                            print("```")
                    else:
                        print(f"\nNo examples found for '{title}'")

                elif cmd == 'stats':
                    stats = db.get_statistics()
                    print("\nDatabase Statistics:")
                    print(f"  Total Documents: {stats['total_documents']}")
                    print(f"  Functions: {stats['total_functions']}")
                    print(f"  Objects: {stats['total_objects']}")
                    print(f"  Code Examples: {stats['total_code_examples']}")
                    print(f"  Sections: {stats['total_sections']}")
                    print(f"\nDocuments by Type:")
                    for doc_type, count in stats['documents_by_type'].items():
                        print(f"  {doc_type}: {count}")

                else:
                    print("Unknown command. Type 'quit' to exit.")

            except KeyboardInterrupt:
                print("\n\nExiting...")
                break
            except Exception as e:
                print(f"Error: {e}")

    finally:
        db.close()


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        # Command-line mode
        db = AHKDocsDB()

        if sys.argv[1] == 'search':
            query = ' '.join(sys.argv[2:])
            results = db.search(query)
            for result in results:
                format_result(result, 'search')

        elif sys.argv[1] == 'function':
            result = db.get_function(sys.argv[2])
            if result:
                format_result(result, 'function')
            else:
                print(f"Function '{sys.argv[2]}' not found")

        elif sys.argv[1] == 'object':
            result = db.get_object(sys.argv[2])
            if result:
                format_result(result, 'object')
            else:
                print(f"Object '{sys.argv[2]}' not found")

        elif sys.argv[1] == 'stats':
            stats = db.get_statistics()
            print(json.dumps(stats, indent=2))

        db.close()
    else:
        # Interactive mode
        interactive_mode()
