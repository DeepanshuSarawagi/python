import shelve
blt = ["bacon", "lettuce", "tomato", "bread"]
bread_on_toast = ["bread", "tomato"]
pasta = ["pasta", "cheese", "broccoli"]
dessert = ["milk", "flour", "rice", "sugar"]
soup = ["tomato soup"]

# with shelve.open("recipes") as recipe:
#     recipe["blt"] = blt
#     recipe["bread on toast"] = bread_on_toast
#     recipe["pasta"] = pasta
#     recipe["dessert"] = dessert
#     recipe["soup"] = soup
#
#     # recipe["blt"].append("butter")    # this will not work. Although we have updated the list but have not triggered
#     #                                   # the sheleve to update it
#     # recipe["pasta"].append("tomato")  # same is the case here
#
#     temp_list = recipe["blt"]         # creating a temporary list
#     temp_list.append("butter")        # we are then appending the value we want to add in the list
#     recipe["blt"] = temp_list         # assigning the temp_list to recipe["blt"]. This is method 1 used to update shelve
#     temp_list = recipe["pasta"]
#     temp_list.append("tomato")
#     recipe["pasta"] = temp_list
#
#     for snack in recipe:
#         print(snack, recipe[snack])

"""Let's learn about updating shelves using method 2 which is adding a named argument while opening the shelve.
set writeback=True. For now lets comment the above code and rewrite the code below."""

with shelve.open("recipes", writeback=True) as recipe:
    recipe["blt"] = blt
    recipe["bread on toast"] = bread_on_toast
    recipe["pasta"] = pasta
    recipe["dessert"] = dessert
    recipe["soup"] = soup

    # recipe["blt"].append("butter")    # this will not work. Although we have updated the list but have not triggered
    #                                   # the shelve to update it
    # recipe["pasta"].append("tomato")  # same is the case here

    temp_list = recipe["blt"]         # creating a temporary list
    temp_list.append("butter")        # we are then appending the value we want to add in the list
    recipe["blt"] = temp_list         # assigning the temp_list to recipe["blt"]. This is method 1 used to update shelve
    temp_list = recipe["pasta"]
    temp_list.append("tomato")
    recipe["pasta"] = temp_list
    recipe["soup"].append("bread crumbs")

    del recipe["pasta"][4]  # did this because I added duplicate entry in the shelve
    del recipe["soup"][2]   # did this because I added duplicate entry in the shelve
    for snack in recipe:
        print(snack, recipe[snack])