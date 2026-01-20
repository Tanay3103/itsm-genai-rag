from config.config import OPENAI_MODEL


def _fallback(query: str):
    q = query.lower()
    if any(k in q for k in ["status", "ticket", "inc-", "req-", "sr-"]):
        return "TICKET_LOOKUP"
    if any(k in q for k in ["error", "issue", "problem", "not working", "failed"]):
        return "ISSUE_REPORTED"
    return "GENERAL"


try:
    from langchain_core.messages import HumanMessage
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(model=OPENAI_MODEL, temperature=0)
except Exception:
    llm = None


def classify_intent(query: str) -> str:
    if not llm:
        return _fallback(query)

    prompt = f"""
Classify the intent into exactly ONE:
- TICKET_LOOKUP
- ISSUE_REPORTED
- FOLLOW_UP_ANSWER
- GENERAL

User input:
{query}

Return ONLY the label.
"""
    try:
        return llm.invoke([HumanMessage(content=prompt)]).content.strip()
    except Exception:
        return _fallback(query)
