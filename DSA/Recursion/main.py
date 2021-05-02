def recursive_method(n):
    if n == 1:
        print("Recursion completed, I`m the first method.")
    else:
        print("I`m the method no. {} in the recursion".format(n))
        recursive_method(n - 1)


recursive_method(5)

"""
Below beautiful example shows how recursion works. Lets say that we have four methods defined. First method calls
the second method, second method calls the third and so on.. When the first method calls the second method, the first
method execution is stopped and saved in the stack memory. Similarly for second and third. Until the execution of
 fourth method completes, all the other three mnethods will stay STACK memory. Once the execution is completed, 
 STACK memory will then execute third, second and first method. This type of execution is called FILO. 
 First in, Last Out."""


def first_method():
    second_method()
    print("I`m the first method.")


def second_method():
    third_method()
    print("I`m the second method.")


def third_method():
    fourth_method()
    print("I`m the third method.")


def fourth_method():
    print("I`m the fourth method.")


first_method()


def power_of_two(n):
    if n == 0:
        return 1
    else:
        # power = power_of_two(n-1)
        # print(power)
        return power_of_two(n-1) * 2


print(power_of_two(5))


def factorial(n):
    assert 0 <= n == int(n), "n must be a positive integer only."
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(6))


def fibonacci(n):
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(10)


# Challenge 1 how to find the sum of digits of a positive integer


def sum_of_digits(n):
    assert n > 0, "N should be a positive integer"
    if n < 10:
        return int(n)
    else:
        return int(n % 10) + sum_of_digits(n/10)


print(sum_of_digits(230))

# Exercise 2 - Hoe to calculate the power of number using recursion


def power_of_number(n, power):
    assert power > 0, "The parameters should be positive integers"
    if power == 1:
        return n
    else:
        return n * power_of_number(n, power - 1)


print(power_of_number(-2.2, 7))

# Exercise 3, greatest common divisor


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(48, 18))
