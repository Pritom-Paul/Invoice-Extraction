# csv_extraction/csv_functions.py

import pandas as pd
import os

def save_excel(df, filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_dir, f'{filename}.xlsx')
    df.to_excel(output_path, index=False)
    print(f"The Excel file has been saved in the csv_extraction directory as '{filename}.xlsx'")

