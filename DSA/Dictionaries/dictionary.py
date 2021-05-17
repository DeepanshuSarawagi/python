engToEsp = {
    "one": "uno",
    "two": "dos",
    "three": "tres"
}

print(engToEsp)
print(engToEsp["one"])

# Insert/update element in a dictionary
my_dict = {
    "name": "Deepanshu",
    "age": 26
}

my_dict["age"] = 36
print(my_dict)

my_dict["address"] = "location a/b"
print(my_dict)


def traverse_dict(dictionary):
    for key in dictionary.keys():
        print("{}: {}".format(key, dictionary[key]))


traverse_dict(my_dict)

# Searching an element in a dictionary


def search_dictionary(dictionary, value):
    for key in dictionary.keys():
        if dictionary[key] == value:
            return key, value
    return "The value doesn't exist in the dictionary"


print(search_dictionary(my_dict, 26))
