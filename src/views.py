import streamlit as st
from src.pipeline import process_button

def create_app_ui():
    st.title("ATS Application")
    st.text("Improve your resume")
    jd = st.text_area("Paste the job description here")
    uploaded_file = st.file_uploader("upload your resume",type='pdf',help="Please upload the resume")
    if uploaded_file is not None:
        st.success("file uploaded successfully")

    summary_btn = st.button("Resume Summary")
    percentage_btn = st.button("Check the percentage match")
    improve_btn = st.button("Tips to improve the resume")
    keywords_btn = st.button("Check the missing Keywords")

    # Usage example:
    if summary_btn:
        process_button('summary', uploaded_file, jd)

    if percentage_btn:
        process_button('percentage', uploaded_file, jd)

    if improve_btn:
        process_button('improve', uploaded_file, jd)

    if keywords_btn:
        process_button('keywords', uploaded_file, jd)