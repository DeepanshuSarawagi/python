# Day 8 - Exercise 2 - Prime Number Checker

number = int(input("Please enter a number of your choice: "))


def prime_checker(number):
    if number == 2 or number == 1:
        print("{} is a prime number.".format(number))
    else:
        for i in range(2, number):
            count = 0
            if number % i == 0:
                count += 1
                if count > 0:
                    print("{} is not a prime number.".format(number))
                    break
            else:
                print("{} is a prime number.".format(number))
                break


prime_checker(number=number)
