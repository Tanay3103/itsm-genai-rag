from config.config import KNOWLEDGE_COLLECTION, TICKET_COLLECTION
from ingestion.load_csv_tickets import load_ticket_history
from ingestion.load_pdf_knowledge import load_knowledge_pdf
from utils.qdrant_client_utils import get_qdrant_client


def collection_exists(client, name: str) -> bool:
    try:
        client.get_collection(name)
        return True
    except Exception:
        return False


def bootstrap_qdrant():
    client = get_qdrant_client()

    if not collection_exists(client, TICKET_COLLECTION):
        print("🔄 Creating ticket collection")
        load_ticket_history()
    else:
        print("✅ Ticket collection exists")

    if not collection_exists(client, KNOWLEDGE_COLLECTION):
        print("🔄 Creating knowledge collection")
        load_knowledge_pdf()
    else:
        print("✅ Knowledge collection exists")
