# Introduction to Dictionaries
# We can have homogeneous structure (We decide type of key and type of value)
# We can also have hetrogeneous structure (key and value can be any type)

# Homogeneous
employees = { 101:"John", 201:"Jennie", 301:"Jim", 401:"Jack", 501:"Joe" }

# Hetrogenous
data = { 101:"John", "emp1":"Jennie", 2.2:200 }

print(employees)
print(type(employees))

print(data)
print(type(data))

print(employees[301])
print(data["emp1"])
print(data[2.2])

# Updating the Value corresponding to the Key

print(employees)
employees[101] = "John Watson"
del employees[401]
print(employees)

# Length is calculated by counting number of key-value pairs
print("employees length is",len(employees))
print("data length is",len(data))

# For Dictionaries no Indexing.
# Key given by us is always unique and cannot be duplicated. Hence it solves the purpose of Index !!


