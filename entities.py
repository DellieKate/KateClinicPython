from datetime import datetime

class Patient:
    def __init__(self, id, full_name, birthday, sex):
        self.id = id
        self.full_name = full_name
        self.birthday = birthday
        self.age = self.calculate_age(birthday)
        self.sex = sex
        self.labtest_list = []
    
    def calculate_age(self, birthday):
        return datetime.today().date().year - birthday.year
          
    def getDetails(self):
        return (f'Patient ID: {self.id} | Full name: {self.full_name} | Age: {self.age} | Sex: {self.sex}')
    
    def confirm_labtests(self, labtest_list):
        self.labtests = labtest_list

class LabTest:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
class BiochemTest(LabTest):
    def __init__(self):
        self.upper_limit = 2.5
        super().__init__('PSA', f'Normal PSA < {self.upper_limit} ng/mL')
        
    # def set_result(self, reading):
    #     if reading > self.upper_limit:
    #         # Do something!!!!
            
class HemaTest(LabTest):
    def __init__(self):
        self.lower_limit = 3.9
        self.upper_limit = 5.6
        super().__init__('BSL', f'Normal fasting blood glucose level is between {self.lower_limit} mmol/L and {self.upper_limit} mmol/l.')
               
class CytoTest(LabTest):
    def __init__(self):
        super().__init__('Papsmear', 'Normal papsmear: No abnormal cells or HPV detected.')
    
class GenericTest(LabTest):
    def __init__(self, test_name):
        super().__init__(test_name, f"{test_name} - General tests")