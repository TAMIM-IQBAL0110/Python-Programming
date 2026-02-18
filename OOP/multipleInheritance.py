# Multiple inheritance occurs when a child (derived) 
# class inherits from more than one parent (base) class. 
# This allows the child class to access attributes and 
# methods from all parent classes.
class Employee:
    def work(self):
        print("Working in a company")


class Student:
    def study(self):
        print("Studying at university")


class WorkingStudent(Employee, Student):   # Multiple Inheritance
    def manage(self):
        print("Managing both work and study")


# Object
ws = WorkingStudent()

ws.work()
ws.study()
ws.manage()
