"""
class Date:

    # Constructor
    def __init__(self):
        print("Date Object Constructed. HashCode is:", id(self))


    # Decorator / Annotation
    # Use classmethod to construct objects
    @classmethod
    def getDate(cls):
        return cls()    # cls() -> Object Construction and executes constructor

# Object Construction Statement
d1 = Date()
# d2 = Date()

d2 = Date.getDate()
"""

class Date:

    # Constructor
    def __init__(self, dd, mm, yy):
        print("Date Object Constructed. HashCode is:", id(self))
        self.dd = dd
        self.mm = mm
        self.yy = yy

    # Overloading isnt supported in python. i.e. defining the constructor once again !!
    # if we try to redefine the constructor it is overwriting the old definition with new one !!

    # Decorator / Annotation
    # Use classmethod to construct objects
    @classmethod
    def getDate(cls, yy, mm, dd):
        return cls(dd,mm,yy)    # cls() -> Object Construction and executes constructor

d1 = Date(24, 12, 2018)
print(d1.__dict__)

d2 = Date.getDate(2018, 12, 25)
print(d2.__dict__)
