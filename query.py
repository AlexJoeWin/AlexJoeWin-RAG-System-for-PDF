def ask_question(rag_chain):
    query = input("\nWhat would you like to ask? ").strip()
    if not query:
        query = "Who is named in the text? Include no meta data!"
        print(f"\nProviding a test query such as:\n{query}")
    response = rag_chain.invoke(query)
    print(f"\nAnswer:\n{response}\n")