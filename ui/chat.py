from datetime import datetime

import streamlit as st

from config.agent import AGENT_AVATAR, AGENT_NAME, AGENT_ROLE

ICON_MAP = {
    "info": "💬",
    "question": "❓",
    "solution": "🛠️",
    "success": "✅",
    "error": "⚠️",
    "ticket": "🎫",
}


def bot_message(text, kind="info"):
    ts = datetime.utcnow().strftime("%H:%M")
    icon = ICON_MAP.get(kind, "💬")

    with st.chat_message("assistant", avatar=AGENT_AVATAR):
        st.caption(f"{AGENT_NAME} • your {AGENT_ROLE} is typing... • {ts}")
        st.markdown(f"{icon} {text}")
