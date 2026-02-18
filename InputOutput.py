name = input("Enter your name: ")
age = input("Enter the age:")
print("Hello", name, "\nYour age :",age)

# type of python variable by default string when take input
print("Type of name is ", type(name))
print("Type of age is", type(age))

# f-string is a good way to print
print(f"Hello {name} \n Your age is {age}")
