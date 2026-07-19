import sys
import joblib

from embeddings_utils import create_embedding
from similarity_utils import get_similarity

# Load the DataFrame
df = joblib.load("embeddings_dataframe.pkl")

# Take user input
incoming_query = input("Ask a Question: ")

# Create embedding for the question
emb = create_embedding(incoming_query)

if not emb:
    if "embedding" in df.columns and df["embedding"].dropna().shape[0] > 0:
        sample = df["embedding"].dropna().iloc[0]
        length = len(sample)

        print(f"Embedding service unavailable. Using zero vector of length {length}.")
        question_embedding = [0.0] * length
    else:
        print("Embedding service unavailable and no reference embeddings found.")
        sys.exit(1)
else:
    question_embedding = emb

print("\nQuestion Embedding Created Successfully!\n")

# -----------------------------
# Calculate similarity scores
# -----------------------------
scores = []

for _, row in df.iterrows():
    score = get_similarity(
        question_embedding,
        row["embedding"]
    )
    scores.append(score)

# Add score column
df["score"] = scores

# Sort DataFrame by similarity
df = df.sort_values(by="score", ascending=False)

# Retrieve top 5 chunks
top5 = df.head(5)

print("=" * 80)
print("Top 5 Most Relevant Chunks")
print("=" * 80)

for i, (_, row) in enumerate(top5.iterrows(), start=1):
    print(f"\nResult {i}")
    print("-" * 80)
    print(f"Similarity : {row['score']:.4f}")
    print(f"Lecture    : {row['number']}")
    print(f"Title       : {row['title']}")
    print(f"Start Time  : {row['start']}")
    print(f"End Time    : {row['end']}")
    print("\nChunk:")
    print(row["text"])