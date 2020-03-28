import timeit

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


def spamless_comp():
    # meals = [meal for meal in menu if "spam" not in meal]
    meals = [meal for meal in menu if not_spam(meal)]
    return meals


print("------------------------------")


def not_spam(meal_list: list):
    return "spam" not in meal_list


def spamless_filter():
    spamless_meal = list(filter(not_spam, menu))
    return spamless_meal


if __name__ == "__main__":
    print(timeit.timeit(spamless_comp, number=100000))
    print(timeit.timeit(spamless_filter, number=100000))
