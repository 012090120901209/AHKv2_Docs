#!/usr/bin/env python3
"""
Working Demo of AutoHotkey Documentation Database
Demonstrates parsing, loading, and querying with real data
"""

import sys
import os
from pathlib import Path

# Add database directory to path
sys.path.insert(0, str(Path(__file__).parent / 'database'))

print("=" * 70)
print("AutoHotkey Documentation Database - LIVE DEMO")
print("=" * 70)
print()

# ============================================================================
# PART 1: Parse Sample Markdown Files
# ============================================================================

print("PART 1: Parsing Markdown Files")
print("-" * 70)

from database.load_data import MarkdownParser

parser = MarkdownParser()

# Parse a few sample files
sample_files = ['Array.md', 'StrSplit.md', 'Gui.md']
parsed_data = {}

for filename in sample_files:
    filepath = Path(filename)
    if filepath.exists():
        print(f"\n📄 Parsing {filename}...")

        try:
            metadata = parser.parse_file(filepath, Path('.'))
            parsed_data[filename] = metadata

            print(f"  ✓ Title: {metadata['title']}")
            print(f"  ✓ Type: {metadata['doc_type']}")
            print(f"  ✓ Sections: {len(metadata['sections'])}")
            print(f"  ✓ Code Examples: {len(metadata['code_examples'])}")
            print(f"  ✓ Links: {len(metadata['links'])}")

            # Show function/object specific data
            if metadata['doc_type'] == 'function' and 'function_data' in metadata:
                func = metadata['function_data']
                print(f"  ✓ Function: {func['function_name']}")
                print(f"  ✓ Parameters: {len(func.get('parameters', []))}")
                if func.get('syntax'):
                    print(f"  ✓ Syntax: {func['syntax'][:60]}...")

            elif metadata['doc_type'] == 'object' and 'object_data' in metadata:
                obj = metadata['object_data']
                print(f"  ✓ Object: {obj['object_name']}")
                print(f"  ✓ Properties: {len(obj.get('properties', []))}")
                print(f"  ✓ Methods: {len(obj.get('methods', []))}")

        except Exception as e:
            print(f"  ✗ Error: {e}")
    else:
        print(f"  ⚠️  {filename} not found (skipping)")

# ============================================================================
# PART 2: Show Extracted Data Structure
# ============================================================================

print("\n\n" + "=" * 70)
print("PART 2: Extracted Data Examples")
print("-" * 70)

# Show Array.md data if parsed
if 'Array.md' in parsed_data:
    data = parsed_data['Array.md']

    print("\n📦 Array Object Data:")
    print(f"  Title: {data['title']}")
    print(f"  Type: {data['doc_type']}")
    print(f"  Description: {data.get('description', 'N/A')[:100]}...")

    if 'object_data' in data:
        obj = data['object_data']
        print(f"\n  Object Name: {obj['object_name']}")
        print(f"  Extends: {obj.get('extends', 'Object')}")

        if obj.get('methods'):
            print(f"\n  Methods ({len(obj['methods'])} found):")
            for method in obj['methods'][:5]:
                print(f"    - {method['method_name']}")
            if len(obj['methods']) > 5:
                print(f"    ... and {len(obj['methods']) - 5} more")

        if obj.get('properties'):
            print(f"\n  Properties ({len(obj['properties'])} found):")
            for prop in obj['properties'][:5]:
                print(f"    - {prop['property_name']}")

    # Show sections
    if data.get('sections'):
        print(f"\n  Sections ({len(data['sections'])} found):")
        for section in data['sections'][:5]:
            print(f"    - [{section['section_type']}] {section['heading']}")

    # Show code examples
    if data.get('code_examples'):
        print(f"\n  Code Examples ({len(data['code_examples'])} found):")
        example = data['code_examples'][0]
        print(f"    Language: {example['language']}")
        print(f"    Code Preview:")
        for line in example['code'].split('\n')[:3]:
            print(f"      {line}")
        if len(example['code'].split('\n')) > 3:
            print(f"      ...")

