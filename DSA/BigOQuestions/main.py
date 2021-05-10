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


# Calculate the time complexity of below example


def print_pairs(array):
    for i in array:
        for j in array:
            print(str(i) + ", " + str(j))


# If we observe the above function carefully, the inner for loop takes the O(n) complexity however, since it is nested
# and we are iterating the same array and printing the pairs, in the nested for loop, the outer for loop will have time
# complexity of O(n^2) complexity.

print_pairs([1, 2, 3, 4, 5])
print()


def print_unordered_pairs(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            print("{}, {}".format(array[i], array[j]))


# In the above case, we can see that outer for loop runs O(n) times and inner loop will run o(n/2) times,
# hence, n^2 / 2 times which can be simplified to time complexity of O(n^2) time complexity


print_unordered_pairs([1, 2, 3, 4, 5])
print()


def print_pairs(array1, array2):
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] < array2[j]:
                print("{}, {}".format(array1[i], array2[j]))


# Here, we need to understand the length of an array. If both the arrays have same length then it will have a quadratic
# time complexity because for every n elements in array1, every element in array2 will loop n times.
# If the lengths of both the arrays are different, then for every n elements in array1, every element in array2 will
# only loop m times where m is the length of array2. hence, we can say that it will have a time complexity of O(n*m)

print_pairs([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
print()


def print_10_pairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0, 10):
                print("{}, {}".format(arrayA[i], arrayB[j]))


# Here, we know that from the previous example, we know that the two outer for loops have a time complexity of O(n*m)
# time complexity. How about the third for loop? We have to understand that that we are looping through the constant
# time range of 1000 times, hence, it will have a time complexity of O(1). Hence even this function has a time
# complexity of O(n*m)

print_10_pairs([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
