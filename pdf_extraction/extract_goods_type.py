# pdf_extraction/extract_goods_type.py

import re

def extract_goods_type(text):
    goods_types = []
    lines = text.split('\n')
    for i in range(len(lines) - 1):  # Adjust to prevent index error
        line = lines[i]
        match = re.search(r'\d+\s+Cartons\s+(.*?)\s+P', line)
        if match:
            goods_type = match.group(1)
            # Check the next line for additional information
            next_line = lines[i + 1]
            if len(next_line.split()) <= 3 and not next_line.strip().split()[-1].isdigit():
                goods_type += " " + next_line  # Append the next line
            goods_types.append(goods_type)
    return goods_types
