# main_app/extract_exporter_refs.py

import os
import pandas as pd
from pdf_extraction.extract_tables_with_pdfplumber import extract_tables_with_pdfplumber

def extract_exporter_refs(directory):
    exporter_refs = []
    pdf_files = [file for file in os.listdir(directory) if file.endswith('.pdf')]
    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)
        tables = extract_tables_with_pdfplumber(pdf_path)
        for table in tables:
            df = pd.DataFrame(table)
            if len(df) >= 8 and any(df.iloc[7].notna()):
                exporter_ref = df.iloc[7].values[0]  # Extracting the value from the 8th row
                if 'Exporters Ref:' in exporter_ref:
                    exporter_ref = exporter_ref.replace('Exporters Ref:', '').replace('\n', ' ')  # Remove 'Exporters Ref:' and replace newline characters with spaces
                    exporter_ref = exporter_ref.replace('Cont. No.', '')  # Remove 'Cont. No.'
                    exporter_refs.append(exporter_ref.strip())  # Strip any leading/trailing spaces
    return pd.DataFrame(exporter_refs, columns=['Exporters Ref'])
