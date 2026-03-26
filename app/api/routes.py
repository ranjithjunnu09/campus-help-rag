from fastapi import APIRouter
from app.core.models import ChatRequest
from app.services.retrieval_service import retrieve_chunks
from app.services.prompt_service import build_prompt
from app.services.llm_service import generate_answer

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/chat")
def chat(request: ChatRequest):
    question = request.question.strip()

    if not question:
        return {
            "answer": "Question cannot be empty",
            "sources": [],
            "retrieved_chunks_count": 0
        }

    # Step 1: Retrieve top_k chunks
    chunks = retrieve_chunks(question)

    # Step 2: Build prompt
    prompt = build_prompt(chunks, question)

    # Step 3: Get answer from LLM
    answer = generate_answer(prompt)

    # Step 4: Handle NO-ANSWER case
    if "do not have enough information" in answer.lower():
        return {
            "answer": answer,
            "sources": [],
            "retrieved_chunks_count": 0
        }

    # Step 5: Format sources (REMOVE text field)
    formatted_sources = [
        {
            "chunk_id": c["chunk_id"],
            "section_title": c["section_title"].split(":", 1)[-1].strip(),
            "source_file": c["source_file"]
        }
        for c in chunks
    ]

    return {
        "answer": answer,
        "sources": formatted_sources,
        "retrieved_chunks_count": len(chunks)
    }