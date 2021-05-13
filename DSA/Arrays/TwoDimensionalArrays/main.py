# Creating two dimensional arrays
# We will be creating it using a simple for loop

from array import *

two_d_array = []
for i in range(1, 11):
    two_d_array.append([i * j for j in range(2, 6)])

print(two_d_array)
