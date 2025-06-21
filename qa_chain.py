import os
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

def get_answer(vector_index, question):
    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="Context: {context}\nQ: {question}\nA:"
    )

    # ✅ Using 'stuff' chain_type for compatibility with custom prompt
    chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=prompt_template)

    docs = vector_index.similarity_search(question, k=3)
    result = chain.run(input_documents=docs, question=question)

    return result
