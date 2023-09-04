import pandas as pd
import os

# Get user input
excel_file_path = input("Enter the path to the Excel file: ")
csv_directory = input("Enter the path to the output CSV directory: ")
chunk_size = int(input("Enter the chunk size: "))
csv_separator = input("Enter the CSV file separator (e.g., ',' or ';'): ")

# Get user input from environment variables
# excel_file_path = os.environ.get('excel_file_path', 'excel/Employee Sample Data_1M.xlsx')
# csv_directory = os.environ.get('csv_directory', 'csv')
# chunk_size = int(os.environ.get('chunk_size', '100000'))
# csv_separator = os.environ.get('csv_separator', ',')

host_directory = '/app/host_data'
csv_prefix = 'output_'

# Load Excel file with multiple sheets
file_path = os.path.join(host_directory, excel_file_path)
xlsx = pd.ExcelFile(file_path)

# Iterate through each sheet in the Excel file
for sheet_name in xlsx.sheet_names:
    # Load sheet into DataFrame
    df = pd.read_excel(xlsx, sheet_name)
    
    # Split DataFrame into smaller chunks to avoid memory issues
    num_chunks = len(df) // chunk_size + 1
    chunks = [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)]
    
    # Convert each chunk to CSV
    for i, chunk in enumerate(chunks):
        csv_file_path = f"{host_directory}/{csv_prefix}{sheet_name}_part{i+1}.csv"
        chunk.to_csv(csv_file_path, index=False, sep=csv_separator)
        print(f"Chunk {i+1} of {sheet_name} saved as CSV: {csv_file_path}")

