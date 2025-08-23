# Random Permutations of Elements
# A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.

# The NumPy Random module provides two methods for this: shuffle() and permutation().

# Shuffling Arrays
# Shuffle means changing arrangement of elements in-place. i.e. in the array itself.
import numpy as np 
from numpy import random 

arr = np.array([1,2,3,4,5])
random.shuffle(arr) #The shuffle() method makes changes to the original array.
print(arr)

# Generating Permutation of Arrays

arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))#The permutation() method returns a re-arranged array (and leaves the original array un-changed).

