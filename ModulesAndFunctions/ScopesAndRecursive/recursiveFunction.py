def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n+1):
            result *= f
    return result


for i in range(50):
    print(i, fact(i))

print("=" * 50)

"""Use recursive method to create a function to calculate n!"""


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)  # calling the function recursively


for i in range(50):
    print(i, factorial(i))
