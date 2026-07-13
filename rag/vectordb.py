import os

from langchain_chroma import Chroma

from rag.loader import load_documents
from rag.splitter import split_documents
from rag.embeddings import get_embedding_model

from config import CHROMA_DB_PATH


def get_vector_db():
    """
    Load an existing Chroma database.
    If it doesn't exist, create it first.
    """

    embedding_model = get_embedding_model()

    # Database already exists
    if os.path.exists(CHROMA_DB_PATH) and os.listdir(CHROMA_DB_PATH):
        print("Loading existing ChromaDB...")

        return Chroma(
            persist_directory=CHROMA_DB_PATH,
            embedding_function=embedding_model
        )

    ##### else creating new one
    print("Creating ChromaDB...")

    documents = load_documents("data/hr_policies")

    chunks = split_documents(documents)

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_DB_PATH
    )

    return vector_db
