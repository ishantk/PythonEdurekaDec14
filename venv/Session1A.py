names = ["Fionna","Mike","Leo","John","Sia"]

# Accessing the element of list
print(names[0])     # First Element
print(names[-1])    # Last Element
print(names[1:3])   # begin from 1 till less than 3
print(names[2:])    # begins with 2 goes till the end
print(names[:3])    # begins with 0 goes less than 3
# Explore
print(names[-2:-4]) # ?
print(names[-2:])   # ?
print(names[:-4])   # ?

# Update Operation on List
print("Before",names)
names[3] = "John Watson"
print("After",names)

del names[3] # Deletes the Index
print("Deletion",names)
print(names[3])

names.remove("Leo") # Deletes the Value
print("Remove",names)

# Stack Operation -> LIFO
names.pop()
print("Pop",names)

print(type(names))

numbers = [10,20,30,40,50]
# Reading Elements one by one using a loop
sum = 0
for x in numbers:
    sum = sum + x # Logical Operation
    print(x)

print("Sum of Elements in numbers is",sum)

print("===========")
print( [x**2 for x in [1,2,3,4,5] ] )
print("===========")

# Append Operation
numbers.append(12)
numbers.append(121)

print(numbers)

# Extension
moreNumbers = [11,22,33]
numbers.extend(moreNumbers)

print(numbers)
print(moreNumbers)

numbers.remove(10) # Removes the Value

print("Numbers",numbers)

print("===Sorting Numbers===")
print(sorted(numbers))