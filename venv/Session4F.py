# Function Arguments: a, b and c i.e. Inputs

# def addNumbers(a, b, c):
# def addNumbers(a=1, b=2, c):  # error | non-default argument follows default argument
# def addNumbers(a, b=2, c=3):  # work  | non-default argument not following default argument
def addNumbers(a=1, b=2, c=1):  # Default Arguments
    sum = a+b+c
    print("Sum of Numbers is:",sum)

addNumbers(10,20,30)
addNumbers(a=11,b=12,c=13)
addNumbers(c=22,a=33,b=44) # Keyword Arguments

# addNumbers(10,20) # ?? -> Results into error as we have not supplied the value for c
addNumbers(10,20)
addNumbers(10)
addNumbers(c=111)

