#all valid strings declaration
str1 = "its string 1"
str2 = 'its a string 2'
str3 = """its a string 3"""
str4 = "it's a string"
str5 = 'it"s a string'
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)


#string operations

#string concatenation
str1 = "hello"
str2 = "world"
print(str1+str2)

#length of a string
print(len(str1))

#indexing
print(f"first character of str1 is {str1[0]}")
# in python assign a character in specific position not allowed
# like s[1] = 't' not allowed
#  hello = -5 -4 -3 -2 -1 backword (negative indexing)
a = "hello world"
print(a[:4])
print(a[2:])
print(a[:-1])
print(a[:len(a)])




