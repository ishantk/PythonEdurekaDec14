import matplotlib.pyplot as plt

X = list(range(6))
print(X)

Y1 = [n for n in X]
print(Y1)

Y2 = [n*n for n in X]
print(Y2)

Y3 = [n*n*n for n in X]
print(Y3)

# plt.plot(X, Y1, "y")
# plt.plot(X, Y2, "m")
# plt.plot(X, Y3, "b")

# plt.plot(X, Y1, "--")
# plt.plot(X, Y2, "-.")
# plt.plot(X, Y3, ":")

plt.plot(X, Y1, "s")
plt.plot(X, Y2, "^")
plt.plot(X, Y3, "D")


plt.show()

