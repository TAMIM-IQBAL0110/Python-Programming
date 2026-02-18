#define a employee class with attributes role, department
# and salary. This class also has a showDetails() method
# Create an Engineer class that inherits properties from 
# Employee and  has additional attributes: name and age

class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary
    
    def showDetails(self):
        print(f"Employee Role:{self.role}")
        print(f"Employee department:{self.department}")
        print(f"Employee salary:{self.salary}")

class Engineer(Employee):
    def __init__(self,name,age,department,salary):
        self.name = name
        self.age = age
        super().__init__("Engineer",department,salary)
    def showDetails(self):
        print(f"Employee Name:{self.name}")
        print(f"Employee age:{self.age}")
        super().showDetails()
        
        
eng = Engineer("Tamim",23,"ML",700000)
eng.showDetails()