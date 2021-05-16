integers = [1, 2, 3, 4, 5]
print(integers)

shopping_list = ["Milk", "Eggs", "Bacon", "Cheese", "Bread"]
print(shopping_list)

mixed_list = [45, "food", 87.5, 100, "spam"]
print(mixed_list)

nested_list = [1, 2, 3, 5, [1.6, 1.7], ["spam", "eggs"]]
print(nested_list)

print("milk".title() in shopping_list)

for i in shopping_list:
    print(i)

print(shopping_list[-1])

print(shopping_list[::-1])  # printing the list in reverse order

sum_of_items = 0
for i in range(len(integers)):
    sum_of_items += integers[i]

print(sum_of_items)

# Updating the list

shopping_list[2] = "Tofu"
print(shopping_list)

shopping_list.insert(3, "Apples")
print(shopping_list)

shopping_list.append("Mulberry")
print(shopping_list)

dry_fruits = ["Walnuts", "Almonds", "Cashew"]
shopping_list.extend(dry_fruits)
print(shopping_list)

# Slicing elements from a list

print(shopping_list[0:3])

new_list = shopping_list[0:3]
print(new_list)

new_shopping_list = shopping_list[0::2]  # This will omit every alternative element from the list and create new list
print(new_shopping_list)

shopping_list.pop(1)  # Delete an element from the list at a given index
print(shopping_list)

shopping_list.remove("Cheese")
del shopping_list[1]
print(shopping_list)

if 4 in integers:
    print("Found the element")


def searchInList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return "The value does not exist in the list"


print(searchInList(shopping_list, "Apples"))

# List operations and functions
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# We can increase the elements in the list by n times using the * operator

a = [1, 2, 3, 4]
b = 4
c = a * b  # the list will have repetitive elements 4 times
print(c)

# max function returns the highest value in the list

list1 = [98, 65, 57, 89, 99, 88, 47]
print(max(list1))

print(min(list1))

print(sum(list1))  # This will return the sum of all the elements in the list

values = []
while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    values.append(float(inp))

print("Average = {}".format(sum(values) / len(values)))

# creating a list from string

string = "abcdefghi"
list_of_strings = list(string)
print(list_of_strings)

words = "This is a sentence and it will be converted into a list of words"
list_of_words = words.split(" ")
print(list_of_words)
