from langchain_core.runnables import RunnableMap
from langchain_core.output_parsers import StrOutputParser

def build_rag_chain(retriever, prompt, llm):
    return (
        RunnableMap({
            "context": retriever,
            "input": lambda x: x  # Simple passthrough
        })
        | prompt
        | llm
        | StrOutputParser()
    )