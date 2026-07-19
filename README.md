# 🎓 AI Teaching Assistant (Local RAG)

A **Retrieval-Augmented Generation (RAG)** based AI Teaching Assistant that answers questions from lecture videos using semantic search and a local Large Language Model (LLM).

## ✨ Features

- 🎥 Convert lecture videos into searchable knowledge
- 📝 Lecture transcription using Whisper
- 🧠 Generate embeddings with **BGE-M3**
- 🔍 Semantic search using **Cosine Similarity**
- 🤖 Answer questions using **Llama 3.2 (Ollama)**
- ⚡ Fully local and offline
- 💾 Efficient storage with Joblib

---

## 🏗️ Workflow

```text
Lecture Videos
      │
      ▼
Whisper Transcription
      │
      ▼
Text Chunking
      │
      ▼
BGE-M3 Embeddings
      │
      ▼
Joblib DataFrame
      │
      ▼
User Question
      │
      ▼
Question Embedding
      │
      ▼
Top-K Retrieval
      │
      ▼
Llama 3.2 (Ollama)
      │
      ▼
Final Answer
```

---

## 🛠️ Tech Stack

- Python
- Pandas
- OpenAI Whisper
- Ollama
- BGE-M3
- Llama 3.2
- Scikit-Learn
- Joblib

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Teaching-Assistant.git
cd AI-Teaching-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download the required Ollama models:

```bash
ollama pull bge-m3
ollama pull llama3.2
```

Run the project:

```bash
python create_embeddings.py
python create_dataframe.py
python pandas_df.py
```

---

## 📂 Project Structure

```text
AI-Teaching-Assistant/
│── audios/
│── chunks/
│── embeddings/
│── create_embeddings.py
│── create_dataframe.py
│── embeddings_utils.py
│── similarity_utils.py
│── pandas_df.py
│── embeddings_dataframe.pkl
│── README.md
```

---

## 🚧 Future Improvements

- FAISS vector database
- Streamlit web interface
- Chat history
- PDF support
- Citation with timestamps

---

## ⭐ If you found this project useful, consider giving it a star!
