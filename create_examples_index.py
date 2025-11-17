#!/usr/bin/env python3
"""
Create comprehensive index of all examples.
"""

import re
from pathlib import Path
from collections import defaultdict

# Find all example files
examples_dir = Path('examples')
all_examples = sorted(examples_dir.rglob('*.ahk'))

# Organize by category
by_category = defaultdict(list)

for example_file in all_examples:
    category = example_file.parent.name
    name = example_file.stem.replace('_Example', '')
    by_category[category].append((name, example_file))

# Create index
output = []
output.append("# AutoHotkey v2 Complete Examples Index\n\n")
output.append(f"**Total Examples:** {len(all_examples)}\n")
output.append(f"**Categories:** {len(by_category)}\n\n")

output.append("## 📚 Quick Navigation\n\n")

# Create category links
for category in sorted(by_category.keys()):
    cat_title = category.replace('-', ' ').title()
    count = len(by_category[category])
    output.append(f"- [{cat_title}](#{category}) ({count} examples)\n")

output.append("\n---\n\n")

# Detailed listing by category
for category in sorted(by_category.keys()):
    cat_title = category.replace('-', ' ').title()
    examples = sorted(by_category[category])

    output.append(f"## {cat_title}\n\n")
    output.append(f"**Total Examples:** {len(examples)}\n\n")

    for name, filepath in examples:
        rel_path = filepath.relative_to(Path('examples'))
        output.append(f"### {name}\n")
        output.append(f"**File:** `{rel_path}`\n\n")

        # Try to extract description from file
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read(500)  # Read first 500 chars
                # Look for description in comments
                desc_match = re.search(r'Description:\s*(.+)', content)
                if desc_match:
                    output.append(f"**Description:** {desc_match.group(1)}\n\n")
                else:
                    output.append(f"**Description:** Demonstrates usage of {name}\n\n")
        except:
            output.append(f"**Description:** Demonstrates usage of {name}\n\n")

    output.append("\n")

# Write index
index_file = Path('examples/EXAMPLES_INDEX.md')
with open(index_file, 'w', encoding='utf-8') as f:
    f.writelines(output)

print(f"Created {index_file}")
print(f"Total examples indexed: {len(all_examples)}")
print(f"Categories: {len(by_category)}")
