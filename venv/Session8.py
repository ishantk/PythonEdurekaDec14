import os

"""
path = os.getcwd()
print("Path of CWD:", path)

os.chdir("/Users/ishantkumar/Downloads")
path = os.getcwd()
print("Path of CWD Now is:", path)

os.mkdir("/Users/ishantkumar/Downloads/MyPython")
print("==Directory Created==")

# Use this command carefully
# os.rmdir()

"""

"""
print(os.name)
print(os.getlogin()) # username for current account
print(os.getppid())
"""

path = os.path.join(os.getcwd(), "lib")
print(path)

print(os.path.split(path))
print(os.path.split(os.getcwd()))

print(os.path.exists("/Users/ishantkumar/Downloads/MyPython"))
print(os.path.isdir("/Users/ishantkumar/Downloads/MyPython")) # isFile

# Using os.walk list .mp3 files, .mp4 files, .jpg files separately !! Try Creating a File Explorer App !!
files = os.walk(os.getcwd())
allFiles = list(files)
for f in allFiles:
    print(f)

# Refer Documentation to Explore More !!
