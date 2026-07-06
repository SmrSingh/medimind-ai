

from ai.report_analyzer.parser import MedicalReportParser
from ai.report_analyzer.extractor import MedicalParameterExtractor
from ai.report_analyzer.analyzer import MedicalReportAnalyzer
from ai.report_analyzer.detector import MedicalReportDetector
from ai.rag import MedicalRAG
class ReportService:

    def __init__(self):
        self.current_report_text = ""
        self.current_report_type = None
        self.rag = MedicalRAG()

        self.detector = MedicalReportDetector()
        self.extractor = MedicalParameterExtractor()
        self.analyzer = MedicalReportAnalyzer()
    def analyze(self, pdf_path: str):

        parser = MedicalReportParser(pdf_path)

        text = parser.extract_text()
        self.current_report_text = text
        report_type = self.detector.detect(text)
        self.current_report_type = report_type

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
    def chat(self, question: str):

        if not self.current_report_text:
            return {
            "answer": "Please upload a medical report first.",
            "sources": []
        }

        prompt = f"""
        You are MediMind AI.

        The following is the patient's uploaded medical report.

        =========================
        {self.current_report_text}
        =========================

        Patient Question:
        {question}

        Instructions:

        - First use the uploaded report to answer the question.
        - If the uploaded report is insufficient, use the medical knowledge base.
        - Clearly mention if the answer comes from general medical knowledge.
        - Do not hallucinate.
        - Do not diagnose.
        - Keep the answer simple and concise.
        """
        response = self.rag.ask(prompt)

        return {
        "answer": response["answer"],
        "sources": response["sources"]
        }