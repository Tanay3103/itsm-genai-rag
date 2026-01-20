from langchain_qdrant import QdrantVectorStore

from config.config import KNOWLEDGE_COLLECTION
from embeddings.embeddings import get_embeddings
from utils.qdrant_client_utils import get_qdrant_client

embeddings = get_embeddings()


def search_knowledge(query):
    try:
        store = QdrantVectorStore(
            client=get_qdrant_client(),
            collection_name=KNOWLEDGE_COLLECTION,
            embedding=get_embeddings(),
        )
        return store.similarity_search_with_score(query, k=3)
    except Exception:
        return []
