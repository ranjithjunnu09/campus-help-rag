from app.services.vector_store_service import collection
from app.core.config import settings
from app.services.llm_service import get_embedding

def retrieve_chunks(question: str):
    # Step 1: Convert query → embedding
    query_embedding = get_embedding(question)

    # Step 2: Search in vector DB (TOP_K always)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=settings.TOP_K
    )

    chunks = []

    # Step 3: Collect top_k chunks (NO strict filtering)
    for i in range(len(results["ids"][0])):
        chunks.append({
            "chunk_id": results["ids"][0][i],
            "text": results["documents"][0][i],
            "section_title": results["metadatas"][0][i]["section_title"],
            "source_file": results["metadatas"][0][i]["source_file"]
        })

    return chunks