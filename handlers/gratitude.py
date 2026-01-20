from ui.chat import bot_message


def handle_gratitude(memory):
    response = "You’re very welcome! 😊\n\n" "If you need help again, just let me know."
    memory.add_ai(response)
    bot_message(response, kind="success")
    memory.reset()
