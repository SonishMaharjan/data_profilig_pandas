import pandas as pd

df = pd.read_csv('Cental Windborough Data - 2_2_2023.csv')

selected_columns = ['observation_id', 'patient_ssn', 'hospital_id', 'practitioner_id', 'nurse_id', 'medication_id']

uniqueness_percentage = {}

total_rows = len(df)

for column in selected_columns:
    unique_values = df[column][0:].nunique()  # Exclude the header row when calculating unique values
    percentage = (unique_values / total_rows) * 100
    uniqueness_percentage[column] = percentage

print(uniqueness_percentage)