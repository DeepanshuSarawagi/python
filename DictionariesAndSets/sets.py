# Just like dictionaries, even sets can be defined in the curly parenthesis.
# Let's create a set and assign to be variable farm_animals

farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)
print("=" * 50)

wild_animals = set(["lion", "tiger", "panther", "wild elephant", "cheetah", "leopard"])
"""Ignore the above warning, we are just learning different methods to define a set."""
# wild_animals = set(wild_animals)
print(wild_animals)
for animal in wild_animals:
    print(animal)
wild_animals = sorted(wild_animals)  # we can also sort a set and it will return the list of sorted items in it
print("=" * 50)
print(wild_animals)

"""It is also easy to add an item in the set by using the add() method."""
farm_animals.add("buffalo")
"""Since I sorted wild_animals, I cannot use the add method now. Hence, first we need to convert the sorted list of 
wild_animals to set."""
wild_animals = set(wild_animals)
wild_animals.add("horse")
print("=" * 50)
print(farm_animals)
print(wild_animals)

"""Notice the warning on line 11, when you hover over the warning it says, ""Function call can be replaced with set 
literal. Sometimes, we need to define the set function when we want to create an empty set. Because empty curly braces
would create a dictionary and not a set. Refer to below code for illutration."""

empty_set = set()
empty_set2 = {}
empty_set.add("6")
#empty_set2.add("6")
"""Notice on line 38 that add method is not available since it is an empty dictionary and not a set.
(Uncomment the code on line 38 to understand more)"""
print(empty_set)
"""We can use any iterable object such as lists, tuples or ranges to create a set"""
even = set(range(0, 40, 2))
print(even)
even_tuple = (2, 4, 6, 8, 10)
even_set = set(even_tuple)
print(even_set)
print("=" * 50)
"""We can also perform operations like union, intersection, subset and superset on any object which is a set data 
type. Union operation on two sets can be performed using the union() method"""
odd = set(range(1, 40, 2))
print(odd)
print(len(odd))
squares_tuple = (1, 4, 9, 36)
squares = set(squares_tuple)
print(squares)
print(len(squares))
print(odd.union(squares))
print(len(odd.union(squares)))
"""Intersection method can be performed using the intersection() method or we can use the & symbol and python will 
recognise it as intersection because it is a built-in type"""
print(odd.intersection(squares))
print("=" * 50)
print(odd & squares)
"""When you print line 63 and 64, you will get the same output"""
