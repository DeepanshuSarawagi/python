# In this lesson we are going to learn about the lists in Python
# We can initialise an empty list by just using the empty square brackets
# Or add items in the list by enclosing items in the square brackets separated by commas
# We can add items to the end of the list by using the append() function or extend the list by using the
# extend() function.

cities_of_india = ["Ahmedabad", "Bengaluru", "Chennai", "Delhi", "Hyderabad", "Pune", "Agra", "Gwalior"]
# cities_of_india.sort()
print(cities_of_india)
cities_of_india.append("Jaipur")
print(cities_of_india)
cities_of_india.extend(["Mumbai", "Thiruvananthapuram"]) # Notice that we need to have the iterable items passed as an
# argument in the extend function of lists
print(cities_of_india)
