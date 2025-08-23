# Random number does NOT mean a different number every time. Random means something that can not be predicted logically.

# Generate Random Number
from numpy import random 

x = random.randint(100)
print(x)

# Generate a random float from 0 to 1:
x = random.rand()
print(x)


# Generate a 1-D array containing 5 random integers from 0 to 100:
x = random.randint(100, size=(5))
print(x)


# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
x = random.randint(100,size=(3,5))
print(x)

# Generate a 1-D array containing 5 random floats:
x = random.rand(5)
print(x)

# Generate a 2-D array with 3 rows, each row containing 5 random numbers:
x = random.rand(3,5)
print(x)

# Generate Random Number From Array
# The choice() method allows you to generate a random value based on an array of values.
# The choice() method takes an array as a parameter and randomly returns one of the values.

x = random.choice([1,2,3,4,5])
print(x)

# Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9)
x = random.choice([3,5,7,9],size=(3,5))
print(x)