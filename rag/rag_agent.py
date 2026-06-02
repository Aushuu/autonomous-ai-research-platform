from rag.retriever import Retriever


class RAGAgent:

    def __init__(self):

        self.retriever = Retriever()

    def get_context(self, topic):

        return self.retriever.retrieve(topic)