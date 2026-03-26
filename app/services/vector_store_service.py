import chromadb
from app.core.config import settings

client = chromadb.PersistentClient(path=settings.VECTOR_STORE_DIR)
collection = client.get_or_create_collection("campus")

def store_embeddings(chunks, embeddings):
    for i, chunk in enumerate(chunks):
        collection.add(
            ids=[chunk["chunk_id"]],
            documents=[chunk["text"]],
            metadatas=[{
                "section_title": chunk["section_title"],
                "source_file": chunk["source_file"]
            }],
            embeddings=[embeddings[i]]
        )