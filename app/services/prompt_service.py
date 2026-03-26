def build_prompt(chunks, question):
    context = "\n\n".join([c["text"] for c in chunks])

    return f"""
You are a helpful campus assistant.

Answer ONLY from the provided context.
If the answer is not in the context, say:
"I do not have enough information in the provided knowledge base to answer that."

Context:
{context}

Question:
{question}

Answer:
"""