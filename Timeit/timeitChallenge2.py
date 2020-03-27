# We created two ways to calculate factorial 1) using the iterative approach and 2) using the recursive function
# use the timeit module to see which performs better and calculate the performance
import timeit


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


if __name__ == "__main__":
    print(f"It took {timeit.timeit('x=fact(200)', setup='from __main__ import fact', number=10000)} "
          f"seconds to calculate factorial using iterative method")
    print(f"It took {timeit.timeit('x=factorial(200)', setup='from __main__ import factorial', number=10000)} "
          f"seconds to calculate factorial using recursive method")
