import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # ========================
    # OPENROUTER CONFIG
    # ========================
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

    # ========================
    # MODEL CONFIG
    # ========================
    CHAT_MODEL = "meta-llama/llama-3-8b-instruct"   # Free model
    EMBEDDING_MODEL = "all-MiniLM-L6-v2"           # Local embedding model

    # ========================
    # VECTOR STORE CONFIG
    # ========================
    VECTOR_STORE_DIR = "data/vector_store"
    COLLECTION_NAME = "campus_collection"

    # ========================
    # RETRIEVAL CONFIG
    # ========================
    TOP_K = 3

settings = Settings()