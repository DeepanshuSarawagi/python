# In this lesson we are going to learn about list comprehension
# we will be creating lists using list

numbers = [1, 2, 3, 4, 5]
new_list = [(n + 1) for n in numbers]  # Here we are creating new list using existing list using list comprehension
print(new_list)

name = "Deepanshu"

new_list = [letter for letter in name]
print(new_list)

squared_list = [n * 2 for n in range(1, 5)]
print(squared_list)

# Conditional list comprehension

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Fred"]

short_names = [name for name in names if len(name) <= 4]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)

# Day 26 - Challenge 1

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)
