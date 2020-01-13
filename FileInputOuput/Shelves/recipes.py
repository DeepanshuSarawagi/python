import shelve
blt = ["bacon", "lettuce", "tomato", "bread"]
bread_on_toast = ["bread", "tomato"]
pasta = ["pasta", "cheese", "broccoli"]
dessert = ["milk", "flour", "rice", "sugar"]

with shelve.open("recipes") as recipe:
    recipe["blt"] = blt
    recipe["bread on toast"] = bread_on_toast
    recipe["pasta"] = pasta
    recipe["dessert"] = dessert
