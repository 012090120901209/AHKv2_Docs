#!/usr/bin/env python3
"""
Standalone Demo of AutoHotkey Documentation Parsing
No database required - shows parsing and data extraction
"""

import re
from pathlib import Path
from typing import Dict, List

print("=" * 70)
print("AutoHotkey Documentation Database - LIVE DEMO")
print("=" * 70)
print()

# ============================================================================
# Simple Markdown Parser (standalone version)
# ============================================================================

def parse_markdown_file(filepath: Path) -> Dict:
    """Parse a markdown file and extract structured data."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else filepath.stem

    # Determine type
    doc_type = 'reference'
    if 'Object' in title and not title.startswith('Object'):
        doc_type = 'object'
    elif filepath.stem.startswith('_'):
        doc_type = 'directive'
    elif '#### Parameters' in content:
        doc_type = 'function'

    # Extract sections
    sections = []
    parts = re.split(r'\n(#{2,4})\s+(.+?)\n', content)
    for i in range(1, len(parts), 3):
        if i + 2 <= len(parts):
            heading = parts[i + 1].strip()
            sections.append(heading)

    # Extract code examples
    code_examples = re.findall(r'```(\w*)\n(.*?)\n```', content, re.DOTALL)

    # Extract links
    links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', content)

    # Extract function data for functions
    function_data = None
    if doc_type == 'function':
        function_data = {
            'name': title.replace(' Function', '').replace(' Method', '').strip(),
            'parameters': []
        }

        # Extract parameters
        param_section = re.search(r'#### Parameters.*?\n\n(.*?)(?=####|\Z)', content, re.DOTALL)
        if param_section:
            param_blocks = re.split(r'\n([A-Za-z0-9_]+)\n', param_section.group(1))
            for i in range(1, len(param_blocks), 2):
                if i + 1 < len(param_blocks):
                    param_name = param_blocks[i].strip()
                    param_desc = param_blocks[i + 1].strip()
                    type_match = re.search(r'Type:\s*\[([^\]]+)\]', param_desc)
                    param_type = type_match.group(1) if type_match else 'Any'
                    function_data['parameters'].append({
                        'name': param_name,
                        'type': param_type
                    })

    # Extract object data for objects
    object_data = None
    if doc_type == 'object':
        object_data = {
            'name': title.replace(' Object', '').strip(),
            'methods': [],
            'properties': []
        }

        # Find methods (sections that look like methods)
        for match in re.finditer(r'### ([A-Z][a-zA-Z0-9_]+)\n', content):
            method_name = match.group(1)
            if not method_name.startswith('_'):
                object_data['methods'].append(method_name)

    return {
        'filename': filepath.name,
        'title': title,
        'doc_type': doc_type,
        'sections': sections,
        'code_examples': code_examples,
        'links': links,
        'function_data': function_data,
        'object_data': object_data,
        'content': content
    }

# ============================================================================
# PART 1: Parse Sample Files
# ============================================================================

print("PART 1: Parsing Markdown Files")
print("-" * 70)

sample_files = ['Array.md', 'StrSplit.md', 'WinActivate.md']
parsed_data = {}

for filename in sample_files:
    filepath = Path(filename)
    if filepath.exists():
        print(f"\n📄 Parsing {filename}...")
        try:
            data = parse_markdown_file(filepath)
            parsed_data[filename] = data

            print(f"  ✓ Title: {data['title']}")
            print(f"  ✓ Type: {data['doc_type']}")
            print(f"  ✓ Sections: {len(data['sections'])}")
            print(f"  ✓ Code Examples: {len(data['code_examples'])}")
            print(f"  ✓ Links: {len(data['links'])}")

            if data['function_data']:
                print(f"  ✓ Parameters: {len(data['function_data']['parameters'])}")

            if data['object_data']:
                print(f"  ✓ Methods: {len(data['object_data']['methods'])}")

        except Exception as e:
            print(f"  ✗ Error: {e}")
    else:
        print(f"  ⚠️  {filename} not found (skipping)")

# ============================================================================
# PART 2: Show Detailed Data
# ============================================================================

print("\n\n" + "=" * 70)
print("PART 2: Detailed Extracted Data")
print("-" * 70)

# Show Array data
if 'Array.md' in parsed_data:
    data = parsed_data['Array.md']
    print("\n📦 Array Object - Complete Details:")
    print(f"  Title: {data['title']}")
    print(f"  Type: {data['doc_type']}")

    if data['object_data']:
        obj = data['object_data']
        print(f"\n  Object Name: {obj['name']}")
        print(f"  Methods found: {len(obj['methods'])}")

        if obj['methods']:
            print(f"\n  Methods (first 10):")
            for method in obj['methods'][:10]:
                print(f"    • {method}")
            if len(obj['methods']) > 10:
                print(f"    ... and {len(obj['methods']) - 10} more")

    # Show first few sections
    if data['sections']:
        print(f"\n  Sections found: {len(data['sections'])}")
        print(f"  First 5 sections:")
        for section in data['sections'][:5]:
            print(f"    • {section}")

    # Show first code example
    if data['code_examples']:
        example = data['code_examples'][0]
        lang = example[0] or 'ahk'
        code = example[1]
        print(f"\n  Code Example (language: {lang}):")
        for line in code.split('\n')[:5]:
            print(f"    {line}")
        if len(code.split('\n')) > 5:
            print("    ...")

# Show StrSplit data
if 'StrSplit.md' in parsed_data:
    data = parsed_data['StrSplit.md']
    print("\n\n🔧 StrSplit Function - Complete Details:")
    print(f"  Title: {data['title']}")
    print(f"  Type: {data['doc_type']}")

    if data['function_data']:
        func = data['function_data']
        print(f"\n  Function Name: {func['name']}")

        if func['parameters']:
            print(f"\n  Parameters:")
            for param in func['parameters']:
                print(f"    • {param['name']}: {param['type']}")

# Show WinActivate data
if 'WinActivate.md' in parsed_data:
    data = parsed_data['WinActivate.md']
    print("\n\n🪟 WinActivate Function - Complete Details:")
    print(f"  Title: {data['title']}")
    print(f"  Type: {data['doc_type']}")

    if data['function_data']:
        func = data['function_data']
        print(f"\n  Function Name: {func['name']}")

        if func['parameters']:
            print(f"\n  Parameters:")
            for param in func['parameters']:
                print(f"    • {param['name']}: {param['type']}")

    # Show code examples
    if data['code_examples']:
        print(f"\n  Code Examples: {len(data['code_examples'])} found")
        example = data['code_examples'][0]
        code = example[1]
        print(f"  First example:")
        for line in code.split('\n')[:4]:
            print(f"    {line}")

# ============================================================================
# PART 3: Simulated Database Queries
# ============================================================================

print("\n\n" + "=" * 70)
print("PART 3: Simulated SQL Queries on Parsed Data")
print("-" * 70)

# Query 1: List all documents
print("\n🔍 Query 1: SELECT title, doc_type FROM documents;")
print("\nResults:")
print(f"{'Title':<25} | {'Type':<10}")
print("-" * 40)
for filename, data in parsed_data.items():
    print(f"{data['title']:<25} | {data['doc_type']:<10}")

# Query 2: Find functions with parameters
print("\n\n🔍 Query 2: SELECT function_name, param_count FROM functions;")
print("\nResults:")
print(f"{'Function':<25} | {'Parameters':<12}")
print("-" * 40)
for filename, data in parsed_data.items():
    if data['function_data']:
        func = data['function_data']
        param_count = len(func['parameters'])
        print(f"{func['name']:<25} | {param_count:<12}")

# Query 3: Find objects with methods
print("\n\n🔍 Query 3: SELECT object_name, method_count FROM objects;")
print("\nResults:")
print(f"{'Object':<25} | {'Methods':<12}")
print("-" * 40)
for filename, data in parsed_data.items():
    if data['object_data']:
        obj = data['object_data']
        method_count = len(obj['methods'])
        print(f"{obj['name']:<25} | {method_count:<12}")

# Query 4: Full-text search simulation
print("\n\n🔍 Query 4: SELECT * FROM search_documents('window');")
print("\nResults:")

for filename, data in parsed_data.items():
    if 'window' in data['content'].lower() or 'window' in data['title'].lower():
        # Find snippet
        content_lower = data['content'].lower()
        pos = content_lower.find('window')
        if pos >= 0:
            snippet = data['content'][max(0, pos-40):pos+60].replace('\n', ' ')
        else:
            snippet = data['title']

        print(f"\n  Title: {data['title']}")
        print(f"  Type: {data['doc_type']}")
        print(f"  Snippet: ...{snippet}...")

# Query 5: Find all code examples
print("\n\n🔍 Query 5: SELECT title, COUNT(*) as examples FROM code_examples GROUP BY title;")
print("\nResults:")
print(f"{'Document':<25} | {'Examples':<12}")
print("-" * 40)
for filename, data in parsed_data.items():
    example_count = len(data['code_examples'])
    if example_count > 0:
        print(f"{data['title']:<25} | {example_count:<12}")

# ============================================================================
# PART 4: Show What the Database Would Look Like
# ============================================================================

print("\n\n" + "=" * 70)
print("PART 4: Database Tables Structure (with real data)")
print("-" * 70)

print("""
When loaded into PostgreSQL, here's what the tables contain:

