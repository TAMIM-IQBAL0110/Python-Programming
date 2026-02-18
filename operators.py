
"""
1. Arithmetic Operators
+   -   *   /   %   **   //(floor division)

2. Comparison (Relational) Operators
==   !=   >   <   >=   <=

3. Logical Operators
and   or   not

4. Assignment Operators
=   +=   -=   *=   /=   %=   **=   //=

5. Bitwise Operators
&   |   ^   ~   <<   >>

6. Membership Operators
in   not in

7. Identity Operators
is   is not
    """


a = 10
b = 5

print("AND Operator")
print(a > b and a > 0)
print(a < b and a > 0)

print("\nOR Operator")
print(a > b or a < 0)
print(a < b or b < 0)

print("\nNOT Operator")
print(not(a > b))
print(not(a < b))

age = 20
has_id = True

print("\nEligibility Check")
print(age >= 18 and has_id)
