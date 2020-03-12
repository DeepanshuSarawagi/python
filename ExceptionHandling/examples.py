import sys


def factorial(n):
    """To calculate the factorial of n recursively."""

    if n <= 1:
        return 1
    else:
        print(n / 0)  # Merely to catch the exception and handle multiple exceptions
        return n * factorial(n-1)


try:
    print(factorial(900))
except (RecursionError, ZeroDivisionError):
    print("This program cannot calculate large factorials")
    print("This program is terminating")


def getInt(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid Number, please try again")
        except EOFError:
            sys.exit(1)
        finally:
            print("The finally clause always executes if there is error or not.")

        """Use this clause to do something even if there is error in program. You can use finally clause to close the 
        cursors, db connections, print out a message when the program finished executing."""


first_number = getInt("Please enter first number: ")
second_number = getInt("Please enter second number: ")

try:
    print(f"{first_number} divided by {second_number} is {first_number/second_number}")
except ZeroDivisionError:
    print("You cant divide a number by zero.")
    sys.exit(2)
