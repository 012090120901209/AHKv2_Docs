# Quick Start Guide - AutoHotkey Documentation Database

## 🎬 See It In Action

Run the live demo (no database required):

```bash
python3 demo_standalone.py
```

This demo:
- ✅ Parses actual markdown files
- ✅ Extracts functions, objects, methods
- ✅ Shows what the database contains
- ✅ Simulates SQL queries
- ✅ Real data, real results!

---

## 🚀 Set Up Full Database

### Option 1: Docker (Recommended - 5 minutes)

```bash
cd database
./init_db.sh
```

**Done!** Database is ready at `localhost:5432`

### Option 2: Local PostgreSQL (10 minutes)

```bash
# 1. Install PostgreSQL
sudo apt-get install postgresql  # Ubuntu/Debian
brew install postgresql          # macOS

# 2. Create database
createdb ahk_docs

# 3. Load schema
psql -d ahk_docs < database/schema.sql

# 4. Install Python dependencies
pip install psycopg2-binary

# 5. Load data
python3 database/load_data.py .
```

---

## 💻 Query the Database

### Interactive Python Shell

```bash
python3 database/query_db.py
```

```
> search array methods
> function StrSplit
> object Array
> list functions
> examples Array Object
> stats
> quit
```

### Command Line

```bash
# Search
python3 database/query_db.py search "window activation"

# Get function
python3 database/query_db.py function StrSplit

# Get object
python3 database/query_db.py object Array

# Statistics
python3 database/query_db.py stats
```

### SQL Queries

```bash
psql -h localhost -p 5432 -U postgres -d ahk_docs
```

```sql
-- Search
SELECT * FROM search_documents('array methods');

-- Function details
SELECT * FROM v_functions_complete WHERE function_name = 'StrSplit';

-- Object details
SELECT * FROM v_objects_complete WHERE object_name = 'Array';

-- Most referenced docs
SELECT title, COUNT(*) as refs
FROM documents d
JOIN links l ON d.id = l.target_document_id
GROUP BY d.id, title
ORDER BY refs DESC
LIMIT 10;
```

### Python API

```python
from database.query_db import AHKDocsDB

db = AHKDocsDB()

# Search
results = db.search('window activation', limit=10)
for r in results:
    print(f"{r['title']}: {r['snippet']}")

# Get function
func = db.get_function('StrSplit')
print(f"Syntax: {func['syntax']}")
print(f"Returns: {func['return_type']}")
for param in func['parameters']:
    print(f"  - {param['name']}: {param['type']}")

# Get object
obj = db.get_object('Array')
print(f"Methods: {obj['methods']}")
print(f"Properties: {obj['properties']}")

# Code examples
examples = db.get_code_examples('Array Object')
for ex in examples:
    print(ex['code'])

# Statistics
stats = db.get_statistics()
print(f"Documents: {stats['total_documents']}")
print(f"Functions: {stats['total_functions']}")
print(f"Objects: {stats['total_objects']}")

db.close()
```

---

## 📊 What's In The Database

After loading all 413 files:

| Table | Contents | Count |
|-------|----------|-------|
| **documents** | All markdown files | 413 |
| **sections** | Document sections | ~2,000 |
| **functions** | Function definitions | ~200 |
| **function_parameters** | Parameters | ~800 |
| **objects** | Objects/classes | ~30 |
| **object_methods** | Methods | ~150 |
| **object_properties** | Properties | ~100 |
| **code_examples** | Code blocks | ~800 |
| **links** | Internal/external links | ~3,000 |

---

## 🔍 Common Queries

### Find Functions

```sql
-- All functions
SELECT function_name, return_type FROM v_functions_complete;

-- Functions with specific parameter
SELECT f.function_name
FROM functions f
JOIN function_parameters fp ON f.id = fp.function_id
WHERE fp.param_name ILIKE '%string%';

-- Functions returning arrays
SELECT function_name FROM functions WHERE return_type = 'Array';
```

### Find Objects

```sql
-- All objects
SELECT object_name, extends FROM v_objects_complete;

-- Objects with specific method
SELECT o.object_name, om.method_name
FROM objects o
JOIN object_methods om ON o.id = om.object_id
WHERE om.method_name ILIKE '%push%';
```

### Search Documentation

```sql
-- Full-text search
SELECT * FROM search_documents('gui button click', NULL, NULL, 10);

-- Search only functions
SELECT * FROM search_documents('string split', 'function', NULL, 5);

-- Search in category
SELECT * FROM search_documents('window', NULL, 'functions', 10);
```

### Code Examples

```sql
-- Find examples with specific code
SELECT d.title, ce.code
FROM code_examples ce
JOIN documents d ON ce.document_id = d.id
WHERE ce.code ILIKE '%MsgBox%'
LIMIT 10;

-- Documents with most examples
SELECT d.title, COUNT(*) as example_count
FROM code_examples ce
JOIN documents d ON ce.document_id = d.id
GROUP BY d.id, d.title
ORDER BY example_count DESC
LIMIT 10;
```

### Link Analysis

```sql
-- Most referenced documents
SELECT d.title, COUNT(*) as references
FROM documents d
JOIN links l ON d.id = l.target_document_id
WHERE l.is_external = false
GROUP BY d.id, d.title
ORDER BY references DESC
LIMIT 20;

-- Broken links
SELECT d.title, l.link_url
FROM links l
JOIN documents d ON l.source_document_id = d.id
WHERE l.is_external = false AND l.target_document_id IS NULL;
```

