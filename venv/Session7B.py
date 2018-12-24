class Cab:

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        print("==Cab Object Constructed==")

    def bookCab(self):
        print("Cab Booked from", self.source, " to ", self.destination)

# Inheritance UberCab(Cab)
class UberCab(Cab):

    # Why to create Constructor in Child ?
    # Customization !! We need to add typeOfCab as well

    """
    def __init__(self, source, destination, typeOfCab):
        self.source = source
        self.destination = destination
        self.typeOfCab = typeOfCab
        print("==Uber Cab Object Constructed==")
    """

    def __init__(self, source, destination, typeOfCab):
        Cab.__init__(self, source, destination)
        self.typeOfCab = typeOfCab
        print("==Uber Cab Object Constructed==")

    # Re-Defining Parent's Method in Child as well so as to customize !!
    # Overriding
    def bookCab(self):
        print(self.typeOfCab,"Cab Booked from", self.source, "to", self.destination)

    def show(self):
        print(self.typeOfCab," Booked !!") # or print(self.typeOfCab + " Booked !!") + is to concatenate Strings
        Cab.bookCab(self)

# Inheritance OLACab(Cab)
class OLACab(Cab):
    pass



print(Cab.__dict__)
print(UberCab.__dict__)
print(OLACab.__dict__)

# While creating Object of UberCab or OLACab i.e. Child Objects
# Classes have no Constructor !!
# So, Parent's Constructor definition is used to create objects !!
# Child Classes are not inheriting definations from Parent !!
# Just creating a relationship between 2 classes

uRef = UberCab("Pristine Magnum", "Country Homes", "Luxury")
oRef = OLACab("Pristine Magnum", "Country Homes")

# PS: bookCab is not inherited into UberCab or OLACab Child classes
#     bookCab of Parent is being used !!

# Remeber, Inheritance in Python is Parent and Child Relationship !!
#          Parent has a vehicle, child does not have a vehicle. But in need child will use Parent's vehicle !!
uRef.bookCab()
# oRef.bookCab()

# uRef.show()
