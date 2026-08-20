from database import SessionLocal
from ingestion import ingest_document


def main():
    db = SessionLocal()

    try:
        document = ingest_document(
            db=db,
            filename="ai_architecture.txt",
            content=(
                "Artificial intelligence systems use machine learning, "
                "large language models, embeddings, vector databases, "
                "and retrieval augmented generation."
            ),
        )

        print("Document stored successfully!")
        print("Document ID:", document.id)
        print("Filename:", document.filename)

    finally:
        db.close()


if __name__ == "__main__":
    main()