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
