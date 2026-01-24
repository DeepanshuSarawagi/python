def fibonacci_number(n):
    """
    This function returns the `n` th Fibonacci number for the positive `n`.
    :param n: The number to return.
    """

    if 0 <= n <= 1:
        return n
    result = None
    n_minus1, n_minus2 = 1, 0
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    return result


for i in range(40):
    print(i, fibonacci_number(i))