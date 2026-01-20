import re

YES_PATTERNS = [
    r"\byes\b",
    r"\bresolved\b",
    r"\bfixed\b",
    r"\bworking\b",
    r"\bit worked\b",
]

NO_PATTERNS = [
    r"\bno\b",
    r"\bnot resolved\b",
    r"\bdid not work\b",
    r"\bstill not working\b",
    r"\bissue persists\b",
]


def is_positive_confirmation(text: str) -> bool:
    text = text.lower()
    return any(re.search(p, text) for p in YES_PATTERNS)


def is_negative_confirmation(text: str) -> bool:
    text = text.lower()
    return any(re.search(p, text) for p in NO_PATTERNS)
