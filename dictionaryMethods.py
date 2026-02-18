# .keys() : returns all keys
# .values():returns all values
# .items() : returns all (key,value) pairs as tuples
# .get(key) : safely gets value of a key
# .update(newDict) : insert the specified items to the dictionaries
# 6. pop() :Removes a key and returns its value.
#clear():Removes everything from dictionary.
# copy():Makes a copy of dictionary.

d = {"name": "Tamim", "age": 22, "city": "Dhaka"}

print(d.get("name"))
print(d.get("country", "Not Found"))

print(d.keys())

print(d.values())

print(d.items())

for k, v in d.items():
    print(k, v)

d.update({"age": 23})
d.update({"country": "Bangladesh"})
print(d)


d.pop("city")
print(d)

d.clear()
print(d)

d = {"name": "Tamim", "age": 22, "city": "Dhaka"}
new_d = d.copy()
print(new_d)