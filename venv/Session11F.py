# r is read mode
file = open("Session11E.py", "r")
# file1 = open("Session11D.py", "r")
print(type(file))

# read will read entire file !!
# fileContents = file.read()

# read till mentioned size
# fileContents = file.read(100)
# print(fileContents)

# print(">> Reading Remaining File <<")

# Remaining data in file will be read from here onwards
# fileContents = file.read()
# print(fileContents)

# print("Re-Reading File:")
#
# fileContentsAgain = file.read()
# print(fileContentsAgain)

# Read Single Line
# line = file.readline()
# print(line)

# Reads the file as in all the lines !!
lines = file.readlines()

for line in lines:
    print(">>", line)

# to release memory resources !!
file.close()
