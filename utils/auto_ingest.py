from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings
from utils.qdrant_client import get_qdrant_client
from config import TICKET_COLLECTION

def ingest_resolved_ticket(text, metadata):
    Qdrant.from_texts(
        [text],
        OpenAIEmbeddings(),
        metadatas=[metadata],
        client=get_qdrant_client(),
        collection_name=TICKET_COLLECTION
    )
