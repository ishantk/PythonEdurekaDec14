# Container in a Container

# List of Lists
votes1 = [ [1234,1256,5678,1235], [4567,2345,7894,2345] ]

# Tuple of Tuples
votes2 = ( (1234,1256,5678,1235), (4567,2345,7894,2345) )

print(len(votes1))
print(len(votes2))

print(votes1[0][1]) # 1256
print(votes2[1][2]) # 7894

# List of Tuples
# Tuple of Lists
# List of Lists and Tuples
# Tuple of Lists and Tuples

votes3 = [ (1234,1256,5678,1235), [4567,2345,7894,2345] ]
votes4 = ( (1234,1256,5678,1235), [4567,2345,7894,2345] )

# Requirement is that we will have data which shall change      -> List  (Slow)
# Requirement is that we will have data which shall not change  -> Tuple (Fast)

# votes2 is Tuple and is IMMUTABLE !!
# del votes2[0] # error
# print(votes2)

# List in a Tuple can be easily Modified due to its default nature i.e. it is MUTABLE
votes4[1][0] = 9999 # manipulate element of list in a tuple
votes4[1].append(1111) # increase the size of list automatically
print(votes4)


numbers = (1,2,3,4,5)           # IMMUTABLE
newNumbers = list(numbers)      # Convert tuple int List and newNumbers is now MUTABLE

print(numbers)
print(newNumbers)
newNumbers.append(12)
print(newNumbers)

numbers = [10, 20, 30]
names = ["John","Jennie","Jim"]

# Zipping: Left out for future
result = zip(numbers,names)

print(result)
print(type(result))

result1 = list(result)
print(result1)