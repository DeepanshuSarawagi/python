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
