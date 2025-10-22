def get_retriever(vectorstore):
    return vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 5,
            "fetch_k": 20,  # Number of candidates to consider
            "lambda_mult": 0.5  # 0 = more diverse, 1 = more relevant
        }
    )
