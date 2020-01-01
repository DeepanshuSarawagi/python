# In this lesson we are going to learn about lists in Python.

parrot_list = ["Not pinin'", "no more", "a stiff", "bereft of life"]
for state in parrot_list:
    print(f"This parrot is {state}", end="\t")
# below code will show how to append an item to a list

parrot_list.append("A Norwegian Blue")
print()
print()

for state in parrot_list:
    print(f"This parrot is {state}")

print()

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers.sort()
print(numbers)
