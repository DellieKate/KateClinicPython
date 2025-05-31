import random
import string

from entities import Patient

# Add new patient
def add_patient(patient_list):
    first_name = str(input('Enter first name: ')).strip().capitalize()
    last_name = str(input('Enter last name: ')).strip().capitalize()
    age = int(input('Enter age: '))
    sex = str(input('Enter sex (M/F): ')).strip().capitalize()
    
    full_name = (f'{first_name} {last_name}')
    
    if full_name in patient_list:
        print(f'{full_name} is already an existing patient.')
    else:
        # Generate random ID
        patient_id = (lambda: ''.join(random.choices(string.digits, k=6)))()
        new_patient = Patient(patient_id,full_name,age,sex)
        patient_list.append(new_patient)
        print(f'{full_name} has been added to Patients\' records.')
        print(f'{new_patient.getDetails()}')

    # Display all patient records
    # print('\nAll patients:')
    # for patient in patient_list:
    #     print(f'{patient.getDetails()}')
        
# to call function to main menu  
def reception_main_menu(patient_list = []):
    print(f'\nWelcome to Reception: Main Files.\n')
    while True:
        add_patient(patient_list)
        add = input('Add another patient? (y/n): ').strip().lower()
        if add != 'y':
            break
        
# Uncomment to test in isolation
# reception_main_menu()
        

