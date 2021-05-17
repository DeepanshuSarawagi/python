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
