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
