import streamlit as st

def ask_questions(topic):
    st.subheader("👤 Personalization Questions")

    prior_knowledge = st.selectbox("What is your current knowledge level?", ["Beginner", "Intermediate", "Advanced"])
    interest = st.text_input(f"What are you most curious about within {topic}?")
    format_pref = st.selectbox("Preferred learning format:", ["Text", "Visuals", "Examples", "All"])

    return {
        "knowledge": prior_knowledge,
        "interest": interest,
        "format": format_pref
    }
