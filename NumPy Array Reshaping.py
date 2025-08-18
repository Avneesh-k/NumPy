import numpy as np 

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_arr = arr.reshape(4,3) #2d array 
print(new_arr)

new_arr = arr.reshape(2,3,2)
print(new_arr)

# Flattening the arrays
arr = np.array([[1,2,3],[4,5,6]])
new_arr = arr.reshape(-1)
print(new_arr)