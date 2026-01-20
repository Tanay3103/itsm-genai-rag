import streamlit as st

from config.agent import AGENT_AVATAR, AGENT_NAME, AGENT_ROLE, USER_AVATAR
from utils.format_time import format_ts


def render_history(memory):
    for msg in memory.get():
        ts = format_ts(msg.get("ts"))
        role = msg["role"]

        if role == "assistant":
            with st.chat_message("assistant", avatar=AGENT_AVATAR):
                st.caption(f"{AGENT_NAME} • {AGENT_ROLE}" + (f" • {ts}" if ts else ""))
                st.markdown(msg["content"])
        else:
            with st.chat_message("user", avatar=USER_AVATAR):
                if ts:
                    st.caption(ts)
                st.markdown(msg["content"])
