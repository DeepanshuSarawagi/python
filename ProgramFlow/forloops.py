parrot = "Norwegian Blue"

for char in parrot:
    print(char)
numbers = "123,456,789"
for char in numbers:
    print(char)
print(numbers)
separator = ""

for char in numbers:
    if not char.isnumeric():
        separator = separator + char

print(separator)

values = "".join(char if char not in separator else " " for char in numbers).split()

int_values = sum([int(val) for val in values])
print(int_values)

shopping_list = ["milk", "pasta", "cottage cheese", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# using continue statement

for item in shopping_list:
    if item == "spam":
        continue
    print("Buy " + item)

print()

# Using break statement
for item in shopping_list:
    if item == "spam":
        break
    print("Buy " + item)

# Searching exercise

print()
item_to_find = "spam"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

print("Found {} at index {}".format(item_to_find, found_at))

item_to_find = "albatross"
found_at = None
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

if found_at is not None:
    print("Found {} at index {}".format(item_to_find, found_at))
else:
    print("{} not found".format(item_to_find))