---

## 🛠️ Integration Examples

### Flask Web API

```python
from flask import Flask, jsonify, request
from database.query_db import AHKDocsDB

app = Flask(__name__)
db = AHKDocsDB()

@app.route('/api/search')
def search():
    query = request.args.get('q', '')
    results = db.search(query, limit=20)
    return jsonify(results)

@app.route('/api/function/<name>')
def get_function(name):
    func = db.get_function(name)
    return jsonify(func) if func else ('Not found', 404)

@app.route('/api/object/<name>')
def get_object(name):
    obj = db.get_object(name)
    return jsonify(obj) if obj else ('Not found', 404)

if __name__ == '__main__':
    app.run(port=5000)
```

### RAG System

```python
from database.query_db import AHKDocsDB
import openai

def get_ahk_answer(question: str) -> str:
    """Get answer from documentation using RAG."""

    # Get relevant docs
    db = AHKDocsDB()
    results = db.search(question, limit=5)

    # Build context
    context = "\n\n".join([
        f"# {r['title']}\n{r['snippet']}"
        for r in results
    ])

    # Query LLM
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AutoHotkey expert. Answer based on the provided documentation."},
            {"role": "user", "content": f"Documentation:\n{context}\n\nQuestion: {question}"}
        ]
    )

    db.close()
    return response.choices[0].message.content

# Use it
answer = get_ahk_answer("How do I create an array and add items to it?")
print(answer)
```

### Static Site Generator

```python
from database.query_db import AHKDocsDB
from pathlib import Path

db = AHKDocsDB()

# Generate pages for all functions
functions = db.list_functions(limit=1000)
for func in functions:
    # Get full details
    details = db.get_function(func['function_name'])

    # Generate HTML
    html = generate_function_page(details)

    # Save
    output_path = Path(f"site/functions/{func['function_name']}.html")
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(html)

print(f"Generated {len(functions)} function pages")
```

---

## 🐳 Docker Commands

```bash
# Start database
docker-compose up -d

# Stop database
docker-compose down

# View logs
docker-compose logs -f postgres

# Access PostgreSQL shell
docker-compose exec postgres psql -U postgres -d ahk_docs

# Access pgAdmin (web UI)
# Open http://localhost:5050
# Email: admin@ahkdocs.local
# Password: admin

# Backup database
docker-compose exec postgres pg_dump -U postgres ahk_docs > backup.sql

# Restore database
docker-compose exec -T postgres psql -U postgres ahk_docs < backup.sql

# Reset (delete all data)
docker-compose down -v
./init_db.sh
```

---

## 📁 File Structure

```
/database/
├── schema.sql              # Database schema (17KB)
├── load_data.py            # Data loader (21KB)
├── query_db.py             # Python API (15KB)
├── query_examples.sql      # 50+ example queries (12KB)
├── init_db.sh              # Setup script
├── docker-compose.yml      # Docker config
├── requirements.txt        # Python deps
└── README.md               # Full documentation (13KB)

/scripts/
└── (vectorization scripts for embeddings)

demo_standalone.py          # Live demo (no database required)
DATABASE_SUMMARY.md         # Overview
QUICK_START.md              # This file
```

---

## 🎯 What to Do Next

### 1. Try the Demo
```bash
python3 demo_standalone.py
```

### 2. Set Up Database
```bash
cd database && ./init_db.sh
```

### 3. Try Some Queries
```bash
python3 database/query_db.py
```

### 4. Build Your Application
- Use Python API
- Create web interface
- Build RAG system
- Generate static site
- Power IDE autocomplete

---

## 💡 Tips

1. **Performance**: Database queries are fast (1-50ms)
2. **Search**: Use `search_documents()` function for best results
3. **Examples**: See `database/query_examples.sql` for 50+ queries
4. **API**: Use `query_db.py` as starting point for your app
5. **Export**: Can export to JSON, CSV, or other formats

---

## 🆘 Troubleshooting

### "Connection refused"
```bash
# Check PostgreSQL is running
docker-compose ps
# Or
sudo systemctl status postgresql
```

### "Module not found"
```bash
# Install dependencies
pip install -r database/requirements.txt
```

### "Permission denied"
```bash
# Make scripts executable
chmod +x database/*.sh database/*.py
```

### Database not loading
```bash
# Check logs
docker-compose logs postgres

# Reset and retry
docker-compose down -v
./database/init_db.sh
```

---

## 📚 Documentation

- **DATABASE_SUMMARY.md** - Quick overview
- **database/README.md** - Complete guide (13KB)
- **database/query_examples.sql** - 50+ SQL examples
- **database/schema.sql** - Full schema with comments
- **VECTORIZATION_ANSWER.md** - Vector database option
- **scripts/README.md** - Vectorization scripts

---

## ✨ Summary

You have **two powerful options**:

### PostgreSQL Database (This Guide)
✅ Structured SQL queries
✅ Full-text search
✅ Relational data
✅ Perfect for: APIs, websites, analytics

### Vector Database (See scripts/)
✅ Semantic search
✅ AI embeddings
✅ Perfect for: RAG, LLM apps

### Or Use Both!
The PostgreSQL schema supports vector embeddings.
Combine SQL queries with semantic search!

---

**Start now**: `python3 demo_standalone.py` 🚀

All the code is ready to use. Just run it!
