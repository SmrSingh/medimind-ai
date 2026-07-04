import fitz
from pathlib import Path


class MedicalReportParser:

    def __init__(self, pdf_path: str):

        self.pdf_path = Path(pdf_path)

    def extract_text(self):

        document = fitz.open(self.pdf_path)

        full_text = []

        for page in document:

            full_text.append(page.get_text())

        document.close()

        return "\n".join(full_text)


if __name__ == "__main__":

    parser = MedicalReportParser(
        "datasets/reports/Sample_CBC_Report.pdf"
    )

    text = parser.extract_text()

    print("=" * 80)

    print(text)