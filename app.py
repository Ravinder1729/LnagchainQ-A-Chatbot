from langchain.llms import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Function to load OpenAI model and get responses
def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="text-davinci-003", temperature=0.5)
    response = llm(question)
    return response

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input_text = st.text_input("Ask the Question:", key="input")
submit = st.button("submit")

# If the Ask button is clicked
if submit:
    response = get_openai_response(input_text)
    st.subheader("The Response is")
    st.write(response)
