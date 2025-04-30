# main_app/extract_exporter_refs.py

import os
import pandas as pd
import re
from pdf_extraction.extract_tables_with_pdfplumber import extract_tables_with_pdfplumber
from pdf_extraction.extract_text_with_pdfplumber import extract_text_with_pdfplumber

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
#                     exporter_ref = exporter_ref.replace('Exporters Ref:', '')
                    
#                     # Check if the exporter_ref starts with a line break and remove it if so
#                     if exporter_ref.startswith('\n'):
#                         exporter_ref = exporter_ref[1:]  # Remove the first line break
                    
#                     exporter_refs.append(exporter_ref)
#         # print(exporter_refs)
#         return exporter_refs
#     except Exception as e:
#         raise Exception(f'Error occurred while extracting exporter refs from {pdf_path}: {str(e)}')
    
    
# #option2
# def extract_exporter_refs(pdf_path):
#     try:
#         exporter_refs = []
#         tables = extract_tables_with_pdfplumber(pdf_path)
#         for i, table in enumerate(tables):
#             # print(f"Table {i+1}: {table}")  # Debugging each table
#             df = pd.DataFrame(table)
            
#             if df.empty:
#                 continue  # Skip empty tables
            
#             # Search for "Exporters Ref:" in each row
#             for index, row in df.iterrows():
#                 for cell in row:
#                     if isinstance(cell, str) and 'Exporters Ref:' in cell:
#                         exporter_ref = cell.replace('Exporters Ref:', '').strip()
#                         if exporter_ref.startswith('\n'):
#                             exporter_ref = exporter_ref[1:]  # Remove leading line breaks
#                         exporter_refs.append(exporter_ref)

#         print("Exporter References OPTION 2:", exporter_refs)  # Debug the list of extracted references
#         return exporter_refs
#     except Exception as e:
#         raise Exception(f'Error occurred while extracting exporter refs from {pdf_path}: {str(e)}')


# # Merged original and option 2
# def extract_exporter_refs(pdf_path):
#     try:
#         exporter_refs = []
#         tables = extract_tables_with_pdfplumber(pdf_path)
#         for table in tables:
#             df = pd.DataFrame(table)
#             print(df)
#             if len(df) >= 8 and any(df.iloc[7].notna()):
#                 exporter_ref = df.iloc[7].values[0]
#                 if 'Exporters Ref:' in exporter_ref:
#                     exporter_ref = exporter_ref.replace('Exporters Ref:', '')
                    
#                     # Check if the exporter_ref starts with a line break and remove it if so
#                     if exporter_ref.startswith('\n'):
#                         exporter_ref = exporter_ref[1:]  # Remove the first line break
                    
#                     exporter_refs.append(exporter_ref)
        
        
#         if exporter_refs:
#             # print("USED THE FIRST OPTION")
#             return exporter_refs  # If references found, return them
        
#         # If no references found using the first approach, try the second approach
#         exporter_refs = []
#         for i, table in enumerate(tables):
#             df = pd.DataFrame(table)
#             if df.empty:
#                 continue  # Skip empty tables

#             # Search for "Exporters Ref:" in each row
#             for index, row in df.iterrows():
#                 for cell in row:
#                     if isinstance(cell, str) and 'Exporters Ref:' in cell:
#                         exporter_ref = cell.replace('Exporters Ref:', '').strip()
#                         if exporter_ref.startswith('\n'):
#                             exporter_ref = exporter_ref[1:]  # Remove leading line breaks
#                         exporter_refs.append(exporter_ref)

#         return exporter_refs  # Return the references found by the second approach

#     except Exception as e:
#         raise Exception(f'Error occurred while extracting exporter refs from {pdf_path}: {str(e)}')

# #FOR LAILA
# def extract_exporter_refs(pdf_path):
#     try:
#         exporter_refs = []
#         tables = extract_tables_with_pdfplumber(pdf_path)
#         text = extract_text_with_pdfplumber(pdf_path)
#         print(text)
#         print(tables)
#         for table in tables:
#             df = pd.DataFrame(table)
#             if len(df) >= 8 and any(df.iloc[7].notna()):
#                 exporter_ref = df.iloc[7].values[0]
#                 if 'Exporters Ref:' in exporter_ref:
#                     exporter_ref = exporter_ref.replace('Exporters Ref:', '')
                    
#                     # Check if the exporter_ref starts with a line break and remove it if so
#                     if exporter_ref.startswith('\n'):
#                         exporter_ref = exporter_ref[1:]  # Remove the first line break
                        
#                      # Insert a line break before 'Date' and 'Exp' (ignoring case)
#                     exporter_ref = re.sub(r'(?i)(?=\b(?:Date|Exp)\b)', '\n', exporter_ref)
                    
#                     exporter_refs.append(exporter_ref)
#         # print(exporter_refs)
#             return exporter_refs
#     except Exception as e:
#         raise Exception(f'Error occurred while extracting exporter refs from {pdf_path}: {str(e)}')