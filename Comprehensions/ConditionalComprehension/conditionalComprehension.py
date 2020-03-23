menu = [
    ["eggs", "spam", "eggs"],
    ["eggs, ""bread", "bacon"],
    ["bread", "butter", "jam"],
    ["panini", "tofu", "cheese"],
    ["eggs", "spam", "spam", "milk"],
    ["milk", "cookies", "spam"],
    ["milk", "cookies", "cereal"]
    ]

for meal in menu:
    if "spam" not in meal:
        print(meal)
