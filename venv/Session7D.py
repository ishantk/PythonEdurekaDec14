class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Setter and getter for an Object
    def setPoint(self, x, y):
        if x > 0 and y > 0:
            self.x = x
            self.y = y
        else:
            print("Please Enter a Valid Point !!")

    def getPoint(self):
        point = [self.x , self.y]
        return point

    # Setter and Getter for an Attribute
    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

pRef = Point(10, 20)
print("Point is: ", pRef.x, ":", pRef.y)

# If we wish to update the data in object
# We can Access the Attribute Directly !!
pRef.x = 11
pRef.y = 18

print("Point Now is: ", pRef.x, ":", pRef.y)

# pRef.setPoint(-1,1)
# print("Point Now is: ", pRef.x, ":", pRef.y)

point = pRef.getPoint()
print(point)

