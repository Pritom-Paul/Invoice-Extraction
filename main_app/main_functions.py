# main_app/main_functions.py

import os
import pandas as pd
import sys

# Adding the parent directory to the system path to enable imports from sibling directories
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from pdf_extraction.extract_text_with_pdfplumber import extract_text_with_pdfplumber
from pdf_extraction.extract_invoice_numbers import extract_invoice_numbers
from pdf_extraction.extract_invoice_dates import extract_invoice_dates
from pdf_extraction.extract_hs_code import extract_hs_code
from pdf_extraction.extract_goods_type import extract_goods_type
from pdf_extraction.extract_quantity import extract_quantity
from pdf_extraction.extract_hm_code import extract_hm_code
from pdf_extraction.extract_MOT import extract_MOT
from pdf_extraction.extract_description import extract_description
from pdf_extraction.extract_goods_description import extract_goods_description
from main_app.extract_exporter_refs import extract_exporter_refs
from pdf_extraction.extract_tables_with_pdfplumber import extract_tables_with_pdfplumber
from pdf_extraction.extract_toPay import extract_to_pay
from pdf_extraction.extract_POL import extract_POL
from pdf_extraction.extract_warehouse_id import extract_warehouse_id

def extract_pdf_data(directory):
    try:
        pdf_files = [file for file in os.listdir(directory) if file.lower().endswith(('.pdf', '.PDF'))]
        all_invoice_data = []
        valid_invoices = 0
        invoice_filecount = 0
        invoice_filenames = []
        text=""

        for pdf_file in pdf_files:
            pdf_path = os.path.join(directory, pdf_file)  # Ensure this is defined inside the loop  # Ensure this is defined inside the loop
            text = extract_text_with_pdfplumber(pdf_path)
            invoice_numbers = extract_invoice_numbers(text)
            invoice_dates = extract_invoice_dates(text)
            hs_codes = extract_hs_code(text)
            goods_types = extract_goods_type(text)
            quantities = extract_quantity(text)
            MOT_values = extract_MOT(text)
            goods_descriptions = extract_goods_description(text)
            hm_codes = extract_hm_code(text)
            exporter_refs = extract_exporter_refs(pdf_path)  # Correct use of pdf_path
            toPay=extract_to_pay(text)
            POL=extract_POL(text)
            warehouse_id=extract_warehouse_id(text)

            # Check if any invoice number is extracted
            if invoice_numbers:
                invoice_filecount += 1
                invoice_filenames.append(pdf_file)
            else:
                print(f"Invalid Invoice === {pdf_file}.")
                continue

            exporter_ref = exporter_refs[0] if exporter_refs else "N/A"

            for number, hs_code, toPay, POL, warehouse_id, goods_type, quantity, MOT, description, hm_code in zip(
                    invoice_numbers, hs_codes, toPay, POL, warehouse_id, goods_types, quantities, MOT_values, goods_descriptions, hm_codes):
                

                all_invoice_data.append({
                    'INVOICE NO': number,
                    # 'INVOICE DATE': invoice_dates, 
                    'EXPORTERS REF': exporter_ref,
                    # 'HS CODE': hs_code,
                    # 'DESCRIPTION': goods_type,
                    # 'COMPOSITION': description,
                    # 'QUANTITY': quantity,
                    # 'PO NO': hm_code,
                    # 'COUNTRY ISO': MOT,
                    # 'TO PAY': toPay,
                    # 'POL': POL,
                    # 'WAREHOUSE ID': warehouse_id,
                    # 'FCR STATUS': None
                })
                valid_invoices += 1
                invoice_filenames.remove(pdf_file)

        if valid_invoices == 0:
            print("No valid invoices found in the directory.")
        
        if invoice_filecount == valid_invoices:
            print("All invoices have been extracted successfully.")
        else:
            print(f"{valid_invoices} out of {invoice_filecount} invoices have been extracted successfully.")
            print(f"The following {len(invoice_filenames)} files could not be extracted successfully: {invoice_filenames}")


        return all_invoice_data
    except Exception as e:
        raise Exception(f'Error occurred while extracting data from {directory}: {str(e)}')

