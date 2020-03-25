# We are going to create burgers using nested comprehension

burgers = ["veg", "paneer", "mexican"]

toppings = ["cheese", "salad", "jalepenos"]

meals = [(burger, topping) for burger in burgers for topping in toppings]

print(meals)
print()

meals = []
for burger in burgers:
    for topping in toppings:
        meals.append((burger, topping))

print(meals)

print("*" * 50)

for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(nested_meals)

print()

nested_meals = []
for topping in toppings:
    for burger in burgers:
        nested_meals.append((burger, topping))

print(nested_meals)

# Nested for loop to nested comprehension challenge
# Create a nested comprehension by converting below for loop

print()
for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)

times_table = [f"{i} {i*j}" for i in range(1, 11) for j in range(1, 11)]
print(times_table)
