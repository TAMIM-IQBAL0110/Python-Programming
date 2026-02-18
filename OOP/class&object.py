#class is a blueprint for creating objects. 
# It defines a set of attributes and methods that the created objects will have.


# creating class :
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# create object of the class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# call method of the class
print(person1.greet())
print(person2.greet())