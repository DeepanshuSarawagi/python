import random
names = input("Please enter the names of people who joined for dinner separated by comma and space. Eg: A, B, C: ")
list_of_names = names.split(", ")
randomChoice = random.randint(0, (len(list_of_names) - 1))
print("{} will pay the bill today!".format(list_of_names[randomChoice]))

# Simplified solution by instructor using the random.choice() method to randomly pick an item from an iterative object
person_to_pay = random.choice(list_of_names)
print(person_to_pay + " will pay the bill today")
