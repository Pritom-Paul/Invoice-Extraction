# pdf_extraction/extract_text.py

import pdfplumber

def extract_text_with_pdfplumber(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text
