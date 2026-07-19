import requests

def ask_llm(context, question):

    prompt = f"""
You are an AI Teaching Assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{question}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":"llama3.2",
            "prompt":prompt,
            "stream":False
        }
    )

    return response.json()["response"]