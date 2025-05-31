from entities import Patient

def find_patient_by_id(patient_list, patient_id):
    for patient in patient_list:
        if patient.id == patient_id:
            return patient
    
def doctor_main_menu(patient_list = []):
    print(f'\nWelcome to Doctor\'s Files.')
    option = 0
    while (option <= 4):
        print(f'\nPlease choose an option:\n 1 = Search patient \n 2 = Export patient report \n 3 = Exit\n')
        option = int(input('Option: \n'))
        match option:
            case 1:
                pID = input('Input patient ID: ' )
                patient = find_patient_by_id(patient_list, pID)
                # print(f'Patient details: {patient.getDetails()}')
                print(f'Patient details: ')
                add = input('Confirm patient? (y/n): ').strip().lower()
                if add != 'y':
                    pass
                # while True:
                #     add_patient(patient_list)
                #     add = input('Add another patient? (y/n): ').strip().lower()
                #     if add != 'y':
                #         break
            case 2:
                print(f'Export patient report to PDF.')
                # Export patient files
            case 3:
                print(f'\nThank you!\n')
                break
            case _:
                print(f'\nInvalid option. Please try again.\n')
                user = 0
            #should include error-handling here
    
    
