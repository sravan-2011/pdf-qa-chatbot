import streamlit as st
from dotenv import load_dotenv
import os
#from pdf_processor import extract_text_from_pdf
from pdf_processor_ocr import extract_text_from_pdf
from text_splitter import split_text
from vector_store import store_vectors
from qa_chain import get_answer

load_dotenv()

st.title("PDF Q&A Chatbot")


# OLD: single file uploader
# uploaded = st.file_uploader("Upload PDF", type=["pdf"])

# ✅ NEW: multi-file uploader
uploaded_files = st.file_uploader("Upload PDF(s)", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    all_text = ""
    for uploaded_file in uploaded_files:
        st.info(f"Processing: {uploaded_file.name}")
        file_text = extract_text_from_pdf(uploaded_file)
        all_text += file_text + "\n"

    # Rest of your existing code stays the same
    chunks = split_text(all_text)
    vector_index = store_vectors(chunks)

    st.success("All PDFs processed. Ask a question!")

    question = st.text_input("Your question:")
    if question:
        with st.spinner("Thinking..."):
            answer = get_answer(vector_index, question)
            st.markdown(f"**Answer:** {answer}")
