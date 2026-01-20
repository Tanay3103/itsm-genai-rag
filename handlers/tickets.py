from rag.ticket_lookup import extract_ticket_id, get_ticket_by_id
from ui.cards import ticket_card
from ui.chat import bot_message


def handle_ticket_lookup(user_query):
    ticket_id = extract_ticket_id(user_query)
    if not ticket_id:
        return False

    ticket = get_ticket_by_id(ticket_id)
    if ticket:
        bot_message(f"Here’s the current status of ticket **{ticket_id}**")
        ticket_card(ticket)
    else:
        bot_message(f"No ticket found with ID **{ticket_id}**", kind="error")

    return True
