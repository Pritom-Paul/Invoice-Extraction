# pdf_extraction/extract_hs_code.py

import re

def extract_hs_code(text):
    hs_codes = re.findall(r'hs\s*code:\s*(\d+)', text, re.IGNORECASE)
    if hs_codes:
        return hs_codes
    else:
        return ['']

