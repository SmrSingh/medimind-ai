from pydantic import BaseModel
from typing import List


class Source(BaseModel):
    document: str
    page: int
    source: str


class Parameter(BaseModel):
    parameter: str
    value: float
    unit: str
    reference_range: str
    status: str
    ai_explanation: str | None = None
    sources: List[Source] = []


class ReportResponse(BaseModel):
    report_type: str
    overall_summary: str
    parameters: List[Parameter]