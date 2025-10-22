# 🧠 Modular RAG pipeline for PDF based retrieval

This project implements a reproducible Retrieval-Augmented Generation (RAG) pipeline using LangChain, PyPDFLoader, OpenAI embeddings, GPT-4, and Chroma vectorstore. It supports multilingual queries, modular architecture, and context-aware prompting for (hopeful) minimal hallucinations.

---

## 📂 Project Structure

```
rag_project/
├── data/			# Drop zone for PDFs
├── chroma_db/ 			# Persistent vectorstore
├── config.py 			# API key and chunking variables
├── loaders.py 			# PDF loading logic
├── splitter.py 		# Chunking strategy
├── embeddings.py 		# Embedding setup
├── vectorstore.py 		# Chroma setup
├── retriever.py 		# Retriever configuration
├── prompt.py 			# Prompt templates
├── rag_chain.py 		# Chain assembly
├── query.py 			# Interactive query logic
└── main.py 			# Entry point
```


## 🚀 Quickstart

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt

2.  **Add your OpenAI key**  
Create a `.env` file:
    
    ```env
    OPENAI_TOKEN=your-api-key-here
    ```
    
3.  **Drop PDFs into `/data`**  
This folder is automatically created if missing.


4.  **Run the pipeline**
    
    ```bash
    python main.py
    ```
    

----------

## 🧩 Features

-   ✅ Token-based chunking with overlap
-   ✅ MMR retrieval (provided best results among different setups)
-   ✅ Context-bound prompting with fallback logic
-   ✅ Modular components for easy testing and extension

----------

## 🛠️ Configuration

Edit `config.py` to adjust:

-   API keys
-   Chunk size / overlap  
-   Directory for PDF storage
-   Directory for a Chroma database

----------

## 📚 Prompt Template

```text
You are a concise assistant who answers questions strictly based on the provided context.
Use only the information from the context to answer the question.
If the answer is not clearly stated in the context, say so honestly.
Question: {input}
Context: {context}
Answer:
```

----------

## 🧪 Testing

To run a default query:

```bash
python main.py
```

If no input is provided, a test query is created:

```text
Who is named in the text? Include no meta data!
```

----------

## 📖 License

MIT License. See `LICENSE.md`