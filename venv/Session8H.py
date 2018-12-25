# In Python our scripts are Interpreted and not compiled !!
# What ever error shall occur will be an error at run time
# Errors which occurs at Run Time they simply crash our program
# Execution of Program shall be disrupted i.e. abnormal termination of program

"""
print("Welcome")
num1 = int(input("Enter Number 1 "))
num2 = int(input("Enter Number 2 "))
num3 = num1/num2
print("Result is", num3)
print("Thank You !! B.Byee !!")
"""
# If everything is running fine, our program i.e. main thread shall run from top to bottom !!
# All the statements will execute and program shall terminate normally !!

# If error occurs at Run Time we call it Exception !!
# We got techniques to handle exceptions with try catch and finally blocks

print("Welcome")

# Exception Handling : With this we make our apps robust !!
try:
    num1 = int(input("Enter Number 1 "))
    num2 = int(input("Enter Number 2 "))
    num3 = num1/num2
# except ZeroDivisionError:
#     print("OOPS!! num2 cannot be 0")
# except ValueError:
#     print("OOPS!! Number in a text format isn't allowed")
except Exception as e:
    print("Some Error Occurred !!", e)
else:
    print("Result is", num3)
finally:
    print("--Finally--")

print("Thank You !! B.Byee !!")

"""
    try is a block where we keep statement in which error may occur
    except is a block which catches the errors and we shall print some message to the user
    else, if exception will not come use else block to perform the task
    finally is a block which is executed at last regardless of exception occurring or not
    
    Q. How shall we remember exception classes or how will we come to know about them ?
    A. When you will get error you will learn about it or refer documentation about how many errors are thr
       But of all the errors Exception class is Parent to them !!
"""

"""
User Defined Exceptions

class MyException(Exception):
    pass

class YourException(ZeroDivisionError):
    pass
"""