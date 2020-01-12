import shelve
with shelve.open("ShelfTest") as fruit:
    fruit["orange"] = "A sweet, orange, citrus fruit"
    fruit["apple"] = "good for making ciders"
    fruit["lime"] = "A sour, green, citrus fruit"
    fruit["grape"] = "A small, sweet fruit, growing in bunches"
    fruit["lemon"] = "A sour, yellow, citrus fruit"

    print(fruit["lemon"])
    print(fruit["lime"])

"""A shelve is dictionary-like persistent object used to used for serialization of Python objects which can be pickled.
 The values of the dictionary in the shelve can be any class instances, recursive data types, and objects containing 
 lots of shared sub-objects. The keys are ordinary strings."""