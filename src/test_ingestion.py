from database import SessionLocal
from ingestion import ingest_document


def test_ingest_document():
    db = SessionLocal()

    try:
        documents = ingest_document(
            db,
            "data/company_policy.txt",
        )

        assert len(documents) > 0

        for document in documents:
            assert document.id is not None
            assert document.filename == "company_policy.txt"
            assert document.content
            assert document.embedding is not None
            assert len(document.embedding) == 384

    finally:
        db.close()