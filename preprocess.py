import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
import sys
import os

def main():
    # Get input file from command line or use default
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'data_raw.csv'
    
    # Check if file exists
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist")
        sys.exit(1)
    
    # Load data
    df = pd.read_csv(input_file)
    print(f"Loaded data with {len(df)} rows and {len(df.columns)} columns")
    
    # 1. DATA CLEANING
    print("\n1. Data Cleaning:")
    # Handle missing values
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    
    for col in numeric_cols:
        if df[col].isnull().sum() > 0:
            df[col].fillna(df[col].median(), inplace=True)
            print(f"  - Filled missing values in {col} with median")
    
    for col in categorical_cols:
        if df[col].isnull().sum() > 0:
            df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else 'Unknown', inplace=True)
            print(f"  - Filled missing values in {col} with mode")
    
    # Remove duplicates
    initial_rows = len(df)
    df.drop_duplicates(inplace=True)
    if len(df) < initial_rows:
        print(f"  - Removed {initial_rows - len(df)} duplicate rows")
    
    # 2. FEATURE TRANSFORMATION
    print("\n2. Feature Transformation:")
    # Encode categorical columns
    label_encoders = {}
    for col in categorical_cols:
        if col != 'name':  # Don't encode names
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            label_encoders[col] = le
            print(f"  - Encoded categorical column: {col}")
    
    # Scale numeric columns
    if len(numeric_cols) > 0:
        scaler = StandardScaler()
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
        print(f"  - Scaled numeric columns: {list(numeric_cols)}")
    
    # 3. DIMENSIONALITY REDUCTION
    print("\n3. Dimensionality Reduction:")
    # Select subset of columns (remove id and name if they exist)
    columns_to_keep = [col for col in df.columns if col not in ['id', 'name']]
    df = df[columns_to_keep]
    print(f"  - Selected {len(df.columns)} features: {list(df.columns)}")
    
    # 4. DISCRETIZATION
    print("\n4. Discretization:")
    # Bin age column if it exists
    if 'age' in df.columns:
        df['age_binned'] = pd.cut(df['age'], bins=3, labels=['Young', 'Middle', 'Senior'])
        print("  - Binned 'age' into 3 categories")
    
    # Bin salary column if it exists  
    if 'salary' in df.columns:
        df['salary_binned'] = pd.cut(df['salary'], bins=3, labels=['Low', 'Medium', 'High'])
        print("  - Binned 'salary' into 3 categories")
    
    # Save processed data
    df.to_csv('data_preprocessed.csv', index=False)
    print(f"\nPreprocessed data saved as 'data_preprocessed.csv'")
    print(f"Final dataset: {len(df)} rows and {len(df.columns)} columns")
    
    return 'data_preprocessed.csv'

if __name__ == "__main__":
    output_file = main()
    print(f"\nNext script should use: {output_file}")