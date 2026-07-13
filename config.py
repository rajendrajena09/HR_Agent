from dotenv import load_dotenv
import os

load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")


MODEL_NAME = "llama-3.3-70b-versatile"


CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


CHROMA_DB_PATH = "./chroma_db"


EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

TOP_K_RESULTS = 3