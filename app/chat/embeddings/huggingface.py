from langchain.embeddings import HuggingFaceEmbeddings

embeddings_model_name = "sentence-transformers/all-MiniLM-L6-v2"

embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)