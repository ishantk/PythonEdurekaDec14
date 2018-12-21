# Anything created in class belongs to Class
# Anything created using self belongs to Object
class Counter:
    """Test on OOPS""" # Documentation of Class
    # Attribute of Class
    count1 = 1

    # Constructor and property of class
    # self is a ref variable which shall hold the address of current object
    def __init__(self):
        self.count2 = 1

    # Method, belongs to class
    # self is a ref variable which shall hold the address of current object
    def incrementCount(self):
        Counter.count1 = Counter.count1 + 1
        self.count2 = self.count2 + 1

    # Method, belongs to class
    # self is a ref variable which shall hold the address of current object
    def showCount(self):
        print("count1:",Counter.count1," count2:",self.count2)

# Object Construction Statement
c1 = Counter()
c2 = Counter()

c3 = c1     #  Reference Copy

c1.incrementCount()
c2.incrementCount()
c3.incrementCount()
c1.incrementCount()
c1.showCount() # count1: 5 count2: 4
c2.showCount() # count1: 5 count2: 2
c3.showCount() # count1: 5 count2: 4


# Built In Attributes of Class
print("__dict__",Counter.__dict__) # content of class
print("__name__",Counter.__name__) # name of class
print("__doc__",Counter.__doc__) # documentation
print("__module__",Counter.__module__) # main
print("__bases__",Counter.__bases__) # Parent Class


# object is a class in python which is by default parent of all the classes, either user defined classes or built in classes

# to access class's attribute
print(Counter.count1)
print(c1.count1)


