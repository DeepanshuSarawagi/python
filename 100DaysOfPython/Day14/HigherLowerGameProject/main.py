import game_data
import random

# for i in range(len(game_data.data)):
#     list_of_keys = list(game_data.data[i].keys())
#     list_value = list(game_data.data[i].values())
#     print(list_of_keys)
#     print(list_value)
#     for j in range(len(list_of_keys)):
#         print("{}: {}".format(list_of_keys[j], list_value[j]))


for i in game_data.data:
    for key, value in i.items():
        print(key, value)
    print()

first_random = random.choice(game_data.data)
first_item = list(first_random.values())
second_random = random.choice(game_data.data)
second_item = list(second_random.values())

print(first_random)
print(second_random)

print()

print("Compare {}: {}, {}, {}, {}".format("A", first_item[0], first_item[1], first_item[2], first_item[3]))
print("Compare {}: {}, {}, {}, {}".format("B", second_item[0], second_item[1], second_item[2], second_item[3]))

choice = input("Who has more followers? Type 'A' or 'B': ").upper()

if choice == "A":
    if first_item[1] > second_item[1]:
        first_item = second_item
        second_item = list(random.choice(game_data.data).values())
        print(first_item)
        print(second_item)

