Restaurant Review RAG Assistant

A simple learning project built to understand how Retrieval-Augmented Generation (RAG) works end-to-end. The agent reviews restaurants by comparing their star ratings against the actual written feedback, and gives an honest suggestion on whether the rating can be trusted.


Project Structure

restaurant-review-rag/

├── data/     # raw restaurant review data

├── vectorstore/          # persisted vector store

├── main.py              # entry point / CLI

├── requirements.txt

└── README.md

Prerequisites

Python 3.10+
Ollama installed locally

Pull the models

bash
ollama pull llama3.2

ollama pull mxbai-embed-large
