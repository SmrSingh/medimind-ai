from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self):
        print("Loading embedding model...")

        self.model = SentenceTransformer(
            "BAAI/bge-base-en-v1.5"
        )

        print("Model loaded successfully!")

    def encode(self, texts):

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
            show_progress_bar=True
        )

        return embeddings


if __name__ == "__main__":

    model = EmbeddingModel()

    sentences = [
        "Diabetes is diagnosed using HbA1c.",
        "Hyperglycemia means high blood sugar.",
        "Hypertension is high blood pressure."
    ]

    embeddings = model.encode(sentences)

    print()

    print(f"Number of embeddings : {len(embeddings)}")
    print(f"Embedding dimension  : {len(embeddings[0])}")
    