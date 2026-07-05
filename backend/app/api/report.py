from pathlib import Path
import shutil
import uuid

from fastapi import APIRouter, UploadFile, File, HTTPException

from backend.app.services.report_service import ReportService

router = APIRouter()

service = ReportService()


@router.post("/report-analysis")
async def analyze_report(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    upload_dir = Path("uploads")
    upload_dir.mkdir(exist_ok=True)

    pdf_path = upload_dir / f"{uuid.uuid4()}.pdf"

    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = service.analyze(str(pdf_path))

    pdf_path.unlink(missing_ok=True)

    return result