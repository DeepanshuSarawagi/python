import numpy

# Write the function to find the missing number from the list

list1 = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def find_missing(list, n):
    sum1 = n * (n+1) / 2
    sum2 = sum(list)
    return sum1 - sum2


print(find_missing(list1, 20))


def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)


findPairs([1, 6, 3, 4, 5, 8, 11], 9)

my_array = numpy.array([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21])


def find_element(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return "Value found in the given array at index {}".format(i)
    return "Value not found in the given array"


print(find_element(my_array, 18))


def max_product(array):
    array.sort()
    max = array[-1] * array[-2]
    print(max)


max_product(my_array)

list = [1, 2, 5, 55, 76, 23, 45, 55, 10]


def determine_unique(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                return "The given list is not unique"
    return "The given list is unique"


print(determine_unique(list))


def permutation(list1, list2):
    if len(list2) != len(list1):
        return False
    list1.sort()
    list2.sort()
    return list1 == list2


print(permutation([1, 1, 3, 4], [4, 1, 3, 1]))

TwoDArray = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(TwoDArray)


def rotate_matrix(array):
    n = len(array)
    for layer in range(n // 2):
        pass  # Come back again