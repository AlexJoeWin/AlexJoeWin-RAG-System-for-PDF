import os
from langchain_community.document_loaders import PyPDFLoader

def load_pdf(filepath):
    pdf_files = [os.path.join(filepath, f) for f in os.listdir(filepath) if f.endswith(".pdf")]

    if not pdf_files:
        print(f"No PDFs found in {filepath}. Drop your files there and rerun the script.")

    all_docs = []
    for file_path in pdf_files:
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        all_docs.extend(docs)
    return all_docs