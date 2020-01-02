# In this lesson we are going to learn about lists in Python.

parrot_list = ["Not pinin'", "no more", "a stiff", "bereft of life"]
for state in parrot_list:
    print(f"This parrot is {state}", end="\t")
# below code will show how to append an item to a list

parrot_list.append("A Norwegian Blue")
print()
print()

for state in parrot_list:
    print(f"This parrot is {state}")

print()

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers.sort()
print(numbers)

print(list("The lists are equal"))  # Python will automatically create a list and print the list of characters.
print()
even = [2, 4, 6, 8]
another_even = even
another_even.sort(reverse=True)
print(even)

print()

numbers = [even, odd]
print(numbers)  # This will return a list containing two lists.

print()

for number_set in numbers:
    print(number_set)  # this will print the list members
    for value in number_set:
        print(value)  # this will print the members of the individual lists.

# Lists challenge

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])
print()
print(menu)

# write a program in such a way that it finds a meal without spam and then prints out each individual ingredients of the
# meal
print()

for meal in menu:
    if "spam" not in meal:
        for ingredients in meal:
            print(ingredients)
