def extract_goods_description(text):
    goods_descriptions = []
    lines = text.split('\n')
    found_usd_usd = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if 'USD USD' in line:
            found_usd_usd = True
            i += 1
            continue
        if found_usd_usd:
            # Process first sentence to exclude any text following a parenthesis or specific patterns
            first_sentence_parts = line.split()[:-3]
            first_sentence = ' '.join(first_sentence_parts)
            if "(" in first_sentence:
                first_sentence = first_sentence.split("(")[0].strip()
            elif ")" in first_sentence:
                first_sentence = first_sentence.split(")")[0].strip()
            
            next_line = lines[i+1]
            # Adjust to handle both opening and closing parenthesis, and specific patterns in next line
            if "(" in next_line:
                next_line = next_line.split("(")[0].strip()
            elif ")" in next_line:
                next_line = next_line.split(")")[0].strip()

            # Applying PCS/PACK trimming to both first_sentence and next_line
            if "PCS/PACK" in first_sentence:
                first_sentence = first_sentence.split("PCS/PACK")[0].strip()
            if "PCS/PACK" in next_line:
                next_line = next_line.split("PCS/PACK")[0].strip()
                
            description = f"{first_sentence} {next_line}".strip()
            if "Container" in description:
                description = description.split("Container")[0].strip()
            goods_descriptions.append(description)
            found_usd_usd = False
        else:
            i += 1
    return goods_descriptions

