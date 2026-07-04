from chromadb import PersistentClient
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction


class MedicalSearcher:

    def __init__(self):

        self.client = PersistentClient(path="database")

        embedding_function = SentenceTransformerEmbeddingFunction(
            model_name="BAAI/bge-base-en-v1.5"
        )

        self.collection = self.client.get_collection(
            name="medical_knowledge",
            embedding_function=embedding_function
        )

    def search(self, query, top_k=3):

        results = self.collection.query(
            query_texts=[query],
            n_results=top_k
        )

        return results


if __name__ == "__main__":

    searcher = MedicalSearcher()

    results = searcher.search(
        "What are the diagnostic criteria for diabetes?"
    )

    print("=" * 80)

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    for i, (doc, meta) in enumerate(zip(documents, metadatas), start=1):

        print("=" * 80)
        print(f"Result {i}")

        print(f"Document : {meta['document']}")
        print(f"Page     : {meta['page']}")
        print(f"Source   : {meta['source']}")
        print(f"Category : {meta['category']}")

        print("-" * 80)

        print(doc[:600])