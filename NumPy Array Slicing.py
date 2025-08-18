# Slicing arrays
# Slicing in python means taking elements from one given index to another given index.

import numpy as np 
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])
print(arr[3:])
print(arr[:3])

# Negative Slicing
print(arr[-3:-1])

# Use the step value to determine the step of the slicing:
print(arr[1:5:2])

# Return every other element from the entire array:
print(arr[::2])

# Slicing 2-D Arrays
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4])
print(arr[0:2,2])
print(arr[0:2, 1:4])