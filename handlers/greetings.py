from ui.chat import bot_message


def handle_greeting(memory):
    response = "Hi there! 👋\n\n" "Please describe the issue you’re facing, and I’ll help you."
    memory.add_ai(response)
    bot_message(response)
