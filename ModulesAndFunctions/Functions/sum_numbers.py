def sum_numbers(*numbers: int)-> int:
    """
    Sums a variable number of integer arguments and returns the result.

    Parameters:
        *numbers: Variable number of integer arguments to be summed.

    Returns:
        int: The sum of the provided integer arguments.
    """
    result = 0
    for number in numbers:
        result += number
    return result

print(sum_numbers(1, 2, 3, 4, 5))
print(sum_numbers(10, 20, 30, 40, 50))