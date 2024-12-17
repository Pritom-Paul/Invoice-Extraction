# pdf_extraction/extract_invoice_dates.py

import re
from datetime import datetime

# def extract_invoice_dates(text):
#     pattern = re.findall(r'.Date:\s+(\d{2}-\d{2}-\d{4}|\d{4}-\d{2}-\d{2})', text)

#     invoice_dates = pattern
#     if invoice_dates:
#         date_str = invoice_dates[0]
#         try:
#             date_obj = datetime.strptime(date_str, '%Y-%m-%d')
#         except ValueError:
#             date_obj = datetime.strptime(date_str, '%d-%m-%Y')
#         return date_obj.strftime('%d-%m-%Y')
#     else:
#         return None
    
def extract_invoice_dates(text):
    pattern = re.findall(r'.Invoice Date:\s+(\d{2}-\d{2}-\d{4}|\d{4}-\d{2}-\d{2})', text)

    invoice_dates = pattern
    if invoice_dates:
        date_str = invoice_dates[0]
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            date_obj = datetime.strptime(date_str, '%d-%m-%Y')
        return date_obj.strftime('%d-%m-%Y')
    else:
        return None