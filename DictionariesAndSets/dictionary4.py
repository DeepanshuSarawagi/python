# Create the adventure game program in a more organised way as per the Udemy challenge.

locations = {0: {"desc": "You are sitting in front of the computer learning Python",
                 "exits": {},
                 "namedExits": {}},
             1: {"desc": "You are standing at the end of the road before a small brick building",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
             2: {"desc": "You are at the top of a hill",
                 "exits": {"N": 5, "Q": 0},
                 "namedExits": {"5": 5}},
             3: {"desc": "You are inside a building, a well house for small stream",
                 "exits": {"W": 1, "Q": 0},
                 "namedExits": {"1": 1}},
             4: {"desc": "You are in a valley beside a stream",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "namedExits": {"1": 1, "2": 2}},
             5: {"desc": "You are in the forest",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "namedExits": {"2": 2, "1": 1}}}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5", }

loc = 1
while True:
    availableExits = ", ".join(locations[loc]["exits"].keys())
    print(locations[loc]["desc"])
    if loc == 0:
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    chosenDirection = input("Available exits are " + availableExits + ": ").upper()
    if len(chosenDirection) > 1:
        words = chosenDirection.split()
        for word in words:
            if word in vocabulary:
                chosenDirection = vocabulary[word]

    if chosenDirection in allExits:
        loc = allExits[chosenDirection]
    else:
        print("You cannot go in that direction")
