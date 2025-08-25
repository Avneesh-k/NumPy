# To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

# The frompyfunc() method takes the following arguments:

# function - the name of the function.
# inputs - the number of input arguments (arrays).
# outputs - the number of output arrays.

import numpy as np 

def myadd(x,y):
    return x+y 

myadd = np.frompyfunc(myadd,2,1) 

print(myadd([1,2,4],[5,6,7]))


# Check if a Function is a ufunc
# Check the type of a function to check if it is a ufunc or not.

# A ufunc should return <class 'numpy.ufunc'>.
print(type(myadd))

# Simple Arithmetic

# Addition
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)
print(newarr)

# Subtraction 
newarr = np.subtract(arr1,arr2)
print(newarr)

# Multiplication
newarr = np.multiply(arr1,arr2) 
print(newarr)

# Division
newarr = np.divide(arr1,arr2)
print(newarr)

# Power
newarr = np.power(arr1,arr2)
print(newarr)