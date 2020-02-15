a = 12
b = 4
print(a + b)
print(a.__add__(b))  # notice that both the code on line 3 and line 4 gives the same result since "+" operator on line 3
                     # calls the same builtin function __add__ as on line 4.
