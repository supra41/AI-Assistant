import os
import json
import pandas as pd

embedding_files = sorted(
    os.listdir("embeddings"),
    key=lambda x: int(x.split("_")[0])
)

all_chunks = []

for file in embedding_files:
    with open(f"embeddings/{file}", "r", encoding="utf-8") as f:
        content = json.load(f)

    all_chunks.extend(content["chunks"])

df = pd.DataFrame.from_records(all_chunks)

print(df.head())
print(df.shape)