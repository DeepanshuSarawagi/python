"""
In this project we are going to create a simple Calculator program.
This program will do basic mathematical operations like add, subtract, multiply and divide
"""


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for operate in operations:
    print(operate)
choice = input("Which operation would you like to perform? ")

function = operations[choice](num1, num2)

print("{} {} {} is = {}".format(num1, choice, num2, function))
