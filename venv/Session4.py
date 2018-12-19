# Typically when we execute a module i.e. a Python Program it is executed from top to bottom.

print("This is Hello from Session4")

def squareOfNum(num):
    result = num*num
    print("Square of {} is {}".format(num,result))

# squareOfNum(5)

# When we execute Program Python Interpreter shall execute the program from top to bottom i.e. line by line
# Before execution of code some special variables are defined in our source file !!
# One of the special variable is __name__ whose value is set to be __main__
# But if the same python module Session4 is imported in other module __name__ is name of python module i.e. Session4

if __name__ == "__main__":
    squareOfNum(5)
else:
    print("Session4 Else Executed")
    print("__name__ is ",__name__)