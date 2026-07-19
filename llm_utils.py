import requests


def ask_llm(context, question):

    prompt = f"""
You are an AI Teaching Assistant.

Answer ONLY using the context below.

Context:
{context}

Question:
{question}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    print(data)

    if "response" in data:
        return data["response"]

    if "error" in data:
        return data["error"]

    return str(data)