#!/usr/bin/env python3
"""
Query vectorized documentation for semantic search.
Example usage of the vectorized docs.
"""

import json
import numpy as np
from typing import List, Dict
from pathlib import Path

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

class DocQuery:
    """Query interface for vectorized documentation."""

    def __init__(self, data_source='vectorized_docs.json', provider='openai'):
        self.provider = provider
        self.chunks = []

        if data_source.endswith('.json'):
            self.load_json(data_source)
            self.mode = 'json'
        else:
            self.load_chromadb(data_source)
            self.mode = 'chromadb'

        if provider == 'openai' and HAS_OPENAI:
            self.client = OpenAI()

    def load_json(self, filepath: str):
        """Load chunks from JSON file."""
        with open(filepath, 'r') as f:
            data = json.load(f)
            self.chunks = data['chunks']
            self.stats = data.get('stats', {})

        print(f"Loaded {len(self.chunks)} chunks")
        print(f"Categories: {', '.join(self.stats.get('categories', []))}")

    def load_chromadb(self, collection_name: str):
        """Load from ChromaDB collection."""
        if not HAS_CHROMA:
            raise ImportError("ChromaDB not installed")

        client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = client.get_collection(name=collection_name)
        print(f"Connected to ChromaDB collection: {collection_name}")

    def embed_query(self, query: str) -> List[float]:
        """Generate embedding for query."""
        if self.provider == 'openai':
            response = self.client.embeddings.create(
                input=query,
                model='text-embedding-3-small'
            )
            return response.data[0].embedding
        return None

    def cosine_similarity(self, a: List[float], b: List[float]) -> float:
        """Calculate cosine similarity between two vectors."""
        a = np.array(a)
        b = np.array(b)
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def search(self, query: str, n_results: int = 5, category_filter: str = None) -> List[Dict]:
        """Search documentation."""
        if self.mode == 'chromadb':
            return self.search_chromadb(query, n_results, category_filter)
        else:
            return self.search_json(query, n_results, category_filter)

    def search_chromadb(self, query: str, n_results: int, category_filter: str) -> List[Dict]:
        """Search using ChromaDB."""
        where_filter = {"category": category_filter} if category_filter else None

        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where=where_filter
        )

        return [
            {
                'content': doc,
                'metadata': meta,
                'distance': dist
            }
            for doc, meta, dist in zip(
                results['documents'][0],
                results['metadatas'][0],
                results['distances'][0]
            )
        ]

    def search_json(self, query: str, n_results: int, category_filter: str) -> List[Dict]:
        """Search using JSON data with embeddings."""
        # Filter by category if specified
        chunks = self.chunks
        if category_filter:
            chunks = [c for c in chunks if c['metadata'].get('category') == category_filter]

        # If no embeddings, fall back to keyword search
        if not chunks or not chunks[0].get('embedding'):
            return self.keyword_search(query, chunks, n_results)

        # Embed query
        query_embedding = self.embed_query(query)

        # Calculate similarities
        scored_chunks = []
        for chunk in chunks:
            if chunk.get('embedding'):
                similarity = self.cosine_similarity(query_embedding, chunk['embedding'])
                scored_chunks.append((similarity, chunk))

        # Sort by similarity
        scored_chunks.sort(reverse=True, key=lambda x: x[0])

        # Return top results
        return [
            {
                'content': chunk['content'],
                'metadata': chunk['metadata'],
                'similarity': score
            }
            for score, chunk in scored_chunks[:n_results]
        ]

    def keyword_search(self, query: str, chunks: List[Dict], n_results: int) -> List[Dict]:
        """Fallback keyword search when embeddings not available."""
        query_terms = query.lower().split()

        scored_chunks = []
        for chunk in chunks:
            content_lower = chunk['content'].lower()
            score = sum(content_lower.count(term) for term in query_terms)

            if score > 0:
                scored_chunks.append((score, chunk))

        scored_chunks.sort(reverse=True, key=lambda x: x[0])

        return [
            {
                'content': chunk['content'],
                'metadata': chunk['metadata'],
                'score': score
            }
            for score, chunk in scored_chunks[:n_results]
        ]

    def get_by_category(self, category: str) -> List[str]:
        """Get all files in a category."""
        if self.mode == 'json':
            files = set()
            for chunk in self.chunks:
                if chunk['metadata'].get('category') == category:
                    files.add(chunk['metadata']['file_path'])
            return sorted(list(files))
        return []

def format_result(result: Dict, index: int):
    """Format a search result for display."""
    meta = result['metadata']
    content = result['content']

    # Truncate content
    if len(content) > 200:
        content = content[:200] + "..."

    score = result.get('similarity', result.get('score', 0))

    print(f"\n--- Result {index + 1} (Score: {score:.4f}) ---")
    print(f"File: {meta.get('file_path', 'unknown')}")
    print(f"Category: {meta.get('category', 'unknown')}")
    print(f"Section: {meta.get('section', 'unknown')}")
    print(f"\n{content}\n")

def interactive_search(query_engine: DocQuery):
    """Interactive search loop."""
    print("\n" + "=" * 70)
    print("AutoHotkey Documentation Search")
    print("=" * 70)
    print("\nCommands:")
    print("  search <query>           - Search documentation")
    print("  filter <category>        - Set category filter")
    print("  category <name>          - List files in category")
    print("  categories               - List all categories")
    print("  quit                     - Exit")
    print("")

    category_filter = None

    while True:
        try:
            cmd = input("\n> ").strip()

            if not cmd:
                continue

            if cmd == 'quit':
                break

            elif cmd == 'categories':
                if hasattr(query_engine, 'stats'):
                    cats = query_engine.stats.get('categories', [])
                    print(f"\nCategories: {', '.join(cats)}")
                else:
                    print("\nCategories: functions, objects, guides, reference, directives")

            elif cmd.startswith('category '):
                category = cmd[9:].strip()
                files = query_engine.get_by_category(category)
                print(f"\nFiles in {category}:")
                for f in files:
                    print(f"  - {f}")

            elif cmd.startswith('filter '):
                category_filter = cmd[7:].strip()
                print(f"Filter set to: {category_filter}")

            elif cmd.startswith('search '):
                query = cmd[7:].strip()

                if not query:
                    print("Please provide a search query")
                    continue

                print(f"\nSearching for: '{query}'")
                if category_filter:
                    print(f"Filter: {category_filter}")

                results = query_engine.search(query, n_results=5, category_filter=category_filter)

                if not results:
                    print("\nNo results found")
                else:
                    for i, result in enumerate(results):
                        format_result(result, i)

            else:
                print("Unknown command. Try 'search <query>' or 'quit'")

        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Query AutoHotkey documentation')
    parser.add_argument('--source', default='vectorized_docs.json',
                        help='Data source (JSON file or ChromaDB collection name)')
    parser.add_argument('--query', help='Single query (non-interactive)')
    parser.add_argument('--category', help='Filter by category')

    args = parser.parse_args()

    # Initialize query engine
    query_engine = DocQuery(data_source=args.source)

    if args.query:
        # Single query mode
        results = query_engine.search(args.query, category_filter=args.category)

        for i, result in enumerate(results):
            format_result(result, i)
    else:
        # Interactive mode
        interactive_search(query_engine)
