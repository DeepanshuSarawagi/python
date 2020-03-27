# We created two ways to calculate factorial 1) using the iterative approach and 2) using the recursive function
# use the timeit module to see which performs better and calculate the performance
import timeit


fact_test = """\
def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n+1):
            result *= f
    return result
x = fact(130)
"""

factorial_test = """\
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
y = factorial(130)
"""

result_1 = timeit.timeit(fact_test, number=10000)
result_2 = timeit.timeit(factorial_test, number=10000)

print(f"It took {result_1} seconds to calculate factorial using iterative method")
print(f"It took {result_2} seconds to calculate factorial using recursive method")
