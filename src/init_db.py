from database import engine, Base
from models import Document


def initialize_database():
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")


if __name__ == "__main__":
    initialize_database()