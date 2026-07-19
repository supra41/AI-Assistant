import os
import json
import pandas as pd
import joblib

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

# Save the dataframe
joblib.dump(df, "embeddings_dataframe.pkl")

print("DataFrame saved successfully!")