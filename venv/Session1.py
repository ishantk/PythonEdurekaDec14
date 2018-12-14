# Single Value Container
age = 10 # int

# Multi Value Container

# Homogeneous
ages = [10, 20, 30, 40, 50]                     # list -> list of integers
names = ["John","Jennie","Jim","Jack","Joe"]    # list -> list of strings

# Hetrogeneous
data = [10,2.2,"John","Jennie",45]              # list -> list of objects

# Reading data out of Container
print(age)
print(ages)

# Every Storage Container has a type
print("Type of age is",type(age))
print("Type of ages is",type(ages))

# Get the HashCodes for thr storage
# Notations : Decimal, Binary, Octal, Hexadecimal (Please Explore)
print("HashCode of age is",hex(id(age)))
print("HashCode of ages is",hex(id(ages)))

# SEQUENCE OPERATIONS:
moreAges = [11,35,69]
moreNames = ["Kim","Kia","Sia"]

# Concatenation
print(ages+moreAges)
print(names+moreNames)

#Repetition
print(ages*3)
print(names*2)

# Membership Testing
print(1007 in ages)
print("John" in names)

#Indexing
print(ages[0])
print(names[1])

#Slicing
print(names[0:3]) # from 0 to less than 3