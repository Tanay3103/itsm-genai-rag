import uuid
from datetime import datetime

import streamlit as st

from config.agent import USER_AVATAR
from conversation.history import render_history
from conversation.smalltalk import is_gratitude, is_greeting
from handlers.confirmation import handle_confirmation
from handlers.gratitude import handle_gratitude
from handlers.greetings import handle_greeting
from handlers.tickets import handle_ticket_lookup
from handlers.triage import handle_triage
from memory.conversation import ConversationMemory
from ui.sidebar import render_sidebar
from utils.bootstrap_qdrant import bootstrap_qdrant

st.set_page_config(page_title="AI ITSM Agent", page_icon="🤖", layout="wide")
st.title("AI ITSM Agent")


@st.cache_resource
def init():
    bootstrap_qdrant()


init()

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "memory" not in st.session_state:
    st.session_state.memory = ConversationMemory(st.session_state.session_id)

memory = st.session_state.memory

render_sidebar(memory)
render_history(memory)

user_query = st.chat_input("How can I help you today?")

if not user_query:
    st.stop()

# 1️⃣ Immediately show user message (chat-app behavior)
with st.chat_message("user", avatar=USER_AVATAR):
    st.caption(datetime.utcnow().strftime("%H:%M"))
    st.markdown(user_query)

# 2️⃣ Persist message
memory.add_user(user_query)

# 3️⃣ Handle conversation
if is_greeting(user_query):
    handle_greeting(memory)
    st.rerun()

if is_gratitude(user_query):
    handle_gratitude(memory)
    st.rerun()

if handle_confirmation(user_query, memory):
    st.rerun()

if handle_ticket_lookup(user_query):
    st.rerun()

handle_triage(user_query, memory)

# 4️⃣ Force rerender so history updates immediately
st.rerun()
