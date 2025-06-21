
# 📄 PDF Q&A Chatbot with GPT-4 + FAISS

This project is a simple, chatbot that lets you upload a PDF file and ask natural language questions about its content. 
It uses OpenAI's GPT-4 for answering questions and FAISS for efficient vector similarity search.

---

## 🚀 Features

- ✅ Upload a PDF file
- ✅ Extracts and chunks PDF text
- ✅ Embeds chunks using OpenAI embeddings
- ✅ Stores and retrieves using FAISS vector store
- ✅ Asks questions and answers contextually via GPT-4
- ✅ Built using Streamlit for a clean UI

---

## 🧱 Project Structure

```
pdf_qa_chatbot/
├── app.py               # Main Streamlit frontend
├── pdf_processor.py     # Extracts text from PDF
├── text_splitter.py     # Chunks long text into smaller pieces
├── vector_store.py      # Builds and stores FAISS vector index
├── qa_chain.py          # Handles Q&A using GPT-4
├── .env                 # (Ignored) Stores your OpenAI API key
├── requirements.txt     # All dependencies
```

---

## ⚙️ Setup

### 1. Clone the repo

```
git clone https://github.com/YOUR_USERNAME/pdf_qa_chatbot.git
cd pdf_qa_chatbot
```

### 2. Create a virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add your OpenAI API key to `.env`

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Run the app

```
streamlit run app.py
```

---

## 🧠 How it Works

1. User uploads a PDF
2. Text is extracted and chunked with overlaps
3. Chunks are embedded using OpenAI embeddings
4. FAISS indexes vectors for similarity search
5. GPT-4 is prompted only with the most relevant chunks

---

## 📁 .gitignore Tip

Make sure your `.env` file is listed in `.gitignore`:

```
.env
__pycache__/
.venv/
```

---


