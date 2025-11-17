-- AutoHotkey Documentation Database - Query Examples
-- Common queries for accessing the documentation database

-- ============================================================================
-- BASIC QUERIES
-- ============================================================================

-- Get all documents
SELECT id, title, doc_type, file_path
FROM documents
ORDER BY title
LIMIT 20;

-- Get documents by type
SELECT title, file_path, description
FROM documents
WHERE doc_type = 'function'
ORDER BY title;

-- Get all functions
SELECT f.function_name, d.title, d.file_path, f.return_type
FROM functions f
JOIN documents d ON f.document_id = d.id
ORDER BY f.function_name;

-- Get all objects
SELECT o.object_name, o.extends, d.file_path
FROM objects o
JOIN documents d ON o.document_id = d.id
ORDER BY o.object_name;

-- ============================================================================
-- FULL-TEXT SEARCH
-- ============================================================================

-- Search documents by keyword
SELECT * FROM search_documents('array methods', NULL, NULL, 10);

-- Search only functions
SELECT * FROM search_documents('window activate', 'function', NULL, 5);

-- Search in specific category
SELECT * FROM search_documents('string split', NULL, 'functions', 5);

-- Manual full-text search with ranking
SELECT
    d.id,
    d.title,
    d.doc_type,
    d.file_path,
    ts_rank(d.search_vector, query) as rank,
    ts_headline('english', d.content, query, 'MaxWords=50') as snippet
FROM
    documents d,
    plainto_tsquery('english', 'gui button click') as query
WHERE
    d.search_vector @@ query
ORDER BY rank DESC
LIMIT 10;

-- ============================================================================
-- FUNCTION QUERIES
-- ============================================================================

-- Get function with all parameters
SELECT * FROM v_functions_complete
WHERE function_name = 'StrSplit';

-- Find functions with specific parameter
SELECT DISTINCT f.function_name, d.title
FROM functions f
JOIN function_parameters fp ON f.id = fp.function_id
JOIN documents d ON f.document_id = d.id
WHERE fp.param_name ILIKE '%string%'
ORDER BY f.function_name;

-- Find functions by return type
SELECT f.function_name, f.return_type, d.file_path
FROM functions f
JOIN documents d ON f.document_id = d.id
WHERE f.return_type = 'Integer'
ORDER BY f.function_name;

-- Get functions with optional parameters
SELECT DISTINCT f.function_name, COUNT(fp.id) as optional_param_count
FROM functions f
JOIN function_parameters fp ON f.id = fp.function_id
WHERE fp.is_optional = true
GROUP BY f.id, f.function_name
ORDER BY optional_param_count DESC;

-- ============================================================================
-- OBJECT QUERIES
-- ============================================================================

-- Get object with all methods and properties
SELECT * FROM v_objects_complete
WHERE object_name = 'Array';

-- Find objects with specific method
SELECT o.object_name, om.method_name, d.file_path
FROM objects o
JOIN object_methods om ON o.id = om.object_id
JOIN documents d ON o.document_id = d.id
WHERE om.method_name ILIKE '%push%';

-- Get object hierarchy (inheritance)
WITH RECURSIVE obj_hierarchy AS (
    -- Base case
    SELECT o.id, o.object_name, o.extends, 0 as level
    FROM objects o
    WHERE o.extends IS NULL

    UNION ALL

    -- Recursive case
    SELECT o.id, o.object_name, o.extends, h.level + 1
    FROM objects o
    JOIN obj_hierarchy h ON o.extends = h.object_name
)
SELECT
    REPEAT('  ', level) || object_name as hierarchy,
    extends,
    level
FROM obj_hierarchy
ORDER BY level, object_name;

-- ============================================================================
-- CODE EXAMPLE QUERIES
-- ============================================================================

-- Find documents with most code examples
SELECT
    d.title,
    d.file_path,
    COUNT(ce.id) as example_count
FROM documents d
JOIN code_examples ce ON d.id = ce.document_id
GROUP BY d.id, d.title, d.file_path
ORDER BY example_count DESC
LIMIT 20;

-- Get code examples for specific document
SELECT
    ce.code,
    ce.language,
    ce.description
FROM code_examples ce
JOIN documents d ON ce.document_id = d.id
WHERE d.title = 'Array Object'
ORDER BY ce.example_order;

-- Search code examples
SELECT
    d.title,
    ce.code,
    ce.description
FROM code_examples ce
JOIN documents d ON ce.document_id = d.id
WHERE ce.code ILIKE '%loop%'
LIMIT 10;

-- ============================================================================
-- LINK ANALYSIS
-- ============================================================================

-- Find most referenced documents (most inbound links)
SELECT
    d.title,
    d.file_path,
    COUNT(l.id) as inbound_links
FROM documents d
JOIN links l ON d.id = l.target_document_id
GROUP BY d.id, d.title, d.file_path
ORDER BY inbound_links DESC
LIMIT 20;

-- Find documents with most outbound links
SELECT
    d.title,
    d.file_path,
    COUNT(l.id) as outbound_links
FROM documents d
JOIN links l ON d.id = l.source_document_id
GROUP BY d.id, d.title, d.file_path
ORDER BY outbound_links DESC
LIMIT 20;

-- Find broken internal links
SELECT
    d.title as source_doc,
    l.link_text,
    l.link_url
FROM links l
JOIN documents d ON l.source_document_id = d.id
WHERE
    l.is_external = false
    AND l.target_document_id IS NULL
ORDER BY d.title;

-- Get link graph for document
SELECT
    source.title as from_doc,
    target.title as to_doc,
    l.link_text
