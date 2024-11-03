from fastapi import FastAPI, HTTPException
from app.core.config import settings
from app.services.bing_search import search_bing_query, extract_main_content
from app.services.gpt_integration import generate_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend's URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to Mini Perplexity Q&A System!"}


@app.get("/keys")
async def get_keys():
    return {
        "bing_search_api_key": settings.bing_search_api_key,
        "openai_api_key": settings.openai_api_key
    }


@app.get("/search")
async def answer_search(query: str):
    """
    Search endpoint that uses Bing Search API to retrieve results for a query,
    extracts the snippet, URL, and content from the top 2 results, and generates a GPT response.
    """
    try:
        results, prompt_content = search_bing_query(query)
        gpt_response = generate_response(prompt_content)

        # Return the result including URLs, snippets, content, and GPT response
        return {
            "sources": results,
            "gpt_response": gpt_response,
            "citations": [result["url"] for result in results]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
