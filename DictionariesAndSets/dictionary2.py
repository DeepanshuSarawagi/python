locations = {0: "You are sitting in front of the computer learning Python",
             1: "You are standing at the end of the road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}
# We have created a dictionary containing the locations and its corresponding keys.
# Now we will create a list of dictionaries for available exits.

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:
    availableExits = ""
    for direction in exits[loc].keys():
        print(direction)
        availableExits += direction + ", "
    print(locations[loc])

    if loc == 0:
        break

    chosenDirection = input("Available exits are: " + availableExits).upper()
    if chosenDirection in exits[loc]:
        loc = exits[loc][chosenDirection]
        print(loc)
    else:
        print("You cannot go in that direction")
