#!/usr/bin/env python3
"""
Static Site Generator for AutoHotkey v2 Documentation
Converts markdown files to HTML using Docusaurus-style templates
"""

import os
import re
import json
import shutil
from pathlib import Path
from typing import Dict, List, Tuple
import markdown
from jinja2 import Environment, FileSystemLoader

# Configuration
SOURCE_DIR = Path('..')
TEMPLATE_DIR = Path('templates')
OUTPUT_DIR = Path('../docs')  # GitHub Pages uses /docs folder
STATIC_DIRS = ['css', 'js']

class SiteBuilder:
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))
        self.documents = []
        self.search_index = []

        # Markdown extensions
        self.md = markdown.Markdown(extensions=[
            'extra',
            'codehilite',
            'toc',
            'tables',
            'fenced_code',
            'attr_list',
            'def_list',
            'footnotes'
        ])

    def build(self):
        """Main build process."""
        print("🔨 Building AutoHotkey Documentation Site")
        print("=" * 60)

        # Clean output directory
        if OUTPUT_DIR.exists():
            print("🧹 Cleaning output directory...")
            shutil.rmtree(OUTPUT_DIR)

        OUTPUT_DIR.mkdir(exist_ok=True)

        # Copy static assets
        self.copy_static_assets()

        # Find all markdown files
        md_files = self.find_markdown_files()
        print(f"📄 Found {len(md_files)} markdown files\n")

        # Process files
        for md_file in md_files:
            self.process_file(md_file)

        # Generate index page
        self.generate_index()

        # Generate search index
        self.generate_search_index()

        # Generate sitemap
        self.generate_sitemap()

        print("\n" + "=" * 60)
        print("✅ Build complete!")
        print(f"📁 Output: {OUTPUT_DIR.absolute()}")
        print(f"📊 Generated {len(self.documents)} pages")

    def copy_static_assets(self):
        """Copy CSS, JS, and other static files."""
        print("📦 Copying static assets...")

        for static_dir in STATIC_DIRS:
            src = Path(static_dir)
            dst = OUTPUT_DIR / static_dir

            if src.exists():
                shutil.copytree(src, dst, dirs_exist_ok=True)
                print(f"   ✓ Copied {static_dir}/")

    def find_markdown_files(self) -> List[Path]:
        """Find all markdown files in source directory."""
        md_files = []

        for pattern in ['*.md']:
            md_files.extend(SOURCE_DIR.glob(pattern))

        # Exclude some files
        exclude = {'README.md', 'LICENSE.md', 'CHANGELOG.md'}
        md_files = [f for f in md_files if f.name not in exclude]

        return sorted(md_files)

    def process_file(self, md_file: Path):
        """Convert markdown file to HTML."""
        rel_path = md_file.relative_to(SOURCE_DIR)

        # Determine output path
        output_path = self.get_output_path(md_file)

        print(f"   Processing: {rel_path}")

        try:
            # Read markdown
            content = md_file.read_text(encoding='utf-8')

            # Extract metadata
            metadata = self.extract_metadata(content, md_file)

            # Convert to HTML
            html_content = self.md.convert(content)

            # Generate TOC
            toc_html = self.md.toc if hasattr(self.md, 'toc') else ''

            # Generate breadcrumb
            breadcrumb_html = self.generate_breadcrumb(md_file)

            # Render template
            template = self.env.get_template('base.html')
            html = template.render(
                title=metadata['title'],
                description=metadata.get('description', ''),
                content=html_content,
                toc=toc_html,
                breadcrumb=breadcrumb_html,
                source_file=str(rel_path),
                prev_page=None,  # TODO: implement
                next_page=None   # TODO: implement
            )

            # Write output
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(html, encoding='utf-8')

            # Add to documents list
            self.documents.append({
                'path': str(rel_path),
                'output': str(output_path.relative_to(OUTPUT_DIR)),
                'title': metadata['title'],
                'url': f"/{output_path.relative_to(OUTPUT_DIR)}"
            })

            # Add to search index
            self.search_index.append({
                'title': metadata['title'],
                'url': f"/{output_path.relative_to(OUTPUT_DIR)}",
                'path': str(rel_path),
                'content': self.strip_html(html_content)[:500]  # First 500 chars
            })

            # Reset markdown instance for next file
            self.md.reset()

        except Exception as e:
            print(f"   ✗ Error: {e}")

    def extract_metadata(self, content: str, filepath: Path) -> Dict:
        """Extract metadata from markdown content."""
        # Extract title from first h1
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else filepath.stem

        # Clean title
        title = re.sub(r'\{[^}]+\}', '', title).strip()

        # Extract description (first paragraph)
        desc_match = re.search(r'^#.+?\n\n(.+?)\n', content, re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ''

        return {
            'title': title,
            'description': description[:200]
        }

    def get_output_path(self, md_file: Path) -> Path:
        """Determine output HTML path for markdown file."""
        rel_path = md_file.relative_to(SOURCE_DIR)

        # Convert to .html
        html_name = rel_path.stem + '.html'

        # Organize by category if in subdirectory
        if rel_path.parent != Path('.'):
            return OUTPUT_DIR / rel_path.parent / html_name
        else:
            return OUTPUT_DIR / html_name

    def generate_breadcrumb(self, md_file: Path) -> str:
        """Generate breadcrumb HTML."""
        rel_path = md_file.relative_to(SOURCE_DIR)
        parts = list(rel_path.parts[:-1])  # Exclude filename

        breadcrumb = '<a href="/">Home</a>'

        current_path = ''
        for part in parts:
            current_path += '/' + part
            breadcrumb += f' <i class="fas fa-chevron-right"></i> <a href="{current_path}/">{part.title()}</a>'

        breadcrumb += f' <i class="fas fa-chevron-right"></i> <span>{md_file.stem}</span>'

        return breadcrumb

    def generate_index(self):
        """Generate index.html homepage."""
        print("\n🏠 Generating index page...")

        template = self.env.get_template('base.html')

        # Create homepage content
        content = """
        <div class="home-hero">
            <h1>AutoHotkey v2 Documentation</h1>
            <p class="lead">Complete reference documentation for AutoHotkey v2</p>

            <div class="home-buttons">
                <a href="/guides/Tutorial.html" class="btn btn-primary">
                    <i class="fas fa-book"></i> Get Started
                </a>
                <a href="/reference/Language.html" class="btn btn-secondary">
                    <i class="fas fa-code"></i> Language Reference
                </a>
            </div>
        </div>

        <div class="home-features">
            <div class="feature-card">
                <div class="feature-icon"><i class="fas fa-code"></i></div>
                <h3>Functions</h3>
                <p>200+ built-in functions for string manipulation, file operations, window management, and more.</p>
                <a href="/functions/">Browse Functions →</a>
            </div>

            <div class="feature-card">
                <div class="feature-icon"><i class="fas fa-cube"></i></div>
                <h3>Objects</h3>
                <p>Powerful object system with classes like Array, Map, Gui, and more.</p>
                <a href="/objects/Array.html">Explore Objects →</a>
            </div>

            <div class="feature-card">
                <div class="feature-icon"><i class="fas fa-book"></i></div>
                <h3>Guides</h3>
                <p>Learn AutoHotkey with tutorials, examples, and conceptual guides.</p>
                <a href="/guides/Tutorial.html">Read Guides →</a>
            </div>

            <div class="feature-card">
                <div class="feature-icon"><i class="fas fa-keyboard"></i></div>
                <h3>Hotkeys</h3>
                <p>Create powerful keyboard shortcuts and automate repetitive tasks.</p>
                <a href="/reference/Hotkeys.html">Learn Hotkeys →</a>
            </div>
        </div>

        <style>
        .home-hero {
            text-align: center;
            padding: 4rem 0;
            max-width: 800px;
            margin: 0 auto;
        }

        .home-hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }

        .lead {
            font-size: 1.25rem;
            color: var(--text-secondary);
            margin-bottom: 2rem;
        }

        .home-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.75rem 1.5rem;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 500;
            transition: all var(--transition);
        }

        .btn-primary {
            background-color: var(--primary);
            color: white;
        }

        .btn-primary:hover {
            background-color: var(--primary-dark);
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }

        .btn-secondary {
            background-color: var(--surface);
            color: var(--text-primary);
            border: 1px solid var(--border);
        }

        .btn-secondary:hover {
            border-color: var(--primary);
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }

        .home-features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 4rem;
        }

        .feature-card {
            padding: 2rem;
            background-color: var(--surface);
            border: 1px solid var(--border);
            border-radius: 8px;
            transition: all var(--transition);
        }

        .feature-card:hover {
            border-color: var(--primary);
            box-shadow: var(--shadow-md);
            transform: translateY(-4px);
        }

        .feature-icon {
            width: 48px;
            height: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: var(--primary);
            color: white;
            border-radius: 8px;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .feature-card h3 {
            margin: 0 0 0.5rem 0;
        }

        .feature-card p {
            color: var(--text-secondary);
            margin: 0 0 1rem 0;
        }

        .feature-card a {
            color: var(--primary);
            text-decoration: none;
            font-weight: 500;
        }
        </style>
        """

        html = template.render(
            title='AutoHotkey v2 Documentation',
            description='Complete reference documentation for AutoHotkey v2',
            content=content,
            toc='',
            breadcrumb='',
            source_file='index.md'
        )

        (OUTPUT_DIR / 'index.html').write_text(html, encoding='utf-8')

    def generate_search_index(self):
        """Generate search index JSON."""
        print("🔍 Generating search index...")

        search_file = OUTPUT_DIR / 'search-index.json'
        search_file.write_text(
            json.dumps(self.search_index, indent=2),
            encoding='utf-8'
        )

        print(f"   ✓ Created search index with {len(self.search_index)} entries")

    def generate_sitemap(self):
        """Generate sitemap.xml."""
        print("🗺️  Generating sitemap...")

        sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
        sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

        base_url = 'https://012090120901209.github.io/AHKv2_Docs'

        for doc in self.documents:
            sitemap += f'  <url>\n'
            sitemap += f'    <loc>{base_url}{doc["url"]}</loc>\n'
            sitemap += f'    <changefreq>weekly</changefreq>\n'
            sitemap += f'  </url>\n'

        sitemap += '</urlset>'

        (OUTPUT_DIR / 'sitemap.xml').write_text(sitemap, encoding='utf-8')

    @staticmethod
    def strip_html(html: str) -> str:
        """Strip HTML tags from string."""
        return re.sub(r'<[^>]+>', '', html)


if __name__ == '__main__':
    builder = SiteBuilder()
    builder.build()
