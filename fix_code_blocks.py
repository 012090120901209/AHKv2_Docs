#!/usr/bin/env python3
"""
Fix code blocks in markdown files to have proper syntax highlighting.
Adds language identifiers to code fences that don't have them.
"""

import re
from pathlib import Path

def fix_code_blocks(content):
    """Add language identifiers to code blocks without them."""
    lines = content.split('\n')
    fixed_lines = []
    in_code_block = False

    for i, line in enumerate(lines):
        # Check for code fence
        if line.strip() == '```':
            if not in_code_block:
                # Starting a code block - determine language
                # Look at next line to guess language
                next_line = lines[i+1] if i+1 < len(lines) else ''

                # Check if it looks like AHK code
                if any(keyword in next_line for keyword in ['MsgBox', '::', 'WinActivate', 'Send', 'Loop', 'if (', 'return']):
                    fixed_lines.append('```ahk')
                # Check if it looks like code at all
                elif next_line.strip() and not next_line.strip().startswith('#'):
                    fixed_lines.append('```ahk')
                else:
                    fixed_lines.append(line)
                in_code_block = True
            else:
                # Ending a code block
                fixed_lines.append(line)
                in_code_block = False
        # Check for labeled code blocks like "``` Syntax"
        elif line.strip().startswith('```') and line.strip() != '```':
            # Replace with proper language identifier
            if 'Syntax' in line or 'syntax' in line:
                fixed_lines.append('```ahk')
            else:
                fixed_lines.append('```ahk')
            in_code_block = True
        else:
            fixed_lines.append(line)

    return '\n'.join(fixed_lines)

def main():
    """Fix code blocks in all markdown files."""
    md_files = list(Path('.').glob('*.md'))

    fixed_count = 0
    for md_file in md_files:
        # Skip certain files
        if md_file.name in ['README.md', 'index.md']:
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if file has unfixed code blocks
            if '\n```\n' in content or '\n``` ' in content:
                fixed_content = fix_code_blocks(content)

                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)

                fixed_count += 1
                print(f'Fixed: {md_file.name}')

        except Exception as e:
            print(f'Error processing {md_file.name}: {e}')

    print(f'\nTotal files fixed: {fixed_count}')

if __name__ == '__main__':
    main()
