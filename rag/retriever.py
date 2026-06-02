from rag.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.vector_store = VectorStore()

    def retrieve(self, query):

        docs = self.vector_store.search(query)

        context = ""

        for doc in docs:

            context += doc.page_content + "\n\n"

        return context