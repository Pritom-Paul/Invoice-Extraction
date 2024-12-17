import re

def extract_warehouse_id(text):
    warehouse_ids = []
    lines = text.split('\n')
    for line in lines:
        # Check if the line ends with "USD USD"
        if line.strip().endswith('USD USD'):
            # Extract the first word before "USD USD"
            warehouse_id = line.split()[0]
            warehouse_ids.append(warehouse_id)
    return warehouse_ids
