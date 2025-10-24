import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
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
    
    # Select numeric features for clustering
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    if len(numeric_cols) < 2:
        print("Not enough numeric features for clustering")
        # Use all columns if not enough numeric ones
        X = df.values
    else:
        # Use only numeric columns
        X = df[numeric_cols].values
    
    # Apply K-Means clustering
    print("Applying K-Means clustering...")
    
    # Determine optimal number of clusters (max 3 for small dataset)
    n_clusters = min(3, len(X))
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(X)
    
    # Add cluster labels to dataframe
    df['cluster'] = clusters
    
    # Count samples per cluster
    cluster_counts = df['cluster'].value_counts().sort_index()
    
    # Save cluster counts to file
    with open('clusters.txt', 'w') as f:
        f.write("K-Means Clustering Results\n")
        f.write("==========================\n")
        f.write(f"Number of clusters: {n_clusters}\n")
        f.write(f"Total samples: {len(df)}\n\n")
        f.write("Samples per cluster:\n")
        for cluster_num, count in cluster_counts.items():
            f.write(f"Cluster {cluster_num}: {count} samples\n")
        
        f.write(f"\nCluster distribution:\n")
        f.write(str(cluster_counts))
    
    print(f"Clustering completed with {n_clusters} clusters")
    print("Cluster results saved to 'clusters.txt'")
    
    # Print cluster summary
    print("\nCluster distribution:")
    for cluster_num, count in cluster_counts.items():
        print(f"Cluster {cluster_num}: {count} samples")
    
    return 'data_preprocessed.csv'

if __name__ == "__main__":
    output_file = main()
    print(f"Next script should use: {output_file}")