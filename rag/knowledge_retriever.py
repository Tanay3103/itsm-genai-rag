from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings
from utils.qdrant_client import get_qdrant_client
from config import KNOWLEDGE_COLLECTION

def search_knowledge(query):
    store = Qdrant(
        client=get_qdrant_client(),
        collection_name=KNOWLEDGE_COLLECTION,
        embedding=OpenAIEmbeddings()
    )
    return store.similarity_search_with_score(query, k=3)
