from langchain_openai import OpenAIEmbeddings
from config import OPENAI_TOKEN

def get_embeddings():
    return OpenAIEmbeddings(api_key=OPENAI_TOKEN)