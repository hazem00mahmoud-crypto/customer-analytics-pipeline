\# Customer Analytics Pipeline - Assignment #1



\## Team Members

\- \[Hazem Mohamed]

\- \[Mohamed Tarek]

\- \[Ryad elsheimy]

\- \[Mohamed Khaled]



## Project Overview
A complete data analytics pipeline implemented using Docker containers. The system processes customer data through ingestion, preprocessing, analytics, visualization, and clustering stages.

## Pipeline Architecture
1. **Data Ingestion** (`ingest.py`) - Loads raw dataset
2. **Data Preprocessing** (`preprocess.py`) - Cleaning, transformation, dimensionality reduction
3. **Analytics** (`analytics.py`) - Generates textual insights
4. **Visualization** (`visualize.py`) - Creates correlation heatmaps
5. **Clustering** (`cluster.py`) - Applies K-means algorithm
6. **Summary** (`summary.sh`) - Collects and organizes outputs

## Technical Stack
- **Containerization:** Docker with Python 3.11-slim
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Visualization:** Matplotlib, Seaborn
- **Analysis:** Scipy

## Installation & Execution

### Build Docker Image
```bash
docker build -t customer-analytics .

