"""
In this project we are going to create a simple Calculator program.
This program will do basic mathematical operations like add, subtract, multiply and divide
"""
import os

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


def calculator():
    num1 = int(input("What's the first number?: "))

    def print_operations():
        for operate in operations:
            print(operate)

    print_operations()
    choice = input("Which operation would you like to perform? ")

    num2 = int(input("What's the second number?: "))

    function = operations[choice]

    result = function(num1, num2)

    print("{} {} {} is = {}".format(num1, choice, num2, result))

    should_continue = True

    def continue_operation(num):
        print_operations()
        choice = input("Which operation would you like to perform? ")
        num3 = int(input("Enter another number of your choice: "))
        function = operations[choice]
        another_result = function(num, num3)
        print("{:.2f} {} {:.2f} is = {:.2f}".format(num, choice, num3, another_result))
        return another_result

    while should_continue:
        to_continue = input("Do you want to continue the operation? Type 'y' for Yes or 'n' for No: ").lower()
        if to_continue == "y":
            result = continue_operation(num=result)
        else:
            should_continue = False
            os.system("clear")
            calculator()


calculator()
