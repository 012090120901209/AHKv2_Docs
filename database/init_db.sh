#!/bin/bash
# Initialize AutoHotkey Documentation Database

set -e

echo "=========================================="
echo "AutoHotkey Documentation Database Setup"
echo "=========================================="
echo ""

# Check if Docker is available
if command -v docker &> /dev/null && command -v docker-compose &> /dev/null; then
    echo "✓ Docker and Docker Compose found"
    USE_DOCKER=true
else
    echo "⚠️  Docker not found. Will use local PostgreSQL."
    USE_DOCKER=false
fi

# Configuration
export POSTGRES_DB=${POSTGRES_DB:-ahk_docs}
export POSTGRES_USER=${POSTGRES_USER:-postgres}
export POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-postgres}
export POSTGRES_HOST=${POSTGRES_HOST:-localhost}
export POSTGRES_PORT=${POSTGRES_PORT:-5432}

if [ "$USE_DOCKER" = true ]; then
    echo ""
    echo "Starting PostgreSQL with Docker..."
    docker-compose up -d postgres

    echo "Waiting for PostgreSQL to be ready..."
    sleep 5

    # Check if healthy
    until docker-compose exec -T postgres pg_isready -U postgres > /dev/null 2>&1; do
        echo "  Waiting for PostgreSQL..."
        sleep 2
    done

    echo "✓ PostgreSQL is ready"
fi

# Create database and schema
echo ""
echo "Creating database schema..."

if [ "$USE_DOCKER" = true ]; then
    docker-compose exec -T postgres psql -U postgres -d ahk_docs < schema.sql
else
    psql -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER -d $POSTGRES_DB < schema.sql
fi

echo "✓ Schema created"

# Load data
echo ""
echo "Loading documentation data..."
echo "This may take a few minutes..."

# Check for Python and psycopg2
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required"
    exit 1
fi

# Install dependencies if needed
if ! python3 -c "import psycopg2" 2>/dev/null; then
    echo "Installing psycopg2..."
    pip3 install psycopg2-binary
fi

# Run data loader
python3 load_data.py ../

echo ""
echo "=========================================="
echo "✓ SETUP COMPLETE!"
echo "=========================================="
echo ""
echo "Database Information:"
echo "  Database: $POSTGRES_DB"
echo "  Host: $POSTGRES_HOST"
echo "  Port: $POSTGRES_PORT"
echo "  User: $POSTGRES_USER"
echo ""

if [ "$USE_DOCKER" = true ]; then
    echo "Docker Services:"
    echo "  PostgreSQL: localhost:5432"
    echo "  pgAdmin: http://localhost:5050"
    echo "    Email: admin@ahkdocs.local"
    echo "    Password: admin"
    echo ""
    echo "Commands:"
    echo "  Stop: docker-compose down"
    echo "  Start: docker-compose up -d"
    echo "  Logs: docker-compose logs -f"
fi

echo ""
echo "Connect to database:"
echo "  psql -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER -d $POSTGRES_DB"
echo ""
echo "Run example queries:"
echo "  psql -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER -d $POSTGRES_DB < query_examples.sql"
echo ""
