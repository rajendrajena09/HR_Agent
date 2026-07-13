# HR Agentic AI Assistant

An AI-powered HR Assistant built using LangChain, LangGraph, Groq, ChromaDB, and Streamlit.

## Features

- RAG-based HR Policy Question Answering
- Leave Balance Tool
- Employee Information Tool
- Intelligent Tool Routing
- Streamlit UI

## Tech Stack

- Python
- LangChain
- LangGraph
- Groq (Llama 3.3 70B)
- ChromaDB
- HuggingFace Embeddings
- Streamlit

## Project Structure

```
data/
rag/
tools/
app.py
agent.py
config.py
```

## Run

```
uv sync
uv run streamlit run app.py
```
