import streamlit as st
from src.pdf_utils import extract_text_from_pdf
from src.generators import generate_summary, generate_training, generate_quiz, parse_quiz

st.set_page_config(page_title="AI Trainer", layout="wide")

# 🔹 Initialize session state
if "generated" not in st.session_state:
    st.session_state.generated = False

# 🔹 Title
st.title("📘 SOP → AI Training System")

uploaded_file = st.file_uploader("Upload SOP PDF", type=["pdf"])

if uploaded_file:

    # 🔹 Generate button
    if st.button("🚀 Generate Training Content"):
        st.session_state.generated = True

        with st.spinner("Processing SOP..."):
            text = extract_text_from_pdf(uploaded_file)

            # Store results in session state
            st.session_state.summary = generate_summary(text)
            st.session_state.training = generate_training(text)
            st.session_state.quiz = generate_quiz(text)

    # 🔹 Show results AFTER generation
    if st.session_state.generated:

        # 📄 Summary
        st.subheader("📄 Summary")
        st.markdown(st.session_state.summary)

        # 📘 Training
        st.subheader("📘 Training Steps")
        st.markdown(st.session_state.training)

        st.markdown("---")

        # 🧠 Quiz Section
        st.markdown("## 🧠 Knowledge Check")

        quiz_data = parse_quiz(st.session_state.quiz)

        if not quiz_data:
            st.error("⚠️ Quiz parsing failed. Please check format.")
        else:
            for i, q in enumerate(quiz_data):

                st.markdown(f"### {q['question']}")

                selected = st.radio(
                    "Choose an option:",
                    q["options"],
                    key=f"q_{i}",
                    index=None
                )

                if selected is not None:
                    answer_letter = q["answer"].strip()[0]
                    
                    correct_option = None
                    for opt in q["options"]:
                        if opt.startswith(answer_letter):
                            correct_option = opt
                            break
                        
                        if selected == correct_option:
                            st.success("✅ Correct!")
                        else:
                            st.error(f"❌ Incorrect! Correct answer: {correct_option}")

                st.markdown("---")