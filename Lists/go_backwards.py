data = [4, 104, 105, 110, 120, 130, 5, 360, 130, 150, 160, 350, 170, 183, 185, 187, 188, 191, 350, 360, 107, 120]
min_valid = 100
max_valid = 200

# for index in range(len(data) -1, -1, -1):
#
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]
# print(data)

reversed_list = list(reversed(data))  # Needs the data to be type-casted to list since the reversed() fn returns reversed iterator
print(reversed_list)

"""There is an efficient way of deleting the items from the list of unsorted data using the reversed function"""

top_index = len(data) -1

for index, value in enumerate(reversed_list):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]
print(data)