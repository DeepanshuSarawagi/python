# We are going to practice some examples on Python on dictionary
# Exercise 1: Write a Python script to sort (ascending and descending) a dictionary by value.
vowels = {"a": "An apple a day keeps the doctor away",
          "e": "English is globally spoken.",
          "i": "India is a very beautiful country",
          "o": "Outstanding that you are practicing problems on Dictionary",
          "u": "Umbrella protects one from harsh weather"}
print(vowels)
print(vowels.keys())
print(vowels.items())
for f in sorted(vowels.keys()):
    print(f"{f} - {vowels[f]}")
print(sorted(vowels.values()))
reverse_vowels = sorted(vowels.values(), reverse=True)
print(reverse_vowels)

# Write a program to add a key in dictionary
multiples_of_tens = {1: 10,
                     2: 20,
                     3: 30,
                     4: 40}
print(multiples_of_tens)
multiples_of_tens[5] = 50
print(multiples_of_tens)

# Exercise 3: Write a Python script to concatenate following dictionaries to create a new one.
dict1 = {1: 10,
         2: 20}
dict2 = {3: 30,
         4: 40}
dict3 = dict1.copy()
dict3.update(dict2)
print("This solution is for Exercise 3: ", dict3)

# Solution proposed by someone else is as follows.
dict4 = {}

for d in (dict1, dict2):
    dict4.update(d)
print(dict4)

# Exercise 4: Write a Python script to check if a given key already exists in a dictionary.
dict1 = {"a": "value1",
         "b": "value2",
         "c": "value3",
         "d": "value4",
         "e": "value5"}
dict1_keys = sorted(dict1.keys())
new_key = input("Enter a key to update the dictionary: ")
if new_key in dict1_keys:
    print(f"The following key {new_key} is already present in the dictionary")
else:
    print("This is a new key")
