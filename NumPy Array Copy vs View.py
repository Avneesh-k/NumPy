# The Difference Between Copy and View
# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

# COPY:
import numpy as np 

arr = np.array([1,2,3,4,5])
copy_arr = arr.copy()
arr[0] = 42 #does not change copy array 
print(copy_arr)
print(arr)

# VIEW:
arr = np.array([1,2,3,4,5])
view_arr = arr.view()
arr[0] = 42 #change the orginal array
print(arr)
print(view_arr)


# Check if Array Owns its Data

arr = np.array([1,2,3,4,5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)