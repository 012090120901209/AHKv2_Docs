-- AutoHotkey v2 Documentation Database Schema
-- PostgreSQL database for organized, searchable documentation

-- Enable extensions
CREATE EXTENSION IF NOT EXISTS pg_trgm;  -- For fuzzy text search
CREATE EXTENSION IF NOT EXISTS vector;   -- For embeddings (optional, requires pgvector)

-- ============================================================================
-- CORE TABLES
-- ============================================================================

-- Categories table
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    parent_id INTEGER REFERENCES categories(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_categories_name ON categories(name);

-- Document types
CREATE TYPE doc_type AS ENUM ('function', 'object', 'directive', 'guide', 'reference', 'changelog');

-- Main documents table
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    file_path VARCHAR(500) NOT NULL UNIQUE,
    title TEXT NOT NULL,
    doc_type doc_type NOT NULL,
    category_id INTEGER REFERENCES categories(id),
    subcategory VARCHAR(100),
    description TEXT,
    version VARCHAR(20) DEFAULT 'v2',

    -- Content
    content TEXT,
    raw_markdown TEXT,

    -- Metadata
    line_count INTEGER,
    word_count INTEGER,
    has_code_examples BOOLEAN DEFAULT false,
    has_syntax_section BOOLEAN DEFAULT false,
    has_parameters BOOLEAN DEFAULT false,

    -- Search
    search_vector tsvector,

    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_documents_title ON documents(title);
CREATE INDEX idx_documents_type ON documents(doc_type);
CREATE INDEX idx_documents_category ON documents(category_id);
CREATE INDEX idx_documents_path ON documents(file_path);
CREATE INDEX idx_documents_search ON documents USING gin(search_vector);

-- Sections/chunks within documents
CREATE TABLE sections (
    id SERIAL PRIMARY KEY,
    document_id INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    section_type VARCHAR(50),  -- 'parameters', 'return_value', 'examples', 'remarks', etc.
    heading VARCHAR(255),
    heading_level INTEGER,  -- 1-6 for h1-h6
    content TEXT NOT NULL,
    section_order INTEGER,
    parent_section_id INTEGER REFERENCES sections(id),

    -- Metadata
    word_count INTEGER,
    has_code BOOLEAN DEFAULT false,

    -- Search
    search_vector tsvector,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_sections_document ON sections(document_id);
CREATE INDEX idx_sections_type ON sections(section_type);
CREATE INDEX idx_sections_order ON sections(document_id, section_order);
CREATE INDEX idx_sections_search ON sections USING gin(search_vector);

-- ============================================================================
-- FUNCTION-SPECIFIC TABLES
-- ============================================================================

CREATE TABLE functions (
    id SERIAL PRIMARY KEY,
    document_id INTEGER UNIQUE REFERENCES documents(id) ON DELETE CASCADE,
    function_name VARCHAR(100) NOT NULL UNIQUE,
    syntax TEXT,
    return_type VARCHAR(50),
    return_description TEXT,
    is_method BOOLEAN DEFAULT false,
    parent_object VARCHAR(100),  -- For methods

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_functions_name ON functions(function_name);
CREATE INDEX idx_functions_parent ON functions(parent_object);

CREATE TABLE function_parameters (
    id SERIAL PRIMARY KEY,
    function_id INTEGER NOT NULL REFERENCES functions(id) ON DELETE CASCADE,
    param_name VARCHAR(100) NOT NULL,
    param_type VARCHAR(50),
    is_optional BOOLEAN DEFAULT false,
    default_value TEXT,
    description TEXT,
    param_order INTEGER,

    UNIQUE(function_id, param_name)
);

CREATE INDEX idx_function_params_function ON function_parameters(function_id);

-- ============================================================================
-- OBJECT-SPECIFIC TABLES
-- ============================================================================

CREATE TABLE objects (
    id SERIAL PRIMARY KEY,
    document_id INTEGER UNIQUE REFERENCES documents(id) ON DELETE CASCADE,
    object_name VARCHAR(100) NOT NULL UNIQUE,
    extends VARCHAR(100),  -- Parent class
    is_built_in BOOLEAN DEFAULT true,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_objects_name ON objects(object_name);

CREATE TABLE object_properties (
    id SERIAL PRIMARY KEY,
    object_id INTEGER NOT NULL REFERENCES objects(id) ON DELETE CASCADE,
    property_name VARCHAR(100) NOT NULL,
    property_type VARCHAR(50),
    is_readonly BOOLEAN DEFAULT false,
    description TEXT,

    UNIQUE(object_id, property_name)
);

CREATE INDEX idx_object_props_object ON object_properties(object_id);

CREATE TABLE object_methods (
    id SERIAL PRIMARY KEY,
    object_id INTEGER NOT NULL REFERENCES objects(id) ON DELETE CASCADE,
    method_name VARCHAR(100) NOT NULL,
    syntax TEXT,
    return_type VARCHAR(50),
    description TEXT,
    is_static BOOLEAN DEFAULT false,

    UNIQUE(object_id, method_name)
);

CREATE INDEX idx_object_methods_object ON object_methods(object_id);

-- ============================================================================
-- CODE EXAMPLES
-- ============================================================================

CREATE TABLE code_examples (
    id SERIAL PRIMARY KEY,
    document_id INTEGER REFERENCES documents(id) ON DELETE CASCADE,
    section_id INTEGER REFERENCES sections(id) ON DELETE CASCADE,
    code TEXT NOT NULL,
    language VARCHAR(50) DEFAULT 'ahk',
    description TEXT,
    example_order INTEGER,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_code_examples_document ON code_examples(document_id);
CREATE INDEX idx_code_examples_section ON code_examples(section_id);

-- ============================================================================
-- LINKS AND REFERENCES
-- ============================================================================

CREATE TABLE links (
    id SERIAL PRIMARY KEY,
    source_document_id INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    target_document_id INTEGER REFERENCES documents(id) ON DELETE SET NULL,
    link_text TEXT,
    link_url TEXT NOT NULL,
    is_external BOOLEAN DEFAULT false,
    is_broken BOOLEAN DEFAULT false,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_links_source ON links(source_document_id);
CREATE INDEX idx_links_target ON links(target_document_id);

-- ============================================================================
-- TAGS AND KEYWORDS
-- ============================================================================

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    tag_name VARCHAR(100) UNIQUE NOT NULL,
    tag_type VARCHAR(50),  -- 'keyword', 'feature', 'version', etc.
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_tags_name ON tags(tag_name);

CREATE TABLE document_tags (
    document_id INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    tag_id INTEGER NOT NULL REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (document_id, tag_id)
);

CREATE INDEX idx_document_tags_doc ON document_tags(document_id);
CREATE INDEX idx_document_tags_tag ON document_tags(tag_id);

-- ============================================================================
-- RELATED DOCUMENTS
-- ============================================================================

CREATE TABLE related_documents (
    document_id INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    related_document_id INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    relationship_type VARCHAR(50),  -- 'similar', 'prerequisite', 'see_also', etc.
    PRIMARY KEY (document_id, related_document_id),
    CHECK (document_id != related_document_id)
);

CREATE INDEX idx_related_docs_source ON related_documents(document_id);
CREATE INDEX idx_related_docs_target ON related_documents(related_document_id);

-- ============================================================================
-- VECTOR EMBEDDINGS (optional - requires pgvector extension)
-- ============================================================================

-- Uncomment if you have pgvector installed
/*
CREATE TABLE embeddings (
    id SERIAL PRIMARY KEY,
    document_id INTEGER REFERENCES documents(id) ON DELETE CASCADE,
    section_id INTEGER REFERENCES sections(id) ON DELETE CASCADE,
    embedding vector(1536),  -- OpenAI text-embedding-3-small dimension
    model VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CHECK ((document_id IS NOT NULL) OR (section_id IS NOT NULL))
);

CREATE INDEX idx_embeddings_document ON embeddings(document_id);
CREATE INDEX idx_embeddings_section ON embeddings(section_id);
CREATE INDEX idx_embeddings_vector ON embeddings USING ivfflat (embedding vector_cosine_ops);
*/

-- ============================================================================
-- TRIGGERS FOR SEARCH VECTORS
-- ============================================================================

-- Function to update search vector for documents
CREATE OR REPLACE FUNCTION documents_search_vector_update() RETURNS trigger AS $$
BEGIN
    NEW.search_vector :=
        setweight(to_tsvector('english', COALESCE(NEW.title, '')), 'A') ||
        setweight(to_tsvector('english', COALESCE(NEW.description, '')), 'B') ||
        setweight(to_tsvector('english', COALESCE(NEW.content, '')), 'C');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER documents_search_vector_trigger
BEFORE INSERT OR UPDATE ON documents
FOR EACH ROW EXECUTE FUNCTION documents_search_vector_update();

-- Function to update search vector for sections
CREATE OR REPLACE FUNCTION sections_search_vector_update() RETURNS trigger AS $$
BEGIN
    NEW.search_vector :=
        setweight(to_tsvector('english', COALESCE(NEW.heading, '')), 'A') ||
        setweight(to_tsvector('english', COALESCE(NEW.content, '')), 'B');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER sections_search_vector_trigger
BEFORE INSERT OR UPDATE ON sections
FOR EACH ROW EXECUTE FUNCTION sections_search_vector_update();

-- ============================================================================
-- VIEWS FOR COMMON QUERIES
-- ============================================================================

-- Complete document view with category info
CREATE VIEW v_documents_complete AS
SELECT
    d.*,
    c.name as category_name,
    c.description as category_description,
    (SELECT COUNT(*) FROM sections s WHERE s.document_id = d.id) as section_count,
    (SELECT COUNT(*) FROM code_examples ce WHERE ce.document_id = d.id) as example_count,
    (SELECT COUNT(*) FROM links l WHERE l.source_document_id = d.id) as outbound_link_count,
    (SELECT COUNT(*) FROM links l WHERE l.target_document_id = d.id) as inbound_link_count
FROM documents d
LEFT JOIN categories c ON d.category_id = c.id;

-- Functions with parameters
CREATE VIEW v_functions_complete AS
SELECT
    f.*,
    d.title,
    d.file_path,
    d.description,
    ARRAY_AGG(
        json_build_object(
            'name', fp.param_name,
            'type', fp.param_type,
            'optional', fp.is_optional,
            'default', fp.default_value,
            'description', fp.description
        ) ORDER BY fp.param_order
    ) FILTER (WHERE fp.id IS NOT NULL) as parameters
FROM functions f
JOIN documents d ON f.document_id = d.id
LEFT JOIN function_parameters fp ON f.id = fp.function_id
GROUP BY f.id, d.title, d.file_path, d.description;

-- Objects with methods and properties
CREATE VIEW v_objects_complete AS
SELECT
    o.*,
    d.title,
    d.file_path,
    d.description,
    ARRAY_AGG(DISTINCT op.property_name) FILTER (WHERE op.id IS NOT NULL) as properties,
    ARRAY_AGG(DISTINCT om.method_name) FILTER (WHERE om.id IS NOT NULL) as methods
FROM objects o
JOIN documents d ON o.document_id = d.id
LEFT JOIN object_properties op ON o.id = op.object_id
LEFT JOIN object_methods om ON o.id = om.object_id
GROUP BY o.id, d.title, d.file_path, d.description;

-- ============================================================================
-- HELPER FUNCTIONS
-- ============================================================================

-- Full-text search function
CREATE OR REPLACE FUNCTION search_documents(
    search_query TEXT,
    doc_type_filter doc_type DEFAULT NULL,
    category_filter VARCHAR(50) DEFAULT NULL,
    limit_results INTEGER DEFAULT 20
)
RETURNS TABLE (
    document_id INTEGER,
    title TEXT,
    doc_type doc_type,
    file_path VARCHAR(500),
    rank REAL,
    snippet TEXT
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        d.id,
        d.title,
        d.doc_type,
        d.file_path,
        ts_rank(d.search_vector, plainto_tsquery('english', search_query)) as rank,
        ts_headline('english', d.content, plainto_tsquery('english', search_query),
                   'MaxWords=50, MinWords=25, ShortWord=3') as snippet
    FROM documents d
    LEFT JOIN categories c ON d.category_id = c.id
    WHERE
        d.search_vector @@ plainto_tsquery('english', search_query)
        AND (doc_type_filter IS NULL OR d.doc_type = doc_type_filter)
        AND (category_filter IS NULL OR c.name = category_filter)
    ORDER BY rank DESC
    LIMIT limit_results;
END;
$$ LANGUAGE plpgsql;

-- Find related documents
CREATE OR REPLACE FUNCTION get_related_documents(
    doc_id INTEGER,
    max_results INTEGER DEFAULT 10
)
RETURNS TABLE (
    related_id INTEGER,
    title TEXT,
    relationship_type VARCHAR(50),
    doc_type doc_type
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        d.id,
        d.title,
        rd.relationship_type,
        d.doc_type
    FROM related_documents rd
    JOIN documents d ON rd.related_document_id = d.id
    WHERE rd.document_id = doc_id
    LIMIT max_results;
END;
$$ LANGUAGE plpgsql;

-- ============================================================================
-- SAMPLE DATA INSERTION
-- ============================================================================

-- Insert default categories
INSERT INTO categories (name, description) VALUES
    ('functions', 'Built-in AutoHotkey functions'),
    ('objects', 'Object and class reference'),
    ('directives', 'Compiler directives and preprocessor commands'),
    ('guides', 'Tutorials and conceptual guides'),
    ('reference', 'Reference materials and lookup tables'),
    ('changelog', 'Version history and changes')
ON CONFLICT (name) DO NOTHING;

-- Add subcategories for functions
INSERT INTO categories (name, description, parent_id) VALUES
    ('string', 'String manipulation functions', (SELECT id FROM categories WHERE name = 'functions')),
    ('window', 'Window management functions', (SELECT id FROM categories WHERE name = 'functions')),
    ('file', 'File and directory operations', (SELECT id FROM categories WHERE name = 'functions')),
    ('system', 'System functions', (SELECT id FROM categories WHERE name = 'functions'))
ON CONFLICT (name) DO NOTHING;

-- Add common tags
INSERT INTO tags (tag_name, tag_type) VALUES
    ('v2', 'version'),
    ('deprecated', 'status'),
    ('beginner', 'difficulty'),
    ('advanced', 'difficulty'),
    ('gui', 'feature'),
    ('hotkey', 'feature'),
    ('automation', 'category')
ON CONFLICT (tag_name) DO NOTHING;

-- ============================================================================
-- COMMENTS
-- ============================================================================

COMMENT ON TABLE documents IS 'Main table storing all documentation files';
COMMENT ON TABLE sections IS 'Sections/chunks within documents for detailed indexing';
COMMENT ON TABLE functions IS 'AutoHotkey function documentation';
COMMENT ON TABLE objects IS 'AutoHotkey object/class documentation';
COMMENT ON TABLE code_examples IS 'Code examples extracted from documentation';
COMMENT ON TABLE links IS 'Internal and external links between documents';

COMMENT ON COLUMN documents.search_vector IS 'Full-text search vector for efficient text search';
COMMENT ON COLUMN documents.doc_type IS 'Type of documentation: function, object, guide, etc.';
COMMENT ON COLUMN sections.section_type IS 'Type of section: parameters, examples, remarks, etc.';
