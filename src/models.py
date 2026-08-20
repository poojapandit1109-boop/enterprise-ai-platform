from sqlalchemy import Column, Integer, String, Text
from pgvector.sqlalchemy import Vector

from database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)

    # Embedding vector
    embedding = Column(Vector(384), nullable=True)