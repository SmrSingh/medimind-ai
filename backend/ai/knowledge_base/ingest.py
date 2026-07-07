"""
ingest.py

Responsible for loading medical PDF documents
and extracting text with metadata.
"""

from pathlib import Path
import fitz

from ai.knowledge_base.chunker import MedicalChunker
from ai.vector_store.store import VectorStore


class PDFIngestor:
    """
    Reads PDF documents and extracts text page by page.
    Metadata is automatically inferred from the folder structure.
    """

    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)

    def get_metadata(self):
        """
        Example path:

        datasets/
            knowledge_base/
                clinical_guidelines/
                    diabetes/
                        ADA_Standards_of_Care_2026.pdf
        """

        return {
            "document": self.pdf_path.name,
            "organization": self.pdf_path.stem.split("_")[0],
            "specialty": self.pdf_path.parent.name,
            "document_type": self.pdf_path.parent.parent.name.replace("_", " ").title(),
        }

    def extract(self):

        metadata = self.get_metadata()

        document = fitz.open(self.pdf_path)

        pages = []

        for page_number, page in enumerate(document, start=1):

            text = page.get_text("text").strip()

            if not text:
                continue

            pages.append(
                {
                    **metadata,
                    "page": page_number,
                    "text": text,
                }
            )

        document.close()

        return pages


if __name__ == "__main__":

    pdf = PDFIngestor(
        "datasets/knowledge_base/clinical_guidelines/diabetes/ADA_Standards_of_Care_2026.pdf"
    )

    pages = pdf.extract()

    chunker = MedicalChunker()

    chunks = chunker.chunk_pages(pages)

    print("=" * 70)
    print(f"Pages  : {len(pages)}")
    print(f"Chunks : {len(chunks)}")
    print("=" * 70)

    print()
    print(pages[0])

    vector_store = VectorStore()

    vector_store.add_chunks(chunks)