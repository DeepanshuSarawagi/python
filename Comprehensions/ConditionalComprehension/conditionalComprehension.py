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

# Solution using conitional comprehension

print("Below is the solution using conditional comprehension")
meals = [meal for meal in menu if "spam" not in meal]

"""As we learned in previous lecture, list comprehension is a combination of expression and iteration. However, a 
conditional comprehension contains 'expression, iteration and filters'. As you can see in the above code, 
'if "spam" not in meal' is the filter which is applied to the conditional comprehension list. The list appends the items
only when the filter satisfies the condition.
"""

print(meals)
for good_meal in meals:  # iterate over the list of items when retrieved using conditional comprehension
    print(good_meal)
