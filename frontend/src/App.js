import React, { useState } from 'react';
import axios from 'axios';
import SearchBar from './components/SearchBar';
import ResultDisplay from './components/ResultDisplay';
import './components/App.css';

const App = () => {
    const [answer, setAnswer] = useState('');
    const [citations, setCitations] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleSearch = async (query) => {
        setError(null);
        setLoading(true);
        setAnswer('');
        setCitations([]);
        try {
            const response = await axios.get(`${process.env.REACT_APP_BACKEND_URL}/search`, {
                params: { query },
            });
            console.log(response)
            const { gpt_response, citations } = response.data;
            console.log ("citations : ", citations)
            setAnswer(gpt_response);
            setCitations(citations);
            setLoading(false);
        } catch (err) {
            setError('An error occurred. Please try later.');
            console.error(err);
        }
    };

    return (
        <div className="app">
            <h1 className="app-title">
                <span className="title-main">⚅ Perplexity</span>
                <span className="title-greyed"> | By Amit Bhushan</span>
                <span className="title-beta">BETA</span>
            </h1>
            <SearchBar onSearch={handleSearch} />
            {loading && <img src="/Bean Eater2.gif" alt="Loading..." className="loading-gif" />}
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {answer && <ResultDisplay answer={answer} citations={citations} />}
        </div>
    );
};

export default App;
