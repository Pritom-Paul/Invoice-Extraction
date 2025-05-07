# import re

# def extract_exp_no(text):
#     # 1. Try standard "EXP: 123-456-789"
#     match = re.findall(r'EXP:\s*(\d+-\d+-\d+)', text, re.IGNORECASE)
#     if match:
#         return match[0]

#     # 2. Try alternative "Exp No: 1471\n003417-2025"
#     alt_match = re.search(r'Exp\s*No:\s*(\d+)[\s\n\-]*(\d+)-(\d+)', text, re.IGNORECASE)
#     if alt_match:
#         return f"{alt_match.group(1)}-{alt_match.group(2)}-{alt_match.group(3)}"

#     # 3. Handle split/malformed patterns like "EXP: 1471-\n032468-2024"
#     malformed_match = re.search(r'EXP:\s*(\d+)-\s*\n?(\d+)-(\d+)', text, re.IGNORECASE)
#     if malformed_match:
#         return f"{malformed_match.group(1)}-{malformed_match.group(2)}-{malformed_match.group(3)}"

#     return ''


import re

# Precompile regex patterns
patterns = [
    # Standard: "EXP: 123-456-789"
    re.compile(r'EXP:\s*(?P<part1>\d+)-(?P<part2>\d+)-(?P<part3>\d+)', re.IGNORECASE),
    
    # Alternate: "Exp No: 1471\n003417-2025"
    re.compile(r'Exp\s*No:\s*(?P<part1>\d+)[\s\n\-]*(?P<part2>\d+)-(?P<part3>\d+)', re.IGNORECASE),
    
    # Malformed: "EXP: 1471-\n032468-2024"
    re.compile(r'EXP:\s*(?P<part1>\d+)-\s*\n?(?P<part2>\d+)-(?P<part3>\d+)', re.IGNORECASE)
]

def extract_exp_no(text):
    for pattern in patterns:
        match = pattern.search(text)
        if match:
            return f"{match.group('part1')}-{match.group('part2')}-{match.group('part3')}"
    return ''

