#  In this lesson we are going to learn about Nested Lists
# Nested lists is nothing but lists inside a list
# We can create two different lists and then combine them like this "new_list = [list1, list2]

# We are going to create a list of fruits and vegetables which has most pesticides residue.

vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Apple", "Nectarines", "Grapes", "Pears", "Peaches", "Cherries"]

dirty_dozen = [vegetables, fruits]
print(dirty_dozen)

# This is how we traverse through list of lists

for items in dirty_dozen:
    for item in items:
        print(item)
