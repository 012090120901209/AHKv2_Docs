# AutoHotkey v2 Documentation Vectorization Scripts

This directory contains scripts to clean up, reorganize, and vectorize the AutoHotkey v2 documentation for use in RAG (Retrieval Augmented Generation) systems and semantic search.

## 🎯 Quick Answer: Flat vs Hierarchical for Vectorization

**Use HIERARCHICAL structure** for vectorization. Here's why:

| Benefit | Explanation |
|---------|-------------|
| **Better Metadata** | Directory structure provides free categorization |
| **Filtered Search** | Can search only functions/, objects/, etc. |
| **Context Preservation** | File path indicates document type |
| **Easier Maintenance** | Organized files are easier to update |
| **Improved Retrieval** | Category + semantic search = better results |

The hierarchical structure gives you automatic metadata that significantly improves retrieval quality.

## 📋 Scripts Overview

### 1. `1_analyze_files.py` - Analysis & Categorization

**Purpose**: Analyze all markdown files and categorize them.

**Usage**:
```bash
cd /home/user/AHKv2_Docs
python scripts/1_analyze_files.py
```

**Output**:
- Console report showing file categorization
- `analysis_report.json` with detailed metadata
- Statistics on content (tokens, sections, code examples)

**Example Output**:
```
CATEGORIZATION SUMMARY
======================================================================

FUNCTIONS: 215 files
  window: 45 files
  string: 32 files
  file: 28 files
  ...

OBJECTS: 30 files
  - Array.md
  - Map.md
  - Gui.md
  ...

Total estimated tokens: 850,000
Files with code examples: 380 (92.1%)
```

---

### 2. `2_reorganize_files.py` - File Reorganization

**Purpose**: Reorganize files into hierarchical structure and fix links.

**Usage**:
```bash
# Dry run (preview changes)
python scripts/2_reorganize_files.py

# Actually reorganize files
python scripts/2_reorganize_files.py --execute
```

**What it does**:
1. Creates organized directory structure (functions/, objects/, etc.)
2. Moves files to appropriate directories
3. Updates all internal links (.htm → .md, fixes paths)
4. Creates category README files
5. Preserves special files (index, search, etc.)

**Output Structure**:
```
docs_reorganized/
  functions/
    string/
      StrSplit.md
      InStr.md
      Format.md
    window/
      WinActivate.md
      ControlClick.md
    file/
      FileRead.md
      DirCreate.md
  objects/
    Array.md
    Map.md
    Gui.md
  guides/
    Tutorial.md
    FAQ.md
    Concepts.md
  reference/
    hotkeys/
      Hotkeys.md
      Hotstrings.md
    language/
      Language.md
      Variables.md
      Functions.md
```

---

### 3. `3_vectorize_docs.py` - Vectorization

**Purpose**: Create vector embeddings for semantic search.

**Requirements**:
```bash
pip install openai          # For OpenAI embeddings
pip install chromadb        # For ChromaDB (optional)
export OPENAI_API_KEY="..."  # Your API key
```

**Usage**:
```bash
# Basic: Create chunks without embeddings (JSON export)
python scripts/3_vectorize_docs.py

# With embeddings (requires OpenAI API key)
python scripts/3_vectorize_docs.py --embed

# Export to ChromaDB
python scripts/3_vectorize_docs.py --format chromadb --embed

# Use current flat structure (if not reorganized)
python scripts/3_vectorize_docs.py --input .
```

**Chunking Strategy**:
- Chunks by sections (preserves headings)
- Size: ~800 tokens per chunk
- Overlap: 150 tokens
- Preserves code examples
- Rich metadata per chunk

**Chunk Metadata**:
```json
{
  "file_path": "functions/string/StrSplit.md",
  "category": "functions",
  "subcategory": "string",
  "title": "StrSplit",
  "section": "Parameters",
  "doc_type": "function",
  "chunk_index": 2,
  "total_chunks": 5,
  "has_code": true,
  "code_examples": 3
}
```

**Output**:
- `vectorized_docs.json` - All chunks with embeddings (if --embed used)
- Or ChromaDB database in `./chroma_db/`

---

### 4. `4_query_docs.py` - Query Interface

**Purpose**: Search the vectorized documentation.

**Usage**:
```bash
# Interactive mode
python scripts/4_query_docs.py

# Single query
python scripts/4_query_docs.py --query "How do I split a string?"

# Filter by category
python scripts/4_query_docs.py --query "array methods" --category objects

# Use ChromaDB
python scripts/4_query_docs.py --source ahk_docs_vectordb
```

**Interactive Commands**:
```
> search how to create a gui
> filter functions
> search window activation
> category objects
> categories
> quit
```

---

## 🚀 Complete Workflow

### Option 1: Hierarchical Structure (Recommended)

