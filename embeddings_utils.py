import requests

def create_embedding(text):
    response = requests.post(
        "http://localhost:11434/api/embeddings",
        json={
            "model": "bge-m3",
            "prompt": text
        }
    )

    response.raise_for_status()
    return response.json()["embedding"]