import os
import pinecone
from langchain.vectorstores import Pinecone
#from app.chat.embeddings.openai import embeddings
from app.chat.embeddings.huggingface import embeddings

pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV_NAME")
)

vector_store = Pinecone.from_existing_index(
    os.getenv("PINECONE_INDEX_NAME"), embeddings
)