```bash
# 1. Analyze files
python scripts/1_analyze_files.py

# 2. Review the analysis_report.json
cat analysis_report.json | less

# 3. Reorganize files (dry run first)
python scripts/2_reorganize_files.py

# 4. If satisfied, execute reorganization
python scripts/2_reorganize_files.py --execute

# 5. Vectorize with embeddings
export OPENAI_API_KEY="sk-..."
python scripts/3_vectorize_docs.py --input docs_reorganized --embed

# 6. Query the documentation
python scripts/4_query_docs.py
```

### Option 2: Keep Flat Structure

```bash
# 1. Analyze files
python scripts/1_analyze_files.py

# 2. Vectorize directly (flat structure)
export OPENAI_API_KEY="sk-..."
python scripts/3_vectorize_docs.py --input . --embed

# 3. Query
python scripts/4_query_docs.py
```

---

## 💾 Storage Comparison

### Flat Structure
```
✓ Simpler paths
✗ No automatic categorization
✗ Harder to filter by type
✗ Less context in chunks
```

### Hierarchical Structure
```
✓ Automatic category metadata
✓ Easy filtering (search only functions/)
✓ Better context preservation
✓ More maintainable
✓ Better for RAG retrieval
```

---

## 📊 Expected Results

### File Counts (Approximate)
- **Functions**: 215 files
  - window: 45 files
  - string: 32 files
  - file: 28 files
  - system: 25 files
  - misc: 85 files
- **Objects**: 30 files
- **Guides**: 20 files
- **Reference**: 40 files
- **Directives**: 20 files

### Vectorization Stats
- **Total chunks**: ~1,500 - 2,000
- **Avg chunk size**: 600-800 tokens
- **Total tokens**: ~850,000
- **JSON size** (with embeddings): ~200-300 MB
- **Embedding cost** (OpenAI): ~$0.10 for text-embedding-3-small

---

## 🔧 Customization

### Adjust Chunk Size

Edit `3_vectorize_docs.py`:
```python
chunker = DocumentChunker(
    chunk_size=1000,  # Increase for larger chunks
    overlap=200       # Increase overlap
)
```

### Change Categorization Rules

Edit `1_analyze_files.py` to modify the `CATEGORIES` dictionary.

### Use Different Embedding Model

Edit `3_vectorize_docs.py`:
```python
vectorizer = DocumentVectorizer(
    provider='openai',
    model='text-embedding-3-large'  # Better quality, higher cost
)
```

---

## 🎓 RAG Integration Examples

### With LangChain

```python
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

# Load ChromaDB
vectorstore = Chroma(
    persist_directory="./chroma_db",
    collection_name="ahk_docs_vectordb",
    embedding_function=OpenAIEmbeddings()
)

# Query
docs = vectorstore.similarity_search("array methods", k=3)
```

### With LlamaIndex

```python
from llama_index import VectorStoreIndex, SimpleDirectoryReader

# Load from JSON
with open('vectorized_docs.json') as f:
    data = json.load(f)

# Create index
documents = [chunk['content'] for chunk in data['chunks']]
index = VectorStoreIndex.from_documents(documents)

# Query
response = index.query("How do I split a string?")
```

### Custom RAG Pipeline

```python
# Load vectorized docs
query_engine = DocQuery('vectorized_docs.json')

# Get relevant chunks
results = query_engine.search("gui creation", n_results=5)

# Build context for LLM
context = "\n\n".join([r['content'] for r in results])

# Query LLM
prompt = f"""Based on this AutoHotkey documentation:

{context}

Answer this question: How do I create a simple GUI window?"""

# Send to your LLM...
```

---

## ⚡ Performance Tips

1. **Batch Processing**: Scripts process in batches (100 chunks) to avoid rate limits
2. **Caching**: Analysis results are cached in JSON
3. **Filtering**: Use category filters to reduce search space
4. **Chunk Size**: 800 tokens is optimal for most models
5. **Embeddings**: Use `text-embedding-3-small` for cost-effectiveness

---

## 🐛 Troubleshooting

### "OpenAI not installed"
```bash
pip install openai
export OPENAI_API_KEY="sk-..."
```

### "ChromaDB not installed"
```bash
pip install chromadb
```

### "No such file or directory"
```bash
# Make sure you're in the right directory
cd /home/user/AHKv2_Docs
python scripts/1_analyze_files.py
```

### Links not updating correctly
The script should handle this, but if issues occur:
- Check that source files use `.htm` extensions in links
- Verify the `analysis_report.json` was created
- Run in dry-run mode first to preview changes

---

## 📝 Summary

**For vectorization, use hierarchical structure because:**

1. ✅ Free metadata from directory structure
2. ✅ Better search filtering capabilities
3. ✅ Improved context for retrieval
4. ✅ More maintainable organization
5. ✅ Better RAG performance

Run the scripts in order (1 → 2 → 3 → 4) for best results!
