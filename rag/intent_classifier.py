from langchain.chat_models import ChatOpenAI

def classify_intent(query):
    prompt = f"""
Classify intent into one of:
KNOWN_ISSUE_QUERY
NEW_ISSUE_INVESTIGATION
HOW_TO_FIX
STATUS_CONFIRMATION
GENERAL_ITSM_QUESTION

User query: {query}
Return only the intent.
"""
    return ChatOpenAI(temperature=0).predict(prompt).strip()
