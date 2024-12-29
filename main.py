# main.py

from main_app.main_functions import extract_pdf_data, extract_exporter_refs, extract_text_with_pdfplumber
from csv_extraction.csv_functions import save_excel
import pandas as pd
import os


if __name__ == "__main__":
    directory = r'C:\Users\Altersense\Desktop\NEW\Bitopi'

    try:
        all_invoice_data = extract_pdf_data(directory)
        df = pd.DataFrame(all_invoice_data)

        # Print the text of all the pdfs
        
        # for pdf_file in os.listdir(directory):
        #     if pdf_file.lower().endswith(('.pdf', '.PDF')):
        #         pdf_path = os.path.join(directory, pdf_file)
        #         text = extract_text_with_pdfplumber(pdf_path)
        #         print(f"Text from {pdf_file}: {text}")

        # Print DataFrame to EXCEL file in the same directory
        
        # output_file_path = os.path.join(directory, 'invoice_data.xlsx')
        # save_excel(df, 'invoice_data')
        # save_excel(df, output_file_path)

        print(df.to_string(index=False))

    except Exception as e:
        print(f"An error occurred: {str(e)}")

