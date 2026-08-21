from embeddings import generate_embedding, generate_embeddings


def test_generate_embedding():
    text = "Employees can work remotely."

    embedding = generate_embedding(text)

    assert len(embedding) == 384


def test_generate_embeddings():
    texts = [
        "Employees can work remotely.",
        "Employees must follow company policies.",
        "Remote work requires manager approval.",
    ]

    embeddings = generate_embeddings(texts)

    assert len(embeddings) == 3
    assert all(len(embedding) == 384 for embedding in embeddings)