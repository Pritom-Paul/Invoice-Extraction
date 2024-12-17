# main_app/extract_exporter_refs.py

import os
import pandas as pd
from pdf_extraction.extract_tables_with_pdfplumber import extract_tables_with_pdfplumber

def extract_exporter_refs(pdf_path):
    try:
        exporter_refs = []
        tables = extract_tables_with_pdfplumber(pdf_path)
        for table in tables:
            df = pd.DataFrame(table)
            if len(df) >= 8 and any(df.iloc[7].notna()):
                exporter_ref = df.iloc[7].values[0]
                if 'Exporters Ref:' in exporter_ref:
                    exporter_ref = exporter_ref.replace('Exporters Ref:', '').replace('\n', ' ')
                    exporter_ref = exporter_ref.replace('Cont. No.', '')
                    exporter_ref = exporter_ref.strip()
                    if exporter_ref.lower().startswith("s/c no :".lower()) or exporter_ref.lower().startswith("S/C NO:".lower()):
                        exporter_ref = exporter_ref[8:].strip()  # Strip "s/c no :" from the start
                    if exporter_ref.lower().startswith("s/c: inctl".lower()) or exporter_ref.lower().startswith("s/c:inctl".lower()):  
                        exporter_ref = exporter_ref[4:].strip()  # Strip "S/C:" from the start when it's concatenated or spaced
                    exporter_refs.append(exporter_ref)
        # print(exporter_refs)
        return exporter_refs
    except Exception as e:
        raise Exception(f'Error occurred while extracting exporter refs from {pdf_path}: {str(e)}')
    

    
#FOR LAILA
# def extract_exporter_refs(pdf_path):
#     try:
#         exporter_refs = []
#         tables = extract_tables_with_pdfplumber(pdf_path)
#         for table in tables:
#             df = pd.DataFrame(table)
#             if len(df) >= 8 and any(df.iloc[7].notna()):
#                 exporter_ref = df.iloc[7].values[0]
#                 if 'Exporters Ref:' in exporter_ref:
#                     exporter_ref = exporter_ref.replace('Exporters Ref:', '').replace('\n', ' ')
#                     exporter_ref = exporter_ref.replace('Cont. No.', '')
#                     exporter_ref = exporter_ref.strip()
#                     if exporter_ref.lower().startswith("s/c no :".lower()) or exporter_ref.lower().startswith("S/C NO:".lower()):
#                         exporter_ref = exporter_ref[8:].strip()  # Strip "s/c no :" from the start
#                     if exporter_ref.lower().startswith("s/c: inctl".lower()) or exporter_ref.lower().startswith("s/c:inctl".lower()):  
#                         exporter_ref = exporter_ref[4:].strip()  # Strip "S/C:" from the start when it's concatenated or spaced
                    
#                     # Get the first word (or identifier) before the first space
#                     exporter_ref = exporter_ref.split()[0]  # This takes the first part of the string before any space
                    
#                     exporter_refs.append(exporter_ref)
        
#         print(exporter_refs)
#         return exporter_refs
#     except Exception as e:
#         raise Exception(f'Error occurred while extracting exporter refs from {pdf_path}: {str(e)}')


# #FOR AKH
# def extract_exporter_refs(pdf_path):
#     try:
#         exporter_refs = []
#         tables = extract_tables_with_pdfplumber(pdf_path)
#         for table in tables:
#             df = pd.DataFrame(table)
#             if len(df) >= 8 and any(df.iloc[7].notna()):
#                 exporter_ref = df.iloc[7].values[0]
#                 if 'Exporters Ref:' in exporter_ref:
#                     exporter_ref = exporter_ref.replace('Exporters Ref:', '').replace('\n', '')
#                     exporter_refs.append(exporter_ref)
#         # print(exporter_refs)
#         return exporter_refs
#     except Exception as e:
#         raise Exception(f'Error occurred while extracting exporter refs from {pdf_path}: {str(e)}')