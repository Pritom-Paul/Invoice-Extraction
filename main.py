# main.py
import os
import pandas as pd
from pdf_extraction.extract_text_with_pdfplumber import extract_text_with_pdfplumber
from pdf_extraction.extract_tables_with_pdfplumber import extract_tables_with_pdfplumber
from pdf_extraction.extract_fields import *
from datetime import datetime
from pdf_extraction.excel_function import save_excel

# Main function to process PDFs
directory = r'C:\Users\Altersense\Desktop\FAULTS\New folder\New folder'
def extract_pdf_data(directory):
    

    # List to store rows of data for the DataFrame
    data = []

    try:
        # Process each PDF file in the directory
        for pdf_file in os.listdir(directory):
            if pdf_file.lower().endswith(('.pdf', '.PDF')):
                pdf_path = os.path.join(directory, pdf_file)
                text = extract_text_with_pdfplumber(pdf_path)

                tables = extract_tables_with_pdfplumber(pdf_path)
                # print(f"Extracted text from {pdf_file}: {text}")
                # print(f"Extracted tables from {pdf_file}: {tables}")
                

                # Extract countries, quantities, cartons, and gross weight from the tables
                countries = extract_countries(tables)
                quantities = extract_quantities(tables)
                # print(quantities)
                cartons = extract_cartons(tables)
                gross_weight = extract_gross_weight(tables)
                contract_date = extract_contract_dates(text)
                contract_no = extract_contract_number(text)
                exp_date = extract_exp_dates(text)
                invoice_date = extract_invoice_dates(text)
                invoice_no = extract_invoice_numbers(text)
                # print(invoice_no)
                order_no = extract_order_numbers(text)
                exp_no = extract_exp_numbers(text)
                warehouse_codes = extract_warehouse_code(text)
                goods_description = extract_goods_description(text)
                # print(goods_description)
                hs_code = extract_hs_code(text)
                concern = extract_concern(text)
                # print(name)
                carrier = extract_carrier(text)
                # print(carrier)
                port_of_loading = extract_port_of_loading(text)
                # print(port_of_loading)
                total_amount = extract_total_amount(text)
                total_quantity = sum(int(q) for q in quantities if q.isdigit()) if quantities else None
                # print(f"invoice_no: {invoice_no}")
                # print(f"invoice_date: {invoice_date}")
                # print(f"exp_no: {exp_no}")
                # print(f"exp_date: {exp_date}")
                # print(f"contract_no: {contract_no}")
                # print(f"contract_date: {contract_date}")
                # print(f"order_no: {order_no}")
                # print(f"goods_description: {goods_description}")
                # print(f"hs_code: {hs_code}")
                # print(f"warehouse_codes: {warehouse_codes}")
                # print(f"countries: {countries}")
                # print(f"quantities: {quantities}")
                # print(f"cartons: {cartons}")
                # print(f"gross_weight: {gross_weight}")
                # print(f"concern: {concern}")                
                # print(f"carrier: {carrier}")
                # print(f"port_of_loading: {port_of_loading}")                
                # print(f"total_amount: {total_amount}")
                # print(f"total_quantity: {total_quantity}")
                
                # Extract the country_iso
                if '-' in warehouse_codes[0]:
                    country_iso = warehouse_codes[0].split('-')[1]
                else:
                    country_iso = countries[0] if countries else None
                    # print(f"country_iso: {country_iso}")

                # Append the extracted warehouse codes (as a list or string), goods description, HS code, and table data to the data list
                data.append({
                    # "PDF File Name": pdf_file,
                    # "Invoice No": invoice_no,
                    # "Invoice Date": invoice_date,
                    # "Exp No": exp_no, 
                    # "Exp Date": exp_date,
                    # "Contract No": contract_no,
                    # "Contract Date": contract_date,
                    # "Order No": order_no,
                    # "Goods Description": goods_description,
                    # "HS CODE": hs_code,                 
                    # "Warehouse Code": warehouse_codes,
                    # "Countries": countries,
                    # "Quantities": quantities,
                    # "Cartons": cartons,
                    # "Gross Weight": gross_weight,
                    # "Country ISO": country_iso,
                    # "Concern": concern,
                    # "Carrier": carrier,
                    # "Port of Loading": port_of_loading,
                    # "Total Amount": total_amount,
                    # "Total Quantity": total_quantity
                })

        # Convert the list of dictionaries into a DataFrame
        # df = pd.DataFrame(data)
        # print(df)

        # Save the DataFrame to an Excel file
        # output_file_path = os.path.join(directory, 'invoice_data.xlsx')
        # save_excel(df, 'invoice_data')
        # save_excel(df, output_file_path)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Entry point for the script
if __name__ == "__main__":
    extract_pdf_data(directory)