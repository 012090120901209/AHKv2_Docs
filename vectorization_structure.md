# Recommended Directory Structure for Vectorization

## Proposed Organization

```
/docs/
  /functions/           # Built-in functions (200+ files)
    /string/           # String functions (Str*, InStr, Format, etc.)
    /file/             # File operations (File*, Dir*)
    /window/           # Window management (Win*, Control*)
    /system/           # System functions (Process*, Run, etc.)
    /gui/              # GUI-related functions
    /misc/             # Other functions

  /objects/            # Object/Class documentation (30+ files)
    Array.md
    Map.md
    Gui.md
    GuiControl.md
    Error.md
    Buffer.md
    etc.

  /directives/         # Compiler directives (20+ files)
    _Include.md
    _Requires.md
    _HotIf.md
    etc.

  /guides/             # Tutorials and guides (20+ files)
    Tutorial.md
    FAQ.md
    Concepts.md
    Scripts.md
    Program.md
    etc.

  /reference/          # Reference materials (30+ files)
    /hotkeys/
      Hotkeys.md
      Hotstring.md
      WriteHotkeys.md
    /language/
      Language.md
      Variables.md
      Functions.md
      Objects.md
    /tables/
      KeyList.md
      Colors.md
      Styles.md
      SendKeys.md

  /changelog/
    ChangeLog.md
    v2-changes.md
    v1-changes.md
    Compat.md
```

## Vectorization Benefits

### 1. Metadata Structure
Each chunk gets automatic metadata:
```json
{
  "file_path": "functions/string/StrSplit.md",
  "category": "functions",
  "subcategory": "string",
  "doc_type": "function_reference",
  "title": "StrSplit",
  "chunk_id": "functions_string_strsplit_1"
}
```

### 2. Contextual Chunking Strategy

**Small Chunks with Rich Context:**
- Chunk size: 500-1000 tokens
- Include file path in metadata
- Preserve section headers
- Add category tags

**Example Chunk:**
```
[Category: functions/string]
[File: StrSplit.md]
[Section: Parameters]

StrSplit splits a string into an array of substrings using
the specified delimiters.

Parameters:
- String: The string to split
- Delimiters: Characters to split on
- OmitChars: Characters to exclude
...
```

### 3. Retrieval Strategies

**Hybrid Search:**
1. Semantic search across all chunks
2. Filter by category metadata
3. Re-rank by relevance + category match

**Category-Specific Queries:**
- "array methods" → Filter: category=objects, file=Array.md
- "string functions" → Filter: category=functions, subcategory=string
- "hotkey syntax" → Filter: category=reference, subcategory=hotkeys

### 4. Chunk Overlap Strategy

For better context preservation:
- 100-200 token overlap between chunks
- Preserve section boundaries
- Keep code examples intact
- Maintain heading hierarchy

## Implementation Notes

### File Categorization Rules

**Functions** (files matching pattern):
- Win*.md → functions/window/
- Control*.md → functions/window/
- File*.md, Dir*.md → functions/file/
- Str*.md, InStr.md, etc. → functions/string/
- Process*.md, Run*.md → functions/system/
- Sound*.md, Mouse*.md, etc. → functions/misc/

**Objects** (files with "Object" or class-like structure):
- Array.md, Map.md, Object.md → objects/
- Gui.md, GuiControl.md → objects/
- Error.md, Buffer.md, File.md → objects/

**Directives** (files starting with _):
- _*.md → directives/

**Guides** (conceptual/tutorial content):
- Tutorial.md, FAQ.md, Concepts.md → guides/
- Scripts.md, Program.md → guides/

**Reference** (lookup tables, comprehensive lists):
- KeyList.md, Colors.md, Styles.md → reference/tables/
- Hotkeys.md, Hotstrings.md → reference/hotkeys/
- Language.md, Variables.md, Functions.md, Objects.md → reference/language/

### Embedding Model Considerations

**Recommended Models:**
- OpenAI: text-embedding-3-large (3072 dimensions)
- Open source: all-MiniLM-L6-v2 (384 dimensions) for smaller deployment
- Cohere: embed-english-v3.0 for better technical docs

**Chunk Size Optimization:**
- Target: 512-768 tokens per chunk
- Max: 1024 tokens
- Overlap: 128 tokens

### Vector DB Schema

```python
{
    "id": "uuid",
    "content": "chunk text",
    "embedding": [vector],
    "metadata": {
        "file_path": "str",
        "category": "str",
        "subcategory": "str",
        "title": "str",
        "section": "str",
        "chunk_index": int,
        "total_chunks": int,
        "version": "v2",
        "has_code_example": bool,
        "doc_type": "function|object|guide|reference|directive"
    }
}
```

### Query Enhancement

**Pre-processing queries:**
1. Classify intent (function lookup, how-to, reference)
2. Extract key terms (function names, object types)
3. Apply category filters
4. Expand synonyms (e.g., "array" → ["Array", "list", "collection"])

**Post-processing results:**
1. Group by file (show related sections together)
2. Highlight code examples
3. Show breadcrumb (category/subcategory/file)
4. Include related links from same category
