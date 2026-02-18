s = {1, 2, 3, 4}
t = {3, 4, 5, 6}

# add() : Adds one element to the set.
s.add(10)
print(s)

# update() : Adds multiple elements to the set.
s.update([7, 8, 9])
print(s)

# remove() : Removes an element from the set (gives error if not found).
s.remove(2)
print(s)

# discard() : Removes an element from the set (no error if not found).
s.discard(100)
print(s)

# pop() : Removes a random element from the set.
s.pop()
print(s)

# clear() : Removes all elements from the set.
s.clear()
print(s)

# union() : Returns a new set containing all elements from both sets.
print(s.union(t))

# intersection() : Returns a new set containing common elements.
print(s.intersection(t))

# difference() : Returns elements present in first set but not in second.
print(s.difference(t))

# symmetric_difference() : Returns elements in either set but not in both.
print(s.symmetric_difference(t))

# issubset() : Checks if one set is a subset of another.
a = {1, 2}
print(a.issubset(s))

# issuperset() : Checks if one set is a superset of another.
print(s.issuperset(a))

# isdisjoint() : Checks if two sets have no common elements.
print(s.isdisjoint(t))


s = {1, 2, 3, 4}

print(3 in s)   # True
print(10 in s)  # False