import pandas as pd

# Assuming your CSV file is named 'Cental Windborough Data - 2_2_2023.csv'
df = pd.read_csv('Cental Windborough Data - 2_2_2023.csv')

# Print the first row data
print("First row data:")
print(df.head(1))

# Print the last row data
print("Last row data:")
print(df.tail(1))

print("Total")
print(len(df))