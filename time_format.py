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

selected_columns = nurses

data_percentage = {}

total_rows = len(df)

for column in selected_columns:
    non_null_data = df[column].dropna()  # Filter out non-null values
    time_data_count_120pm = non_null_data.apply(lambda x: pd.to_datetime(x, format='%I:%M %p', errors='coerce')).notna().sum()
    total_non_null = len(non_null_data)

    time_percentage_120pm = round((time_data_count_120pm / total_non_null) * 100, 3) if total_non_null > 0 else 0

    data_percentage[column] = time_percentage_120pm

print(data_percentage)
