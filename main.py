import pandas as pd

df = pd.read_csv('Cental Windborough Data - 2_2_2023.csv')


uniqueness_percentage = {}

for column in df.columns:
    total_rows = len(df) - 1  # Exclude the header row
    unique_values = df[column][1:].nunique()  # Exclude the header row when calculating unique values
    percentage = (unique_values / total_rows) * 100
    uniqueness_percentage[column] = percentage

print(uniqueness_percentage)