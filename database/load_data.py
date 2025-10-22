#!/usr/bin/env python3
"""
Load AutoHotkey documentation into PostgreSQL database.
Parses markdown files and extracts structured data.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import psycopg2
from psycopg2.extras import execute_batch, Json
from datetime import datetime

class MarkdownParser:
    """Parse markdown files and extract structured information."""

    def __init__(self):
        self.function_pattern = re.compile(r'^#\s+(.+?)(?:\s+Function|\s+Method)?$', re.MULTILINE)
        self.object_pattern = re.compile(r'^#\s+(.+?)\s+Object$', re.MULTILINE)

    def parse_file(self, filepath: Path, base_dir: Path = None) -> Dict:
        """Parse a markdown file and extract all structured data."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Calculate relative path
        if base_dir:
            rel_path = str(filepath.relative_to(base_dir))
        else:
            rel_path = filepath.name

        # Basic metadata
        metadata = {
            'filename': filepath.name,
            'file_path': rel_path,
            'content': content,
            'raw_markdown': content,
        }

        # Extract title
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        metadata['title'] = title_match.group(1).strip() if title_match else filepath.stem

        # Determine document type
        metadata['doc_type'] = self.determine_doc_type(filepath, content, metadata['title'])

        # Extract sections
        metadata['sections'] = self.extract_sections(content)

        # Extract code examples
        metadata['code_examples'] = self.extract_code_examples(content)

        # Extract links
        metadata['links'] = self.extract_links(content)

        # Extract function/object specific data
        if metadata['doc_type'] == 'function':
            metadata['function_data'] = self.extract_function_data(content, metadata['title'])
        elif metadata['doc_type'] == 'object':
            metadata['object_data'] = self.extract_object_data(content, metadata['title'])

        # Calculate statistics
        metadata['line_count'] = len(content.split('\n'))
        metadata['word_count'] = len(content.split())
        metadata['has_code_examples'] = len(metadata['code_examples']) > 0
        metadata['has_syntax_section'] = '```Syntax' in content or '``` Syntax' in content
        metadata['has_parameters'] = '#### Parameters' in content or '### Parameters' in content

        # Extract description (first paragraph after title)
        description_match = re.search(r'^#\s+.+?\n\n(.+?)\n\n', content, re.MULTILINE | re.DOTALL)
        metadata['description'] = description_match.group(1).strip() if description_match else None

        return metadata

    def determine_doc_type(self, filepath: Path, content: str, title: str) -> str:
        """Determine the document type."""
        name = filepath.stem

        # Check path-based categorization
        parts = Path(filepath).parts
        if len(parts) > 1:
            if 'objects' in parts:
                return 'object'
            elif 'functions' in parts:
                return 'function'
            elif 'directives' in parts or name.startswith('_'):
                return 'directive'
            elif 'guides' in parts:
                return 'guide'
            elif 'reference' in parts:
                return 'reference'
            elif 'changelog' in parts or name.startswith('v') or 'ChangeLog' in name:
                return 'changelog'

        # Check content-based patterns
        if 'Object' in title and not title.startswith('Object'):
            return 'object'
        elif name.startswith('_'):
            return 'directive'
        elif name in ['Tutorial', 'FAQ', 'Concepts', 'Scripts', 'Program']:
            return 'guide'
        elif name in ['ChangeLog', 'v2-changes', 'v1-changes', 'Compat']:
            return 'changelog'
        elif '#### Parameters' in content or 'return' in content.lower():
            return 'function'

        return 'reference'

    def extract_sections(self, content: str) -> List[Dict]:
        """Extract sections with headings."""
        sections = []

        # Split by headers (h2, h3, h4)
        parts = re.split(r'\n(#{2,4})\s+(.+?)\n', content)

        current_section = None
        section_order = 0

        for i in range(1, len(parts), 3):
            if i + 2 > len(parts):
                break

            heading_level = len(parts[i])
            heading = parts[i + 1].strip()
            section_content = parts[i + 2].strip() if i + 2 < len(parts) else ''

            # Determine section type
            section_type = self.classify_section(heading)

            sections.append({
                'heading': heading,
                'heading_level': heading_level,
                'content': section_content,
                'section_type': section_type,
                'section_order': section_order,
                'word_count': len(section_content.split()),
                'has_code': '```' in section_content
            })

            section_order += 1

        return sections

    def classify_section(self, heading: str) -> str:
        """Classify section by heading."""
        heading_lower = heading.lower()

        if 'parameter' in heading_lower:
            return 'parameters'
        elif 'return' in heading_lower:
            return 'return_value'
        elif 'example' in heading_lower:
            return 'examples'
        elif 'remark' in heading_lower or 'note' in heading_lower:
            return 'remarks'
        elif 'syntax' in heading_lower:
            return 'syntax'
        elif 'description' in heading_lower:
            return 'description'
        elif 'error' in heading_lower or 'exception' in heading_lower:
            return 'errors'
        elif 'see also' in heading_lower or 'related' in heading_lower:
            return 'related'
        else:
            return 'general'

    def extract_code_examples(self, content: str) -> List[Dict]:
        """Extract code blocks."""
        examples = []

        # Find all code blocks
        code_blocks = re.finditer(r'```(\w*)\n(.*?)\n```', content, re.DOTALL)

        for i, match in enumerate(code_blocks):
            language = match.group(1) or 'ahk'
            code = match.group(2).strip()

            # Get surrounding context for description
            start_pos = match.start()
            context_start = max(0, start_pos - 200)
            context = content[context_start:start_pos]

            # Look for description in preceding paragraph
            desc_match = re.search(r'([^\n]+)\n*$', context)
            description = desc_match.group(1).strip() if desc_match else None

            examples.append({
                'code': code,
                'language': language,
                'description': description,
                'example_order': i
            })

        return examples

    def extract_links(self, content: str) -> List[Dict]:
        """Extract markdown links."""
        links = []

        link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'

        for match in re.finditer(link_pattern, content):
            link_text = match.group(1)
            link_url = match.group(2)

            is_external = link_url.startswith('http')

            links.append({
                'link_text': link_text,
                'link_url': link_url,
                'is_external': is_external
            })

        return links

    def extract_function_data(self, content: str, title: str) -> Dict:
        """Extract function-specific data."""
        function_data = {
            'function_name': title.replace(' Function', '').replace(' Method', '').strip(),
            'parameters': []
        }

        # Extract syntax
        syntax_match = re.search(r'```\s*Syntax\n(.+?)\n```', content, re.DOTALL)
        if syntax_match:
            function_data['syntax'] = syntax_match.group(1).strip()

        # Extract return value
        return_match = re.search(r'#### Return Value.*?\n\n(.*?)\n\n', content, re.DOTALL)
        if return_match:
            return_text = return_match.group(1).strip()
            # Extract type from "Type: [Integer]"
            type_match = re.search(r'Type:\s*\[([^\]]+)\]', return_text)
            if type_match:
                function_data['return_type'] = type_match.group(1)
            function_data['return_description'] = return_text

        # Extract parameters
        param_section = re.search(r'#### Parameters.*?\n\n(.*?)(?=####|\Z)', content, re.DOTALL)
        if param_section:
            param_text = param_section.group(1)
            function_data['parameters'] = self.parse_parameters(param_text)

        return function_data

    def parse_parameters(self, param_text: str) -> List[Dict]:
        """Parse parameter definitions."""
        parameters = []

        # Split by parameter name (line that doesn't start with :)
        param_blocks = re.split(r'\n([A-Za-z0-9_]+)\n', param_text)

        for i in range(1, len(param_blocks), 2):
            if i + 1 >= len(param_blocks):
                break

            param_name = param_blocks[i].strip()
            param_desc = param_blocks[i + 1].strip()

            # Extract type
            type_match = re.search(r'Type:\s*\[([^\]]+)\]', param_desc)
            param_type = type_match.group(1) if type_match else None

            # Check if optional
            is_optional = '[optional]' in param_desc.lower() or ', optional' in param_desc.lower()

            # Extract default value
            default_match = re.search(r'[Dd]efault[s]?[:\s]+([^.\n]+)', param_desc)
            default_value = default_match.group(1).strip() if default_match else None

            parameters.append({
                'param_name': param_name,
                'param_type': param_type,
                'is_optional': is_optional,
                'default_value': default_value,
                'description': param_desc,
                'param_order': len(parameters)
            })

        return parameters

    def extract_object_data(self, content: str, title: str) -> Dict:
        """Extract object-specific data."""
        object_data = {
            'object_name': title.replace(' Object', '').strip(),
            'properties': [],
            'methods': []
        }

        # Extract extends/inheritance
        extends_match = re.search(r'class\s+\w+\s+extends\s+(\w+)', content)
        if extends_match:
            object_data['extends'] = extends_match.group(1)

        # Extract properties (look for property sections)
        prop_section = re.search(r'### (\w+)\n\nRetrieves or sets', content, re.MULTILINE)
        if prop_section:
            # Find all properties
            for match in re.finditer(r'### (\w+)\n\nRetrieves or sets (.+?)\.', content):
                object_data['properties'].append({
                    'property_name': match.group(1),
                    'description': match.group(2)
                })

        # Extract methods (look for method sections)
        for match in re.finditer(r'### (\w+)\n\n(.+?)\n\n```', content, re.DOTALL):
            method_name = match.group(1)
            if method_name != '__New' and not method_name.startswith('_'):
                object_data['methods'].append({
                    'method_name': method_name,
                    'description': match.group(2).strip()
                })

        return object_data


