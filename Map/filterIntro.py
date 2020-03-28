menu = [["eggs", "spam", "milk"],
        ["milk", "bread", "butter"],
        ["bread", "bacon", "cheese"],
        ["eggs", "spam", "spam"],
        ["bread", "spam", "eggs"],
        ["salad", "bread", "cheese"],
        ["salad", "spam"],
        ["cheese", "tofu", "salad"]]

for meal in menu:
    if "spam" not in meal:
        print(meal)

print("------------------------------")
# using list comprehension

meals = [meal for meal in menu if "spam" not in meal]
print(meals)

print("------------------------------")


def not_spam(meal_list: list):
    return "spam" not in meal_list


spamless_meal = list(filter(not_spam, menu))
print(spamless_meal)

