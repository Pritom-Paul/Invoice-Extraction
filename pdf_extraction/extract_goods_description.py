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
                first_line = lines[i].split()[:-3]  # Removing the last three words
                first_line = ' '.join(first_line)
                # Further clean-up for parenthesis within the first line
                first_line = first_line.split('PCS/PACK')[0].split('(')[0].split(')')[0].strip()
                # Strip double quotes if present
                if first_line.startswith('"') :
                    first_line = first_line[1:].strip()
                description_parts.append(first_line)
                i += 1

            # Process subsequent lines
            while i < len(lines) and not lines[i].startswith("Container"):
                current_line = lines[i].split('PCS/PACK')[0].split('(')[0].split(')')[0].strip()
                description_parts.append(current_line)
                i += 1
            
            description = " ".join(description_parts).strip()
            goods_descriptions.append(description)
            found_usd_usd = False
        else:
            i += 1
    return goods_descriptions
