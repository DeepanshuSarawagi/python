shopping_list = ["milk", "bread", "pasta", "batter", "spam", "cheese", "butter"]
for item in shopping_list:
    if item == "spam":
        continue
    print(f"Buy {item}")

# In this example, we are learning about continue. As soon as the item in the list matches "spam", python skips and
# moves on to the next item in the list. This is the use of continue in loops.

meal = ["milk", "bread", "wheat", "spam", "cheese"]
for item in meal:
    if item == "spam":
        print("Can`t I have a meal without {}".format(item))
        break
