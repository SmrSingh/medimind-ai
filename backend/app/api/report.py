from fastapi import APIRouter
from backend.app.services.report_service import ReportService

router = APIRouter()

service = ReportService()


@router.get("/sample-report")
def sample_report():

    result = service.analyze(
        "datasets/reports/Sample_CBC_Report.pdf"
    )

    return result