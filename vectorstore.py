from langchain_community.vectorstores import Chroma

def build_vectorstore(split_docs, embeddings, persist_dir, collection_name="rag_collection"):
    return Chroma.from_documents(
        documents=split_docs,
        embedding=embeddings,
        persist_directory=persist_dir,
        collection_name=collection_name
    )