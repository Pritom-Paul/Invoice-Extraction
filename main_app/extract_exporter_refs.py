# main_app/extract_exporter_refs.py

import os
import pandas as pd
from pdf_extraction.extract_tables_with_pdfplumber import extract_tables_with_pdfplumber

def extract_exporter_refs(pdf_path):
    try:
        exporter_refs = []
        tables = extract_tables_with_pdfplumber(pdf_path)
        # # Print Tables in a Readable Format
        # for i, table in enumerate(tables):
        #     print(f"Table {i+1}:")
        #     print(pd.DataFrame(table).to_string(index=False, header=False))
        #     print()
        for table in tables:
            df = pd.DataFrame(table)
            if len(df) >= 8 and any(df.iloc[7].notna()):
                exporter_ref = df.iloc[7].values[0]
                if 'Exporters Ref:' in exporter_ref:
                    exporter_ref = exporter_ref.replace('Exporters Ref:', '').replace('\n', '')
                    exporter_refs.append(exporter_ref)
        # print(exporter_refs)
        return exporter_refs
    except Exception as e:
        raise Exception(f'Error occurred while extracting exporter refs from {pdf_path}: {str(e)}')





# # Print Tables in a Readable Format
# for i, table in enumerate(tables):
#     print(f"Table {i+1}:")
#     print(pd.DataFrame(table).to_string(index=False, header=False))
#     print()