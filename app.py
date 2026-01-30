import os
from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

# Example usage
if __name__ == "__main__":
    # Step 1: Load all documents from your data folder
    docs = load_all_documents("data")

    # Step 2: Initialize the Faiss vector store
    store = FaissVectorStore("faiss_store")
    # Step 3: Build the index if it doesn't exist yet
    faiss_index_path = os.path.join("faiss_store", "faiss.index")
    meta_path = os.path.join("faiss_store", "metadata.pkl")
    if not (os.path.exists(faiss_index_path) and os.path.exists(meta_path)):
        print("[INFO] No existing index found. Building new Faiss index...")
        store.build_from_documents(docs)
    else:
        print("[INFO] Existing index found. Loading Faiss index...")
        store.load()
    # Step 4: Run a RAG search query
    rag_search = RAGSearch()
    query = "What is rag?"
    summary = rag_search.search_and_summarize(query, top_k=3)

    print("Summary:", summary)