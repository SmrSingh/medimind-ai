import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


class MedicalLLM:

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = "gemini-2.5-flash-lite"

    def generate(self, question: str, context: str):

        prompt = f"""
You are MediMind AI.

You are an evidence-based medical assistant.

Use ONLY the medical evidence below.

If the answer cannot be found in the evidence, clearly say:

"I could not find this information in the provided medical documents."

Medical Evidence
----------------
{context}

Question
--------
{question}

Instructions

- Do not hallucinate.
- Do not add medical advice.
- Answer in simple English.
- Mention important values if present.
"""

        import time

        for attempt in range(3):
            try:
                response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
                    )
                return response.text

            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(2)

        return "The language model is temporarily unavailable. Please try again."
    def generate_without_rag(self, prompt: str):

        import time

        for attempt in range(3):
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt
                )

                return response.text

            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(2)

        return "The language model is temporarily unavailable. Please try again."

if __name__ == "__main__":

    llm = MedicalLLM()

    answer = llm.generate(
        "What is diabetes?",
        "Diabetes is a metabolic disorder characterized by hyperglycemia."
    )

    print(answer)