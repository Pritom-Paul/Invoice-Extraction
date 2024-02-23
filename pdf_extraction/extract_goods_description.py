# pdf_extraction/extract_goods_description.py

def extract_goods_description(text):
    goods_descriptions = []
    lines = text.split('\n')
    found_usd_usd = False
    for i, line in enumerate(lines):
        if 'USD USD' in line:
            found_usd_usd = True
            continue
        if found_usd_usd:
            first_sentence = line.split()[:-3]
            first_sentence = ' '.join(first_sentence)
            next_line = lines[i+1]
            description = f"{first_sentence} {next_line}"
            goods_descriptions.append(description)
            found_usd_usd = False
    return goods_descriptions
