#!/bin/bash

# Navigate to the dataset directory
cd ~/assignment-01-CassieLu0/_output

# Count occurrences of 'python' in CSV files (case insensitive)
count=$(grep -i "python" question_tags.csv questions.csv | wc -l)

# Print the result
echo "Number of lines containing 'python' in CSV files: $count"
