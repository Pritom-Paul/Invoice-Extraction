# pdf_extraction/extract_invoice_dates.py

import re

def extract_invoice_dates(text):
    first_pattern_dates = re.findall(r'Date:\s+(\d{4}-\d{2}-\d{2})', text)
    second_pattern_dates = re.findall(r'Date:\s+(\d{2}-\d{2}-\d{4})', text)
    
    if first_pattern_dates:
        invoice_dates = first_pattern_dates
    else:
        invoice_dates = second_pattern_dates
