# we have to open a file before reading or writing 
# f = open("file name","mode")
# mode : r -> read mode , w -> write mode
# data = f.read() returns the form of a string
# f.close() 

"""
Character — Meaning
'r' — open for reading (default)        r+ -> read and write
'w' — open for writing (overwrite)      w+ -> read and write
'x' — create a new file and open it for writing
'a' — open for writing, appending
'b' — binary mode
't' — text mode (default)
'+' — updating (reading and writing)
"""

# ----------------------------
# Read Mode (r)
# ----------------------------
f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()


# ----------------------------
# Write Mode (w)
# ----------------------------
f = open("demo.txt", "w")
f.write("This is new text written in demo.txt")
f.close()

# Now read again to see result
f = open("demo.txt", "r")
print(f.read())
f.close()


# ----------------------------
# Append Mode (a)
# ----------------------------
f = open("demo.txt", "a")
f.write("\nThis line is appended.")
f.close()

# Read again
f = open("demo.txt", "r")
print(f.read())
f.close()


# ----------------------------
# Create Mode (x)
# ----------------------------
# Run only once, otherwise error
f = open("newfile.txt", "x") 
# if we do same thing as w or a mode, file will be created if it doesn't exist
f.write("This file is created using x mode.")
f.close()


# ----------------------------
# Read + Write Mode (r+)
# ----------------------------
f = open("demo.txt", "r+")
print("Before Writing:")
print(f.read())

f.write("\nAdded using r+ mode.")
f.close()


# ----------------------------
# Write + Read Mode (w+)
# ----------------------------
f = open("demo.txt", "w+")
f.write("Written using w+ mode.")

f.seek(0)  # Move cursor back to beginning
print("Reading after writing:")
print(f.read())

f.close()


# ----------------------------
# Seek Example
# ----------------------------
f = open("demo.txt", "r")
print(f.read())

f.seek(0)   # move cursor back to start

print(f.read())
f.close()



# f.read() -> reads the entire file and returns it as a string. 
# After this operation, the cursor is at the end of the file, 
# so subsequent read operations will return an empty string 
# unless you move the cursor back to the beginning using f.seek(0).

#f.readline() -> reads a single line from the file and returns it as a string.
# After reading a line, the cursor moves to the beginning of the next line.
# so line1 = readline()
# line2 = readline()
