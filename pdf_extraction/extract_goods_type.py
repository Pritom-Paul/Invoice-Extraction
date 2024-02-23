# pdf_extraction/extract_goods_type.py

import re

def extract_goods_type(text):
    goods_types = []
    for line in text.split('\n'):
        match = re.search(r'\d+\s+Cartons\s+(.*?)\s+P', line)
        if match:
            goods_types.append(match.group(1))
    return goods_types
