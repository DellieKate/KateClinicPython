# Main page
from reception import reception_main_menu
from doctor import doctor_main_menu

patient_list = []

user = 0
while (user <= 4):
    print(f'\n*** KLM MEDICAL CENTRE ***')
    print(f'-- Melbourne, Victoria --')
    print("-" * 25)
    print(f'\nWELCOME!')
   
    print(f'\nPlease choose user:\n 1 = Reception \n 2 = Doctor \n 3 = Laboratory \n 4 = Exit\n')

    user = int(input('User:  '))  
    # 1 = "Reception: Main Files"
    # 2 = "Doctor\'s Files"
    # 3 = "Laboratory Department"
    # 4 = "Exit"
    
    match user:
        case 1:
            reception_main_menu(patient_list)
            # opens to patients' files
        case 2:
            doctor_main_menu(patient_list)
            # opens Doctor's Files
        case 3:
            print(f'\nWelcome to Laboratory Department\n')
            # opens lab's files
        case 4:
            print(f'\nThank you!\n')
            break
        case _:
            print(f'\nInvalid user. Please choose another option.\n')
            user = 0
            #should include error-handling here
            
  


