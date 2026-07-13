from langchain.tools import tool

from rag.rag_chain import ask_hr_policy


@tool
def get_hr_policy(question: str):
    """
    Answer questions related to HR policies such as:

    - Leave Policy
    - Holiday Policy
    - Carry Forward
    - Public Holidays
    - Leave Encashment
    - Maternity Leave
    """

    return ask_hr_policy(question)