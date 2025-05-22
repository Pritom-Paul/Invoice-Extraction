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
from pdf_extraction.extract_carton import extract_carton
from pdf_extraction.extract_gross_weight import extract_gross_weight
from pdf_extraction.extract_port_of_loading import extract_port_of_loading
from pdf_extraction.extract_exporter import extract_exporter_from_table
from pdf_extraction.extract_exp_no import extract_exp_no

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
            try:
                text = extract_text_with_pdfplumber(pdf_path)
            except Exception as e:
                print(f"Error reading {pdf_file}: {e}")
                continue
            tables = extract_tables_with_pdfplumber(pdf_path)
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
            cartons = extract_carton(text)
            gross_weight = extract_gross_weight(text)
            port_of_loading = extract_port_of_loading(text)  
            exporter = extract_exporter_from_table(tables)
            full_exp_no = extract_exp_no(exporter_refs[0]) if exporter_refs else "N/A"
            # full_exp_no = extract_exp_no(exporter_refs['Exporters Ref'].iloc[0]) #Works for inctl

            

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
                    # 'EXPORTERS REF': exporter_ref,
                    # 'HS CODE': hs_code,
                    # 'DESCRIPTION': goods_type,
                    'COMPOSITION': description,
                    # 'QUANTITY': quantity,
                    # 'PO NO': hm_code,
                    # 'COUNTRY ISO': MOT,
                    # 'TO PAY': toPay,
                    # 'POL': POL,
                    # 'WAREHOUSE ID': warehouse_id,
                    # 'CARTONS': cartons,
                    # 'GROSS WEIGHT': gross_weight,
                    # 'PORT OF LOADING': port_of_loading,
                    # 'EXPORTER': exporter,
                    # 'EXP NO': full_exp_no,
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


# def extract_pdf_data(directory):
#     try:
#         # print(f"Processing directory: {directory}")
#         pdf_files = [file for file in os.listdir(directory) if file.lower().endswith(('.pdf', '.PDF'))]
#         # print(f"Found {len(pdf_files)} PDF files.")
        
#         all_invoice_data = []
#         valid_invoices = 0
#         invoice_filecount = 0
#         invoice_filenames = []
#         text = ""

#         for pdf_file in pdf_files:
#             try:
#                 # print(f"Processing file: {pdf_file}")
#                 pdf_path = os.path.join(directory, pdf_file)
#                 text = extract_text_with_pdfplumber(pdf_path)
#                 # print(f"Extracted text length: {len(text)} characters")

#                 invoice_numbers = extract_invoice_numbers(text)         
#                 invoice_dates = extract_invoice_dates(text)
#                 hs_codes = extract_hs_code(text)
#                 goods_types = extract_goods_type(text)
#                 quantities = extract_quantity(text)
#                 MOT_values = extract_MOT(text)
#                 goods_descriptions = extract_goods_description(text)
#                 hm_codes = extract_hm_code(text)
#                 exporter_refs = extract_exporter_refs(pdf_path)
#                 toPay = extract_to_pay(text)
#                 POL = extract_POL(text)
#                 warehouse_id = extract_warehouse_id(text)
#                 cartons = extract_carton(text)
#                 gross_weight = extract_gross_weight(text)
#                 print(f"cartons: {cartons}")
#                 print(f"gross_weight: {gross_weight}")

#                 # print(f"Extracted data for {pdf_file}:")
#                 # print(f"  Invoice Numbers: {invoice_numbers}")
#                 # print(f"  Invoice Dates: {invoice_dates}")
#                 # print(f"  HS Codes: {hs_codes}")
#                 # print(f"  Goods Types: {goods_types}")
#                 # print(f"  Quantities: {quantities}")
#                 # print(f"  MOT Values: {MOT_values}")
#                 # print(f"  Goods Descriptions: {goods_descriptions}")
#                 # print(f"  HM Codes: {hm_codes}")
#                 # print(f"  Exporter Refs: {exporter_refs}")
#                 # print(f"  To Pay: {toPay}")
#                 # print(f"  POL: {POL}")
#                 # print(f"  Warehouse ID: {warehouse_id}")

#                 if invoice_numbers:
#                     invoice_filecount += 1
#                     invoice_filenames.append(pdf_file)
#                 else:
#                     # print(f"Invalid Invoice === {pdf_file} (No invoice number found). Skipping.")
#                     continue

#                 exporter_ref = exporter_refs[0] if exporter_refs else "N/A"

#                 for number, hs_code, toPay, POL, warehouse_id, goods_type, quantity, MOT, description, hm_code in zip(
#                         invoice_numbers, hs_codes, toPay, POL, warehouse_id, goods_types, quantities, MOT_values, goods_descriptions, hm_codes):
                    
#                     # print(f"Appending data for invoice {number}")
#                     all_invoice_data.append({
#                         'INDEX': len(all_invoice_data) + 1,
#                         'INVOICE NO': number,
#                         'INVOICE DATE': invoice_dates, 
#                         'EXPORTERS REF': exporter_ref,
#                         'HS CODE': hs_code,
#                         'DESCRIPTION': goods_type,
#                         'COMPOSITION': description,
#                         'QUANTITY': quantity,
#                         'PO NO': hm_code,
#                         'COUNTRY ISO': MOT,
#                         'TO PAY': toPay,
#                         'POL': POL,
#                         'WAREHOUSE ID': warehouse_id,
#                         'CARTONS': cartons,
#                         'GROSS WEIGHT': gross_weight,
#                     })
#                     valid_invoices += 1
#                     invoice_filenames.remove(pdf_file)
#             except Exception as e:
#                 print(f"Error processing {pdf_file}: {str(e)}")
#                 continue

#         print("\nSummary of extraction:")
#         if valid_invoices == 0:
#             print("No valid invoices found in the directory.")
        
#         if invoice_filecount == valid_invoices:
#             print("All invoices have been extracted successfully.")
#         else:
#             print(f"{valid_invoices} out of {invoice_filecount} invoices have been extracted successfully.")
#             print(f"The following {len(invoice_filenames)} files could not be extracted successfully: {invoice_filenames}")

#         return all_invoice_data
#     except Exception as e:
#         raise Exception(f'Error occurred while extracting data from {directory}: {str(e)}')