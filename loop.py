# Loops are used to repeat instructions
# for loop , while loop, do while loop

# while loop 
n = 6
while n>0:
    print(n,end = " ")
    n-=1

#for loop

# 1. Basic for loop (0 to 4)
for i in range(5): print(i)

# 2. Print 1 to 5
for i in range(1, 6): 
    print(i)

# 3. Print in one line
for i in range(1, 6): 
    print(i, end=" ")
    
print()

# 4. Loop through a list
for x in ["apple", "banana", "mango"]: 
    print(x)

# 5. Loop through a string
for ch in "Python": 
    print(ch)

# 6. For loop with step
for i in range(1, 11, 2): 
    print(i)

# 7. Reverse loop
for i in range(5, 0, -1): 
    print(i)