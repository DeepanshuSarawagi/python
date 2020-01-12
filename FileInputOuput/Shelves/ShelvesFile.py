import shelve

with shelve.open("ShelfTest") as fruit:
    fruit_dict = {"orange": "A sweet, orange, citrus fruit",
             "apple": "good for making ciders",
             "lime": "A sour, green, citrus fruit",
             "grape": "A small, sweet fruit, growing in bunches",
             "lemon": "A sour, yellow, citrus fruit"}

print(fruit_dict["lime"])
print(fruit_dict["apple"])
print(fruit_dict)
"""A shelve is dictionary-like persistent object used to used for serialization of Python objects which can be pickled.
 The values of the dictionary in the shelve can be any class instances, recursive data types, and objects containing 
 lots of shared sub-objects. The keys are ordinary strings."""