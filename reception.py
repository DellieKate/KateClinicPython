import random
import string
from entities import Patient


# Add new patient
def add_patient(patient_list):
    correct_input = False
    while correct_input != True:
        while True:
            first_name = input('Enter first name: ').strip().capitalize()
            if first_name: 
                break
        while True:
            last_name = input('Enter last name: ').strip().capitalize()
            if last_name: 
                break
        full_name = (f'{first_name} {last_name}')
        
        while True:
            try:
                age = int(input("Enter age: ").strip())
                if age >= 0:
                    break
            except ValueError:
                print("Please enter a valid number for age.")

        while True:
            try:
                sex = input("Enter sex (M/F): ").strip().upper()
                if sex == 'M' or sex == 'F':
                    break
            except ValueError:
                print("Sex must be 'M' or 'F'.")
        correct_input = True
                
    if full_name in patient_list:
                print(f'{full_name} is already an existing patient.')
    else:
        # Generate random ID
        patient_id = (lambda: ''.join(random.choices(string.digits, k=6)))()
        new_patient = Patient(patient_id,full_name,age,sex)
        patient_list.append(new_patient)
        print(f'{full_name} has been added to Patient records.')
        print(f'{new_patient.getDetails()}')

            
# to call function to main menu  
def reception_main_menu(patient_list = []):
    print(f'\n--Welcome to Reception: Main Files--\n')
    option = 0
    while (option <= 4):
        print(f'Please choose an option:\n 1 = Add new patient \n 2 = Export patient details \n 3 = Exit\n')
        option = int(input('Option: \n'))
        match option:
            case 1:
                while True:
                    add_patient(patient_list)
                    add = input('Add another patient? (y/n): \n').strip().lower()
                    if add != 'y':
                        break
            case 2:
                print(f'Patient files exported to file storage.')
                # Export patient files
            case 3:
                print(f'\nThank you!\n')
                break
            case _:
                print(f'\nInvalid option. Please try again.\n')
                user = 0
            #should include error-handling here
    
            
   
            
  
    
    
            

        

