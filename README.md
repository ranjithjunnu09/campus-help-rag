# 🚀 Campus Help Assistant — Mini RAG Backend

> 💡 A knowledge-grounded AI system that answers campus-related queries strictly from a predefined knowledge base (no hallucination).

---

## 🧠 Overview

This project implements a **Retrieval-Augmented Generation (RAG) pipeline** to provide accurate and explainable answers based on a campus handbook.

Unlike traditional LLM applications, this system ensures that:

* ✅ Answers are generated **only from retrieved context**
* ❌ No external knowledge is used
* 🛑 Hallucinations are prevented using strict prompt constraints

---

## 🔧 Tech Stack

* **Backend:** FastAPI
* **Vector Database:** Chroma DB
* **LLM:** OpenRouter (`meta-llama/llama-3-8b-instruct`)
* **Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`)
* **Language:** Python

---

## 🏗️ Architecture

![Architecture](assets/architecture.png)

---

## 🔄 RAG Pipeline Flow

```
User Query
   ↓
Embedding (Sentence Transformers)
   ↓
Vector Search (Chroma DB)
   ↓
Top-K Retrieval (k = 3)
   ↓
Context-Based Prompt
   ↓
LLM (OpenRouter)
   ↓
Structured Response
```

---

## ✂️ Chunking Strategy

* Section-based chunking
* Each section = one chunk
* Maintains semantic clarity and interpretability

---

## 🔍 Retrieval Strategy

* Semantic similarity search using embeddings
* Retrieves **Top-K (k = 3)** relevant chunks
* Balances context coverage and precision

---

## 🛡️ Hallucination Control

The system enforces strict grounding:

* LLM is instructed to answer **only from provided context**
* If answer is not found, it returns:

```
"I do not have enough information in the provided knowledge base to answer that."
```

---

## 📦 API Endpoints

### 🔹 Health Check

```
GET /health
```

---

### 🔹 Chat Endpoint

```
POST /chat
```

#### Request

```json
{
  "question": "What is the revaluation fee?"
}
```

#### Response

```json
{
  "answer": "The revaluation fee is 500 rupees per subject.",
  "sources": [
    {
      "chunk_id": "chunk_4",
      "section_title": "Examination Revaluation",
      "source_file": "campus_handbook.txt"
    }
  ],
  "retrieved_chunks_count": 3
}
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/ranjithjunnu09/campus-help-rag.git
cd campus-help-rag
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add environment variables

Create `.env` file:

```
OPENROUTER_API_KEY=your_api_key_here
```

---

### 5️⃣ Run ingestion

```
python -m scripts.ingest
```

---

### 6️⃣ Start server

```
uvicorn app.main:app --reload
```

---

### 7️⃣ Open API docs

```
http://127.0.0.1:8000/docs
```

---

## 📁 Project Structure

```
rag-backend/
│
├── app/
│   ├── api/
│   ├── services/
│   ├── core/
│   └── main.py
│
├── data/
├── scripts/
├── tests/
├── requirements.txt
└── README.md
```

---

## 💡 Key Learnings

* Vector search returns nearest neighbors, not guaranteed relevance
* Embedding quality directly impacts retrieval accuracy
* Simpler chunking strategies can outperform complex ones
* Prompt design is critical to prevent hallucination
* Structured outputs improve transparency and debugging

---

## 🚀 Future Improvements

* Logging and monitoring system
* WhatsApp bot integration
* Frontend UI for interaction
* Improved ranking / filtering of retrieved chunks

---

## 👨‍💻 Author

**Ranjith J**

---

## ⭐ If you found this useful

Give it a ⭐ on GitHub and feel free to connect!
