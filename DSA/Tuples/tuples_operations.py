my_tuple = (1, 2, 3, 4, 5)
my_tuple1 = (1, 2, 6, 9, 8, 7, 1, 1, 1)

print(my_tuple1 + my_tuple)  # Concatenating two tuples using + operator

print(my_tuple * 4)  # This tuple creates a new tuple 4 times.

print( 1 in my_tuple)  # in operator returns boolean if the element exists in tuple

print(my_tuple1.count(1))  # This will return the count of element exists in tuple

print(my_tuple1.index(9))  # This returns the index of element passed as a parameter in the index() method

print(max(my_tuple1))
print(min(my_tuple1))
