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
