from conversation.confirmations import is_negative_confirmation, is_positive_confirmation
from ui.chat import bot_message


def handle_confirmation(user_query: str, memory) -> bool:
    """
    Returns True if confirmation was handled
    """

    if memory.support_state["mode"] != "CONFIRM":
        return False

    if is_positive_confirmation(user_query):
        solution = memory.support_state.get("current_solution")
        response = (
            f"✅ Great! I’m glad the following resolved the issue:\n\n"
            f"🛠️ *{solution}*\n\n"
            "I’ve marked this as resolved. If you need help again, just let me know."
        )

        memory.reset()
        memory.add_ai(response)
        bot_message(response, kind="success")
        return True

    if is_negative_confirmation(user_query):
        response = (
            "Thanks for confirming. 👍\n\n" "Let’s try another approach or escalate this if needed."
        )

        memory.support_state(mode="TRIAGE")
        memory.add_ai(response)
        bot_message(response, kind="info")
        return True

    # If user says something unclear while in CONFIRM mode
    response = (
        "Just to confirm — did the previous steps resolve the issue?\n\n"
        "Please reply with *Yes* or *No*."
    )
    memory.add_ai(response)
    bot_message(response, kind="question")
    return True
