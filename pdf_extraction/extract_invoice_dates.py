# pdf_extraction/extract_invoice_dates.py

import re

def extract_invoice_dates(text):
    pattern = re.findall(r'.Date:\s+(\d{2}-\d{2}-\d{4}|\d{4}-\d{2}-\d{2})', text)

    invoice_dates = pattern
    if invoice_dates:
        return invoice_dates[0]
    else:
        return None


