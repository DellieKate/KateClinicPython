class Patient:
    def __init__(self, full_name, age, sex):
        self.full_name = full_name
        self.age = age
        self.sex = sex
        
    def getDetails(self):
        return (f'Full name: {self.full_name} | Age: {self.age} | Sex: {self.sex}')    


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