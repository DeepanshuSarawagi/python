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
