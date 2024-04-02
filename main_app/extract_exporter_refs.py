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
                    if exporter_ref.strip().lower().startswith("s/c no :".lower()) or exporter_ref.strip().lower().startswith("S/C NO:".lower()):
                        exporter_ref = exporter_ref.strip()[8:]  # Strip "s/c no :" from the start
                    exporter_refs.append(exporter_ref.strip())
        return exporter_refs
    except Exception as e:
        raise Exception(f'Error occurred while extracting exporter refs from {pdf_path}: {str(e)}')