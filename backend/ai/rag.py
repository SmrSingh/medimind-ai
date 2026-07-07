from ai.vector_store.search import MedicalSearcher
from ai.llm import MedicalLLM


class MedicalRAG:

    def __init__(self):

        self.searcher = MedicalSearcher()
        self.llm = MedicalLLM()

    def ask(self, question):

        results = self.searcher.search(question, top_k=3)

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        context = "\n\n".join(documents)

        answer = self.llm.generate(
            question=question,
            context=context
        )

        return {
            "question": question,
            "answer": answer,
            "documents": documents,
            "sources": metadatas
        }


if __name__ == "__main__":

    rag = MedicalRAG()

    while True:

        question = input("\nAsk a medical question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        response = rag.ask(question)

        print("\n" + "=" * 80)
        print("ANSWER")
        print("=" * 80)

        print(response["answer"])

        print("\n" + "=" * 80)
        print("SOURCES")
        print("=" * 80)

        for i, source in enumerate(response["sources"], start=1):

            print(
                f"{i}. {source['source']} | "
                f"{source['document']} | "
                f"Page {source['page']}"
            )