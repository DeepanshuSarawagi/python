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

"""We can also retrieve the values using the keys in the dictionaries by using the below while loop."""
# while True:
#     dictKey = input("Please enter a fruit name: ")
#     if dictKey == "quit":
#         break
#     if dictKey == "":
#         print("Fruit Name cannot be empty")
#         dictKey = input("Please enter a fruit name: ")
#     if dictKey in fruits:
#         description = fruits.get(dictKey)
#         print(description)
#     else:
#         print(f"We don't have {dictKey}")

"""We have commented out above code to retreive the key:value pairs from dictionary by using an alternative way."""

while True:
    dictKey = input("Please enter a fruit name: ")
    if dictKey == "quit":
        break
    description = fruits.get(dictKey, "We don't have a " + dictKey)
    print(description)

"""we can also print just the corresponding values of the individual keys in the dictionary by using a for loop"""

for snack in fruits:
    print(snack, fruits[snack])
print()

"""Whenever we retrieve a key value pair in dictionary, the value of key changes. To understand more, run the below
code and see that the order is getting changed."""
for i in range(10):
    for snack in fruits:
        print(snack + " is " + fruits[snack])
    print("=" * 50)

print()
# ordered_keys = list(fruits.keys())
# ordered_keys.sort()
ordered_keys = sorted(list(fruits.keys()))
for f in ordered_keys:
    print(f + " - " + fruits[f])

"""reduced line of code for sorting the keys in alphabetical order"""
print()

for f in sorted(fruits.keys()):
    print(f + " - " + fruits[f])

print("=" * 50)
fruit_keys = fruits.keys()
print(fruit_keys)

print("=" * 50)
fruits["Tomato"] = "A fruit but normally eaten as a salad"
print(fruit_keys)
print("=" * 50)
print(fruits)
print("=" * 50)
print(fruits.items())
f_tuple = tuple(fruits.items())
print(f_tuple)
print()
for i in f_tuple:
    name, description = i
    print(name + " - " + description)

"""We will learn how to use join() method on the immutable objects such as string."""
print()
myList = ["a", "b", "c", "d"]
newString = ", ".join(myList)
print(newString)

letters = "abcdefghijklmnopqrstuvwxyz"
newLetters = ", ".join(letters)
print(newLetters)
