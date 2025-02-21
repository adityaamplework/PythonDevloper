import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes

load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

model=ChatGroq(model_name="Gemma2-9b-It" )

generic_template="Translate the following into {language}"

prompt=ChatPromptTemplate.from_messages([
    ("system",generic_template),
    ("user","{text}")
])

paser=StrOutputParser()

chain=prompt|model|paser

chain.invoke({"text":"my name is aditya","language":"hindi"})