# Indexing and Slicing on numpy arrays
import numpy as np

numbers = [10, 20, 30, 40, 50]
# Accessing an Index
print(numbers[1])
# Slicing
print(numbers[1:4])

print()

arr = np.arange(1, 51)
print(arr)
# Read an Element on the basis of index
print(arr[49])

print()

# Read Multiple Elements
slices = slice(1, 10, 2)  # -> 1, 3, 5, 7, 9
print(type(slices))

print(arr[slices])  # in numpy array we can pass a slice object

print(arr[10:])     # 10th index onwards
print(arr[:15])     # 0th index to 14th index
print(arr[10:15])   # 10th index till 14th index

print()

# Slicing on Multi Dim Array
arr1 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(arr1[0:2, 0:2])

# Numpy Array Attributes
print("Shape is:", arr1.shape)
print("Dimension is:", arr1.ndim)
print("Size is:", arr1.itemsize)

print()
arr2 = np.zeros(5)
print(arr2)

arr3 = np.empty([3, 2], dtype=float)
print(arr3)
