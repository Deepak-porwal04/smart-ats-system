import streamlit as st
from src import generative_model
from utils import pdf_parser, prompts

def process_button(btn_type, uploaded_file, jd):
    if uploaded_file is not None:
        if jd !="":
            with st.spinner("Processing..."):
                text = pdf_parser.pdf_text(uploaded_file)
                prompt = None

                if btn_type == 'summary':
                    prompt = prompts.summary_prompt
                elif btn_type == 'percentage':
                    prompt = prompts.match_prompt
                elif btn_type == 'improve':
                    prompt = prompts.improve_prompt
                elif btn_type == 'keywords':
                    prompt = prompts.keywords_prompt

                if prompt is not None:
                    response = generative_model.get_response(prompt.format(text=text, jd=jd))
                    st.subheader("Response")
                    st.write(response)
        else:
            st.warning("Please enter the Job Description first")
    else:
        st.warning("Please upload the resume")