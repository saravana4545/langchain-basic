import streamlit as st
from langchain_community.llms import Ollama

# Initialize Ollama
llm = Ollama(model="llama2")

st.title("Ollama Chatbot")

# User input
user_input = st.text_input("Ask me anything:")

if user_input:
    response = llm.invoke(user_input)
    st.write(response)
