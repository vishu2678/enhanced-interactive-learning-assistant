
import streamlit as st
from interaction.question_handler import ask_questions
from reports.generator import generate_report

st.title("📘 Enhanced Interactive Learning Assistant")

# Step 1: Topic Input
topic = st.text_input("Enter a learning topic (e.g., 'Climate Change'):")

if topic:
    # Step 2: Ask questions
    user_profile = ask_questions(topic)

    # Step 3: Generate report
    if st.button("Generate Report"):
        report = generate_report(topic, user_profile)
        st.markdown("### 📄 Generated Report:")
        st.markdown(report, unsafe_allow_html=True)
