import re

def extract_carton(text):
    # Pattern to match numbers followed by "Cartons" (case sensitive)
    cartons = re.findall(r'\b(\d+)\s+Cartons\b', text)
    return cartons[0] if cartons else ''