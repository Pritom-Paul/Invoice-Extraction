# pdf_extraction/extract_tables_with_pdfplumber.py

import pdfplumber

def extract_tables_with_pdfplumber(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        tables = []
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                tables.extend(table)
    return tables
