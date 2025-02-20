from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
import streamlit as st

#llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
llm = Ollama(model="llama2")

st.title("Simple Chat Bot")
input_text = st.text_input("Enter your query:")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Your name is Sandal's Assistant."),
    ("user", "User query: {query}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({"query": input_text})
    st.write(response)
