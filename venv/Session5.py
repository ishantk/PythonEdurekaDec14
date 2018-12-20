"""

    Introduction to Object Oriented Programming

    	User        -> as an Object
			name
			phone
			email
			age
			gender
			address

"""

# Creating a class, having nothing in it !!
class User:
    pass

print(User)

# What class contains ??
# As per our created class we have created nothing in it
print("Class Data:",User.__dict__) # __dict__ shall print contents in the class

# We didnt create anything in our class even though we see lot of content, which comes automatically for us !!

# If you wish to see contents in Class or in Object use __dict__

# Creating Objects for User class !!
# Object Construction Statement
uRef1 = User()
print("uRef1 HashCode",id(uRef1))

# uRef1 is a Reference Variable pointing to an Object

uRef2 = User()
print("uRef2 HashCode",id(uRef2))

print("uRef1's Object's Data:",uRef1.__dict__)
print("uRef2's Object's Data:",uRef2.__dict__)

# Reference Copy
uRef3 = uRef1
print("uRef3 HashCode",id(uRef3))

# Since, my object is empty Lets ADD DATA in object !!
uRef1.name = "John"
uRef1.phone = "+91 99999 88888"
uRef1.email = "john@example.com"
uRef3.gender = "Male"
uRef3.age = 30
uRef3.address = "Redwood Shores"

uRef2.name = "Fionna"
uRef2.phone = "+91 77777 88888"
uRef2.email = "fionna@example.com"
uRef2.gender = "Female"
uRef2.age = 28
uRef2.address = "Pristine Magnum"
uRef2.status = "Be Exceptional"
uRef2.vehicles = 3

print("uRef1's Object's Data Now is :",uRef1.__dict__)
print("uRef2's Object's Data Now is :",uRef2.__dict__)
print("uRef3's Object's Data Now is :",uRef3.__dict__)

# UPDATE DATA in object !!

uRef1.age = 45
uRef3.name = "John Watson"

print("===Update====")

print("uRef1's Object's Data Now is :",uRef1.__dict__)

print("===Delete====")
# DELETE DATA in object !!
del uRef1.address # it means deleted for uRef3 also. But Why? because uRef1 and uRef3 are pointing to the same single object
print("uRef1's Object's Data Now is :",uRef1.__dict__)

# Anything in Object can be done using its Reference Variable
#===================Introduction Finished====================







