import streamlit as st
from utils_1 import get_answer
import os

#UI code file
st.set_page_config("FileAnalyzer " , page_icon=':crescent_moon:')

api_key_input = st.sidebar.text_input('Welcome to file Analyzer 😃' , type='password')

if api_key_input:
    st.session_state['API_Key'] = api_key_input
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = st.session_state['API_Key']


st.title("Let's do some analysis on your file")
st.header("Please upload your any file here:")



#Capture the csv file

data = st.file_uploader("Upload file here" ,type=['csv', 'txt', 'ppt', 'pptx', 'doc', 'docx', 'pdf'])
query = st.text_area("Enter your query")
button = st.button("Generate Response")

if button:

    answer =  get_answer(data, query, st.session_state['API_Key'])
    st.write(answer)
    