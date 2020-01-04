fruits = {"Orange": "A sweet citrus food. Good for skin",
          "Apple": "A sweet fruit, largely grown in Kashmir, India.",
          "Lime": "A sour green citrus fruit",
          "Lemon": "A sour yellow citrus fruit",
          "Grapes": "A small sweet fruit grown in bunches"}
print(fruits)
print(fruits["Lemon"])
print(fruits["Lime"])
"""Another useful data type in Python is Dictionary. Unlike sequences which are indexed by range of values, dictionaries
are indexed by keys. Dict keys can be any immutable types such as strings and numbers. Tuples can be used as keys which
can be any strings or numbers or tuples. But if a tuple contains any mutable type like lists then it cannot be used as 
Dict Key since it can changed using indexing, slicing or methods like append() and extend().

In the above example, anything before colon is a dict key and their corresponding entry is the value"""

bike = {"make": "Bajaj",
        "model": "Pulsar 200NS",
        "capacity": "200CC",
        "color": "Blue",
        "year": 2013}
print(bike)
print(bike["year"])
print(bike["model"])

"""We can also add a key: pair value to dictionary like below."""
fruits["Pear"] = "An odd shaped green apple"
print(fruits)
print()
"""When we assign a new value to the already existing key in the dictionary, we end up replacing the value rather than
creating new entry. Let's below example to understand more."""
fruits["Pear"] = "Great with Tequila"
print(fruits)

"""We can also delete a key: value pair in dictionary using del in Python."""
del fruits["Pear"]
"""In the above code on line 35, we have issued a del command to the dictionary asking it to delete Key "Pear" and 
its value. Let's print fruits to confirm it."""

print(fruits)

"""We can also retreive the values using the keys in the dictionaries by using the below while loop."""
while True:
    dictKey = input("Please enter a fruit name: ")
    if dictKey == "quit":
        break
    if dictKey == "":
        print("Fruit Name cannot be empty")
        dictKey = input("Please enter a fruit name: ")
    if dictKey in fruits:
        description = fruits.get(dictKey)
        print(description)
    else:
        print(f"We don't have {dictKey}")
