 # def func_name(param1,param2..):
 #     # some work
 #     return result
 
def sum(a,b):
    s = a+b
    return s

# factorial calculation
def fact(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result

#factorial in recursion method
def factr(n):
    if(n == 1):
        return 1
    return n*fact(n-1)

print(factr(5))
print(sum(10,20))
