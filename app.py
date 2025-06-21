import streamlit as st
from dotenv import load_dotenv
import os
from pdf_processor import extract_text_from_pdf
from text_splitter import split_text
from vector_store import store_vectors
from qa_chain import get_answer

load_dotenv()

st.title("PDF Q&A Chatbot")

uploaded = st.file_uploader("Upload PDF", type=["pdf"])
if uploaded:
    text = extract_text_from_pdf(uploaded)
    chunks = split_text(text)
    vector_index = store_vectors(chunks)
    st.success("Ready! Ask your question.")
    question = st.text_input("Question:")
    if question:
        with st.spinner("Thinking..."):
            ans = get_answer(vector_index, question)
            st.markdown(f"**Answer:** {ans}")
