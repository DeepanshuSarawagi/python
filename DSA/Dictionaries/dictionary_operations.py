my_dict = {
    "one": "uno",
    "two": "dos",
    "three": "tres",
    "four": "cuarto"
}

# Use of in operator in dictionary
print("one" in my_dict)  # This will return True if "one" key exists in my_dict keys
print("uno" in my_dict.values())

# In operator uses different algorithm in case of lists and dictionaries
# In lists, it uses the linear search algorithm. Meaning, the search time execution will increase when the elements in
# in the search increases
# But in case of dictionary, it uses the hash table. The in operator takes about same amount of time, no matter how many
# items are there in the dictionary. The in operator takes the key, it calculates the hash function, it compares it with
# its associated array and returns True or False

for key in my_dict:
    print(key)
