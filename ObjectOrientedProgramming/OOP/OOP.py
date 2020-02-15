a = 12
b = 4
print(a + b)
print(a.__add__(b))  # notice that both the code on line 3 and line 4 gives the same result since "+" operator on line 3


# calls the same builtin function __add__ as on line 4.

# create your first class and its objects.


class Kettle(object):
    power_source = "electricity"  # Creating an attribute for the class Kettle. All the instances of this class will

    # will share the same class attribute

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)

"""kenwood is the instance of the Kettle class and it shares the same characteristics defined in the Kettle class such
 as make, price and on."""
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
print(hamilton.make)
print(hamilton.price)
print(hamilton.on)

print(f"Models: {kenwood.make} = {kenwood.price}, {hamilton.make} = {hamilton.price}")

"""
Class: A template for creating objects. All objects created using the same class will share the same characteristics
Object: An instance of a class
Instantiate: Create an instance of a class
Method: A function defined in the class
Attribute: A variable bound to an instance of a class
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print("Is it on?")
print(kenwood.on)
print("Is Kenwood kettle on yet?")
kenwood.switch_on()  # this will not return any value since kenwood kettle is already on and its value is set to True

kenwood.power = 1.5
print(kenwood.power)  # this will execute because we created a data attribute for kenwood instance of kettle class

# print(hamilton.power)  # this will throw error since Kettle object has no attribute power

print(kenwood.power_source)
print(hamilton.power_source)
