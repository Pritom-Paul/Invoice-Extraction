# main.py

from main_app.main_functions import extract_pdf_data, extract_exporter_refs
from csv_extraction.csv_functions import save_excel
import pandas as pd

if __name__ == "__main__":
    directory = r'C:\Users\pc\Desktop\Invoice-Extraction\Invoices'

    try:
        all_invoice_data = extract_pdf_data(directory)
        df = pd.DataFrame(all_invoice_data)

        exporter_refs_df = extract_exporter_refs(directory)

        df['Exporters Ref'] = exporter_refs_df['Exporters Ref']

        # Print DataFrame to CSV file in the same directory
        save_excel(df, 'invoice_data')

    except Exception as e:
        print(f"An error occurred: {str(e)}")

