import sys
import pandas as pd
import os

def main():
    # Check if file path is provided as command-line argument
    if len(sys.argv) < 2:
        print("Error: Please provide the dataset file path as an argument")
        print("Usage: python ingest.py <dataset_file_path>")
        sys.exit(1)
    
    # Get the file path from command-line argument
    file_path = sys.argv[1]
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist")
        sys.exit(1)
    
    try:
        # Load the dataset (supports CSV, Excel, JSON)
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file_path)
        elif file_path.endswith('.json'):
            df = pd.read_json(file_path)
        else:
            # Try reading as CSV by default
            df = pd.read_csv(file_path)
        
        # Save as data_raw.csv
        df.to_csv('data_raw.csv', index=False)
        print(f"Dataset loaded successfully from '{file_path}'")
        print(f"Raw data saved as 'data_raw.csv' with {len(df)} rows and {len(df.columns)} columns")
        
        # Return the path for the next script
        return 'data_raw.csv'
        
    except Exception as e:
        print(f"Error loading dataset: {e}")
        sys.exit(1)

if __name__ == "__main__":
    output_file = main()
    print(f"Next script should use: {output_file}")