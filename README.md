
# Mini Perplexity Q&A System

This project is a Mini Perplexity Q&A System, featuring a FastAPI backend and React frontend to provide answers to user queries. It uses Bing Search API for web data and OpenAI LLMs for response generation, offering search results and GPT-powered answers. Below are setup, deployment, and usage instructions.

## Table of Contents

- [Overview](#overview)
- [Setup and Installation](#setup-and-installation)
- [Deployment](#deployment)
- [Usage](#usage)
- [Design Decisions and Challenges](#design-decisions-and-challenges)
- [Future Improvements](#future-improvements)

---

## Overview

This system aims to answer user questions using the Bing Search API to retrieve relevant web information and GPT-4 to generate responses. The backend fetches, processes, and passes the data to the frontend, which provides an interface for user interaction.

## Setup and Installation

### Prerequisites

- Python 3.7+
- Node.js and npm
- API keys for Bing Search and OpenAI

### Backend (FastAPI)

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd mini_perplexity_qna
   ```

2. **Navigate to the backend directory:**

   ```bash
   cd backend
   ```

3. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   ```

   - **For MacOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

   - **For Windows:**
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables in `.env`:**

   ```plaintext
   BING_SEARCH_API_KEY=your_bing_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

6. **Start the FastAPI backend:**

   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend (React)

1. **Navigate to the frontend directory:**

   ```bash
   cd ../frontend
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Set the backend API endpoint in the frontend configuration (e.g., `.env` or configuration file).**

4. **Start the React frontend:**

   ```bash
   npm start
   ```

## Deployment



## Usage

1. Open the frontend URL in your browser.
2. Enter a query in the search box and hit enter.
3. View the response from GPT-4 and citations from Bing in the results area.

## Design Decisions and Challenges

- **Content Extraction**: Used BeautifulSoup to fetch and process relevant text from sources, balancing accuracy with performance.


## Future Improvements

- **Caching**: Integrate a caching system for frequent queries.
- **Expanded API Options**: Add support for other search APIs or AI models.

---

For any questions, please feel free to reach out.
