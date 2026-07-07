import re
from backend.ai.rag import MedicalRAG


from backend.ai.llm import MedicalLLM

class MedicalReportAnalyzer:

    def __init__(self):

        self.rag = MedicalRAG()
        self.llm = MedicalLLM()

    def extract_parameters(self, text):

        pattern = re.compile(
            r"([A-Za-z ()]+)\s+([\d.]+)\s+([A-Za-z/%µ]+)\s+([\d.]+\s*[-–]\s*[\d.]+)"
        )

        parameters = []

        matches = pattern.findall(text)

        for match in matches:

            parameters.append(
                {
                    "parameter": match[0].strip(),
                    "value": float(match[1]),
                    "unit": match[2],
                    "reference_range": match[3]
                }
            )

        return parameters

    def determine_status(self, parameters):

        for parameter in parameters:
            if parameter["reference_range"] is None:
                parameter["status"] = "Unknown"
                continue

            reference = parameter["reference_range"].replace("–", "-")

            low, high = reference.split("-")

            low = float(low.strip())
            high = float(high.strip())

            value = parameter["value"]

            if value < low:
                parameter["status"] = "Low"

            elif value > high:
                parameter["status"] = "High"

            else:
                parameter["status"] = "Normal"

        return parameters

    def explain_abnormal_parameters(self, parameters):

        for parameter in parameters:

            if parameter["status"] == "Normal":
                continue

            question = (
                f"What is the clinical significance of "
                f"{parameter['status']} {parameter['parameter']}?"
            )

            response = self.rag.ask(question)

            parameter["ai_explanation"] = response["answer"]
            parameter["sources"] = response["sources"]

        return parameters
    def generate_summary(self, parameters):

        findings = []

        for parameter in parameters:

            findings.append(
                f"{parameter['parameter']}: "
                f"{parameter['value']} {parameter['unit']} "
                f"({parameter['status']})"
            )

        prompt = f"""
You are an experienced physician.

Below are the laboratory findings.

{chr(10).join(findings)}

Generate:

1. A short overall summary.
2. Mention any abnormal parameters.
3. Mention possible clinical patterns without making a diagnosis.
4. Suggest discussing abnormal findings with a healthcare professional.
5. State that this is educational information and not medical advice.

Keep the response concise and easy to understand.
"""

        return self.llm.generate_without_rag(prompt)

from backend.ai.report_analyzer.parser import MedicalReportParser

if __name__ == "__main__":

    parser = MedicalReportParser(
        "datasets/reports/Sample_CBC_Report.pdf"
    )

    text = parser.extract_text()

    analyzer = MedicalReportAnalyzer()

    parameters = analyzer.extract_parameters(text)

    parameters = analyzer.determine_status(parameters)

    parameters = analyzer.explain_abnormal_parameters(parameters)
    summary = analyzer.generate_summary(parameters)

    print()

    for parameter in parameters:

        print("=" * 80)

        print(parameter["parameter"])
        print(f"Value : {parameter['value']} {parameter['unit']}")
        print(f"Status: {parameter['status']}")

        if parameter["status"] != "Normal":

            print("\nAI Explanation\n")

            print(parameter["ai_explanation"])

            print("\nSources")

            for source in parameter["sources"]:
                print(
                    f"- {source['source']} | "
                    f"{source['document']} | "
                    f"Page {source['page']}"
                )
            print("=" * 80)
            print("OVERALL SUMMARY")
            print("=" * 80)

            print(summary)

        print()