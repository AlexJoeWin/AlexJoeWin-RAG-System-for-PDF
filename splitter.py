from langchain_text_splitters import TokenTextSplitter

def split_documents(docs, chunk_size, chunk_overlap):
    splitter = TokenTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)