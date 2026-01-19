from langchain.chat_models import ChatOpenAI
from config import OPENAI_MODEL

def classify_intent(query: str) -> str:
    prompt = f"""
Classify intent into one of:
KNOWN_ISSUE_QUERY
NEW_ISSUE_INVESTIGATION
HOW_TO_FIX
STATUS_CONFIRMATION
GENERAL_ITSM_QUESTION

User query: {query}
Return only intent.
"""
    return ChatOpenAI(model=OPENAI_MODEL, temperature=0).predict(prompt).strip()
    
