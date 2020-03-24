#  Modify the below code using list comprehensions.

for x in range(1, 61):
    fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)

fizzbuzz1 = ["fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz"
             if x % 5 == 0 else str(x) for x in range(1, 31)]
print(fizzbuzz1)

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

# loc = 5
# forest = [locations[exit] for exit in exits if loc in exits[exit].values()]
# print(forest)

# print the locations and its keys as a tuple

loc = 5
forest = [(exit, locations[exit]) for exit in exits if loc in exits[exit].values()]
print(forest)

for loc in sorted(locations):
    forest = [(exit, locations[exit]) for exit in exits if loc in exits[exit].values()]
    print(f"Locations leading to {loc}", end='\t')
    print(forest)

# convert comprehensions to for loop
print("* " * 40)


for loc in sorted(locations):
    forest = []
    for xit in exits:
        if loc in exits[xit].values():
            forest.append((xit, locations[xit]))
    print(f"Locations leading to {loc}", end='\t')
    print(forest)
