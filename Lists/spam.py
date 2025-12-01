menu = [
        ["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "bacon", "sausage", "spam"],
        ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
        ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for item in meal:
            print(item)
    else:
        print("{} has spam score of {}".format(meal, meal.count("spam")))

print()

for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(meal)

menu = [
        ["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "bacon", "sausage", "spam"],
        ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
        ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for mean in menu:
    for item in mean:
        if item != "spam":
            print(item, end="\t")
    print()

print()

for meal in menu:
    items = ", ".join(item for item in meal if item != "spam")
    print(items)