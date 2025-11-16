computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable"]

"""Carefully observe below code where you will see how Python behaves when you want to replace an item in a list using list slicing"""
# computer_parts[3:5] = "trackball"  # This will output ['computer', 'monitor', 'keyboard', 't', 'r', 'a', 'c', 'k', 'b', 'a', 'l', 'l', 'hdmi cable']
# To resolve this issue, following is the right way of ding it
computer_parts[3:5] = ["trackball"]
print(computer_parts)

# Delete items from a list

data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]

"""While removing items from a sorted list, things can go horribly wrong when we move forward during iteration since the
length of the list changes and the index can get messed up."""

"""Below code which is commented out will illustrate the problem"""

min_value = 100
max_value = 200

# for index, value in enumerate(data):
#     if value < min_value or value > max_value:
#         del data[index]
# print(data)

"""Hence to solve this problem since this is a sorted list, we can remove items from the start and end of the list"""

start = 0

for index, value in enumerate(data):
    if value >= min_value:
        start = index
        break
del data[:start]
print(data)

stop = 0
for index in range(len(data) -1, -1, -1):
    if data[index] <= max_value:
        stop = index + 1
        break

del data[stop:]
print(data)

"""The above example is good if list is small and is sorted, however, if you are dealing with large data, this is not very
efficient."""

