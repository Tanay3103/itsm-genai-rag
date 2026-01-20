from utils.auto_ingest import ingest_new_ticket


def create_servicenow_ticket(payload):
    ticket = {
        "id": "INC-" + str(10000),
        "status": "Open",
        "description": payload.get("description"),
        "resolution": "Pending investigation",
    }

    ingest_new_ticket(ticket)
    return ticket


def get_servicenow_ticket(ticket_id: str):
    # Mock lookup
    if ticket_id.startswith("INC-"):
        return {
            "id": ticket_id,
            "status": "In Progress",
            "priority": "High",
            "description": "VPN access failure after password reset",
            "resolution": "Under investigation by network team",
        }
    return None
