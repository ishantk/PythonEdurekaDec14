import numpy as np

# Read Data from txt file as numpy array
arr = np.loadtxt("data.txt")
print(arr)

# Write data into txt file from numpy array
arr1 = np.arange(10, 100, 5)
print(arr1)

np.savetxt("data1.txt", arr1)
print("==Data Saved==")

