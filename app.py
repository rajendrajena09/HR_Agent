import streamlit as st

from agent import agent
from rag.rag_chain import ask_hr_policy

st.set_page_config(
    page_title="HR Assistant",
    page_icon="🤖"
)

st.title("🤖 HR Assistant")

question = st.text_input(
    "Ask your HR question"
)

if st.button("Submit"):

    if question:

        policy_keywords = [
            "policy",
            "leave policy",
            "holiday",
            "carry forward",
            "encashment",
            "insurance",
            "maternity",
            "paternity",
            "public holiday"
        ]

        with st.spinner("Thinking..."):

            if any(
                keyword in question.lower()
                for keyword in policy_keywords
            ):

                answer = ask_hr_policy(question)

            else:

                response = agent.invoke(
                    {
                        "messages": [
                            {
                                "role": "user",
                                "content": question
                            }
                        ]
                    }
                )

                answer = response["messages"][-1].content

        st.success(answer)