class DatabaseLoader:
    """Load parsed data into PostgreSQL."""

    def __init__(self, connection_string: str):
        self.conn = psycopg2.connect(connection_string)
        self.cursor = self.conn.cursor()

    def load_document(self, metadata: Dict) -> int:
        """Load a document and return its ID."""

        # Get category ID
        category_id = self.get_or_create_category(metadata['file_path'])

        # Insert document
        self.cursor.execute("""
            INSERT INTO documents (
                filename, file_path, title, doc_type, category_id,
                description, content, raw_markdown,
                line_count, word_count, has_code_examples,
                has_syntax_section, has_parameters
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
            RETURNING id
        """, (
            metadata['filename'],
            metadata['file_path'],
            metadata['title'],
            metadata['doc_type'],
            category_id,
            metadata.get('description'),
            metadata['content'][:50000],  # Limit content length
            metadata['raw_markdown'][:100000],
            metadata['line_count'],
            metadata['word_count'],
            metadata['has_code_examples'],
            metadata['has_syntax_section'],
            metadata['has_parameters']
        ))

        document_id = self.cursor.fetchone()[0]

        # Load sections
        self.load_sections(document_id, metadata['sections'])

        # Load code examples
        self.load_code_examples(document_id, metadata['code_examples'])

        # Load links
        self.load_links(document_id, metadata['links'])

        # Load function/object specific data
        if metadata['doc_type'] == 'function' and 'function_data' in metadata:
            self.load_function(document_id, metadata['function_data'])
        elif metadata['doc_type'] == 'object' and 'object_data' in metadata:
            self.load_object(document_id, metadata['object_data'])

        return document_id

    def get_or_create_category(self, file_path: str) -> Optional[int]:
        """Get or create category based on file path."""
        parts = Path(file_path).parts

        if len(parts) < 2:
            return None

        category_name = parts[0] if parts[0] != '.' else None

        if not category_name:
            return None

        self.cursor.execute(
            "SELECT id FROM categories WHERE name = %s",
            (category_name,)
        )
        result = self.cursor.fetchone()

        if result:
            return result[0]

        return None

    def load_sections(self, document_id: int, sections: List[Dict]):
        """Load document sections."""
        for section in sections:
            self.cursor.execute("""
                INSERT INTO sections (
                    document_id, section_type, heading, heading_level,
                    content, section_order, word_count, has_code
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                document_id,
                section['section_type'],
                section['heading'],
                section['heading_level'],
                section['content'][:10000],  # Limit length
                section['section_order'],
                section['word_count'],
                section['has_code']
            ))

    def load_code_examples(self, document_id: int, examples: List[Dict]):
        """Load code examples."""
        for example in examples:
            self.cursor.execute("""
                INSERT INTO code_examples (
                    document_id, code, language, description, example_order
                ) VALUES (%s, %s, %s, %s, %s)
            """, (
                document_id,
                example['code'],
                example['language'],
                example.get('description'),
                example['example_order']
            ))

    def load_links(self, document_id: int, links: List[Dict]):
        """Load document links."""
        for link in links:
            self.cursor.execute("""
                INSERT INTO links (
                    source_document_id, link_text, link_url, is_external
                ) VALUES (%s, %s, %s, %s)
            """, (
                document_id,
                link['link_text'],
                link['link_url'],
                link['is_external']
            ))

    def load_function(self, document_id: int, function_data: Dict):
        """Load function-specific data."""
        self.cursor.execute("""
            INSERT INTO functions (
                document_id, function_name, syntax, return_type, return_description
            ) VALUES (%s, %s, %s, %s, %s)
            RETURNING id
        """, (
            document_id,
            function_data['function_name'],
            function_data.get('syntax'),
            function_data.get('return_type'),
            function_data.get('return_description')
        ))

        function_id = self.cursor.fetchone()[0]

        # Load parameters
        for param in function_data.get('parameters', []):
            self.cursor.execute("""
                INSERT INTO function_parameters (
                    function_id, param_name, param_type, is_optional,
                    default_value, description, param_order
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                function_id,
                param['param_name'],
                param.get('param_type'),
                param['is_optional'],
                param.get('default_value'),
                param.get('description'),
                param['param_order']
            ))

    def load_object(self, document_id: int, object_data: Dict):
        """Load object-specific data."""
        self.cursor.execute("""
            INSERT INTO objects (
                document_id, object_name, extends
            ) VALUES (%s, %s, %s)
            RETURNING id
        """, (
            document_id,
            object_data['object_name'],
            object_data.get('extends')
        ))

        object_id = self.cursor.fetchone()[0]

        # Load properties
        for prop in object_data.get('properties', []):
            self.cursor.execute("""
                INSERT INTO object_properties (
                    object_id, property_name, description
                ) VALUES (%s, %s, %s)
            """, (
                object_id,
                prop['property_name'],
                prop.get('description')
            ))

        # Load methods
        for method in object_data.get('methods', []):
            self.cursor.execute("""
                INSERT INTO object_methods (
                    object_id, method_name, description
                ) VALUES (%s, %s, %s)
            """, (
                object_id,
                method['method_name'],
                method.get('description')
            ))

    def commit(self):
        """Commit transaction."""
        self.conn.commit()

    def close(self):
        """Close database connection."""
        self.cursor.close()
        self.conn.close()


