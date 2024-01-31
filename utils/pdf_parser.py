import PyPDF2

def pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text =""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text