# What is NumPy?

# NumPy is a Python library used for working with arrays.

# It also has functions for working in domain of linear algebra, fourier transform, and matrices.

# NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.

# NumPy stands for Numerical Python.

# Why Use NumPy?

# In Python we have lists that serve the purpose of arrays, but they are slow to process.

# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

# Arrays are very frequently used in data science, where speed and resources are very important.


# Why is NumPy Faster Than Lists?

# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

# This behavior is called locality of reference in computer science.

# This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.

# NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.


import numpy as np 

print(np.__version__)#check the Version of the numPy


#Create a NumPy ndarray Object

arr = np.array([1,2,3,4,5])
print(type(arr))

# Dimensions in Arrays

# 0-D Arrays
arr = np.array(42)
print(arr)
print(arr.ndim)

# 1-D Arrays
arr = np.array([1,2,3,4,5])
print(type(arr))
print("Dimension is : ",arr.ndim)

# 2-D Arrays
arr= np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)
print("Dimension is : ",arr.ndim)

# 3-D arrays
arr = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
print(arr)
print("Dimension is : ",arr.ndim)

# Higher Dimensional Arrays
# An array can have any number of dimensions.

# When the array is created, you can define the number of dimensions by using the ndmin argument.

arr = np.array([1,2,3,4],ndmin=5)
print(arr)
print("Number of Dimension is : ",arr.ndim)