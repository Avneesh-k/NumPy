# There are primarily five ways of rounding off decimals in NumPy:

# truncation
# fix
# rounding
# floor
# ceil

# Truncation
# Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
import numpy as np

arr = np.trunc([-3.1666, 3.6667])
print(arr)

arr = np.fix([-3.1666, 3.6667])
print(arr)


# Rounding

# The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
# E.g. round off to 1 decimal point, 3.16666 is 3.2

arr = np.around(3.6666, 2)
print(arr)


# Floor
# The floor() function rounds off decimal to nearest lower integer.
# E.g. floor of 3.166 is 3.

arr = np.floor([-3.1666,3.6667])
print(arr)


# Ceil
# The ceil() function rounds off decimal to nearest upper integer.
# E.g. ceil of 3.166 is 4.

arr = np.ceil([-3.1666,3.6667]) 
print(arr)


# Logs
# NumPy provides functions to perform log at the base 2, e and 10.

# We will also explore how we can take log for any base by creating a custom ufunc.

# Log at Base 2
# Use the log2() function to perform log at the base 2.

arr = np.arange(1,10)
print(np.log2(arr))

# Log at Base 10
# Use the log10() function to perform log at the base 10.
print(np.log10(arr))


# Natural Log, or Log at Base e
# Use the log() function to perform log at the base e.
print(np.log(arr))