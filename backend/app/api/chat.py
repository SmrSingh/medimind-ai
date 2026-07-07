from fastapi import APIRouter
from pydantic import BaseModel

from ai.rag import MedicalRAG

router = APIRouter()

# Lazy-loaded singleton
rag = None


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):
    global rag

    if rag is None:
        print("Loading Medical RAG...")
        rag = MedicalRAG()
        print("Medical RAG loaded.")

    response = rag.ask(request.question)

    return response