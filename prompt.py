from langchain_core.prompts import ChatPromptTemplate

def get_prompt():
    template = """
    You are a concise assistant who answers questions strictly based on the provided context.
    Use only the information from the context to answer the question.
    If the answer is not clearly stated in the context, say so honestly.
    Question: {input}
    Context: {context}
    Answer:
    """
    return ChatPromptTemplate.from_template(template)