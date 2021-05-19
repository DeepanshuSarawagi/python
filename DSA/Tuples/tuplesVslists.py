list1 = [0, 1, 2, 3, 4, 5, 6]
list1[1] = 3
list1 = [7, 6, 5, 4, 3]
print(list1)

del list1[0]
print(list1)

tuple1 = (0, 1, 2, 3, 4, 5, 6, 7)
# tuple1[1] = 8  # Tuples are immutable
print(tuple1)

tuple1 = (7, 8, 10, 9, 15, 11)
print(tuple1)  # We can reassign entire tuple but we cannot change single element of a tuple
print(tuple1[1:4])
# del tuple1[1] tuple doesnt support item deletion

list2 = [(1, 2), (3, 4), (5, 6)]  # Storing list of tuples
print(list2)

tuples2 = ([1, 2], [3, 4], [5, 6])
print(tuples2)  # Storing tuple of lists

nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)
