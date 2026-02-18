#__init__ method
# constructor method that is called when an object is created.
# It is used to initialize the attributes of the object.
# __init__ is called automatically when an object is created, 
# and it is used to initialize the object’s attributes.
# The __init__ method takes "self" as the first parameter, 
# which refers to the instance of the class being created.

class Student:
    
    #default constructor, If you don’t define an __init__() method, 
    # Python provides a default constructor automatically.
    def __init__(self):
        pass
    
    #parameterized constructor
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def displayDetails(self):
        print(f"student name :{self.name}")
        print(f"student id:{self.id}")

s1 = Student("tamim",2103094)
s1.displayDetails()