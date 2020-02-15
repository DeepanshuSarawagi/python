a = 12
b = 4
print(a + b)
print(a.__add__(b))  # notice that both the code on line 3 and line 4 gives the same result since "+" operator on line 3
                     # calls the same builtin function __add__ as on line 4.

# create your first class and its objects.


class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


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
