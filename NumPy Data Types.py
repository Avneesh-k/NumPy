# strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"

# integer - used to represent integer numbers. e.g. -1, -2, -3

# float - used to represent real numbers. e.g. 1.2, 42.42

# boolean - used to represent True or False.

# complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j

# Data Types in NumPy:
# NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc

# checking datatypes in numpy 
import numpy as np

arr = np.array([1,2,3,4])
print(arr.dtype)

arr = np.array(['apple','banana','mango'])
print(arr.dtype)

arr = np.array(['Avneesh'],dtype='U6') #U6 stands for unicode means it can store the string with length 6 you can increase it U7,U8.....
print(arr)

# Creating Arrays With a Defined Data Type

arr = np.array([1,2,3,4,5],dtype='S') #tells numpy to store the data as byte string[b'1,b'2,...]
print(arr)

arr = np.array([1,2,3,4,5],dtype='i4') #i4 = 32 bit signed integer.
print(arr)


# Converting Data Type on Existing Arrays
# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

# The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

arr = np.array([1.1,2.1,3.1,4.1,5.1]) 
newarr = arr.astype('i') #create a copy of the array 

print(newarr)
print(newarr.dtype)

newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

arr = np.array([1,0,3]) #when you convert numbers to bool in python 0 is stands for false and all non zero element are convert in the true.
newarr = arr.astype(bool)
print(newarr)

