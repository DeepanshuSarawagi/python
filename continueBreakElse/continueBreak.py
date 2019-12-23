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
# In the above example, when we use a break statement in loop, if item matches spam in the "meal" list, the for loop
# breaks and stops executing further. This is a basic difference between continue and break.

# Coding exercise on using break

for i in range (0, 100, 7):
    print(i)
    if i > 0 and (i % 11) == 0:
        break
