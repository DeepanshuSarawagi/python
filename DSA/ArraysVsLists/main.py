import numpy

myArray = numpy.array([1, 2, 3, 4, 5, 6])
print(myArray)
myList = [1, 2, 3, 4, 5, 6]
print(myList)

# Advantage of array over lists is that we can perform mathematical operations on array of values but on list of values

print(myArray / 2)  # This will divide every element by 2
# print(myList / 2)  # This will error out

# Second difference is that in arrays all the elements should be of same datatype but that is not the case with lists
myArray = numpy.array([1, 2, 3, 4, 5, 6, 'a'])
myList = [1, 2, 3, 4, 5, 6, 'a']
print(myArray)
print(myList)