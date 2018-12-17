name = "John"
print(name)

# String Operations
print(len(name))
print(name[1:3]) # 1 inclusive, < 3 and 3 not inclusive
print("e" in name)

# String Formatting
print("Welcome to %s"%("Edureka"))         # %s Formatting Operator
print("Welcome to {}".format("Edureka"))   # {} Wild Card

print("Welcome, %s !! Is Your age %d ."%("John",22))
print("Welcome, {} !! Is Your age {} .".format("John",22))

names = "John, Jennie, Jim, Jack, Joe"
newNames = names.upper() # Convert String into UPPER CASE !!
# names are not converted to upper case
# because likewise TUPLES, STRINGS ARE ALSO IMMUTABLE
# Manipulation of String shall generate a new String in return
print("Names:",names)
print("New Names:",newNames)

word = "discombobulated" # Try with Mix Case
print(max(word))
print(min(word))


namesAgain = names.replace('J','K')
print("Names Again:",namesAgain)
print("Names:",names)


# names = "John, Jennie, Jim, Jack, Joe"
print(names.index('J'))

allNames = names.split(",")
print(allNames)
print(type(allNames))

for n in allNames:
    print(n.strip())

print(names.find("Jennie")) # return the index from where matched String begins

# String Concatenation
saluatation = "Mr."
fname = "John"
lname = "Watson"

fullName = saluatation +" "+ fname + " " +lname
print(fullName)
print(fullName*2)

# Slicing the String
quote = "Search the Candle, rather than cursing the darkness !!"
print(quote[::-1]) # Reverse of a String
print(quote[3:6])  # start with 3 go less than 6