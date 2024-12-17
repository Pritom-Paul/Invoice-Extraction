import re

def extract_POL(text):
    terms_payment_values = re.findall(r'Terms of Payment:\s*(\S+)', text)
    if terms_payment_values:
        return terms_payment_values
    else:
        return ['']