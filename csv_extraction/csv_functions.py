# csv_extraction/csv_functions.py

import pandas as pd
import os

def save_csv(df, filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_dir, filename)
    df.to_csv(output_path, index=False)
