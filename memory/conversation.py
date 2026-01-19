class ConversationMemory:
    def __init__(self):
        import streamlit as st
        if "history" not in st.session_state:
            st.session_state.history = []

    def add_user(self, message: str):
        import streamlit as st
        st.session_state.history.append({"role": "user", "content": message})

    def add_ai(self, message: str):
        import streamlit as st
        st.session_state.history.append({"role": "assistant", "content": message})

    def get(self):
        import streamlit as st
        return st.session_state.history

    def clear(self):
        import streamlit as st
        st.session_state.history = []
