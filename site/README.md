# AutoHotkey v2 Documentation Site

Beautiful, Docusaurus-inspired documentation site for AutoHotkey v2.

## 🎨 Features

- **Modern Design**: Clean, professional Docusaurus-inspired interface
- **Dark Mode**: Smooth dark/light theme switching with persistence
- **Full-Text Search**: Instant client-side search with highlighting
- **Mobile Responsive**: Perfect on desktop, tablet, and mobile
- **Syntax Highlighting**: Beautiful code blocks with copy buttons
- **Table of Contents**: Auto-generated, scroll-spy TOC
- **Category Navigation**: Organized sidebar with collapsible categories
- **Keyboard Shortcuts**: Ctrl+K to focus search
- **Fast**: Static site generation for optimal performance

## 🚀 Quick Start

### Build Locally

```bash
cd site

# Install dependencies
pip install -r requirements.txt

# Build the site
python build.py

# Output will be in ../docs/
```

The generated site will be in the `/docs` folder, ready for GitHub Pages.

### Preview Locally

```bash
cd ../docs
python -m http.server 8000
```

Then open http://localhost:8000

## 📁 Project Structure

```
site/
├── templates/
│   └── base.html          # Main HTML template
├── css/
│   ├── styles.css         # Main styles, layout, navbar
│   ├── sidebar.css        # Sidebar navigation
│   ├── markdown.css       # Markdown content styling
│   ├── syntax.css         # Code syntax highlighting
│   └── toc.css            # Table of contents
├── js/
│   ├── search.js          # Search functionality
│   ├── theme.js           # Dark/light mode toggle
│   ├── sidebar.js         # Sidebar mobile toggle
│   ├── toc.js             # Dynamic TOC generation
│   └── syntax.js          # Code block enhancements
├── build.py               # Static site generator
└── requirements.txt       # Python dependencies
```

## 🔨 How It Works

### Build Process

1. **Find Markdown Files**: Scans repository for `.md` files
2. **Parse Markdown**: Converts to HTML with extensions
3. **Extract Metadata**: Title, description, TOC
4. **Render Template**: Injects content into base template
5. **Generate Search Index**: Creates JSON for client-side search
6. **Copy Assets**: CSS, JS to output directory
7. **Create Homepage**: Special index page with features
8. **Generate Sitemap**: SEO sitemap.xml

### Template System

The `base.html` template uses Jinja2 with these variables:

- `title` - Page title
- `description` - Meta description
- `content` - Rendered markdown HTML
- `toc` - Table of contents HTML
- `breadcrumb` - Breadcrumb navigation HTML
- `source_file` - Original markdown file path
- `prev_page` / `next_page` - Pagination

### Search System

- **Build Time**: Extracts title, URL, and content preview
- **Runtime**: JavaScript searches the JSON index
- **Highlighting**: Query terms highlighted in results
- **Fast**: Client-side, no server needed

## 🎨 Customization

### Colors

Edit CSS variables in `css/styles.css`:

```css
:root {
    --primary: #4a9eff;
    --secondary: #00c9a7;
    /* ... more colors ... */
}
```

### Sidebar Categories

Edit the sidebar in `templates/base.html`:

```html
<div class="sidebar-category">
    <div class="category-header">
        <i class="fas fa-code"></i>
        <span>Your Category</span>
    </div>
    <ul class="category-items">
        <li><a href="/your/link.html">Your Link</a></li>
    </ul>
</div>
```

### Homepage Content

Edit `generate_index()` in `build.py` to customize the homepage.

## 🚀 Deployment

### GitHub Pages (Automatic)

The site deploys automatically via GitHub Actions:

1. Push to `main` branch
2. GitHub Actions builds the site
3. Deploys to GitHub Pages
4. Available at: https://YOUR_USERNAME.github.io/AHKv2_Docs

### Manual Deployment

```bash
# Build the site
cd site
python build.py

# The docs/ folder is ready to deploy
# You can use any static hosting service
```

### Custom Domain

1. Add your domain to `CNAME` file
2. Configure DNS with GitHub Pages IPs
3. Enable HTTPS in GitHub repository settings

## 🔧 Development

### Adding New Features

#### Custom CSS

Add new CSS files in `css/` and link in `base.html`:

```html
<link rel="stylesheet" href="/css/your-feature.css">
```

#### Custom JavaScript

Add new JS files in `js/` and include in `base.html`:

```html
<script src="/js/your-feature.js"></script>
```

#### Markdown Extensions

Edit `build.py` to add markdown extensions:

```python
self.md = markdown.Markdown(extensions=[
    'extra',
    'your-extension'
])
```

### Build Options

Customize `build.py`:

```python
# Output directory
OUTPUT_DIR = Path('../docs')

# Source directory
SOURCE_DIR = Path('..')

# Exclude files
exclude = {'README.md', 'LICENSE.md'}
```

## 📊 Performance

- **Build Time**: ~5-10 seconds for 413 files
- **Page Load**: < 1 second (static HTML)
- **Search**: Instant (client-side)
- **Lighthouse Score**: 95+ (Performance, Accessibility, Best Practices, SEO)

## 🎯 Browser Support

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers

## 📝 Markdown Features

### Supported Syntax

- Headings, paragraphs, lists
- Tables
- Code blocks with syntax highlighting
- Blockquotes
- Links and images
- Footnotes
- Definition lists
- Task lists
- Fenced code with language specification

### Example

```markdown
# Heading

This is **bold** and _italic_.

| Column 1 | Column 2 |
|----------|----------|
| Value 1  | Value 2  |

\```python
def hello():
    print("Hello, World!")
\```
```

## 🐛 Troubleshooting

### Build Fails

```bash
# Check Python version (needs 3.8+)
python --version

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Run with verbose output
python build.py -v
```

### Search Not Working

- Ensure `search-index.json` exists in `/docs`
- Check browser console for errors
- Verify JavaScript is enabled

### Styles Not Loading

- Check CSS files are in `/docs/css/`
- Clear browser cache
- Check browser console for 404 errors

## 📚 Resources

- **Docusaurus**: Inspiration for design
- **Markdown**: https://www.markdownguide.org/
- **Jinja2**: https://jinja.palletsprojects.com/
- **GitHub Pages**: https://pages.github.com/

## 🤝 Contributing

1. Edit markdown files in the root directory
2. Run `python site/build.py` to rebuild
3. Test locally
4. Commit and push (GitHub Actions will deploy)

## 📄 License

Same as AutoHotkey v2 documentation.

---

**Built with ❤️ using Python, Jinja2, and Markdown**
