import random
import string
# import shortuuid
from entities import Patient
from dateutil.parser import parse

        
# Add new patient
def add_patient(patient_list):
    correct_input = False
    while correct_input != True:
        # First name
        while True:
            first_name = input('Enter first name: \n').strip().capitalize()
            if first_name: 
                break
        # Last name
        while True:
            last_name = input('Enter last name: \n').strip().capitalize()
            if last_name: 
                break
            
        full_name = (f'{first_name} {last_name}')
        
        # Birthday
        while True:
            try:
                birthday_str = input("Enter birthdate DD/MM/YYYY: \n").strip()
                birthday = parse(birthday_str).date()
                break
            except (ValueError, OverflowError):
                print("Please enter a valid date of birth.\n")
        
        # Sex / Gender
        while True:
            sex = input("Enter sex (M/F): \n").strip().upper()
            if sex in ['M','F']:
                break
            print("Sex must be 'M' or 'F'.\n")
        
        # existing patient
        if full_name in patient_list:
                    print(f'{full_name} is already an existing patient.\n')
        else:
            # Generate random ID
            patient_id = (lambda: ''.join(random.choices(string.digits, k=6)))()
            
            # Add new patient to patient list
            new_patient = Patient(patient_id,full_name,birthday,sex)
            patient_list.append(new_patient)
            
            print(f'{full_name} has been added to Patient records.\n')
            print(f'{new_patient.getDetails()}')
            
        correct_input = True

            
# Call function(options) to main menu  
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
                print(f'Patient files exported to file storage.\n')
                # Export patient files
            case 3:
                print(f'\nThank you! Exiting system.\n')
                break
            case _:
                print(f'\nInvalid option. Please try again.\n')
                user = 0
            #should include error-handling here
    
            
   
            
  
    
    
            

        

