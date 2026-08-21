from sentence_transformers import SentenceTransformer


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def generate_embedding(text: str) -> list[float]:
    """
    Generate a 384-dimensional embedding for the supplied text.
    """
    embedding = model.encode(text)
    return embedding.tolist()


def generate_embeddings(texts: list[str]) -> list[list[float]]:
    """
    Generate embeddings for multiple text chunks.
    """
    embeddings = model.encode(texts)
    return embeddings.tolist()