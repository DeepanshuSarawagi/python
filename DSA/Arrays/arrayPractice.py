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
