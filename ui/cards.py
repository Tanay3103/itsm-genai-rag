import streamlit as st


def ticket_card(ticket: dict):
    with st.chat_message("assistant"):
        st.markdown("### 🎫 Ticket Summary")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Ticket ID:** `{ticket.get('id')}`")
            st.markdown(f"**Status:** `{ticket.get('status')}`")

        with col2:
            st.markdown(f"**Priority:** `{ticket.get('priority', 'Normal')}`")
            st.markdown(f"**Source:** `{ticket.get('source', 'ServiceNow')}`")

        st.markdown("**Issue Description**")
        st.info(ticket.get("description"))

        if ticket.get("resolution"):
            st.success(ticket["resolution"])
