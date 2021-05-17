# Write the function to find the missing number from the list

list1 = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def find_missing(list, n):
    sum1 = n * (n+1) / 2
    sum2 = sum(list)
    return sum1 - sum2


print(find_missing(list1, 20))
