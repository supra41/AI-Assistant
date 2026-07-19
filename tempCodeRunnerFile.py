import requests
import os
import json
import pandas as pd


def create_embedding(text_list):
    # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings
    try:
        r = requests.post("http://localhost:11434/api/embed", json={
            "model": "bge-m3",
            "input": text_list
        }, timeout=30)
        r.raise_for_status()
        embedding = r.json().get("embeddings")
        return embedding
    except requests.exceptions.RequestException as e:
        print("Error: could not reach embedding service at http://localhost:11434/api/embed")
        print(f"Detail: {e}")
        return None


if __name__ == "__main__":
    # When run as a script, process all jsons and build the dataframe.
    jsons = os.listdir("jsons")  # List all the jsons 
    my_dicts = []
    chunk_id = 0

    for json_file in jsons:
        with open(f"jsons/{json_file}") as f:
            content = json.load(f)
        print(f"Creating Embeddings for {json_file}")
        embeddings = create_embedding([c['text'] for c in content['chunks']])
           
        for i, chunk in enumerate(content['chunks']):
            chunk['chunk_id'] = chunk_id
            chunk['embedding'] = embeddings[i]
            chunk_id += 1
            my_dicts.append(chunk) 

    df = pd.DataFrame.from_records(my_dicts)
    print(df)
