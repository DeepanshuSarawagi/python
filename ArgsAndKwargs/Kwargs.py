def print_backwards(*args, **kwargs):

    """Just similar to *args which unpacks the tuple of arguments passed as parameter in functions, **kwargs will
    unpack the dictionary of named keywords which is passed. In the below program, we will define a simple function
    without specifying the named parameter file= yet pass it as an argument while calling the method"""
    print(kwargs.keys())
    print(kwargs)
    kwargs.pop('end', None)
    print(kwargs)
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)


with open('backwards.txt', 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