# Show StrSplit.md data if parsed
if 'StrSplit.md' in parsed_data:
    data = parsed_data['StrSplit.md']

    print("\n\n🔧 StrSplit Function Data:")
    print(f"  Title: {data['title']}")
    print(f"  Type: {data['doc_type']}")

    if 'function_data' in data:
        func = data['function_data']
        print(f"\n  Function Name: {func['function_name']}")

        if func.get('syntax'):
            print(f"  Syntax: {func['syntax'][:80]}...")

        if func.get('return_type'):
            print(f"  Return Type: {func['return_type']}")

        if func.get('parameters'):
            print(f"\n  Parameters ({len(func['parameters'])} found):")
            for param in func['parameters']:
                optional = " (optional)" if param['is_optional'] else ""
                param_type = param.get('param_type', 'Any')
                print(f"    - {param['param_name']}: {param_type}{optional}")

# ============================================================================
# PART 3: Simulate Database Queries
# ============================================================================

print("\n\n" + "=" * 70)
print("PART 3: Simulated Database Queries")
print("-" * 70)

# Simulate: Find all functions
print("\n🔍 Query: Find all functions")
print("SQL: SELECT function_name, return_type FROM functions;")
print("\nResults:")

for filename, data in parsed_data.items():
    if data['doc_type'] == 'function' and 'function_data' in data:
        func = data['function_data']
        return_type = func.get('return_type', 'N/A')
        print(f"  {func['function_name']:<20} | {return_type}")

# Simulate: Find all objects
print("\n🔍 Query: Find all objects with methods")
print("SQL: SELECT object_name, extends, COUNT(methods) FROM objects;")
print("\nResults:")

for filename, data in parsed_data.items():
    if data['doc_type'] == 'object' and 'object_data' in data:
        obj = data['object_data']
        extends = obj.get('extends', 'Object')
        method_count = len(obj.get('methods', []))
        print(f"  {obj['object_name']:<20} | extends {extends:<15} | {method_count} methods")

# Simulate: Search for code examples
print("\n🔍 Query: Find code examples containing 'MsgBox'")
print("SQL: SELECT title, code FROM code_examples WHERE code LIKE '%MsgBox%';")
print("\nResults:")

found_examples = 0
for filename, data in parsed_data.items():
    for example in data.get('code_examples', []):
        if 'MsgBox' in example['code'] or 'msgbox' in example['code'].lower():
            print(f"\n  From: {data['title']}")
            print(f"  Code:")
            for line in example['code'].split('\n')[:4]:
                print(f"    {line}")
            found_examples += 1
            break  # Just show first example per file

if found_examples == 0:
    print("  (No examples with MsgBox found in sample files)")

# Simulate: Full-text search
print("\n🔍 Query: Full-text search for 'array'")
print("SQL: SELECT * FROM search_documents('array', NULL, NULL, 5);")
print("\nResults:")

for filename, data in parsed_data.items():
    content_lower = data['content'].lower()
    title_lower = data['title'].lower()

    if 'array' in content_lower or 'array' in title_lower:
        # Calculate simple relevance score
        score = content_lower.count('array') + title_lower.count('array') * 5

        # Get snippet
        snippet_start = content_lower.find('array')
        if snippet_start >= 0:
            snippet = data['content'][max(0, snippet_start-50):snippet_start+100]
            snippet = snippet.replace('\n', ' ')
        else:
            snippet = data.get('description', '')[:100]

        print(f"\n  Title: {data['title']}")
        print(f"  Type: {data['doc_type']}")
        print(f"  Score: {score}")
        print(f"  Snippet: ...{snippet}...")

# ============================================================================
# PART 4: Show Database Schema Preview
# ============================================================================

print("\n\n" + "=" * 70)
print("PART 4: Database Schema Preview")
print("-" * 70)

