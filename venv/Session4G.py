# Variable Arguments:

def addNumbers(*args): # def addNumbers(*nums): | *args, args can be any name
    # print(args)
    # print(type(args))

    sum = 0

    for num in args:
        sum = sum+num

    print("Sum is",sum)

addNumbers(10,20,30)
addNumbers(10,20,30,40,50)
addNumbers(10,20)
addNumbers(10,20,30,40,50,60,70,80,90)
