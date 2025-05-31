## Add new patients in a list
# patient_list = []

# def patient():
#     new_patient = input("Please input first name: ").strip().capitalize()
#     if new_patient in patient_list:
#         print(f'{new_patient} is an existing patient.')    
#     else:
#         patient_list.append(new_patient)
#         print(f"{new_patient} has been added to the patient list.")

# patient()    
# print('Current patient list:', patient_list)


patients = {}

# Define a function to add a patient
def add_patient():
    first_name = input('Enter first name: ').strip().capitalize()
    last_name = input('Enter last name: ').strip().capitalize()
    age = input('Enter age: ').strip()
    sex = input('Enter sex (M/F): ').strip()
    
    full_name = f'{first_name} {last_name}'
    
    if full_name in patients:
        print(f'{full_name} is already an existing patient.')
    else:
        patients[full_name] = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "sex": sex
        }
        print(f'{full_name} has been added to the patient records.')

while True:
    add_patient()
    add = input('Add another patient? (y/n): ').strip().lower()
    if add != 'y':
        break

# Display all patient records
print('\nAll patients:')
for name, details in patients.items():
    print(f'{name}: {details}')