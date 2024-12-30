# main.py
import os
import pandas as pd
from pdf_extraction.extract_text_with_pdfplumber import extract_text_with_pdfplumber
from pdf_extraction.extract_tables_with_pdfplumber import extract_tables_with_pdfplumber
from pdf_extraction.extract_fields import *
from datetime import datetime
from pdf_extraction.excel_function import save_excel

# Main function to process PDFs
directory = r'C:\Users\Altersense\Desktop\NEW\Bitopi'
def extract_invoices(directory):
    

    # List to store rows of data for the DataFrame
    data = []

    try:
        # Process each PDF file in the directory
        for pdf_file in os.listdir(directory):
            if pdf_file.lower().endswith(('.pdf', '.PDF')):
                pdf_path = os.path.join(directory, pdf_file)
                text = extract_text_with_pdfplumber(pdf_path)

                tables = extract_tables_with_pdfplumber(pdf_path)
                # print(f"Tables from {pdf_file}: {tables}")
                

                # Extract countries, quantities, cartons, and gross weight from the tables
                countries = extract_countries(tables)
                quantities = extract_quantities(tables)
                cartons = extract_cartons(tables)
                gross_weight = extract_gross_weight(tables)
                contract_date = extract_contract_dates(text)
                contract_no = extract_contract_number(text)
                exp_date = extract_exp_dates(text)
                invoice_date = extract_invoice_dates(text)
                invoice_no = extract_invoice_numbers(text)
                order_no = extract_order_numbers(text)
                exp_no = extract_exp_numbers(text)
                warehouse_codes = extract_warehouse_code(text)
                goods_description = extract_goods_description(text)
                hs_code = extract_hs_code(text)

                # Append the extracted warehouse codes (as a list or string), goods description, HS code, and table data to the data list
                data.append({
                    "PDF File Name": pdf_file,
                    "Invoice No": invoice_no,
                    "Invoice Date": invoice_date,
                    "Exp No": exp_no, 
                    "Exp Date": exp_date,
                    "Contract No": contract_no,
                    "Contract Date": contract_date,
                    "Order No": order_no,
                    "Goods Description": goods_description,
                    "HS CODE": hs_code,                 
                    "Warehouse Code": warehouse_codes,
                    "Countries": countries,
                    "Quantities": quantities,
                    "Cartons": cartons,
                    "Gross Weight": gross_weight,
                })

        # Convert the list of dictionaries into a DataFrame
        df = pd.DataFrame(data)
        print(df)

        # Save the DataFrame to an Excel file
        # output_file_path = os.path.join(directory, 'invoice_data.xlsx')
        # save_excel(df, 'invoice_data')
        # save_excel(df, output_file_path)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Entry point for the script
if __name__ == "__main__":
    extract_invoices(directory)