from langchain_qdrant import QdrantVectorStore

from config.config import QDRANT_URL, TICKET_COLLECTION
from embeddings.embeddings import get_embeddings


def ingest_new_ticket(ticket):
    text = f"""
Issue: {ticket['description']}
Resolution: {ticket.get('resolution', 'Pending')}
"""

    QdrantVectorStore.from_texts(
        texts=[text],
        embedding=get_embeddings(),
        metadatas=[ticket],
        url=QDRANT_URL,
        collection_name=TICKET_COLLECTION,
    )
