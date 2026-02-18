#Used to delete object properties or object itself
# syntax: del objectName.attributeName
# del objectName -> delete object

class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Anil")
print(s1.name)
del s1.name # name attribute deleted and if wanna access give error
print(s1)
del s1 # s1 object deleted