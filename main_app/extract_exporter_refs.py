# main_app/extract_exporter_refs.py

import os
import pandas as pd
from pdf_extraction.extract_tables_with_pdfplumber import extract_tables_with_pdfplumber

def extract_exporter_refs(directory):
    try:
        exporter_refs = []
        pdf_files = [file for file in os.listdir(directory) if file.endswith('.pdf')]
        for pdf_file in pdf_files:
            pdf_path = os.path.join(directory, pdf_file)
            tables = extract_tables_with_pdfplumber(pdf_path)
            for table in tables:
                df = pd.DataFrame(table)
                if len(df) >= 8 and any(df.iloc[7].notna()):
                    exporter_ref = df.iloc[7].values[0]
                    if 'Exporters Ref:' in exporter_ref:
                        exporter_ref = exporter_ref.replace('Exporters Ref:', '').replace('\n', ' ')
                        exporter_ref = exporter_ref.replace('Cont. No.', '')
                        exporter_refs.append(exporter_ref.strip())
        return pd.DataFrame(exporter_refs, columns=['Exporters Ref'])
    except Exception as e:
        raise Exception(f'Error occurred while extracting exporter refs from {directory}: {str(e)}')
