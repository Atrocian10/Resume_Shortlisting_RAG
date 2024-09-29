import sys, os
sys.dont_write_bytecode = True

import pandas as pd
import openai
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.faiss import DistanceStrategy
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from llm_agent import ChatBot
from ingest_data import ingest
from retriever import SelfQueryRetriever
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
DATA_PATH = CURRENT_DIR + "/../data/main-data/synthetic-resumes.csv"
FAISS_PATH = CURRENT_DIR + "/../vectorstore"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

embedding_model=HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL, model_kwargs={"device": "cpu"})
"""
vectordb = FAISS.load_local(FAISS_PATH,embedding_model, distance_strategy=DistanceStrategy.COSINE, allow_dangerous_deserialization=True) 

rag_pipeline = SelfQueryRetriever(vectordb, pd.read_csv(DATA_PATH))

"""
df_load = pd.read_csv('resume_file.csv')

vectordb = ingest(df_load, "Resume", embedding_model)

retriever = SelfQueryRetriever(vectordb, df_load)

user_query = ""
llm = ChatBot(
  api_key="sk-proj-uFtY23YsXzoZXwZqZmuWT3BlbkFJ9THodJSmM3cj1nXIQhpH",
  model="gpt-3.5-turbo",
)
if user_query is not None and user_query != "":
      document_list = retriever.retrieve_docs(user_query, llm, "Generic RAG")
else:
 print(______________________________________)
df=pd.DataFrame(document_list)
df.to_csv('Solution.csv')
print(df)

