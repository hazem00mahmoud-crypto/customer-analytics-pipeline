import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import os

def main():
    # Get input file from command line or use default
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'data_preprocessed.csv'
    
    # Check if file exists
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist")
        sys.exit(1)
    
    # Load data
    df = pd.read_csv(input_file)
    print(f"Loaded data with {len(df)} rows and {len(df.columns)} columns")
    
    # Set style for better looking plots
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Create a meaningful plot - Correlation Heatmap
    plt.figure(figsize=(10, 8))
    
    # Select only numeric columns for correlation
    numeric_df = df.select_dtypes(include=[np.number])
    
    if len(numeric_df.columns) > 1:
        # Create correlation matrix
        correlation_matrix = numeric_df.corr()
        
        # Create heatmap
        sns.heatmap(correlation_matrix, 
                   annot=True, 
                   cmap='coolwarm', 
                   center=0,
                   square=True,
                   fmt='.2f',
                   cbar_kws={"shrink": .8})
        
        plt.title('Feature Correlation Heatmap\n(Preprocessed Data)', fontsize=16, pad=20)
        plt.tight_layout()
        
    else:
        # If not enough numeric columns, create a histogram
        if len(numeric_df.columns) > 0:
            plt.hist(numeric_df.iloc[:, 0], bins=10, alpha=0.7, edgecolor='black')
            plt.title(f'Distribution of {numeric_df.columns[0]}', fontsize=16)
            plt.xlabel(numeric_df.columns[0])
            plt.ylabel('Frequency')
        else:
            # If no numeric columns, create a bar plot of categorical data
            categorical_cols = df.select_dtypes(include=['object']).columns
            if len(categorical_cols) > 0:
                df[categorical_cols[0]].value_counts().plot(kind='bar')
                plt.title(f'Distribution of {categorical_cols[0]}', fontsize=16)
                plt.xlabel(categorical_cols[0])
                plt.ylabel('Count')
                plt.xticks(rotation=45)
            else:
                print("No suitable columns for visualization")
                return
    
    # Save the plot
    plt.savefig('summary_plot.png', dpi=300, bbox_inches='tight')
    print("Plot saved as 'summary_plot.png'")
    
    plt.show()
    
    return 'data_preprocessed.csv'

if __name__ == "__main__":
    output_file = main()
    print(f"Next script should use: {output_file}")