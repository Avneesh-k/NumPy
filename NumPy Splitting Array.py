import numpy as np 
arr = np.array([1,2,3,4,5,6])
new_arr = np.array_split(arr,4) #plit the array in 3 parts:
print(new_arr)



arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)