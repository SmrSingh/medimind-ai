from fastapi import APIRouter
from pydantic import BaseModel

from backend.ai.rag import MedicalRAG

router = APIRouter()

rag = MedicalRAG()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    response = rag.ask(request.question)

    return response