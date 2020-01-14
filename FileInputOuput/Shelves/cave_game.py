import shelve

locations = shelve.open("locations")
vocabulary = shelve.open("vocabulary")

loc = "1"
while True:
    availableExits = ", ".join(locations[loc]["exits"].keys())
    print(locations[loc]["desc"])
    if loc == "0":
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

vocabulary.close()
locations.close()