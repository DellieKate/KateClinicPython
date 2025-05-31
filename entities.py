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
    def __init__(self, psa, blood_sugar):
        self.psa = psa
        self.blood_sugar = blood_sugar
        super().__init__("psa", "psa description")
        
class HemaTest(LabTest):
    def __init__(self, hemoglobin):
        self.hgb = hemoglobin
        super().__init__("Hemoglobin", "Hemoglobin description")
         
class CytoTest(LabTest):
    def __init__(self, papsmear):
        self.papsmear = papsmear
        super().__init__("papsmear", "papsmear description")