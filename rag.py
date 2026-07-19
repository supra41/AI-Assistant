import joblib

from embeddings_utils import create_embedding
from similarity_utils import get_similarity

# Load the DataFrame only once
df = joblib.load("embeddings_dataframe.pkl")


def retrieve(question, top_k=5):
    """
    Retrieves the top-k most relevant chunks for the given question.
    """

    # Create embedding for the user's question
    question_embedding = create_embedding(question)

    if not question_embedding:
        raise Exception("Failed to create question embedding.")

    scores = []

    # Calculate cosine similarity with every chunk
    for _, row in df.iterrows():

        score = get_similarity(
            question_embedding,
            row["embedding"]
        )

        scores.append(score)

    # Create a copy to avoid modifying the original dataframe
    result_df = df.copy()

    result_df["score"] = scores

    # Sort by similarity
    result_df = result_df.sort_values(
        by="score",
        ascending=False
    )

    # Return Top-K chunks
    return result_df.head(top_k)