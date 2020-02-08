def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n+1):
            result *= f
    return result


for i in range(50):
    print(i, fact(i))

print("=" * 50)

"""Use recursive method to create a function to calculate n!"""


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)  # calling the function recursively


for i in range(50):
    print(i, factorial(i))

"""Write a program recursively to calculate fibonacci series"""


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    global result
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            # print(f"n_minus2 is now {n_minus2}")  # just to understand the code
            # print(f"n_minus1 is now {n_minus1}")
            # print(f"result is now {result}")
            n_minus2 = n_minus1
            # print(f"n_minus2 is now {n_minus2}")
            n_minus1 = result
            # print(f"n_minus1 is now {n_minus1}")
    return result


for i in range(36):
    print(i, fibonacci(i))
