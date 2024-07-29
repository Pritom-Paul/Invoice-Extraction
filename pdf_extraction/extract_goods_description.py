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
            description_parts = []
            # Special processing for the first line after "USD USD"
            if i < len(lines):
                first_sentence = lines[i].split()[:-3]
                first_sentence = ' '.join(first_sentence)  # Preserve spaces between words
                
                # Further clean-up for parenthesis within the first sentence
                first_sentence = first_sentence.split('PCS/PACK')[0].split('(')[0].split(')')[0].strip()
                # Strip double quotes if present
                if first_sentence.startswith('"'):
                    first_sentence = first_sentence[1:].strip()
                description_parts.append(first_sentence)
                i += 1

            # Process subsequent lines
            while i < len(lines) and not lines[i].startswith("Container"):
                current_sentence = lines[i].split('PCS/PACK')[0].split('(')[0].split(')')[0].strip()
                description_parts.append(current_sentence)
                i += 1
            
            description = " ".join(description_parts).strip()
            if "Container" in description:
                description = description.split("Container")[0].strip()
            goods_descriptions.append(description)
            found_usd_usd = False
        else:
            i += 1
    return goods_descriptions
