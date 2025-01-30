from langchain import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI

class RAG:
    def __init__(self, embedding_model_name="text-embedding-ada-002", llm_model_name="gpt-3.5-turbo"):
        self.embeddings = OpenAIEmbeddings(model=embedding_model_name)
        self.llm = OpenAI(model=llm_model_name)
        self.vector_store = FAISS(embedding_function=self.embeddings)

    def add_documents(self, documents):
        self.vector_store.add_documents(documents)

    def generate_response(self, query):
        retrieval_qa = RetrievalQA(llm=self.llm, retriever=self.vector_store.as_retriever())
        return retrieval_qa.run(query)