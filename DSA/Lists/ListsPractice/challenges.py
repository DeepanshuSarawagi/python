my_list = [1, 2, 3, 4, 5]


def middle(list1):
    return list1[1:-1]


print(middle(my_list))


# Print the sum of all diagonal element:

myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def sumDiagonal(a):
    sum_of_diagonal = 0
    for i in range(0, len(a)):
        print(i)
        sum_of_diagonal += a[i][i]
    return sum_of_diagonal


print(sumDiagonal(myList2D))


# Return the first and second best scroes from the list
given_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]


def firstSecond(givenList):
    givenList.sort()
    first = givenList[-1]
    second = givenList[-2]
    for i in range(len(givenList) - 1):
        if givenList[i] > second:
            second = givenList[i]
    return first, second


print(firstSecond(given_list))