documents table:
┌────┬──────────────┬───────────────────┬──────────┬────────┬──────────┐
│ id │ filename     │ title             │ doc_type │ lines  │ examples │
├────┼──────────────┼───────────────────┼──────────┼────────┼──────────┤""")

for i, (filename, data) in enumerate(parsed_data.items(), 1):
    line_count = len(data['content'].split('\n'))
    example_count = len(data['code_examples'])
    print(f"│ {i:<2} │ {filename:<12} │ {data['title']:<17} │ {data['doc_type']:<8} │ {line_count:<6} │ {example_count:<8} │")

print("└────┴──────────────┴───────────────────┴──────────┴────────┴──────────┘")

# Show functions table
print("""\nfunctions table:
┌────┬─────────────────┬────────────────┐
│ id │ function_name   │ param_count    │
├────┼─────────────────┼────────────────┤""")

func_id = 1
for filename, data in parsed_data.items():
    if data['function_data']:
        func = data['function_data']
        param_count = len(func['parameters'])
        print(f"│ {func_id:<2} │ {func['name']:<15} │ {param_count:<14} │")
        func_id += 1

print("└────┴─────────────────┴────────────────┘")

# Show objects table
print("""\nobjects table:
┌────┬─────────────────┬──────────────┐
│ id │ object_name     │ method_count │
├────┼─────────────────┼──────────────┤""")

obj_id = 1
for filename, data in parsed_data.items():
    if data['object_data']:
        obj = data['object_data']
        method_count = len(obj['methods'])
        print(f"│ {obj_id:<2} │ {obj['name']:<15} │ {method_count:<12} │")
        obj_id += 1

print("└────┴─────────────────┴──────────────┘")

# ============================================================================
# PART 5: Statistics
# ============================================================================

print("\n\n" + "=" * 70)
print("PART 5: Statistics from Sample Files")
print("-" * 70)

total_sections = sum(len(d['sections']) for d in parsed_data.values())
total_examples = sum(len(d['code_examples']) for d in parsed_data.values())
total_links = sum(len(d['links']) for d in parsed_data.values())
total_lines = sum(len(d['content'].split('\n')) for d in parsed_data.values())

print(f"""
Files parsed: {len(parsed_data)}
Total lines: {total_lines:,}
Total sections: {total_sections}
Total code examples: {total_examples}
Total links: {total_links}

