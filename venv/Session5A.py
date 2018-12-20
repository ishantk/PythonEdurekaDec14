# method is a function in a class

class Student:

    # Special Method : Constructor
    # methods will contain 1st input as self.
    # self is reference variable pointing to the current object i.e. object in action
    def __init__(self):
        print("Student Object Constructed",self)

# We can create objects and anytime write any data in it
# When we create an object constructor is executed automatically  i.e. __init__ is executed automatically
s1 = Student() # Student() -> is going to execute __init__ method
s2 = Student()

print("s1 hashCode in hex is",hex(id(s1)))
print("s2 hashCode in hex is",hex(id(s2)))