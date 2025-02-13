import pandas as pd
import requests

# Load the CSV files
files = ["data/question_tags.csv", "data/questions.csv"]  # Replace with actual file names
count = 0

for file in files:
    try:
        # Read CSV file
        df = pd.read_csv(file, dtype=str, on_bad_lines="skip")

print("First few rows of DataFrame:")
print(df.head())  # Display first few rows
print("\nData types of each column:")
print(df.dtypes)  # Show column types

if not df.empty:
    count = df.apply(lambda row: row.astype(str).str.contains("GitHub", case=False, na=False).any(), axis=1).sum()
    print(f"\nCount of occurrences: {count}")
else:
    print("Warning: DataFrame is empty!")

# Print the total count
print(f"Total lines containing 'GitHub': {count}")

# Save the result to a text file
with open("_output/github_count.txt", "w") as f:
    f.write(f"Total lines containing 'GitHub': {count}\n")

