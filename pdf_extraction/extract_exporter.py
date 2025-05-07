import re
from typing import List, Optional

def extract_exporter_from_table(tables: List[List[List[Optional[str]]]]) -> str:
    for row in tables:
        for cell in row:
            if cell and "Exporter:\n" in cell:
                # Extract content between 'Exporter:\n' and '\nSupplier:'
                match = re.search(r'Exporter:\n(.*?)\nSupplier:', cell, re.DOTALL)
                if match:
                    content = match.group(1).strip()
                    lines = content.splitlines()
                    # Remove the first line and return the rest joined
                    if len(lines) > 1:
                        return "\n".join(lines[1:]).strip()
                    else:
                        return ''
    return ''

