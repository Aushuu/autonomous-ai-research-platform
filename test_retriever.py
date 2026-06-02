from rag.retriever import Retriever

retriever = Retriever()

context = retriever.retrieve(
    "Artificial Intelligence in Healthcare"
)

print(context[:1000])