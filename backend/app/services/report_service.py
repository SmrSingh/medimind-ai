from ai.report_analyzer.parser import MedicalReportParser
from ai.report_analyzer.extractor import MedicalParameterExtractor
from ai.report_analyzer.analyzer import MedicalReportAnalyzer
from ai.report_analyzer.detector import MedicalReportDetector

class ReportService:

    def __init__(self):

        self.detector = MedicalReportDetector()
        self.extractor = MedicalParameterExtractor()
        self.analyzer = MedicalReportAnalyzer()
    def analyze(self, pdf_path: str):

        parser = MedicalReportParser(pdf_path)

        text = parser.extract_text()
        report_type = self.detector.detect(text)

        print(f"Detected Report Type: {report_type}")

        parameters = self.extractor.extract(text)

        parameters = self.analyzer.determine_status(parameters)

        parameters = self.analyzer.explain_abnormal_parameters(parameters)

        summary = self.analyzer.generate_summary(parameters)

        return {
            "report_type": report_type.value,
            "overall_summary": summary,
            "parameters": parameters
        }