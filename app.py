import streamlit as st

from rag.intent_classifier import classify_intent
from rag.ticket_retriever import search_tickets
from rag.knowledge_retriever import search_knowledge
from rag.decision_router import route_decision
from utils.confidence import compute_confidence
from utils.auto_ingest import ingest_ticket
from mock_itsm.servicenow_api import create_servicenow_ticket
from memory.conversation import ConversationMemory

st.set_page_config(page_title="AI ITSM Copilot", layout="wide")
st.title("🤖 AI ITSM Copilot")

memory = ConversationMemory()

if st.sidebar.button("🧹 Clear Conversation"):
    memory.clear()
    st.experimental_rerun()

for msg in memory.get():
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_query = st.chat_input("Describe your IT issue...")

if user_query:
    memory.add_user(user_query)
    with st.chat_message("user"):
        st.markdown(user_query)

    intent = classify_intent(user_query)

    ticket_results = search_tickets(user_query)
    kb_results = search_knowledge(user_query)

    decision, doc, score = route_decision(ticket_results, kb_results)

    if decision == "TICKET":
        response = (
            f"✅ **This issue has occurred before**\n\n"
            f"**Confidence:** {compute_confidence(score)}%\n\n"
            f"{doc.page_content}"
        )

    elif decision == "KNOWLEDGE":
        response = (
            f"ℹ️ **This issue is documented in internal knowledge**\n\n"
            f"**Confidence:** {compute_confidence(score)}%\n\n"
            f"{doc.page_content}"
        )

    else:
        ticket = create_servicenow_ticket({"description": user_query})
        ingest_ticket(user_query, {"ticket_id": ticket["id"], "status": "Open"})

        response = (
            "❌ **I couldn’t find this issue in ticket history or knowledge base.**\n\n"
            f"🎫 **Ticket Created:** `{ticket['id']}`\n\n"
            "This issue has been saved for future reference."
        )

    with st.chat_message("assistant"):
        st.markdown(response)

    memory.add_ai(response)
