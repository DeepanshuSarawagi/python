fruits = {"orange": "A sweet citrus food. Good for skin",
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
