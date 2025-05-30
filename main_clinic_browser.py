# KLM Medical Centre
# Melbourne, Victoria

# Main page

print(f'Welcome to KLM Medical Centre\n')

print(f'Please choose user:\n 1 = Receptionist \n 2 = Doctor \n 3 = Laboratory \n')

user = int(input('User:  '))    
# 1 = "Reception: Main Files"
# 2 = "Doctor\'s Files"
# 3 = "Laboratory Department"

match user:
    case 1:
        print(f'Reception: Main Files.')
        # opens to clinics' main file (patients' directories)
    case 2:
        print(f'Doctor\'s Files.')
        # opens Doctor's Files
    case 3:
        print(f'Laboratory Department')
        # opens lab's files
    case _:
        print(f'Invalid user. Please choose another option.')
        #should include error-handling here

print(f'Welcome to {user}!')



    
