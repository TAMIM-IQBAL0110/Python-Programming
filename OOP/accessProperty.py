# Public (name) can be accessed inside the class, 
# outside the class, and in child classes.

# Protected (_name) can be accessed inside the class 
# and in child classes, and also outside the class 
# but should be avoided.


# Private (__name) can be accessed only inside the same class 
# and cannot be accessed outside the class or in child classes directly.

# public
class Student1:
    def __init__(self):
        self.name = "Tamim"   # public

s = Student1()
print(s.name)   # accessible outside



#protected 
class Student2:
    def __init__(self):
        self._name = "Tamim"   # protected

class Child(Student2):
    def show(self):
        print(self._name)      # accessible in child class

c = Child()
c.show()

# Unlike C++ or Java, in Python, protected members can be 
# accessed outside the class, but it is not recommended to do so.
s = Student2()
print(s._name)   # accessible outside but should be avoided

#private
class Student3:
    def __init__(self):
        self.__name = "Tamim"   # private

    def show(self):
        print(self.__name)      # accessible inside class

s = Student3()
s.show()

# print(s.__name) ❌ Error

