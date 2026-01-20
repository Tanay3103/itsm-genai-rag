import re

from langchain_qdrant import QdrantVectorStore

from config.config import TICKET_COLLECTION
from embeddings.embeddings import get_embeddings
from mock_itsm.jira_api import get_jira_ticket
from mock_itsm.servicenow_api import get_servicenow_ticket
from utils.qdrant_client_utils import get_qdrant_client


def extract_ticket_id(text: str):
    match = re.search(r"\b(INC|REQ|SR|TASK)-\d+\b", text.upper())
    return match.group(0) if match else None


def search_tickets(query):
    try:
        store = QdrantVectorStore(
            client=get_qdrant_client(),
            collection_name=TICKET_COLLECTION,
            embedding=get_embeddings(),
        )
        return store.similarity_search_with_score(query, k=3)
    except Exception:
        return []


def get_ticket_by_id(ticket_id: str) -> dict | None:
    """
    Fetch ticket details from ServiceNow, Jira, or history.
    """

    # 1️⃣ ServiceNow
    ticket = get_servicenow_ticket(ticket_id)
    if ticket:
        ticket["source"] = "ServiceNow"
        return ticket

    # 2️⃣ Jira
    ticket = get_jira_ticket(ticket_id)
    if ticket:
        ticket["source"] = "Jira"
        return ticket

    # 3️⃣ Vector DB fallback (best effort)
    hits = search_tickets(ticket_id)
    if hits:
        doc, _ = hits[0]
        meta = doc.metadata or {}
        meta.setdefault("id", ticket_id)
        meta.setdefault("status", "Closed")
        meta.setdefault("description", doc.page_content)
        meta["source"] = "History"
        return meta

    return None


def parse_ticket_content(text: str) -> dict:
    """
    Parses Issue / Details / Root Cause / Resolution from stored ticket text
    """
    result = {}

    for line in text.splitlines():
        line = line.strip()
        if line.lower().startswith("issue:"):
            result["issue"] = line.replace("Issue:", "").strip()
        elif line.lower().startswith("details:"):
            result["details"] = line.replace("Details:", "").strip()
        elif line.lower().startswith("root cause:"):
            result["root_cause"] = line.replace("Root Cause:", "").strip()
        elif line.lower().startswith("resolution:"):
            result["resolution"] = line.replace("Resolution:", "").strip()

    return result
