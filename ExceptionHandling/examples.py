def factorial(n):
    """To calculate the factorial of n recursively."""

    if n <= 1:
        return 1
    else:
        print(n / 0)  # Merely to catch the exception and handle multiple exceptions
        return n * factorial(n-1)


try:
    print(factorial(900))
except RecursionError:
    print("This program cannot calculate large factorials")
    print("This program is terminating")
except ZeroDivisionError:
    print("What are you doing dividing by zero???")
