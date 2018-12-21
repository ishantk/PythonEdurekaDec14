class Point:

    subjectName = "Mathematics"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # This is overwriting the previous constructor
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    """

    # Method which belongs to class and takes 1st input as reference of object i.e. self
    def showPoint(self):
        # print("Subject is:",Point.subjectName) # Accessing class attribute with class name
        print("Subject is:", self.subjectName)   # Accessing Class attribute with reference variable of Object
        print("Point is",self.x,":",self.y)

    # Having a method without specifying the 1st input as self is not possible !! It gives an error !!
    # we can give an annotation | DECORATOR | called @classmethod on top of method
    @classmethod
    def showPointAgain(cls):    # cls is reference to class
        print("This is showPoint Again")
        print("Subject is",cls.subjectName)

    @staticmethod
    def sayHello(name):             # belongs to class, shall not take self or cls as input
        print("Hello Dear",name,"from Python's static method")


p1 = Point(10,20)
# p1.showPoint()

# p1.showPointAgain()
Point.showPointAgain()

# p1.sayHello()
Point.sayHello("John")