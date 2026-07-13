from rag.vectordb import get_vector_db
from config import TOP_K_RESULTS



def get_retriever():
    """
    Create and return the document retriever.
    """

    vector_db = get_vector_db()

    retriever = vector_db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": TOP_K_RESULTS}
    )

    return retriever