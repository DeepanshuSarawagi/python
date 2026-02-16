def factorial(n: int) -> int:
    """
    A function that returns the factorial of a number.
    :param n: The number to calculate the factorial of.
    :return: The factorial of n.
    """
    if n <= 1:
        return 1
    return n * factorial(n-1)


for i in range(36):
    print(i, factorial(i))