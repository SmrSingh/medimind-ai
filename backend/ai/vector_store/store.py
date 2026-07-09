from chromadb import PersistentClient
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction


class VectorStore:

    def __init__(self):

        self.client = PersistentClient(path="database")

        embedding_function = SentenceTransformerEmbeddingFunction(
            model_name="BAAI/bge-small-en-v1.5"
        )

        self.collection = self.client.get_or_create_collection(
            name="medical_knowledge",
            embedding_function=embedding_function
        )

    def add_chunks(self, chunks):

        documents = []
        metadatas = []
        ids = []

        for index, chunk in enumerate(chunks):

            documents.append(chunk["text"])

            metadatas.append(
                {
                    "document": chunk["document"],

                    "organization": chunk["organization"],

                    "specialty": chunk["specialty"],

                    "document_type": chunk["document_type"],

                    "page": chunk["page"]

                }
            )

            document_name = chunk["document"].replace(".pdf", "")

            ids.append(f"{document_name}_{chunk['page']}_{chunk['chunk_id']}")

        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

        print(f"Stored {len(chunks)} chunks successfully.")