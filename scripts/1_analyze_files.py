#!/usr/bin/env python3
"""
Analyze markdown files and categorize them for reorganization.
Run this first to preview the reorganization.
"""

import os
import re
from pathlib import Path
from collections import defaultdict
import json

# Categorization rules
CATEGORIES = {
    'functions': {
        'window': r'^(Win|Control|GroupAdd|GroupActivate|GroupClose|GroupDeactivate)',
        'file': r'^(File|Dir)',
        'string': r'^(Str|InStr|Format|SubStr|Trim)',
        'system': r'^(Process|Run|Exit|Reload|Shutdown|Suspend|Pause|Sleep)',
        'input': r'^(Send|Click|Mouse|Input|KeyWait|Hotkey|Hotstring|Block)',
        'gui': r'^(Gui(?!\.md$)|Menu|ToolTip|TrayTip|TraySetIcon|MsgBox|InputBox|FileSelect|DirSelect)',
        'registry': r'^Reg',
        'sound': r'^Sound',
        'monitor': r'^Monitor',
        'clipboard': r'^Clip',
        'misc': None  # Catch-all for other functions
    },
    'objects': [
        'Array', 'Map', 'Object', 'Any', 'Buffer', 'Func', 'Enumerator', 'Functor',
        'Gui', 'GuiControl', 'Menu',
        'File', 'Error',
        'ComValue', 'ComObject', 'ComObjArray'
    ],
    'directives': r'^_',
    'guides': [
        'Tutorial', 'FAQ', 'Concepts', 'Scripts', 'Program',
        'Editors', 'Install', 'Performance',
        'ManageWindows', 'RunPrograms', 'RunExamples',
        'Threads', 'DPIScaling', 'LongPaths'
    ],
    'reference': {
        'hotkeys': ['Hotkeys', 'Hotstrings', 'WriteHotkeys', 'Remap', 'RemapController', 'HotkeyFeatures'],
        'language': ['Language', 'Variables', 'Functions', 'Objects', 'Labels', 'EscapeChar', 'Macros'],
        'tables': ['KeyList', 'Colors', 'Styles', 'SendKeys', 'FontsStandard', 'CLSID-List', 'ImageHandles', 'SendMessageList'],
        'loops': ['Loop', 'LoopFiles', 'LoopRead', 'LoopParse', 'LoopReg', 'For', 'While', 'Until', 'Break', 'Continue'],
        'flow': ['If', 'Else', 'Switch', 'Try', 'Catch', 'Finally', 'Throw', 'Return', 'Goto', 'Block'],
        'misc': None
    },
    'changelog': ['ChangeLog', 'v2-changes', 'v1-changes', 'Compat'],
    'special': ['index', 'index_1', 'index_1_2', 'search', '404', 'settings', 'license', 'Acknowledgements']
}

def categorize_file(filename):
    """Determine the category and subcategory for a file."""
    base = filename.replace('.md', '')

    # Check special files
    if base in CATEGORIES['special']:
        return 'root', base

    # Check changelog
    if base in CATEGORIES['changelog']:
        return 'changelog', None

    # Check directives
    if re.match(CATEGORIES['directives'], base):
        return 'directives', None

    # Check objects
    if base in CATEGORIES['objects']:
        return 'objects', None

    # Check guides
    if base in CATEGORIES['guides']:
        return 'guides', None

    # Check reference subcategories
    for subcat, files in CATEGORIES['reference'].items():
        if files and base in files:
            return 'reference', subcat

    # Check function subcategories
    for subcat, pattern in CATEGORIES['functions'].items():
        if pattern and re.match(pattern, base):
            return 'functions', subcat

    # Check if it's likely a function (has parameters, return value, etc.)
    # For now, default to functions/misc for uncategorized
    return 'functions', 'misc'

