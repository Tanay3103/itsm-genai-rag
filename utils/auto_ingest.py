from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Qdrant
from utils.qdrant_client import get_qdrant_client
from config import TICKET_COLLECTION

def ingest_ticket(text, metadata):
    Qdrant.from_texts(
        texts=[text],
        embedding=OpenAIEmbeddings(),
        metadatas=[metadata],
        client=get_qdrant_client(),
        collection_name=TICKET_COLLECTION
    )
