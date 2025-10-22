import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_TOKEN = os.getenv("OPENAI_TOKEN")
PDF_DIR = "data"
CHROMA_DIR = "chroma_db"
CHUNK_SIZE = 512
CHUNK_OVERLAP = 50