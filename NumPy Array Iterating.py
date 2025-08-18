# Iterating Arrays
import numpy as np 

arr = np.array([1,2,3,4,5])

for x in arr:
    print(x)


# Iterating 2-D Arrays
arr = np.array([[1,2,3],[4,5,6]])

for x in arr:
    print(x)


# Iterating Arrays Using nditer()
arr = np.array([[[1,2],[3,4],[5,6],[7,8]]])
for x in np.nditer(arr):
    print(x)



# Iterating Array With Different Data Types
# NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].
arr = np.array([1,2,3])
for x in np.nditer(arr,flags=['buffered'],op_dtypes=['S']):
    print(x)



# Enumerated Iteration Using ndenumerate()
arr = np.array([1,2,3])
for idx, x in np.ndenumerate(arr):
    print(idx,x)


arr = np.array([[1,2,3,4],[5,6,7,8]])
for idx,x in np.ndenumerate(arr):
    print(idx,x)