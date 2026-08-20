from sqlalchemy.orm import Session

from embeddings import generate_embedding
from models import Document


def ingest_document(
    db: Session,
    filename: str,
    content: str,
) -> Document:
    """
    Store a document and its embedding in PostgreSQL.
    """

    embedding = generate_embedding(content)

    document = Document(
        filename=filename,
        content=content,
        embedding=embedding,
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document