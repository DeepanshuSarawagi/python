parrot = "Norwegian Blue"

for char in parrot:
    print(char)

numbers = input("Please enter a series of numbers using any separators ';,.:': ")
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

# using continue

for item in shopping_list:
    if item == "spam":
        continue
    print("Buy " + item)