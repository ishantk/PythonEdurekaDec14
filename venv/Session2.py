# Tuples
# We are using Tuple just like a list
names = ("Sia","Fionna","Abby","Kim","Jennie")
# names = ("Sia","Fionna","Abby","Kim","Jennie") Have a mixed upper case and lower case as 1st alphabet and see what happens
print(names)
print(type(names))

print("Length of names is",len(names))
print(max(names)) # A, B , C  -> {S}... Z
print(min(names))

ages = (11,56,34,63,90)

# Once we sort the data as in tuple we get sorted list as in return
newNames = sorted(names)
newAges = sorted(ages)

print(newNames)
print(newAges)

print(type(newNames))
print(type(newAges))

print(ages[1])
print(ages[1:3])
print(ages[::-1]) # Reverse

# names = ("Sia","Fionna","Abby","Kim","Jennie")
print(names*2)
print("John" in names)

voteCountSate1 = (1234, 3456, 7890, 6576)
voteCountSate2 = (3421, 6754, 1211, 9876)

# Concatenating 2 different tuples
voteCount = voteCountSate1 + voteCountSate2
print(voteCount)

vowels = ('a','e','i','o','u')

# Tuples are IMMUTABLE i.e. they cannot be changed
# Anytime we manipulate Tuple it generate a new tuple. Old Tuple shall not be modified !!
newVowels = vowels*2 # A new tuple shall be created and no change shall happen in the previous tuple
print(vowels*2)
print(newVowels)
print(vowels)
