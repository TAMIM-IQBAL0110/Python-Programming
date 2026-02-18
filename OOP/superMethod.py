# super() method is used to access methods of the parent class
class Parent:
    def __init__(self,name):
        self.name = name
    
    def greet(self):
        print(f"Hello , I am {self.name}")
    
class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name) # call Parent's constructor
        self.age = age
    
    def show(self):
        print(f"my age is {self.age}")

c = Child("Shanto", 18)
c.greet()
c.show()
