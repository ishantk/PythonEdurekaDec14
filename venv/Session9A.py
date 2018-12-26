import numpy as np

# np.array() takes list as input and creates an array !!
# arr = np.array([1, 2, 3, 4, 5])                   # 1-D Array

# Now we are creating an array which will contain three 1-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])   # 2-D Arrays -> Multi Dimensional Arrays

print(arr)
print(type(arr))

# List Wrapping : Converting List into Numpy Array
numbers = [[10, 20, 30, 40, 50], [11, 12, 13, 14, 15]]
print(numbers)
arr1 = np.array(numbers)
print(arr1)
print(type(arr1))

# 3-D Array : Array Containing 2 2d Arrays, with each Array having 3 arrays fo 3 elements
arr2 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(arr2)
print(type(arr2))


# Q What is use of n-D Arrays
# A : One of the applications is Image Processing eg: Rotating an Image, Making the Image grey scale !!
#     Image is an array of Pixels -> Pixel is an array with R, G, B Values !!
