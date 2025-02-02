
import re
from datetime import datetime


# Function to extract warehouse codes
def extract_warehouse_code(text):
    lines = text.splitlines()
    warehouse_codes = []  # List to store warehouse codes for each PDF

    # Search for the line that ends with "US$"
    for i, line in enumerate(lines):
        if line.strip().endswith("US$"):
            # The next line contains the warehouse code
            next_line = lines[i + 1].strip()
        
            # Extract the first word from the next line (the warehouse code)
            warehouse_code = next_line.split()[0]
            warehouse_codes.append(warehouse_code)
        
            # Now check subsequent lines, extracting the warehouse code until we find a line starting with "TOTAL"
            for j in range(i + 2, len(lines)):
                next_line = lines[j].strip()
                if next_line.startswith("TOTAL"):
                    break  # Stop when a line starts with "TOTAL"
                # If the line doesn't start with "TOTAL", get the first word (warehouse code)
                warehouse_code = next_line.split()[0]
                warehouse_codes.append(warehouse_code)
        
            break  # Stop after processing the first line that ends with "US$"

    return warehouse_codes  # Return list of warehouse codes


# Function to extract goods description
# def extract_goods_description(text):
#     lines = text.splitlines()

#     # Search for the line containing "Total Amount"
#     for i, line in enumerate(lines):
#         if "Total Amount" in line:
#             # The next line contains the order number and the description
#             next_line = lines[i + 1].strip()  # Get the line immediately after "Total Amount"
            
#             # Extract the goods description which is between the start of the line and the first full stop
#             description_match = re.search(r"([A-Za-z\s]+)(?=\.)", next_line)
            
#             if description_match:
#                 description = description_match.group(1).strip()
#                 return description
#             else:
#                 return "No goods description found."
#             break  # Stop after processing the first "Total Amount" line
#     return "'Total Amount' not found in the text."


# Function to extract goods description
import re

def extract_goods_description(text):
    lines = text.splitlines()

    # Search for the line containing "Total Amount"
    for i, line in enumerate(lines):
        if "Total Amount" in line:
            # The next line contains the order number and the description
            next_line = lines[i + 1].strip() if i + 1 < len(lines) else ""
            
            # First attempt: Extract the goods description which is between the start of the line and the first full stop
            description_match = re.search(r"([A-Za-z\s\-&]+)(?=\.)", next_line)
            
            if description_match:
                description = description_match.group(1).strip()
                return description
            else:
                # Second attempt: If no full stop, match until the first number or dollar sign
                description_match_alt = re.search(r"([A-Za-z\s\-&]+)(?=\s\d|\s\$)", next_line)
                
                if description_match_alt:
                    description = description_match_alt.group(1).strip()
                    return description
                else:
                    return ""  # Return empty string if neither pattern matches
            break  # Stop after processing the first "Total Amount" line
    return "'Total Amount' not found in the text."

# Function to extract HS CODE
def extract_hs_code(text):

    # Search for the HS CODE pattern
    hs_code_match = re.search(r"HS CODE\.\s*(\d+)", text)

    # If an HS CODE is found
    if hs_code_match:
        hs_code = hs_code_match.group(1)
        return hs_code
    else:
        return ''
    
# Function to extract countries from tables
def extract_countries(tables):
    countries = []  # List to store country values
    for table in tables:
        if table:
            countries.append(table[1])  # table[1] corresponds to 'Country' column
            
    # Trim the first value if it's 'Country'
    if countries and countries[0] == 'Country':
        countries.pop(0)
        
    # return ', '.join(countries) if countries else None  # Join countries with comma
    return countries

# Function to extract quantities from tables
def extract_quantities(tables):
    quantities = []  # List to store quantity values
    for table in tables:
        if table:
            quantities.append(table[2])  # table[2] corresponds to 'Quantity' column
            
    # Trim the first value if it's 'Quantity'
    if quantities and quantities[0] == 'Quantity':
        quantities.pop(0)
        
    # return ', '.join(quantities) if quantities else None  # Join quantities with comma
    return quantities

# Function to extract cartons from tables
def extract_cartons(tables):
    cartons = []  # List to store carton values
    for table in tables:
        if table:
            cartons.append(table[3])  # table[3] corresponds to 'Cartons' column
            
    # Trim the first value if it's 'Carton'
    if cartons and cartons[0] == 'Carton':
        cartons.pop(0)
        
    # return ', '.join(cartons) if cartons else None  # Join cartons with comma
    return cartons

