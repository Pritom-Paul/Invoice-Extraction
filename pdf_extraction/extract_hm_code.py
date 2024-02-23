# pdf_extraction/extract_hm_code.py

import re

def extract_hm_code(text):
    hm_codes = []
    lines = text.split('\n')
    for line in lines:
        match = re.search(r'H&M Order No: (\d{6}-\d{4})', line)
        if match:
            hm_codes.append(match.group(1))
    return hm_codes
