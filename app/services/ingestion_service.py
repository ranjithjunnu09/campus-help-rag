import os
import json

RAW_PATH = "data/raw/campus_handbook.txt"
PROCESSED_PATH = "data/processed/chunks.json"

def read_raw_data():
    if not os.path.exists(RAW_PATH):
        raise Exception("Knowledge base file not found")

    with open(RAW_PATH, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        raise Exception("Knowledge base is empty")

    return text


def chunk_data(text):
    sections = text.split("Section ")[1:]
    chunks = []

    for i, sec in enumerate(sections):
        parts = sec.split("\n", 1)
        title = parts[0].strip()
        content = parts[1].strip()

        chunks.append({
            "chunk_id": f"chunk_{i+1}",
            "section_title": title,
            "text": content,
            "source_file": "campus_handbook.txt"
        })

    return chunks


def save_chunks(chunks):
    os.makedirs("data/processed", exist_ok=True)

    with open(PROCESSED_PATH, "w") as f:
        json.dump(chunks, f, indent=2)