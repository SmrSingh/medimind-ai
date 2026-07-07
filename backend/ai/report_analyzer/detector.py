from backend.ai.report_analyzer.report_types import ReportType


class MedicalReportDetector:

    def detect(self, text: str) -> ReportType:

        text = text.upper()

        # CBC
        if (
            "COMPLETE BLOOD COUNT" in text
            or "CBC" in text
            or "HAEMATOLOGY" in text
        ):
            return ReportType.CBC

        # Liver Function Test
        if (
            "LIVER FUNCTION TEST" in text
            or "LFT" in text
            or "SGOT" in text
            or "SGPT" in text
            or "ALT" in text
            or "AST" in text
        ):
            return ReportType.LFT

        # Kidney Function Test
        if (
            "KIDNEY FUNCTION TEST" in text
            or "KFT" in text
            or "CREATININE" in text
            or "UREA" in text
            or "EGFR" in text
        ):
            return ReportType.KFT

        # Lipid Profile
        if (
            "LIPID PROFILE" in text
            or "CHOLESTEROL" in text
            or "HDL" in text
            or "LDL" in text
            or "TRIGLYCERIDES" in text
        ):
            return ReportType.LIPID

        # Diabetes
        if (
            "HBA1C" in text
            or "GLUCOSE" in text
            or "FASTING BLOOD SUGAR" in text
            or "POST PRANDIAL" in text
        ):
            return ReportType.DIABETES

        # Thyroid
        if (
            "THYROID" in text
            or "TSH" in text
            or "T3" in text
            or "T4" in text
        ):
            return ReportType.THYROID

        # Vitamin
        if (
            "VITAMIN B12" in text
            or "VITAMIN D" in text
        ):
            return ReportType.VITAMIN

        return ReportType.UNKNOWN