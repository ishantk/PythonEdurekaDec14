# List VS Tuple

data1 = [10, 2.2, "John", "Sia"]
data2 = (10, 2.2, "John", "Sia")

print(type(data1))
print(type(data2))

data1[1] = 12.33   # We can manipulate data in data1 i.e. a list
print(data1)

# data2[1] = 12.33 # Error: We cannot manipulate data2 i.e. tuple

name = ("John") # it still remains string
print(name)
print(type(name))

anotherName = ("Jennie",) # it becomes tuple
print(anotherName)
print(type(anotherName))

# We cannot append data in tuple the way we were appending in the list
# ?? Why ? Because Tuple is IMMUTABLE
data2.append(12)