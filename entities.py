class Patient:
    def __init__(self, id, full_name, age, sex):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.sex = sex
        self.lab_test_list = []
        
    def getDetails(self):
        return (f'Patient ID: {self.id} | Full name: {self.full_name} | Age: {self.age} | Sex: {self.sex}')
    
    def confirm_lab_tests(self, lab_test_list):
        self.lab_tests = lab_test_list

class LabTest:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
class BiochemTest(LabTest):
    def __init__(self):
        super().__init__("psa", "Normal PSA < 2.5 ng/mL")
        
class HemaTest(LabTest):
    def __init__(self):
        super().__init__("bsl", "Normal sugar level: 4.0 - 7.8 (mmol/L)")
         
class CytoTest(LabTest):
    def __init__(self):
        super().__init__("papsmear", "Papsmear: No abnormal cells or HPV detected")
        
class GenericTest(LabTest):
    def __init__(self, test_name):
        super().__init__(test_name, f"{test_name} - General tests")