from rag.vector_store import VectorStore

docs = [
    """
    Artificial Intelligence improves
    healthcare diagnostics and
    patient outcomes.
    """
]

db = VectorStore().build_vector_db(
    docs
)

print("RAG Working")