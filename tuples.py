# A build-in data type that lets us create immutable sequence of values
tup = (2,1,3,1)
print(tup[0]) #allowed but value change is not allowed
print(tup[1])

# but tup = (1) is a integer . must declare as (1,) for single value
# tuple allow slicing
print(tup[1:3]) # (1,3)