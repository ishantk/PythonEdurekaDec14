import numpy as np

arr = np.genfromtxt("CityTemps.csv", delimiter=",")
print(arr)
print(arr[0][2])

# Use file API's and clean your data sets in case required !!
np.savetxt("CityTemps1.csv", arr, delimiter=",")
print("==File Saved==")