# Function to extract gross weight from tables
def extract_gross_weight(tables):
    gross_wt = []  # List to store gross weight values
    for table in tables:
        if table:
            gross_wt.append(table[5])  # table[5] corresponds to 'Gross Weight' column
            
    # Trim the first value if it's 'Gross Wt.\nKGS'
    if gross_wt and gross_wt[0] == 'Gross Wt.\nKGS':
        gross_wt.pop(0)
        
    # return ', '.join(gross_wt) if gross_wt else None  # Join gross weight with comma
    return gross_wt  

def extract_contract_dates(text):
    # Update the regex to also capture dates in DD.MM.YYYY format
    pattern = re.findall(r'(?i)Date\s*[:\-]?\s*(\d{2}\.\d{2}\.\d{4})', text)

    dates = pattern
    if dates:
        contract_date = dates[2]
        try:
            contract_date = datetime.strptime(contract_date, '%d.%m.%Y')
        except ValueError:
            print(f"Error in converting date: {contract_date}")
            return None
       
        # print(contract_date.strftime('%Y-%m-%d'))
        return contract_date.strftime('%Y-%m-%d')
    else:
        return None
    
# Function to extract contract number
def extract_contract_number(text):
    contract_no = re.findall(r'Contract No\.\s*[:\-]?\s*([A-Za-z0-9\/\-\&]+)', text)
    return contract_no[0]

# Function to extract exp date
def extract_exp_dates(text):
    # Update the regex to also capture dates in DD.MM.YYYY format
    pattern = re.findall(r'(?i)Date\s*[:\-]?\s*(\d{2}\.\d{2}\.\d{4})', text)

    dates = pattern
    if dates:
        exp_date = dates[1]
        try:
            exp_date = datetime.strptime(exp_date, '%d.%m.%Y')
        except ValueError:
            print(f"Error in converting date: {exp_date}")
            return None
       
        # print(exp_date.strftime('%Y-%m-%d'))
        return exp_date.strftime('%Y-%m-%d')
    else:
        return None

# Function to extract exp number 
def extract_exp_numbers(text):
    exp_no = re.findall(r'Exp\. No\.\s*[:\-]?\s*([A-Za-z0-9\-]+)', text)
    return exp_no[0]

# Function to extract invoice date
def extract_invoice_dates(text):
    # Update the regex to also capture dates in DD.MM.YYYY format
    pattern = re.findall(r'(?i)Date\s*[:\-]?\s*(\d{2}\.\d{2}\.\d{4})', text)

    dates = pattern
    if dates:
        invoice_date = dates[0]
        try:
            invoice_date = datetime.strptime(invoice_date, '%d.%m.%Y')
        except ValueError:
            print(f"Error in converting date: {invoice_date}")
            return None
       
        # print(invoice_date.strftime('%Y-%m-%d'))
        return invoice_date.strftime('%Y-%m-%d')
    else:
        return None

# Function to extract invoice number
def extract_invoice_numbers(text):
    invoice_numbers = re.findall(r'Invoice No\.\s*:\s*(\d+)', text)
    # print(invoice_numbers)
    return invoice_numbers[0]

def extract_order_numbers(text):
    # Split the text into lines
    lines = text.splitlines()

    # Search for the line containing "Total Amount"
    for i, line in enumerate(lines):
        if "Total Amount" in line:
            # The next line contains the order number
            next_line = lines[i + 1].strip()  # Get the line immediately after "Total Amount"
        
            # Capture the order number from the next line
            order_number_match = re.match(r"(\d{6}-\d{4})", next_line)
        
            if order_number_match:
                # print(f"Order Number: {order_number_match.group(1)}")
                return order_number_match.group(1)
            else:
                print("No order number found in the line after 'Total Amount'.")
            break  # Stop after processing the first "Total Amount" line
        

def extract_concern(text):
    lines = text.splitlines()
    concern = lines[0].strip()
    concern = concern.split(" ")[0]
    concern = concern.upper()
    return concern

def extract_carrier(text):
    # First attempt: Matching "Carrier : By <CarrierName>"
    match = re.search(r'Carrier\s*:\s*By\s+([\w-]+)', text, re.IGNORECASE)
    
    if match:
        return match.group(1)
    
    # Second attempt: Matching "Carrier : <CarrierName>"
    match = re.search(r'Carrier\s*:\s*([\w-]+)', text, re.IGNORECASE)
    
    return match.group(1) if match else None

def extract_port_of_loading(text):
    # First attempt: Matching "Port of Loading : <PortName>, <Country>"
    match = re.search(r'Port of Loading\s*:\s*([\w\s]+),', text, re.IGNORECASE)
    
    if match:
        return match.group(1).strip() 
    else:
        return None
