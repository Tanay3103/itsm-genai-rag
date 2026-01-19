from config import TICKET_SIM_THRESHOLD, KB_SIM_THRESHOLD

def route_decision(ticket_results, kb_results):
    if ticket_results:
        doc, score = ticket_results[0]
        if score >= TICKET_SIM_THRESHOLD:
            return "TICKET", doc, score

    if kb_results:
        doc, score = kb_results[0]
        if score >= KB_SIM_THRESHOLD:
            return "KNOWLEDGE", doc, score

    return "NEW", None, 0.0
