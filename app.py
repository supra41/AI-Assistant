import streamlit as st

from rag import retrieve
from llm_utils import ask_llm

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Teaching Assistant",
    page_icon="🎓",
    layout="wide"
)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.title("🎓 AI Teaching Assistant")

    st.markdown("---")

    st.subheader("Project Information")

    st.write("**Embedding Model:** BGE-M3")
    st.write("**LLM:** Llama 3.2")
    st.write("**Search:** Cosine Similarity")

    st.markdown("---")

    st.success("🟢 Local RAG Ready")

# ---------------------------------------------------
# Main Page
# ---------------------------------------------------

st.title("🎓 AI Teaching Assistant")

st.write(
    "Ask questions about your lecture videos and get answers generated using your local RAG pipeline."
)

question = st.text_input(
    "Ask your question",
    placeholder="Example: What is SQL?"
)

# ---------------------------------------------------
# Ask Button
# ---------------------------------------------------

if st.button("Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    # -----------------------------
    # Retrieve relevant chunks
    # -----------------------------

    with st.spinner("Searching lecture materials..."):

        top5 = retrieve(question)

    # -----------------------------
    # Build Context
    # -----------------------------

    context = ""

    for _, row in top5.iterrows():
        context += row["text"]
        context += "\n\n"

    # -----------------------------
    # Ask LLM
    # -----------------------------

    with st.spinner("Generating answer..."):

        answer = ask_llm(
            context=context,
            question=question
        )

    # -----------------------------
    # Display Answer
    # -----------------------------

    st.markdown("## 🤖 Answer")

    st.success(answer)

    # -----------------------------
    # Display Sources
    # -----------------------------

    st.markdown("---")

    st.markdown("## 📚 Sources")

    for _, row in top5.iterrows():

        with st.expander(
            f"📖 {row['title']} | Similarity: {row['score']:.3f}"
        ):

            st.write(f"**Lecture:** {row['number']}")
            st.write(f"**Start:** {row['start']}")
            st.write(f"**End:** {row['end']}")

            st.markdown("**Content**")

            st.write(row["text"])