# pdf_extraction/extract_hs_code.py

import re

def extract_hs_code(text):
    hs_codes = re.findall(r'HS Code:\s+(\d+)', text)
    return hs_codes
