import pandas as pd

# Define file paths (replace with your actual paths)
file1_path = "0.xlsx"
file2_path = "2.xlsx"
file3_path = "3.xlsx"
file4_path = "data.xlsx"

# Read the Excel files using pandas
df1 = pd.read_excel(file1_path)
df2 = pd.read_excel(file2_path)
df3 = pd.read_excel(file3_path)
df4 = pd.read_excel(file4_path)

# Define merged_df within the interpreter
merged_df = pd.merge(df1, df2, on='Barcode', how='outer')
merged_df = pd.merge(merged_df, df3, on='Barcode', how='outer')
merged_df = pd.merge(merged_df,df4, on='Barcode',how='outer')

# Filter for values of 0
filtered_df = merged_df[merged_df['في التحويل إلى الاحساء'] == 0]

# Select desired columns from the merged DataFrame (optional)
# You can choose the specific columns you want from each file here
# filtered_df = filtered_df[['column1_from_file1', 'column2_from_file1', 'column_from_file2', 'barcode']]

# Save the filtered data to a new Excel file
filtered_df.to_excel("merged_filtered_data.xlsx", index=False)

print("Merge and filtering completed. The filtered data is saved to 'merged_filtered_data.xlsx'.")
