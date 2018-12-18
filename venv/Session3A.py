# Dictionary of Dictionaries
customers = { 1001: {"name":"John", "phone":"+91 99999 88888"}, 2001: {"name":"Jennie", "phone":"+91 77777 88888"}  }

print(customers[1001])
print(customers[2001])

# get is built in function to again get the data on the basis of key
print(customers.get(1001))
print(customers.get(2001))

# item is a tuple of key value pair
# items is a list of tuples of key value pairs
items = customers.items()
print(items)
print(type(items))

keys = customers.keys()
values = customers.values()

print(keys)
print(type(keys))

print(values)
print(type(values))

print("====Copying customers to newCustomers===")
newCustomers = customers.copy()

print(newCustomers)
print(type(newCustomers))

print(hex(id(customers)))
print(hex(id(newCustomers)))

customers.clear()
print(customers)

# ****************

employees = { 111:"John", 21:"Jennie", 45:"Jim", 33:"Jack", 65:"Joe" }
# Fetch the keys and convert them into list
keys = list(employees.keys()) # to convert data into list
print(keys)

sortedKeys = sorted(keys)
print(sortedKeys)

# iterating in Sorted Keys
for key in sortedKeys:
    print(key," ",employees[key])

"""
    Combinations
    
    -> List of Tuples
    -> List of Sets
    -> List of Dictionaries
    -> List of Strings
    -> List of Any Type
    
    -> Tuple of Any Type
    -> Set of Any Type
    -> Dictionary of Any Type
    
    Strings are Just collection of characters !!
"""
