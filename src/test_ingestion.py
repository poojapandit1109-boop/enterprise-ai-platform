from ingestion import load_document, chunk_text


def test_load_document():
    text = load_document("data/company_policy.txt")

    assert text
    assert "Remote Work Policy" in text


def test_chunk_text():
    text = " ".join([f"word{i}" for i in range(1200)])

    chunks = chunk_text(
        text,
        chunk_size=500,
        overlap=50
    )

    assert len(chunks) == 3
    assert len(chunks[0].split()) == 500
    assert len(chunks[1].split()) == 500
    assert len(chunks[2].split()) == 300


def test_invalid_chunk_size():
    text = "This is a test document."

    try:
        chunk_text(text, chunk_size=0)
        assert False
    except ValueError:
        assert True