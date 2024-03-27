# main_app/main_functions.py

import os
import pandas as pd
import sys

# Adding the parent directory to the system path to enable imports from sibling directories
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from pdf_extraction.extract_text_with_pdfplumber import extract_text_with_pdfplumber
from pdf_extraction.extract_invoice_numbers import extract_invoice_numbers
#from pdf_extraction.extract_invoice_dates import extract_invoice_dates
from pdf_extraction.extract_hs_code import extract_hs_code
from pdf_extraction.extract_goods_type import extract_goods_type
from pdf_extraction.extract_quantity import extract_quantity
from pdf_extraction.extract_hm_code import extract_hm_code
from pdf_extraction.extract_MOT import extract_MOT
from pdf_extraction.extract_description import extract_description
from pdf_extraction.extract_goods_description import extract_goods_description
from main_app.extract_exporter_refs import extract_exporter_refs
from pdf_extraction.extract_tables_with_pdfplumber import extract_tables_with_pdfplumber


def extract_pdf_data(directory):
    try:
        pdf_files = [file for file in os.listdir(directory) if file.endswith('.pdf')]
        all_invoice_data = []
        for pdf_file in pdf_files:
            pdf_path = os.path.join(directory, pdf_file)
            text = extract_text_with_pdfplumber(pdf_path)
            invoice_numbers = extract_invoice_numbers(text)
            #invoice_dates = extract_invoice_dates(text)
            hs_codes = extract_hs_code(text)
            goods_types = extract_goods_type(text)
            quantities = extract_quantity(text)
            MOT_values = extract_MOT(text)
            goods_descriptions = extract_goods_description(text)
            hm_codes = extract_hm_code(text)
            exporter_refs = extract_exporter_refs(directory)  # Get exporter references
            for number, hs_code, goods_type, quantity, MOT, description, hm_code, exporter_ref in zip(
                    invoice_numbers, hs_codes,
                    goods_types, quantities, MOT_values, goods_descriptions, hm_codes,
                    exporter_refs['Exporters Ref']):
                all_invoice_data.append(
                    {'Invoice Number': number,'Exporters Ref': exporter_ref,
                     'HS Code': hs_code, 'Goods Type': goods_type, 'Goods Description': description,
                     'Quantity': quantity, 'HM Code': hm_code, 'MOT': MOT, 'Fcr Status': None})
        return all_invoice_data
    except Exception as e:
        raise Exception(f'Error occurred while extracting data from {directory}: {str(e)}')
