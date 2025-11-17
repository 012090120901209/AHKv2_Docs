#!/usr/bin/env python3
"""
Vectorize documentation for RAG/semantic search.
Creates chunks with metadata and embeddings.

Supports multiple vector stores:
- ChromaDB (local)
- Pinecone (cloud)
- JSON export (for custom implementations)
"""

import os
import re
import json
import hashlib
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass, asdict

# Optional dependencies - install as needed
try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

try:
    import chromadb
    HAS_CHROMA = True
except ImportError:
    HAS_CHROMA = False

@dataclass
class DocumentChunk:
    """Represents a chunk of documentation."""
    id: str
    content: str
    metadata: Dict
    embedding: List[float] = None

class DocumentChunker:
    """Smart chunker that preserves context and structure."""

    def __init__(self, chunk_size=800, overlap=150):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_by_section(self, content: str, metadata: Dict) -> List[DocumentChunk]:
        """Chunk document by sections, preserving headers."""
        chunks = []

        # Split by h2 and h3 headers
        sections = re.split(r'\n(#{2,3}\s+.+)\n', content)

        current_chunk = ""
        current_section = metadata.get('title', 'Introduction')
        chunk_index = 0

        for i, part in enumerate(sections):
            # Check if this is a header
            if re.match(r'^#{2,3}\s+', part):
                # Save previous chunk if it exists
                if current_chunk.strip():
                    chunks.append(self._create_chunk(
                        current_chunk, metadata, current_section, chunk_index
                    ))
                    chunk_index += 1

                # Start new chunk with this header
                current_section = part.replace('#', '').strip()
                current_chunk = f"{part}\n\n"
            else:
                # Add content to current chunk
                if len(current_chunk) + len(part) > self.chunk_size:
                    # Save current chunk
                    if current_chunk.strip():
                        chunks.append(self._create_chunk(
                            current_chunk, metadata, current_section, chunk_index
                        ))
                        chunk_index += 1

                    # Start new chunk with overlap
                    overlap_text = current_chunk[-self.overlap:] if len(current_chunk) > self.overlap else current_chunk
                    current_chunk = overlap_text + part
                else:
                    current_chunk += part

        # Add final chunk
        if current_chunk.strip():
            chunks.append(self._create_chunk(
                current_chunk, metadata, current_section, chunk_index
            ))

        # Update total chunks count in metadata
        for chunk in chunks:
            chunk.metadata['total_chunks'] = len(chunks)

        return chunks

    def _create_chunk(self, content: str, file_metadata: Dict, section: str, index: int) -> DocumentChunk:
        """Create a DocumentChunk with metadata."""
        # Generate unique ID
        content_hash = hashlib.md5(content.encode()).hexdigest()[:8]
        chunk_id = f"{file_metadata.get('file_path', 'unknown')}_{index}_{content_hash}"

        # Extract code examples
        has_code = bool(re.search(r'```', content))
        code_examples = len(re.findall(r'```', content)) // 2

        # Build metadata
        metadata = {
            **file_metadata,
            'section': section,
            'chunk_index': index,
            'has_code': has_code,
            'code_examples': code_examples,
            'chunk_length': len(content),
        }

        return DocumentChunk(
            id=chunk_id,
            content=content.strip(),
            metadata=metadata
        )

class DocumentVectorizer:
    """Vectorizes documents using various embedding providers."""

    def __init__(self, provider='openai', model='text-embedding-3-small'):
        self.provider = provider
        self.model = model

        if provider == 'openai':
            if not HAS_OPENAI:
                raise ImportError("OpenAI package not installed. Run: pip install openai")
            self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def embed_chunks(self, chunks: List[DocumentChunk], batch_size=100) -> List[DocumentChunk]:
        """Add embeddings to chunks."""
        if self.provider == 'openai':
            return self._embed_openai(chunks, batch_size)
        else:
            raise ValueError(f"Unknown provider: {self.provider}")

    def _embed_openai(self, chunks: List[DocumentChunk], batch_size: int) -> List[DocumentChunk]:
        """Embed using OpenAI API."""
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]
            texts = [chunk.content for chunk in batch]

            print(f"Embedding batch {i//batch_size + 1}/{(len(chunks)-1)//batch_size + 1}...")

            response = self.client.embeddings.create(
                input=texts,
                model=self.model
            )

            for j, embedding_obj in enumerate(response.data):
                batch[j].embedding = embedding_obj.embedding

        return chunks

