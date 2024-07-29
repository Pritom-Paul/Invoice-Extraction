# pdf_extraction/extract_hs_code.py

import re

def extract_hs_code(text):
    hs_codes = re.findall(r'HS Code:\s+(\d+)', text)
    if hs_codes:
        return hs_codes
    else:
        return ['']