print("""
When loaded into PostgreSQL, the data structure would be:

documents table:
┌────┬──────────┬──────────────┬──────────┬─────────────┐
│ id │ filename │ title        │ doc_type │ category_id │
├────┼──────────┼──────────────┼──────────┼─────────────┤
│ 1  │ Array.md │ Array Object │ object   │ 2           │
│ 2  │ StrSpl...│ StrSplit     │ function │ 1           │
│ 3  │ Gui.md   │ Gui Object   │ object   │ 2           │
└────┴──────────┴──────────────┴──────────┴─────────────┘

functions table:
┌────┬─────────────┬────────────┬─────────────┬────────────┐
│ id │ document_id │ function_n │ return_type │ syntax     │
├────┼─────────────┼────────────┼─────────────┼────────────┤
│ 1  │ 2           │ StrSplit   │ Array       │ StrSplit(S │
└────┴─────────────┴────────────┴─────────────┴────────────┘

function_parameters table:
┌────┬─────────────┬────────────┬────────────┬────────────┐
│ id │ function_id │ param_name │ param_type │ is_optiona │
├────┼─────────────┼────────────┼────────────┼────────────┤
│ 1  │ 1           │ String     │ String     │ false      │
│ 2  │ 1           │ Delimiters │ String     │ true       │
│ 3  │ 1           │ OmitChars  │ String     │ true       │
└────┴─────────────┴────────────┴────────────┴────────────┘

objects table:
┌────┬─────────────┬─────────────┬─────────┐
│ id │ document_id │ object_name │ extends │
├────┼─────────────┼─────────────┼─────────┤
│ 1  │ 1           │ Array       │ Object  │
│ 2  │ 3           │ Gui         │ Object  │
└────┴─────────────┴─────────────┴─────────┘

object_methods table:
┌────┬───────────┬─────────────┬──────────────────────┐
│ id │ object_id │ method_name │ description          │
├────┼───────────┼─────────────┼──────────────────────┤
│ 1  │ 1         │ Push        │ Appends values to... │
│ 2  │ 1         │ Pop         │ Removes and returns..│
│ 3  │ 1         │ Clone       │ Returns a shallow... │
└────┴───────────┴─────────────┴──────────────────────┘
""")

# ============================================================================
# PART 5: Show Statistics
# ============================================================================

print("\n" + "=" * 70)
print("PART 5: Statistics from Sample Files")
print("-" * 70)

total_sections = sum(len(d['sections']) for d in parsed_data.values())
total_examples = sum(len(d['code_examples']) for d in parsed_data.values())
total_links = sum(len(d['links']) for d in parsed_data.values())

print(f"""
Files parsed: {len(parsed_data)}
Total sections: {total_sections}
Total code examples: {total_examples}
Total links: {total_links}

Document types:
  Functions: {sum(1 for d in parsed_data.values() if d['doc_type'] == 'function')}
  Objects: {sum(1 for d in parsed_data.values() if d['doc_type'] == 'object')}

Average per document:
  Sections: {total_sections / len(parsed_data):.1f}
  Examples: {total_examples / len(parsed_data):.1f}
  Links: {total_links / len(parsed_data):.1f}
""")

# ============================================================================
# Summary
# ============================================================================

print("=" * 70)
print("✅ DEMO COMPLETE!")
print("=" * 70)
print("""
This demo showed:
  1. ✓ Parsing markdown files into structured data
  2. ✓ Extracting functions, objects, parameters, methods
  3. ✓ Finding code examples and links
  4. ✓ Simulating database queries
  5. ✓ Database schema structure

To run with full database:
  cd database
  ./init_db.sh                    # Initialize PostgreSQL
  python3 query_db.py             # Interactive queries
  python3 query_db.py search "array methods"  # Search

For live database queries:
  psql -h localhost -p 5432 -U postgres -d ahk_docs

  SELECT * FROM search_documents('array methods');
  SELECT * FROM v_functions_complete WHERE function_name = 'StrSplit';
  SELECT * FROM v_objects_complete WHERE object_name = 'Array';
""")
