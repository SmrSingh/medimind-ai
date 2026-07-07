from pathlib import Path

from backend.ai.knowledge_base.ingest import PDFIngestor
from backend.ai.knowledge_base.chunker import MedicalChunker
from backend.ai.vector_store.store import VectorStore


class KnowledgeBaseBuilder:

    def __init__(self):

        self.chunker = MedicalChunker()
        self.vector_store = VectorStore()

    def build(self, folder):

        folder = Path(folder)

        pdf_files = list(folder.rglob("*.pdf"))

        print(f"\nFound {len(pdf_files)} PDF(s).\n")

        all_chunks = []

        for pdf in pdf_files:

            print(f"Processing: {pdf.name}")

            ingestor = PDFIngestor(str(pdf))

            pages = ingestor.extract()

            chunks = self.chunker.chunk_pages(pages)

            all_chunks.extend(chunks)

        print(f"\nTotal Chunks : {len(all_chunks)}")

        self.vector_store.add_chunks(all_chunks)

        print("\nKnowledge Base Updated Successfully!")


if __name__ == "__main__":

    builder = KnowledgeBaseBuilder()

    builder.build("datasets/knowledge_base")