FROM links l
JOIN documents source ON l.source_document_id = source.id
LEFT JOIN documents target ON l.target_document_id = target.id
WHERE source.title = 'Array Object'
    AND l.is_external = false;

-- ============================================================================
-- SECTION QUERIES
-- ============================================================================

-- Get all sections for a document
SELECT
    s.heading,
    s.heading_level,
    s.section_type,
    LEFT(s.content, 100) as content_preview
FROM sections s
JOIN documents d ON s.document_id = d.id
WHERE d.title = 'Array Object'
ORDER BY s.section_order;

-- Find sections with specific content
SELECT
    d.title,
    s.heading,
    s.section_type
FROM sections s
JOIN documents d ON s.document_id = d.id
WHERE s.content ILIKE '%example%'
ORDER BY d.title;

-- Get parameter sections across all functions
SELECT
    d.title,
    s.heading,
    s.content
FROM sections s
JOIN documents d ON s.document_id = d.id
WHERE s.section_type = 'parameters'
    AND d.doc_type = 'function'
ORDER BY d.title;

-- ============================================================================
-- CATEGORY QUERIES
-- ============================================================================

-- Get document count by category
SELECT
    c.name,
    COUNT(d.id) as doc_count
FROM categories c
LEFT JOIN documents d ON c.id = d.category_id
GROUP BY c.id, c.name
ORDER BY doc_count DESC;

-- Get documents by category
SELECT
    c.name as category,
    d.title,
    d.doc_type
FROM documents d
JOIN categories c ON d.category_id = c.id
WHERE c.name = 'functions'
ORDER BY d.title
LIMIT 20;

-- ============================================================================
-- TAG QUERIES
-- ============================================================================

-- Get documents by tag
SELECT
    d.title,
    d.file_path,
    t.tag_name
FROM documents d
JOIN document_tags dt ON d.id = dt.document_id
JOIN tags t ON dt.tag_id = t.id
WHERE t.tag_name = 'gui'
ORDER BY d.title;

-- Get most common tags
SELECT
    t.tag_name,
    COUNT(dt.document_id) as usage_count
FROM tags t
LEFT JOIN document_tags dt ON t.id = dt.tag_id
GROUP BY t.id, t.tag_name
ORDER BY usage_count DESC;

-- ============================================================================
-- STATISTICS
-- ============================================================================

-- Database statistics
SELECT
    'Documents' as entity,
    COUNT(*) as count
FROM documents

UNION ALL

SELECT 'Sections', COUNT(*) FROM sections
UNION ALL
SELECT 'Functions', COUNT(*) FROM functions
UNION ALL
SELECT 'Objects', COUNT(*) FROM objects
UNION ALL
SELECT 'Code Examples', COUNT(*) FROM code_examples
UNION ALL
SELECT 'Links', COUNT(*) FROM links;

-- Document type distribution
SELECT
    doc_type,
    COUNT(*) as count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER(), 2) as percentage
FROM documents
GROUP BY doc_type
ORDER BY count DESC;

-- Average content statistics
SELECT
    doc_type,
    ROUND(AVG(line_count)) as avg_lines,
    ROUND(AVG(word_count)) as avg_words,
    ROUND(100.0 * SUM(CASE WHEN has_code_examples THEN 1 ELSE 0 END) / COUNT(*), 1) as pct_with_examples
FROM documents
GROUP BY doc_type
ORDER BY avg_words DESC;

-- ============================================================================
-- RELATED DOCUMENTS
-- ============================================================================

-- Get related documents for a specific document
SELECT * FROM get_related_documents(
    (SELECT id FROM documents WHERE title = 'Array Object'),
    10
);

-- Find documents with similar titles (fuzzy matching)
SELECT
    title,
    file_path,
    similarity(title, 'Array') as similarity_score
FROM documents
WHERE similarity(title, 'Array') > 0.3
ORDER BY similarity_score DESC
LIMIT 10;

-- ============================================================================
-- ADVANCED QUERIES
-- ============================================================================

-- Find functions that accept arrays as parameters
SELECT DISTINCT
    f.function_name,
    fp.param_name,
    fp.param_type
FROM functions f
JOIN function_parameters fp ON f.id = fp.function_id
WHERE fp.param_type ILIKE '%array%'
ORDER BY f.function_name;

-- Get complete document information
SELECT * FROM v_documents_complete
WHERE title LIKE '%Win%'
ORDER BY title
LIMIT 10;

-- Find documents that link to each other (mutual links)
SELECT DISTINCT
    d1.title as doc1,
    d2.title as doc2
FROM links l1
JOIN links l2 ON l1.source_document_id = l2.target_document_id
                AND l1.target_document_id = l2.source_document_id
JOIN documents d1 ON l1.source_document_id = d1.id
JOIN documents d2 ON l1.target_document_id = d2.id
WHERE l1.source_document_id < l1.target_document_id  -- Avoid duplicates
ORDER BY d1.title;

-- Export document structure as JSON
SELECT
    json_build_object(
        'title', d.title,
        'type', d.doc_type,
        'path', d.file_path,
        'sections', (
            SELECT json_agg(
                json_build_object(
                    'heading', s.heading,
                    'type', s.section_type,
                    'level', s.heading_level
                )
                ORDER BY s.section_order
            )
            FROM sections s
            WHERE s.document_id = d.id
        ),
        'examples', (
            SELECT json_agg(
                json_build_object(
                    'code', ce.code,
                    'language', ce.language
                )
                ORDER BY ce.example_order
            )
            FROM code_examples ce
            WHERE ce.document_id = d.id
        )
    ) as document_json
FROM documents d
WHERE d.title = 'Array Object';
