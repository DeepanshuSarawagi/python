menu = [
    ["eggs", "spam", "eggs"],
    ["eggs", "bread", "bacon"],
    ["bread", "butter", "jam"],
    ["bread", "tofu", "cheese"],
    ["eggs", "spam", "spam", "milk"],
    ["milk", "cookies", "spam"],
    ["milk", "cookies", "cereal"],
    ["cookies", "butter"]
]
meals = []

for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append(f"a meal was skipped")

print(meals)
print()

# Lets try creating a solution using else clause in conditional comprehension

meals = [meal if "spam" not in meal else "a meal was skipped" for meal in menu]
print(meals)

"""As we can see in the output, we have produced identical outputs by creation a more complex expression. If we notice
here, filter is now part of the expression."""

x = 12
expression = "Tweleve" if x == 12 else "unknown"
print(expression)

print()

items = set()

for meal in menu:
    for item in meal:
        items.add(item)
print(items)

print()

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append(f"A meal containing spam was skipped")
print(meals)

for meal in menu:
    print(meal, "contains spam" if "spam" in meal else "contains bread" if "bread" in meal else "contains milk" if
          "milk" in meal else "contains egg")
# this is not a desired expression since meal defaults to egg if none of the above condition is satisfied

print()

for meal in menu:
    for item in items:
        if item in meal:
            print(f"A {meal} contains {item}")
            break

print()
count_fizz = 0
count_buzz = 0
count_fizzbuzz = 0
for x in range(1, 61):
    fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    if fizzbuzz == "fizz buzz":
        count_fizzbuzz += 1
    if fizzbuzz == "fizz":
        count_fizz += 1
    if fizzbuzz == "buzz":
        count_buzz += 1
    print(fizzbuzz)

print(f"There {count_buzz} buzz in this range")
print(f"There are {count_fizz} fizz in this range")
print(f"There are {count_fizzbuzz} fizzbuzz in this range")


