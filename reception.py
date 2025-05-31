# Add new patient
patients = {}
def add_patient():
    first_name = input('Enter first name: ').strip().capitalize()
    last_name = input('Enter last name: ').strip().capitalize()
    age = int(input('Enter age: ')).strip()
    sex = input('Enter sex (M/F): ').strip()
    
    full_name = (f'{first_name} {last_name}')
    
    if full_name in patients:
        print(f'{full_name} is already an existing patient.')
    else:
        patients[full_name] = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "sex": sex
        }
        print(f'{full_name} has been added to patient records.')

    # display all patient records
    print('\nAll patients:')
    for name, details in patients.items():
        print(f'{name}: {details}')
        
# to call function to main menu  
def reception_main_menu():
    while True:
        add_patient()
        add = input('Add another patient? (y/n): ').strip().lower()
        if add != 'y':
            break
        
        
reception_main_menu()
        

