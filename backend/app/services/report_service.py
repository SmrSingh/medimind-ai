from ai.report_analyzer.parser import MedicalReportParser
from ai.report_analyzer.analyzer import MedicalReportAnalyzer


class ReportService:

    def __init__(self):
        self.analyzer = MedicalReportAnalyzer()

    def analyze(self, pdf_path: str):

        parser = MedicalReportParser(pdf_path)

        text = parser.extract_text()

        parameters = self.analyzer.extract_parameters(text)

        parameters = self.analyzer.determine_status(parameters)

        parameters = self.analyzer.explain_abnormal_parameters(parameters)

        summary = self.analyzer.generate_summary(parameters)

        return {
            "report_type": "CBC",
            "overall_summary": summary,
            "parameters": parameters
        }