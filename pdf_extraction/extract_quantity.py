# pdf_extraction/extract_quantity.py

import re

def extract_quantity(text):
    quantities = re.findall(r'\b(\d+)\s+\d+\.\d+\s+\d+\.\d+\b', text)
    return quantities
