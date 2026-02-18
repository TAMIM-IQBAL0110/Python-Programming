# static methods don't use the self parameter (work at class level)

# class is a collection of methods and attributes
# methods are functions that belong to objects

# decoratos allow us to wrap another function in order to 
# extend the behaviour of the wrapped function , without
# permanently modifying it

class Student:
    college_name = "ABC College"
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        self.welcome()
        
    # static method
    @staticmethod # decorator
    def welcome():
        print("welcome the college")
    
    def get_marks(self):
        return self.marks
    
s1 = Student("karim",97)
print(s1.get_marks())