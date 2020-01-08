fruits = {"Orange": "A sweet orange citrus fruit, usually good for skin",
          "Apple": "Good for health if eaten once a day",
          "Lime": "A green sour/sweet citrus fruit",
          "Lemon": "A yellow sour citrus fruit, usually good with Vodka"}

print(fruits)
print(fruits.keys())
print(fruits["Lemon"])

vegetables = {"cabbage": {1: "Good for health"},
              "carrot": {2: "Good for eye"}}
print(vegetables["carrot"][2])  # Extracting the value from dictionary within dictionary


veg = {"Cabbage": "Good for health. Mostly preferred in salads",
       "Carrot": "Very good for eyes. Rich in Vitamin A",
       "Spinach": "High proteins. Good for hair and eyes",
       "Broccoli": "Very high proteins."}

print(veg)
print()
veg.update(fruits)  # We have updated the dictionary veg by adding fruits dictionary in it.
print()
print(veg)

print(fruits["Orange"].split())
print()

nice_veg = fruits.copy()  # Creating a new dictionary by copying fruits dictionary in it
nice_veg.update(veg)      # Updating the newly created dictionary by adding another dictionary "veg" in it
print(nice_veg)
print()

for f in sorted(nice_veg.keys()):
    print(f + " - " + nice_veg[f])

"""Continued dictionary challenge as per dictionary2.py We need to modify the program in such a way that users can 
enter the location name instead of the exits and the program should work."""

locations = {0: "You are sitting in front of the computer learning Python",
             1: "You are standing at the end of the road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}
# We have created a dictionary containing the locations and its corresponding keys.
# Now we will create a list of dictionaries for available exits.

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "2": 2},
              5: {"2": 2, "1": 1}}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    # for direction in exits[loc].keys():
    #     print(direction)
    #     availableExits += direction + ", "
    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])

    chosenDirection = input("Available exits are " + availableExits + ": ").upper()

    # We are going to create a for loop to check if the user input is in vocabulary
    if len(chosenDirection) > 1:
        words = chosenDirection.split()
        for word in words:
            if word in vocabulary:
                chosenDirection = vocabulary[word]

    if chosenDirection in allExits:
        loc = allExits[chosenDirection]
        print(loc)
    else:
        print("You cannot go in that direction")
