# We are going to create burgers using nested comprehension

burgers = ["veg", "paneer", "mexican"]

toppings = ["cheese", "salad", "jalepenos"]

meals = [(burger, topping) for burger in burgers for topping in toppings]

print(meals)