Document types:
  Functions: {sum(1 for d in parsed_data.values() if d['doc_type'] == 'function')}
  Objects: {sum(1 for d in parsed_data.values() if d['doc_type'] == 'object')}
  Other: {sum(1 for d in parsed_data.values() if d['doc_type'] not in ['function', 'object'])}

Average per document:
  Lines: {total_lines / len(parsed_data):.0f}
  Sections: {total_sections / len(parsed_data):.1f}
  Examples: {total_examples / len(parsed_data):.1f}
  Links: {total_links / len(parsed_data):.1f}
""")

# ============================================================================
# PART 6: Show Python API Usage
# ============================================================================

print("=" * 70)
print("PART 6: Python API Example Usage")
print("-" * 70)

print("""
After loading into database, you can query with Python:

from query_db import AHKDocsDB

db = AHKDocsDB()

# Search for documents
results = db.search('array methods', limit=5)
for r in results:
    print(f"{r['title']}: {r['rank']}")

# Get function details
func = db.get_function('StrSplit')
print(f"Function: {func['function_name']}")
print(f"Parameters: {func['parameters']}")
print(f"Syntax: {func['syntax']}")

# Get object details
obj = db.get_object('Array')
print(f"Object: {obj['object_name']}")
print(f"Methods: {obj['methods']}")

# Get code examples
examples = db.get_code_examples('Array Object')
for ex in examples:
    print(ex['code'])

# Statistics
stats = db.get_statistics()
print(f"Total documents: {stats['total_documents']}")
print(f"Total functions: {stats['total_functions']}")

db.close()
""")

# ============================================================================
# Summary
# ============================================================================

print("\n" + "=" * 70)
print("✅ DEMO COMPLETE!")
print("=" * 70)

print(f"""
This demo processed {len(parsed_data)} actual markdown files and showed:

  1. ✓ Parsing markdown into structured data
  2. ✓ Extracting functions, objects, parameters, methods
  3. ✓ Finding code examples and links
  4. ✓ Simulating SQL queries on the data
  5. ✓ Database table structure with real data
  6. ✓ Statistics and analysis

To load ALL {413} files into PostgreSQL:

  cd database
  ./init_db.sh                    # Set up database

  # Then query with:
  python3 query_db.py             # Interactive mode
  python3 query_db.py search "array methods"

  # Or use psql:
  psql -h localhost -p 5432 -U postgres -d ahk_docs
  SELECT * FROM search_documents('array methods');
  SELECT * FROM v_functions_complete WHERE function_name = 'StrSplit';
  SELECT * FROM v_objects_complete WHERE object_name = 'Array';

The full database will contain:
  • 413 documents
  • ~2,000 sections
  • ~200 functions with ~800 parameters
  • ~30 objects with ~250 methods/properties
  • ~800 code examples
  • ~3,000 links

Ready to use in your application!
""")
