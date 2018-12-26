import numpy as np

# numpy Array are much more advanced than regular python lists when it comes to processing of data !!
# they are faster and optimised on memory when it comes to comparison with lists !!

# arange will create an array from 10 to 19
# arr1 = np.arange(10, 20)
arr1 = np.arange(10, 20, 2)
print(arr1)

print()

arr2 = np.zeros((3, 3))     # 3 1-D Arrays with 3 elements each and all the elements shall be 0
print(arr2)

print()

arr3 = np.linspace(0, 20, 5)    # breaking a range linearly !! start from 10 till 20 with 5 elements
print(arr3)

numbers = [10, 20, 30, 40, 50]
arr4 = np.asarray(numbers)      # asarray which takes list as input and converts it to numpy array
print(arr4)
print(type(arr4))

print()

arr5 = np.zeros(8)
print(arr5)
arr6 = arr5.reshape(2, 2, 2)    # we want 2, 2 dim arrays, with each array having 2 elements
print(arr6)

# Flatten the Array to 1-D Array
arr7 = arr6.ravel()
print(arr7)
