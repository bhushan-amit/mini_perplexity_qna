import React, { useState } from 'react';

const SearchBar = ({ onSearch }) => {
    const [query, setQuery] = useState('');

    const handleSearch = () => {
        onSearch(query);
    };

    const handleKeyUp = (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            handleSearch();
        }
    };

    return (
        <div className="search-bar-container">
            <span className="chat-icon">💬</span>
            <input
                type="text"
                placeholder="Tell me about..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                onKeyUp={handleKeyUp}
                className="search-input"
            />
            <button onClick={handleSearch} className="search-button">Search</button>
        </div>
    );
};

export default SearchBar;
