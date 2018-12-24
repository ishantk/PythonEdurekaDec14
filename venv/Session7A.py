# Amazon eCommerce has various Products

# Product class contains common attributes which will be in all the Products i.e. Child Classes
"""
class Product:

    def __init__(self, pid, name, brand, price):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price

    def showProduct(self):
        print("===", self.pid, self.name, "===")
        print("Brand:", self.brand)
        print("Price:", self.price)
        print("==============================")


# Inheritance : Mobile IS-A Product now i.e. Mobile is child of Product, and Product is Parent
class Mobile(Product):

    def __init__(self, pid, name, brand, price, os, ram, memory):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.os = os
        self.ram = ram
        self.memory = memory

    def showMobile(self):
        print("===", self.pid, self.name, "===")
        print("Brand:",self.brand)
        print("Price:", self.price)
        print("OS:", self.os)
        print("RAM:", self.ram)
        print("Memory:", self.memory)


# Inheritance : Shoe IS-A Product now i.e. Shoe is child of Product, and Product is Parent
class Shoe(Product):

    def __init__(self, pid, name, brand, price, weight, size, color):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.weight = weight
        self.size = size
        self.color = color

    def showShoe(self):
        print("===", self.pid, self.name, "===")
        print("Brand:",self.brand)
        print("Price:", self.price)
        print("Weight:", self.weight)
        print("Size:", self.size)
        print("Color:", self.color)

"""

class Product:

    def __init__(self, pid, name, brand, price):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price

    def showProduct(self):
        print("===", self.pid, self.name, "===")
        print("Brand:", self.brand)
        print("Price:", self.price)


class Mobile(Product):

    def __init__(self, pid, name, brand, price, os, ram, memory):
        Product.__init__(self, pid, name, brand, price)  # Executing Parent's Constructor from the Child Contructor
        self.os = os
        self.ram = ram
        self.memory = memory

    def showMobile(self):
        Product.showProduct(self)
        print("OS:", self.os)
        print("RAM:", self.ram)
        print("Memory:", self.memory)
        print("=====================")


# Inheritance : Shoe IS-A Product now i.e. Shoe is child of Product, and Product is Parent
class Shoe(Product):

    def __init__(self, pid, name, brand, price, weight, size, color):
        Product.__init__(self, pid, name, brand, price)
        self.weight = weight
        self.size = size
        self.color = color

    def showShoe(self):
        Product.showProduct(self)
        print("Weight:", self.weight)
        print("Size:", self.size)
        print("Color:", self.color)
        print("====================")


# print()
#
# print("Product Class Contains:")
# print(Product.__dict__)
#
# print()
#
# print("Mobile Class Contains:")
# print(Mobile.__dict__)
#
# print()
#
# print("Shoe Class Contains:")
# print(Shoe.__dict__)

m1 = Mobile(1001, "iPhone", "Apple", 80000, "iOS", 4, 256)
m1.showMobile()

s1 = Shoe(2001, "Loafer", "Carlton London", 3000, 3, 7, "Black")
s1.showShoe()