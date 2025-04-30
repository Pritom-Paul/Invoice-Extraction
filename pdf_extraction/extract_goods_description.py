import re
# def extract_goods_description(text):
#     goods_descriptions = []
#     lines = text.split('\n')
#     found_usd_usd = False
#     i = 0
#     while i < len(lines):
#         line = lines[i]
#         if 'USD USD' in line:
#             found_usd_usd = True
#             i += 1
#             continue
#         if found_usd_usd:
#             description_parts = []
#             # Special processing for the first line after "USD USD"
#             if i < len(lines):
#                 words = lines[i].split()
#                 if len(words) > 3:
#                     first_sentence = ' '.join(words[:-3])  # Preserve spaces between words
#                 else:
#                     i += 1
#                     if i < len(lines):
#                         words = lines[i].split()
#                         first_sentence = ' '.join(words[:-3])  # Preserve spaces between words
                
#                 # Further clean-up for parenthesis within the first sentence
#                 first_sentence = first_sentence.split('PCS/PACK')[0].split('(')[0].split(')')[0].strip()
#                 # Strip double quotes if present
#                 if first_sentence.startswith('"'):
#                     first_sentence = first_sentence[1:].strip()
#                 description_parts.append(first_sentence)
#                 i += 1

#             # Process subsequent lines
#             while i < len(lines) and not lines[i].startswith("Container"):
#                 current_sentence = lines[i].split('PCS/PACK')[0].split('(')[0].split(')')[0].strip()
#                 description_parts.append(current_sentence)
#                 i += 1
            
#             description = " ".join(description_parts).strip()
#             if "Container" in description:
#                 description = description.split("Container")[0].strip()

#             # Trim description at the first occurrence of "cat" (case-insensitive) as a whole word
#             index_of_cat = re.search(r'\bcat\b', description, flags=re.IGNORECASE)
#             if index_of_cat:
#                 description = description[:index_of_cat.start()].strip()
#             goods_descriptions.append(description)
#             found_usd_usd = False
#         else:
#             i += 1
#     return goods_descriptions


# #AKH

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
                words = lines[i].split()
                if len(words) > 3:
                    first_sentence = ' '.join(words[:-3])  # Preserve spaces between words
                else:
                    i += 1
                    if i < len(lines):
                        words = lines[i].split()
                        first_sentence = ' '.join(words[:-3])  # Preserve spaces between words
                
                # Further clean-up for parenthesis within the first sentence
                first_sentence = first_sentence.split('PCS/PACK')[0].split('(')[0].split(')')[0].strip()
                # Strip double quotes if present
                if first_sentence.startswith('"'):
                    first_sentence = first_sentence[1:].strip()

                # If the first line ends with "-", join it with the next line
                if first_sentence.endswith('-'):
                    i += 1
                    if i < len(lines):
                        first_sentence = first_sentence[:-1] + lines[i].strip()  # Remove "-" and join the next line

                # Check if the next sentence doesn't start with a number
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    if not next_line[0].isdigit():  # If next line does not start with a number
                        first_sentence += " " + next_line  # Add it to the first sentence

                description_parts.append(first_sentence)
                i += 1

            # Process subsequent lines
            while i < len(lines) and not lines[i].startswith("Container"):
                current_sentence = lines[i].split('PCS/PACK')[0].split('(')[0].split(')')[0].strip()
                description_parts.append(current_sentence)
                i += 1
            
            # Join all parts, adding line breaks in between where applicable
            description = "\n".join(description_parts).strip()
            if "Container" in description:
                description = description.split("Container")[0].strip()

            # Trim description at the first occurrence of "cat" (case-insensitive) as a whole word
            index_of_cat = re.search(r'\bcat\b', description, flags=re.IGNORECASE)
            if index_of_cat:
                description = description[:index_of_cat.start()].strip()
            
            # Trim description at the first occurrence of the "Pack = Pcs" pattern
            index_of_pack = re.search(r'\b\d+\s*Pack\s*=\s*\d+\s*Pcs\b', description, flags=re.IGNORECASE)
            if index_of_pack:
                description = description[:index_of_pack.start()].strip()

            goods_descriptions.append(description)
            found_usd_usd = False
        else:
            i += 1
    return goods_descriptions
