# Attributes:
# Class can have attributes
# Object can have attributes

# Whatever we create in class is the property of class (can be an attribute or a method)

class Employee:

    # Attribute of Class
    companyName = "Edureka"

    # Special Method called Constructor which is property of class
    def __init__(self, eid, name, salary):
        # In constructor or any method of class 1st input is reference to object i.e. captured in self
        # Now in constructor i.e. __init__ we are creating attributes in object
        self.eid = eid
        self.name = name
        self.salary = salary

    def showDetails(self):
        # companyName is not accessible directly
        # print("Company Name is:",companyName) # error

        # print("Company Name is:", Employee.companyName) # companyName is attribute of Employee Class which is accessed with class name
        print("Company Name is:", self.companyName) # Attribute companyName is not found in Object, so a lookup in class will happen !!

print("Contents of Employee Class:",Employee.__dict__)
# Object Construction Statement
# If we have created a constructor in our class, it will be executed automatically upon object's construction
e1 = Employee(111,"Fionna",50000)
print("Content of Employee Object pointed by e1:",e1.__dict__)

# e1.showDetails() # -> Employee.showDetails(e1)
# Employee.showDetails(e1)

# Property of class i.e. an Attribute is accessible with class name or reference variable of the object
print(Employee.companyName)
print(e1.companyName)

# Property of class i.e. a method is accessible with class name or reference variable of the object
Employee.showDetails(e1)
e1.showDetails()