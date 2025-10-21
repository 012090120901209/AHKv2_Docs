#!/usr/bin/env python3
"""
Reorganize markdown files into hierarchical structure.
Updates internal links to reflect new structure.
Run after 1_analyze_files.py
"""

import os
import re
import json
import shutil
from pathlib import Path
from collections import defaultdict

# Import categorization from analysis script
import sys
sys.path.insert(0, os.path.dirname(__file__))

def load_analysis():
    """Load the analysis report."""
    with open('analysis_report.json', 'r') as f:
        return json.load(f)

def create_directory_structure(categorization, output_dir='docs_reorganized'):
    """Create the new directory structure."""
    base = Path(output_dir)
    base.mkdir(exist_ok=True)

    # Create category directories
    for category, subcats in categorization.items():
        if category == 'root':
            continue

        cat_dir = base / category
        cat_dir.mkdir(exist_ok=True)

        # Create subcategory directories
        for subcat in subcats.keys():
            if subcat != '_root':
                (cat_dir / subcat).mkdir(exist_ok=True)

    return base

def update_links_in_content(content, old_file, new_file, file_mapping):
    """Update internal links to reflect new file locations."""
    # Find all markdown links
    link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'

    def replace_link(match):
        text = match.group(1)
        target = match.group(2)

        # Skip external links
        if target.startswith('http'):
            return match.group(0)

        # Skip anchors only
        if target.startswith('#'):
            return match.group(0)

        # Extract filename and anchor
        if '#' in target:
            target_file, anchor = target.split('#', 1)
            anchor = '#' + anchor
        else:
            target_file = target
            anchor = ''

        # Convert .htm to .md if needed
        if target_file.endswith('.htm'):
            target_file = target_file.replace('.htm', '.md')

        # Handle relative paths
        target_file = os.path.basename(target_file)

        # Find new location of target file
        if target_file in file_mapping:
            new_target_path = file_mapping[target_file]

            # Calculate relative path from new_file to new_target
            new_file_dir = os.path.dirname(new_file)
            rel_path = os.path.relpath(new_target_path, new_file_dir)

            return f'[{text}]({rel_path}{anchor})'

        # If not found, keep original but fix .htm
        return f'[{text}]({target_file}{anchor})'

    return re.sub(link_pattern, replace_link, content)

def reorganize_files(dry_run=True):
    """Reorganize files based on analysis."""
    analysis = load_analysis()
    categorization = analysis['categorization']
    file_metadata = analysis['file_metadata']

    output_dir = 'docs_reorganized'

    if not dry_run:
        # Create directory structure
        base = create_directory_structure(categorization, output_dir)
    else:
        base = Path(output_dir)

    # Build file mapping (old -> new)
    file_mapping = {}

    for filename, meta in file_metadata.items():
        category = meta['category']
        subcategory = meta['subcategory']

        if category == 'root':
            new_path = filename
        elif subcategory and subcategory != '_root':
            new_path = f"{category}/{subcategory}/{filename}"
        else:
            new_path = f"{category}/{filename}"

        file_mapping[filename] = new_path

    # Print reorganization plan
    print("=" * 70)
    print("REORGANIZATION PLAN")
    print("=" * 70)

    moves_by_category = defaultdict(list)
    for old, new in sorted(file_mapping.items()):
        if old != new and not new.startswith('index'):
            category = new.split('/')[0] if '/' in new else 'root'
            moves_by_category[category].append((old, new))

    for category in sorted(moves_by_category.keys()):
        moves = moves_by_category[category]
        print(f"\n{category.upper()}: {len(moves)} files")
        for old, new in moves[:5]:  # Show first 5
            print(f"  {old} -> {new}")
        if len(moves) > 5:
            print(f"  ... and {len(moves) - 5} more")

    if dry_run:
        print("\n" + "=" * 70)
        print("DRY RUN - No files were moved")
        print("Run with --execute to perform reorganization")
        print("=" * 70)
        return

    # Actually move and update files
    print("\n" + "=" * 70)
    print("EXECUTING REORGANIZATION")
    print("=" * 70)

    moved_count = 0
    updated_count = 0

    for filename, meta in file_metadata.items():
        old_path = Path(filename)
        new_path = base / file_mapping[filename]

        if not old_path.exists():
            continue

        # Read content
        with open(old_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update links
        updated_content = update_links_in_content(
            content, filename, file_mapping[filename], file_mapping
        )

        # Write to new location
        new_path.parent.mkdir(parents=True, exist_ok=True)
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        moved_count += 1
        if updated_content != content:
            updated_count += 1

        if moved_count % 50 == 0:
            print(f"  Processed {moved_count} files...")

    # Copy special files
    for special in ['LICENSE', 'README.md', '.gitignore']:
        if Path(special).exists():
            shutil.copy(special, base / special)

    print(f"\nMoved {moved_count} files")
    print(f"Updated links in {updated_count} files")
    print(f"\nReorganized documentation: {output_dir}/")

    # Create category README files
    create_category_readmes(base, categorization)

def create_category_readmes(base, categorization):
    """Create README.md files for each category."""
    category_descriptions = {
        'functions': 'Built-in AutoHotkey v2 functions',
        'objects': 'Object and class reference documentation',
        'directives': 'Compiler directives and preprocessor commands',
        'guides': 'Tutorials and conceptual guides',
        'reference': 'Reference materials and lookup tables',
        'changelog': 'Version history and changes'
    }

    for category, subcats in categorization.items():
        if category == 'root':
            continue

        cat_dir = base / category
        readme_path = cat_dir / 'README.md'

        files = []
        for subcat, file_list in subcats.items():
            for f in file_list:
                if subcat == '_root':
                    files.append((None, f))
                else:
                    files.append((subcat, f))

        # Create README content
        content = f"# {category.title()}\n\n"
        content += f"{category_descriptions.get(category, '')}\n\n"

        # Group by subcategory
        by_subcat = defaultdict(list)
        for subcat, f in files:
            by_subcat[subcat].append(f)

        for subcat in sorted(by_subcat.keys(), key=lambda x: (x is None, x)):
            if subcat:
                content += f"\n## {subcat.title()}\n\n"

            for f in sorted(by_subcat[subcat]):
                title = f.replace('.md', '').replace('_', ' ')
                link = f if not subcat else f"{subcat}/{f}"
                content += f"- [{title}]({link})\n"

        with open(readme_path, 'w') as f:
            f.write(content)

        print(f"Created {readme_path}")

if __name__ == '__main__':
    import sys
    dry_run = '--execute' not in sys.argv

    if dry_run:
        print("Running in DRY RUN mode. Use --execute to actually reorganize files.\n")

    reorganize_files(dry_run=dry_run)
