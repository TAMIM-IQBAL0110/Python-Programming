
#write to a file(overwrite file)
with open("example.txt","w") as f:
    f.write("Hello python file operations!\n")
    f.write("This is second line\n")
    # no need to close file

# append to a file
with open ("example.txt","a") as f:
    f.write("Appending a new line using with.\n")

# Read the entire file
with open("example.txt","r") as f:
    data = f.read()
    print("file data:\n",data)

#Read file line by line
with open("example.txt","r") as f:
    print("print line by line")
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()
        
#Read all lines into a list using readlines()
with open("example.txt","r") as f:
    lines = f.readlines()
    print("All lines as list:",lines)

# Write and read binary file
data = b"Binary data example"
with open("example.bin", "wb") as f:
    f.write(data)

with open("example.bin", "rb") as f:
    binary_content = f.read()
    print("Binary file content:", binary_content)



# Open existing file for reading and writing
with open("example.txt", "r+") as f:
    print("Before writing with r+:")
    print(f.read())  # Read current content
    
    f.seek(0)  # Move cursor to start
    f.write("First line updated using r+\n")  # Overwrites from start

# Check updated content
with open("example.txt", "r") as f:
    print("After r+ update:")
    print(f.read())


# Open file for writing and reading
with open("example_w+.txt", "w+") as f:
    f.write("This is a new file with w+\n")
    f.write("Second line added.\n")
    
    f.seek(0)  # Move cursor to start to read what we wrote
    content = f.read()
    print("Content of w+ file:")
    print(content)
