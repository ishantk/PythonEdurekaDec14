# Importing a Module
import Session4

print("This is Hi !! from Session4A")

Session4.squareOfNum(7)

if __name__ == "__main__":
    print("Main of Session4A")
else:
    print("Main Not Executed")

"""
    While executing current python module
    __name__ is __main__
    
    But if the same python module is imported in other module
     __name__ is name of python module
"""

# Exploring Built In Functions/Methods/API's

numbers = [50, 30, 10, 20, 40]
print(numbers)
print(sorted(numbers))
print(len(numbers))

a = 1
print(eval('a + 1')) # eval is evaluating an expression

names = ["John","Sia","Fionna"]
newNames = enumerate(names)
print(newNames)
print(type(newNames))

print(list(newNames))