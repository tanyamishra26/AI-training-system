import streamlit as st
from src.pdf_utils import extract_text_from_pdf
from src.generators import generate_summary, generate_training, generate_quiz

st.set_page_config(page_title="AI Trainer", layout="wide")

st.title("AI Training System")

uploaded_file = st.file_uploader("Upload SOP PDF", type=["pdf"])

if uploaded_file:
    if st.button("Generate Training Content"):

        with st.spinner("Processing SOP..."):

            # Extract text
            text = extract_text_from_pdf(uploaded_file)

            # Generate outputs
            summary = generate_summary(text)
            training = generate_training(text)
            quiz = generate_quiz(text)

        # Display results
        st.subheader("📄 Summary")
        st.write(summary)

        st.subheader("📘 Training Steps")
        st.write(training)

        st.subheader("🧠 Quiz")
        st.write(quiz)