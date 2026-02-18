#Dictionaries are used to store data values in key:value pairs.
#They are unordered,mutable(changeable) and indexed.
#They do not allow duplicate members.

#Creating a dictionary (key:value)
info = {
    "name":"tamim",
    "age":23,
    "cgpa":3.66,
    "institude":"RUET",
    34.5:34
}
print(info)

# there is no order in dictionary , element can access by key
dict = {
    "name":"junaid",
    "cgpa":3.54,
    "marks":[98,97,95]
}
print(dict["name"])
print(dict["marks"])
dict["cgpa"] = 3.77
print(dict)

#null dictionary 
null_dict = {}

#nested dictioary

student = {
    "name": "ratul mia",
    "subjects":{
        "phy":45,
        "math":46,
        "chemistry":65
    }
}
print(student["subjects"]["phy"])
