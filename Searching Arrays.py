# To search an array, use the where() method.
import numpy as np 
arr = np.array([1,2,3,4,5,4,4])
x = np.where(arr == 4) #return the index of 4 
print(x)

# Find the indexes where the values are even:
arr = np.array([1,2,3,4,5,6,7,8])
x = np.where(arr%2 == 0)
print(x)

# Find the indexes where the values are odd:
arr = np.array([1,2,3,4,5,6,7,8])
x = np.array(arr%2 == 1)
print(x)

# Search Sorted
# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
# The searchsorted() method is assumed to be used on sorted arrays.

arr = np.array([6,7,8,9])
x = np.searchsorted(arr,7)
print(x)
# By default the left most index is returned, but we can give side='right' to return the right most index instead.

y = np.searchsorted(arr,7,side='right')
print(y)


# Multiple Values
# To search for more than one value, use an array with the specified values.
arr = np.array([1,3,5,7])
x = np.searchsorted(arr,[2,4,6]) #return the indexes where 2,4,6 would be inserted in the original array to maintain order.
print(x)