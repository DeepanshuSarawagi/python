print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Please enter a number and i'll tell you its square: "))

squares = [number ** 2 for number in numbers]

"""A list comprehension produces a list of items by evaluating the expression first for each
item in the list. Comprehensions are divided into two parts: 1) expression 2) Iteration
number ** 2 is the expression and it returns the number squared. Iteration over a sequence part 'for number in numbers'
is iterated except for the fact that a semicolon is not required in the end."""

index_pos = numbers.index(number)
print(index_pos)
print()
print(squares[index_pos])

# Udemy challenge 1 on list comprehension

# Write the below code using list comprehensions instead of for loop. print both the outputs and see if its producing
# the same results

text = input(" Please enter the text of your choice: ")

output = []
for t in text.split(' '):
    output.append(len(t))

print(output)
output = []
for t in text.split():
    output.append((t, len(t)))

print(output)

# solution using list comprehensions
text1 = input("Please enter a text of your choice: ")
listComp = []
[listComp.append(len(t)) for t in text1.split(" ")]
print()
print(listComp)

listComp1 = []
[listComp1.append((t, len(t))) for t in text1.split()]
print(listComp1)

inch_measurement = (3, 8, 20)

cm_measurement = [inch * 2.54 for inch in inch_measurement]
print(cm_measurement)
