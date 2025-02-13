import pandas as pd

# Define CSV files to process
files = ["question_tags.csv", "questions.csv"]
count = 0
chunk_size = 50000  # Read 50,000 rows at a time for efficiency

# Function to count occurrences of "GitHub" in chunks
def count_github_in_csv(file):
    local_count = 0
    try:
        for chunk in pd.read_csv(file, encoding="utf-8", low_memory=False, chunksize=chunk_size):
            # Vectorized string search across all columns
            local_count += chunk.astype(str).apply(lambda col: col.str.contains("GitHub", case=False, na=False)).any(axis=1).sum()
    except Exception as e:
        print(f"Error processing {file}: {e}")
    return local_count

# Process each file
for file in files:
    count += count_github_in_csv(file)

# Print and save the result
result = f"Total lines containing 'GitHub': {count}"
print(result)

# Save the output to a file
with open("github_count.txt", "w") as f:
    f.write(result + "\n")
