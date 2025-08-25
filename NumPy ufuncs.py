# ufuncs stands for "Universal Functions" and they are NumPy functions that operate on the ndarray object.
# They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.

# ufuncs also take additional arguments, like:

# where boolean array or condition defining where the operations should take place.

# dtype defining the return type of elements.

# out output array where the return value should be copied.

# What is Vectorization?
# Converting iterative statements into a vector based operation is called vectorization.
# It is faster as modern CPUs are optimized for such operations.


# Example 
# without ufunc, we can use python's built-in zip() method:

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)

# NumPy has a ufunc for this, called add(x, y) that will produce the same result.
import numpy as np 
x = [1,2,3,4,5] 
y = [4,5,6,7,9] 
z = np.add(x,y)
print(z)