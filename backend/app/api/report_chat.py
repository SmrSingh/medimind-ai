from fastapi import APIRouter
from pydantic import BaseModel

from backend.app.services.service_container import report_service

router = APIRouter()


class ReportChatRequest(BaseModel):
    question: str


@router.post("/report-chat")
def report_chat(request: ReportChatRequest):

    return report_service.chat(request.question)