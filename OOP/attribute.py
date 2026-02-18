# A class attribute is defined inside the class, 
# but outside __init__(). but its same for all instance
# An instance attribute is defined inside __init__() using self.
# and it may different from other instance 

# instance attributes precedence is higher than class attributes
# if name is both class and instance attribute , instance attribute will print


class student:
    collegeName = "ABC College" # class attribute
    
    def __init__(self,name,marks):
        self.name = name # instance of attribute
        self.marks = marks
        print("instance is created")

    def displayDetails(self):
        print(f"student name : {self.name}")
        print(f"college:{self.collegeName}")
        print(f"marks:{self.marks}")


s1 = student('tamim',3.66)
s1.displayDetails()
