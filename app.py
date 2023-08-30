# LangChain QuickStart App with TextGen API

import streamlit as st
from langchain.llms import TextGen

model_url = "http://localhost:5000"

st.title("🦜🔗 Langchain Quickstart App")

def generate_response(input_text):
    llm = TextGen(model_url=model_url ,max_new_tokens=1024)
    st.info(llm(input_text))


with st.form("my_form"):
    text = st.text_area("Enter text:", "What are 3 key advice for learning how to code?")
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)
