# Value Vs Reference : Nothing like Value in Python. Its all about References !!

# Single Value Container
num1 = 10

# Multi Value Container
numbers1 = [10, 20, 30, 40, 50]

# Copy Operation : Reference Copy (We copy HashCodes)
# Python has nothing like Value Copy
num2 = num1 # Basically HashCode was Copied not the Value
numbers2 = numbers1

print("num1 is",num1," hashCode:",hex(id(num1)))
print("num2 is",num2," hashCode:",hex(id(num2)))

print("numbers1 is",numbers1," hashCode:",hex(id(numbers1)))
print("numbers2 is",numbers2," hashCode:",hex(id(numbers2)))

# if we do not modify the data, HashCodes remains same
# Small Twist in Multi Value Container !!
print("******** Modifying Data In List *********")

numbers2[2] = 111
numbers1[3] = 333

print("numbers1 now is",numbers1," hashCode:",hex(id(numbers1)))
print("numbers2 now is",numbers2," hashCode:",hex(id(numbers2)))

# Whats the Use ? In WhatsApp we are holding reference to the Group. If any user changes the data it is reflected ot other !!

"""

print("******** Modifying Content *********")

# Lets modify content
num2 = 20
numbers2 = [11,22,33,44,55]

print("num2 is",num2," hashCode:",hex(id(num2)))
print("numbers2 is",numbers2," hashCode:",hex(id(numbers2)))



"""

