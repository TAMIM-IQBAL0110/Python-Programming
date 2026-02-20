#[expression for item in iterable]
#[expression for item in iterable if condition]
#[expression_if_true if condition else expression_if false for item in iterable]
nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums]
print(squares)

# even number print
evens = [x for x in nums if x%2==0]
print(evens)

#boolean value if even true, else false
result = ["even" if x%2 == 0 else "false" for x in nums]
print(result)