def process_file(filepath: Path, base_dir: Path = None) -> Tuple[Dict, str]:
    """Extract metadata and content from a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Calculate relative path
    if base_dir:
        rel_path = str(filepath.relative_to(base_dir))
    else:
        rel_path = filepath.name

    # Determine category from path
    parts = Path(rel_path).parts
    category = parts[0] if len(parts) > 1 else 'root'
    subcategory = parts[1] if len(parts) > 2 else None

    # Extract title
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else filepath.stem

    # Determine doc type
    doc_type = 'reference'
    if category == 'functions':
        doc_type = 'function'
    elif category == 'objects':
        doc_type = 'object'
    elif category == 'guides':
        doc_type = 'guide'
    elif category == 'directives':
        doc_type = 'directive'

    metadata = {
        'file_path': rel_path,
        'filename': filepath.name,
        'category': category,
        'subcategory': subcategory,
        'title': title,
        'doc_type': doc_type,
        'version': 'v2',
    }

    return metadata, content

def vectorize_documentation(
    docs_dir: str = 'docs_reorganized',
    output_format: str = 'json',
    use_embeddings: bool = False
):
    """Main vectorization pipeline."""

    docs_path = Path(docs_dir)
    if not docs_path.exists():
        print(f"Error: Directory '{docs_dir}' not found.")
        print("Run script 2_reorganize_files.py first, or use current directory.")
        docs_path = Path('.')

    # Find all markdown files
    md_files = list(docs_path.rglob('*.md'))
    print(f"Found {len(md_files)} markdown files")

    # Initialize chunker
    chunker = DocumentChunker(chunk_size=800, overlap=150)

    # Process all files
    all_chunks = []

    for i, filepath in enumerate(md_files, 1):
        print(f"[{i}/{len(md_files)}] Processing {filepath.name}...")

        metadata, content = process_file(filepath, docs_path)
        chunks = chunker.chunk_by_section(content, metadata)

        all_chunks.extend(chunks)

    print(f"\nCreated {len(all_chunks)} chunks from {len(md_files)} files")

    # Add embeddings if requested
    if use_embeddings:
        if not HAS_OPENAI:
            print("Warning: OpenAI not available. Skipping embeddings.")
            print("Install with: pip install openai")
        else:
            print("\nGenerating embeddings...")
            vectorizer = DocumentVectorizer(provider='openai')
            all_chunks = vectorizer.embed_chunks(all_chunks)

    # Export based on format
    if output_format == 'json':
        export_to_json(all_chunks, 'vectorized_docs.json')
    elif output_format == 'chromadb':
        export_to_chromadb(all_chunks, 'ahk_docs_vectordb')
    else:
        print(f"Unknown format: {output_format}")

def export_to_json(chunks: List[DocumentChunk], output_file: str):
    """Export chunks to JSON."""
    data = {
        'chunks': [
            {
                'id': chunk.id,
                'content': chunk.content,
                'metadata': chunk.metadata,
                'embedding': chunk.embedding
            }
            for chunk in chunks
        ],
        'stats': {
            'total_chunks': len(chunks),
            'total_files': len(set(c.metadata['file_path'] for c in chunks)),
            'categories': list(set(c.metadata['category'] for c in chunks)),
        }
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print(f"\nExported to {output_file}")
    print(f"Total size: {os.path.getsize(output_file) / 1024 / 1024:.2f} MB")

def export_to_chromadb(chunks: List[DocumentChunk], collection_name: str):
    """Export to ChromaDB."""
    if not HAS_CHROMA:
        print("ChromaDB not installed. Install with: pip install chromadb")
        return

    client = chromadb.PersistentClient(path="./chroma_db")

    # Create or get collection
    collection = client.get_or_create_collection(
        name=collection_name,
        metadata={"description": "AutoHotkey v2 Documentation"}
    )

    # Add chunks
    batch_size = 100
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]

        collection.add(
            ids=[c.id for c in batch],
            documents=[c.content for c in batch],
            metadatas=[c.metadata for c in batch],
            embeddings=[c.embedding for c in batch] if batch[0].embedding else None
        )

        print(f"Added batch {i//batch_size + 1}/{(len(chunks)-1)//batch_size + 1}")

    print(f"\nCreated ChromaDB collection: {collection_name}")
    print(f"Location: ./chroma_db")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Vectorize AutoHotkey documentation')
    parser.add_argument('--input', default='docs_reorganized',
                        help='Input directory (default: docs_reorganized)')
    parser.add_argument('--format', choices=['json', 'chromadb'], default='json',
                        help='Output format (default: json)')
    parser.add_argument('--embed', action='store_true',
                        help='Generate embeddings (requires OpenAI API key)')

    args = parser.parse_args()

    vectorize_documentation(
        docs_dir=args.input,
        output_format=args.format,
        use_embeddings=args.embed
    )
