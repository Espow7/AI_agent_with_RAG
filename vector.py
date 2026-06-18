from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("realistic_restaurant_reviews.csv")
embeddings = OllamaEmbeddings(model='mxbai-embed-large')

df_location = './chrome_langchain_db'
add_document = not os.path.exists(df_location)

if add_document:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content=row['Title']+''+row['Review'],
            metadeta={'rating': row["Rating"],"date":row['Date']},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=df_location,
    embedding_function=embeddings

)

if add_document:
    vector_store.add_documents(documents=documents, ids=ids)

retriver = vector_store.as_retriever(
    search_kwargs={"k": 5}
)
