# pdf_extraction/extract_description.py

import re

def extract_description(text):
    descriptions = []
    lines = text.split('\n')
    pattern = r'USD\s+USD\s+(.*?)$'
    for i, line in enumerate(lines):
        match = re.search(pattern, line)
        if match:
            description = match.group(1)
            descriptions.append(description)
    return descriptions
