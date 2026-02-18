# A built-in data type that strores set of values
#It can store elements of different data types(int,float,string,..etc)
# its a mutable data type (can be modified after creation)

marks = [90, 80, 70, 60, 50.5]
print(marks)
print(type(marks))
# can access element by index
print(marks[0]) # 90
print(marks[1]) # 80

student = ["Alice", 210345, "CSE", 3.5]
student[3] = 3.7
print(student)

# list slicing -> similar to String slicing
print(marks[1:4]) # [80, 70, 60]
print(marks[:3]) # [90, 80, 70]
print(marks[2:]) # [70, 60, 50.5]
print(marks[-3:]) # [70, 60, 50.5]
print(marks[:-1]) # [90, 80, 70, 60]