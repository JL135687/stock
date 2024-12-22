import os

# Check current working directory
print("Current Working Directory:", os.getcwd())

# Check if the file exists in this directory
EXCEL_FILE = "Components.xlsx"
if not os.path.exists(EXCEL_FILE):
    print(f"Error: '{EXCEL_FILE}' not found in the current directory!")
