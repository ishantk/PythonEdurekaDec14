# Why we need Constructor ??
# With Constructor we can specify what should be the data we want in our object as default data
class Student:

    # Special Method : Constructor
    # methods will contain 1st input as self. self is reference variable pointing to the current object i.e. object in action
    # roll, name, phone are minimum attributes required in each object now
    # Property of class and not of Object
    # Object's hold only data !! nothing other than that
    def __init__(self, roll, name, phone):
        print("Student Object Constructed",self)
        # we are creating attributes in our object using self
        # i.e. we are writing data in our storage container
        self.roll = roll
        self.name = name
        self.phone = phone # self.phone i.e. lhs is creating an attribute phone in object with value as phone on rhs

    # Any Function which we create in class is called a method
    # Every Method in class contains 1st input as self, which is a ref variable pointing to the object in action
    # showStudentDetails method reads the data from Object and displays it
    def showStudentDetails(self):
        print("{} belongs to {} and can be called at {}".format(self.roll,self.name,self.phone))

# Object Construction
# We have put a restriction on Object Construction i.e. please enter roll name and phone on a minimum
s1 = Student(101, "John", "+91 99999 88888")
print("s1 hashCode in hex is",hex(id(s1)))
print(s1.__dict__)

# s1 = Student() # Error -> Inputs are missing
# it means for any object which we create now, we need to pass 3 inputs
# which will be data associated with the object

s2 = Student(201,"Fionna","+91 99999 77777")
s2.stream = "Computer Science" # we can later on add more data the way we were adding earlier
print("s2 hashCode in hex is",hex(id(s2)))
print(s2.__dict__)

print("Contents of Student Class: ",Student.__dict__)

# we are executing method showStudentDetails() of Student class using reference variable of object
s1.showStudentDetails()
s2.showStudentDetails()