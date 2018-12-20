# Variable Arguments:

def addNumbers(*args): # def addNumbers(*nums): | *args, args can be any name
    # print(args)
    # print(type(args)) # Tuple

    sum = 0

    for num in args:
        sum = sum+num

    print("Sum is",sum)

addNumbers(10,20,30)
addNumbers(10,20,30,40,50)
addNumbers(10,20)
addNumbers(10,20,30,40,50,60,70,80,90)

# keyword arguments
def hello(**kwargs):  # def hello(**anyName):
    print(kwargs)
    print(type(kwargs))

hello(name="John",age=30,city="Bengaluru")
hello(eid=101, ename="George", salary=50000, exp=5)