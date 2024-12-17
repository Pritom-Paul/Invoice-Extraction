import re

def extract_to_pay(text):
    to_pay = re.findall(r'To Pay\s+(\d+\.\d{2})', text)
    if to_pay:
        return to_pay
    else:
        return ['']
