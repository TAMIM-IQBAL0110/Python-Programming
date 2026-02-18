# A class method is bound to the class and receives the
# class as an implicit first argument
# Note : static method can't access or modify class state
# and generally for utility

# so we use class method to change the class attributes

class Person:
    name = "anonymous" # class attributes
    
    @classmethod
    def changeName(cls,name):
        cls.name = name
    
p1 = Person()
p1.changeName("Weird")
print(p1.name)