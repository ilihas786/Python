# File Handling in Python

# File handling allows you to create, read, write, and delete files from within a Python program.
# The built-in open() function is used to work with files.
# Common modes:
#   'r' - read (default), 'w' - write, 'a' - append, 'b' - binary, 'x' - create
#

########################### Opening a file ############################################
# File Modes in open()
#
# 'r'  : Read (default). Opens the file for reading. File must exist.
# 'w'  : Write. Opens the file for writing (creates new or truncates existing file).
# 'a'  : Append. Opens the file for appending (creates new if not exists).
# 'b'  : Binary mode. Used with other modes (e.g., 'rb', 'wb') for binary files.
# 'x'  : Exclusive creation. Fails if file already exists.
# 't'  : Text mode (default). Used with other modes (e.g., 'rt', 'wt').
# '+'  : Update mode. Read and write (e.g., 'r+', 'w+', 'a+').
#
# Examples:
# open('file.txt', 'r')   # Read text file
# open('file.txt', 'rb')  # Read binary file
# open('file.txt', 'w')   # Write (overwrite) text file
# open('file.txt', 'a')   # Append to text file
# open('file.txt', 'x')   # Create new file, fail if exists
# open('file.txt', 'r+')  # Read and write

file = open('example.txt', 'r')  # Opens a file for reading (must exist)

########################### Reading from a file ########################################

# Read the entire content of the file
content = file.read()
print('File content:')
print(content)

# Reading using for loop
for line in file:
    print(line)

# Reading and returing the first 5 characters
print('First 5 characters:', file.read(5))  # Returns the first 5 characters of the file content

# Reading the entire Line in file
print('First line:', file.readline())  # Reads the first line of the file

# Reading from a file with open('example.txt', 'r') as f:
with open('example.txt', 'r') as f:
    content = f.read()
    print('File content:')
    print(content)

########################### Closing a file ########################################
file.close()  # Always close the file when done     

########################### Writing to a file ########################################

# Example: Writing to a file
with open('example.txt', 'w') as f:
    f.write('Hello, world!\n')
    f.write('This is a new file.\n')

# Reading and writing to a file together
file=open('sample.txt','r+')
file.write('Hello, world!')
file.seek(0)  # Move the cursor back to the beginning of the file
print(file.read())  # This will print the content after writing
file.close()

############################ Appending to a file ########################################

# Example: Appending to a file
with open('example.txt', 'a') as f:
    f.write('Appended line.\n')

# Example: Reading file line by line
with open('example.txt', 'r') as f:
    for line in f:
        print('Line:', line.strip())

# Always close files when done (with statement handles this automatically)
