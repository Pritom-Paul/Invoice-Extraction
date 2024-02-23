# About
This Python project aims to automate the extraction of data from PDF invoices, providing a structured output in tabular format. The code utilizes various extraction functions to parse essential information from each invoice, such as the invoice number, invoice date, exporter's reference, HS code, goods type, goods description, quantity, HM code, and mode of transport (MOT).

The main.py script serves as the entry point for the project. It imports functions from main_functions.py, which orchestrates the extraction process. The extracted data is then structured into a DataFrame using the Pandas library, allowing for easy manipulation and analysis.

Additionally, the project includes a csv_extraction package with csv_functions.py, facilitating the reading and writing of CSV files. This functionality enables users to save the extracted data into a CSV file for further processing or analysis.

The project is organized into separate packages (pdf_extraction, csv_extraction, and main_app) to promote modularity and maintainability. Each package contains individual scripts for specific extraction tasks, enhancing code readability and reusability.

Overall, this project streamlines the process of extracting data from PDF invoices, providing a structured output that can be easily utilized for various business applications. If you have any questions or require further assistance, feel free to reach out!
