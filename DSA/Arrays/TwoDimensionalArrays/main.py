import numpy
# Creating two dimensional arrays
# We will be creating it using a simple for loop


two_d_array = []
for i in range(1, 11):
    two_d_array.append([i * j for j in range(2, 6)])

print(two_d_array)

twoDArray = numpy.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
print(twoDArray)

# Insertion in 2D array
new2DArray = numpy.insert(twoDArray, 1, [[21, 22, 23, 24]], axis=1)  # The first int parameter is the position
# where we want to add. And axis=1 denotes we want to add new values as columns, if axis=0, add it as rows

print(new2DArray)
