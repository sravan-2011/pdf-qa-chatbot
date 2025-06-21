import numpy as np, faiss
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore import InMemoryDocstore
from langchain.schema import Document

def store_vectors(text_parts):
    emb = OpenAIEmbeddings()
    vecs = np.array([emb.embed_query(t) for t in text_parts])
    idx = faiss.IndexFlatL2(vecs.shape[1]); idx.add(vecs)
    docs = [Document(page_content=t) for t in text_parts]
    ds = InMemoryDocstore({i: d for i, d in enumerate(docs)})
    return FAISS(index=idx, docstore=ds,
                 index_to_docstore_id={i:i for i in range(len(docs))},
                 embedding_function=emb.embed_query)
