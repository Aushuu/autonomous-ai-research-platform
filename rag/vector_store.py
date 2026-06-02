from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


class VectorStore:

    def __init__(self):

        self.embedding_model = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        # Load existing Chroma DB
        self.db = Chroma(
            persist_directory="chroma_db",
            embedding_function=self.embedding_model
        )

    def build_vector_db(self, documents):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        chunks = splitter.create_documents(
            documents
        )

        self.db = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory="chroma_db"
        )

        return self.db

    def search(self, query, k=4):

        return self.db.similarity_search(
            query,
            k=k
        )