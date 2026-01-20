import streamlit as st


def render_sidebar(memory):
    state = memory.support_state

    with st.sidebar:
        st.header("🧠 Support Context")
        st.markdown(f"**Mode:** `{state['mode']}`")

        if state["issue_summary"]:
            st.markdown("**Issue Summary**")
            st.info(state["issue_summary"])

        if state["answers"]:
            st.markdown("**Collected Details**")
            for q, a in state["answers"].items():
                st.write(f"- **{q}**: {a}")

        if state["solutions_tried"]:
            st.markdown("**Attempted Solutions**")
            for i, s in enumerate(state["solutions_tried"], 1):
                st.write(f"{i}. {s[:80]}…")
