def sum_eo(n,t):
    """
    Given an integer n and a string t ("even" or "odd"), return the sum of all even or odd integers from 1 to n (exclusive) based on the value of t.

    :param n: An integer representing the upper limit of the range (1 to n).
    :param t: A string that can be either "even" or "odd".
    :return: The sum of all even integers if t is "even", or the sum of all odd integers if t is "odd".
    """
    if t == "e":
        return sum(i for i in range(1, n) if i % 2 == 0)
    elif t == "o":
        return sum(i for i in range(1, n) if i % 2 != 0)
    else:
        return -1  # Invalid input for t

print(sum_eo(200,"spam"))
