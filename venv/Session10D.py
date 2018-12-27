import matplotlib.pyplot as plt

# X coordinates as indexes
# Y coordinates as values
"""
points = [5, 7, 9, 11, 15]
plt.plot(points)
plt.show()  # Show us graph of points
"""

# Specifying X and Y Coordinates !!
"""
X = list(range(6))
print(X)

Y = [n**2 for n in X]
print(Y)

plt.plot(X, Y)
plt.show()

"""

X = list(range(6))
print(X)

Y1 = [n for n in X]
print(Y1)

Y2 = [n*n for n in X]
print(Y2)

Y3 = [n*n*n for n in X]
print(Y3)

plt.plot(X, Y1)
plt.plot(X, Y2)
plt.plot(X, Y3)

plt.grid(True)

plt.show()


