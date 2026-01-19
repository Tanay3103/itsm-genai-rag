import streamlit as st
from rag.intent_classifier import classify_intent
from rag.ticket_retriever import search_tickets
from rag.knowledge_retriever import search_knowledge
from utils.confidence import compute_confidence
from utils.auto_ingest import ingest_ticket
from mock_itsm.servicenow_api import create_servicenow_ticket
from config import TICKET_SIM_THRESHOLD, KB_SIM_THRESHOLD

st.set_page_config(page_title="AI ITSM Copilot")
st.title("🤖 AI ITSM Copilot")

query = st.text_area("Describe your IT issue")

if st.button("Analyze"):
    intent = classify_intent(query)
    st.write(f"**Detected Intent:** `{intent}`")

    ticket_results = search_tickets(query)

    if ticket_results and ticket_results[0][1] >= TICKET_SIM_THRESHOLD:
        doc, score = ticket_results[0]
        st.success("Known issue found (Ticket History)")
        st.metric("Confidence", f"{compute_confidence(score)}%")
        st.write(doc.page_content)

    else:
        kb_results = search_knowledge(query)
        if kb_results and kb_results[0][1] >= KB_SIM_THRESHOLD:
            doc, score = kb_results[0]
            st.info("Found in internal knowledge")
            st.metric("Confidence", f"{compute_confidence(score)}%")
            st.write(doc.page_content)

        else:
            st.warning("New issue detected – creating ITSM ticket")
            ticket = create_servicenow_ticket({"description": query})
            ingest_ticket(query, {"ticket_id": ticket["id"], "status": "Open"})
            st.success(f"Ticket created: {ticket['id']}")
