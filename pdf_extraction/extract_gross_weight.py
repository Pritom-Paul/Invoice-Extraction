import re
def extract_gross_weight(text):
    # Pattern to match numbers after "Gross Weight:" followed by optional spaces and "KG" (case sensitive)
    weights = re.findall(r'Gross Weight:\s*(\d+\.\d+)\s*KG', text)
    return weights[0] if weights else ''