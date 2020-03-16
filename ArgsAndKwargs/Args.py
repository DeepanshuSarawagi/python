def average(*args):
    print(type(args))
    print(f"args is: {args}")  # this will print the arguments passed as tuple
    print(f"*args is: ", *args)  # this will print the unpacked tuple of arguments
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


"""In this program, args is the tuple of arguments and *args is the unpacked tuple. The function is saying python to 
expect the unpacked tuple of arguments since we are passing 4 different arguments in line 14 of the code. This is a
very powerful feature when we have to pass multiple arguments to a function in python."""

print(average(1, 2, 3, 4, 5, 6))


# def average_broken(first_arg, *args, second_arg):
#     print(type(args))
#     print(f"args is: {args}")  # this will print the arguments passed as tuple
#     print(f"*args is: ", *args)  # this will print the unpacked tuple of arguments
#     mean = 0
#     for arg in args:
#         mean += arg
#     return mean / len(args)
#
#
# print(average_broken(1, 2, 3, 4))

"""this program will crash from line 18 since as per the documentation we have the specify *args at the end of list of all 
the positional arguments. So it has to be def average(first_arg, second_arg, *args)"""

"""Udemy challenge"""


def build_tuple(*args):
    return "The tuple is: ", args


print(build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "master"))
