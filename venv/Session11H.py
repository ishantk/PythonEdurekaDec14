import numpy as np
import pandas as pd

# Numpy Array which can store data for n-Dimensions
# 1-D Array
arr = np.arange(1, 101, 2)
print(arr)

# 1-D Array in Pandas is Series
s1 = pd.Series(arr)
# print(s1)
# print(s1.axes)
# print(s1.values)

print(s1.head(30))  # 30 not inclusive i.e. 0 to 29
print("---------")
print(s1.tail(3))   # Last 3 records

oddNumbers = np.arange(1, 100, 2)
evenNumbers = np.arange(0, 100, 2)

print(oddNumbers)
print(evenNumbers)

numbers = {"odd": oddNumbers, "even": evenNumbers}
table = pd.DataFrame(numbers)

print("---------")
print(table)
print("---------")
print(table.sum())
print("---------")
print(table.std())
print("---------")

