from pathlib import Path

from sqlalchemy.orm import Session

from embeddings import generate_embeddings
from models import Document


def load_document(file_path: str) -> str:
    """
    Load a text document from disk.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return path.read_text(encoding="utf-8")


def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50,
) -> list[str]:
    """
    Split text into overlapping chunks.
    """

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0:
        raise ValueError("overlap cannot be negative")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    words = text.split()
    chunks = []

    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)

        if end >= len(words):
            break

        start = end - overlap

    return chunks


def ingest_document(
    db: Session,
    file_path: str,
) -> list[Document]:
    """
    Load, chunk, embed, and store a document in PostgreSQL.
    """

    text = load_document(file_path)

    chunks = chunk_text(text)

    embeddings = generate_embeddings(chunks)

    documents = []

    filename = Path(file_path).name

    for chunk, embedding in zip(chunks, embeddings):
        document = Document(
            filename=filename,
            content=chunk,
            embedding=embedding,
        )

        db.add(document)
        documents.append(document)

    db.commit()

    for document in documents:
        db.refresh(document)

    return documents