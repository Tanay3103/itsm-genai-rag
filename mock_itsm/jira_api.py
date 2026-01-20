def create_jira_ticket(payload):
    return {"id": "JIRA-101", "payload": payload}


def get_jira_ticket(ticket_id: str):
    if ticket_id.startswith("TASK-") or ticket_id.startswith("BUG-"):
        return {
            "id": ticket_id,
            "status": "Open",
            "priority": "Medium",
            "description": "Application login error reported by user",
            "resolution": None,
        }
    return None
