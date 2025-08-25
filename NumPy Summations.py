# Summations
# What is the difference between summation and addition?

# Addition is done between two arguments whereas summation happens over n elements.
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])
print(newarr)

# Summation Over an Axis
# If you specify axis=1, NumPy will sum the numbers in each array.
newarr = np.sum([arr1,arr2],axis=1)
print(newarr)


# Cummulative Sum
# Cummulative sum means partially adding the elements in array.
# E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
# Perfom partial sum with the cumsum() function.

arr = np.array([1,2,3,4,5]) 
print(np.cumsum(arr))

# NumPy Products
arr = [1,2,3,4,5]
x = np.prod(arr)
print(x)

# Find the product of the elements of two arrays:
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8]) 
x = np.prod([arr1,arr2]) 
print(x)


# Perform summation in the following array over 1st axis:
newarr = np.prod([arr1,arr2],axis =1) 
print(newarr)


# Cummulative Product
arr = np.array([5,6,7,8])
newarr = np.cumprod(arr)
print(newarr)


# Differences
# A discrete difference means subtracting two successive elements.

arr =np.array([10,15,25,5]) 
newarr = np.diff(arr)
print(newarr)

# Compute discrete difference of the following array twice:
newarr = np.diff(arr,n=2)
print(newarr)