def main():
    """Main loading process."""
    import sys

    # Configuration
    DB_CONFIG = {
        'dbname': os.getenv('POSTGRES_DB', 'ahk_docs'),
        'user': os.getenv('POSTGRES_USER', 'postgres'),
        'password': os.getenv('POSTGRES_PASSWORD', 'postgres'),
        'host': os.getenv('POSTGRES_HOST', 'localhost'),
        'port': os.getenv('POSTGRES_PORT', '5432')
    }

    connection_string = f"dbname={DB_CONFIG['dbname']} user={DB_CONFIG['user']} " \
                       f"password={DB_CONFIG['password']} host={DB_CONFIG['host']} " \
                       f"port={DB_CONFIG['port']}"

    # Get input directory
    input_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    docs_path = Path(input_dir)

    if not docs_path.exists():
        print(f"Error: Directory '{input_dir}' not found")
        sys.exit(1)

    # Find all markdown files
    md_files = list(docs_path.rglob('*.md'))
    print(f"Found {len(md_files)} markdown files")

    # Initialize parser and loader
    parser = MarkdownParser()
    loader = DatabaseLoader(connection_string)

    # Process files
    success_count = 0
    error_count = 0

    for i, filepath in enumerate(md_files, 1):
        try:
            print(f"[{i}/{len(md_files)}] Processing {filepath.name}...", end=' ')

            metadata = parser.parse_file(filepath, docs_path)
            document_id = loader.load_document(metadata)

            print(f"✓ (ID: {document_id})")
            success_count += 1

            # Commit every 10 documents
            if i % 10 == 0:
                loader.commit()
                print(f"  Committed {i} documents")

        except Exception as e:
            print(f"✗ Error: {e}")
            error_count += 1
            continue

    # Final commit
    loader.commit()
    loader.close()

    print("\n" + "=" * 70)
    print(f"LOADING COMPLETE")
    print("=" * 70)
    print(f"Success: {success_count} documents")
    print(f"Errors: {error_count} documents")
    print(f"Database: {DB_CONFIG['dbname']}@{DB_CONFIG['host']}")

if __name__ == '__main__':
    main()
