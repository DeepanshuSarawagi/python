"""
In this lesson we are going to learn about unlimited keyword arguments and how it can be used in functions. The general
syntax is to define a function with just one parameter **kwargs.
We can then loop through the 'many' keyword arguments and perform necessary actions.

Syntax: def function(**kwargs):
            some operation
"""


def calculate(**kwargs):
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")


calculate(add=5, subtract=6, multiply=10, divide=2)


def calculate(n, **kwargs):

    n += kwargs["add"]
    print(n)
    n -= kwargs["subtract"]
    print(n)
    n *= kwargs["multiply"]
    print(n)
    n /= kwargs["divide"]
    print(n)


calculate(n=10, add=5, subtract=6, multiply=10, divide=2)


"""Similarly we can use **kwargs in the __init__ method while creating a class. Refer to below exmaple"""


class Car:

    def __init__(self, **kwargs):
        self.model = kwargs["model"]
        self.make = kwargs["make"]

    def print_car_details(self):
        print("You created a car. Your car make is {} and model is {}.".format(self.make, self.model))


my_car = Car(make="BMW", model="GT")
my_car.print_car_details()
