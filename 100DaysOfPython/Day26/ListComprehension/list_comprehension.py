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
