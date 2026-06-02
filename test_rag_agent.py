from rag.rag_agent import RAGAgent

rag = RAGAgent()

context = rag.get_context(
    "Artificial Intelligence in Healthcare"
)

print(context[:1000])