from embeddings import generate_embedding

text = "Enterprise AI platform for document search"

embedding = generate_embedding(text)

print("Embedding generated successfully!")
print("Vector dimensions:", len(embedding))
print("First 5 values:", embedding[:5])
