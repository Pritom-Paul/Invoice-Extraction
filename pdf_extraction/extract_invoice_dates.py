# pdf_extraction/extract_invoice_dates.py

import re

def extract_invoice_dates(text):
    invoice_dates = re.findall(r'Date:\s+(\d{4}-\d{2}-\d{2})', text)
    return invoice_dates
