def route(ticket_results, kb_results, t_thresh, kb_thresh):
    if ticket_results and ticket_results[0].score >= t_thresh:
        return "TICKET"
    if kb_results and kb_results[0].score >= kb_thresh:
        return "KNOWLEDGE"
    return "NEW"
