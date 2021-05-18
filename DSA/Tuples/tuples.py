new_t = ("a", "b", "c", "d", "e")
print(new_t)

# remember that tuples are immutable and hashable.

# If we want to create a tuple with just one element then we need to end it with a comma
new_t2 = ("a",)
print(new_t2)

tuple_1 = tuple("abcdefghijklmnopqrstuvwxyz")
print(tuple_1)

for i in range(len(tuple_1)):
    print(tuple_1[i])
