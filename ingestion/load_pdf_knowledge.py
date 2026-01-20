from langchain_community.document_loaders import PyPDFLoader
from langchain_qdrant import QdrantVectorStore

from config.config import KNOWLEDGE_COLLECTION, QDRANT_URL
from embeddings.embeddings import get_embeddings

embeddings = get_embeddings()


def load_knowledge_pdf():
    docs = PyPDFLoader("data/itsm_context_knowledge.pdf").load()

    QdrantVectorStore.from_documents(
        docs, embedding=embeddings, url=QDRANT_URL, collection_name=KNOWLEDGE_COLLECTION
    )
