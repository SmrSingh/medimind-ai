from langchain_text_splitters import RecursiveCharacterTextSplitter

class MedicalChunker:

    def __init__(
        self,
        chunk_size=800,
        chunk_overlap=150
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def chunk_pages(self, pages):

        chunks = []

        for page in pages:

            texts = self.splitter.split_text(page["text"])

            for i, chunk in enumerate(texts):

                chunks.append({
                    "document": page["document"],
                    "page": page["page"],
                    "chunk_id": i,
                    "text": chunk,
                    "source": page["source"],
                    "category": page["category"],
                })

        return chunks