#!/usr/bin/env python3
"""
Extract all headers from all markdown files in the AHKv2 documentation.
Creates a comprehensive inventory of all topics covered.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def extract_headers(file_path):
    """Extract all markdown headers from a file."""
    headers = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                # Match markdown headers (# Header)
                match = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
                if match:
                    level = len(match.group(1))
                    title = match.group(2).strip()
                    headers.append({
                        'level': level,
                        'title': title,
                        'line': line_num
                    })
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

    return headers

def main():
    # Get all markdown files
    md_files = sorted(Path('.').glob('*.md'))

    # Dictionary to store file -> headers mapping
    inventory = {}

    # Process each file
    for md_file in md_files:
        file_name = md_file.name
        headers = extract_headers(md_file)

        if headers:
            inventory[file_name] = headers

    # Generate the inventory document
    output = []
    output.append("# AutoHotkey v2 Documentation Complete Inventory\n")
    output.append(f"**Total Files:** {len(inventory)}\n")
    output.append(f"**Generated:** {Path.cwd()}\n")
    output.append("\n---\n\n")
    output.append("## Table of Contents\n\n")

    # Create TOC
    for file_name in sorted(inventory.keys()):
        # Create anchor link (lowercase, replace spaces/special chars with hyphens)
        anchor = file_name.replace('.md', '').lower().replace('_', '-')
        output.append(f"- [{file_name}](#{anchor})\n")

    output.append("\n---\n\n")

    # Add detailed inventory
    for file_name in sorted(inventory.keys()):
        headers = inventory[file_name]
        output.append(f"## {file_name}\n\n")

        # Count headers by level
        level_counts = defaultdict(int)
        for h in headers:
            level_counts[h['level']] += 1

        output.append(f"**Total Headers:** {len(headers)}\n\n")

        # List all headers
        for header in headers:
            indent = "  " * (header['level'] - 1)
            output.append(f"{indent}- {'#' * header['level']} {header['title']}\n")

        output.append("\n")

    # Write to file
    output_file = Path('DOCUMENTATION_INVENTORY.md')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output)

    print(f"Inventory created: {output_file}")
    print(f"Total files processed: {len(inventory)}")
    total_headers = sum(len(headers) for headers in inventory.values())
    print(f"Total headers found: {total_headers}")

if __name__ == '__main__':
    main()
