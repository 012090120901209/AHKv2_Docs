#!/usr/bin/env python3
"""
Enhance the inventory with statistics and categorization.
"""

import re
from pathlib import Path
from collections import defaultdict

def categorize_file(filename):
    """Categorize files based on their name patterns."""
    filename_lower = filename.lower()

    # Categories
    if filename.startswith('_') or filename.startswith('#'):
        return 'Directives & Special'
    elif 'win' in filename_lower and filename not in ['Winamp.md']:
        return 'Window Management'
    elif 'control' in filename_lower:
        return 'Control Functions'
    elif 'gui' in filename_lower:
        return 'GUI Functions'
    elif 'file' in filename_lower or 'dir' in filename_lower:
        return 'File & Directory'
    elif 'drive' in filename_lower:
        return 'Drive Functions'
    elif 'reg' in filename_lower and 'regex' not in filename_lower:
        return 'Registry Functions'
    elif 'process' in filename_lower:
        return 'Process Management'
    elif 'sound' in filename_lower:
        return 'Sound Functions'
    elif 'mouse' in filename_lower or 'click' in filename_lower:
        return 'Mouse Functions'
    elif 'key' in filename_lower or 'send' in filename_lower or 'hotkey' in filename_lower or 'hotstring' in filename_lower:
        return 'Keyboard & Hotkeys'
    elif 'loop' in filename_lower or 'for' in filename_lower or 'while' in filename_lower:
        return 'Flow Control & Loops'
    elif 'str' in filename_lower or 'substr' in filename_lower or 'trim' in filename_lower:
        return 'String Functions'
    elif 'com' in filename_lower and filename.startswith('Com'):
        return 'COM Functions'
    elif 'error' in filename_lower or 'try' in filename_lower or 'catch' in filename_lower or 'throw' in filename_lower:
        return 'Error Handling'
    elif any(x in filename_lower for x in ['math', 'random', 'round', 'sqrt', 'abs', 'ceil', 'floor']):
        return 'Math Functions'
    elif filename in ['Functions.md', 'Objects.md', 'Variables.md', 'Language.md', 'Concepts.md', 'Program.md']:
        return 'Core Concepts'
    elif filename in ['Tutorial.md', 'FAQ.md', 'Install.md', 'Acknowledgements.md']:
        return 'Documentation & Help'
    elif filename in ['Array.md', 'Map.md', 'Object.md', 'Buffer.md', 'Func.md', 'Functor.md']:
        return 'Built-in Types'
    else:
        return 'Other Functions'

def main():
    # Read existing inventory
    inventory_file = Path('DOCUMENTATION_INVENTORY.md')

    if not inventory_file.exists():
        print("Error: DOCUMENTATION_INVENTORY.md not found")
        return

    with open(inventory_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract file entries
    file_pattern = re.compile(r'^## (.+\.md)\s*\n\n\*\*Total Headers:\*\* (\d+)', re.MULTILINE)
    matches = file_pattern.findall(content)

    # Categorize files
    categories = defaultdict(list)
    total_headers = 0

    for filename, header_count in matches:
        category = categorize_file(filename)
        categories[category].append((filename, int(header_count)))
        total_headers += int(header_count)

    # Create enhanced summary
    summary = []
    summary.append("# AutoHotkey v2 Documentation Complete Inventory\n\n")
    summary.append("This document provides a comprehensive map of **everything** documented in AutoHotkey v2.\n")
    summary.append("Every header, section, and subsection from all 411 markdown files is catalogued here.\n\n")

    summary.append("## 📊 Statistics\n\n")
    summary.append(f"- **Total Documentation Files:** {len(matches)}\n")
    summary.append(f"- **Total Headers/Topics:** {total_headers:,}\n")
    summary.append(f"- **Categories:** {len(categories)}\n\n")

    summary.append("## 📁 Content by Category\n\n")
    for category in sorted(categories.keys()):
        files = categories[category]
        header_sum = sum(count for _, count in files)
        summary.append(f"### {category}\n")
        summary.append(f"**Files:** {len(files)} | **Headers:** {header_sum}\n\n")
        for filename, count in sorted(files):
            summary.append(f"- [{filename}](#{filename.replace('.md', '').lower().replace('_', '-')}) ({count} headers)\n")
        summary.append("\n")

    # Append original content after the header section
    summary.append("\n---\n\n")

    # Find where the detailed inventory starts
    detail_start = content.find("## Table of Contents")
    if detail_start > 0:
        summary.append(content[detail_start:])
    else:
        summary.append(content)

    # Write enhanced version
    with open(inventory_file, 'w', encoding='utf-8') as f:
        f.write(''.join(summary))

    print(f"Enhanced inventory created with {len(categories)} categories")
    print(f"Total: {len(matches)} files, {total_headers:,} headers")

if __name__ == '__main__':
    main()
