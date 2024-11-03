import React from 'react';
import CitationList from './CitationList';

const ResultDisplay = ({ answer, citations }) => {
    return (
        <div>
            <h3 className="perplexity-heading">⚡ PERPLEXITY</h3>
            <p>{answer}</p>
            <CitationList citations={citations} />
        </div>
    );
};

export default ResultDisplay;
