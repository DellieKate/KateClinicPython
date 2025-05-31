# Main page
from reception import reception_main_menu

user = 0
while (user <= 4):
    print(f'\nWelcome to KLM Medical Centre\n')
    print(f'Melbourne, Victoria')

    print("-" * 25)

    print(f'\nPlease choose user:\n 1 = Receptionist \n 2 = Doctor \n 3 = Laboratory \n 4 = Exit\n')

    user = int(input('User:  '))  
    # 1 = "Reception: Main Files"
    # 2 = "Doctor\'s Files"
    # 3 = "Laboratory Department"
    # 4 = "Exit"
    
    match user:
        case 1:
            print(f'Welcome to Reception: Main Files.\n')
            reception_main_menu()
            # opens to clinics' main file (patients' directories)
        case 2:
            print(f'Welcome to Doctor\'s Files.\n')
            # opens Doctor's Files
        case 3:
            print(f'Welcome to Laboratory Department\n')
            # opens lab's files
        case 4:
            print(f'Thank you!\n')
            break
        case _:
            print(f'Invalid user. Please choose another option.\n')
            user = 0
            #should include error-handling here
            
  


