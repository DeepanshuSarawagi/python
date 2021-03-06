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
"""Intersection method can be performed using the intersection() method or we can use the "&" symbol and python will 
recognise it as intersection because it is a built-in type"""
print(odd.intersection(squares))
print("=" * 50)
print(odd & squares)
"""When you print line 63 and 64, you will get the same output"""

"""We can also perform the difference operation on sets. When you do print(setA.difference(setB)), it will remove the 
common items between setA and setB and print rest of the items in setA"""
print("odd minus squares")
print(odd.difference(squares))
print(odd - squares)
print("squares minus odd")
print(squares.difference(odd))
print(squares - odd)
print("=" * 50)
print(odd)
"""We can also perform the difference_update() method on the sets. When we do setA.difference_update(setB), python 
updates setA by removing the common items between setA and setB. As you can see, we performed a difference operation on 
odd and then printed set odd on line 76. Now we will perform difference_update() operation on "odd" set and then print
it. Look at the below example to understand more."""
odd.difference_update(squares)
print(odd)
"""As you can see on line 82, it has permanently removed the items "1" and "9" from the set "odd" since we performed
difference_update operation as per code on line 81."""

"""Symmetric difference in Python is nothing but union of elements that are in either setA or in setB but not in 
both of them. Please refer to below example."""

letters = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
           "v", "w", "x", "y", "z"}
print(letters)
vowels = {"a", "e", "i", "o", "u"}
print(sorted(letters.symmetric_difference(vowels)))
"""When you prin the line 93, you can see that python has printed only those elements which are either in set ""letters,
or in set "vowels" but not in both of them. We have sorted the items for easy reading/understanding."""

"""How to discard/remove items from the sets? We can perform the discard() or remove() method on sets"""
letters.remove("a")
letters.discard("e")
print(letters)
vowels.discard("d")
# vowels.remove("d")  # This will throw an error since "d" is not an item of set "vowels".

# We will look into the try and catch exceptions, for now just understand the below code.
try:
    vowels.remove("d")
except KeyError:
    print("'d' is not a member of set 'vowels'.")

"""Final two operations on sets are subset and superset. We need to use the issubset() or issuperset() method to
perform these operations."""
letters.add("a")
letters.add("e")

if vowels.issubset(letters):
    print("vowels is a subset of letters")
if letters.issuperset(vowels):
    print("letters is a superset of vowels")

myString = input("Please enter a string of your choice: ").lower()
myString = set(myString)
vowels = {"a", "e", "i", "o", "u"}

print(sorted(myString.difference(vowels)))
