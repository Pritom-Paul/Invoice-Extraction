# pdf_extraction/extract_invoice_numbers.py

import re

def extract_invoice_numbers(text):
    invoice_numbers = re.findall(r'Number:\s*(\S+)', text)
    
    # If no matches are found, search for 'Invoice No:' followed by the number
    if not invoice_numbers:
        invoice_numbers = re.findall(r'Invoice No:\s*(\S+)', text)
    
    return invoice_numbers
