def fun(array):
    sum = 0                                             # This has a time complexity of O(1)
    product = 1                                         # This has a time complexity of O(1)

    for i in array:                                     # This has a time complexity of O(n)
        sum += i                                        # This has a time complexity of O(1)

    for i in array:                                     # This has a time complexity of O(n)
        product *= i                                    # This has a time complexity of O(1)

    print("Sum: {}, Product: {}".format(sum, product))  # This has a time complexity of O(1)


# If we combine all the steps equation can be simplified to 5 + 2(O(n)).
# If we remove the constants from the equation, it can be further simplified to O(n) time complexity

fun([1, 2, 3, 4, 5])
