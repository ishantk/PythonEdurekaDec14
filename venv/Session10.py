import pandas as pd
import numpy as np

# Series is Data Structure which shall hold 1-D Array as Data !!
# Demonstrates Data in Tabular Form
series = pd.Series()
print(series)
print(type(series))

print()

arr = np.arange(10, 21)  # Elements from 10 to 20
print("Printing Numpy Array")
print(arr)

print()

nummbers = [11, 22, 33, 44, 55]
print("Printing List")
print(nummbers)

print()

# Passing a numpy Array
series1 = pd.Series(arr)
print("Printing Series")
print(series1)

print()

# Passing a list
series2 = pd.Series(nummbers)
print("Printing Series")
print(series2)

print()

# Passing a Dictionary
ages = {"john": 10000, "jennie": 20000, "jim": 23000, "jack": 30000, "joe": 35000}
print(ages)

print()

series3 = pd.Series(ages)
print(series3)

# Access Data from Series
print(series1[0])
print(series2[1])
print(series3["jim"])

# PS: We can construct a Series Data Structure from various different data structures !!
#     Series Shall represent 1-D Array as index and values

print()
print(series1)
print(series1[2])
print(series1[3:])
print(series1[:5])
print(series1[3:5])

