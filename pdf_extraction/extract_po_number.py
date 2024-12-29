# pdf_extraction/extract_po_number.py

import re

def extract_po_number(text):
    po_numbers = []
    lines = text.split('\n')
    for line in lines:
        match = re.search(r'H&M Order No: (\d{6}-\d{4})', line)
        if match:
            po_numbers.append(match.group(1))
    return po_numbers
