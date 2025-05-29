
# ##DEBUG

# def extract_pdf_data(directory):
#     # List to store rows of data for the DataFrame
#     all_invoice_data = []
#     valid_invoices = 0
#     invoice_filecount = 0
#     total_pdf = 0
#     invoice_filenames = []

#     try:
#         print(f"Starting PDF processing in directory: {directory}")
#         pdf_files = [file for file in os.listdir(directory) if file.lower().endswith(('.pdf', '.PDF'))]
#         total_pdf = len(pdf_files)
#         print(f"Total number of pdf files: {total_pdf}")
        
#         for pdf_file in pdf_files:
#             print(f"\nProcessing file: {pdf_file}")
#             try:
#                 if pdf_file.lower().endswith(('.pdf', '.PDF')):  # Ensures the file is a PDF
#                     pdf_path = os.path.join(directory, pdf_file)
#                     print(f"Extracting text from: {pdf_path}")
#                     text = extract_text_with_pdfplumber(pdf_path)
#                     print(f"Extracting tables from: {pdf_path}")
#                     tables = extract_tables_with_pdfplumber(pdf_path)
                    
#                     # Extract data with debug prints
#                     countries = extract_countries(tables)
#                     print(f"Countries extracted: {countries}")
                    
#                     quantities = extract_quantities(tables)
#                     print(f"Quantities extracted: {quantities}")
                    
#                     cartons = extract_cartons(tables)
#                     print(f"Cartons extracted: {cartons}")
                    
#                     gross_weight = extract_gross_weight(tables)
#                     print(f"Gross weight extracted: {gross_weight}")
                    
#                     contract_date = extract_contract_dates(text)
#                     print(f"Contract date extracted: {contract_date}")
                    
#                     contract_no = extract_contract_number(text)
#                     print(f"Contract number extracted: {contract_no}")
                    
#                     exp_date = extract_exp_dates(text)
#                     print(f"Exp date extracted: {exp_date}")
                    
#                     invoice_date = extract_invoice_dates(text)
#                     print(f"Invoice date extracted: {invoice_date}")
                    
#                     invoice_no = extract_invoice_numbers(text)
#                     print(f"Invoice number extracted: {invoice_no}")
        
#                     order_no = extract_order_numbers(text)
#                     print(f"Order number extracted: {order_no}")

#                     exp_no = extract_exp_numbers(text)
#                     print(f"Exp number extracted: {exp_no}")
                    
#                     warehouse_codes = extract_warehouse_code(text)
#                     print(f"Warehouse codes extracted: {warehouse_codes}")
                    
#                     goods_description = extract_goods_description(text)
#                     print(f"Goods description extracted: {goods_description}")
            
#                     hs_code = extract_hs_code(text)
#                     print(f"HS code extracted: {hs_code}")
                    
#                     concern = extract_concern(text)
#                     print(f"Concern extracted: {concern}")
                    
#                     total_amount = extract_total_amount(text)
#                     print(f"Total amount extracted: {total_amount}")
                    
#                     carrier = extract_carrier(text)
#                     print(f"Carrier extracted: {carrier}")
                    
#                     port_of_loading = extract_port_of_loading(text)
#                     print(f"Port of loading extracted: {port_of_loading}")
                    
#                     request_id = str(uuid.uuid4())
                    
#                     total_quantity = sum(int(q) for q in quantities if q.isdigit()) if quantities else None
#                     print(f"Total quantity calculated: {total_quantity}")
                    
#                     # Extract the country_iso
#                     if warehouse_codes and warehouse_codes[0]:
#                         if '-' in warehouse_codes[0]:
#                             country_iso = warehouse_codes[0].split('-')[1]
#                         else:
#                             country_iso = countries[0] if countries else None
#                     else:
#                         country_iso = countries[0] if countries else None
                                                       
