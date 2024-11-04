from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Mini Perplexity Q&A System!"}

def test_search_endpoint():
    response = client.get("/search?query=example")
    assert response.status_code == 200
    assert "gpt_response" in response.json()
    assert "sources" in response.json()
    assert "citations" in response.json()
