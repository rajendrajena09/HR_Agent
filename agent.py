from langchain.agents import create_agent
from langchain_groq import ChatGroq

from tools.leave_tool import get_leave_balance
from tools.employee_tool import get_employee_details


from config import (
    GROQ_API_KEY,
    MODEL_NAME
)

model = ChatGroq(
    model=MODEL_NAME,
    api_key=GROQ_API_KEY
)

agent = create_agent(
    model=model,
    tools=[
        get_leave_balance,
        get_employee_details
    ],
    system_prompt="""
You are an intelligent HR Assistant.

Use the available tools whenever required.

- Use the Leave Tool for leave balance.
- Use the Employee Tool for employee information.
- Use the HR Policy Tool for questions about company policies.

Never make up answers.

Do not make up information.
Always use the appropriate tool.
"""
)