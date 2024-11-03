import React from 'react';

const CitationList = ({ citations }) => {
    return (
        <div>
            <h3 className="citations-heading"> [  ]   CITATIONS</h3>
            <ul>
                {citations.map((citation, index) => (
                    <li key={index}>
                        <a href={citation} target="_blank" rel="noopener noreferrer">
                            {citation}
                        </a>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default CitationList;
