def is_greeting(text: str) -> bool:
    return any(p in text.lower() for p in ["hi", "hello", "hey", "good morning", "good evening"])


def is_gratitude(text: str) -> bool:
    return any(p in text.lower() for p in ["thanks", "thank you", "appreciate", "thx"])
