"""
# We are going to prompt user to enter a number and convert it into integer
# Whatever is displayed or read from console is always string !!
number = int(input("Enter a Number of Your Choice: "))
# print(number)
# print(type(number))

print("====Table of",number,"====")
for i in range(1,11): # Loop shall run from 1 to 10
    print(number,i,"'s are",(number*i))

print("==========================")
"""
# Let us create a function i.e. a procedure for printing table of a number
# We created a function which takes no input and has no acknowledgement !!
# Function will be executed in a Sequence i.e. whatever instruction is written in it will be executed line by line
def printTable():

    number = int(input("Enter a Number of Your Choice: "))

    print("====Table of", number, "====")
    for i in range(1, 11):  # Loop shall run from 1 to 10
        print(number, i, "'s are", (number * i))

    print("==========================")

# How we execute it
# printTable() # Calling the function i.e. executing it !!
# printTable()
# printTable()

# We are creating a function which takes inputs and has no acknowledgement !!
def addNumbers(num1, num2):
    num3 = num1 + num2
    print("Sum of",num1,"and",num2,"is",num3)
    print("hashCode of num1",hex(id(num1)))
    print("hashCode of num2", hex(id(num2)))


# addNumbers(10,20)
# addNumbers(11,21)
# addNumbers(65,45)
# addNumbers(11,11)

a = 55
b = 77

print("hashCode of a",hex(id(a)))
print("hashCode of b", hex(id(b)))

addNumbers(a, b)


# We are creating a function which takes inputs and has acknowledgement !!

def areaOfCircle(radius):
    area = 3.14 * radius * radius
    return area # Acknowledgement

result = areaOfCircle(2.2)
print("Area of Circle with radius 2.2 is",result)

# We can process the result returned from a function
if(result>5):
    print("We shall proceed")
else:
    print("We shall skip")


print("Area of Circle with radius 3.3 is",areaOfCircle(3.3))

# ***********************
print("********************")

def factorial(num):

    factorialResult = 1

    if num < 0:
        print("Please Enter a Valid Number")
    elif num == 0:
        print("Factorial is:", factorialResult)
    else:
        for i in range(1, num + 1):
            factorialResult = factorialResult * i

    return factorialResult


number = int(input("Enter a Number: "))
result = factorial(number)
print("Factorial of",number,"is",result)



