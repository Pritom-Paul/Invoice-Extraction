import re

def extract_port_of_loading(text):
    match = re.search(r'Terms of Payment:\s*\n\s*(\S+)', text)
    return match.group(1) if match else ''