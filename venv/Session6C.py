
class Product:

    # Constructor : Property of class
    def __init__(self, pid, name, price):
        #public attribute
        self.productId = pid
        # protected attribute
        self._productName = name
        # private attribute -> becomes protected attribute
        self.__productPrice = price # Name Mangling for __productPrice shall result as _Product__productPrice (becomes protected)

    # def _showProductDetails(self):
    def __showProductDetails(self): # __showProductDetails(self): -> _Product___showProductDetails(self):
        print(self.productId,"belongs to ",self._productName," and is available for",self.__productPrice)


# When we create object init is executed automatically and it expects 3 inputs from us
pRef = Product(101,"Apple iPhoneX",70000)

print("Product class contains:",Product.__dict__)
print("Product Object pointed by pRef Contains:",pRef.__dict__)

# Lets try to read data of Object
# print(pRef.productId," - ",pRef._productName," - ",pRef.__productPrice) # error
print(pRef.productId," - ",pRef._productName," - ",pRef._Product__productPrice)

# pRef._showProductDetails()
pRef._Product__showProductDetails()

# PS: In python we can read and write data i.e. fully access public, protected and private
# Why protected and private ? Just to tell the user with a warning please do not access them

# In python we got public or non public
# non public : variable name starting with _ -> warning that do not access this variable !!

# When to use protected ? Lets say i created a python code to read an image file and rotate it
# as per python we can fully access variables !! public or non public both are accessible
# Now, my python code is imported by you people to rotate images !! _rotateAngle = 180
# I will make few attributes in my Python Program as protected so as to tell you not to modify them