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


def missingNumber(myList, totalCount):
    sum1 = totalCount * (totalCount + 1) / 2
    sum2 = sum(myList)
    return sum1 - sum2


print(missingNumber([1, 2, 3, 5, 6], 6))


my_list = [1, 1, 2, 2, 3, 4, 5]


def removeDuplicates(myList):
    new_list = []
    for i in range(len(myList)):
        if myList[i] in new_list:
            continue
        else:
            new_list.append(myList[i])
    return new_list


print(removeDuplicates(my_list))


my_list = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]


def pairSum(myList, sum):
    pair_sum = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] == myList[j]:
                continue
            elif myList[i] + myList[j] == sum:
                new_pair = str(myList[i]) + "+" + str(myList[j])
                pair_sum.append(new_pair)
    return pair_sum


print(pairSum(my_list, 7))