#                     country_iso_dict = {
#                         'AUW118': 'AU',
#                         'AUW270': 'OO',
#                         'JPW053': 'JP',
#                         'JPW171': 'OJ',
#                         'KRW057': 'KR',
#                         'KRW0183': 'OK',
#                     }
                    
#                     if warehouse_codes and warehouse_codes[0] in country_iso_dict:
#                         country_iso = country_iso_dict[warehouse_codes[0]]
#                         print(f"Updated country ISO from dict: {country_iso}")
                    
#                     # Check if any invoice number is extracted
#                     if invoice_no:
#                         invoice_filecount += 1
#                         invoice_filenames.append(pdf_file)
#                         print("Invoice filenames before process: ", invoice_filenames)
#                     else:
#                         print(f"No invoice number found in {pdf_file}")
#                         create_bot_activity_log(ActivityLogSchema(
#                             activity_type='Invoice Extraction', activity=f'{pdf_file} is not valid', request_id='fcr_bot'))
#                         continue

#                     # Append extracted data to the list
#                     print("Appending extracted data...")
#                     all_invoice_data.append({
#                         "invoice_no": invoice_no,
#                         "invoice_date": invoice_date,
#                         "exp_no": exp_no, 
#                         "exp_date": exp_date,
#                         "contract_no": contract_no,
#                         "contract_date": contract_date,
#                         "order_no": order_no,
#                         "goods_description": goods_description,
#                         "hs_code": hs_code,                 
#                         "warehouse_codes": warehouse_codes,
#                         "sku": country_iso,
#                         "countries": countries,
#                         "quantities": quantities,
#                         "cartons": cartons,
#                         "gross_weight": gross_weight,
#                         "concern": concern,
#                         "total_amount": total_amount,
#                         "total_quantity": total_quantity,
#                         "carrier": carrier,
#                         "port_of_loading": port_of_loading,
#                         'fcr_status': None,
#                         'request_id': request_id
#                     })
#                     valid_invoices += 1
#                     print(f"Successfully processed {pdf_file}. Valid invoices count: {valid_invoices}")

#                     if invoice_filecount == valid_invoices:
#                         create_bot_activity_log(ActivityLogSchema(
#                             activity_type='Invoice Extraction', activity=f'Invoice {pdf_file} has been extracted successfully.', request_id=request_id))
#                 else:
#                     print(f"Skipping non-PDF file: {pdf_file}")

#             except Exception as e:
#                 print(f"Error processing file {pdf_file}: {str(e)}")
#                 raise

#         # Logging based on the number of invoices successfully extracted
#         print("\nProcessing summary:")
#         print(f"Total PDFs: {total_pdf}, Valid invoices: {valid_invoices}")
        
#         if valid_invoices == 0:
#             print("No valid invoices found")
#             create_bot_activity_log(ActivityLogSchema(
#                 activity_type='Invoice Extraction', activity=f'Data from the invoices could not be extracted.', request_id='fcr'))

#         if valid_invoices == total_pdf:
#             print("All invoices processed successfully")
#             create_bot_activity_log(ActivityLogSchema(
#                 activity_type='Invoice Extraction', activity=f'All {total_pdf} invoices have been extracted successfully. Request ID: {request_id}', request_id='fcr'))
#         else:
#             print(f"Partial processing: {valid_invoices}/{total_pdf} succeeded")
#             create_bot_activity_log(ActivityLogSchema(
#                 activity_type='Invoice Extraction', activity=f'Out of {total_pdf} invoices, {valid_invoices} have been extracted successfully. The following invoices could not be extracted: {invoice_filenames}', request_id='fcr'))
        
#         print("Attempting to map data...")
#         try:
#             mapped_data = map_bl(all_invoice_data)
#             print("Data mapping successful")
#             return mapped_data
#         except Exception as e:
#             print(f"Error in map_bl: {str(e)}")
#             return False

#     except Exception as e:
#         print(f"Fatal error in extract_pdf_data: {str(e)}")
#         raise Exception(f'Error occurred while extracting data from {directory}: {str(e)}')