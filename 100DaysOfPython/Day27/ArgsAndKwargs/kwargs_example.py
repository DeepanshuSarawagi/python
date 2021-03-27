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
