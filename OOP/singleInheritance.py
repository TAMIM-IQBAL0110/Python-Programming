#One parent → one child
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")


class Developer(Employee):   # Single Inheritance
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def show_dev_details(self):
        print(f"{self.name} codes in {self.programming_language}")


# Object
dev = Developer("Tamim", 50000, "Python")

dev.show_details()
dev.show_dev_details()
