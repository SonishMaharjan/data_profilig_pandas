import pandas as pd

df = pd.read_csv('Cental Windborough Data - 2_2_2023.csv')

observations = ['observation_id', 'observation_date', 'observation_time', 'observation_remark']

patients = ['patient_ssn', 'patient_firstName', 'patient_lastName', 'patient_country',
                    'patient_address1', 'patient_address2', 'patient_number1', 'patient_number2', 
                    'patient_sex', 'patient_DOD', 'patient_email', 'patient_height', 'patient_weight',
                    'patient_bloodType', 'patient_educationBackground', 'patient_occupation'
                    ]

hospitals = ['hospital_id', 'hospital_name', 'hospital_address', 'hospital_number', 'hospital_email']


practitioners = ['practitioner_id', 'practitioner_firstName', 'practitioner_lastName', 'practitioner_address1', 
                    'practitioner_address2', 'practitioner_number1', 'practitioner_number2', 
                    'practitioner_checkIn', 'practitioner_checkOut']

nurses = ['nurse_id', 'nurse_firstName', 'nurse_lastName', 'nurse_address1', 
                    'nurse_address2', 'nurse_number1', 
                    'nurse_checkIn', 'nurse_checkOut']

medications = ['medication_id', 'medication_name', 'medication_company', 'medication_level', 'medication_remark']


selected_columns = medications

completeness_percentage = {}

total_rows = len(df) 

for column in selected_columns:
    non_null_count = df[column].count()  # Count the non-null values in the column
    percentage = round((non_null_count / total_rows) * 100, 3)
    completeness_percentage[column] = percentage

print(completeness_percentage)