def analyze_file_content(filepath):
    """Extract metadata from file content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title (first h1)
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else None

    # Check for code examples
    has_code = bool(re.search(r'^```', content, re.MULTILINE))

    # Count sections
    sections = len(re.findall(r'^#{2,3}\s+', content, re.MULTILINE))

    # Estimate tokens (rough: ~4 chars per token)
    estimated_tokens = len(content) // 4

    # Check for special markers
    has_syntax_block = '```Syntax' in content or '``` Syntax' in content
    has_parameters = '#### Parameters' in content or '### Parameters' in content
    has_examples = '## Example' in content or '### Example' in content

    return {
        'title': title,
        'has_code': has_code,
        'sections': sections,
        'estimated_tokens': estimated_tokens,
        'has_syntax_block': has_syntax_block,
        'has_parameters': has_parameters,
        'has_examples': has_examples,
        'lines': len(content.split('\n'))
    }

def main():
    """Analyze all markdown files and create categorization report."""
    docs_dir = Path('.')
    md_files = sorted(docs_dir.glob('*.md'))

    categorization = defaultdict(lambda: defaultdict(list))
    file_metadata = {}
    stats = defaultdict(int)

    print(f"Analyzing {len(md_files)} markdown files...\n")

    for md_file in md_files:
        category, subcategory = categorize_file(md_file.name)
        metadata = analyze_file_content(md_file)

        # Store categorization
        if subcategory:
            categorization[category][subcategory].append(md_file.name)
        else:
            categorization[category]['_root'].append(md_file.name)

        # Store metadata
        file_metadata[md_file.name] = {
            'category': category,
            'subcategory': subcategory,
            **metadata
        }

        stats[category] += 1

    # Print summary
    print("=" * 70)
    print("CATEGORIZATION SUMMARY")
    print("=" * 70)
    for category in sorted(stats.keys()):
        print(f"\n{category.upper()}: {stats[category]} files")
        if category in categorization:
            for subcat in sorted(categorization[category].keys()):
                files = categorization[category][subcat]
                subcat_name = subcat if subcat != '_root' else '(root)'
                print(f"  {subcat_name}: {len(files)} files")
                if len(files) <= 10:  # Show files if not too many
                    for f in files:
                        print(f"    - {f}")

    # Print detailed stats
    print("\n" + "=" * 70)
    print("CONTENT STATISTICS")
    print("=" * 70)

    total_tokens = sum(m['estimated_tokens'] for m in file_metadata.values())
    total_sections = sum(m['sections'] for m in file_metadata.values())
    files_with_code = sum(1 for m in file_metadata.values() if m['has_code'])
    files_with_examples = sum(1 for m in file_metadata.values() if m['has_examples'])

    print(f"Total estimated tokens: {total_tokens:,}")
    print(f"Total sections: {total_sections:,}")
    print(f"Files with code examples: {files_with_code} ({files_with_code/len(md_files)*100:.1f}%)")
    print(f"Files with examples: {files_with_examples} ({files_with_examples/len(md_files)*100:.1f}%)")

    # Find largest files
    print("\nLargest files (by tokens):")
    sorted_by_tokens = sorted(file_metadata.items(), key=lambda x: x[1]['estimated_tokens'], reverse=True)
    for filename, meta in sorted_by_tokens[:10]:
        print(f"  {filename}: {meta['estimated_tokens']:,} tokens, {meta['lines']} lines")

    # Save detailed report
    output = {
        'categorization': dict(categorization),
        'file_metadata': file_metadata,
        'stats': dict(stats),
        'summary': {
            'total_files': len(md_files),
            'total_tokens': total_tokens,
            'total_sections': total_sections,
            'files_with_code': files_with_code,
            'files_with_examples': files_with_examples
        }
    }

    with open('analysis_report.json', 'w') as f:
        json.dump(output, f, indent=2)

    print("\n" + "=" * 70)
    print("Detailed report saved to: analysis_report.json")
    print("=" * 70)

if __name__ == '__main__':
    main()
