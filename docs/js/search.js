// Search functionality

let searchIndex = [];
let searchResults = document.getElementById('searchResults');
let searchInput = document.getElementById('searchInput');

// Load search index
async function loadSearchIndex() {
    try {
        const response = await fetch('/search-index.json');
        searchIndex = await response.json();
    } catch (error) {
        console.error('Failed to load search index:', error);
    }
}

// Search function
function search(query) {
    if (!query || query.length < 2) {
        return [];
    }

    query = query.toLowerCase();
    const results = [];

    for (const doc of searchIndex) {
        const titleMatch = doc.title.toLowerCase().includes(query);
        const contentMatch = doc.content.toLowerCase().includes(query);

        if (titleMatch || contentMatch) {
            const score = (titleMatch ? 10 : 0) + (contentMatch ? 1 : 0);
            const snippet = getSnippet(doc.content, query);

            results.push({
                ...doc,
                score,
                snippet
            });
        }
    }

    return results.sort((a, b) => b.score - a.score).slice(0, 10);
}

// Get content snippet around query
function getSnippet(content, query, contextLength = 100) {
    const lowerContent = content.toLowerCase();
    const index = lowerContent.indexOf(query.toLowerCase());

    if (index === -1) {
        return content.substring(0, contextLength) + '...';
    }

    const start = Math.max(0, index - contextLength / 2);
    const end = Math.min(content.length, index + query.length + contextLength / 2);

    let snippet = content.substring(start, end);

    if (start > 0) snippet = '...' + snippet;
    if (end < content.length) snippet = snippet + '...';

    // Highlight the query
    const regex = new RegExp(`(${query})`, 'gi');
    snippet = snippet.replace(regex, '<span class="search-result-highlight">$1</span>');

    return snippet;
}

// Display search results
function displayResults(results) {
    if (results.length === 0) {
        searchResults.innerHTML = '<div class="search-result-item"><div class="search-result-title">No results found</div></div>';
        searchResults.style.display = 'block';
        return;
    }

    const html = results.map(result => `
        <a href="${result.url}" class="search-result-item">
            <div class="search-result-title">${result.title}</div>
            <div class="search-result-path">${result.path || ''}</div>
            <div class="search-result-snippet">${result.snippet}</div>
        </a>
    `).join('');

    searchResults.innerHTML = html;
    searchResults.style.display = 'block';
}

// Event listeners
if (searchInput) {
    let searchTimeout;

    searchInput.addEventListener('input', (e) => {
        clearTimeout(searchTimeout);
        const query = e.target.value;

        if (query.length < 2) {
            searchResults.style.display = 'none';
            return;
        }

        searchTimeout = setTimeout(() => {
            const results = search(query);
            displayResults(results);
        }, 200);
    });

    searchInput.addEventListener('focus', (e) => {
        if (e.target.value.length >= 2) {
            searchResults.style.display = 'block';
        }
    });

    // Close search results when clicking outside
    document.addEventListener('click', (e) => {
        if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
            searchResults.style.display = 'none';
        }
    });

    // Keyboard shortcut: Ctrl+K or Cmd+K
    document.addEventListener('keydown', (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            searchInput.focus();
        }

        // Escape to close
        if (e.key === 'Escape') {
            searchResults.style.display = 'none';
            searchInput.blur();
        }
    });
}

// Initialize
loadSearchIndex();
