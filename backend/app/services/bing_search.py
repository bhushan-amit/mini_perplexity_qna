import requests
from fastapi import HTTPException
from bs4 import BeautifulSoup
import re
from app.core.config import settings

def extract_main_content(url, word_limit=200):
    """
    Extracts the main content from a given URL up to a specified word limit.
    """
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        paragraphs = soup.find_all('p')
        text_content = ""

        for para in paragraphs:
            text = para.get_text(strip=True)
            text = re.sub(r'\s+', ' ', text)

            if len(text.split()) > 5:  # Ignore very short paragraphs
                text_content += " " + text

            if len(text_content.split()) >= word_limit:
                break

        trimmed_text = ' '.join(text_content.split()[:word_limit])
        return trimmed_text

    except Exception as e:
        print(f"Failed to fetch content from {url}: {e}")
        return None

def search_bing_query(query):
    """
    Searches Bing for a query and returns formatted search results along with a prompt for GPT.
    """
    bing_api_url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": settings.bing_search_api_key}
    params = {"q": query, "textDecorations": True, "textFormat": "HTML"}

    response = requests.get(bing_api_url, headers=headers, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error with Bing Search API")

    search_results = response.json()
    top_results = search_results.get("webPages", {}).get("value", [])[:2]

    results = []
    prompt_content = "Here is the query and its search result. Query: '{}'\n\n".format(query)

    for result in top_results:
        url = result["url"]
        snippet = result["snippet"]

        # Extract main content from the URL
        content = extract_main_content(url)

        # Append data in desired format
        results.append({
            "url": url,
            "snippet": snippet,
            "content": content
        })

        prompt_content += f"Snippet: {snippet}\nContent: {content}\n\n"

    return results, prompt_content
