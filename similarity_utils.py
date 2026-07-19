from sklearn.metrics.pairwise import cosine_similarity

def get_similarity(question_embedding, chunk_embedding):
    return cosine_similarity(
        [question_embedding],
        [chunk_embedding]
    )[0][0]