from array import *

my_array = array('i', [1, 2, 3, 4, 5])

for i in my_array:
    print(i)

print()

print(my_array[0])  # Accessing individual elements

# Append a value to the array. We can only insert at the end of array using append() method

my_array.append(6)
print(my_array)

# Insert an element in array at any position in an array
my_array.insert(0, 11)
print(my_array)

# Extend the array. Using this method we can extend the array with more than one value. The parameter passed in the
# extend() method should be an iterable object
my_array1 = array('i', [10, 11, 12])
my_array.extend(my_array1)
print(my_array)

# Insert the elements in an array from list
list1 = [20, 21, 22]
my_array.fromlist(list1)  # This will add extra three elements from the list at the end of this array
print(my_array)

# Remove an element from array
my_array.remove(11)  # This method will remove first occurrence of value/element in the array
print(my_array)

# Remove the last element from array using pop method
my_array.pop()
print(my_array)

# Fetch any element from array using index() method
print(my_array.index(21))

# Reverse an array
my_array.reverse()
print(my_array)

# Get the buffer info of an array
buffer = my_array.buffer_info()
print(buffer)  # This will print the buffer address of the array memory and also prints the no. of elements in an array

# Use the count method, to count the occurrence of an element in an array
my_array.append(11)
print(my_array.count(11))

# Convert the array to string
string_array = my_array.tostring()
print(string_array)

# Convert the string array to int using fromString() method
int_array = array('i')
int_array.fromstring(string_array)
print(int_array)
