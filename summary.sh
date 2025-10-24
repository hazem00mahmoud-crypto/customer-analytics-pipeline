#!/bin/bash
mkdir -p ../results
cp *.csv *.txt *.png ../results/
echo "Files copied to results directory:"
ls ../results/
echo "Pipeline completed successfully!"