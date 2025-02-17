import os
from dotenv import load_dotenv

from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")


prompt=ChatPromptTemplate(
    [
        ("system","you are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{Qusetion}")
    ]
)

st.title("Langchain Demo With Gemma Model")
input_text=st.text_input("What question you have in mind?")

llm=OllamaLLM(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"Qusetion":input_text}))