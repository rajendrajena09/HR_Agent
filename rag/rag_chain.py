from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from config import GROQ_API_KEY

from rag.retriever import get_retriever


model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)


retriever = get_retriever()

prompt = ChatPromptTemplate.from_template(
"""
You are an HR Assistant.

Answer the user's question ONLY using the provided context.

If the answer is not present in the context,
reply:

"I couldn't find that information in the HR policy documents."

Context:
{context}

Question:
{question}

Answer:
"""
)


def ask_hr_policy(question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    chain = prompt | model

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response.content