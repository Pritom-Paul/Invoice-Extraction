# pdf_extraction/extract_invoice_numbers.py

import re

def extract_invoice_numbers(text):
    invoice_numbers = re.findall(r'Number:\s*(\d+)', text)
    return invoice_numbers
