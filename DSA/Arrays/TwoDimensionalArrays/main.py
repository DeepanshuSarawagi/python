# Creating two dimensional arrays
# We will be creating it using a simple for loop

from array import *

two_d_array = []
for i in range(1, 11):
    two_d_array.append([i * j for j in range(2, 6)])

print(two_d_array)

import numpy

twoDArray = numpy.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
print(twoDArray)
