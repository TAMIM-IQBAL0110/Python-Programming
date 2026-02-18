"""
| Method   | Work                       |
| -------- | -------------------------- |
| count(x) | Counts occurrences of `x`  |
| index(x) | Returns first index of `x` |

    """
t = (10, 20, 30, 20, 40)
#count() → Count how many times a value appears
print(t.count(20)) # 2 

#index() → Find the position of a value
print(t.index(30)) # 2

#length
print(len(t))

#Max / Min
print(max(t))
print(min(t))

#Membership
print(20 in t)