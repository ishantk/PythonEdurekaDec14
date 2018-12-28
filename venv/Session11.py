import matplotlib.pyplot as plt

X = list(range(6))
print(X)

Y1 = [n for n in X]
print(Y1)

Y2 = [n*n for n in X]
print(Y2)

Y3 = [n*n*n for n in X]
print(Y3)

plt.plot(X, Y1, label="Linear")
plt.plot(X, Y2, label="Square")
plt.plot(X, Y3, label="Cube")

plt.grid(True)

plt.xlim(0, 10)
plt.ylim(0, 200)

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.title("Polynomial Graph")

plt.legend()

plt.savefig("MyPlot.png")
print("==Graph Image Saved==")

plt.show()



