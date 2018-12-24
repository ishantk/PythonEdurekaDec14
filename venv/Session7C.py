class Uber:
    def bookCab(self):
        print("Uber Cab Booked")

class LuxuryUber(Uber):
    def bookCab(self):
        print("Luxury Uber Cab Booked")


class UberGo(Uber):
    def bookCab(self):
        print("UberGo Uber Cab Booked")

class UberMoto(Uber):
    def bookCab(self):
        print("UberMoto Uber Cab Booked")


# uRef = Uber()
# uRef.bookCab()

"""
uRef = UberGo()
uRef.bookCab()

print()

uRef = UberMoto()
uRef.bookCab()

print()

uRef = LuxuryUber()
uRef.bookCab()
"""


def bookUber(typeOfCab):

    cab = None

    if typeOfCab == 1:
        cab = UberGo()

    elif typeOfCab == 2:
        cab = UberMoto()

    elif typeOfCab == 3:
        cab = LuxuryUber()

    return cab

print("==Welcome to Uber===")
print("==1. To Book Uber Go Cab==")
print("==2. To Book Uber Moto Cab==")
print("==3. To Book Uber Luxury Cab==")

choice = int(input(">>Enter your Choice: "))

cab = bookUber(choice)
cab.bookCab()
