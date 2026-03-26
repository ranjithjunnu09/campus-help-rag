from sentence_transformers import SentenceTransformer
import requests
import os
from app.core.config import settings

# ========================
# LOAD EMBEDDING MODEL (LOCAL)
# ========================
embedding_model = SentenceTransformer(settings.EMBEDDING_MODEL)

# ========================
# EMBEDDING FUNCTION
# ========================
def get_embedding(text: str):
    return embedding_model.encode(text).tolist()

# ========================
# OPENROUTER LLM CALL
# ========================
def generate_answer(prompt: str):
    url = settings.OPENROUTER_BASE_URL + "/chat/completions"

    headers = {
        "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": settings.CHAT_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        raise Exception(f"LLM Error: {response.text}")

    return response.json()["choices"][0]["message"]["content"].strip()