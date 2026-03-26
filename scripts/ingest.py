from app.services.ingestion_service import read_raw_data, chunk_data, save_chunks
from app.services.llm_service import get_embedding
from app.services.vector_store_service import store_embeddings

def run_ingestion():
    text = read_raw_data()

    chunks = chunk_data(text)

    save_chunks(chunks)

    embeddings = [get_embedding(chunk["text"]) for chunk in chunks]

    store_embeddings(chunks, embeddings)

    print("✅ Ingestion complete!")


if __name__ == "__main__":
    run_ingestion()