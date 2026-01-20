def decide_next_action(ticket_hits, knowledge_hits, state):
    """
    Decide next step based on confidence, attempts, and info completeness
    """

    if state["mode"] == "CONFIRM":
        return "WAIT_CONFIRMATION"

    if ticket_hits and ticket_hits[0][1] > 0.8:
        return "TRY_EXISTING_FIX"

    if knowledge_hits and knowledge_hits[0][1] > 0.7:
        return "TRY_KB_FIX"

    if len(state["answers"]) < 2:
        return "ASK_MORE_QUESTIONS"

    if len(state["solutions_tried"]) >= 2:
        return "ESCALATE"

    return "TRY_KB_FIX"
