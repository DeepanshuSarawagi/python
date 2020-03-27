# We created two ways to calculate factorial 1) using the iterative approach and 2) using the recursive function
# use the timeit module to see which performs better and calculate the performance
import timeit
import statistics


def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n+1):
            result *= f
    return result


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


# if __name__ == "__main__":
#     print(f"It took {timeit.repeat('x=fact(200)', setup='from __main__ import fact', number=10000)} "
#           f"seconds to calculate factorial using iterative method")
#     print(f"It took {timeit.repeat('x=factorial(200)', setup='from __main__ import factorial', number=10000)} "
#           f"seconds to calculate factorial using recursive method")

# Commented above code to assing the list of repeat values to a variable
# and then calculate the mean and standard deviation

if __name__ == "__main__":
    list1 = timeit.repeat('x = fact(200)', setup='from __main__ import fact', number=1000)
    list2 = timeit.repeat('x = factorial(200)', setup='from __main__ import factorial', number=1000)

    print(f" The mean value of fact function is {statistics.mean(list1)} "
          f"and Standard Deviation is {statistics.stdev(list1)}")
    print(f" The mean value of factorial function is {statistics.mean(list2)} "
          f"and Standard Deviation is {statistics.stdev(list2)}")
