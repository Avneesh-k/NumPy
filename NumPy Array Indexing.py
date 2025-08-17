import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])
print(arr[1])
print(arr[2]+arr[3])

# Access 2-D Arrays

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)
print('2nd elememt of 1st row is :',arr[0,1])
print('5th element on 2nd row: ', arr[1, 4])


# Access 3-D Arrays

arr = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
print(arr)
print(arr[0, 1, 2])

# Negative Indexing
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('last element from 2nd dim: ',arr[0,-1])