import os
import json
import requests

CHUNK_DIR = "chunks"
OUTPUT_DIR = "embeddings"

os.makedirs(OUTPUT_DIR, exist_ok=True)


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


# Sort files based on lecture number
files = sorted(
    os.listdir(CHUNK_DIR),
    key=lambda x: int(x.split("_")[0])
)

for filename in files:

    print(f"Processing {filename}...")

    with open(
        os.path.join(CHUNK_DIR, filename),
        "r",
        encoding="utf-8"
    ) as f:
        data = json.load(f)

    embedded_chunks = []

    for chunk in data["chunks"]:

        embedding = create_embedding(chunk["text"])

        embedded_chunks.append({
            "number": chunk["number"],
            "title": chunk["title"],
            "start": chunk["start"],
            "end": chunk["end"],
            "text": chunk["text"],
            "embedding": embedding
        })

    output = {
        "text": data["text"],
        "chunks": embedded_chunks
    }

    output_path = os.path.join(OUTPUT_DIR, filename)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False)

print("All embeddings created successfully.")