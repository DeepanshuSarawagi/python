print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

squares = [number ** 2 for number in numbers]

"""A list comprehension produces a list of items by evaluating the expression first for each 
item in the list. Comprehensions are divided into two parts: 1) expression 2) Iteration
number ** 2 is the expression and it returns the number squared. Iteration over a sequence part 'for number in numbers'
is iterated except for the fact that a semicolon is not required in the end."""

print(squares)
