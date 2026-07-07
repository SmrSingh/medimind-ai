from chromadb import PersistentClient

from ai.build_knowledge_base import KnowledgeBaseBuilder


def ensure_knowledge_base():

    client = PersistentClient(path="database")

    try:

        client.get_collection("medical_knowledge")

        print("Knowledge Base already exists.")

    except Exception:

        print("Knowledge Base not found.")
        print("Building Knowledge Base...")

        builder = KnowledgeBaseBuilder()

        builder.build("datasets/knowledge_base")

        print("Knowledge Base created successfully.")