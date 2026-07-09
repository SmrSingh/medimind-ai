# 🩺 MediMind AI
### Intelligent AI-Powered Medical Report Analysis & Clinical Decision Support System

MediMind AI is an end-to-end AI healthcare application that analyzes medical laboratory reports, extracts structured clinical information, performs evidence-based interpretation using Large Language Models (LLMs), and enables users to interact with their reports through Retrieval-Augmented Generation (RAG).

The project demonstrates modern AI engineering practices including FastAPI, React, ChromaDB, Retrieval-Augmented Generation (RAG), OCR-based PDF parsing, semantic search, and LLM integration.

> **Disclaimer:** MediMind AI is designed for educational purposes and clinical decision support. It is **not** a replacement for professional medical advice, diagnosis, or treatment.

---
# Demo Video
  https://www.loom.com/share/2487764fd9bf4fd89bedeafd15807d62
  
#  Features

##  Medical Report Analysis

- Upload laboratory reports in PDF format
- Automatic report type detection
- CBC (Complete Blood Count) analysis
- Liver Function Test (LFT) analysis
- Structured parameter extraction
- Automatic reference range comparison
- High / Low / Normal classification
- AI-generated clinical summary

---

##  AI Medical Report Chat

Users can ask natural language questions such as:

- Are my liver enzymes normal?
- Which values are abnormal?
- Explain my CBC report.
- What does high bilirubin indicate?

The AI answers using only information extracted from the uploaded report.

---

##  Retrieval-Augmented Generation (RAG)

The application retrieves evidence from a curated medical knowledge base before generating responses.

Knowledge sources include:

- Clinical Guidelines
- Medical Reference Documents
- Laboratory Interpretation Resources

Responses are grounded in retrieved evidence instead of relying only on the language model.

---

##  AI Technologies Used

- Google Gemini API
- Retrieval-Augmented Generation (RAG)
- ChromaDB Vector Database
- Sentence Transformers
- Semantic Search
- PDF Parsing
- OCR Pipeline
- Embedding-based Retrieval

---

#  System Architecture

```
                    Medical PDF
                         │
                         ▼
                PDF Processing Engine
                         │
                         ▼
              Parameter Extraction Engine
                         │
                         ▼
             Clinical Report Classification
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
   AI Report Analysis            Structured Parameters
          │                             │
          ▼                             ▼
      Gemini LLM                  Frontend Dashboard
          │
          ▼
      AI Summary
          │
          ▼
      Report Chat (RAG)
          │
          ▼
     ChromaDB Knowledge Base
```

---

#  Tech Stack

## Backend

- Python
- FastAPI
- Pydantic
- Uvicorn
- ChromaDB
- Google Gemini API

---

## Frontend

- React
- Vite
- Axios
- CSS

---

## AI / ML

- Retrieval-Augmented Generation (RAG)
- Sentence Transformers
- ChromaDB
- Semantic Search
- PDF Parsing
- Prompt Engineering

---

#  Project Structure

```
MediMind AI
│
├── backend
│   ├── ai
│   │   ├── knowledge_base
│   │   ├── report_analyzer
│   │   ├── vector_store
│   │   ├── rag.py
│   │   ├── llm.py
│   │   └── startup.py
│   │
│   ├── app
│   │   ├── api
│   │   ├── services
│   │   └── main.py
│   │
│   ├── datasets
│   ├── database
│   ├── uploads
│   └── requirements.txt
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
└── README.md
```

---

#  Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/MediMind-AI.git

cd MediMind-AI
```

---

## Backend Setup

```bash
cd backend

python -m venv .venv

source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create

```
backend/.env
```

```
GEMINI_API_KEY=YOUR_API_KEY
```

Start backend

```bash
python -m uvicorn app.main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend

```
http://localhost:5173
```

---

# API Endpoints

## Report Analysis

```
POST /api/report-analysis
```

Uploads a laboratory report and returns:

- Report Type
- Parameters
- Reference Ranges
- AI Summary

---

## Report Chat

```
POST /api/report-chat
```

Ask questions about the uploaded report.

---

## General Medical Chat

```
POST /api/chat
```

Evidence-based medical Q&A using RAG.

---

#  RAG Pipeline

```
Clinical Documents
        │
        ▼
PDF Ingestion
        │
        ▼
Text Chunking
        │
        ▼
Sentence Embeddings
        │
        ▼
ChromaDB Vector Store
        │
        ▼
Semantic Search
        │
        ▼
Relevant Context
        │
        ▼
Gemini LLM
        │
        ▼
Grounded Medical Response
```

---

#  Key AI Engineering Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Vector Databases
- Embedding Models
- Semantic Search
- Clinical Document Retrieval
- PDF Parsing
- Medical NLP
- FastAPI REST APIs
- React Integration
- AI-powered Decision Support

---

#  Future Improvements

- Support additional laboratory reports
- Drug interaction analysis
- Explainable AI with citations
- Multi-report comparison
- Patient history tracking
- Doctor dashboard
- Authentication
- Docker deployment
- Cloud deployment
- CI/CD pipeline

---

#  License

This project is intended for educational and research purposes.

---

#  Author

**Smriti**



Python • FastAPI • React • RAG • LLM • NLP • Generative AI • Healthcare AI
