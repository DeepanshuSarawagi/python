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

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

with open("file1.txt", "r") as file1:
    list1 = file1.readlines()
    final_list1 = []
    for li in list1:
        li = int(li.strip("\n"))
        final_list1.append(li)

with open("file2.txt", "r") as file2:
    list2 = file2.readlines()
    final_list2 = []
    for li in list2:
        li = int(li.strip("\n"))
        final_list2.append(li)

print(final_list1)
print(final_list2)

common_numbers = [num for num in final_list1 if num in final_list2]
print(common_numbers)
