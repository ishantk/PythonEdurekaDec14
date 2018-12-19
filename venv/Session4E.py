# Global Variable
a = 10

print("a is:",a)

def addNumbers(x, y): # Local Variable
    z = x+y
    z = z + a
    print("sum of",x,"and",y,"is",z)

addNumbers(10,20)

print("a is:",a)

# print("z is",z) # Error

def printNumber():
    a = 100 # when we write this statement a new local variable a is created in the scope of printNumber
    print(">> a is",a)

printNumber()

print(">> global guy a is",a)


# Principle : Initialize a Variable Before using it
def incrementNumber():
    # a = 1
    global a # we are telling our function to use value of global variable a
    a = a + 10
    print("a's incremented value is",a)

incrementNumber()

print(">> global guy a now is",a)