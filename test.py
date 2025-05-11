import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv('studentmarks9.csv')  # replace with your actual filename

# # Step 2: Find duplicate codes
# duplicate_codes = df['studentID'][df['studentID'].duplicated(keep=False)]

# # Step 3: Filter rows with duplicate codes
# duplicate_rows = df[df['studentID'].isin(duplicate_codes)]

# # Optional: Sort by code for clarity
# duplicate_rows = duplicate_rows.sort_values('studentID')

# print(duplicate_rows)
# Display the result
# duplicate_rows.to_csv('fayad_dupe.csv')
print(df.info())