import sys, os
sys.dont_write_bytecode = True                                                                                                                  
import pandas as pd
import openai                                                                                                                                               from langchain_core.messages import AIMessage, HumanMessage                                                                                                 from langchain_community.vectorstores import FAISS                                                                                                          from langchain_community.vectorstores.faiss import DistanceStrategy                                                                                         from langchain_community.embeddings import HuggingFaceEmbeddings                                                                                                                                                                                                                                                        from llm_agent import ChatBot                                                                                                                               from ingest_data import ingest                                                                                                                              from retriever import SelfQueryRetriever


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__)) 
sys.path.append(os.path.dirname(CURRENT_DIR))
DATA_PATH = CURRENT_DIR + "/../data/main-data/synthetic-resumes.csv"
FAISS_PATH = CURRENT_DIR + "/../vectorstore"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


