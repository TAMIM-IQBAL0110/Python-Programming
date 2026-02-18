s = "i am a coder."

# 1. startswith()
# Checks if a string begins with a specific word or character.
print(s.startswith("I"))

# 2. endswith()
# Checks if the string ends with something.
print(s.endswith("er."))

# 3. capitalize()
# Makes the first character uppercase.
print(s.capitalize())

# 4. replace(old, new)
# Replaces all occurrences of a substring.
print(s.replace("coder", "programmer"))

# 5. find()
# Returns the first index where the word appears.
print(s.find("am"))

# 6. count()
# Counts how many times a substring appears.
print(s.count("a"))

# 7. lower()
# Converts the string into lowercase.
print(s.lower())

# 8. upper()
# Converts the string into uppercase.
print(s.upper())

# 9. strip()
# Removes extra spaces from start and end.
print(s.strip())

# 10. lstrip()
# Removes spaces only from the left side.
print(s.lstrip())

# 11. rstrip()
# Removes spaces only from the right side.
print(s.rstrip())

# 12. split()
# Splits the string into a list of words.
print(s.split())

# 13. join()
# Joins list elements into a single string.
words = ["I", "am", "coder"]
print(" ".join(words))

# 14. index()
# Returns index of substring, but gives error if not found.
print(s.index("am"))

# 15. isalpha()
# Checks if the string contains only alphabets.
print("Tamim".isalpha())

# 16. isdigit()
# Checks if the string contains only digits.
print("1234".isdigit())

# 17. isalnum()
# Checks if the string contains alphabets and digits.
print("Tamim123".isalnum())

# 18. title()
# Capitalizes the first letter of each word.
print("i am a coder".title())

# 19. swapcase()
# Converts uppercase to lowercase and lowercase to uppercase.
print("PyThOn".swapcase())
