# pdf_extraction/extract_MOT.py

import re

def extract_MOT(text):
    MOT_values = re.findall(r'([A-Z]{2})\nPort of Loading:', text)
    return MOT_values
