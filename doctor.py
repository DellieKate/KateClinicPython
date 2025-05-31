from entities import Patient

def find_patient_by_id(patient_list, patient_id):
    for patient in patient_list:
        if patient.id == patient_id:
            return patient
    
def doctor_main_menu(patient_list = []):
    print(f'\nWelcome to Doctor\'s Files.\n')
    # from main_clinic_browser import patient_list
   
    pID = input('Input patient ID: ' )
    patient = find_patient_by_id(patient_list, pID)
    print(f'Patient details: {patient.getDetails()}')
    add = input('Confirm patient? (y/n): ').strip().lower()
    if add != 'y':
        pass
    
    